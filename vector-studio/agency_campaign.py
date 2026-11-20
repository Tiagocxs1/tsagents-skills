from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def _trace_body(trace_svg: str) -> tuple[str, str, str, str]:
    root = ET.fromstring(trace_svg)
    if not root.tag.endswith("svg"):
        raise ValueError("The VTracer output root is not SVG.")
    view_box = root.attrib.get("viewBox")
    if not view_box:
        width = root.attrib.get("width", "1200").replace("px", "")
        height = root.attrib.get("height", "1500").replace("px", "")
        view_box = f"0 0 {width} {height}"
    # Serialize child nodes instead of slicing the raw XML. VTracer may emit
    # an XML declaration, namespace prefix or leading metadata before the root.
    body = "".join(ET.tostring(child, encoding="unicode") for child in list(root))
    if not body.strip():
        raise ValueError("VTracer returned an empty SVG scene.")
    return body, view_box, root.attrib.get("width", "1200"), root.attrib.get("height", "1500")


def build_guardian_campaign(
    trace_svg: str,
    output: dict,
    copy: dict,
    brand: dict,
    source_page: str,
    photographer: str,
) -> str:
    width = int(output.get("width", 1080))
    height = int(output.get("height", 1350))
    body, view_box, _, _ = _trace_body(trace_svg)

    navy = brand.get("colors", {}).get("navy", "#04344C")
    red = brand.get("colors", {}).get("red", "#CB3033")
    cyan = brand.get("colors", {}).get("cyan", "#00FFFF")
    white = brand.get("colors", {}).get("white", "#FFFFFF")
    brand_name = str(brand.get("name", "Guardian")).upper()

    kicker = copy.get("kicker", "PORTARIA REMOTA  ·  CONTROLE DE ACESSO")
    line1, line2 = copy.get("headline", ["A ROTINA", "NÃO PARA."])
    support = copy.get("support", [
        "Portaria remota e controle de acesso",
        "no ritmo do seu condomínio.",
    ])
    support1 = support[0] if support else ""
    support2 = support[1] if len(support) > 1 else ""
    caption = copy.get("caption", "")
    cta = copy.get("cta", "CONVERSE COM A GUARDIAN")

    # The VTracer paths are nested as SVG geometry. No JPEG/PNG is embedded.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Guardian — {esc(line1)} {esc(line2)}</title>
<desc id="desc">Arte vetorial social-first com uma pessoa em uma entrada residencial à noite. A cena parte de fotografia real de {esc(photographer)}, vetorizada por caminhos SVG com VTracer. Imagem ilustrativa; não representa instalação nem cliente Guardian.</desc>
<defs>
  <linearGradient id="leftShade" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#031C2A" stop-opacity=".97"/>
    <stop offset=".22" stop-color="#031C2A" stop-opacity=".80"/>
    <stop offset=".38" stop-color="#031C2A" stop-opacity=".34"/>
    <stop offset=".53" stop-color="#031C2A" stop-opacity=".06"/>
    <stop offset=".70" stop-color="#031C2A" stop-opacity="0"/>
    <stop offset="1" stop-color="#031C2A" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="bottomShade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#031C2A" stop-opacity="0"/>
    <stop offset=".70" stop-color="#031C2A" stop-opacity=".08"/>
    <stop offset=".88" stop-color="#031C2A" stop-opacity=".48"/>
    <stop offset="1" stop-color="#031C2A" stop-opacity=".94"/>
  </linearGradient>
  <linearGradient id="topTint" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{navy}" stop-opacity=".30"/>
    <stop offset=".55" stop-color="{navy}" stop-opacity=".06"/>
    <stop offset="1" stop-color="{navy}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="edgeGlass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#D9F5F7" stop-opacity="0"/>
    <stop offset=".5" stop-color="#D9F5F7" stop-opacity=".27"/>
    <stop offset="1" stop-color="#D9F5F7" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="warmBloom">
    <stop offset="0" stop-color="#F8B75B" stop-opacity=".32"/>
    <stop offset="1" stop-color="#F8B75B" stop-opacity="0"/>
  </radialGradient>
  <filter id="foregroundBlur" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="18"/>
  </filter>
  <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="10"/>
  </filter>
  <clipPath id="frame"><rect width="{width}" height="{height}"/></clipPath>
</defs>

<g clip-path="url(#frame)">
  <!-- Layer 1: the complete scene, converted into editable vector paths. -->
  <rect width="{width}" height="{height}" fill="{navy}"/>
  <svg x="0" y="0" width="{width}" height="{height}" viewBox="{view_box}" preserveAspectRatio="xMidYMid slice">
    {body}
  </svg>

  <!-- Layer 2: restrained Guardian color grade and light shaping. -->
  <rect width="{width}" height="{height}" fill="{navy}" opacity=".11"/>
  <rect width="{width}" height="{height}" fill="url(#topTint)"/>
  <rect width="{width}" height="{height}" fill="url(#leftShade)"/>
  <rect width="{width}" height="{height}" fill="url(#bottomShade)"/>
  <ellipse cx="825" cy="565" rx="390" ry="500" fill="url(#warmBloom)" opacity=".78"/>

  <!-- Layer 3: architectural glass planes in the middle distance. -->
  <path d="M820 -40 L820 910 M1005 -30 L1005 980" stroke="#D8F2F5" stroke-width="3" opacity=".14"/>
  <path d="M790 0 L1080 0 L1080 15 L790 15Z" fill="#D8F2F5" opacity=".12"/>
  <path d="M818 910 L1080 910" stroke="{cyan}" stroke-width="2" opacity=".24"/>
  <path d="M904 0 L904 820" stroke="url(#edgeGlass)" stroke-width="30" opacity=".32"/>

  <!-- Layer 4: foreground foliage/glass silhouettes, intentionally out of focus. -->
  <g filter="url(#foregroundBlur)" opacity=".48">
    <path d="M-70 1110 C-5 1035 76 1055 112 1140 C75 1115 35 1168 15 1240 C-20 1210 -45 1160 -70 1110Z" fill="#0A2937"/>
    <path d="M-35 1230 C45 1135 125 1170 152 1255 C88 1235 45 1322 12 1405Z" fill="#244552"/>
    <path d="M890 1195 C930 1090 1035 1080 1115 1150 C1050 1165 1035 1240 1070 1335 C1000 1285 940 1260 890 1195Z" fill="#092A38"/>
    <path d="M960 1290 C1015 1195 1090 1220 1120 1300 L1120 1450 L1000 1450Z" fill="#506A76" opacity=".34"/>
  </g>
  <path d="M0 1260 C80 1180 150 1190 215 1290" fill="none" stroke="#91AAB6" stroke-width="4" opacity=".10"/>
  <path d="M930 1350 L1080 1230" fill="none" stroke="#D9F5F7" stroke-width="6" opacity=".08"/>

  <!-- Layer 5: expressive campaign typography, not a document template. -->
  <path d="M66 112 L118 112" stroke="{red}" stroke-width="9" stroke-linecap="square"/>
  <text x="140" y="124" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="28" font-weight="900" letter-spacing="3.4">{esc(brand_name)}</text>
  <text x="68" y="190" fill="#C9DDE4" font-family="DejaVu Sans, sans-serif" font-size="19" font-weight="700" letter-spacing="2.1">{esc(kicker.upper())}</text>

  <text x="60" y="365" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="142" font-weight="900" font-style="italic" letter-spacing="-8" textLength="650" lengthAdjust="spacingAndGlyphs">{esc(line1)}</text>
  <text x="58" y="514" fill="{red}" font-family="DejaVu Sans, sans-serif" font-size="154" font-weight="900" font-style="italic" letter-spacing="-9" textLength="720" lengthAdjust="spacingAndGlyphs">{esc(line2)}</text>
  <path d="M66 548 L410 548" fill="none" stroke="{cyan}" stroke-width="7" stroke-linecap="round"/>
  <path d="M430 548 L530 548" fill="none" stroke="{white}" stroke-width="2" opacity=".55"/>

  <text x="72" y="625" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="25" font-weight="600">{esc(support1)}</text>
  <text x="72" y="665" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="25" font-weight="600">{esc(support2)}</text>

  <!-- A loose, directional graphic stroke cuts across the composition. -->
  <path d="M850 730 C900 705 965 700 1035 716" fill="none" stroke="{cyan}" stroke-width="3" opacity=".35"/>
  <path d="M868 754 C920 733 980 734 1048 750" fill="none" stroke="{white}" stroke-width="1.5" opacity=".18"/>

  <!-- Minimal action line; no boxed CTA. -->
  <text x="72" y="1270" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="24" font-weight="800" letter-spacing="1.2">{esc(cta.upper())}</text>
  <path d="M72 1294 L350 1294" stroke="{red}" stroke-width="5" stroke-linecap="square"/>
  <path d="M1010 1260 L1040 1290 L1010 1320" fill="none" stroke="{cyan}" stroke-width="4" opacity=".75"/>
</g>
</svg>'''
    ET.fromstring(svg)
    return svg
