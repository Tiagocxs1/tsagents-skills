# Upstream sources

This directory contains Git submodules pointing to the original upstream projects. Do not edit files inside these submodules as part of TS Digitais adaptations.

To retrieve the full upstream source trees:

```bash
git submodule update --init --recursive
```

The exact source URLs, license notes, usage guidance and pinned revisions are documented in [docs/UPSTREAM-ARSENAL.md](../docs/UPSTREAM-ARSENAL.md).

## Referências de apresentações e propostas

| Submodule | Origem | Licença | Commit fixado |
|---|---|---|---|
| frontend-slides | https://github.com/zarazhangrui/frontend-slides | MIT | 9906a34d640d2111f724544cbc50f7f130569ae1 |
| guizang-ppt-skill | https://github.com/op7418/guizang-ppt-skill | AGPL-3.0 | 93d21bf4a73a851907a6eb00acbf30618236667a |
| pptx-tools | https://github.com/jongalloway/pptx-tools | MIT | ccd99730d6274365284dbcc288b207bece4fc549 |

ppt-master não é submodule porque seu upstream é grande; instalar somente a Skill com a CLI documentada em docs/PRESENTATION-TOOLING.md. A referência de proposta contract-and-proposal-writer já está no submodule alireza-claude-skills.
