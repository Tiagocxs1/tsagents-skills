from __future__ import annotations
import base64
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import cairosvg
import requests
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps

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

def recolor_logo_white(raw: bytes) -> bytes:
    """Create a white, transparent variant from the original grey logo pixels."""
    with Image.open(io.BytesIO(raw)) as source:
        rgba = source.convert("RGBA")
    luminance = ImageOps.grayscale(rgba.convert("RGB"))
    original_alpha = rgba.getchannel("A")
    values = list(luminance.getdata())
    ink_values = [value for value in values if value < 248]
    if not ink_values:
        raise ValueError("Não foi possível separar o desenho do fundo do logo original.")
    darkest = min(ink_values)
    threshold = 250
    if darkest >= threshold:
        raise ValueError("Contraste insuficiente no logo original para gerar a versão branca.")
    scale = max(1, threshold - darkest)
    mask = luminance.point(
        lambda value: 0 if value >= threshold else max(0, min(255, round((threshold - value) * 255 / scale)))
    )
    if original_alpha.getextrema() != (255, 255):
        mask = ImageChops.multiply(mask, original_alpha)
    # The source artwork is grey; normalize its strongest logo pixel to full opacity.
    # This makes the recolored mark truly white while retaining anti-aliased contours.
    maximum_alpha = mask.getextrema()[1]
    if maximum_alpha <= 0:
        raise ValueError("Não foi possível extrair pixels visíveis do logo original.")
    mask = mask.point(lambda value: min(255, round(value * 255 / maximum_alpha)))
    white = Image.new("RGBA", rgba.size, (255, 255, 255, 0))
    white.putalpha(mask)
    buffer = io.BytesIO()
    white.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()


def load_logo(url: str) -> tuple[str, str, dict, bytes]:
    raw = fetch_bytes(url, "logo")
    if not raw.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("O logo não possui assinatura PNG válida.")
    with Image.open(io.BytesIO(raw)) as im:
        im.verify()
    with Image.open(io.BytesIO(raw)) as im:
        if im.size != (192, 50):
            raise ValueError(f"Dimensões inesperadas do logo oficial: {im.size}; esperado 192x50.")
    white_bytes = recolor_logo_white(raw)
    original_uri = "data:image/png;base64," + base64.b64encode(raw).decode("ascii")
    white_uri = "data:image/png;base64," + base64.b64encode(white_bytes).decode("ascii")
    with Image.open(io.BytesIO(white_bytes)) as white_check:
        white_check.load()
        if white_check.size != (192, 50) or white_check.mode != "RGBA":
            raise ValueError("A versão branca do logo não preservou dimensões/transparência.")
        alpha_min = white_check.getchannel("A").getextrema()[0]
    if alpha_min == 255:
        raise ValueError("A versão branca do logo parece ter perdido a transparência.")
    return original_uri, white_uri, {
        "source_url": url,
        "format": "PNG",
        "dimensions": [192, 50],
        "bytes": len(raw),
        "sha256": sha256(raw),
        "embedded_unchanged": True,
        "white_variant": {
            "method": "recolor original luminance to white; convert white background to alpha; preserve anti-aliased contours",
            "format": "PNG",
            "dimensions": [192, 50],
            "bytes": len(white_bytes),
            "sha256": sha256(white_bytes),
            "fill": "#FFFFFF",
            "background": "transparent"
        }
    }, white_bytes

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


FONT_SOURCES = {
    "Oswald": {
        "url": "https://raw.githubusercontent.com/google/fonts/main/ofl/oswald/Oswald%5Bwght%5D.ttf",
        "file": "Oswald[wght].ttf"
    },
    "Manrope": {
        "url": "https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/Manrope%5Bwght%5D.ttf",
        "file": "Manrope[wght].ttf"
    }
}


def prepare_campaign_fonts(out_dir: Path) -> dict:
    """Download OFL display/body families and register them with Fontconfig."""
    font_dir = Path.home() / ".local" / "share" / "fonts" / "guardian-social"
    font_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for family, item in FONT_SOURCES.items():
        target = font_dir / item["file"]
        response = requests.get(item["url"], timeout=(20, 90), allow_redirects=True)
        response.raise_for_status()
        data = response.content
        if len(data) < 50000 or not (data.startswith(b"\x00\x01\x00\x00") or data.startswith(b"OTTO")):
            raise ValueError(f"Arquivo TTF inválido ou inesperado para {family}.")
        target.write_bytes(data)
        paths[family] = str(target)
    subprocess.run(["fc-cache", "-f", str(font_dir)], check=True, capture_output=True, text=True)
    for family in FONT_SOURCES:
        match = subprocess.run(
            ["fc-match", "-f", "%{family}", family],
            check=True, capture_output=True, text=True
        ).stdout
        if family.lower() not in match.lower():
            raise RuntimeError(f"Fontconfig não está usando a fonte {family}: {match}")
    (out_dir / "campaign-font-licenses.txt").write_text(
        "Tipografia de campanha (escolha criativa provisória; não é tipografia oficial Guardian):\n"
        "Oswald — variável, arquivos do Google Fonts; SIL Open Font License 1.1.\n"
        "Manrope — variável, arquivos do Google Fonts; SIL Open Font License 1.1.\n"
        "Fontes e licenças: https://github.com/google/fonts/tree/main/ofl/oswald e "
        "https://github.com/google/fonts/tree/main/ofl/manrope\n",
        encoding="utf-8"
    )
    return paths


def font_for_measurement(path: str, size: int, weight: int) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(path, size=size)
    try:
        axes = font.get_variation_axes()
        values = [axis.get("default", 400) for axis in axes]
        for index, axis in enumerate(axes):
            axis_name = axis.get("name", "")
            if isinstance(axis_name, bytes):
                axis_name = axis_name.decode("utf-8", errors="ignore")
            if "weight" in str(axis_name).lower():
                values[index] = weight
        if axes:
            font.set_variation_by_axes(values)
    except (AttributeError, OSError, ValueError):
        pass
    return font


def campaign_text(
    value: str, x: int, y: int, size: int, color: str,
    family: str, weight: int, font_paths: dict, max_width: int,
    tracking: float = 0, opacity: float = 1
) -> str:
    """Manually sized display/support text; fail rather than silently shrinking."""
    font = font_for_measurement(font_paths[family], size, weight)
    measured = font.getlength(value) + max(0, len(value) - 1) * tracking
    if measured > max_width - 12:
        raise ValueError(
            f"Texto '{value}' ultrapassa o espaço desenhado: {measured:.1f}px > {max_width}px. "
            "Rever copy, fonte ou composição; não reduzir automaticamente."
        )
    return (
        f'<text x="{x}" y="{y}" fill="{color}" opacity="{opacity}" '
        f'font-family="{family}, sans-serif" font-size="{size}" font-weight="{weight}" '
        f'letter-spacing="{tracking}">{esc(value)}</text>'
    )


def direct_logo(logo_uri: str, x: int, y: int, width: int) -> str:
    height = width * 50 / 192
    return (
        f'<image x="{x}" y="{y}" width="{width}" height="{height:.2f}" '
        f'preserveAspectRatio="none" href="{logo_uri}"/>'
    )


def compose_social_test_svg(post: dict, white_logo_uri: str, photo_uri: str, font_paths: dict) -> str:
    slug = re.sub(r"[^a-z0-9-]", "-", post["slug"].lower())
    box = post["photo_box"]
    layout = post["layout"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{slug}-title {slug}-desc">',
        f'<title id="{slug}-title">Guardian — {esc(post["name"])}</title>',
        f'<desc id="{slug}-desc">{esc(post["alt_text"])}</desc>',
        "<defs>",
        f'<clipPath id="photo-clip"><rect x="{box["x"]}" y="{box["y"]}" width="{box["width"]}" height="{box["height"]}"/></clipPath>',
        '<linearGradient id="photo-dark" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#031724" stop-opacity=".74"/><stop offset=".44" stop-color="#031724" stop-opacity=".14"/><stop offset="1" stop-color="#031724" stop-opacity=".96"/></linearGradient>',
        '<linearGradient id="photo-left" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#031724" stop-opacity=".1"/><stop offset=".7" stop-color="#031724" stop-opacity=".18"/><stop offset="1" stop-color="#031724" stop-opacity=".5"/></linearGradient>',
        '<linearGradient id="maintenance-shade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#031724" stop-opacity="0"/><stop offset=".78" stop-color="#031724" stop-opacity=".16"/><stop offset="1" stop-color="#031724" stop-opacity=".42"/></linearGradient>',
        "</defs>",
    ]

    if layout == "flow":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo_uri, box),
            '<rect width="1080" height="1350" fill="url(#photo-dark)"/>',
            '<path d="M0 0H1080V15H0Z" fill="#CB3033"/>',
            direct_logo(white_logo_uri, 72, 62, 278),
            campaign_text("SOLUÇÕES PARA CONDOMÍNIOS", 76, 720, 22, CYAN, "Manrope", 700, font_paths, 760, 2.0),
            campaign_text("ACESSO", 66, 920, 178, WHITE, "Oswald", 700, font_paths, 860, -4.5),
            campaign_text("COM GESTÃO.", 72, 1065, 126, RED, "Oswald", 700, font_paths, 900, -3.5),
            campaign_text("Portaria remota e controle de acesso", 76, 1150, 25, WHITE, "Manrope", 600, font_paths, 900),
            campaign_text("para a dinâmica do condomínio.", 76, 1187, 25, WHITE, "Manrope", 600, font_paths, 900),
            '<path d="M76 1230H308" stroke="#00FFFF" stroke-width="3"/>',
            campaign_text("FALE COM A GUARDIAN", 76, 1280, 20, WHITE, "Manrope", 800, font_paths, 410, 1.5),
        ]
    elif layout == "monitor":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo_uri, box),
            '<rect width="1080" height="1350" fill="url(#photo-dark)" opacity=".72"/>',
            '<path d="M0 858L1080 758V1350H0Z" fill="#04344C"/>',
            '<path d="M0 858L1080 758" fill="none" stroke="#CB3033" stroke-width="9"/>',
            '<path d="M0 875L1080 775" fill="none" stroke="#FFFFFF" stroke-opacity=".28" stroke-width="2"/>',
            direct_logo(white_logo_uri, 72, 62, 278),
            '<path d="M880 145H1004V269M1004 145L1032 173M880 269L908 297" fill="none" stroke="#00FFFF" stroke-width="3" opacity=".78"/>',
            campaign_text("MONITORAMENTO DE IMAGEM 24H", 74, 902, 19, "#C9E1EA", "Manrope", 700, font_paths, 760, 1.7),
            campaign_text("ALÉM DO", 66, 1038, 148, WHITE, "Oswald", 700, font_paths, 860, -4.2),
            campaign_text("ALERTA.", 72, 1225, 180, RED, "Oswald", 700, font_paths, 860, -4.8),
            campaign_text("A imagem complementa a análise de eventos pela central.", 74, 1278, 20, WHITE, "Manrope", 600, font_paths, 930),
            campaign_text("FALE COM A GUARDIAN", 74, 1320, 18, WHITE, "Manrope", 800, font_paths, 400, 1.2),
        ]
    elif layout == "maintenance_test":
        parts += [
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            photo_image(photo_uri, box),
            '<rect x="0" y="0" width="690" height="1350" fill="url(#maintenance-shade)"/>',
            '<path d="M700 0H1080V1350H535Z" fill="#04344C"/>',
            '<path d="M682 0L517 1350" fill="none" stroke="#CB3033" stroke-width="12"/>',
            direct_logo(white_logo_uri, 716, 72, 278),
            campaign_text("PREVENTIVA + CORRETIVA", 674, 405, 18, CYAN, "Manrope", 700, font_paths, 365, 1.4),
            campaign_text("SISTEMA", 670, 575, 104, WHITE, "Oswald", 700, font_paths, 360, -3.0),
            campaign_text("EM DIA.", 670, 710, 122, RED, "Oswald", 700, font_paths, 400, -3.6),
            campaign_text("Alarmes, câmeras,", 674, 815, 21, WHITE, "Manrope", 600, font_paths, 360),
            campaign_text("automatizadores, interfonia", 674, 850, 21, WHITE, "Manrope", 600, font_paths, 375),
            campaign_text("e controle de acesso.", 674, 885, 21, WHITE, "Manrope", 600, font_paths, 360),
            '<path d="M674 1040H950" stroke="#00FFFF" stroke-width="3"/>',
            campaign_text("SOLICITE UMA", 674, 1115, 21, WHITE, "Manrope", 800, font_paths, 310, 1.2),
            campaign_text("AVALIAÇÃO TÉCNICA", 674, 1152, 21, WHITE, "Manrope", 800, font_paths, 340, 1.1),
            campaign_text("GUARDIAN • FLORIANÓPOLIS", 674, 1292, 15, "#C9E1EA", "Manrope", 700, font_paths, 355, 0.6),
        ]
    else:
        raise ValueError(f"Layout de teste Guardian desconhecido: {layout}")

    parts.append("</svg>")
    return "\n".join(parts)


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
    logo_uri, logo_white_uri, logo_meta, logo_white_bytes = load_logo(request["logo"]["url"])
    (out_dir / "guardian-logo-white.png").write_bytes(logo_white_bytes)
    font_paths = prepare_campaign_fonts(out_dir) if any(post.get("layout") in ("flow", "monitor", "maintenance_test") for post in request["posts"]) else {}
    report_posts = []
    preview_items = []
    captions = []
    for post in request["posts"]:
        photo_uri, photo_meta = prepare_photo(post)
        selected_logo_uri = logo_white_uri if post.get("logo_variant") == "white" else logo_uri
        if post.get("layout") in ("flow", "monitor", "maintenance_test"):
            svg = compose_social_test_svg(post, logo_white_uri, photo_uri, font_paths)
            selected_logo_uri = logo_white_uri
        else:
            svg = compose_svg(post, logo_uri, photo_uri)
        slug = post["slug"]
        svg_path = out_dir / f"{slug}.svg"
        png_path = out_dir / f"{slug}.png"
        svg_path.write_text(svg, encoding="utf-8")
        validation = validate_svg(svg_path, selected_logo_uri, photo_uri)
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
            "name": post["name"], "slug": slug, "layout": post["layout"], "logo_variant": "white" if selected_logo_uri == logo_white_uri else "original",
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
        "campaign_fonts": {
            "display": "Oswald variable 700 (OFL)",
            "support": "Manrope variable 600/700/800 (OFL)",
            "official_brand_typeface": False
        } if font_paths else None,
        "rendered_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "visual_method": "Fotografia raster original preservada e incorporada por data URI; tipografia, recortes e grafismos em SVG. Não é raster-to-vector nem imagem gerada por IA.",
        "posts": report_posts,
        "quality_checks": {
            "all_svg_xml_valid": True, "one_logo_and_one_photo_per_post": True,
            "white_logo_variant_generated_from_original": True,
            "white_logo_has_transparent_background": True,
            "campaign_fonts_loaded_and_fontconfig_checked": bool(font_paths),
            "new_campaign_uses_white_logo_without_contrast_plate": True,
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
