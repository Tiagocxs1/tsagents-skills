"""Minimal Cloudflare Workers shim for FastMCP's optional reload watcher.

FastMCP imports Change and awatch from this package in its CLI module.
Cloudflare Workers has no local filesystem to watch, and the production MCP
runtime never enables FastMCP's CLI reload mode. Keep the import surface
available, but make the watcher inert rather than pretending to watch files.
"""

from __future__ import annotations

import asyncio
from enum import Enum


__version__ = "1.0.0"


class Change(Enum):
    added = 1
    modified = 2
    deleted = 3


async def awatch(*_paths, **_kwargs):
    """Never emit file changes; hot reload is unsupported in Workers."""
    await asyncio.Event().wait()
    if False:  # Make this an async generator for API compatibility.
        yield set()
