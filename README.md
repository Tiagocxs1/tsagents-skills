# TS Agents Skills

Biblioteca reutilizável de skills para os projetos TS Digitais. As skills são organizadas em pastas com um arquivo `SKILL.md` e referências/scripts quando aplicável. Os projetos originais avaliados ficam separados como Git submodules em `upstream/`; nossas adaptações permanecem na raiz.

## SEO, pesquisa e auditoria técnica

| Skill / runtime | Uso |
|---|---|
| [Google Trends Research](./google-trends-research/SKILL.md) | Trendspyg 1.9.0 (MIT), compatibilidade para projetos Pytrends, comparação de interesse e tendências |
| [Technical SEO Audit](./technical-seo-audit/SKILL.md) | Lighthouse 13.6.0 para lab de 1–5 URLs e SiteOne Crawler v2.5.1 para crawls limitados do site; relatórios HTML/JSON sem servidor permanente |
| [Coletor Google Trends](./.github/workflows/google-trends-collect.yml) | GitHub Actions reutilizável, execução mensal/manual e relatório privado por projeto |
| [Coletor Lighthouse](./.github/workflows/lighthouse-collect.yml) | GitHub Actions reutilizável, até cinco URLs por execução, mobile/desktop e relatórios na branch separada seo-reports |
| [Coletor SiteOne](./.github/workflows/siteone-crawler-audit.yml) | GitHub Actions reutilizável, crawler Rust MIT com URL/depth/rate limits e relatório de site inteiro na branch separada seo-reports |

Google Trends fornece índice relativo 0–100, não volume absoluto, CPC ou concorrência de anúncios. Lighthouse fornece medições de laboratório, não dados de campo nem garantia de ranking. SiteOne usa uma escala própria de qualidade de 0–10; não comparar diretamente com Lighthouse. Os workflows dos repositórios privados consomem minutos da cota incluída do GitHub Actions; não são execução ilimitada. O Pytrends original está arquivado; projetos novos devem usar Trendspyg e a camada de compatibilidade quando aplicável.

## UI, UX e qualidade de produto

| Skill | Uso |
|---|---|
| [ui-ux-pro-max](./ui-ux-pro-max/SKILL.md) | Design systems, padrões visuais, UX, pesquisa de estilos e boas práticas por stack |
| [responsive-web-adaptation](./responsive-web-adaptation/SKILL.md) | Adaptação de app shells, navegação, painéis e layouts para desktop/tablet/mobile |
| [web-interface-guidelines](./web-interface-guidelines/SKILL.md) | Acessibilidade, teclado, foco, formulários, navegação e acabamento web |
| [accessibility-compliance-wcag-audit-patterns](./accessibility-compliance-wcag-audit-patterns/SKILL.md) | Auditoria e correção de acessibilidade WCAG |
| [accessibility-compliance-screen-reader-testing](./accessibility-compliance-screen-reader-testing/SKILL.md) | Testes de leitores de tela |
| [design-system](./design-system/SKILL.md) | Tokens, componentes, tipografia, cores e consistência |
| [design-taste-frontend](./design-taste-frontend/SKILL.md) | Direção visual e revisão de landing pages/portfólios (não usar como regra única para dashboards) |

## Engenharia e especificação

| Skill | Uso |
|---|---|
| [spec-driven-development](./spec-driven-development/SKILL.md) | Especificar, planejar, dividir tarefas, implementar e verificar mudanças; inspirado no GitHub Spec Kit |
| [privacy-by-design](./privacy-by-design/SKILL.md) | Engenharia de privacidade e minimização para qualquer produto que trate dados pessoais |
| [privacy-legal](./privacy-legal/SKILL.md) | Análise procedimental LGPD/GDPR, direitos, RIPD/DPIA e fontes oficiais |
| [leis-mcp](https://github.com/mazulo/leis-mcp) | MCP opcional e local para consultar e citar legislação brasileira (inclui LGPD); requer configuração no cliente MCP |
| [messaging-private-storage](./messaging-private-storage/SKILL.md) | Segurança de mensageria, isolamento de usuários, uploads, downloads e retenção |

## Instalação por projeto

Use a CLI de skills para instalar somente o que o projeto precisa:

```bash
npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill responsive-web-adaptation
npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill web-interface-guidelines
npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill spec-driven-development
```

Para UI/UX, instale também `ui-ux-pro-max`. Para auditorias de acessibilidade, instale as duas skills WCAG conforme o escopo do projeto.

## Fontes e atribuição

- UI/UX Pro Max: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), MIT.
- Responsive adaptation: [pbakaus/impeccable](https://github.com/pbakaus/impeccable), Apache-2.0; também consulta [UI Skills](https://www.ui-skills.com/skills/frontend).
- Web Interface Guidelines: [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines), MIT.
- Spec-driven development: [github/spec-kit](https://github.com/github/spec-kit).

As skills agregadoras são guias de trabalho, não substituem a leitura das fontes oficiais. Revise os repositórios de origem antes de atualizar cópias locais e não instale dependências de UI sem necessidade demonstrada.

## Privacidade, LGPD/GDPR e segurança de agentes

| Recurso | Uso |
|---|---|
| [Privacy by Design](./privacy-by-design/SKILL.md) | Guardrails técnicos para todo tratamento de dados pessoais |
| [LGPD/GDPR](./privacy-legal/SKILL.md) | Mapeamento jurídico-procedimental com fontes oficiais e decisões pendentes |
| [Mensageria e arquivos privados](./messaging-private-storage/SKILL.md) | Autorização por objeto, RLS, storage privado, URLs assinadas, retenção e expurgo |
| [Privacy Engineer](./agents/privacy-engineer.md) | Implementação de controles e testes |
| [Privacy Reviewer](./agents/privacy-reviewer.md) | Revisão independente de segurança e privacidade |
| [MCP Privacy Auditor](./agents/mcp-privacy-auditor.md) | Avaliação de origem, licença, permissões e rede de agentes/MCPs |
| [Curadoria de ferramentas](./docs/PRIVACY-TOOLING.md) | OTTO, skills jurídicas, limitações, templates e critérios para MCPs |

Para disponibilizar as três skills em todos os projetos no computador, use a instalação global da CLI:

~~~bash
npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill privacy-by-design --skill privacy-legal --skill messaging-private-storage -g -a '*' -y
~~~

O workflow OTTO é opcional e está em [templates/github-actions/otto-privacy-review.yml](./templates/github-actions/otto-privacy-review.yml). Os templates de exclusão de arquivos sensíveis estão em [templates/privacy/](./templates/privacy/). Não foi conectado nenhum MCP jurídico externo sem origem/código verificável. Consulte a curadoria antes de ativar automações ou serviços de terceiros.

## Direção de arte, social e publicidade

| Skill | Uso |
|---|---|
| [visual-design](./visual-design/SKILL.md) | Skill obrigatória antes de qualquer arte, SVG, HTML, CSS ou JSON visual |
| [social-media-creative](./social-media-creative/SKILL.md) | Posts, stories, carrosséis, thumbnails, formatos e safe zones |
| [social-first-art-direction](./social-first-art-direction/SKILL.md) | Direção de arte social-first transversal; composições de impacto, anti-documento, imagens licenciadas e validação visual real |
| [advertising-creative](./advertising-creative/SKILL.md) | Criativos de anúncios, hooks, ofertas e testes A/B |
| [motion-design](./motion-design/SKILL.md) | Vídeos, animações e motion graphics |
| [visual-quality-review](./visual-quality-review/SKILL.md) | Revisão de qualidade antes da entrega |

## Perfis de agentes criativos

- [Creative Director](./agents/creative-director.md)
- [Brand Guardian](./agents/brand-guardian.md)
- [Ad Creative Strategist](./agents/ad-creative-strategist.md)
- [Visual Critic](./agents/visual-critic.md)

Esses arquivos são perfis reutilizáveis para subagentes ou etapas sequenciais; não representam agentes autônomos implantados.

## Regras globais

O arquivo [AGENTS.md](./AGENTS.md) exige consulta às skills visuais antes de qualquer criação e revisão do preview real antes da entrega. Para posts sociais, também exige [Social-First Art Direction](./social-first-art-direction/SKILL.md), uma regra transversal que impede que posts de impacto sejam tratados como documentos ou templates genéricos.

## Catálogos e fontes externas

- [Catálogo visual de ferramentas e MCPs](./docs/visual-tool-registry.md): ferramentas conectadas, opções externas, custos e roteamento.
- [Arsenal upstream completo](./docs/UPSTREAM-ARSENAL.md): originais, commits fixados, licenças, riscos e recomendações para copy, estratégia, UX/UI, marketing brasileiro, dados, GA4 e MCPs.
- [Fontes originais](./.gitmodules): lista de repositórios preservados como submódulos.

## Recuperar os projetos originais completos

```bash
git clone --recurse-submodules https://github.com/Tiagocxs1/tsagents-skills.git
```

Em um clone existente:

```bash
git submodule update --init --recursive
```

Os submódulos preservam o código e os arquivos originais sem modificações. O repositório principal fixa cada origem em um commit específico. Eles não ficam automaticamente instalados ou conectados em runtime.

## Instalação da biblioteca TS Digitais

    npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill visual-design
    npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill social-media-creative
    npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill advertising-creative
    npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill visual-quality-review

Instalar os módulos adicionais apenas quando necessários. O AGENTS.md é lido automaticamente apenas por agentes/ambientes que adotem esse padrão; o ChatGPT também precisa consultar os arquivos pelo conector GitHub quando iniciar uma tarefa visual.

## Runtimes MCP

- [Arquitetura de execução](./docs/MCP-RUNTIME-ARCHITECTURE.md): diferença entre GitHub Actions, Cloudflare Workers, Render e runtimes locais.
- [MCP Brasil — Render Free Docker](./runtimes/render-mcp-brasil/README.md): runtime Python/Linux com CI aprovado.
- [Checklist de implantação](./docs/RENDER-DEPLOY-CHECKLIST.md): configuração pendente na conta Render.
- [Cloudflare Python Worker experimental](./runtimes/cloudflare-mcp-brasil/README.md): não apto ao deploy devido a dependências sem wheels Pyodide compatíveis.

**Estado MCP Brasil:** CI aprovado em 18/11/2026 (build Docker, container limitado a 512 MiB, health check, handshake Bearer, descoberta BM25 e chamada read-only `listar_features`). O endpoint ainda não foi publicado; falta criar o Blueprint e definir `MCP_BRASIL_API_TOKEN` como segredo no Render. A conta ChatGPT Free não pode conectar um MCP personalizado; esse endpoint não habilita acesso automático neste chat.

## Apresentações e propostas comerciais

| Skill / referência | Uso |
|---|---|
| [presentation-studio](./presentation-studio/SKILL.md) | Orquestra a criação e revisão de PowerPoint editável, Google Slides e apresentações HTML |
| [commercial-proposal](./commercial-proposal/SKILL.md) | Propostas comerciais com escopo, entregáveis, cronograma, investimento e condições verificáveis |
| [slides](./slides/SKILL.md) | Estratégia de slides, copywriting, layouts e apresentações HTML |
| [frontend-slides](./frontend-slides/SKILL.md) | Apresentações web responsivas e animadas |
| [Catálogo de ferramentas de apresentação](./docs/PRESENTATION-TOOLING.md) | Ranking conferido, licenças, MCPs, custos e roteamento de ferramentas |

Upstreams adicionados: Frontend Slides, Guizang PPT Skill e pptx-tools. O PPT Master é instalado pelo comando da Skill CLI para evitar clonar o histórico completo do repositório. Consulte o catálogo antes de habilitar serviços por créditos ou MCPs com permissões externas.

## Perfis de marca

- [Guardian Seg — Brand Profile](./brands/guardianseg/BRAND-PROFILE.md): serviços, área de atuação, identidade visual, claims e restrições.
- [Guardian Seg — Diretrizes de conteúdo social](./brands/guardianseg/SOCIAL-CONTENT-GUIDELINES.md): pilares editoriais e guardrails para calendário/postagens.

As fichas da marca são a fonte única antes de criar conteúdo. Os números internos recebidos da equipe estão marcados como pendentes de validação de data/base. Nunca versionar tokens, chaves ou credenciais.


## Biblioteca temporária de imagens
- [Image Asset Ingestion](./image-asset-ingestion/SKILL.md): regra universal para importar, usar, recuperar e expirar fotografias de terceiros.
- [Cloudflare Image Library](./runtimes/cloudflare-image-library/README.md): Worker/MCP remoto, API, bucket R2, catálogo D1 e retenção temporária.
- Regra padrão: os binários em R2 expiram após sete dias (com processamento de exclusão normalmente concluído até 24h depois). O catálogo mantém somente metadados e URLs de origem para tentar baixar novamente — não garante recuperação se a fonte sair do ar ou exigir URL temporária.
