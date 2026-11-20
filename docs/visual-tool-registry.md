# Catálogo visual — skills, MCPs, agentes e ferramentas

Pesquisa e inventário inicial em 17/11/2026. “Conectado” significa que o conector foi identificado nas ferramentas disponíveis nesta conversa; não significa que todo recurso externo foi autenticado ou que todo uso é gratuito. Créditos, permissões e planos devem ser conferidos antes de gerar.

## 1. Ferramentas conectadas nesta conta

| Ferramenta | Status | Melhor aplicação | Observação |
|---|---|---|---|
| Canva | Conectado | Posts, carrosséis, flyers, anúncios, Brand Kits, templates, autofill e resize | Já integrado; não precisa instalar um segundo Canva MCP. |
| Figma | Conectado | Vetores editáveis, ilustrações em camadas, design systems, componentes e protótipos | MCP oficial; algumas ações de IA e escrita no canvas dependem de seat/créditos. |
| Adobe Express / Creative Cloud | Conectado | Templates, composição, texto, imagens, fontes, animação e export | Inicializar o conector com adobe_mandatory_init antes do primeiro uso Adobe em cada conversa. |
| MagicPath | Conectado | Interfaces web/mobile, componentes React/Tailwind, canvas e preview | Skills já habilitadas: frontend-design, magicpath-design, typeset, polish e animations. Priorizar UI, não flyer por padrão. |
| Comfy Cloud | Conectado | Workflows ComfyUI, pesquisa de modelos, geração e edição | Conferir estimativa de créditos antes de executar. |
| fal.ai | Conectado | Imagem/vídeo, fotografia comercial, anúncios, UGC e pipelines de mídia | Skills de marketing/commercial/UGC e model-routing disponíveis; conferir custo por job. |
| Cloudinary | Conectado | Biblioteca de mídia, busca, organização, transformação e entrega de assets | Gestão e transformação de mídia; não substitui direção de arte. |
| ElevenLabs | Conectado | Voz, áudio, vídeo e recursos de mídia criativa | Usar quando voz/áudio fizer sentido; conferir créditos. |
| Browser | Conectado | Inspecionar referências e previews web | Útil para validação do resultado renderizado. |
| GitHub | Conectado | Versionar skills, diretrizes e perfis de agentes | Este repositório é a fonte de verdade dos guias TS Digitais. |

## 2. Skills e referências prioritárias

### Arte, design e interface
| Projeto | Uso | Recomendação |
|---|---|---|
| https://github.com/anthropics/skills | Canvas Design para pôster/arte estática; Algorithmic Art para arte generativa; Frontend Design para interfaces | Referência oficial. Instalar no agente apropriado; não copiar/republicar arquivos sem confirmar a licença. |
| https://github.com/pbakaus/impeccable | Crítica e polimento de UI/front-end, prevenção de padrões genéricos | Apache-2.0. Forte para HTML/interfaces; não é uma skill específica para anúncios impressos. |
| https://github.com/Leonxlnx/taste-skill | Design Taste para art direction e interfaces menos genéricas | Usar especialmente em landing pages e front-end; não substitui direção de arte para social. |
| https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Estilos, paletas, tipografia, UX e padrões por stack | Já existe cópia local em ui-ux-pro-max; sua contagem de estilos/paletas está desatualizada, revisar upstream antes de atualizar. |
| https://github.com/ComposioHQ/awesome-claude-skills | Catálogo de skills, incluindo AnyDesign e outras ferramentas criativas | Diretório curado, não uma skill única. Avaliar repositório, licença e atividade de cada item. |

### Social e publicidade
| Projeto | Uso | Licença / popularidade | Recomendação |
|---|---|---|---|
| https://github.com/social-media-skills/skills | Estratégia social, identidade, carrossel, thumbnail, infográfico, prompts de imagem, vídeo, planejamento e analytics | MIT; catálogo com 106 skills no snapshot consultado | Prioridade máxima para produção de conteúdo social. Instalar módulos seletivos. |
| https://github.com/coreyhaines31/marketingskills | Copy, psicologia, anúncios, social content e CRO | Catálogo popular; skills de ads e ad-creative têm alto uso no skills.sh | Prioridade máxima para estratégia/copy de anúncios; não é gerador de layout. |
| https://github.com/adkit/ads-skills | Estratégia e skills de execução para Meta, Google e outros canais; estratégia standalone, MCP opcional para criar/publicar | Repositório MIT, mas `meta-ads-strategy` e `google-ads-strategy` têm licença própria sem redistribuição; MCP AdKit é externo | Manter link externo. Não copiar as duas skills com licença especial; não ativar serviço de execução sem avaliar custo e autorização de publicação. |

### Motion e mídia
- https://gsap.com/ — timeline e motion web avançado.
- https://motion.dev/ — animação e interação de interfaces.
- CSS transitions e Web Animations API — preferir quando resolvem o caso sem dependências extras.
- Skills fal.ai já acessíveis: marketing, commercial, ugc, model-routing, cinematography, storytelling, recipes e workflow.
- HeyGen tem skill de carousel e motion; fluxos de geração usam créditos e devem ser validados antes de começar.

## 3. MCPs externos — não conectados atualmente

| Recurso | O que oferece | Decisão |
|---|---|---|
| https://github.com/mobbin/mobbin-mcp-server | Referências e pesquisa de telas reais de apps/sites, via MCP oficial | Opcional para pesquisa de UI. Não gera anúncios nem artes; acesso depende da conta Mobbin. |
| https://github.com/OpenArt-AI/skills | MCP de geração de imagens/vídeos e skills para UGC, performance ads, hooks e variações | Opcional; sobrepõe fal.ai, Comfy Cloud, Adobe e ferramentas já conectadas. Usa créditos da conta OpenArt. |
| https://mcp.higgsfield.ai/mcp | Geração de imagem/vídeo e ferramentas para publicidade | Não priorizar: documentação atual informa exigência de assinatura ativa. |
| https://github.com/Upload-Post/upload-post-mcp | Publicação, agendamento e analytics de redes sociais | Ferramenta de distribuição, não de direção de arte. Considerar apenas quando automação de publicação for prioridade. |
| https://robinreach.com/mcp/v1/messages | Publicação, agendamento e gestão de redes sociais | Mesmo papel de Upload-Post; não é gerador de peças. |

## 4. Instalação seletiva via skills CLI

Executar no agente/editor que realmente use a CLI. A instalação da CLI não adiciona automaticamente skills ao registro interno do ChatGPT; cada runtime tem seu próprio mecanismo de carregamento.

Social e peças:
    npx skills add social-media-skills/skills --skill brand-profile
    npx skills add social-media-skills/skills --skill design-and-templates
    npx skills add social-media-skills/skills --skill carousel-writer
    npx skills add social-media-skills/skills --skill thumbnail-design
    npx skills add social-media-skills/skills --skill infographic-and-data-viz
    npx skills add social-media-skills/skills --skill image-prompt

Copy e anúncios:
    npx skills add coreyhaines31/marketingskills --skill ad-creative
    npx skills add coreyhaines31/marketingskills --skill social-content
    npx skills add coreyhaines31/marketingskills --skill marketing-psychology

Arte e front-end:
    npx skills add anthropics/skills --skill canvas-design
    npx skills add anthropics/skills --skill algorithmic-art
    npx skills add anthropics/skills --skill frontend-design
    npx skills add pbakaus/impeccable
    npx skills add Leonxlnx/taste-skill --skill design-taste-frontend

Instalar apenas as necessárias para cada projeto. Verificar a nomenclatura atual das skills no repositório upstream antes de rodar comandos, pois catálogos mudam.

## 5. Fluxo recomendado por objetivo

| Trabalho | Direção/skills | Ferramenta principal | Revisão |
|---|---|---|---|
| Post, story, carrossel | visual-design + social-media-creative + brand-profile/carousel-writer | Canva ou Adobe; Figma quando o vetor precisa ser editável | visual-quality-review |
| Anúncio de performance | visual-design + advertising-creative + ad-creative | Canva/Adobe para layout; fal.ai/Comfy para imagem base quando necessário | visual-quality-review |
| Flyer, pôster, material gráfico | visual-design + Canvas Design | Canva/Adobe ou SVG/HTML/Figma conforme precisão | visual-quality-review |
| Ilustração vetorial | visual-design + Algorithmic Art quando pertinente | Figma vector illustration ou SVG | validar no tamanho final |
| Banner ou arte HTML/SVG/JSON | visual-design + módulo social/ads conforme canal | SVG/HTML/CSS e preview do navegador | screenshot real + visual-quality-review |
| Site/landing/dashboard | ui-ux-pro-max + design-system + responsive + web-interface-guidelines + taste/impeccable conforme contexto | MagicPath, Figma ou código | inspeção de UI em breakpoints |
| Motion/vídeo | visual-design + motion-design + fal/HeyGen conforme caso | CSS/Motion/GSAP ou ferramenta de vídeo conectada | assistir ao arquivo exportado |

## 6. Política gratuita e de custos

1. Começar com recursos já conectados, templates gratuitos, SVG/HTML/CSS e ferramentas open-source.
2. Usar geração paga por crédito só quando acrescentar valor claro e o custo estiver visível.
3. Não pressupor que um plano free possui geração ilimitada.
4. Não iniciar lote de imagens/vídeos sem informar quantidades e consumo estimado.
5. Não adicionar outro MCP que duplique Canva/Figma/Adobe/fal/Comfy sem uma lacuna real.
6. Consultar preços e licenças atuais antes de recomendar conexão ou instalar recursos externos.

## 7. Fontes e avaliação

- https://skills.sh/ — diretório e telemetria de instalação; popularidade não prova qualidade.
- https://developers.figma.com/docs/figma-mcp-server/ — referência oficial Figma MCP.
- https://helpx.adobe.com/br/express/web/add-ons-and-integrations/chatgpt-integration-with-express.html — integração Adobe Express no ChatGPT.
- https://github.com/mobbin/mobbin-mcp-server — MCP oficial Mobbin.
- https://github.com/OpenArt-AI/skills — MCP/skills OpenArt.
- https://github.com/Upload-Post/upload-post-mcp — MCP Upload-Post.

Revisar atividade, licença, documentação e preços antes de novas adoções. Atualizar este catálogo periodicamente.

## 8. Complementos citados no briefing original — verificados

| Recurso | Link | O que acrescenta | Licença / condição |
|---|---|---|---|
| Mono-Color / Monocolor Editorial Print | https://github.com/yanliudesign/mono-color-skill | Peças editoriais de uma ou duas tintas, papel, halftone, pôsteres, zines, retratos e embalagens | MIT; skill especializada em uma direção visual, não deve ser aplicada a toda marca ou campanha. |
| Line Art Animation | https://github.com/JDhruv14/line-art-animation | Ilustração animada em SVG + TypeScript, figuras com ciclos de caminhada e cenas com variação dia/noite; usa biblioteca de código pequena | MIT; README pede Node 22.18+ para os exemplos. Recomendado para motion SVG, não para posts estáticos. |
| AnyDesign | https://github.com/uxKero/anydesign | Analisa screenshot, site ou Figma e gera design.md, tokens, inventário de componentes e notas de reconstrução | MIT; ideal para estudar referências e documentar padrões, não para copiar uma peça sem autorização. |
| Imagen Skill (Gemini API) | https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen | Skill para gerar assets visuais com a API de imagem do Gemini | Apache-2.0; requer GEMINI_API_KEY e uso da API. Conferir o modelo e o preço atuais antes de executar; não assumir gratuidade. |

Instalação sugerida em agentes compatíveis:

    npx skills add yanliudesign/mono-color-skill
    npx skills add JDhruv14/line-art-animation
    npx skills add uxKero/anydesign
    npx skills add sanjay3290/ai-skills --skill imagen

Esses comandos são opcionais e instalam no runtime que executa a skills CLI; eles não ativam essas skills automaticamente no registro interno do ChatGPT.

## 9. Critério de seleção dessas skills

- Mono-Color: usar somente quando o conceito pedir linguagem editorial limitada a uma ou duas tintas; não converter toda arte para esse estilo.
- Line Art Animation: usar em ilustração vetorial animada, personagens ou cenas SVG; verificar compatibilidade do runtime e não carregar a biblioteca quando CSS/SVG simples resolver.
- AnyDesign: ativar quando o usuário enviar um site, screenshot ou arquivo Figma como referência. Extrair tokens e componentes com nível de confiança e separar observação de inferência.
- Imagen: alternativa de geração, não padrão obrigatório. Priorizar imagem_gen e ferramentas já conectadas com custo claro; avaliar Gemini somente se houver API key e custo/qualidade justificarem.

## 10. Arsenal de copy, UX, dados e mercado brasileiro

Para os projetos upstream completos, versões fixadas, licenças, riscos e instruções de checkout, consultar [docs/UPSTREAM-ARSENAL.md](./UPSTREAM-ARSENAL.md). Os originais licenciados estão referenciados como Git submodules em `upstream/`; os itens sem licença clara ou com licenças de subpasta são somente referências externas. Nenhum MCP foi conectado nem nenhuma API autenticada nesta atualização.


## 3. Apresentações e propostas comerciais

O roteamento, a situação de cada MCP, as licenças, os custos e os commits upstream estão centralizados em docs/PRESENTATION-TOOLING.md. Skills locais: presentation-studio/SKILL.md e commercial-proposal/SKILL.md. Reutilizar Canva já catalogado; não instalar conectores duplicados. Google Slides MCP oficial continua em Developer Preview e não está autenticado por este registro.

## 11. Revistas digitais, e-books e flipbooks

### Separação de responsabilidades

Uma revista profissional exige duas camadas distintas:
- **Produção editorial:** direção de arte, sequência narrativa, copy, sistema tipográfico, grid, margens, imagens e diagramas.
- **Leitor/flipbook:** renderização de páginas, virada, zoom, pan, navegação, fullscreen e acessibilidade.

O motor de flipbook não é ferramenta de direção de arte. Primeiro aprovar o sistema editorial e as páginas-piloto; depois selecionar ou trocar o motor.

### Skills e agentes TS Digitais

- `editorial-magazine/SKILL.md` — padrão obrigatório de produção de revistas digitais.
- `design-driven-copywriter/SKILL.md` — copy dimensionada para os elementos do layout.
- `editorial-print-design/SKILL.md` — linguagem gráfica de impressão/zine quando adequada.
- `visual-design/SKILL.md` e `visual-quality-review/SKILL.md` — direção visual e gate final.
- `agents/editorial-art-director.md` — direção e arquitetura de publicação.
- `agents/brand-guardian.md` — verificação de marca/claims.
- `agents/visual-critic.md` — revisão independente.

### Motores e referências avaliados

| Projeto | Papel | Licença/estado verificado | Decisão |
|---|---|---|---|
| [StPageFlip / page-flip](https://github.com/Nodlik/StPageFlip) | Motor JS sem dependências, páginas HTML/imagens, modos portrait/landscape, folhas rígidas/flexíveis | MIT; package.json consultado com versão 2.0.7 | Candidato prioritário para prova de conceito React. Validar manutenção, acessibilidade, tamanho, touch, zoom/pan e compatibilidade antes de adoção. |
| [create-photo-flipbook-ui](https://github.com/HaichaoLihc/create-photo-flipbook-ui) | Skill de direção de arte para fotolivros e zines, com ideação, plano de sequência e geração de spreads | Repositório externo; skill exige geração de toda abertura com ImageGen e inclui runtime 3D de hardcover | Referência de direção criativa/ritmo, não incorporar integralmente ao fluxo corporativo quando texto exato, selecionável e editável for obrigatório. Não consta instalado no registro do ChatGPT nem como submódulo TS. |
| [flip-book-jquery](https://github.com/iberezansky/flip-book-jquery) | Motor 3D jQuery para PDF, imagens e HTML | GPL-2.0; dependências/empacotador antigos e pacote sem testes implementados no script npm | Não priorizar para projeto novo sem auditoria de compatibilidade e revisão das obrigações GPL. |
| [DearFlip JS Flipbook](https://github.com/dearhive/dearflip-js-flipbook) | Visualizador de PDF/imagens com modos 2D/3D | Repositório público identifica versão lite como CC BY-NC-ND 4.0, não comercial e sem derivados | Não usar como base de produto comercial. Investigar versão comercial apenas se houver orçamento; priorizar alternativa MIT. |
| [FlipHTML5 MCP](https://fliphtml5.com/pt/features/mcp/) | Publicação, conversão e gestão de flipbooks pela plataforma | MCP não conectado nesta conta; exige conta e API key | Opcional apenas para workflow de publicação/gestão. Não substitui direção de arte nem editor de layout. |

### Estado observado no projeto Guardian Seg (18/11/2026)

- `src/components/MagazineFlipbook.tsx` implementa o leitor React próprio.
- O componente importa React e ícones Lucide, não StPageFlip, DearFlip, flip-book-jquery ou o runtime create-photo-flipbook.
- O package.json inclui Three.js e React Three Fiber para outras partes do projeto, mas o componente de flipbook consultado não importa esses pacotes.
- Não há dependência de motor externo de flipbook identificada no package.json/lockfiles consultados.

**Decisão:** manter o leitor existente enquanto se corrige o sistema editorial. Criar uma prova de conceito isolada com StPageFlip só depois das páginas-piloto; comparar recursos e qualidade antes de qualquer migração. Não instalar vários motores simultaneamente em produção.

### Ferramentas de criação e revisão

- Figma: grid, páginas-mestre, componentes e tokens editáveis.
- Canva/Adobe: composição visual e assets, conforme exigência de editabilidade e controle tipográfico.
- HTML/CSS/SVG: montagem precisa de páginas com texto nativo e responsivo.
- Cloudinary: biblioteca e entrega de imagens, sem substituir direção criativa.
- Browser/Playwright: screenshots e medidas objetivas; inspecionar cada página e spreads em viewports reais.
- fal.ai/Comfy Cloud/Adobe: imagens e ilustrações quando necessárias; estimar créditos antes de produzir e manter texto fora da imagem gerada.

**Não existe um MCP único que transforme copy e assets automaticamente em uma revista de qualidade.** As skills organizam o trabalho; o motor publica/apresenta; a direção editorial e a crítica definem a qualidade.


## 12. Fotografia incorporada, raster-to-vector e SVG fotorrealista

Nova skill: `image-to-vector-pipeline/SKILL.md`. Consultar quando uma peça exigir fotografia real incorporada em SVG, vetorização de raster ou otimização vetorial diferenciável.

### Regra prática
Para posts comerciais com fotografia fotorrealista, preferir SVG híbrido: foto original autorizada incorporada como raster + tipografia, logo, recortes, máscaras, gradientes e elementos gráficos em vetor. Vetorizar a fotografia inteira somente quando o estilo final pedir posterização, mosaico, gravura ou ilustração por camadas.

### Motores e pesquisa
| Ferramenta | Função correta | Licença/custo/estado observado | Decisão |
|---|---|---|---|
| [VTracer](https://github.com/visioncortex/vtracer) | Raster → SVG por clustering de cores, regiões e curvas; possui binding Python | MIT; documentação atual mostra `Config` e linha 1.0.0 alpha | Principal primeira experiência open-source para posterização/vetorização de raster; testar versão e parâmetros isoladamente. A API antiga `convert_image_to_svg_py` não deve ser presumida como atual. |
| [DiffVG](https://github.com/BachiLi/diffvg) | Rasterização vetorial diferenciável e otimização de paths contra imagem-alvo | Apache-2.0; infraestrutura científica/PyTorch, potencialmente exigente | Referência técnica, não conversor semântico pronto. |
| [PyTorch-SVGRender](https://github.com/ximinng/PyTorch-SVGRender) | Coleção de técnicas de renderização/vetorização; inclui LIVE image-to-SVG por camadas | MPL-2.0; projeto ativo, documentação com API ainda incompleta | Laboratório de pesquisa para provas de conceito image-to-SVG. |
| [Chat2SVG](https://github.com/kingnobro/Chat2SVG) | LLM + template SVG + SDEdit/ControlNet + SAM + otimização de paths | Código público; licença não identificada por SPDX no repositório consultado; dependências e modelos pesados | Referência experimental principalmente text-to-SVG; não confundir com vetorizar uma foto fornecida. |
| [Vectorizer.AI](https://vectorizer.ai/api) | Vetorização por API | Pago por créditos; preços consultados em https://vectorizer.ai/pricing | Fallback pago opcional, nunca pressupor uso gratuito. |
| [Illustrator MCP Server](https://github.com/ie3jp/illustrator-mcp-server) | Controle local do Illustrator, manipulação vetorial e export | Servidor MIT, mas requer Adobe Illustrator instalado e licenciado; macOS/Windows, Node 20+ | Não priorizar para ambiente Linux/custo zero. |

Não confundir ferramenta open-source com pipeline leve: DiffVG, PyTorch-SVGRender e Chat2SVG podem exigir ambiente de pesquisa, downloads de modelos e GPU. Conferir versão, licença, modelos, VRAM/RAM e custo antes de instalar. Nunca instalar vários motores por tentativa.