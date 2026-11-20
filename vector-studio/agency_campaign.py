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
    match = re.match(r"^\s*<svg\b[^>]*>(.*)</svg>\s*$", trace_svg, re.S)
    if not match:
        raise ValueError("Could not extract the VTracer SVG body.")
    body = match.group(1)
    body = re.sub(r"<\?xml[^>]*\?>", "", body)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
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
    <stop offset=".34" stop-color="#031C2A" stop-opacity=".86"/>
    <stop offset=".61" stop-color="#031C2A" stop-opacity=".46"/>
    <stop offset=".82" stop-color="#031C2A" stop-opacity=".08"/>
    <stop offset="1" stop-color="#031C2A" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="bottomShade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#031C2A" stop-opacity="0"/>
    <stop offset=".58" stop-color="#031C2A" stop-opacity=".30"/>
    <stop offset="1" stop-color="#031C2A" stop-opacity=".93"/>
  </linearGradient>
  <linearGradient id="topTint" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{navy}" stop-opacity=".50"/>
    <stop offset=".55" stop-color="{navy}" stop-opacity=".10"/>
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
  <rect width="{width}" height="{height}" fill="{navy}" opacity=".20"/>
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
  <g filter="url(#foregroundBlur)" opacity=".66">
    <path d="M-90 1110 C20 920 145 1005 205 1190 C120 1140 70 1260 25 1410 L-90 1410Z" fill="#061F2B"/>
    <path d="M-10 1250 C90 1080 185 1110 245 1290 C150 1230 115 1385 65 1450Z" fill="#173A46"/>
    <path d="M835 1390 C835 1200 950 1100 1095 1095 L1120 1450Z" fill="#092A38"/>
    <path d="M910 1320 C900 1190 1015 1160 1100 1195 C1030 1260 1060 1370 1080 1450Z" fill="#506A76" opacity=".42"/>
  </g>
  <path d="M0 1220 C115 1160 190 1185 300 1350" fill="none" stroke="#91AAB6" stroke-width="5" opacity=".12"/>
  <path d="M830 1350 L1080 1160" fill="none" stroke="#D9F5F7" stroke-width="8" opacity=".09"/>

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
  <path d="M715 720 C810 680 890 665 1000 690" fill="none" stroke="{cyan}" stroke-width="3" opacity=".44"/>
  <path d="M740 748 C835 710 910 710 1020 738" fill="none" stroke="{white}" stroke-width="1.5" opacity=".22"/>

  <!-- Minimal action line; no boxed CTA. -->
  <text x="72" y="1270" fill="{white}" font-family="DejaVu Sans, sans-serif" font-size="24" font-weight="800" letter-spacing="1.2">{esc(cta.upper())}</text>
  <path d="M72 1294 L350 1294" stroke="{red}" stroke-width="5" stroke-linecap="square"/>
  <path d="M1010 1260 L1040 1290 L1010 1320" fill="none" stroke="{cyan}" stroke-width="4" opacity=".75"/>
</g>
</svg>'''
    ET.fromstring(svg)
    return svg
