#!/usr/bin/env python3
"""Run SiteOne with a low, bounded request profile and summarize its JSON report."""

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


class ConfigError(ValueError):
    """Unsafe or invalid crawler configuration."""


def validate_public_url(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ConfigError("start_url must be a non-empty string.")
    try:
        parsed = urlsplit(value.strip())
        host = parsed.hostname
        port = parsed.port
    except ValueError as exc:
        raise ConfigError(f"Invalid start_url: {exc}") from exc
    if parsed.scheme.lower() != "https" or not host:
        raise ConfigError("Only public HTTPS start URLs are allowed.")
    if parsed.username is not None or parsed.password is not None:
        raise ConfigError("Embedded username/password is not allowed.")
    if parsed.query or parsed.fragment:
        raise ConfigError("Query strings and fragments are not accepted.")
    host = host.rstrip(".").lower()
    if host in {"localhost", "localhost.localdomain"} or host.endswith((".local", ".internal")):
        raise ConfigError("Local/internal hostnames are not allowed.")
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None
    if ip is not None and not ip.is_global:
        raise ConfigError("Private/non-global IP addresses are not allowed.")
    netloc = host if port in (None, 443) else f"{host}:{port}"
    return urlunsplit(("https", netloc, parsed.path or "/", "", ""))


def integer(config: dict[str, Any], key: str, default: int, low: int, high: int) -> int:
    value = config.get(key, default)
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise ConfigError(f"{key} must be an integer from {low} to {high}.")
    return value


def load_config(path: Path) -> dict[str, Any]:
    try:
        cfg = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"Config not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON: {exc}") from exc
    if not isinstance(cfg, dict):
        raise ConfigError("Config root must be an object.")
    slug = cfg.get("project_slug")
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        raise ConfigError("project_slug must use lowercase letters, numbers and hyphens.")
    device = cfg.get("device", "mobile")
    if device not in {"mobile", "desktop", "tablet"}:
        raise ConfigError("device must be mobile, desktop or tablet.")
    rate = cfg.get("max_requests_per_second", 2)
    if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not 0.2 <= float(rate) <= 2.0:
        raise ConfigError("max_requests_per_second must be between 0.2 and 2.0.")
    return {
        "project_slug": slug,
        "start_url": validate_public_url(cfg.get("start_url")),
        "device": device,
        "max_visited_urls": integer(cfg, "max_visited_urls", 300, 20, 500),
        "max_depth": integer(cfg, "max_depth", 4, 1, 6),
        "workers": integer(cfg, "workers", 2, 1, 3),
        "max_requests_per_second": float(rate),
        "timeout_seconds": integer(cfg, "timeout_seconds", 10, 5, 30),
    }


def build_command(binary: Path, cfg: dict[str, Any], output: Path) -> list[str]:
    output.mkdir(parents=True, exist_ok=True)
    return [
        str(binary),
        f"--url={cfg['start_url']}",
        f"--device={cfg['device']}",
        f"--timeout={cfg['timeout_seconds']}",
        f"--workers={cfg['workers']}",
        f"--max-reqs-per-sec={cfg['max_requests_per_second']}",
        f"--max-depth={cfg['max_depth']}",
        f"--max-visited-urls={cfg['max_visited_urls']}",
        "--max-queue-length=1500",
        "--max-skipped-urls=1000",
        "--hide-progress-bar",
        "--no-color",
        f"--output-html-report={output / 'siteone-report.html'}",
        f"--output-json-file={output / 'siteone-report.json'}",
    ]


def summarize(report_file: Path) -> dict[str, Any]:
    try:
        data = json.loads(report_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not parse SiteOne JSON: {exc}") from exc
    scores = data.get("qualityScores") or {}
    overall = scores.get("overall") or {}
    categories = scores.get("categories") or []
    category_scores = {
        item.get("code"): {
            "name": item.get("name"),
            "score_0_to_10": item.get("score"),
            "label": item.get("label"),
        }
        for item in categories
        if isinstance(item, dict)
    }
    stats = data.get("stats") or {}
    items = (data.get("summary") or {}).get("items") or []
    severities: dict[str, int] = {}
    for item in items:
        if isinstance(item, dict):
            severity = str(item.get("status") or "UNKNOWN").upper()
            severities[severity] = severities.get(severity, 0) + 1
    return {
        "overall_quality_score_0_to_10": overall.get("score"),
        "overall_quality_label": overall.get("label"),
        "category_scores": category_scores,
        "total_urls_visited": stats.get("totalUrls"),
        "total_execution_time_seconds": stats.get("totalExecutionTime"),
        "http_status_counts": stats.get("countByStatus") or {},
        "finding_severity_counts": severities,
        "summary_findings": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--binary", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    try:
        cfg = load_config(args.config)
        if args.validate_only:
            print(json.dumps({
                "valid": True, "project_slug": cfg["project_slug"],
                "start_url": cfg["start_url"], "device": cfg["device"],
                "max_visited_urls": cfg["max_visited_urls"],
            }, ensure_ascii=False))
            return 0
        if args.binary is None or args.output_dir is None:
            parser.error("--binary and --output-dir are required for a live crawl.")
        if not args.binary.is_file():
            raise RuntimeError(f"SiteOne executable not found: {args.binary}")
        started = datetime.now(timezone.utc).isoformat()
        command = build_command(args.binary, cfg, args.output_dir)
        process = subprocess.run(command, capture_output=True, text=True, timeout=1800)
        finished = datetime.now(timezone.utc).isoformat()
        json_file = args.output_dir / "siteone-report.json"
        html_file = args.output_dir / "siteone-report.html"
        if not json_file.is_file():
            detail = (process.stderr or process.stdout or "No JSON report created.")[-6000:]
            raise RuntimeError(f"SiteOne failed (exit {process.returncode}): {detail}")
        summary = summarize(json_file)
        summary.update({
            "schema_version": "1.0",
            "project_slug": cfg["project_slug"],
            "source": "SiteOne Crawler",
            "start_url": cfg["start_url"],
            "device": cfg["device"],
            "crawl_limits": {
                "max_visited_urls": cfg["max_visited_urls"],
                "max_depth": cfg["max_depth"],
                "workers": cfg["workers"],
                "max_requests_per_second": cfg["max_requests_per_second"],
            },
            "started_at": started,
            "finished_at": finished,
            "exit_code": process.returncode,
            "html_report": html_file.name if html_file.is_file() else None,
            "json_report": json_file.name,
            "score_definition": "SiteOne internal 0–10 quality rubric; not a Google ranking score.",
            "limitations": [
                "Visited URL limit includes assets as well as pages.",
                "Crawler timings are not real-user Core Web Vitals.",
            ],
        })
        (args.output_dir / "summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        rows = [
            f"# SiteOne audit — {cfg['project_slug']}", "",
            f"- Start URL: {cfg['start_url']}",
            f"- Device: {cfg['device']}",
            f"- Visited URLs: {summary.get('total_urls_visited')}",
            f"- Quality score: {summary.get('overall_quality_score_0_to_10')}/10",
            f"- Findings: {json.dumps(summary.get('finding_severity_counts'), ensure_ascii=False)}",
            "",
            "| Category | Score (0–10) | Label |",
            "|---|---:|---|",
        ]
        for code, item in summary["category_scores"].items():
            rows.append(f"| {item.get('name') or code} | {item.get('score_0_to_10')} | {item.get('label')} |")
        rows.extend(["", "SiteOne scores use its own 0–10 rubric. Crawler timings are not real-user Core Web Vitals.", ""])
        (args.output_dir / "summary.md").write_text("\n".join(rows), encoding="utf-8")
        print(json.dumps({
            "project_slug": cfg["project_slug"],
            "exit_code": process.returncode,
            "quality_score_0_to_10": summary.get("overall_quality_score_0_to_10"),
            "visited_urls": summary.get("total_urls_visited"),
            "output_dir": str(args.output_dir),
        }, ensure_ascii=False))
        return 0 if process.returncode == 0 and html_file.is_file() else 1
    except (ConfigError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"SiteOne audit failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
