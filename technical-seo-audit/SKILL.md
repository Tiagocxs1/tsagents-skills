---
name: technical-seo-audit
description: Run repeatable technical SEO and web-performance audits using Google Lighthouse and select the right crawler or monitoring system based on available free infrastructure.
---

# Technical SEO Audit — TS Digitais

## Primary automated runner: Google Lighthouse

- Upstream: https://github.com/GoogleChrome/lighthouse
- License: Apache-2.0
- Version pinned by the shared workflow: 13.6.0
- Runs as a temporary GitHub Actions job; no VPS, database, API key or persistent server is needed.
- Produces HTML and JSON reports for Performance, Accessibility, Best Practices and SEO.
- Mobile is the default preset; desktop can be selected per project.
- Reports are stored in the caller repository's dedicated seo-reports branch and as a 30-day Actions artifact. Never commit reports to main where pushes may deploy a production site.

## Collecting a Lighthouse audit

Shared files:

- .github/workflows/lighthouse-collect.yml: reusable workflow.
- technical-seo-audit/scripts/run_lighthouse.py: validated config + bounded runner.
- technical-seo-audit/templates/caller-lighthouse.yml: caller workflow example.
- technical-seo-audit/templates/config-lighthouse.json: example configuration.

Run manually or monthly from a private project repository. Keep the configuration private if it contains unpublished URLs or staging hostnames. Use public HTTPS URLs only. Maximum five URLs per run to control execution time and avoid unnecessary requests.

The collector runs one Lighthouse navigation for each URL. It does not authenticate to websites, crawl private pages, bypass robots directives, rotate proxies or attempt to evade rate limits.

## Interpretation

- Lighthouse lab scores are controlled test results from a particular run, not a guarantee of real-user performance.
- Use Search Console / CrUX field data when available to assess real-user Core Web Vitals.
- Score changes must be compared on the same device preset, URL, environment and Lighthouse version.
- A 0–100 score is not a Google ranking position and must not be described as a direct ranking factor or traffic forecast.
- Keep Performance, Accessibility, Best Practices and SEO scores separate.
- Treat Lighthouse SEO as a technical checklist, not a complete content-quality or off-page SEO assessment.

## Other audited tools and current fit

| Project | Decision | Reason |
|---|---|---|
| OpenSEO | Candidate, not deployed | Cloudflare self-host is documented, but current upstream requires a DataForSEO or Treg credential for SEO data. Deployment provisions additional Workers, D1, KV, R2 and two Cron schedules; account capacity and the missing external data credential must be resolved first. |
| CrawlSEO | Not installed as a service | Requires a persistent Next.js app, PostgreSQL, background worker and Google OAuth. GitHub Actions is ephemeral and Cloudflare Workers is not a drop-in runtime for its app/worker/DB. |
| SerpBear | Not installed as a service | Requires persistent app storage and a reliable SERP data source. Its README's historical free ScrapingRobot entry is marked as no longer working; do not silently replace it with paid scraping or proxy evasion. |
| SEOnaut | Not installed as a service | Web application with MySQL database; no verified one-shot CI/CLI runner. Running it as containers in Actions would discard its history at job end. |
| Google Lighthouse | Installed as reusable CI tooling | Runs on a GitHub-hosted runner and exports reports without a persistent service. |

Do not call these uninstalled projects "deployed". A repo, skill, container image, or workflow template is not a running service.

## Complementary sources

- Google Search Console: actual clicks, impressions, queries and average position for owned properties.
- Google PageSpeed Insights / CrUX: field performance where eligible.
- Google Trends via google-trends-research/SKILL.md: relative demand signal only, not absolute monthly volume.
- Google Autocomplete: free query suggestions, not search-volume evidence.

## Cost and safety policy

- Prefer the shared GitHub Actions runner over a continuously running server.
- Private-repository GitHub Actions usage is subject to the account's included minutes and billing settings; it is not unlimited.
- Use a monthly schedule and manual dispatch. Do not run a site-wide Lighthouse audit on every commit unless explicitly required.
- Reports are saved on a dedicated report branch, never on a production deployment branch.
- Use only public HTTPS URLs; do not include passwords, session cookies, authorization headers or private preview tokens.
- Do not run audits against arbitrary internal endpoints, localhost, private IP literals or .local hostnames.
- Ask before enabling any service that requires a card, paid API, subscription or external account with a top-up.

## Completion rule

A workflow being committed is not proof that a live audit has succeeded. Confirm the GitHub Actions run, open the HTML/JSON artifact, and inspect its final URL, status, scores and metric data before reporting the result.
