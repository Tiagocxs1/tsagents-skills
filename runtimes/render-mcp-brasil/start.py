"""Start the pinned MCP Brasil server as a normal HTTP process on Render.

Fail closed before importing upstream modules: the static bearer token is
required, and free-tier data/runtime settings are constrained.
"""

import os


def configure_runtime() -> int:
    token = os.environ.get("MCP_BRASIL_API_TOKEN", "").strip()
    if len(token) < 32:
        raise RuntimeError(
            "MCP_BRASIL_API_TOKEN is required and must contain at least 32 characters."
        )

    # Apply security and resource settings before importing upstream modules,
    # because the upstream module constructs its auth provider at import time.
    os.environ["MCP_BRASIL_AUTH_MODE"] = "static"
    os.environ["MCP_BRASIL_API_TOKEN"] = token
    os.environ["MCP_BRASIL_TOOL_SEARCH"] = "bm25"
    os.environ["MCP_BRASIL_DATASETS"] = ""
    os.environ["MCP_BRASIL_HTTP_TIMEOUT"] = "20.0"
    os.environ["MCP_BRASIL_HTTP_MAX_RETRIES"] = "2"
    return int(os.environ.get("PORT", "10000"))


if __name__ == "__main__":
    port = configure_runtime()

    # Import only after the static token and constrained runtime settings exist.
    from mcp_brasil.server import mcp

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp/",
        show_banner=False,
    )
