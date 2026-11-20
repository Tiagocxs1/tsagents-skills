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
    query = parse_qsl(parts.query, keep_blank_values=True)
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
