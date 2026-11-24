# Cloudflare Worker — TS Visual Library

Worker name: ts-visual-library
R2 binding: ASSETS -> bucket ts-visual-library
Runtime: Workers (ES modules)
Compatibility date: 2026-11-24
Public endpoint: https://ts-visual-library.tiagocxs-tdb.workers.dev/

## Routes
- GET / — public catalog UI stored as R2 object catalog/index.html.
- GET /health — catalog and service health.
- GET /api/collections — six public CC0/MIT collections and totals.
- GET /api/search — licence-aware keyword search against R2 catalog/index.json.
- GET /file?key=assets/v1/... — public master/preview retrieval; only the assets/v1 prefix is allowed.
- POST /mcp — read-only MCP Streamable HTTP, protocol 2025-03-26.
- PUT /upload?key=... — protected by GitHub Actions OIDC. Only the exact source repository, immutable IDs, exact workflow and explicitly allow-listed refs are accepted.

## Remote MCP tools
- search_visual_assets
- get_visual_asset
- list_asset_collections

No tool can upload, overwrite, delete, install, publish or schedule social content. Public clients do not receive R2 bucket credentials.

## Storage and rights
- Public bucket contains CC0 1.0 and MIT assets only.
- Private Creative Market packs, fonts and licence-pending content are excluded.
- Source URL, author, licence, size and SHA-256 are recorded in the catalog.
- Public assets are cached for 24h; HTML catalog for 5 minutes; index is held in a Worker isolate for 5 minutes.
- SVG response CSP restricts external execution/content.
- This bucket has no seven-day lifecycle rule. It is the permanent public asset library; it is separate from ts-image-assets-temp / vector-render output storage.

## Deploy
The Worker was initially deployed through the connected Cloudflare account tool. To reproduce:
1. Create/confirm R2 bucket ts-visual-library.
2. Bind it as ASSETS.
3. Upload worker.js as ES module with compatibility date 2026-11-24.
4. Enable workers.dev subdomain.
5. Bootstrap the initial R2 objects from the authorized GitHub Actions workflow.
6. Validate /health, /api/search, MCP tools/list and an asset HEAD URL.

Never deploy this file into ts-svg-assets or any existing client Worker. This Worker name and bucket are dedicated to the public CC0/MIT library.
