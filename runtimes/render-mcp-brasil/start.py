"""Start the pinned MCP Brasil server as a normal HTTP process on Render."""

import os

from mcp_brasil.server import mcp


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp/",
        show_banner=False,
    )
