#!/usr/bin/env python3
"""Collect a bounded Google Trends snapshot for one project.

No absolute search volume or CPC is inferred. The report labels Google's 0-100
relative-interest index and preserves the exact geography and time range.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
GEO_RE = re.compile(r"^[A-Z]{2}$")
DATE_RANGE_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{4}-\d{2}-\d{2}$")
ALLOWED_TIMEFRAMES = {
    "today 3-m",
    "today 12-m",
    "today 5-y",
    "now 7-d",
    "now 1-H",
    "all",
}


class ConfigError(ValueError):
    """Raised when a project's Trends configuration is unsafe or invalid."""


def load_config(path: Path) -> dict[str, Any]:
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"Configuration file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON in {path}: {exc}") from exc

    if not isinstance(config, dict):
        raise ConfigError("The configuration root must be a JSON object.")

    slug = config.get("project_slug")
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        raise ConfigError("project_slug must use lowercase letters, numbers and single hyphens.")

    geo = config.get("geo", "BR")
    if not isinstance(geo, str) or not GEO_RE.fullmatch(geo):
        raise ConfigError("geo must be a two-letter uppercase country code, e.g. BR.")

    timeframe = config.get("timeframe", "today 12-m")
    if not isinstance(timeframe, str) or (
        timeframe not in ALLOWED_TIMEFRAMES and not DATE_RANGE_RE.fullmatch(timeframe)
    ):
        raise ConfigError(
            "Unsupported timeframe. Use one of: "
            + ", ".join(sorted(ALLOWED_TIMEFRAMES))
            + " or 'YYYY-MM-DD YYYY-MM-DD'."
        )

    keywords = config.get("keywords")
    if not isinstance(keywords, list) or not 1 <= len(keywords) <= 5:
        raise ConfigError("keywords must be a list containing 1 to 5 search terms.")

    cleaned: list[str] = []
    for term in keywords:
        if not isinstance(term, str) or not term.strip():
            raise ConfigError("Every keyword must be a non-empty string.")
        term = term.strip()
        if "," in term:
            raise ConfigError(f"Commas are not supported inside comparison terms: {term!r}")
        cleaned.append(term)

    if len({term.casefold() for term in cleaned}) != len(cleaned):
        raise ConfigError("keywords must not contain duplicates.")

    include_trending_now = config.get("include_trending_now", False)
    if not isinstance(include_trending_now, bool):
        raise ConfigError("include_trending_now must be true or false.")

    return {
        "project_slug": slug,
        "geo": geo,
        "timeframe": timeframe,
        "keywords": cleaned,
        "include_trending_now": include_trending_now,
    }


def collect(config: dict[str, Any]) -> dict[str, Any]:
    try:
        package_version = version("trendspyg")
    except PackageNotFoundError as exc:
        raise RuntimeError(
            'Trendspyg is not installed. Install with: pip install "trendspyg==1.9.0"'
        ) from exc

    if package_version != "1.9.0":
        raise RuntimeError(
            f"Expected trendspyg==1.9.0, found {package_version}. "
            "Update the pinned workflow and skill together."
        )

    from trendspyg import (
        download_google_trends_comparison,
        download_google_trends_explore,
    )

    started_at = datetime.now(timezone.utc).isoformat()
    keywords = config["keywords"]
    shared_options = {
        "geo": config["geo"],
        "timeframe": config["timeframe"],
        "cache": "disk",
        "engine": "auto",
        "max_retries": 1,
        "retry_wait": 8.0,
        "include_geo": True,
        "archive": False,
    }

    if len(keywords) == 1:
        trends_data = download_google_trends_explore(
            keywords[0],
            include_related=True,
            **shared_options,
        )
        mode = "single_keyword_explore"
        scale_note = (
            "0-100 relative interest index for this keyword, geography and timeframe; "
            "not monthly search volume."
        )
    else:
        trends_data = download_google_trends_comparison(
            keywords,
            **shared_options,
        )
        mode = "shared_scale_keyword_comparison"
        scale_note = (
            "All compared keywords share one relative 0-100 scale for this comparison, "
            "geography and timeframe; not monthly search volume."
        )

    report: dict[str, Any] = {
        "schema_version": "1.0",
        "project_slug": config["project_slug"],
        "source": "Google Trends via Trendspyg",
        "trendspyg_version": package_version,
        "collected_at": started_at,
        "geo": config["geo"],
        "timeframe": config["timeframe"],
        "keywords": keywords,
        "analysis_mode": mode,
        "metric_definition": scale_note,
        "not_provided": [
            "absolute monthly search volume",
            "Google Ads CPC",
            "Google Ads advertiser competition",
        ],
        "trends": trends_data,
    }

    if config["include_trending_now"]:
        try:
            from trendspyg import download_google_trends_rss

            report["trending_now"] = download_google_trends_rss(
                geo=config["geo"],
                normalize=True,
            )
        except Exception as exc:  # RSS is auxiliary; keep the core research report.
            report["trending_now_error"] = f"{type(exc).__name__}: {exc}"

    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate configuration without importing Trendspyg or making network requests.",
    )
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        if args.validate_only:
            print(
                json.dumps(
                    {
                        "valid": True,
                        "project_slug": config["project_slug"],
                        "geo": config["geo"],
                        "timeframe": config["timeframe"],
                        "keyword_count": len(config["keywords"]),
                    },
                    ensure_ascii=False,
                )
            )
            return 0

        if args.output_dir is None:
            parser.error("--output-dir is required unless --validate-only is used.")

        report = collect(config)
        args.output_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        output_path = args.output_dir / f"{config['project_slug']}-{stamp}.json"
        output_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Report saved: {output_path.as_posix()}")
        print(
            f"Project={config['project_slug']} Geo={config['geo']} "
            f"Keywords={len(config['keywords'])} Mode={report['analysis_mode']}"
        )
        return 0
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Google Trends collection failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
