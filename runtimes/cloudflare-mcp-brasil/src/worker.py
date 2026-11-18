"""Stateless MCP Brasil endpoint on Cloudflare Python Workers.

Cloudflare Python Workers export a Default(WorkerEntrypoint) class. The
original MCP Brasil package is imported only after the Worker secret has been
copied into the environment, because upstream reads auth settings at import.

FastMCP runs with stateless Streamable HTTP so the endpoint does not depend on
a long-lived process or Durable Object session between requests.
"""

from __future__ import annotations

import os
from urllib.parse import urlparse

from workers import WorkerEntrypoint, Response, asgi


_cached_app = None


def build_asgi_app(env):
    """Configure the upstream package and build a stateless ASGI application."""
    token = getattr(env, "MCP_BRASIL_API_TOKEN", None)
    if not token or len(str(token)) < 32:
        raise RuntimeError(
            "MCP_BRASIL_API_TOKEN is missing or too short; configure it as a "
            "Cloudflare Worker secret (minimum 32 characters)."
        )

    # Fail closed: never permit an unauthenticated public MCP endpoint.
    os.environ["MCP_BRASIL_AUTH_MODE"] = "static"
    os.environ["MCP_BRASIL_API_TOKEN"] = str(token)
    os.environ["MCP_BRASIL_TOOL_SEARCH"] = "bm25"
    os.environ["MCP_BRASIL_DATASETS"] = ""
    os.environ["MCP_BRASIL_HTTP_TIMEOUT"] = "20.0"
    os.environ["MCP_BRASIL_HTTP_MAX_RETRIES"] = "2"

    # Import after setting the environment: upstream creates its auth provider
    # during module initialization.
    from mcp_brasil.server import mcp

    return mcp.http_app(path="/mcp/", stateless_http=True, json_response=True)


class Default(WorkerEntrypoint):
    """Cloudflare Python Worker entrypoint."""

    async def fetch(self, request):
        global _cached_app

        path = urlparse(request.url).path.rstrip("/")

        # Liveness check only; does not import the upstream package.
        if path == "/health":
            return Response("ok", status=200)

        if path not in {"/mcp", "/mcp/"}:
            return Response("Not found", status=404)

        token = getattr(self.env, "MCP_BRASIL_API_TOKEN", None)
        if not token:
            return Response("MCP server is not configured", status=503)

        if _cached_app is None:
            _cached_app = build_asgi_app(self.env)

        # Cloudflare's ASGI adapter maps the Fetch Request to the ASGI app.
        # FastMCP stateless_http means each request can be handled independently.
        return await asgi.fetch(_cached_app, request, self.env, self.ctx)
