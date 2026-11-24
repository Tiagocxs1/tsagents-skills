#!/usr/bin/env python3
"""Build and sync the public CC0/MIT visual library directly to Cloudflare R2."""
from __future__ import annotations
import base64, concurrent.futures, hashlib, io, json, mimetypes, os, re, shutil
import subprocess, tempfile, threading, time, unicodedata, zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit, quote

import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://ts-visual-library.tiagocxs-tdb.workers.dev"
OIDC_AUDIENCE = "ts-visual-library"
KITBITZ_REPO = "https://github.com/CaptExcellent/kits-library-assets.git"
KITBITZ_COMMIT = "c67532ddf21cef61827de203344282cc9c2cecae"
IRA_ZIP = "https://raw.githubusercontent.com/ira-design/ira-illustrations/SVG/SVG.zip"
IRA_ZIP_SHA256 = "8da78c4d4671b8f440781114ea82149f9c32c903e7b22c702bfb8b9ff1efccc1"
OPEN_DOODLES_ZIP = "https://www.dropbox.com/sh/egmjlot3o8787sr/AABbIT7a1-3zWvF7HQ8R21_ta?dl=1"
OPEN_DOODLES_ZIP_SHA256 = "e8c9cd23349eeb096fbc55e17a219ca6f1696907468147a4606d474befd4c11b"
ASSET_POLISH_CATALOG = "https://www.assetpolish.com/catalog.json"
ASSET_POLISH_PACKS = {
    "online-safety", "campaign-studio", "creator-desk",
    "ready-plan-icons", "ready-together-stickers", "colour-animals"
}
POLYHAVEN_IDS = [
    "white_plaster_02", "grey_plaster", "painted_concrete_02",
    "concrete_wall_007", "rough_linen", "fabric_leather_01",
    "metal_plate_02", "rust_coarse_01", "decrepit_wallpaper"
]
MAX_FILE_BYTES = 25 * 1024 * 1024
MAX_WORKERS = 10
USER_AGENT = "TS-Digitais-Visual-Library-Sync/1.0 (+https://github.com/Tiagocxs1/tsagents-skills)"

ROOT = Path(__file__).resolve().parent
WORK = Path(tempfile.mkdtemp(prefix="ts-visual-library-"))
FILES: dict[str, dict] = {}
ASSETS: list[dict] = []
COLLECTIONS: list[dict] = []
LOCK = threading.Lock()
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": USER_AGENT})

def norm_text(value: str) -> str:
    raw = unicodedata.normalize("NFKD", str(value or ""))
    raw = "".join(c for c in raw if not unicodedata.combining(c)).lower()
    return " ".join(re.findall(r"[a-z0-9]+", raw))

def mime_for(path: Path) -> str:
    ext = path.suffix.lower()
    return {
        ".svg": "image/svg+xml", ".png": "image/png",
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp", ".json": "application/json",
        ".html": "text/html; charset=utf-8", ".md": "text/markdown; charset=utf-8",
        ".txt": "text/plain; charset=utf-8"
    }.get(ext, mimetypes.guess_type(path.name)[0] or "application/octet-stream")

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def http_download(url: str, destination: Path, max_bytes: int = 1024 * 1024 * 1024) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_suffix(destination.suffix + ".part")
    total = 0
    with SESSION.get(url, stream=True, timeout=(30, 180), allow_redirects=True) as r:
        r.raise_for_status()
        with tmp.open("wb") as f:
            for chunk in r.iter_content(1024 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > max_bytes:
                    raise RuntimeError("Download exceeded allowed size: " + url)
                f.write(chunk)
    if total == 0:
        raise RuntimeError("Empty download: " + url)
    tmp.replace(destination)
    return destination

def safe_archive_path(name: str) -> bool:
    p = PurePosixPath(name)
    return not p.is_absolute() and ".." not in p.parts and "\\" not in name

def register_file(path: Path, key: str, collection: str, license_name: str, source_url: str, author: str) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    size = path.stat().st_size
    if size <= 0 or size > MAX_FILE_BYTES:
        raise RuntimeError(f"File size outside 1..25 MiB: {path} ({size})")
    if not key.startswith("assets/v1/") or ".." in PurePosixPath(key).parts:
        raise RuntimeError("Unsafe R2 object key: " + key)
    item = {
        "key": key, "path": str(path), "relative_path": key,
        "content_type": mime_for(path), "size_bytes": size,
        "sha256": sha256_file(path), "license": license_name,
        "collection": collection, "source_url": source_url, "author": author
    }
    FILES[key] = item
    return item

def add_asset(asset_id: str, name: str, collection: str, collection_name: str,
              category: str, style: str, tags: list[str], license_name: str,
              license_url: str, author: str, source_url: str,
              file_item: dict, preview_item: dict | None = None, notes: str = "") -> None:
    all_tags = list(dict.fromkeys([str(x) for x in tags if x]))
    search_blob = norm_text(" ".join([
        name, category, style, collection_name, " ".join(all_tags), notes
    ]))
    ASSETS.append({
        "id": asset_id, "name": name, "collection": collection,
        "collection_name": collection_name, "category": category,
        "style": style, "tags": all_tags, "license": license_name,
        "license_url": license_url, "commercial_use_confirmed": True,
        "author": author, "source_url": source_url,
        "file_key": file_item["key"],
        "preview_key": (preview_item or file_item)["key"],
        "format": Path(file_item["path"]).suffix.lstrip(".").upper(),
        "bytes": file_item["size_bytes"], "sha256": file_item["sha256"],
        "search_blob": search_blob, "notes": notes
    })

def collection(cid: str, name: str, license_name: str, license_url: str,
               styles: list[str], description: str) -> dict:
    item = {"id": cid, "name": name, "license": license_name,
            "license_url": license_url, "count": 0, "styles": styles,
            "description": description}
    COLLECTIONS.append(item)
    return item

def validate_svg(path: Path) -> None:
    root = ET.parse(path).getroot()
    if not str(root.tag).lower().endswith("svg"):
        raise ValueError("Downloaded SVG root element is not <svg>: " + str(path))
    for element in root.iter():
        if element.tag.lower().endswith("script"):
            raise ValueError("Script element found in public SVG: " + str(path))
        if element.tag.lower().endswith("foreignobject"):
            raise ValueError("foreignObject found in public SVG: " + str(path))

def add_svg_asset(cid: str, col_name: str, rel_key: str, name: str,
                  category: str, style: str, tags: list[str],
                  license_name: str, license_url: str, author: str,
                  source_url: str, path: Path, preview_path: Path | None = None,
                  notes: str = "") -> None:
    validate_svg(path)
    file_item = register_file(path, rel_key, col_name, license_name, source_url, author)
    preview_item = None
    if preview_path and preview_path.is_file():
        # Only use a PNG preview that is itself in the curated public source package.
        preview_item = register_file(
            preview_path, rel_key.rsplit("/", 1)[0] + "/" + preview_path.name,
            col_name, license_name, source_url, author
        )
    add_asset(cid, name, cid.split(":", 1)[0], col_name, category, style, tags,
              license_name, license_url, author, source_url,
              file_item, preview_item, notes)

def download_kitbitz() -> None:
    print("1/6 · Downloading pinned Kitbitz CC0 repository…", flush=True)
    archive = http_download(
        f"https://codeload.github.com/CaptExcellent/kits-library-assets/zip/{KITBITZ_COMMIT}",
        WORK / "kitbitz.zip", max_bytes=900 * 1024 * 1024
    )
    out = WORK / "kitbitz"
    out.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError("Kitbitz ZIP integrity failure at " + bad)
        names = [n for n in z.namelist() if "/kits/" in n and n.lower().endswith((".svg", ".png"))]
        if len(names) < 4500:
            raise RuntimeError(f"Unexpected Kitbitz archive content: {len(names)} files")
        root_prefix = names[0].split("/kits/", 1)[0] + "/"
        for info in z.infolist():
            name = info.filename
            if not name.startswith(root_prefix + "kits/") or not name.lower().endswith((".svg", ".png")):
                continue
            if not safe_archive_path(name):
                raise RuntimeError("Unsafe Kitbitz ZIP path: " + name)
            rel = name[len(root_prefix):]
            target = out / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst, 1024 * 1024)
    svg_files = sorted(out.rglob("*.svg"))
    png_files = {p.relative_to(out).as_posix(): p for p in out.rglob("*.png")}
    col = collection("kitbitz", "Kitbitz Full Library", "CC0-1.0",
        "https://creativecommons.org/publicdomain/zero/1.0/", ["2.5D", "isometric"],
        "Editable 2.5D objects, props and scene components. Generic illustration, not real equipment.")
    for svg in svg_files:
        rel = svg.relative_to(out).as_posix()
        if not rel.startswith("kits/"):
            continue
        kit = rel.split("/")[1] if len(rel.split("/")) > 2 else "kitbitz"
        stem = svg.stem
        png = png_files.get(str(PurePosixPath(rel).with_name(stem + "@2x.png")))
        key = "assets/v1/kitbitz/" + rel[len("kits/"):]
        source = f"https://github.com/CaptExcellent/kits-library-assets/tree/{KITBITZ_COMMIT}/{rel}"
        item = register_file(svg, key, "Kitbitz", "CC0-1.0", source, "Kitbitz contributors")
        preview_item = None
        if png:
            pkey = "assets/v1/kitbitz/" + png.relative_to(out).as_posix()[len("kits/"):]
            preview_item = register_file(png, pkey, "Kitbitz", "CC0-1.0", source, "Kitbitz contributors")
        tags = ["2.5d", "isometric", "object", "prop", "scene", "vector"] + norm_text(stem.replace("-", " ")).split() + [kit]
        add_asset("kitbitz:" + rel, stem.replace("-", " "), "kitbitz", "Kitbitz Full Library",
            "Vector object / scene component", "2.5D / isometric", tags, "CC0-1.0",
            "https://creativecommons.org/publicdomain/zero/1.0/", "Kitbitz contributors",
            source, item, preview_item,
            "Generic illustration. Do not label as an actual Guardian or Intelbras installation.")
    # Some published PNGs have no matching SVG. Keep them searchable as raster visual assets.
    paired = {p for a in ASSETS if a["collection"] == "kitbitz" for p in [a.get("preview_key")]}
    referenced = set()
    for svg in svg_files:
        png = png_files.get(str(PurePosixPath(svg.relative_to(out).as_posix()).with_name(svg.stem + "@2x.png")))
        if png:
            referenced.add(png)
    for png in png_files.values():
        if png in referenced:
            continue
        rel = png.relative_to(out).as_posix()
        kit = rel.split("/")[1] if len(rel.split("/")) > 2 else "kitbitz"
        key = "assets/v1/kitbitz/" + rel[len("kits/"):]
        source = f"https://github.com/CaptExcellent/kits-library-assets/tree/{KITBITZ_COMMIT}/{rel}"
        f = register_file(png, key, "Kitbitz", "CC0-1.0", source, "Kitbitz contributors")
        add_asset("kitbitz-png:" + rel, png.stem.replace("@2x", "").replace("-", " "),
            "kitbitz", "Kitbitz Full Library", "Raster illustration / object", "2.5D / isometric",
            ["2.5d", "isometric", "object", "raster", kit], "CC0-1.0",
            "https://creativecommons.org/publicdomain/zero/1.0/", "Kitbitz contributors",
            source, f, f, "Standalone PNG supplied by the Kitbitz CC0 repository.")
    col["count"] = sum(1 for a in ASSETS if a["collection"] == "kitbitz")
    print("Kitbitz assets:", col["count"], "files:", len([x for x in FILES.values() if x["collection"]=="Kitbitz"]), flush=True)

def download_assetpolish() -> None:
    print("2/6 · Downloading selected AssetPolish CC0 collections…", flush=True)
    response = SESSION.get(ASSET_POLISH_CATALOG, timeout=(30, 90))
    response.raise_for_status()
    catalog = response.json()
    selected = [x for x in catalog if x.get("pack") in ASSET_POLISH_PACKS and str(x.get("license", "CC0-1.0")).upper().startswith("CC0")]
    expected = {"online-safety":153, "campaign-studio":169, "creator-desk":169,
                "ready-plan-icons":15, "ready-together-stickers":40, "colour-animals":93}
    counts = {}
    for x in selected:
        counts[x["pack"]] = counts.get(x["pack"], 0) + 1
    for pack, minimum in expected.items():
        if counts.get(pack, 0) < minimum:
            raise RuntimeError(f"AssetPolish pack {pack} changed: expected at least {minimum}, received {counts.get(pack,0)}")
    col = collection("assetpolish", "AssetPolish Selected Collections", "CC0-1.0",
        "https://creativecommons.org/publicdomain/zero/1.0/", ["outline", "soft duotone", "sticker"],
        "Selected coordinated illustrations for security/privacy, campaigns, creator work and stickers.")
    for i, item in enumerate(selected, 1):
        url = item.get("url") or item.get("sourceUrl")
        if not url:
            raise RuntimeError("AssetPolish record lacks direct SVG URL: " + str(item.get("id")))
        if url.startswith("/"):
            url = "https://www.assetpolish.com" + url
        if not url.startswith("https://www.assetpolish.com/assets/"):
            raise RuntimeError("Unexpected AssetPolish asset host: " + url)
        pack = item["pack"]
        filename = Path(url.split("?",1)[0]).name
        target = WORK / "assetpolish" / pack / filename
        http_download(url, target, max_bytes=5*1024*1024)
        path_key = f"assets/v1/assetpolish/{pack}/{filename}"
        tags = (item.get("tags") or []) + (item.get("subjects") or []) + (item.get("useCases") or [])
        add_svg_asset("assetpolish:" + str(item.get("id") or filename), "AssetPolish Selected Collections",
            path_key, item.get("name") or Path(filename).stem, item.get("category") or item.get("packName") or pack,
            item.get("style") or "vector", tags, "CC0-1.0",
            "https://creativecommons.org/publicdomain/zero/1.0/", item.get("author") or "AssetPolish",
            url, target, notes="CC0 vector from the official AssetPolish catalogue.")
        if i % 100 == 0:
            print("  AssetPolish downloaded:", i, flush=True)
    col["count"] = sum(1 for a in ASSETS if a["collection"] == "assetpolish")
    print("AssetPolish assets:", col["count"], flush=True)

def download_ira() -> None:
    print("3/6 · Downloading official IRA Design MIT archive…", flush=True)
    archive = http_download(IRA_ZIP, WORK/"ira-design.zip", max_bytes=30*1024*1024)
    if sha256_file(archive) != IRA_ZIP_SHA256:
        raise RuntimeError("IRA Design source ZIP hash changed; stop for license/source review.")
    col = collection("ira-design", "IRA Design / Creative Tim", "MIT",
        "https://github.com/ira-design/ira-illustrations/blob/master/LICENSE.md",
        ["gradient", "outline"], "Hand-drawn character poses, objects, backgrounds and examples.")
    extracted = 0
    with zipfile.ZipFile(archive) as z:
        if z.testzip():
            raise RuntimeError("IRA Design ZIP integrity test failed.")
        for info in z.infolist():
            member = info.filename
            if not member.startswith("SVG/") or not member.lower().endswith(".svg") or member.startswith("__MACOSX/"):
                continue
            if not safe_archive_path(member):
                raise RuntimeError("Unsafe IRA ZIP path: " + member)
            rel = member[len("SVG/"):]
            target = WORK/"ira-design"/rel
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            parts = PurePosixPath(rel).parts
            top = parts[0] if parts else "Illustration"
            category = {"Characters":"Character / human pose","Objects":"Object / prop","Backgrounds":"Background / environment","Examples":"Precomposed scene"}.get(top,top)
            style = parts[1].lower() if len(parts)>2 and parts[0] in ("Characters","Objects") else "vector"
            key = "assets/v1/ira-design/" + rel
            src_url = "https://github.com/ira-design/ira-illustrations"
            tags = ["ira-design","creative-tim","illustration","vector",category.lower()]
            if top=="Characters": tags += ["person","people","human","pose","character"]
            if top=="Objects": tags += ["object","prop","accessory"]
            add_svg_asset("ira-design:"+rel, "IRA Design / Creative Tim", key,
                Path(rel).stem, category, style, tags, "MIT",
                "https://github.com/ira-design/ira-illustrations/blob/master/LICENSE.md",
                "Creative Tim", src_url, target,
                notes="MIT asset. Retain copyright and license notice when redistributing copies or substantial portions. Generic illustration, not Guardian staff or customers.")
            extracted += 1
    if extracted < 130:
        raise RuntimeError(f"IRA Design archive unexpectedly contained only {extracted} SVGs.")
    col["count"] = extracted
    print("IRA Design SVGs:", extracted, flush=True)

def download_open_doodles() -> None:
    print("4/6 · Downloading official Open Doodles CC0 source pack…", flush=True)
    archive = http_download(OPEN_DOODLES_ZIP, WORK/"open-doodles.zip", max_bytes=150*1024*1024)
    if sha256_file(archive) != OPEN_DOODLES_ZIP_SHA256:
        raise RuntimeError("Open Doodles source ZIP hash changed; stop for source review.")
    col = collection("open-doodles", "Open Doodles", "CC0-1.0",
        "https://creativecommons.org/publicdomain/zero/1.0/", ["hand-drawn", "sketch"],
        "Hand-drawn characters, compositions and editorial scenes.")
    allowed = {"Illustrations","Compositions","Templates","Website Example"}
    extracted = 0
    with zipfile.ZipFile(archive) as z:
        if z.testzip():
            raise RuntimeError("Open Doodles ZIP integrity test failed.")
        for info in z.infolist():
            member = info.filename
            parts = PurePosixPath(member).parts
            if not member.lower().endswith(".svg") or not parts or parts[0] not in allowed:
                continue
            if not safe_archive_path(member) or any(p.startswith(".") for p in parts):
                continue
            target = WORK/"open-doodles"/member
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            top = parts[0]
            category = {"Illustrations":"Hand-drawn character / object","Compositions":"Precomposed illustration scene","Templates":"Layout reference","Website Example":"Web decoration"}[top]
            key = "assets/v1/open-doodles/" + member
            add_svg_asset("open-doodles:"+member, "Open Doodles", key, Path(member).stem,
                category, "hand-drawn sketch",
                ["open-doodles","pablo-stanley","hand-drawn","sketch","character","scene",category.lower()],
                "CC0-1.0","https://creativecommons.org/publicdomain/zero/1.0/",
                "Pablo Stanley / Fang-Pen Lin", "https://www.opendoodles.com/about", target,
                notes="CC0. Friendly sketch tone; generic characters are not Guardian staff or clients.")
            extracted += 1
    if extracted < 80:
        raise RuntimeError(f"Open Doodles pack unexpectedly contained only {extracted} SVGs.")
    col["count"] = extracted
    print("Open Doodles SVGs:", extracted, flush=True)

def download_open_peeps() -> None:
    print("5/6 · Downloading selected Open Peeps CC0 SVGs…", flush=True)
    source = json.loads((ROOT/"open-peeps-sources.json").read_text(encoding="utf-8"))
    col = collection("open-peeps", "Open Peeps (selected files)", "CC0-1.0",
        "https://creativecommons.org/publicdomain/zero/1.0/", ["hand-drawn", "modular character"],
        "Selected modular portraits and poses; this is not the full Open Peeps pack.")
    for item in source["assets"]:
        url = item["source_url"]
        if not url.startswith("https://cdn.prod.website-files.com/"):
            raise RuntimeError("Unexpected Open Peeps file host.")
        name = Path(url.split("?",1)[0]).name
        target = WORK/"open-peeps"/name
        http_download(url, target, max_bytes=3*1024*1024)
        key = "assets/v1/open-peeps/" + name
        add_svg_asset("open-peeps:"+item["id"], "Open Peeps (selected files)", key, item["name"],
            item.get("category","Human character / pose"), item.get("style","Hand-drawn character illustration"),
            item.get("tags",[])+["people","human","character","hand-drawn"],
            "CC0-1.0","https://creativecommons.org/publicdomain/zero/1.0/",
            item.get("creator") or "Pablo Stanley", url, target,
            notes="Selected 19-file subset. Generic people are not actual Guardian staff or customers.")
    col["count"] = sum(1 for a in ASSETS if a["collection"] == "open-peeps")
    print("Open Peeps SVGs:", col["count"], flush=True)

def download_polyhaven() -> None:
    print("6/6 · Downloading Poly Haven CC0 surface textures…", flush=True)
    catalog_url = "https://api.polyhaven.com/assets?type=textures"
    meta_response = SESSION.get(catalog_url, timeout=(30,90)); meta_response.raise_for_status()
    metadata = meta_response.json()
    col = collection("polyhaven", "Poly Haven Surface Textures", "CC0-1.0",
        "https://polyhaven.com/license", ["photographic surface", "PBR albedo"],
        "2K JPG diffuse/albedo maps for wall, textile and material surfaces.")
    for aid in POLYHAVEN_IDS:
        if aid not in metadata:
            raise RuntimeError("Poly Haven texture is no longer in the catalogue: " + aid)
        f = SESSION.get(f"https://api.polyhaven.com/files/{aid}?resolution=2k&format=jpg", timeout=(30,90))
        f.raise_for_status(); files = f.json()
        diffuse = files.get("Diffuse") or files.get("diffuse") or files.get("diff")
        item = (diffuse or {}).get("2k",{}).get("jpg",{})
        url = item.get("url")
        if not url:
            raise RuntimeError("Poly Haven API did not return 2K JPG for " + aid)
        target = WORK/"polyhaven"/(aid+".jpg")
        http_download(url, target, max_bytes=12*1024*1024)
        authors = ", ".join((metadata[aid].get("authors") or {}).keys())
        key = "assets/v1/polyhaven/" + aid + "-diff-2k.jpg"
        fi = register_file(target,key,"Poly Haven","CC0-1.0",f"https://polyhaven.com/a/{aid}",authors)
        add_asset("polyhaven:"+aid, metadata[aid].get("name",aid), "polyhaven", "Poly Haven Surface Textures",
            "Photographic surface texture", metadata[aid].get("category","PBR albedo"),
            (metadata[aid].get("tags") or [])+["texture","surface","diffuse","albedo","2k"],
            "CC0-1.0","https://polyhaven.com/license",authors,
            f"https://polyhaven.com/a/{aid}", fi, fi,
            "Diffuse/albedo map, not a transparent overlay or a ready-made shadow.")
    col["count"] = sum(1 for a in ASSETS if a["collection"] == "polyhaven")
    print("Poly Haven textures:", col["count"], flush=True)

class OidcTokenProvider:
    def __init__(self):
        self.lock = threading.Lock()
        self.token = None
        self.valid_until = 0
    def get(self, force=False):
        with self.lock:
            if self.token and not force and time.monotonic() < self.valid_until:
                return self.token
            url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
            secret = os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]
            parts = urlsplit(url)
            query = [(k,v) for k,v in parse_qsl(parts.query, keep_blank_values=True) if k!="audience"]
            query.append(("audience",OIDC_AUDIENCE))
            token_url = urlunsplit((parts.scheme,parts.netloc,parts.path,urlencode(query),parts.fragment))
            r = requests.get(token_url,headers={"Authorization":"Bearer "+secret,"Accept":"application/json"},timeout=30)
            r.raise_for_status()
            value = r.json().get("value")
            if not value:
                raise RuntimeError("GitHub OIDC endpoint did not return a token.")
            self.token=value;self.valid_until=time.monotonic()+180
            return self.token
    def invalidate(self):
        with self.lock:
            self.token=None;self.valid_until=0

def upload_one(item: dict, provider: OidcTokenProvider) -> dict:
    key=item["key"]; path=Path(item["path"]); size=item["size_bytes"]
    if size>MAX_FILE_BYTES: raise RuntimeError("File exceeds worker size limit: "+key)
    url=BASE_URL+"/upload?key="+quote(key,safe="")
    for attempt in range(4):
        token=provider.get(force=attempt>0)
        headers={"Authorization":"Bearer "+token,"Content-Type":item["content_type"],
                 "Content-Length":str(size),"X-Asset-Sha256":item["sha256"],"Accept":"application/json"}
        try:
            with path.open("rb") as body:
                r=requests.put(url,data=body,headers=headers,timeout=(30,180))
            if r.status_code==401:
                provider.invalidate()
                continue
            if not r.ok:
                raise RuntimeError(f"Upload failed ({r.status_code}) for {key}: {r.text[:400]}")
            result=r.json()
            if not result.get("ok") or result.get("key")!=key or int(result.get("size",0))!=size:
                raise RuntimeError("Cloudflare returned inconsistent upload metadata for "+key)
            return {"key":key,"bytes":size,"sha256":item["sha256"],"status":r.status_code}
        except Exception:
            if attempt==3: raise
            time.sleep(2**attempt)
    raise RuntimeError("OIDC upload retries exhausted for "+key)

def main():
    if not os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL") or not os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN"):
        raise RuntimeError("GitHub Actions OIDC is required; this script must run in the authorized workflow.")
    download_kitbitz()
    download_assetpolish()
    download_ira()
    download_open_doodles()
    download_open_peeps()
    download_polyhaven()

    # Public library index is published only after every file download and validation succeeded.
    index = {
        "schema_version":1,"name":"TS Digitais Visual Library","version":"v1",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "public_licenses":["CC0-1.0","MIT"],"private_content_excluded":True,
        "asset_count":len(ASSETS),"file_count":len(FILES),
        "total_bytes":sum(x["size_bytes"] for x in FILES.values()),
        "collections":COLLECTIONS,
        "assets":ASSETS,
        "files":[{k:v for k,v in f.items() if k not in ("path",)} for f in FILES.values()]
    }
    catalog_dir=WORK/"catalog";catalog_dir.mkdir(exist_ok=True)
    index_path=catalog_dir/"index.json"
    index_path.write_text(json.dumps(index,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    if index_path.stat().st_size>MAX_FILE_BYTES:
        raise RuntimeError("Search catalogue exceeds Worker upload size limit.")
    # Load user-authored HTML page from this repository.
    html_path=ROOT/"index.html"
    if not html_path.exists():
        raise RuntimeError("Online catalog HTML was not checked into the repository.")
    license_dir=catalog_dir/"licenses";license_dir.mkdir(exist_ok=True)
    license_text="""# Public visual library licences

Only CC0 1.0 and MIT assets are included in this public bucket. The per-asset licence and source URL are present in catalog/index.json.

- Kitbitz, AssetPolish selected collections, Open Doodles, selected Open Peeps files and Poly Haven textures: CC0 1.0.
- IRA Design / Creative Tim: MIT. The original copyright and permission notice is retained in IRA-DESIGN-MIT-LICENSE.md.

CC0/MIT copyright permissions do not grant trademark, patent, property, privacy, publicity, model, endorsement or other third-party rights. Generic illustrations must not be presented as actual Guardian clients, staff, installations, or Intelbras equipment.

Private Creative Market content, fonts, archives and assets with licence-pending status are excluded.
"""
    (license_dir/"PUBLIC-ASSET-LICENSES.md").write_text(license_text,encoding="utf-8")
    mit_url="https://raw.githubusercontent.com/ira-design/ira-illustrations/master/LICENSE.md"
    mit=SESSION.get(mit_url,timeout=(30,60));mit.raise_for_status()
    (license_dir/"IRA-DESIGN-MIT-LICENSE.md").write_bytes(mit.content)

    catalog_uploads=[]
    for path,key,ctype in [
        (index_path,"catalog/index.json","application/json"),
        (html_path,"catalog/index.html","text/html; charset=utf-8"),
        (license_dir/"PUBLIC-ASSET-LICENSES.md","catalog/licenses/PUBLIC-ASSET-LICENSES.md","text/markdown"),
        (license_dir/"IRA-DESIGN-MIT-LICENSE.md","catalog/licenses/IRA-DESIGN-MIT-LICENSE.md","text/markdown")
    ]:
        catalog_uploads.append({"key":key,"path":str(path),"size_bytes":path.stat().st_size,
            "sha256":sha256_file(path),"content_type":ctype})
    all_uploads=list(FILES.values())+catalog_uploads
    print("Prepared",len(ASSETS),"searchable assets and",len(FILES),"source files; total MiB:",
          round(sum(x["size_bytes"] for x in FILES.values())/1024/1024,2),flush=True)

    provider=OidcTokenProvider()
    results=[];errors=[]
    def send(item):
        return upload_one(item,provider)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures={pool.submit(send,x):x for x in all_uploads}
        for n,future in enumerate(concurrent.futures.as_completed(futures),1):
            try: results.append(future.result())
            except Exception as e:
                errors.append({"key":futures[future]["key"],"error":str(e)})
                if len(errors)>=10:
                    for pending in futures: pending.cancel()
                    break
            if n%250==0 or n==len(all_uploads):
                print("Uploaded",n,"/",len(all_uploads),"failed",len(errors),flush=True)
    if errors:
        raise RuntimeError("Upload incomplete; first errors: "+json.dumps(errors[:10],ensure_ascii=False))

    # End-to-end online verification.
    health=SESSION.get(BASE_URL+"/health",timeout=40);health.raise_for_status()
    health_json=health.json()
    if health_json.get("asset_count")!=len(ASSETS) or health_json.get("file_count")!=len(FILES):
        raise RuntimeError("Published Worker counts do not match local manifest: "+json.dumps(health_json))
    search=SESSION.get(BASE_URL+"/api/search",params={"q":"character","limit":8},timeout=40);search.raise_for_status()
    search_json=search.json()
    if not search_json.get("results"):
        raise RuntimeError("Online API returned zero character search results.")
    mcp=SESSION.post(BASE_URL+"/mcp",json={"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}},
        headers={"MCP-Protocol-Version":"2025-03-26","Accept":"application/json"},timeout=40)
    mcp.raise_for_status()
    if "search_visual_assets" not in mcp.text:
        raise RuntimeError("Remote MCP tools/list did not expose search_visual_assets.")
    first=search_json["results"][0]
    file_check=SESSION.head(first["file_url"],timeout=40)
    if not file_check.ok:
        raise RuntimeError("Master asset URL is not publicly reachable: "+first["file_url"])
    report={
        "completed_at":datetime.now(timezone.utc).isoformat(),
        "worker":BASE_URL,"service":"ts-visual-library",
        "asset_count":len(ASSETS),"file_count":len(FILES),
        "source_bytes":sum(x["size_bytes"] for x in FILES.values()),
        "collections":COLLECTIONS,"upload_count":len(results),
        "health":health_json,"search_test":{"query":"character","results":len(search_json["results"])},
        "mcp_tools_list_status":mcp.status_code,
        "public_asset_head":{"status":file_check.status_code,"content_type":file_check.headers.get("content-type"),"content_length":file_check.headers.get("content-length")},
        "private_creative_market_excluded":True,"license_pending_files_uploaded":0
    }
    (WORK/"sync-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    (ROOT/"sync-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)

if __name__=="__main__":
    main()
