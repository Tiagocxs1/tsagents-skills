#!/usr/bin/env python3
"""Run a bounded Lighthouse audit and summarize the resulting JSON reports."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
METRIC_IDS = (
    "first-contentful-paint",
    "largest-contentful-paint",
    "cumulative-layout-shift",
    "interaction-to-next-paint",
    "total-blocking-time",
    "speed-index",
    "server-response-time",
)
CATEGORY_IDS = ("performance", "accessibility", "best-practices", "seo")
LIGHTHOUSE_VERSION = "13.6.0"


class ConfigError(ValueError):
    """Raised for an unsafe or invalid audit configuration."""


def validate_public_url(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ConfigError("Every URL must be a non-empty string.")

    url = value.strip()
    try:
        parsed = urlsplit(url)
        hostname = parsed.hostname
        port = parsed.port
    except ValueError as exc:
        raise ConfigError(f"Invalid URL {url!r}: {exc}") from exc

    if parsed.scheme.lower() != "https":
        raise ConfigError(f"Only public HTTPS URLs are allowed: {url!r}")
    if not hostname:
        raise ConfigError(f"URL is missing a hostname: {url!r}")
    if parsed.username is not None or parsed.password is not None:
        raise ConfigError("URLs must not contain embedded usernames or passwords.")
    if parsed.query or parsed.fragment:
        raise ConfigError("Query strings and fragments are not accepted in audit URLs.")

    hostname = hostname.rstrip(".").lower()
    if hostname in {"localhost", "localhost.localdomain"} or hostname.endswith((".local", ".internal")):
        raise ConfigError(f"Local or internal hostnames are not allowed: {hostname!r}")

    try:
        ip = ipaddress.ip_address(hostname)
    except ValueError:
        ip = None
    if ip is not None and not ip.is_global:
        raise ConfigError(f"Private or non-global IP addresses are not allowed: {hostname!r}")

    netloc = hostname
    if port is not None and port != 443:
        netloc = f"{hostname}:{port}"

    path = parsed.path or "/"
    return urlunsplit(("https", netloc, path, "", ""))


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

    urls = config.get("urls")
    if not isinstance(urls, list) or not 1 <= len(urls) <= 5:
        raise ConfigError("urls must contain between 1 and 5 public HTTPS URLs.")

    normalized_urls = [validate_public_url(url) for url in urls]
    if len(set(normalized_urls)) != len(normalized_urls):
        raise ConfigError("urls must not contain duplicates.")

    preset = config.get("preset", "mobile")
    if preset not in {"mobile", "desktop"}:
        raise ConfigError("preset must be 'mobile' or 'desktop'.")

    return {"project_slug": slug, "urls": normalized_urls, "preset": preset}


def _safe_name(url: str, index: int) -> str:
    parsed = urlsplit(url)
    label = (parsed.hostname or "site") + parsed.path
    label = re.sub(r"[^a-zA-Z0-9]+", "-", label).strip("-").lower()
    return f"{index:02d}-{label[:70] or 'page'}"


def _extract_report(url: str, report_path: Path) -> dict[str, Any]:
    try:
        lighthouse = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"url": url, "status": "failed", "error": f"Could not parse Lighthouse JSON: {exc}"}

    categories: dict[str, int | None] = {}
    for category_id in CATEGORY_IDS:
        category = lighthouse.get("categories", {}).get(category_id, {})
        score = category.get("score")
        categories[category_id] = round(score * 100) if isinstance(score, (int, float)) else None

    audits = lighthouse.get("audits", {})
    metrics: dict[str, dict[str, Any]] = {}
    for audit_id in METRIC_IDS:
        audit = audits.get(audit_id)
        if isinstance(audit, dict):
            metrics[audit_id] = {
                "display_value": audit.get("displayValue"),
                "numeric_value": audit.get("numericValue"),
                "score": audit.get("score"),
            }

    return {
        "url": url,
        "final_url": lighthouse.get("finalDisplayedUrl"),
        "fetch_time": lighthouse.get("fetchTime"),
        "lighthouse_version": lighthouse.get("lighthouseVersion"),
        "status": "completed",
        "categories": categories,
        "metrics": metrics,
        "report_json": report_path.name,
        "report_html": report_path.with_suffix(".html").name,
    }


def collect(config: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []

    for index, url in enumerate(config["urls"], start=1):
        output_base = output_dir / _safe_name(url, index)
        command = [
            "npx", "--yes", f"lighthouse@{LIGHTHOUSE_VERSION}", url,
            "--quiet",
            "--chrome-flags=--headless --no-sandbox --disable-dev-shm-usage",
            "--only-categories=" + ",".join(CATEGORY_IDS),
            "--output=html", "--output=json",
            f"--output-path={output_base}",
            "--locale=pt-BR",
            "--max-wait-for-load=45000",
        ]
        if config["preset"] == "desktop":
            command.append("--preset=desktop")

        try:
            process = subprocess.run(
                command, check=False, capture_output=True, text=True, timeout=300
            )
            json_path = Path(f"{output_base}.report.json")
            if process.returncode != 0:
                detail = (process.stderr or process.stdout or "Lighthouse exited with a non-zero status.")[-4000:]
                results.append({"url": url, "status": "failed", "error": detail})
                continue
            results.append(_extract_report(url, json_path))
        except subprocess.TimeoutExpired:
            results.append({"url": url, "status": "failed", "error": "Lighthouse exceeded the 300-second per-URL timeout."})
        except OSError as exc:
            results.append({"url": url, "status": "failed", "error": f"Could not start Lighthouse: {exc}"})

    completed_at = datetime.now(timezone.utc).isoformat()
    summary: dict[str, Any] = {
        "schema_version": "1.0",
        "project_slug": config["project_slug"],
        "source": "Google Lighthouse",
        "lighthouse_package_version": LIGHTHOUSE_VERSION,
        "preset": config["preset"],
        "started_at": started_at,
        "completed_at": completed_at,
        "requested_urls": config["urls"],
        "completed": sum(1 for result in results if result["status"] == "completed"),
        "failed": sum(1 for result in results if result["status"] != "completed"),
        "results": results,
        "interpretation": (
            "Lighthouse scores are lab measurements from this run. They are not ranking positions, "
            "absolute traffic estimates or a substitute for real-user CrUX/Search Console data."
        ),
    }

    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        f"# Lighthouse audit — {config['project_slug']}", "",
        f"- Preset: {config['preset']}",
        f"- Started: {started_at}",
        f"- Completed: {completed_at}",
        f"- Completed URLs: {summary['completed']}/{len(config['urls'])}",
        "",
        "| URL | Performance | Accessibility | Best Practices | SEO | Status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for result in results:
        categories = result.get("categories", {})
        def score(name: str) -> str:
            value = categories.get(name)
            return str(value) if value is not None else "—"
        lines.append(
            f"| {result['url']} | {score('performance')} | {score('accessibility')} "
            f"| {score('best-practices')} | {score('seo')} | {result['status']} |"
        )
        if result.get("error"):
            lines.extend(["", f"**Error for {result['url']}:**", "", "~~~text", result["error"], "~~~"])
    lines.extend(["", summary["interpretation"], ""])
    (output_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        if args.validate_only:
            print(json.dumps({
                "valid": True, "project_slug": config["project_slug"],
                "preset": config["preset"], "url_count": len(config["urls"]),
            }, ensure_ascii=False))
            return 0
        if args.output_dir is None:
            parser.error("--output-dir is required unless --validate-only is used.")

        summary = collect(config, args.output_dir)
        print(json.dumps({
            "project_slug": config["project_slug"],
            "completed": summary["completed"],
            "failed": summary["failed"],
            "output_dir": str(args.output_dir),
        }, ensure_ascii=False))
        return 0 if summary["failed"] == 0 else 1
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
