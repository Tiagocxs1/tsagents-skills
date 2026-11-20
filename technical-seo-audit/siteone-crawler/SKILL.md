---
name: siteone-crawler-audit
description: Run bounded site-wide technical SEO audits with the SiteOne Rust crawler and review structured HTML/JSON findings.
---

# SiteOne Crawler — Technical SEO & Site QA

## Upstream
- Project: https://github.com/janreges/siteone-crawler
- License: MIT.
- Version pinned by the shared workflow: v2.5.1.
- Linux x64 musl release archive SHA-256: bd96b9502563aea2581fc248625871e69b60d7f1bb68a484f226c551c73706fd.

## Why this tool
SiteOne is a one-shot Rust CLI. It does not need a dashboard, database, persistent server, Google API key or DataForSEO account. It can crawl pages and assets, respecting robots.txt by default, and report broken links, 404s, redirects, metadata, headings, duplicate titles/descriptions, security headers, TLS, caching, response times, accessibility and best practices. It exports a self-contained HTML report and structured JSON.

## Shared runner
- Workflow: .github/workflows/siteone-crawler-audit.yml
- Python runner: technical-seo-audit/siteone-crawler/scripts/run_siteone.py
- Tests: technical-seo-audit/siteone-crawler/scripts/test_run_siteone.py
- Caller template: technical-seo-audit/templates/caller-siteone.yml
- Config template: technical-seo-audit/templates/config-siteone.json

Defaults are deliberately conservative: mobile user agent, 300 visited URLs (pages plus assets), depth 4, two workers, maximum two requests per second, 10-second request timeout. The runner caps configurable limits and never disables robots.txt.

Use monthly or manual execution, not on every push. Results are written to a dedicated reports branch in the calling private repository, never to its production branch.

## Interpreting results
SiteOne's quality score is an internal rubric from 0 to 10 across Performance, SEO, Security, Accessibility and Best Practices. It is not Google's ranking score. Crawler response times are not real-user Core Web Vitals.

Keep these separate from Lighthouse, which uses lab metrics and 0–100 category scores, and from Search Console, which supplies actual impressions/clicks/queries for owned properties.

## Tools not deployed
OpenSEO is not deployed: the upstream currently requires a DataForSEO or Treg key and provisions two Cron schedules, while the TS Digitais Cloudflare account has no spare Cron trigger capacity. CrawlSEO requires a persistent Next.js app, PostgreSQL and worker. SerpBear requires persistent storage and a reliable SERP data source. SEOnaut requires a persistent Go/MySQL app. These projects were audited but are not installed as running services.

## Safety and cost
- No paid SEO API, Google credential, cookie, proxy or third-party report host is used.
- Private GitHub repositories consume included Actions minutes; monitor the allowance.
- Only public HTTPS URLs are accepted.
- Use low concurrency and rate limits; stop on 403/429 or signs of service strain.
- Do not use stress/load-testing flags in SEO crawls.
- Competitor crawls must respect robots.txt and access restrictions.
