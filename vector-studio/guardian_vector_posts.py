from __future__ import annotations
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
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1080, 1350
NAVY = "#04344C"
RED = "#CB3033"
SLATE = "#506A76"
CYAN = "#00FFFF"
WHITE = "#FFFFFF"
INK = "#061C2A"
MAX_IMAGE_BYTES = 20 * 1024 * 1024
CLOUDINARY_HOST = "res.cloudinary.com"
CLOUDINARY_NAME = "dhfek3urm"

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_cloudinary_url(url: str) -> bool:
    p = urlparse(url)
    return (
        p.scheme == "https"
        and p.hostname == CLOUDINARY_HOST
        and not p.username and not p.password
        and p.port in (None, 443)
        and p.path.startswith(f"/{CLOUDINARY_NAME}/image/upload/")
    )

def fetch_bytes(url: str, label: str) -> bytes:
    if not safe_cloudinary_url(url):
        raise ValueError(f"URL de {label} fora da biblioteca Cloudinary aprovada.")
    response = requests.get(
        url, timeout=(15, 60), allow_redirects=False,
        headers={"User-Agent": "TS-Digitais-Guardian-Visual-Studio/2.0", "Accept": "image/png,image/jpeg"}
    )
    response.raise_for_status()
    data = response.content
    if not data or len(data) > MAX_IMAGE_BYTES:
        raise ValueError(f"Arquivo de {label} vazio ou acima do limite de 20 MB.")
    return data

def load_logo(url: str) -> tuple[str, dict]:
    raw = fetch_bytes(url, "logo")
    if not raw.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("O logo não possui assinatura PNG válida.")
    with Image.open(io.BytesIO(raw)) as im:
        im.verify()
    with Image.open(io.BytesIO(raw)) as im:
        if im.size != (192, 50):
            raise ValueError(f"Dimensões inesperadas do logo oficial: {im.size}; esperado 192x50.")
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii"), {
        "source_url": url, "format": "PNG", "dimensions": [192, 50],
        "bytes": len(raw), "sha256": sha256(raw), "embedded_unchanged": True
    }

def prepare_photo(post: dict) -> tuple[str, dict]:
    url = post["image_url"]
    raw = fetch_bytes(url, post["slug"])
    with Image.open(io.BytesIO(raw)) as im:
        im.verify()
    with Image.open(io.BytesIO(raw)) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        source_dimensions = list(image.size)
        box = post["photo_box"]
        width, height = int(box["width"]), int(box["height"])
        centering = tuple(post.get("centering", [0.5, 0.5]))
        crop = ImageOps.fit(
            image, (width, height),
            method=Image.Resampling.LANCZOS,
            centering=centering
        )
        buf = io.BytesIO()
        crop.save(buf, format="JPEG", quality=94, subsampling=0, optimize=True)
        cropped = buf.getvalue()
    if not cropped.startswith(b"\xff\xd8\xff"):
        raise ValueError("A fotografia preparada não tem assinatura JPEG válida.")
    return "data:image/jpeg;base64," + base64.b64encode(cropped).decode("ascii"), {
        "source_url": url,
        "source_public_id": post.get("source_public_id"),
        "source_dimensions": source_dimensions,
        "embedded_dimensions": [width, height],
        "source_sha256": sha256(raw),
        "embedded_sha256": sha256(cropped),
        "bytes_source": len(raw),
        "bytes_embedded": len(cropped),
        "rights_note": "Asset existente na biblioteca Cloudinary da Guardian, identificado como Pexels. Foto ilustrativa; origem/licença específica não revalidada neste job."
    }

def font_file() -> str:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
    ]
    for p in candidates:
        if Path(p).exists():
            return p
    raise FileNotFoundError("Fonte sans-serif bold do runner não encontrada.")

def fit_size(value: str, start: int, max_width: int, min_size: int = 42) -> int:
    path = font_file()
    size = start
    while size > min_size:
        f = ImageFont.truetype(path, size=size)
        if f.getlength(value) <= max_width:
            return size
        size -= 1
    f = ImageFont.truetype(path, size=min_size)
    if f.getlength(value) > max_width:
        raise ValueError(f"Headline não cabe no espaço reservado: {value!r}")
    return min_size

def title_line(x: int, y: int, value: str, size: int, width: int, color: str = WHITE, spacing: int = -3) -> str:
    actual = fit_size(value, size, width)
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans,Arial,sans-serif" '
        f'font-size="{actual}" font-weight="800" letter-spacing="{spacing}">{esc(value)}</text>'
    )

def small_line(x: int, y: int, value: str, size: int = 25, color: str = WHITE, weight: int = 500, spacing: float = 0) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans,Arial,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{esc(value)}</text>'
    )

def logo_plate(logo: str, x: int, y: int, w: int = 310, h: int = 82) -> str:
    # The source mark is embedded byte-for-byte; the white plate is only a contrast field.
    ix = x + 18
    iy = y + 10
    iw = w - 36
    ih = h - 20
    return (
        f'<g id="official-logo-lockup">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#FFFFFF"/>'
        f'<image x="{ix}" y="{iy}" width="{iw}" height="{ih}" preserveAspectRatio="xMidYMid meet" href="{logo}"/>'
        f'</g>'
    )

def photo_image(uri: str, box: dict, clip_id: str = "photo-clip") -> str:
    return (
        f'<g id="photographic-hero" clip-path="url(#{clip_id})">'
        f'<image x="{box["x"]}" y="{box["y"]}" width="{box["width"]}" height="{box["height"]}" '
        f'preserveAspectRatio="none" href="{uri}"/></g>'
    )

def compose_svg(post: dict, logo: str, photo: str) -> str:
    slug = re.sub(r"[^a-z0-9-]", "-", post["slug"].lower())
    box = post["photo_box"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{slug}-title {slug}-desc">',
        f'<title id="{slug}-title">Guardian — {esc(post["name"])}</title>',
        f'<desc id="{slug}-desc">{esc(post["alt_text"])}</desc>',
        '<defs>',
        f'<clipPath id="photo-clip"><rect x="{box["x"]}" y="{box["y"]}" width="{box["width"]}" height="{box["height"]}"/></clipPath>',
        '<linearGradient id="dark-left" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#031724" stop-opacity=".98"/><stop offset=".62" stop-color="#031724" stop-opacity=".88"/><stop offset="1" stop-color="#031724" stop-opacity=".12"/></linearGradient>',
        '<linearGradient id="photo-top-shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#031724" stop-opacity=".48"/><stop offset=".55" stop-color="#031724" stop-opacity="0"/><stop offset="1" stop-color="#031724" stop-opacity=".2"/></linearGradient>',
        '<linearGradient id="bottom-dark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#031724" stop-opacity="0"/><stop offset=".5" stop-color="#031724" stop-opacity=".82"/><stop offset="1" stop-color="#031724" stop-opacity=".98"/></linearGradient>',
        '</defs>'
    ]

    layout = post["layout"]
    if layout == "portaria":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo, box),
            '<rect width="820" height="1350" fill="url(#dark-left)"/>',
            logo_plate(logo, 72, 64, 310, 82),
            small_line(74, 256, "PORTARIA REMOTA 24H", 21, "#D6E4E9", 700, 2.6),
            '<rect x="72" y="278" width="58" height="5" rx="2.5" fill="#CB3033"/>',
            title_line(70, 450, "A ROTINA", 118, 510, WHITE, -4),
            title_line(70, 574, "NÃO PARA.", 124, 540, RED, -4),
            small_line(74, 668, "Controle de acesso integrado", 27, WHITE, 500),
            small_line(74, 710, "à dinâmica do condomínio.", 27, WHITE, 500),
            small_line(74, 1190, "CONVERSE COM A GUARDIAN", 23, WHITE, 800, 1.4),
            '<path d="M74 1218H340" stroke="#00FFFF" stroke-width="3"/>',
            small_line(74, 1280, "FLORIANÓPOLIS • GRANDE FLORIANÓPOLIS", 16, "#C0D3DC", 700, 1.2)
        ]
    elif layout == "alarme":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo, box),
            '<rect x="0" y="0" width="1080" height="760" fill="url(#photo-top-shade)"/>',
            '<path d="M0 686C250 728 580 744 1080 660V1350H0Z" fill="#04344C"/>',
            '<path d="M0 686C250 728 580 744 1080 660" fill="none" stroke="#CB3033" stroke-width="7"/>',
            logo_plate(logo, 72, 755, 290, 76),
            small_line(74, 904, "MONITORAMENTO DE ALARME 24H", 20, "#D6E4E9", 700, 2.0),
            title_line(70, 1030, "O ALERTA", 100, 910, WHITE, -4),
            title_line(70, 1130, "CHEGA À CENTRAL.", 92, 940, RED, -3),
            small_line(74, 1197, "Eventos recebidos e acompanhados pela central.", 24, WHITE, 500),
            small_line(74, 1283, "FALE COM A GUARDIAN", 22, WHITE, 800, 1.5),
            '<path d="M74 1307H314" stroke="#00FFFF" stroke-width="3"/>'
        ]
    elif layout == "imagem":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo, box),
            '<rect x="0" y="0" width="1080" height="220" fill="#04344C"/>',
            logo_plate(logo, 72, 58, 310, 82),
            small_line(620, 170, "MONITORAMENTO DE IMAGEM 24H", 20, "#D6E4E9", 700, 1.5),
            '<path d="M0 922L1080 880" stroke="#CB3033" stroke-width="9"/>',
            '<path d="M0 934L1080 892" stroke="#FFFFFF" stroke-opacity=".23" stroke-width="2"/>',
            small_line(74, 1022, "MONITORAMENTO E ANÁLISE DE EVENTOS", 18, "#C8DCE4", 700, 1.8),
            title_line(70, 1128, "IMAGEM EM FOCO.", 100, 950, WHITE, -4),
            small_line(74, 1195, "Câmeras integradas à operação da central 24h.", 25, WHITE, 500),
            small_line(74, 1280, "FALE COM A GUARDIAN", 22, WHITE, 800, 1.4),
            '<path d="M74 1307H320" stroke="#00FFFF" stroke-width="3"/>'
        ]
    elif layout == "manutencao":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo, box),
            '<path d="M570 0H690L610 1350H520Z" fill="#CB3033"/>',
            '<path d="M690 0H710L630 1350H610Z" fill="#FFFFFF" opacity=".13"/>',
            logo_plate(logo, 665, 64, 340, 82),
            small_line(662, 274, "MANUTENÇÃO PREVENTIVA E CORRETIVA", 15, "#D6E4E9", 700, .5),
            '<rect x="662" y="296" width="52" height="5" rx="2.5" fill="#CB3033"/>',
            title_line(658, 480, "SISTEMA", 94, 370, WHITE, -3),
            title_line(658, 600, "EM DIA.", 102, 390, RED, -4),
            small_line(662, 730, "Preventiva e corretiva", 24, WHITE, 500),
            small_line(662, 770, "em sistemas de segurança.", 24, WHITE, 500),
            small_line(662, 1185, "SOLICITE UMA AVALIAÇÃO", 19, WHITE, 800, .8),
            small_line(662, 1222, "TÉCNICA COM A GUARDIAN", 19, WHITE, 800, .8),
            '<path d="M662 1252H938" stroke="#00FFFF" stroke-width="3"/>',
            small_line(662, 1302, "FLORIANÓPOLIS E REGIÃO", 14, "#C0D3DC", 700, .8)
        ]
    else:
        raise ValueError(f"Layout desconhecido: {layout}")

    parts += ['</svg>']
    return "\n".join(parts)

def validate_svg(svg_path: Path, logo_uri: str, photo_uri: str) -> dict:
    raw = svg_path.read_text(encoding="utf-8")
    root = ET.fromstring(raw)
    images = [node for node in root.iter() if node.tag.endswith("image")]
    logo_images = [node for node in images if (node.attrib.get("href") or "").startswith("data:image/png;base64,")]
    photo_images = [node for node in images if (node.attrib.get("href") or "").startswith("data:image/jpeg;base64,")]
    if len(logo_images) != 1 or len(photo_images) != 1:
        raise ValueError(f"Quantidade de assets incorporados incorreta em {svg_path.name}.")
    if logo_images[0].attrib.get("href") != logo_uri or photo_images[0].attrib.get("href") != photo_uri:
        raise ValueError(f"URI de asset alterada em {svg_path.name}.")
    logo_bytes = base64.b64decode(logo_uri.split(",", 1)[1], validate=True)
    photo_bytes = base64.b64decode(photo_uri.split(",", 1)[1], validate=True)
    if not logo_bytes.startswith(b"\x89PNG\r\n\x1a\n") or not photo_bytes.startswith(b"\xff\xd8\xff"):
        raise ValueError("Assinatura binária de imagem incorporada inválida.")
    return {
        "xml_valid": True, "embedded_image_count": len(images),
        "embedded_logo_count": 1, "embedded_photo_count": 1,
        "logo_sha256": sha256(logo_bytes), "photo_sha256": sha256(photo_bytes)
    }

def render_guardian_vector_posts(request: dict, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    logo_uri, logo_meta = load_logo(request["logo"]["url"])
    report_posts = []
    preview_items = []
    captions = []
    for post in request["posts"]:
        photo_uri, photo_meta = prepare_photo(post)
        svg = compose_svg(post, logo_uri, photo_uri)
        slug = post["slug"]
        svg_path = out_dir / f"{slug}.svg"
        png_path = out_dir / f"{slug}.png"
        svg_path.write_text(svg, encoding="utf-8")
        validation = validate_svg(svg_path, logo_uri, photo_uri)
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=W, output_height=H)
        with Image.open(png_path) as test:
            test.verify()
        with Image.open(png_path) as im:
            if im.size != (W, H):
                raise ValueError(f"Dimensões incorretas em {png_path.name}: {im.size}")
            if im.mode not in ("RGB", "RGBA"):
                im.convert("RGB").save(png_path, format="PNG", optimize=True)
            thumb = im.convert("RGB")
            thumb.thumbnail((270, 338), Image.Resampling.LANCZOS)
            preview_items.append((slug, thumb.copy()))
        caption = post["caption"].strip().replace("\\n", "\n")
        (out_dir / f"{slug}-caption.md").write_text(caption + "\n", encoding="utf-8")
        (out_dir / f"{slug}-alt.txt").write_text(post["alt_text"] + "\n", encoding="utf-8")
        report_posts.append({
            "name": post["name"], "slug": slug, "layout": post["layout"],
            "width": W, "height": H, "svg_bytes": svg_path.stat().st_size,
            "png_bytes": png_path.stat().st_size, "svg_and_image_validation": validation,
            "photo": photo_meta
        })
        captions.append(f"## {post['name']}\n\n{caption}\n")
    sheet = Image.new("RGB", (4 * 285 + 50, 390), (4, 25, 38))
    draw = ImageDraw.Draw(sheet)
    for index, (slug, thumb) in enumerate(preview_items):
        x = 15 + index * 285
        sheet.paste(thumb, (x, 8))
        draw.text((x, 352), slug[:33], fill=(236, 244, 247))
    sheet.save(out_dir / "contact-sheet.jpg", format="JPEG", quality=94, optimize=True)
    (out_dir / "captions-all.md").write_text("\n\n".join(captions), encoding="utf-8")
    report = {
        "project": "Guardian social campaign",
        "pipeline": "TS Digitais Vector Studio — SVG híbrido fotorrealista",
        "format": "Instagram Feed 4:5",
        "canvas": [W, H],
        "logo": logo_meta,
        "rendered_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "visual_method": "Fotografia raster original preservada e incorporada por data URI; tipografia, recortes e grafismos em SVG. Não é raster-to-vector nem imagem gerada por IA.",
        "posts": report_posts,
        "quality_checks": {
            "all_svg_xml_valid": True, "one_original_logo_and_one_photo_per_post": True,
            "all_photos_jpeg_signature_valid": True, "all_png_exports_verified": True,
            "all_png_dimensions": [W, H], "captions_and_alt_text_exported": True
        },
        "rights_warning": "Os assets fotográficos já estavam na biblioteca Cloudinary da Guardian e identificados como Pexels; a página de origem/licença específica não foi revalidada neste job. As legendas identificam todas as fotografias como ilustrativas."
    }
    (out_dir / "metadata.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report

def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    request = json.loads(Path(args.request).read_text(encoding="utf-8"))
    report = render_guardian_vector_posts(request, Path(args.out_dir))
    print(json.dumps({
        "status": "success",
        "post_count": len(report["posts"]),
        "logo_sha256": report["logo"]["sha256"],
        "outputs": [{"slug": p["slug"], "png_bytes": p["png_bytes"], "svg_bytes": p["svg_bytes"]} for p in report["posts"]],
        "quality_checks": report["quality_checks"]
    }, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
