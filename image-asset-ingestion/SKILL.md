---
name: image-asset-ingestion
description: Ingest, cache, reference, recover and expire third-party raster images for visual work using the TS Digitais Cloudflare image library. Use before creating visual pieces that need external photographs or downloaded image assets.
---

# TS Digitais — Image Asset Ingestion

## Purpose
Use the shared TS Digitais image library instead of relying on the chat's file-download or attachment path. This avoids losing time when a source image can be viewed but the assistant runtime cannot save it locally.

## Default infrastructure
- Remote MCP endpoint: `https://ts-image-library.tiagocxs-tdb.workers.dev/mcp`
- HTTP API base: `https://ts-image-library.tiagocxs-tdb.workers.dev`
- R2 bucket: `ts-image-assets-temp` (private; served through the Worker)
- Metadata catalog: D1 `ts-image-assets-index`
- Retention: image objects expire after 7 days; Cloudflare's lifecycle processor typically deletes objects within 24 hours after the expiry time.
- Only lightweight provenance metadata is retained after expiry: sanitized source URL, source page, project, filename, MIME type, size, date, stated license and attribution. No image binary is retained in the catalog.

## Workflow
1. Locate the image's original/public source. Prefer primary sources, official archives, press/media pages or licensed image providers.
2. Inspect actual licensing/permissions separately. A successful download does not grant publication rights. Use `unknown` when license cannot be verified; never label an image commercially cleared without evidence.
3. Call `import_image` with:
   - `url`: direct public image URL
   - `project`: short project/brand identifier (e.g. guardian, edusc, tsdigitais)
   - `source_page_url`: editorial/source page, when available
   - `license`: verified license or `unknown`
   - `attribution`: exact credit when required/known
4. For up to five sources, use `import_images_batch`.
5. Use returned `file_url` in HTML/SVG/CSS/preview workflows while active. Keep the returned asset ID in the project notes if it may need recovery.
6. After expiry, use `search_assets` or `get_asset` to find the old source record, then call `recover_asset`. Recovery re-downloads the original source and creates a new asset ID with a fresh seven-day expiry.
7. Delete early with `delete_asset` when the image is no longer needed or the user asks.

## Tools
- `import_image`
- `import_images_batch`
- `search_assets`
- `get_asset`
- `recover_asset`
- `delete_asset`

Use `Authorization: Bearer <ASSET_API_TOKEN>` for MCP and API calls. Never commit or log the token. Store it in the MCP client's secret/environment configuration.

## Limits and security
- Only public HTTP/HTTPS sources; redirects are revalidated.
- Maximum 15 MB per image; up to five images per batch.
- Accepted raster formats: JPEG, PNG, WebP, GIF and AVIF. SVG/HTML and other file types are rejected for safety.
- URLs with credentials, local/private literal IPs, reserved hosts and non-standard ports are rejected.
- The stored source URL has its query string removed to avoid retaining signed tokens. If the original image URL required a signed query string, later recovery may require the user to provide a fresh URL.
- Do not bypass login walls, paywalls, bot checks, hotlink restrictions or access controls.
- The file URL is a temporary public bearer-style asset link. Share it only where the image itself is intended to be public. It becomes unavailable after expiry.
- Cloudflare R2 lifecycle deletion usually happens within 24 hours after the configured age threshold, so practical removal is approximately 7–8 days from upload, not an exact-to-the-minute guarantee.
- R2 objects are not copied to Cloudinary by default; avoid duplicate permanent storage. Use Cloudinary only as an explicitly chosen transformation stage, and then apply an equivalent deletion policy there.
- The catalog is not a permanent archive of the image; it preserves only enough source metadata to attempt a later re-download. Recovery is not guaranteed if the origin removes or restricts the image.

## Fallback
If the MCP endpoint is not connected in a particular runtime, do not pretend the image has been stored. Use the HTTP API with the secret only in an authenticated server-side client, or provide the user with the source links and explain the integration blocker. Never place the API token in a public URL, HTML, SVG, GitHub, prompt, log or browser bundle.
