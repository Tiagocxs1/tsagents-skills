# TS Image Library — Cloudflare Worker

Temporary, reusable image ingestion service for TS Digitais visual-production agents.

## Deployed resources
- Worker: `ts-image-library`
- Worker URL: https://ts-image-library.tiagocxs-tdb.workers.dev
- MCP: https://ts-image-library.tiagocxs-tdb.workers.dev/mcp
- R2 bucket: `ts-image-assets-temp`
- D1: `ts-image-assets-index`

## Retention
- R2 prefix `images/` has a lifecycle deletion rule at 604800 seconds (7 days).
- Cloudflare says objects are typically deleted within 24 hours after the `x-amz-expiration` timestamp. This gives an operational window of roughly 7–8 days.
- D1 retains only minimal provenance metadata after object deletion so a public source can be re-downloaded later. It does not retain image bytes.
- Source query strings are removed before they are recorded to avoid persisting signed tokens. That may make some expiring/signed URLs non-recoverable.
- Incomplete multipart uploads are aborted after one day.

## Tools exposed via MCP
- `import_image`
- `import_images_batch` (up to 5)
- `search_assets`
- `get_asset`
- `recover_asset`
- `delete_asset`

## HTTP API
All API endpoints require `Authorization: Bearer <ASSET_API_TOKEN>`.
- `GET /healthz` — public health check
- `POST /api/import` — body: `{ "url": "...", "project": "guardian", "source_page_url": "...", "license": "unknown", "attribution": "..." }`
- `POST /api/import-batch` — body: `{ "items": [...] }`
- `GET /api/assets?project=guardian&status=active&limit=20`
- `GET /api/assets/:id`
- `POST /api/recover/:id`
- `DELETE /api/assets/:id`
- `GET|HEAD /file/:id` — temporary public image URL

## Supported source images
JPEG, PNG, WebP, GIF and AVIF, maximum 15 MB each. Up to five images per batch. SVG, HTML, local/private IPs, URL credentials, reserved hosts and non-standard ports are rejected. Redirect targets are revalidated. Do not bypass login, paywall, hotlink, robots or bot controls.

## Configure a compatible MCP client
Use Streamable HTTP at the MCP URL with Bearer token authentication. Store the token in the client secret store/environment, not source control. Example Codex-style configuration:

```toml
[mcp_servers.ts_image_library]
url = "https://ts-image-library.tiagocxs-tdb.workers.dev/mcp"
bearer_token_env_var = "TS_IMAGE_LIBRARY_TOKEN"
default_tools_approval_mode = "prompt"
```

Set `TS_IMAGE_LIBRARY_TOKEN` in the local secret environment of the MCP client.

ChatGPT custom MCP server availability depends on plan/workspace. As of 20 Nov 2026, OpenAI Help lists custom MCP connections for Business and Enterprise/Edu; this user's current Free plan cannot connect a custom MCP server through ChatGPT Settings. Compatible external MCP clients can still use the endpoint.

## Deploy/maintain
The deployed version uses a single ES module `worker.js`, R2 binding `ASSETS`, D1 binding `DB`, and secret `ASSET_API_TOKEN`. The deployed bindings and lifecycle policy are also documented in `deployment.json`.
