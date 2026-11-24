# TS Digitais — Online Visual Asset Library

The public visual library runs on Cloudflare Workers + R2. Agents can access it from anywhere; the user's desktop is not required for search, download, or MCP access.

## Public endpoints
- UI: https://ts-visual-library.tiagocxs-tdb.workers.dev/
- Health: https://ts-visual-library.tiagocxs-tdb.workers.dev/health
- Search: GET /api/search?q=people&limit=20
- Collections: GET /api/collections
- MCP: POST /mcp (read-only)
- Master/preview: GET /file?key=assets/v1/...

## Remote MCP tools
- search_visual_assets — search by query, collection, style, license and file type.
- get_visual_asset — fetch public asset metadata and URL by asset ID.
- list_asset_collections — list collection counts/licenses.

The MCP is intentionally read-only. It does not upload, overwrite, delete or publish designs.

## Public licence allowlist
The initial online library contains only assets with explicit CC0 1.0 or MIT licences:
- Kitbitz CC0 assets (pinned repository commit).
- Six selected AssetPolish CC0 collections.
- IRA Design / Creative Tim MIT vectors.
- Open Doodles CC0 vectors.
- Selected 19 Open Peeps CC0 SVGs.
- Nine Poly Haven CC0 surface textures.

Private Creative Market purchases, font files, archives and licence-pending content are excluded. The library never claims that a generic illustration depicts a real Guardian installation, customer, employee or Intelbras product.

## Cloud sync
sync_public_library.py runs in GitHub Actions and downloads sources from their official endpoints, validates licences/paths/SVGs and hashes, and uploads files directly to the persistent Cloudflare R2 bucket ts-visual-library.

Uploads are authorized only by a short-lived GitHub Actions OIDC token. The Worker validates issuer, audience, repository/repository ID, owner/owner ID, ref and exact workflow identity. There is no static Cloudflare API token in this repository. Only the authorized sync workflow can write; agents and the browser cannot write to the bucket.

The first run is triggered by a push to the deployment feature branch. After successful validation and merge to main, a weekly scheduled run keeps the library refreshed. Asset changes, counts and source hashes are recorded in sync-report.json and GitHub Actions artifacts.

## Online rendering / authoring
The library is one piece of the workflow, not a visual editor. vector-studio is a separate GitHub Actions pipeline for remote SVG/PNG rendering. The existing pipeline currently places generated campaign deliverables in a temporary bucket with a seven-day lifecycle; this is not the permanent library bucket. Do not assume rendered campaign deliverables are permanent until that pipeline is hardened separately.

## Rights and privacy
- No Creative Market or Creative Fabrica scraping.
- No login-cookie reuse, CAPTCHA/Cloudflare bypass, or automated freebie claiming.
- No private client/customer data or purchased private assets in the public bucket.
- CC0/MIT copyright permissions do not grant trademark, privacy, publicity, model/property, patent or endorsement rights.
