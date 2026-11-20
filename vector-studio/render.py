#!/usr/bin/env python3
"""Remote photo + SVG build pipeline for TS Digitais Vector Studio."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import io
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import cairosvg
import requests
import vtracer
from PIL import Image, ImageFont, ImageOps

from agency_campaign import build_guardian_campaign

MAX_SOURCE_BYTES = 25 * 1024 * 1024
ALLOWED_HOSTS = {"images.pexels.com", "www.pexels.com", "pexels.com"}
NAVY = "#04344C"
RED = "#CB3033"
SLATE = "#506A76"
CYAN = "#00FFFF"
WHITE = "#FFFFFF"


def safe_text(value: str) -> str:
    return html.escape(str(value), quote=True)


def allowed_url(url: str) -> bool:
    parsed = urlparse(url)
    return (
        parsed.scheme == "https"
        and parsed.hostname in ALLOWED_HOSTS
        and not parsed.username
        and not parsed.password
        and parsed.port in (None, 443)
    )


def download_source(url: str, destination: Path) -> bytes:
    current = url
    session = requests.Session()
    for hop in range(5):
        if not allowed_url(current):
            raise ValueError(f"Blocked non-Pexels or unsafe image URL: {current}")
        response = session.get(
            current,
            timeout=(20, 90),
            allow_redirects=False,
            headers={"User-Agent": "TS-Digitais-Vector-Studio/1.0", "Accept": "image/avif,image/webp,image/jpeg,image/png,*/*"},
            stream=True,
        )
        if response.status_code in (301, 302, 303, 307, 308):
            location = response.headers.get("Location")
            if not location:
                raise RuntimeError("Image source returned a redirect without Location.")
            from urllib.parse import urljoin
            current = urljoin(current, location)
            continue
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").split(";")[0].lower()
        chunks = []
        total = 0
        for chunk in response.iter_content(chunk_size=1024 * 512):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_SOURCE_BYTES:
                raise ValueError("Source image exceeded 25 MB.")
            chunks.append(chunk)
        data = b"".join(chunks)
        if not data:
            raise ValueError("Source image was empty.")
        with Image.open(io.BytesIO(data)) as check:
            check.verify()
        with Image.open(io.BytesIO(data)) as raw:
            image = ImageOps.exif_transpose(raw).convert("RGB")
            image.save(destination, format="JPEG", quality=95, subsampling=0, optimize=True)
        normalized = destination.read_bytes()
        with Image.open(io.BytesIO(normalized)) as check:
            check.verify()
        if not normalized.startswith(b"\xff\xd8\xff"):
            raise ValueError(f"Image bytes are not JPEG (source Content-Type: {content_type}).")
        return normalized
    raise RuntimeError("Too many image redirects.")


def font_path(bold: bool = False) -> str:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError("No compatible system sans font found on runner.")


def fit_font_size(text: str, maximum_width: int, initial: int, minimum: int = 28, bold: bool = True) -> int:
    path = font_path(bold)
    size = initial
    while size > minimum:
        font = ImageFont.truetype(path, size=size)
        if font.getlength(text) <= maximum_width:
            return size
        size -= 1
    return minimum


def svg_text(x: int, y: int, value: str, size: int, *, weight: int = 400, color: str = WHITE, letter_spacing: float = 0) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{letter_spacing}">{safe_text(value)}</text>'
    )


def create_artboard(image_uri: str, output: dict, copy: dict, brand: dict, source_page: str, photographer: str) -> str:
    width, height = int(output["width"]), int(output["height"])
    layout = output["layout"]
    margin = 64
    inner_width = width - margin * 2

    if layout == "feed":
        photo_y, photo_h = 465, 600
        brand_y, kicker_y = 100, 190
        headline_y = [295, 385]
        headline_size = 78
        support_y = [1160, 1205]
        support_size = 30
        cta_y, cta_h, cta_w, cta_font = 1250, 62, 386, 27
    elif layout == "story":
        photo_y, photo_h = 535, 930
        brand_y, kicker_y = 112, 230
        headline_y = [352, 448]
        headline_size = 84
        support_y = [1550, 1604]
        support_size = 32
        cta_y, cta_h, cta_w, cta_font = 1690, 72, 430, 29
    elif layout == "square":
        photo_y, photo_h = 350, 470
        brand_y, kicker_y = 72, 145
        headline_y = [235, 315]
        headline_size = 68
        support_y = [870, 912]
        support_size = 25
        cta_y, cta_h, cta_w, cta_font = 960, 58, 360, 24
    else:
        raise ValueError(f"Unknown layout: {layout}")

    headline = copy["headline"]
    support = copy["support"]
    headline_size = min(
        fit_font_size(headline[0], inner_width - 16, headline_size, bold=True),
        fit_font_size(headline[1], inner_width - 16, headline_size, bold=True),
    )
    support_size = min(
        fit_font_size(support[0], inner_width, support_size, minimum=20, bold=False),
        fit_font_size(support[1], inner_width, support_size, minimum=20, bold=False),
    )
    kicker_size = 20 if layout != "square" else 17
    brand_size = 40 if layout != "square" else 34
    x = margin
    photo_x = 40
    photo_w = width - 80
    radius = 28 if width > 1080 else 24
    photo_bottom = photo_y + photo_h
    line_y = photo_bottom + (16 if layout == "square" else 32)

    # Gradients keep the photography readable without flattening the actual photo.
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<title>Guardian — O acesso é diário. O controle também.</title>",
        f"<desc>Peça institucional para condomínios com fotografia de banco de imagens de {safe_text(photographer)}. Foto ilustrativa, não representa instalação Guardian.</desc>",
        "<defs>",
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#032B40"/><stop offset="1" stop-color="#062F45"/></linearGradient>',
        '<linearGradient id="photoShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#031C2A" stop-opacity="0"/><stop offset="0.72" stop-color="#031C2A" stop-opacity="0.04"/><stop offset="1" stop-color="#031C2A" stop-opacity="0.22"/></linearGradient>',
        f'<clipPath id="photoClip"><rect x="{photo_x}" y="{photo_y}" width="{photo_w}" height="{photo_h}" rx="{radius}"/></clipPath>',
        "</defs>",
        f'<rect width="{width}" height="{height}" fill="url(#bg)"/>',
        # Quiet brand geometry, not a generic security icon.
        f'<rect x="{margin}" y="{brand_y-33}" width="8" height="48" rx="4" fill="{RED}"/>',
        svg_text(margin + 24, brand_y, brand["name"], brand_size, weight=700, color=WHITE),
        f'<line x1="{margin}" y1="{kicker_y-28}" x2="{margin+48}" y2="{kicker_y-28}" stroke="{CYAN}" stroke-width="3"/>',
        svg_text(margin, kicker_y, copy["kicker"], kicker_size, weight=700, color="#B7D6E2", letter_spacing=2.2),
        svg_text(margin, headline_y[0], headline[0], headline_size, weight=700, color=WHITE, letter_spacing=-2.1),
        svg_text(margin, headline_y[1], headline[1], headline_size, weight=700, color=WHITE, letter_spacing=-2.1),
        f'<image x="{photo_x}" y="{photo_y}" width="{photo_w}" height="{photo_h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip)" href="{image_uri}"/>',
        f'<rect x="{photo_x}" y="{photo_y}" width="{photo_w}" height="{photo_h}" rx="{radius}" fill="url(#photoShade)"/>',
        # Fine frame detail and a restrained red corner marker.
        f'<rect x="{photo_x}" y="{photo_y}" width="{photo_w}" height="{photo_h}" rx="{radius}" fill="none" stroke="#A6B8C2" stroke-opacity="0.32" stroke-width="1.5"/>',
        f'<rect x="{photo_x+photo_w-54}" y="{photo_y+photo_h-10}" width="28" height="4" rx="2" fill="{RED}"/>',
        f'<line x1="{margin}" y1="{line_y}" x2="{margin+92}" y2="{line_y}" stroke="{CYAN}" stroke-width="3"/>',
        svg_text(margin, support_y[0], support[0], support_size, weight=500, color=WHITE),
        svg_text(margin, support_y[1], support[1], support_size, weight=500, color=WHITE),
        f'<rect x="{margin}" y="{cta_y}" width="{cta_w}" height="{cta_h}" rx="{int(cta_h/2)}" fill="{RED}"/>',
        svg_text(margin+28, cta_y+int(cta_h*0.66), copy["cta"], cta_font, weight=700, color=WHITE),
        f'<text x="{width-margin}" y="{height-28}" text-anchor="end" fill="#B7D6E2" opacity="0.72" font-family="DejaVu Sans, Arial, sans-serif" font-size="16" letter-spacing="2">GUARDIAN</text>',
        "</svg>",
    ]
    return "\n".join(svg)


def render_svg(svg_path: Path, png_path: Path, width: int, height: int) -> None:
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width, output_height=height)
    with Image.open(png_path) as image:
        image.verify()
    with Image.open(png_path) as image:
        if image.size != (width, height):
            raise RuntimeError(f"PNG dimensions mismatch: {image.size}, expected {(width, height)}")
        if image.mode not in ("RGB", "RGBA"):
            image.convert("RGB").save(png_path, format="PNG", optimize=True)


def validate_hybrid(svg_path: Path, expected_jpeg_sha: str) -> dict:
    data = svg_path.read_text(encoding="utf-8")
    root = ET.fromstring(data)
    images = [el for el in root.iter() if el.tag.endswith("image")]
    if len(images) != 1:
        raise RuntimeError(f"Expected exactly one embedded photograph, found {len(images)}")
    href = images[0].attrib.get("href") or images[0].attrib.get("{http://www.w3.org/1999/xlink}href")
    if not href or not href.startswith("data:image/jpeg;base64,"):
        raise RuntimeError("Photo is not embedded as a JPEG data URI.")
    decoded = base64.b64decode(href.split(",", 1)[1], validate=True)
    if not decoded.startswith(b"\xff\xd8\xff"):
        raise RuntimeError("Embedded image does not have a JPEG signature.")
    sha = hashlib.sha256(decoded).hexdigest()
    if sha != expected_jpeg_sha:
        raise RuntimeError("Embedded source hash differs from normalized source photo.")
    return {"xml_valid": True, "embedded_photo_count": 1, "embedded_photo_mime": "image/jpeg", "embedded_photo_sha256": sha}


def vectorize_photo(photo_bytes: bytes, trace_request: dict, out_dir: Path, metadata: dict) -> None:
    with Image.open(io.BytesIO(photo_bytes)) as image:
        image = image.convert("RGB")
        max_width = int(trace_request.get("max_width", 1400))
        if image.width > max_width:
            new_height = round(image.height * max_width / image.width)
            image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
        image_buffer = io.BytesIO()
        image.save(image_buffer, format="PNG", optimize=True)
        input_png = image_buffer.getvalue()
        cfg = vtracer.Config.photo()
        cfg.mode = "spline"
        cfg.hierarchical = "stacked"
        cfg.max_colors = int(trace_request.get("max_colors", 96))
        cfg.filter_speckle = int(trace_request.get("filter_speckle", 2))
        cfg.simplify = float(trace_request.get("simplify", 0.8))
        cfg.path_precision = int(trace_request.get('path_precision', 2))
        cfg.optimize = 2
        started = time.time()
        trace_svg = cfg.convert_bytes(input_png)
        elapsed = round(time.time() - started, 2)
        if not isinstance(trace_svg, str):
            raise TypeError("VTracer Config.convert_bytes did not return SVG text.")
        trace_path = out_dir / "guardian-photo-vector-trace.svg"
        trace_path.write_text(trace_svg, encoding="utf-8")
        ET.parse(trace_path)
        png_path = out_dir / "guardian-photo-vector-trace.png"
        cairosvg.svg2png(url=str(trace_path), write_to=str(png_path), output_width=image.width, output_height=image.height)
        with Image.open(png_path) as check:
            check.verify()
        metadata["vector_trace"] = {
            "status": "success",
            "engine": f"VTracer {getattr(vtracer, '__version__', '1.0.0-alpha.4')}",
            "configuration": {
                "preset": "Config.photo()",
                "mode": "spline",
                "hierarchical": "stacked",
                "max_colors": cfg.max_colors,
                "filter_speckle": cfg.filter_speckle,
                "simplify": cfg.simplify,
                "path_precision": cfg.path_precision,
                "optimize": cfg.optimize
            },
            "input_dimensions": [image.width, image.height],
            "duration_seconds": elapsed,
            "svg_bytes": trace_path.stat().st_size,
            "png_bytes": png_path.stat().st_size,
            "note": "The source photograph is converted into stacked SVG paths. The campaign master uses vector paths, not an embedded raster photo."
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    request_path = Path(args.request)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    request = json.loads(request_path.read_text(encoding="utf-8"))
    source = request["source"]
    if not allowed_url(source["image_url"]):
        raise ValueError("Only a public Pexels image URL is accepted.")
    photo_file = out_dir / "source-photo.jpg"
    photo_bytes = download_source(source["image_url"], photo_file)
    with Image.open(io.BytesIO(photo_bytes)) as photo:
        width, height = photo.size
        if width < 1000 or height < 700:
            raise ValueError(f"Source photo resolution too low: {width}x{height}")
    photo_sha = hashlib.sha256(photo_bytes).hexdigest()
    image_uri = "data:image/jpeg;base64," + base64.b64encode(photo_bytes).decode("ascii")
    copy = request["copy"]
    brand = request["brand"]
    metadata = {
        "project": request.get("project"),
        "campaign": request.get("campaign"),
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {
            "page_url": source.get("page_url"),
            "image_url": source.get("image_url").split("?", 1)[0],
            "photographer": source.get("photographer"),
            "license": source.get("license"),
            "use_note": source.get("use_note"),
            "normalized_file": photo_file.name,
            "dimensions": [width, height],
            "sha256": photo_sha
        },
        "brand": brand,
        "outputs": [],
        "quality_checks": {
            "source_downloaded": True,
            "source_signature_jpeg": photo_bytes.startswith(b"\xff\xd8\xff"),
            "source_dimensions": [width, height],
            "hybrid_svg_has_one_embedded_photo": True,
            "svg_xml_validated": True,
            "png_exports_rendered_and_dimension_checked": True
        }
    }
    vector_campaign = request.get("art_direction") == "agency_vector_campaign"
    trace_svg_text = None
    if vector_campaign:
        # Convert the real source photograph into SVG paths before building the campaign.
        vectorize_photo(photo_bytes, request.get("trace", {}), out_dir, metadata)
        trace_svg_text = (out_dir / "guardian-photo-vector-trace.svg").read_text(encoding="utf-8")
        metadata["quality_checks"]["hybrid_svg_has_one_embedded_photo"] = False
        metadata["quality_checks"]["campaign_uses_vector_paths_not_raster"] = True

    for output in request["outputs"]:
        name = re.sub(r"[^a-zA-Z0-9_-]+", "-", output["name"])
        svg_path = out_dir / f"{name}.svg"
        png_path = out_dir / f"{name}.png"
        if vector_campaign:
            svg = build_guardian_campaign(
                trace_svg_text, output, copy, brand,
                source.get("page_url", ""), source.get("photographer", "Pexels")
            )
            svg_path.write_text(svg, encoding="utf-8")
            root = ET.parse(svg_path).getroot()
            path_count = sum(1 for element in root.iter() if element.tag.endswith("path"))
            image_count = sum(1 for element in root.iter() if element.tag.endswith("image"))
            if path_count < 1000:
                raise RuntimeError(f"Vector campaign contains too few paths: {path_count}")
            if image_count:
                raise RuntimeError(f"Vector campaign unexpectedly contains {image_count} raster image elements.")
            validation = {
                "xml_valid": True,
                "vector_path_count": path_count,
                "raster_image_elements": image_count,
                "photo_trace_included_as_nested_svg": True
            }
        else:
            svg = create_artboard(image_uri, output, copy, brand, source.get("page_url", ""), source.get("photographer", "Pexels"))
            svg_path.write_text(svg, encoding="utf-8")
            validation = validate_hybrid(svg_path, photo_sha)
        render_svg(svg_path, png_path, int(output["width"]), int(output["height"]))
        metadata["outputs"].append({
            "name": name,
            "width": int(output["width"]),
            "height": int(output["height"]),
            "layout": output["layout"],
            "svg_bytes": svg_path.stat().st_size,
            "png_bytes": png_path.stat().st_size,
            "validation": validation
        })
    caption = copy["caption"].strip()
    (out_dir / "caption.md").write_text(
        caption + "\n\n#Guardian #Condomínios #PortariaRemota #ControleDeAcesso #Florianópolis\n",
        encoding="utf-8"
    )
    (out_dir / "alt-text.txt").write_text(
        request.get("alt_text", "Arte da Guardian sobre portaria remota e controle de acesso. Cena ilustrativa vetorizada a partir de fotografia de banco de imagens; não representa uma instalação real da Guardian."),
        encoding="utf-8"
    )
    if request.get("trace", {}).get("enabled") and not vector_campaign:
        try:
            vectorize_photo(photo_bytes, request["trace"], out_dir, metadata)
        except Exception as exc:
            metadata["vector_trace"] = {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}
            print(f"WARNING: VTracer experiment failed; hybrid masters remain valid: {exc}", file=sys.stderr)
    report = {
        "pipeline": "TS Digitais Vector Studio",
        "runtime": "GitHub Actions Ubuntu 24.04 / Python 3.12",
        "vtracer_version": getattr(vtracer, "__version__", "1.0.0-alpha.4"),
        **metadata
    }
    (out_dir / "metadata.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "success",
        "source": [width, height],
        "rendered_outputs": len(metadata["outputs"]),
        "vector_trace": metadata.get("vector_trace", {}).get("status", "disabled"),
        "files": sorted(p.name for p in out_dir.iterdir())
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
