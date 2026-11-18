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
| https://github.com/adkit/ads-skills | Planejamento e execução de campanhas Meta/Google | Termos de redistribuição restritivos no README | Não copiar para este repositório. Avaliar apenas no ambiente externo e sob seus termos. |

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
