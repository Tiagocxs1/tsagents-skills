---
name: asset-source-intelligence
description: Find, license-check and use visual assets online through the TS Digitais public library and authorized source APIs.
---

# Asset Source Intelligence

## Primary online visual library
Use this first when a task runs in the cloud or the desktop is unavailable.

- Web catalog: https://ts-visual-library.tiagocxs-tdb.workers.dev/
- Remote MCP: https://ts-visual-library.tiagocxs-tdb.workers.dev/mcp
- Health: https://ts-visual-library.tiagocxs-tdb.workers.dev/health
- Search API: GET /api/search?q=...&limit=...
- Collections API: GET /api/collections

The remote MCP is read-only and provides:
1. search_visual_assets — query by subject, object, style, collection, licence and format.
2. get_visual_asset — fetch metadata and URLs for a selected asset.
3. list_asset_collections — list available collections and licence details.

Example MCP calls:
- search_visual_assets({query:"person holding laptop", limit:20})
- search_visual_assets({query:"concrete wall texture", collection:"polyhaven", limit:10})
- list_asset_collections({})

Returned results include master/preview URLs, author, source, tags, SHA-256, licence, file format and commercial-use flag. Only CC0-1.0 and MIT assets are included in this public library. Private Creative Market assets and licence-pending files are excluded.

## Online-first workflow
1. Read the visual brief and select the art direction before choosing assets.
2. Search the remote MCP for the visual role required: hero subject, character, prop, scene, surface, background, detail or supporting icon.
3. Inspect the SVG/PNG/JPG master at its public file URL; do not substitute a generic geometric icon when a richer illustration or photograph is available.
4. Keep one coherent style family per piece. Do not mix 2.5D, sketch, gradient, outline, sticker and photography without a deliberate collage direction.
5. Record asset ID, source URL, author, licence, file URL and intended role in the project's asset manifest.
6. Verify third-party rights not covered by CC0/MIT: trademarks, privacy, publicity, property, model releases, endorsements, patents and product identity.
7. Render the finished SVG in the cloud and visually inspect desktop/mobile output before approval.

## Collections
- Kitbitz: CC0 1.0; 2.5D/isometric objects, props and scene components.
- AssetPolish selected packs: CC0 1.0; outline, soft duotone, sticker illustrations, security/privacy and campaign topics.
- IRA Design / Creative Tim: MIT; character poses, props, backgrounds and examples. Preserve the MIT copyright/permission notice when redistributing copies or substantial portions.
- Open Doodles: CC0 1.0; hand-drawn characters, sketches and compositions.
- Open Peeps (selected files): CC0 1.0; 19 selected modular hand-drawn people/poses; not the complete pack.
- Poly Haven: CC0 1.0; 2K diffuse/albedo surface maps, not transparent overlays or ready-made shadows.

## Guardian Seg
- Never label a generic illustration as an actual Guardian/Intelbras camera, alarm panel, sensor, customer, employee, control room or installation.
- Use verified Intelbras product photos for real equipment.
- Stock photographs and illustrations are contextual, not evidence of Guardian installations.
- Keep the official Guardian palette and do not introduce green.
- Do not use private/licence-pending assets in client campaigns.

## Local fallback
When the remote MCP is unavailable, the local catalog and CLI are:
 /home/tiago/Downloads/GuardianSeg_Asset_Library_2026/index.html
 python3 /home/tiago/Downloads/GuardianSeg_Asset_Library_2026/scripts/search_asset_library.py "person holding laptop" --commercial-only --limit 20

Local files are a fallback, not a requirement for cloud agents. The online Worker/R2 library is the canonical public source.

## Source updates and acquisition
- GitHub/Poly Haven watcher and source restrictions are documented in vector-studio/asset-library/README.md and the local source intelligence registry.
- Do not scrape Creative Market, Creative Fabrica, unDraw or ManyPixels. Claim account freebies manually where necessary and verify the individual product licence.
- Never bypass login, Cloudflare, CAPTCHA, rate limits or anti-bot protections.
- Do not assume that permission to use an individual asset permits automated scraping or building a mirrored library.


## Cloud source monitor (no desktop dependency)
The GitHub Actions workflow `.github/workflows/visual-source-watch.yml` checks the six approved repositories and Poly Haven public API daily at 09:00 São Paulo time (12:00 UTC). It writes a report to the Actions job summary and a 30-day artifact, and commits the source baseline only when a release/commit/catalog change is detected. It never scrapes or downloads marketplace freebies. The local systemd watcher is an optional duplicate; cloud monitoring continues when the user's PC is off.


## Gate obrigatório — contexto do cliente, território e protagonista em primeiro plano
Antes de selecionar imagens, consultar `client-contextual-visual-assets/SKILL.md`: estudar nicho, público, produtos/serviços, catálogo oficial e regiões atendidas; construir mapa de contexto visual; pesquisar assets locais com licença adequada; não usar fotografia estrangeira/genérica para representar campanha regional. Planejar protagonista real em foreground (produto autêntico, pessoa, objeto ou cena isolada em PNG/foto/3D) quando o conceito comportar. Definir background/midground/foreground e integrar perspectiva, escala, luz, foco, oclusão e sombras. Registrar proveniência e direitos. Reprovar wallpaper fotográfico + texto quando a narrativa exigir presença visual, produto falso, localidade errada ou asset sem permissão.
