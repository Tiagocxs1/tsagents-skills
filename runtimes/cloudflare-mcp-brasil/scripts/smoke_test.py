"""Read-only MCP handshake/tool-list smoke test for local or remote endpoint."""

import asyncio
import os
import sys

from mcp import ClientSession
import httpx2
from mcp.client.streamable_http import streamable_http_client


async def main() -> int:
    url = os.environ.get("MCP_URL", "").strip()
    token = os.environ.get("MCP_BRASIL_API_TOKEN", "").strip()

    if not url:
        print("MCP_URL is required", file=sys.stderr)
        return 2
    if not token:
        print("MCP_BRASIL_API_TOKEN is required", file=sys.stderr)
        return 2

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx2.AsyncClient(headers=headers, timeout=30.0) as http_client:
        async with streamable_http_client(url, http_client=http_client) as (
            read_stream,
            write_stream,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.list_tools()
                names = sorted(tool.name for tool in result.tools)

                if not names:
                    raise RuntimeError("The MCP server returned no tools")
                if "listar_features" not in names:
                    raise RuntimeError(
                        "The MCP Brasil meta-tool 'listar_features' was not exposed"
                    )

                print("MCP handshake: OK")
                print(f"Tools visible to client: {len(names)}")
                print("Required discovery tool: listar_features")
                return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
