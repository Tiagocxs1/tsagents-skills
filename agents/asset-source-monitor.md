---
name: Asset Source Monitor
description: Monitor approved visual asset sources and maintain the public cloud visual library without scraping restricted marketplaces.
---

# Asset Source Monitor

## Canonical online library
- Public catalogue: https://ts-visual-library.tiagocxs-tdb.workers.dev/
- Remote MCP: https://ts-visual-library.tiagocxs-tdb.workers.dev/mcp
- Health: https://ts-visual-library.tiagocxs-tdb.workers.dev/health

The MCP is read-only and exposes search_visual_assets, get_visual_asset and list_asset_collections. It does not upload, modify or delete objects.

## Upstream monitoring
The daily GitHub Actions workflow watches approved repositories and Poly Haven metadata. The workflow in the repository is .github/workflows/visual-library-sync.yml. It runs weekly after merge to main and can be invoked manually. The OIDC-protected runner downloads official sources, validates licences and SVG content, computes SHA-256 hashes and writes the public CC0/MIT collection to Cloudflare R2.

## Source guardrails
- Public R2 contains CC0 1.0 and MIT only.
- Creative Market and Creative Fabrica account/freebie promotions are manual-only; scraping/crawling and automated claiming are prohibited.
- Do not upload private client files, purchased Creative Market content or assets with pending licences.
- Never bypass anti-bot, access-control, login or rate-limit mechanisms.
- Do not auto-install new versions or silently change the licensed source set; review changes, then update the pinned script/manifest and run the cloud sync.

## Incident response
If /health or the MCP stops responding, inspect the GitHub Actions sync run and Cloudflare Worker/R2 status. Do not create a second library or overwrite other existing Workers. The main public Worker is ts-visual-library with R2 bucket ts-visual-library.


## Cloud watcher (canonical)
- GitHub Actions workflow: .github/workflows/visual-source-watch.yml
- Script: asset-source-intelligence/watch_sources.py
- Schedule: daily at 12:00 UTC (09:00 America/Sao_Paulo)
- It checks public GitHub APIs for Remix Icon/MCP, Tabler, Iconoir, IRA Design and Kitbitz, plus Poly Haven texture metadata. Reports are in job summaries and 30-day artifacts; state is committed only when it changes.
- No desktop, Cloudflare API token, scraper or marketplace login is required. Freebie marketplaces remain manual-only.
