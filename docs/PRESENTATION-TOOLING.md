# Apresentações, slides e propostas — catálogo operacional

**Curadoria verificada em 18/11/2026.** Estrelas e atividade são fotografias do GitHub nessa data, não avaliações de qualidade. Revisar antes de atualizar upstreams. O objetivo é privilegiar ferramentas gratuitas, open-source, reutilizáveis e que produzam arquivos editáveis.

## 1. Recomendação principal

| Projeto | Estrelas em 18/11/2026 | Licença | Última atividade observada | Uso e decisão |
|---|---:|---|---|---|
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 78.282 | MIT | 18/11/2026 | **Principal para PPTX nativo.** Geração, reconstrução, edição, templates, formas, gráficos e animações. Instalar a Skill via CLI; evitar submodule do repositório inteiro por seu tamanho/histórico. |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 32.541 | MIT | 23/06/2026 | **Principal para HTML animado.** Apresentações single-file, navegação e conversão de PPTX para HTML. O upstream está há vários meses sem novo push; validar compatibilidade antes de usar. |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 30.053 | AGPL-3.0 | 30/10/2026 | HTML deck com direção editorial e Swiss Style, presenter mode e layouts próprios. Usar quando o formato web for adequado; atenção à AGPL. |

### Instalação de PPT Master

O repositório principal é grande (metadados GitHub indicavam cerca de 138 MiB; o FAQ do upstream alerta que um clone completo pode ultrapassar 1 GB com histórico, e a Skill-only archive fica em torno de 56 MB). O upstream oferece instalação somente da Skill, que é preferível:

~~~bash
npx skills add https://github.com/hugohe3/ppt-master --skill ppt-master
~~~

Para instalar globalmente em clientes compatíveis com a CLI de Skills, usar as opções globais e de agentes documentadas pela própria CLI. O comando acima adiciona a Skill ao ambiente local do agente; **não** cria um MCP, não autentica Google/Canva e não instala um serviço remoto.

Licença MIT. O upstream inclui scripts, referências e um attribution guard obrigatório. Seguir o próprio SKILL.md original, sem copiar apenas o prompt principal e omitir verificações.

## 2. Fontes originais adicionadas como submodules

Os originais ficam em upstream/; não editar esses diretórios. Adaptações TS Digitais ficam nas Skills próprias da raiz.

| Submodule | Commit fixado | Licença | Finalidade |
|---|---|---|---|
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 9906a34d640d2111f724544cbc50f7f130569ae1 | MIT | Fonte upstream para a Skill local frontend-slides/. |
| [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 93d21bf4a73a851907a6eb00acbf30618236667a | AGPL-3.0 | Referência para apresentações HTML editoriais/Swiss. |
| [pptx-tools](https://github.com/jongalloway/pptx-tools) | ccd99730d6274365284dbcc288b207bece4fc549 | MIT | MCP/.NET para ler, atualizar e preencher PPTX existente. |

Recuperar os fontes com:

~~~bash
git submodule update --init --recursive
~~~

O repositório principal fixa commits específicos para reprodutibilidade. Antes de atualizar, revisar diferenças, licença, dependências, scripts de instalação e permissões.

## 3. MCPs e conectores

### Google Slides — oficial

O Google mantém um MCP remoto oficial para Slides no **Developer Preview Program**. Ele permite ler estrutura, estilos e layouts, alterar slides e executar atualizações em lote. Não é um repositório para adicionar como submodule.

Requisitos observados:
- Participação elegível no Google Workspace Developer Preview Program.
- Projeto Google Cloud e OAuth 2.0.
- O cliente OAuth usado pelo agente deve estar marcado em Google Auth Platform como **“Use this client for an AI-powered agent”**. A exigência passou a valer em 11/11/2026 para MCPs Google Workspace.
- O MCP oficial ainda está em Developer Preview; não assumir disponibilidade ou conexão até testar o host e a conta.

Documentação:
- https://developers.google.com/workspace/slides/api/guides/configure-mcp-server
- https://developers.google.com/workspace/slides/release-notes

### Canva — oficial

A Canva documenta seu próprio MCP remoto para assistentes, criação e edição, assets, Brand Kits, templates, busca e exportação. O catálogo visual TS Digitais já registra o conector Canva; reutilizar essa integração em vez de instalar um segundo servidor comunitário. Verificar autenticação, permissões e recursos do plano antes de executar.

Documentação:
- https://www.canva.dev/docs/apps/mcp/
- https://www.canva.dev/blog/developers/canva-and-coding-agents-platforms/

### MCPs comunitários ou de nicho

| Projeto | Estrelas | Licença/atividade | Capacidades | Decisão |
|---|---:|---|---|---|
| [2slides/mcp-2slides](https://github.com/2slides/mcp-2slides) | 34 | MIT; push 01/09/2026 | Wrapper MCP para serviço 2slides hospedado; usa API key e créditos por página/operação. | **Referência opcional, não padrão gratuito.** O README indica 1 crédito/página no Fast PPT, 100 créditos/página para slides gerados por imagem em 1K/2K, 200 em 4K e 210/página para narração. Não executar sem autorização explícita de consumo. |
| [matteoantoci/google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp) | 191 | Sem licença SPDX declarada; push 15/08/2026 | Servidor local Node/stdio para a Google Slides API, OAuth Desktop. | Não adicionar como fonte executável: licença não identificada e já existe alternativa oficial em Developer Preview. |
| [jongalloway/pptx-tools](https://github.com/jongalloway/pptx-tools) | 9 | MIT; .NET 10 | Ler slides, masters/layouts, preencher placeholders, editar conteúdo e atualizar gráficos existentes. | Submodule apenas como referência técnica. Não é ferramenta de design generativo; não cria gráficos do zero nem altera masters/temas. |
| [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) | 1,9 mil | MIT; **arquivado em 03/03/2026** | MCP Python/python-pptx para PowerPoint. | Não instalar: projeto arquivado. |
| [anyideaz/pptx-skills](https://github.com/anyideaz/pptx-skills) | 12 | Licença não identificada; push 29/04/2026 | Skills/comandos para analisar e preencher templates PPTX no Claude Code e Copilot. | Manter somente como referência; pouca adoção e licença não confirmada. |

### Zapier e 2Slides

Zapier MCP é uma integração de automação, não uma engine open-source de design de slides. Avaliar plano, tarefas, permissões e ações antes de conectar. O MCP 2Slides é um wrapper de API hospedada: ter o código do servidor não torna a geração gratuita. Não salvar API keys em arquivos de configuração, repositório, issues ou exemplos versionados.

## 4. Propostas comerciais

| Referência | O que faz | Decisão |
|---|---|---|
| upstream/alireza-claude-skills/business-growth/skills/contract-and-proposal-writer/SKILL.md | Skill já presente no submodule alireza-claude-skills; estrutura propostas, SOWs, contratos e NDAs. Licença MIT do upstream. | Consultar para estrutura documental; suas jurisdições e cláusulas são US/EU/UK/DACH, não aplicar automaticamente ao Brasil. |
| [Mikefluff/skills — proposal-maker](https://github.com/Mikefluff/skills/tree/main/skills/proposal-maker) | Skill MIT, 28 estrelas observadas; gera HTML de proposta com marca e impressão em PDF. | Referência de nicho; não é gerador de PPTX e tem pipeline voltado a outro contexto linguístico. |
| Proposal Generator / Proposal Document / Agency Proposal Template | Os nomes são descrições genéricas, não identificam por si só um upstream canônico único. | Criamos a Skill TS Digitais commercial-proposal/SKILL.md, com escopo, preço, cronograma, ROI e limites verificáveis. |

A Skill local de propostas deve sempre usar valores e condições comerciais aprovados no trabalho atual. Não reutilizar preços antigos, inventar ROI, provas sociais, prazos ou cláusulas jurídicas.

## 5. Produtos SaaS não instaláveis neste repositório

- **Gamma**, **Presentations.AI** e **Manus** são produtos hospedados, não Skills open-source ou MCPs que se instalem como parte deste repositório. Podem ser avaliados pontualmente, mas não são o caminho padrão da TS Digitais.
- O agente/template de propostas para Notion não teve um repositório canônico, licença e pacote de instalação confirmados. Não importar com base apenas em post de rede social.
- Não confundir uma ferramenta listada em catálogo com uma aplicação autenticada ou uma licença gratuita sem limites.

## 6. Roteamento recomendado para TS Digitais

1. **PPTX nativo e editável:** PPT Master, se instalado no ambiente local compatível.
2. **Apresentação HTML:** Skill local frontend-slides; considerar Guizang para estética editorial/Swiss.
3. **Template PPTX já existente:** pptx-tools para ler e preencher; direção visual e criação complexa ficam no editor/gerador apropriado.
4. **Google Slides colaborativo:** MCP oficial apenas depois de habilitar Developer Preview e autenticar OAuth corretamente.
5. **Canva:** reutilizar o conector já listado no catálogo da TS Digitais.
6. **Proposta comercial:** commercial-proposal + presentation-studio; entregar PPTX editável e PDF quando houver runtime capaz de gerar e validar ambos.

## 7. Segurança, custos e validação

- Ler agents/mcp-privacy-auditor.md antes de instalar/ativar qualquer MCP.
- Preferir permissões read-only no começo. Não inserir tokens, segredos ou dados privados de clientes em GitHub.
- Não enviar documentos comerciais ou pessoais para serviços externos sem necessidade e autorização.
- Verificar dependências (Node, Python, .NET), licença, manutenção, transporte MCP (stdio/HTTP), autenticação e destinos de rede.
- Confirmar créditos/custos antes de qualquer geração em serviço hospedado.
- Renderizar e inspecionar o resultado final, slide por slide/página por página. Não declarar “aprovado” sem preview real.

## 8. Fontes oficiais e upstreams

- PPT Master: https://github.com/hugohe3/ppt-master
- Frontend Slides: https://github.com/zarazhangrui/frontend-slides
- Guizang: https://github.com/op7418/guizang-ppt-skill
- pptx-tools: https://github.com/jongalloway/pptx-tools
- Google Slides MCP: https://developers.google.com/workspace/slides/api/guides/configure-mcp-server
- Canva MCP: https://www.canva.dev/docs/apps/mcp/
- 2Slides MCP: https://github.com/2slides/mcp-2slides
- Proposal Maker: https://github.com/Mikefluff/skills/tree/main/skills/proposal-maker
- Proposal writer existente: https://github.com/alirezarezvani/claude-skills
