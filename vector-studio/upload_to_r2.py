#!/usr/bin/env python3
"""Publish generated Vector Studio files to a temporary Cloudflare R2 prefix using GitHub OIDC."""

from __future__ import annotations

import json
import mimetypes
import os
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests


def main() -> int:
    out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "output/vector-studio")
    base_url = os.environ["VECTOR_ASSET_UPLOAD_URL"].rstrip("/")
    oidc_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    oidc_secret = os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]
    run_id = os.environ["GITHUB_RUN_ID"]
    parts = urlsplit(oidc_url)
    query = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != "audience"]
    query.append(("audience", "ts-svg-assets"))
    token_url = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))
    token_response = requests.get(
        token_url,
        headers={"Authorization": "Bearer " + oidc_secret, "Accept": "application/json"},
        timeout=30,
    )
    token_response.raise_for_status()
    oidc_token = token_response.json().get("value")
    if not oidc_token:
        raise RuntimeError("GitHub did not return an OIDC token.")
    # Print only non-secret JWT claims to make trust-policy mismatches diagnosable.
    import base64
    token_parts = oidc_token.split(".")
    if len(token_parts) == 3:
        payload = token_parts[1] + "=" * ((4 - len(token_parts[1]) % 4) % 4)
        claims = json.loads(base64.urlsafe_b64decode(payload.encode("ascii")))
        safe_names = (
            "iss", "aud", "sub", "repository", "repository_id",
            "repository_owner", "repository_owner_id", "ref",
            "workflow", "workflow_ref", "job_workflow_ref",
            "runner_environment", "event_name"
        )
        print("OIDC non-secret claims:", json.dumps(
            {name: claims.get(name) for name in safe_names if name in claims},
            ensure_ascii=False,
            sort_keys=True
        ))

    uploaded = []
    for path in sorted(out_dir.iterdir()):
        if not path.is_file() or path.name == "remote-assets.json":
            continue
        mime, _ = mimetypes.guess_type(path.name)
        if not mime:
            mime = "application/octet-stream"
        data = path.read_bytes()
        if not data:
            continue
        url = base_url + "/upload/" + path.name + "?run_id=" + run_id
        response = requests.put(
            url,
            data=data,
            headers={
                "Authorization": "Bearer " + oidc_token,
                "Content-Type": mime,
                "Accept": "application/json",
            },
            timeout=(20, 120),
        )
        if not response.ok:
            raise RuntimeError(
                "Cloudflare R2 upload failed for " + path.name + ": HTTP "
                + str(response.status_code) + " " + response.text[:1000]
            )
        result = response.json()
        if not result.get("ok") or not result.get("url"):
            raise RuntimeError("Cloudflare returned an incomplete upload result for " + path.name)
        uploaded.append(result)
        print("Uploaded", path.name, str(len(data)) + " bytes", result["url"])

    if not uploaded:
        raise RuntimeError("No generated files were uploaded.")

    # Verify that every published Worker URL is publicly reachable and has the expected metadata.
    for item in uploaded:
        head = requests.head(item["url"], timeout=(20, 60), allow_redirects=False)
        if not head.ok:
            raise RuntimeError(
                "Public asset URL check failed for " + item["filename"]
                + ": HTTP " + str(head.status_code) + " " + head.text[:500]
            )
        actual_length = int(head.headers.get("Content-Length", "-1"))
        if actual_length != int(item["bytes"]):
            raise RuntimeError(
                "Public asset URL length mismatch for " + item["filename"]
                + ": expected " + str(item["bytes"]) + ", received " + str(actual_length)
            )
        actual_type = head.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        expected_type = item.get("content_type", "").split(";", 1)[0].strip().lower()
        if actual_type != expected_type:
            raise RuntimeError(
                "Public asset URL MIME mismatch for " + item["filename"]
                + ": expected " + expected_type + ", received " + actual_type
            )
        item["public_url_verification"] = {
            "method": "HEAD",
            "status_code": head.status_code,
            "content_length": actual_length,
            "content_type": head.headers.get("Content-Type")
        }
        print("Verified public URL", item["filename"], "HTTP", head.status_code, actual_length, "bytes")

    manifest = {
        "service": "ts-svg-assets",
        "storage": "Cloudflare R2 / ts-image-assets-temp",
        "workflow_run_id": run_id,
        "retention": "Existing R2 lifecycle deletes objects under images/ after 7 days (asynchronous processing may add delay).",
        "assets": uploaded,
    }
    (out_dir / "remote-assets.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"uploaded": len(uploaded), "manifest": str(out_dir / "remote-assets.json")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
