# TS Agents Skills

Biblioteca reutilizável de skills para os projetos TS Digitais. As skills são organizadas em pastas com um arquivo `SKILL.md` e referências/scripts quando aplicável.

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
