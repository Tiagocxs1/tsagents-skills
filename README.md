# TS Agents Skills

Biblioteca reutilizável de skills para os projetos TS Digitais. As skills são organizadas em pastas com um arquivo `SKILL.md` e referências/scripts quando aplicável. Os projetos originais avaliados ficam separados como Git submodules em `upstream/`; nossas adaptações permanecem na raiz.

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

## Direção de arte, social e publicidade

| Skill | Uso |
|---|---|
| [visual-design](./visual-design/SKILL.md) | Skill obrigatória antes de qualquer arte, SVG, HTML, CSS ou JSON visual |
| [social-media-creative](./social-media-creative/SKILL.md) | Posts, stories, carrosséis, thumbnails, formatos e safe zones |
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

O arquivo [AGENTS.md](./AGENTS.md) exige consulta às skills visuais antes de qualquer criação e revisão do preview real antes da entrega.

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

- [Arquitetura de execução](./docs/MCP-RUNTIME-ARCHITECTURE.md): diferença entre GitHub Actions, Cloudflare Workers, Durable Objects e runtimes locais.
- [Runtimes](./runtimes/README.md): adaptadores e configuração de serviços remotos.
- [MCP Brasil no Cloudflare](./runtimes/cloudflare-mcp-brasil/README.md): servidor remoto Python/Streamable HTTP, autenticação Bearer, CI e deploy manual.

Para recuperar as fontes e o runtime:

```bash
git clone --recurse-submodules https://github.com/Tiagocxs1/tsagents-skills.git
```

O runtime MCP Brasil está preparado, mas não implantado; o CI precisa validar as dependências e o smoke test antes do primeiro deploy. Nunca versionar `.dev.vars`, tokens, chaves ou credenciais.
