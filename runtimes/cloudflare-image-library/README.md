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
- After automatic R2 expiry, D1 retains only minimal provenance metadata so a public source can be re-downloaded later. Explicit `delete_asset` removes both the R2 object and the D1 record; deleted references are not kept as a soft-delete archive.
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

## Configure the authentication secret

The Worker requires a secret named `ASSET_API_TOKEN`. Rotate/set a value known to the owner before connecting any client:

1. Generate a strong token locally (64 hex characters): `openssl rand -hex 32`.
2. In Cloudflare Dashboard, open **Workers & Pages → ts-image-library → Settings → Variables and Secrets**.
3. Add or edit a **Secret** named `ASSET_API_TOKEN` and paste the generated value. Save/deploy the change.
4. Keep the value in a password manager and in the MCP client's local secret/environment store. Never put it in GitHub, HTML, SVG, logs or prompts.

Alternative: `npx wrangler secret put ASSET_API_TOKEN --name ts-image-library` and paste the generated token when Wrangler prompts.

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
