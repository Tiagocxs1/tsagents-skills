"""Remote MCP Brasil server on Cloudflare Python Workers.

The API token is a Cloudflare Worker secret. Authentication is forced to
static Bearer-token mode before importing mcp_brasil.server, because that
upstream package reads its settings at import time.

The Durable Object keeps one FastMCP instance/session manager stable for
Streamable HTTP requests. Local datasets remain disabled by default.
"""

from workers import DurableObject, Response, asgi


SERVICE_OBJECT_NAME = "mcp-brasil"


def build_asgi_app(env):
    """Configure the upstream package and build its Streamable HTTP ASGI app."""
    import os

    token = getattr(env, "MCP_BRASIL_API_TOKEN", None)
    if not token or len(str(token)) < 32:
        raise RuntimeError(
            "MCP_BRASIL_API_TOKEN is missing or too short; configure it as a "
            "Cloudflare Worker secret (minimum 32 characters)."
        )

    # Fail closed: do not permit an unauthenticated public MCP endpoint.
    os.environ["MCP_BRASIL_AUTH_MODE"] = "static"
    os.environ["MCP_BRASIL_API_TOKEN"] = str(token)
    os.environ["MCP_BRASIL_TOOL_SEARCH"] = "bm25"
    os.environ["MCP_BRASIL_DATASETS"] = ""
    os.environ["MCP_BRASIL_HTTP_TIMEOUT"] = "20.0"
    os.environ["MCP_BRASIL_HTTP_MAX_RETRIES"] = "2"

    # Import after setting the environment: mcp-brasil loads settings and
    # creates its auth provider during module initialization.
    from mcp_brasil.server import mcp

    # FastMCP's HTTP ASGI app uses Streamable HTTP (the remote MCP transport).
    return mcp.http_app()


class MCPBrasilServer(DurableObject):
    """Durable session host for the Streamable HTTP MCP application."""

    def __init__(self, ctx, env):
        self.ctx = ctx
        self.env = env
        self.app = build_asgi_app(env)

    async def on_fetch(self, request, env, ctx):
        return await asgi.fetch(self.app, request, self.env, self.ctx)


async def on_fetch(request, env):
    """Public Worker entry point with an edge health check and DO-backed MCP."""
    path = str(request.url).split("?", 1)[0].rstrip("/")

    # Liveness only: confirms the Worker edge responds without initializing the
    # Python MCP application. The authenticated MCP handshake is the readiness
    # check and exercises the Durable Object/session host.
    if path.endswith("/health"):
        return Response("ok", status=200)

    token = getattr(env, "MCP_BRASIL_API_TOKEN", None)
    if not token:
        return Response("MCP server is not configured", status=503)

    object_id = env.ns.idFromName(SERVICE_OBJECT_NAME)
    durable_object = env.ns.get(object_id)
    return await durable_object.fetch(request)
