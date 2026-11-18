# Biblioteca de privacidade, LGPD/GDPR e segurança de agentes

**Curadoria:** 18/11/2026. Reavaliar upstreams antes de atualizar commits ou instalar novos MCPs.

## O que foi incorporado

| Recurso | Tipo | Uso |
|---|---|---|
| privacy-by-design/SKILL.md | Skill TS Digitais | Guardrails de engenharia de privacidade para todos os projetos |
| privacy-legal/SKILL.md | Skill TS Digitais | Matriz procedimental LGPD/GDPR e fontes oficiais |
| messaging-private-storage/SKILL.md | Skill TS Digitais | Controles para mensageria, anexos, uploads e downloads |
| agents/privacy-engineer.md | Perfil de agente | Desenho e implementação de controles |
| agents/privacy-reviewer.md | Perfil de agente | Revisão independente e adversarial |
| agents/mcp-privacy-auditor.md | Perfil de agente | Auditoria de origem, licença, rede, ferramentas e permissões |
| templates/privacy/.cursorignore | Template | Excluir arquivos sensíveis do contexto normal do Cursor |
| templates/privacy/.gitignore | Template | Evitar versionamento de segredos e dumps locais |
| templates/github-actions/otto-privacy-review.yml | Workflow template | Varredura OTTO opcional em pull requests |

As skills TS Digitais são originais desta biblioteca; não são cópias integrais de skills de terceiros. Os links abaixo são referências de origem e ferramentas candidatas.

## Ferramentas indicadas

### OTTO — Privacy Guardian
- Repositório: https://github.com/metricasboss/otto
- Licença: MIT.
- Commit consultado e fixado no template: f0bb2bd4d69ce18f42f5d183cd0e1c4df10baa1e.
- Detecta padrões como PII em logs/código, segredos expostos, rastreamento sem consentimento e alguns problemas de minimização. Possui CLI, skills e GitHub Action para PRs.
- Hooks automáticos documentados são exclusivos do Claude Code. Cursor, Codex e outros ambientes precisam de chamada manual conforme o upstream.
- O template inicia com fail-under: 0: relatório primeiro, sem bloquear merges. Não habilite threshold obrigatório antes de medir falsos positivos e lacunas em cada stack.
- **Cadeia de suprimentos:** o action.yml inspecionado referencia internamente actions/setup-python@v6 e actions/github-script@v9 por tags mutáveis. Fixar o commit do OTTO não fixa essas dependências transitivas. GitHub recomenda pin por SHA completo e auditoria de código. Por isso o workflow é opcional e não foi ativado globalmente.
- O score é análise automatizada de padrões; não demonstra conformidade jurídica nem substitui análise de arquitetura, testes de autorização e revisão humana.

### LGPD Compliance Skill — legal-skills-open
- Repositório: https://github.com/ThomasMoreAI/legal-skills-open
- O repositório consultado declara Apache License 2.0. Metadata de algumas skills pode conter outra informação; não presumir licença independente sem verificar arquivos/autorizações aplicáveis.
- Inclui material LGPD/GDPR e fluxos de análise, RIPD/DPIA, bases legais e direitos. Esta biblioteca mantém skills próprias e links de referência; não redistribui o conteúdo integral do upstream.
- Verificar versão, licenças, autoria e fontes oficiais antes de copiar/adaptar qualquer arquivo.

### GDPR Engineering — github/awesome-copilot
- Skill de referência: https://github.com/github/awesome-copilot/tree/main/skills/gdpr-compliant
- A pasta e o SKILL.md existem no repositório consultado. A descrição cobre minimização, APIs, logging, retenção, criptografia, segredos e revisão.
- Mantemos skill própria multi-jurisdição, para não depender de instrução externa não versionada como regra de arquitetura.

### Claude for Legal — Anthropic
- Repositório: https://github.com/anthropics/claude-for-legal
- O repositório declara Apache-2.0 e reúne plugins, skills, agentes, hooks e conectores para Claude Cowork/Claude Code. O plugin privacy-legal oferece fluxos de DSAR, DPA, PIA e análise regulatória.
- **Não instalado como plugin global:** estrutura e comandos são próprios do ecossistema Claude; o bundle contém workflows jurídicos e conectores específicos. Não é plugin universal de Cursor/VS Code nem MCP regulatório genérico.
- Os autores deixam claro que resultados são rascunhos sujeitos à revisão de advogado.

### LGPD MCP Server — MCP Market
- Referência citada: https://mcpmarket.com/server/lgpd
- Não localizamos repositório canônico verificável com código, licença, release, mantenedor, documentação de transporte/autenticação e permissões.
- **Status: não instalado.** Uma ficha de diretório ou promessa de “nove ferramentas” não basta para conectar um servidor a mensagens, arquivos ou credenciais.

### Global Compliance Audit MCP Server — artigo Hugging Face
- Referência: https://huggingface.co/blog/MCP-1st-Birthday/global-compliance-audit-mcp-server
- Artigo comunitário de 28/11/2025 que anuncia servidor offline com 120 regras e 14 regulamentos.
- Não encontramos código-fonte canônico, release reproduzível, licença e documentação de instalação/manutenção suficientes para auditar as alegações.
- **Status: não instalado.** Os números do artigo são declarações do autor, não resultados reproduzidos nesta curadoria.

### Cursor Privacy & Data Security
- Não encontramos pacote/skill com origem verificável para o link de marketplace citado.
- Em substituição, foi criado templates/privacy/.cursorignore com base na documentação do Cursor: https://cursor.com/docs/reference/ignore-file
- **Limite essencial:** .cursorignore reduz o contexto acessível ao Agent/Tab e referências @, mas terminal e ferramentas MCP ainda podem ler arquivos ignorados. Não é barreira absoluta. Use também .gitignore, permissões do sistema operacional, secret store e nunca dê acesso de produção a um agente sem necessidade.

## Instalar as skills em todos os projetos locais

O repositório central guarda as definições. Para disponibilizá-las nos agentes de desenvolvimento do computador, a CLI skills suporta instalação global e seleção de agentes. Execute no terminal local:

~~~bash
npx skills add https://github.com/Tiagocxs1/tsagents-skills --skill privacy-by-design --skill privacy-legal --skill messaging-private-storage -g -a '*' -y
~~~

A opção -g instala em escopo global do usuário, disponível entre projetos; -a '*' direciona aos agentes suportados pela CLI. Para versionar as skills dentro de um projeto e compartilhá-las com a equipe, execute o mesmo comando sem -g.

Referência da CLI: https://github.com/vercel-labs/skills/blob/main/docs/commands.md

Para conferir instalação global:

~~~bash
npx skills list -g
~~~

Isto instala instruções no ambiente local. Não instala MCPs, não configura contas, não implanta serviços e não altera automaticamente outros repositórios GitHub.

## Ativar scan OTTO em um projeto

O arquivo templates/github-actions/otto-privacy-review.yml é um modelo. Copie-o para .github/workflows/otto-privacy-review.yml depois de revisar versão e permissões. Começa em report-only (fail-under: 0) e usa comentário de PR; não habilita SARIF nem exige GitHub Advanced Security.

Antes de transformar o resultado em check obrigatório:
1. Execute em PRs com dados sintéticos.
2. Leia cada finding e compare com o fluxo real.
3. Verifique falsos positivos e dados que a ferramenta não observa.
4. Revise dependências transitivas do action no momento da adoção.
5. Só então escolha limite de score e política de bloqueio.

## Política de integração
- Não conectar servidores MCP de diretório sem código, mantenedor, licença, protocolo, autenticação e permissões verificáveis.
- Preferir ferramentas read-only e escopos mínimos.
- Não compartilhar tokens, chaves de serviço, mensagens privadas ou arquivos de clientes com ferramentas externas.
- Não habilitar hooks automáticos sem inspecionar o instalador e entender os arquivos que altera.
- Não confundir skill, plugin, agente, workflow GitHub Actions e servidor MCP: são artefatos diferentes e exigem instalações distintas.
- Toda conclusão de conformidade deve indicar evidências, lacunas, testes e decisões jurídicas pendentes.

## Fontes normativas oficiais
- LGPD — Lei nº 13.709/2018: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- ANPD — regulamentações: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/
- ANPD — direitos dos titulares: https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares
- ANPD — comunicação de incidente: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis
- GDPR — EUR-Lex: https://eur-lex.europa.eu/eli/reg/2016/679/oj
