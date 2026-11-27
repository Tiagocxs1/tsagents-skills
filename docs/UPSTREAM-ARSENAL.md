# Arsenal upstream — originais, skills e MCPs

**Inventário verificado em 23/11/2026.** Este documento separa projetos originais, adaptações TS Digitais, ferramentas conectadas e referências externas. A biblioteca guarda os projetos completos como **Git submodules**: os repositórios de origem não são copiados nem modificados. Cada submódulo fica fixado em um commit específico no repositório principal.

## Como obter os originais completos

Clone incluindo os submódulos:

```bash
git clone --recurse-submodules https://github.com/Tiagocxs1/tsagents-skills.git
```

Se o projeto já estiver clonado:

```bash
git submodule update --init --recursive
git submodule status
```

O arquivo `.gitmodules` lista os endereços originais. O commit gravado em cada submódulo fixa a versão consultada; atualizar o repositório de origem não muda silenciosamente a versão usada pelo projeto TS Digitais. Para atualizar, faça o avanço do submódulo conscientemente, avalie o diff/licença e registre a nova referência no repositório principal.

**Importante:** submódulo não é uma instalação de runtime. Ele disponibiliza os arquivos-fonte completos em um clone com `--recurse-submodules`, mas não executa programas, não instala dependências e não conecta contas. No ChatGPT, o conteúdo pode ser consultado abrindo os arquivos no GitHub Connector; a existência do link não faz a skill carregar automaticamente em toda conversa.

## 1. Originais completos adicionados como submódulos

| Projeto original | Licença verificada | Especialidade e como usar |
|---|---|---|
| [Social Media Skills](https://github.com/social-media-skills/skills) | MIT | Coleção modular para estratégia social, identidade de marca, templates, carrosséis, thumbnails, infográficos, prompts e conteúdo. Consultar os módulos relevantes antes de criar peças sociais. |
| [Corey Haines — Marketing Skills](https://github.com/coreyhaines31/marketingskills) | MIT | Copywriting, psicologia de marketing, CRO, campanhas e conteúdo. Complementa, não substitui, estratégia específica de canal e briefing de marca. |
| [Kostja94 — Marketing Skills](https://github.com/kostja94/marketing-skills) | MIT | Catálogo de 160+ skills divulgado pelo próprio projeto, cobrindo SEO, conteúdo, páginas, anúncios, canais e analytics. Escolher apenas skills pertinentes; não carregar todo o catálogo em cada tarefa. |
| [Hedgehog — Prose Engineering](https://github.com/skyf0xx/hedgehog-core-copywriting-prose-engineering) | MIT | Verificação programática de vícios de texto, legibilidade, variedade de frases, voz passiva e critérios por formato, com ciclos de revisão. A compatibilidade linguística deve ser testada em PT-BR; não presumir que regras/NLP em inglês funcionem igualmente em português. |
| [Alireza Rezvani — Claude Skills](https://github.com/alirezarezvani/claude-skills) | MIT | Biblioteca ampla: o README atual anuncia 428 skills, 136 agentes, 824 scripts Python e 931 documentos de referência, com suporte a vários agentes. Priorizar os bundles de marketing, produto, SEO, CRO e pesquisa; é uma coleção multidomínio, não uma única skill. |
| [Superpowers](https://github.com/obra/superpowers) | MIT | Metodologia de desenvolvimento: brainstorming, especificação, planos, TDD, subagentes, revisão e fechamento. Usar em projetos de engenharia com várias etapas; não aplicar ao fluxo de posts simples ou peças de rotina. |
| [UI/UX Agent Skill System](https://github.com/sergekostenchuk/ui-ux-agent-skill-system) | Apache-2.0 | Orquestrador e skills especialistas de UX/UI, com adaptadores para múltiplos agentes e integração opcional com ferramentas como Figma. Consultar para fluxos completos de descoberta, arquitetura e handoff. |
| [UX/UI Agent Skills (XIAS)](https://github.com/plugin87/ux-ui-agent-skills) | MIT | Sistema extenso de design e revisão: tokens, componentes, acessibilidade WCAG e gates de qualidade. O README anuncia 26 skills, 2.144 sistemas de design e 52 gates; verificar quais gates realmente se aplicam ao stack e ao navegador disponível. |
| [Jakub Krehel — Interface Review Skills](https://github.com/jakubkrehel/skills) | MIT | Skills de avaliação e melhoria da interface, incluindo hierarquia, layout, tipografia, cores e acessibilidade. Boa etapa de crítica independente após implementação. |
| [Google Analytics MCP](https://github.com/googleanalytics/google-analytics-mcp) | Apache-2.0 | MCP oficial no namespace GitHub Google Analytics para consultar dados de propriedades GA4. O modo de consulta é o ponto de partida; ferramentas de escrita são opcionais e dependem de `--allow-write` e escopo OAuth de edição. Requer configuração de Google Cloud/ADC e acesso à propriedade. |
| [Skills Marketing BR](https://github.com/tiago1002bravy/skills-marketing) | MIT | Projeto em português com skills para carrossel, landing pages e criativos Meta Ads; inclui renderização HTML/JSON e validação de fatos. A publicação via Instagram Graph API exige credenciais e autorização explícita; nunca publicar automaticamente. |
| [MCP Brasil](https://github.com/Mcp-Brasil/mcp-brasil) | MIT para o código | MCP comunitário que declara 70 fontes públicas brasileiras, com APIs de economia, IBGE, legislativo, transparência, dados eleitorais, educação, ambiente e outros temas. As fontes de dados têm termos próprios; ler sempre `ACCEPTABLE_USE.md` e `SOURCES.md` antes de uso. Há regras estritas para dados pessoais/sensíveis, saúde, eleições e judiciário. Não usar para perfilamento, reidentificação ou marketing com dados sensíveis. |
| [Ruben Marcus — Agent Skills](https://github.com/rubenmarcus/agent-skills) | MIT | 11 workflows para pesquisa com fontes, AEO, revisão adversarial, debugging, quality gates, planejamento e coordenação. O próprio projeto declara que sua avaliação comportamental ainda é limitada; usar como método e validar os resultados, não como prova de eficácia. |
| [MCP Dev LATAM](https://github.com/codespar/mcp-dev-latam) | MIT | Catálogo de conectores MCP de comércio e operação na América Latina, incluindo serviços brasileiros. O README informa que cerca de um terço dos pacotes está em alpha e que algumas rotas são estimadas; instalar somente pacotes marcados como estáveis e confirmar endpoints na documentação oficial do provedor. |
| [Asaas MCP](https://github.com/theYahia/asaas-mcp) | MIT | Integração independente para cobranças, Pix, clientes, assinaturas e estorno. Exige chave Asaas. Como inclui ações financeiras e irreversíveis, testar em sandbox e exigir confirmação explícita antes de qualquer escrita. |
| [Hotmart MCP](https://github.com/thaleslaray/hotmart-mcp) | MIT | Integra vendas, assinaturas, produtos, área de membros, cupons e eventos. Algumas ferramentas cancelam, estornam ou alteram dados; usar leitura primeiro, proteger credenciais e pedir confirmação explícita antes de toda ação de escrita. |

### Critérios de roteamento

- **Post, carrossel, story e calendário editorial:** social-media-skills + skills-marketing-br quando o texto/destino for PT-BR + Corey/Kostja para estratégia e copy + visual-design/social-media-creative + visual-quality-review.
- **Copy de landing page, e-mail e oferta:** Corey + Kostja ou Alireza (selecionar uma skill adequada) + Hedgehog como verificador complementar, com regras PT-BR revistas manualmente.
- **Anúncios:** advertising-creative + ad-creative/skill relevante; comparar as regras das plataformas e nunca inventar alegações, provas ou métricas.
- **UX/UI e site/app:** XIAS para sistema/tokens/controles, UI/UX Agent Skill System para orquestração e Jakub Krehel para crítica; combinar com ui-ux-pro-max e as ferramentas Figma/MagicPath já conectadas.
- **Pesquisa de mercado brasileira:** MCP Brasil para dados públicos agregados e fontes permitidas, junto com source-backed-research e validação na fonte primária. Nunca tratar resultado de IA como dado oficial sem checagem.
- **GA4:** Google Analytics MCP em modo de leitura primeiro; conferir propriedade, escopos e credenciais antes da configuração.
- **Cobrança e vendas:** MCP Dev LATAM / Asaas / Hotmart somente para o sistema/conta que o usuário identificar e autorizar; leitura antes de escrita, sandbox antes de produção.

### Skills sociais ativadas pelo Social Content System

O submódulo Social Media Skills já estava presente no repositório e está fixado no commit `f28cef2b7067ec64e79c9d85421c022c06659e03`. O submódulo Corey Haines já estava presente e está fixado no commit `73573e94a06a39965978b3fa1f9c1eace8cebc7c`. A alteração de 23/11/2026 não duplicou esses originais: adicionou um roteador local e agentes multi-marca que convocam os módulos corretos.

Módulos selecionados para o fluxo social:

- Social Media Skills: `audience-research`, `competitor-analysis`, `content-research-and-sourcing`, `social-strategy`, `content-pillars`, `content-calendar`, `batch-content-plan`, `seasonal-and-moment-marketing`, `educational-content-and-how-to`, `storytelling-and-narrative`, `hook-writer`, `caption-writer`, `carousel-writer` e `story-writer`.
- Social Media Skills — imagem: `image-prompt/SKILL.md` e `image-prompt/references/prompt-anatomy.md`, roteadas por `layered-image-prompting/SKILL.md` para copy literal, camadas de profundidade e hierarquia tipográfica.
- Corey Haines Marketing Skills: `content-strategy`, `customer-research`, `copywriting` e `social`.

Os caminhos completos são listados em `social-content-system/SKILL.md`. Para carregá-los em outro clone, inicializar os submódulos. A existência do submódulo não significa que todas as skills estejam permanentemente carregadas em todo runtime; o roteador instrui o agente a abrir cada arquivo no momento da tarefa.

## 2. Referências avaliadas — não copiadas como submódulos

| Projeto / link | Motivo para não copiar integralmente | Como aproveitar |
|---|---|---|
| [Kursku — Skills em PT-BR](https://github.com/kursku/skills) | Repositório declara milhares de skills e conteúdo em português, mas não apresenta licença de reuso identificável no metadado/arquivo consultado. | Consultar apenas como diretório de descoberta; não copiar nem redistribuir os arquivos até existir licença clara. Também avaliar origem e qualidade de cada skill. |
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | Coleção oficial útil para React/Next.js e performance, mas não foi encontrada licença no caminho `LICENSE` do repositório durante a verificação. | Link externo para consulta; não duplicar arquivos no nosso repositório sem esclarecer os termos. |
| [AdKit Ads Skills](https://github.com/adkit/ads-skills) | O README declara MIT para o repositório, mas duas skills (`meta-ads-strategy` e `google-ads-strategy`) usam licença própria, sem redistribuição e sem uso em produto concorrente. O MCP de execução é um serviço externo. | Consultar apenas os módulos permitidos no upstream; não copiar as duas skills de licença especial. Estratégia pode ser lida sem o MCP; publicar campanhas exige autorização e pode depender de serviço pago. |
| [AI Marketing Suite for Claude Code — repositório localizado](https://github.com/7711222/AI-Marketing-Suite-for-Claude-Code) | O README anuncia 14 skills e 5 subagentes, mas seus comandos de instalação apontam para outro repositório (`zubair-trabzada/ai-marketing-claude`). Inconsistência de procedência/instalador. | Manter em observação; não executar o instalador nem presumir que o repositório anunciado e o código localizado sejam a mesma origem. |
| [Claude UX Designer Agent — Awesome Copilot](https://github.com/github/awesome-copilot/blob/main/agents/se-ux-ui-designer.agent.md) | É um arquivo específico dentro de um repositório muito grande, não uma coleção de UX para importar inteira. O arquivo original e a licença MIT do projeto foram consultados. | Link para o agente JTBD/jornada do usuário; consultar quando a tarefa exigir descoberta e jornada antes do Figma. |
| [Awesome MCP Servers — PT-BR](https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-pt_BR.md) | Diretório curado e muito grande, não um servidor MCP único. | Usar para descobrir candidatos; avaliar cada servidor individualmente. |
| [GitHub Topic: SEO Agent MCP](https://github.com/topics/seo-agent-mcp) | Página de tópico, não um servidor específico. | Usar para encontrar novos candidatos de SEO e verificar cada licença, manutenção e escopo. |
| [Hotmart CLI](https://github.com/murilloimparavel/hotmart-cli) | Embora o repositório tenha licença MIT, seu README declara o projeto em construção e marca módulos centrais/servidor MCP como planejados; algumas funções são descritas como reverse-engineered. | Não usar como integração operacional até que o status de implementação e os endpoints estejam validados. Preferir avaliar o Hotmart MCP separado. |

### Links incompletos corrigidos

- O link do MCP Brasil aponta para `Mcp-Brasil/mcp-brasil` (maiúsculas do proprietário conforme GitHub).
- O projeto de Alireza Rezvani foi identificado como `alirezarezvani/claude-skills`.
- O nome Hedgehog foi associado ao projeto `skyf0xx/hedgehog-core-copywriting-prose-engineering`; a URL original no material recebido estava incompleta.
- O AI Marketing Suite identificado tem divergência entre a URL do repositório e a URL do instalador, por isso continua em observação.

## 3. Política de integração e segurança

1. **Original preservado:** submódulos são mantidos sem edição; nossas regras e adaptações permanecem fora deles, no restante do repositório TS Digitais.
2. **Licença por projeto:** MIT ou Apache-2.0 do código não substitui os termos das APIs/datasets utilizados pelo projeto. Guardar LICENSE, NOTICE, AUP e termos das fontes de dados.
3. **Sem credenciais no Git:** nunca inserir tokens, client secrets, chaves Asaas/Hotmart, credenciais Google ou arquivos ADC em commits, skills, exemplos preenchidos ou screenshots.
4. **Leitura primeiro:** qualquer MCP conectado a contas começa com operações de consulta, quando disponíveis. Ações de escrita, cancelamento, estorno, cobrança, publicação ou alteração exigem autorização explícita, confirmação contextual e preferencialmente sandbox.
5. **Sem falsa instalação:** submódulos disponíveis não significam MCP conectado, API autenticada, programa executando ou skill automaticamente carregada no ChatGPT.
6. **Sem custo presumido:** verificar planos, limites, créditos e custo de API antes de executar integrações; priorizar ferramentas existentes e modos gratuitos.
7. **Sem confiar em afirmações de marketing:** contagens, pontuações, métricas de desempenho e claims dos READMEs são declarações dos autores até serem reproduzidas em avaliação independente.

## 3.1 Google Trends — Trendspyg

- Repositório: https://github.com/flack0x/trendspyg
- Licença: MIT; versão adotada no coletor compartilhado: `1.9.0`.
- Uso: tendências atuais por RSS, interesse relativo no tempo, comparação de 2–5 termos na mesma escala, consultas relacionadas e interesse por região.
- Compatibilidade: inclui `trendspyg.compat.request.TrendReq` para migrar fluxos comuns do Pytrends 4.9.2; não é uma substituição integral. Conferir `docs/MIGRATING_FROM_PYTRENDS.md`.
- Limite dos dados: o índice de 0–100 é relativo ao termo/conjunto, país e janela escolhida; não representa volume absoluto mensal, CPC ou concorrência de anúncios.
- Runtime adotado: GitHub Actions reutilizável em `.github/workflows/google-trends-collect.yml`, com uma coleta mensal/manual no repositório privado chamador. O runner é efêmero; nenhum cookie Google ou credencial é persistido. Os relatórios vão para a branch privada `seo-reports`, não para a branch de produção, e também ficam disponíveis como artifact de 30 dias.
- Rate limit: no máximo uma chamada Explore/comparação por execução, `engine="auto"`, `max_retries=1`, sem retry loop para 403/429. Parar a coleta quando o Google bloquear.
- **Status:** skill, coletor e workflow compartilhado foram integrados à biblioteca TS Agents Skills; primeira configuração privada da Guardian está em PR separado, sem merge porque o repositório dispara deploy HostGator em qualquer push para `main`.
- O extra `trendspyg[mcp]` disponibiliza MCP local por stdio. Não é serviço remoto HTTP, não foi instalado no computador do usuário e não fica conectado automaticamente ao ChatGPT.

## 3.2 Google Lighthouse — auditoria técnica por GitHub Actions

- Repositório: https://github.com/GoogleChrome/lighthouse
- Licença: Apache-2.0.
- Versão fixada: 13.6.0; Node.js 24 no runner.
- Uso: auditoria lab de Performance, Accessibility, Best Practices e SEO; exporta relatórios HTML/JSON e resumo de métricas.
- Runtime: workflow reutilizável `.github/workflows/lighthouse-collect.yml`, máximo de cinco URLs públicas HTTPS por execução, manual/mensal.
- Relatórios: artifact de 30 dias e branch separada `seo-reports` no repositório chamador. Nunca fazer commit no ramo de produção que dispara deploy.
- Segurança: rejeita HTTP, localhost, nomes locais, IPs não globais, credenciais embutidas, query strings e fragmentos. Não autentica em páginas privadas nem usa cookies.
- Limitação: são medições de laboratório. Para Core Web Vitals de campo, usar CrUX/PageSpeed Insights e Search Console quando disponíveis.
- **Status:** skill e runner implementados; CI de sintaxe/configuração/testes será validado antes do merge. O primeiro caller privado da Guardian será separado e não será integrado à main enquanto o deploy de produção for acionado por push nessa branch.

## 3.3 SiteOne Crawler — auditoria técnica por GitHub Actions

- Repositório: https://github.com/janreges/siteone-crawler
- Licença: MIT; aproximadamente 1.017 estrelas no inventário de 20/11/2026.
- Versão usada pelo workflow: v2.5.1 (Linux x64 musl).
- SHA-256 do archive fixado: `bd96b9502563aea2581fc248625871e69b60d7f1bb68a484f226c551c73706fd`.
- Runtime: GitHub Actions reutilizável `.github/workflows/siteone-crawler-audit.yml`; runner baixa release, valida checksum, executa binário e exporta HTML/JSON. Não requer banco ou servidor persistente.
- Limites padrão: 300 URLs visitadas (incluindo assets), profundidade 4, dois workers, duas requisições/s e timeout de 10 s. A configuração valida até 500 URLs, profundidade 6, três workers e 2 req/s.
- O crawler respeita robots.txt por padrão; o workflow não ativa stress/load testing, não usa proxy e não envia relatórios para serviços externos.
- Relatórios: artifact de 30 dias e branch privada `seo-reports` do projeto chamador, nunca a branch de produção.
- **Status:** runner, workflow e testes adicionados ao branch de feature; a CI valida configuração e construção do comando, sem fazer crawls externos. O resultado real só será confirmado após execução manual/mensal num projeto chamador.
- SiteOne apresenta score próprio de qualidade 0–10; não comparar com os scores Lighthouse 0–100 nem com ranking Google.

## 4. Histórico de versões

- 2026-11-18 — primeira curadoria dos projetos de copywriting, estratégia, UX/UI, GA4, marketing brasileiro, dados públicos e comércio LATAM; submódulos fixados a commits específicos.
- 2026-11-20 — adoção de Trendspyg 1.9.0 para Google Trends e Lighthouse 13.6.0 para auditoria técnica; workflows de baixa frequência em GitHub Actions e guardrails de relatório privado.

## 5. Runtime remoto MCP Brasil — Render Free

O runtime recomendado para executar o pacote upstream completo é o [Render Free Docker](../runtimes/render-mcp-brasil/README.md). O [checklist de implantação](./RENDER-DEPLOY-CHECKLIST.md) descreve a única etapa ainda dependente do proprietário da conta.

**Estado:** CI aprovado em 18/11/2026 (execução #44231297710): build Docker, container com limite de 512 MiB, endpoint saudável, handshake MCP autenticado, descoberta BM25 e chamada read-only `listar_features`. O servidor carregou 42 features ativas e registrou 307 ferramentas internas; sete ferramentas meta/discovery ficam visíveis inicialmente. O teste não consultou APIs externas.

O serviço não foi implantado. Falta conectar o GitHub ao Render, criar o Blueprint da raiz e definir `MCP_BRASIL_API_TOKEN` como segredo privado no painel. O código força autenticação estática Bearer, BM25 e datasets locais desligados.

O experimento Cloudflare Python Worker permanece em `runtimes/cloudflare-mcp-brasil/`, mas não está apto ao deploy: o extra `fastmcp[code-mode]` puxa `pydantic-monty` e `pydantic-monty-client`, que não possuem wheels compatíveis com o build Pyodide usado pelos Python Workers. O workflow do Worker é manual e experimental; seu deploy automático foi removido para evitar publicar um servidor não validado.

**Disponibilidade no ChatGPT:** a documentação OpenAI atual não permite que uma conta Free adicione MCP personalizado. Business e Enterprise/Edu suportam conexões personalizadas; Pro tem permissões limitadas a read/fetch. O endpoint remoto poderá ser usado em outros clientes compatíveis com Streamable HTTP. Para tarefas deste chat, usar os conectores já disponibilizados (GitHub, Canva, Adobe, MagicPath/Figma etc.).

## 6. Roteiro de integração dos demais MCPs

- **Google Analytics MCP:** código original presente como submódulo, ainda não configurado; faltam projeto Google Cloud, OAuth/ADC e autorização sobre a propriedade GA4. Começar somente leitura.
- **MCP Dev LATAM:** catálogo presente como submódulo; não publicar o pacote inteiro como um servidor único. Selecionar somente conector estável, com provedor e rota documentados.
- **Asaas MCP:** presente como submódulo, não conectado; precisa de credencial própria, sandbox e política de confirmação para cobranças, assinaturas e estornos.
- **Hotmart MCP:** presente como submódulo, não conectado; precisa de credenciais OAuth e política de confirmação para cancelamento, estorno, cupons e alterações.
- **Skills de social/marketing/UX e Superpowers:** são fontes de instruções e não exigem servidor MCP permanente. Devem ser carregadas seletivamente no runtime que executa o trabalho.

## 7. Product Discovery, SaaS Validation e Security

### Upstreams adicionados em 27/11/2026

| Fonte | Commit fixado | Licença | Entrypoints / uso |
|---|---|---|---|
| [Claude SaaS Eval Skills](https://github.com/kirillpolevoy/claude-saas-eval-skills) | 6feca4f7ea3eefb687acce51da95d8ca50ef6472 | MIT | ideação de nicho, first-pass e scorecard; não pontuar sem evidência |
| [Solo Founder Skills](https://github.com/whawkinsiv/solo-founder-skills) | 01bd10f79a4b6a741be78e3184612a90ecbd54ef | MIT | validate, secure e pricing; demanda exige comportamento/pagamento |
| [Ultimate Product Discovery](https://github.com/ipavelm/ultimate-product-discovery-skill) | aa26c2e0d56ce2eb1939561345b230b86c5da7ba | MIT | JTBD, entrevistas, OST, Lean Canvas e 18 tarefas |
| [Claude Marketing Research](https://github.com/ishwarjha/claude-marketing-research-skill) | 0b31cbde9a51c4a0a1d2ceca68fd39db00f5c558 | Apache-2.0 | concorrentes, avatar, posicionamento e proposta de valor |
| [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) | e997ac5b9a74eab332d5e9793bb38a38c8cfdd74 | MIT | security-and-hardening, OWASP/STRIDE e hardening |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) | 02894ec5b8a0a70637df5a6b45763de92940cedd | Apache-2.0 | static scanner para Agent Skills; upstream Alpha, execução isolada |
| [Strix](https://github.com/usestrix/strix) | 9ed84f99c8f13fc921baebc59e0c696108cfab3e | Apache-2.0 | pentest dinâmico, apenas staging autorizado, Docker + LLM key |
| [MCP Server Audit](https://github.com/ModelContextProtocol-Security/mcpserver-audit) | f53c1e13691a1fb35555e883b455f7129b9a7cf2 | Apache-2.0 | checks e orientação de segurança MCP; cobertura limitada |

As fontes foram fixadas em commits. Skills e ferramentas não são instaladas nem executadas automaticamente. A autoria e as licenças permanecem nos respectivos upstreams.

### Itens deliberadamente não importados

- agentnode-dev/skills-security-audit: não foi localizada licença explícita; não redistribuir.
- anthropics/claude-code-security-review: origem oficial não verificada para esta inclusão; forks não são tratados como ferramenta oficial.
- MCP Market SaaS Market Research Skill: repositório exato não verificado; não inventar URL nem importar cópia.
- Best Agent Kits / Eyadkelleh Awesome Skills Security: origem exata não confirmada; manter fora até validação.
- Corey Haines Marketing Skills: já estava em upstream/marketing-skills-corey; não duplicar.

### Processo de atualização

1. Comparar commits.
2. Verificar LICENSE, notices, dependências, install scripts e ações de rede.
3. Executar SkillSpector isolado e rever achados.
4. Atualizar submodule/registry em PR.
5. Validar a skill com casos sintéticos e sem credenciais reais.
