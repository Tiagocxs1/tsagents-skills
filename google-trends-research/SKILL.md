---
name: google-trends-research
description: Research Google Trends interest, compare keywords, collect related queries and regional interest with Trendspyg. Use for demand signals, seasonal topic discovery, keyword comparisons and migration from archived Pytrends.
---

# Google Trends Research — TS Digitais

## Purpose and limits

Use the maintained **Trendspyg** project as the shared Google Trends connector for TS Digitais and client projects.

- Upstream: https://github.com/flack0x/trendspyg
- License: MIT
- Pinned version for the shared workflow: `trendspyg==1.9.0`
- The original `pytrends` repository is archived. For existing Pytrends scripts, prefer the compatibility module below instead of depending on the archived package.

**Google Trends does not provide absolute monthly search volume.** Its 0–100 index is relative to the selected query, geography and time range. It is not a count of searches, CPC, ad competition or a forecast. Keep these fields separate from Google Ads Keyword Planner values.

## When to use each data path

| Need | Function | Notes |
|---|---|---|
| Compare 2–5 terms | `download_google_trends_comparison` | One shared 0–100 scale; best for relative comparison |
| Full study of one term | `download_google_trends_explore` | Interest over time, related queries and regional interest |
| Interest history of one term | `download_google_trends_interest_over_time` | Time series only |
| Current trending topics | `download_google_trends_rss` | Fast RSS path; not a keyword-volume service |
| Existing Pytrends code | `trendspyg.compat.request.TrendReq` | Compatibility layer for common Pytrends 4.9.2 workflows |

Do not compare independent single-keyword 0–100 series as though they shared one scale. Use the comparison function for direct comparison.

## Rate-limit policy

Google Trends is an unofficially accessed web interface, not a guaranteed public keyword-data API. Google can throttle or change its response format.

- Default the automated workflow to **one Explore/comparison request per project per month**, with manual dispatch available for deliberate research.
- Use `engine="auto"` so Trendspyg tries its direct path and falls back to Chrome only when necessary.
- Keep `max_retries=1`; do not write outer retry loops for 403/429 or `RateLimitError`.
- On 403, 429, a blocked chart or parse errors: stop, retain the error in the job log, and wait before a later manually scheduled attempt. Never rotate proxies or attempt to bypass access controls.
- Use `cache="disk"` for repeated identical calls within a persistent local environment. GitHub-hosted runners are ephemeral, so their local cache and cookie jar do not automatically survive between jobs.
- Do not persist Google cookies in Git, workflow artifacts, public logs or a shared cache. The shared GitHub Actions workflow intentionally does not enable `cookies="disk"`.
- The RSS path is suitable for lightweight discovery but must not be polled aggressively.

## Standard installation

Basic library (no pandas required for JSON/dict results):

```bash
python -m pip install "trendspyg==1.9.0"
```

For a local MCP client that supports stdio, install the optional extra:

```bash
python -m pip install "trendspyg[mcp]==1.9.0"
```

The MCP server is a **local stdio process** launched as `trendspyg-mcp`; it is not a remote Cloudflare MCP service and is not automatically connected to ChatGPT. For Codex CLI, after installing the optional extra:

```bash
codex mcp add trendspyg -- trendspyg-mcp
```

## Pytrends migration

Change the import; preserve common call patterns:

```python
# Old: from pytrends.request import TrendReq
from trendspyg.compat.request import TrendReq

trends = TrendReq(hl="pt-BR", geo="BR", cache="disk", engine="auto")
trends.build_payload(["portaria remota"], timeframe="today 12-m", geo="BR")
series = trends.interest_over_time()
```

The compatibility layer aims at common Pytrends 4.9.2 workflows and DataFrame output requires `trendspyg[analysis]`. It is not a complete drop-in replacement: consult upstream `docs/MIGRATING_FROM_PYTRENDS.md` before migrating a project. In particular, proxies, multi-range and some older endpoint methods are unsupported or behave differently.

## Cross-project workflow

A monthly/manual GitHub Actions reusable workflow is provided at:

- `.github/workflows/google-trends-collect.yml` — central reusable workflow.
- `templates/caller-workflow.yml` — caller workflow template.
- `templates/config.example.json` — example configuration.

The caller repository stores its own private `.seo/google-trends.json` configuration. The collector writes reports to a dedicated `seo-reports` branch under `reports/seo/google-trends/` and also uploads a 30-day Actions artifact. It never commits report data to the caller's production branch. The central public repository stores only reusable tooling; do not put client domains, private keyword lists or access tokens in this public repository.

GitHub Actions usage from private caller repositories is subject to the owner's included minutes and billing settings. This is not unlimited compute. The template is intentionally monthly and short-running.

## Interpretation rules

1. Label every Trends score as a **relative interest index (0–100)**.
2. Include geography, timeframe, exact keyword spelling and fetch timestamp in every report.
3. Never translate a Trends index into estimated searches/month.
4. Do not call Trends interest "search demand volume" without qualification.
5. For local businesses, use Trends as a relative signal, not proof of demand in a specific city or neighborhood.
6. Combine with Search Console actual impressions/clicks and Google Ads Keyword Planner volume/CPC when those metrics are available.
7. Keep seasonality and related queries as editorial research signals, not proof of conversion intent.

## References

- Trendspyg source and API: https://github.com/flack0x/trendspyg
- Migration guide: https://github.com/flack0x/trendspyg/blob/main/docs/MIGRATING_FROM_PYTRENDS.md
- Google Trends: https://trends.google.com/
- Google Trends API alpha information: https://developers.google.com/search/apis/trends
