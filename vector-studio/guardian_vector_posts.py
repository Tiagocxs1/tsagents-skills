from __future__ import annotations
import base64, hashlib, html, io, json, re
from pathlib import Path
import requests, cairosvg
from PIL import Image, ImageDraw

W,H=1080,1350
NAVY="#04344C"; RED="#CB3033"; SLATE="#506A76"; CYAN="#00FFFF"; WHITE="#FFFFFF"

def e(v): return html.escape(str(v),quote=True)

def logo_data(url):
    r=requests.get(url,timeout=(15,60),headers={"User-Agent":"TS-Digitais-Guardian-Social/1.0"})
    r.raise_for_status(); raw=r.content
    if not raw.startswith(b"\x89PNG\r\n\x1a\n"): raise ValueError("Logo Cloudinary não é um PNG válido.")
    with Image.open(io.BytesIO(raw)) as im: im.verify()
    with Image.open(io.BytesIO(raw)) as im:
        if im.size!=(192,50): raise ValueError(f"Dimensões inesperadas do logo: {im.size}")
    return "data:image/png;base64,"+base64.b64encode(raw).decode("ascii"), {"url":url,"format":"PNG","dimensions":[192,50],"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}

def scene_for(theme):
    if theme=="architecture":
        return f"""
        <g id="architectural-volume">
          <ellipse cx="815" cy="1035" rx="310" ry="75" fill="#010D16" opacity=".65" filter="url(#blur)"/>
          <path d="M560 800L815 650L1040 780L780 940Z" fill="#103E54" stroke="#91B9C7" stroke-width="2"/>
          <path d="M560 800V1050L780 1180V940Z" fill="#0B2D41" stroke="#779EAD" stroke-opacity=".65" stroke-width="2"/>
          <path d="M780 940L1040 780V1030L780 1180Z" fill="#082536" stroke="#779EAD" stroke-opacity=".65" stroke-width="2"/>
          <path d="M625 750V430L825 315V650Z" fill="#0D3449" stroke="#A9D0DB" stroke-opacity=".6" stroke-width="2"/>
          <path d="M825 315L1000 415V805L825 705Z" fill="#1B5066" stroke="#B6D7E0" stroke-opacity=".6" stroke-width="2"/>
          <path d="M625 430L825 545L1000 415L825 315Z" fill="#205970" stroke="#C9E4EB" stroke-opacity=".5" stroke-width="2"/>
          <path d="M660 470L790 545V660L660 585Z M660 620L790 695V810L660 735Z" fill="url(#glass)" stroke="#BDEAF2" stroke-opacity=".6" stroke-width="2"/>
          <path d="M850 375L965 442V560L850 493Z M850 525L965 592V710L850 643Z" fill="url(#glass)" stroke="#BDEAF2" stroke-opacity=".6" stroke-width="2"/>
          <path d="M625 430L825 315L1000 415" fill="none" stroke="{CYAN}" stroke-width="4" opacity=".7"/>
          <path d="M710 835V1050L780 1090V940Z" fill="#A93643" stroke="#F6BFC3" stroke-width="2"/>
          <path d="M710 835L780 795L850 835L780 875Z" fill="url(#redMetal)"/>
          <path d="M780 875L850 835V1050L780 1090Z" fill="#672A37"/>
          <path d="M570 1120L780 1240L1030 1095" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>
          <path d="M540 765L540 1035L780 1175M1040 780L1065 765V1020L780 1190" fill="none" stroke="#B7D4DE" stroke-opacity=".3" stroke-width="2"/>
          <circle cx="930" cy="760" r="120" fill="url(#halo)"/>
        </g>"""
    if theme=="alarm":
        return f"""
        <g id="signal-volume">
          <circle cx="800" cy="930" r="340" fill="url(#halo)"/>
          <g transform="translate(800 930)" fill="none" stroke-linecap="round">
            <circle r="292" stroke="#A4C8D3" stroke-opacity=".25" stroke-width="2"/>
            <circle r="245" stroke="{CYAN}" stroke-opacity=".38" stroke-width="3" stroke-dasharray="5 14"/>
            <circle r="190" stroke="{RED}" stroke-width="8"/>
            <circle r="142" stroke="#D8EDF2" stroke-opacity=".6" stroke-width="2"/>
          </g>
          <ellipse cx="800" cy="1100" rx="270" ry="60" fill="#010D16" opacity=".7" filter="url(#blur)"/>
          <path d="M650 790L800 705L950 790V1010L800 1095L650 1010Z" fill="#082638" stroke="#A4CAD4" stroke-opacity=".7" stroke-width="3"/>
          <path d="M650 790L800 875L950 790M800 875V1095" fill="none" stroke="#C5E2E9" stroke-opacity=".45" stroke-width="2"/>
          <path d="M700 805L800 748L900 805L800 865Z" fill="url(#silver)" stroke="#E4F2F5" stroke-width="2"/>
          <path d="M700 805V960L800 1018V865Z" fill="#244C60"/><path d="M800 865L900 805V960L800 1018Z" fill="#0A3045"/>
          <circle cx="800" cy="865" r="54" fill="url(#redMetal)" stroke="#FFD0D2" stroke-width="3"/><circle cx="800" cy="865" r="22" fill="#FFF0F0"/>
          <path d="M800 700V625M965 865H1040M560 865H635M685 750L630 695M915 750L970 695" stroke="{CYAN}" stroke-width="5" stroke-linecap="round" opacity=".78"/>
          <path d="M800 550V615M1100 865H1035M500 865H565" stroke="{RED}" stroke-width="4"/>
          <path d="M500 865L535 846V884Z M1100 865L1065 846V884Z" fill="{RED}"/>
        </g>"""
    if theme=="image":
        return f"""
        <g id="optic-volume">
          <circle cx="805" cy="920" r="380" fill="url(#halo)"/>
          <ellipse cx="805" cy="1110" rx="340" ry="82" fill="#010D16" opacity=".65" filter="url(#blur)"/>
          <path d="M535 745L805 590L1070 745V1035L805 1190L535 1035Z" fill="#08283B" stroke="#9DBFCA" stroke-opacity=".65" stroke-width="3"/>
          <path d="M535 745L805 900L1070 745M805 900V1190" fill="none" stroke="#C2DDE5" stroke-opacity=".38" stroke-width="2"/>
          <g transform="translate(805 890)">
            <circle r="235" fill="#061B28" stroke="#A9CCD6" stroke-opacity=".7" stroke-width="4"/>
            <circle r="205" fill="none" stroke="{CYAN}" stroke-opacity=".6" stroke-width="5" stroke-dasharray="70 17 20 17"/>
            <circle r="166" fill="#16465A" stroke="#7099A9" stroke-width="14"/>
            <circle r="132" fill="url(#silver)" stroke="#E6F2F5" stroke-width="3"/>
            <circle r="99" fill="#071F2D" stroke="#9CBBC7" stroke-width="10"/>
            <circle r="70" fill="#0B3449" stroke="{RED}" stroke-width="8"/>
            <circle r="40" fill="#020E18" stroke="#C2DDE5" stroke-width="3"/>
            <path d="M-155 -82C-72 -200 75 -198 155 -82" fill="none" stroke="#F1FCFF" stroke-width="9" opacity=".42" stroke-linecap="round"/>
            <path d="M-130 125C-40 197 55 198 130 125" fill="none" stroke="{CYAN}" stroke-width="4" opacity=".5"/>
          </g>
          <path d="M420 850H535M1075 850H1000M470 620L565 720M1040 620L950 720" fill="none" stroke="{RED}" stroke-width="4"/>
          <path d="M420 850L447 830M420 850L447 870M1075 850L1048 830M1075 850L1048 870" fill="none" stroke="{RED}" stroke-width="4"/>
        </g>"""
    return f"""
    <g id="maintenance-volume">
      <ellipse cx="800" cy="1010" rx="360" ry="90" fill="#010D16" opacity=".7" filter="url(#blur)"/>
      <g transform="translate(800 865)">
        <path d="M0 -310L270 -155V155L0 310L-270 155V-155Z" fill="#0A3044" stroke="#A5C7D1" stroke-opacity=".7" stroke-width="3"/>
        <path d="M0 -310V0L270 155V-155Z" fill="#18485D"/><path d="M0 -310V0L-270 155V-155Z" fill="#0D3A51"/>
        <path d="M-270 -155L0 0L270 -155M-270 155L0 310L270 155" fill="none" stroke="#B8D5DE" stroke-opacity=".6" stroke-width="3"/>
        <path d="M0 -205L180 -102V102L0 205L-180 102V-102Z" fill="none" stroke="{CYAN}" stroke-opacity=".65" stroke-width="5"/>
        <path d="M0 -135L118 -67V67L0 135L-118 67V-67Z" fill="url(#silver)" stroke="#E3F1F5" stroke-width="3"/>
        <path d="M0 -135V0L118 67V-67Z" fill="#54798A"/><path d="M0 0L-118 -67V67L0 135Z" fill="#173B50"/>
        <circle r="48" fill="url(#redMetal)" stroke="#FFC4C6" stroke-width="3"/><circle r="16" fill="#FFF1F1"/>
        <path d="M0 -385V-295M330 0H250M0 385V295M-330 0H-250" stroke="#D0E7ED" stroke-opacity=".55" stroke-width="3"/>
      </g>
      <path d="M440 670L550 735M1060 1075L950 1010M445 1080L550 1010M1060 665L955 735" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>
      <path d="M800 385V300H980M800 1190V1115H1000M450 865H330V740M1150 865H1030V985" fill="none" stroke="#C1DDE5" stroke-opacity=".5" stroke-width="2"/>
      <g fill="{CYAN}"><circle cx="980" cy="300" r="6"/><circle cx="1000" cy="1115" r="6"/><circle cx="330" cy="740" r="6"/><circle cx="1030" cy="985" r="6"/></g>
    </g>"""

def make_svg(post,logo):
    theme=post["theme"]
    if theme=="architecture":
        bg1,bg2="#041A29","#0D3D52"; kicker="SOLUÇÕES PARA CONDOMÍNIOS"
        lines=[("A PORTARIA",315,82,600,WHITE,"normal"),("MUDA.",415,124,430,RED,"italic"),("O CONTROLE",515,82,650,WHITE,"normal"),("CONTINUA.",610,108,700,WHITE,"italic")]
        support=["Portaria remota 24h e controle de acesso","integrados à rotina do condomínio."]
        caption="Cada condomínio tem uma dinâmica própria de entradas e circulação. A portaria remota integra comunicação, câmeras e controle de acesso à operação do condomínio, com atendimento da central 24 horas. Converse com a Guardian para avaliar a solução adequada à sua estrutura.\\n\\n#Guardian #PortariaRemota #Condomínios #ControleDeAcesso #Florianópolis"
        alt="Arte vetorial isométrica de um edifício e acesso condominial, sobre portaria remota e controle de acesso."
    elif theme=="alarm":
        bg1,bg2="#031827","#0C344A"; kicker="MONITORAMENTO DE ALARME 24H"
        lines=[("O ALERTA",325,116,600,WHITE,"italic"),("CHEGA.",445,126,545,RED,"italic"),("A CENTRAL",550,98,650,WHITE,"normal"),("ACOMPANHA.",650,88,760,WHITE,"normal")]
        support=["Monitoramento de alarme 24h para","residências e empresas."]
        caption="Um sistema de alarme é parte de uma operação de segurança. Com monitoramento 24 horas, os eventos recebidos podem ser acompanhados pela central conforme os procedimentos definidos para cada contrato. Fale com a Guardian e conheça as possibilidades para sua residência ou empresa.\\n\\n#Guardian #MonitoramentoDeAlarme #SegurançaEletrônica #Florianópolis"
        alt="Arte vetorial com ondas de sinal em camadas e um núcleo vermelho, sobre o acompanhamento de eventos de alarme pela central 24 horas."
    elif theme=="image":
        bg1,bg2="#061B2B","#123D51"; kicker="MONITORAMENTO DE IMAGEM 24H"
        lines=[("IMAGEM",325,140,560,WHITE,"italic"),("NÃO É SÓ",465,105,690,WHITE,"normal"),("REGISTRO.",580,112,720,RED,"italic")]
        support=["Monitoramento de imagem 24h, com análise","de eventos pela central."]
        caption="As imagens podem apoiar a análise de eventos recebidos pela operação de monitoramento. A Guardian integra monitoramento de imagem e sistemas de segurança para apoiar o acompanhamento de ocorrências, conforme a estrutura contratada. Converse com nossa equipe.\\n\\n#Guardian #MonitoramentoDeImagem #Câmeras #SegurançaEletrônica #GrandeFlorianópolis"
        alt="Arte vetorial com uma lente óptica tridimensional em camadas, representando monitoramento de imagem e análise de eventos."
    else:
        bg1,bg2="#041A29","#0C3449"; kicker="MANUTENÇÃO DE SISTEMAS"
        lines=[("SISTEMA",335,132,590,WHITE,"italic"),("EM DIA.",465,124,560,RED,"italic"),("ROTINA MAIS",570,96,750,WHITE,"normal"),("CONFIÁVEL.",675,98,750,WHITE,"normal")]
        support=["Manutenção preventiva e corretiva","em sistemas de segurança."]
        caption="Alarmes, câmeras, automatizadores, interfones e controle de acesso precisam de manutenção adequada. A manutenção preventiva e corretiva ajuda a identificar necessidades técnicas e manter os sistemas em condições de funcionamento. Solicite uma avaliação com a Guardian.\\n\\n#Guardian #Manutenção #SegurançaEletrônica #Condomínios #Florianópolis"
        alt="Arte vetorial geométrica em camadas metálicas, representando manutenção de sistemas de segurança."
    title="\\n".join(f'<text x="72" y="{y}" fill="{col}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="900" font-style="{style}" letter-spacing="-4" textLength="{width}" lengthAdjust="spacingAndGlyphs">{e(txt)}</text>' for txt,y,size,width,col,style in lines)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
    <title id="title">Guardian — {e(post["name"])}</title><desc id="desc">{e(alt)}</desc>
    <defs>
      <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
      <linearGradient id="redMetal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F06B6D"/><stop offset=".45" stop-color="{RED}"/><stop offset="1" stop-color="#791E2A"/></linearGradient>
      <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E0F8FF" stop-opacity=".45"/><stop offset=".5" stop-color="#7BB4C5" stop-opacity=".1"/><stop offset="1" stop-color="#DDF8FF" stop-opacity=".02"/></linearGradient>
      <linearGradient id="silver" x1="0" y1="0" x2=".9" y2="1"><stop offset="0" stop-color="#EAF5F8"/><stop offset=".4" stop-color="#8EABB7"/><stop offset="1" stop-color="#102F43"/></linearGradient>
      <radialGradient id="halo"><stop offset="0" stop-color="{CYAN}" stop-opacity=".24"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
      <filter id="blur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="24"/></filter>
      <pattern id="grid" width="46" height="46" patternUnits="userSpaceOnUse"><path d="M46 0H0V46" fill="none" stroke="#CBE7F0" stroke-opacity=".065"/></pattern>
    </defs>
    <rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#grid)"/>
    <rect width="{W}" height="18" fill="{RED}"/>
    <image x="72" y="70" width="268" height="69.79" preserveAspectRatio="xMinYMid meet" href="{logo}"/>
    <path d="M72 166H127" stroke="{RED}" stroke-width="7"/>
    <text x="147" y="174" fill="#BFD6E0" font-family="DejaVu Sans,Arial,sans-serif" font-size="19" font-weight="700" letter-spacing="3">{e(kicker)}</text>
    <circle cx="850" cy="650" r="450" fill="url(#halo)"/>
    {title}
    <text x="74" y="742" fill="#DCEBF0" font-family="DejaVu Sans,Arial,sans-serif" font-size="25">{e(support[0])}</text>
    <text x="74" y="781" fill="#DCEBF0" font-family="DejaVu Sans,Arial,sans-serif" font-size="25">{e(support[1])}</text>
    {scene_for(theme)}
    <text x="74" y="1140" fill="#8FB1BE" font-family="DejaVu Sans,Arial,sans-serif" font-size="16" font-weight="700" letter-spacing="3">FLORIANÓPOLIS E GRANDE FLORIANÓPOLIS</text>
    <path d="M72 1180H1008" stroke="#B9D5DF" stroke-opacity=".22" stroke-width="1.5"/>
    <text x="74" y="1260" fill="{WHITE}" font-family="DejaVu Sans,Arial,sans-serif" font-size="23" font-weight="700" letter-spacing="1.5">CONVERSE COM A GUARDIAN</text>
    <path d="M920 1240H1008M985 1218L1008 1240L985 1262" fill="none" stroke="{CYAN}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <rect y="1329" width="{W}" height="21" fill="{RED}"/>
    </svg>''',caption,alt

def render_guardian_vector_posts(request,out_dir):
    out_dir=Path(out_dir); out_dir.mkdir(parents=True,exist_ok=True)
    logo,logo_meta=logo_data(request["logo"]["url"]); outputs=[]; thumbs=[]
    for post in request["posts"]:
        stem=re.sub(r"[^a-z0-9-]+","-",post["slug"].lower()).strip("-")
        svg,caption,alt=make_svg(post,logo); sp=out_dir/(stem+".svg"); pp=out_dir/(stem+".png")
        sp.write_text(svg,encoding="utf-8")
        cairosvg.svg2png(bytestring=svg.encode("utf-8"),write_to=str(pp),output_width=W,output_height=H)
        import xml.etree.ElementTree as ET
        root=ET.parse(sp).getroot(); imgs=[x for x in root.iter() if x.tag.endswith("image")]
        href=imgs[0].attrib.get("href","") if len(imgs)==1 else ""
        if len(imgs)!=1 or href!=logo or not href.startswith("data:image/png;base64,"): raise ValueError("Logo original ausente ou alterado em "+stem)
        with Image.open(pp) as im: im.verify()
        with Image.open(pp) as im:
            if im.size!=(W,H): raise ValueError("Dimensão incorreta: "+stem)
            im=im.convert("RGB"); im.thumbnail((250,313)); thumbs.append((stem,im.copy()))
        (out_dir/(stem+"-caption.md")).write_text(caption.replace("\\n","\n")+"\n",encoding="utf-8")
        (out_dir/(stem+"-alt.txt")).write_text(alt+"\n",encoding="utf-8")
        outputs.append({"name":stem,"width":W,"height":H,"svg_bytes":sp.stat().st_size,"png_bytes":pp.stat().st_size,"svg_xml_valid":True,"embedded_logo_count":1,"png_verified":True})
    sheet=Image.new("RGB",(4*270+30,350),(4,21,32)); d=ImageDraw.Draw(sheet)
    for i,(name,im) in enumerate(thumbs):
        x=15+i*270; sheet.paste(im,(x,8)); d.text((x,326),name,fill=(235,245,248))
    sheet.save(out_dir/"contact-sheet.jpg",quality=92,optimize=True)
    report={"pipeline":"TS Digitais Guardian SVG Social Studio","format":"Instagram feed 4:5","canvas":[W,H],"logo":logo_meta,"outputs":outputs,"visual_language":"SVG puro com geometria vetorial tridimensional; sem imagem gerada por IA ou fotografia externa; logo oficial incorporado sem alteração.","quality_checks":{"svg_xml_valid":True,"one_original_logo_per_post":True,"all_pngs_verified":True,"png_dimensions":[W,H]}}
    (out_dir/"metadata.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"success","posts":len(outputs),"logo":logo_meta,"files":sorted(x.name for x in out_dir.iterdir())},ensure_ascii=False,indent=2))
