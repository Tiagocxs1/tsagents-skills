# Stack de SEO, GEO e Analytics

Curadoria inicial em 18/11/2026. Objetivo: fornecer ferramentas gratuitas/open-source para auditorias reproduzíveis, conectando dados reais de GSC e GA4 a skills de diagnóstico. Não confundir código versionado com MCP executando ou API autenticada.

## 1. Recomendação principal

| Camada | Projeto | Licença / situação | Decisão |
|---|---|---|---|
| GA4 MCP | [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) | Apache-2.0; oficial Google Analytics; já existe em `upstream/google-analytics-mcp` como submódulo | Prioridade 1. Usar read-only; o servidor oficial suporta relatórios e descoberta de propriedades. |
| GSC MCP | [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) | MIT; comunidade; Python 3.11+ e uvx/pipx | Prioridade 1. Instalar como MCP local; manter operações destrutivas desativadas. |
| SEO/GEO | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT; coleção multi-skill/subagent | Prioridade 1 para referência e instalação seletiva; não copiar a coleção inteira sem necessidade. |
| Auditoria técnica | [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) | MIT; CLI npm `@seomator/seo-audit` | Prioridade 1 para checks determinísticos; README atual anuncia 373 regras/20 categorias, sujeito a mudanças. |
| Auditoria de página | [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) | MIT; skill + scripts Python | Complementar para auditoria de URL e relatório HTML; começar pelo tier básico. |

## 2. MCPs Google

### Google Analytics — servidor oficial
- Repositório: https://github.com/googleanalytics/google-analytics-mcp
- Documentação oficial: https://developers.google.com/analytics/devguides/MCP
- Licença: Apache-2.0.
- Publicado no PyPI como `analytics-mcp`; Python 3.10+ e `pipx` ou `uvx`.
- Usa Application Default Credentials (ADC) e escopo `analytics.readonly` no modo somente leitura.
- Requer ativar as APIs Admin e Data do GA4 no projeto Google Cloud e conceder pelo menos Viewer na propriedade.
- As versões atuais podem expor opções de escrita quando habilitadas; não usar `--allow-write` para auditoria.

Exemplo de registro local (substituir os caminhos e project ID no computador do operador; nunca commitar valores reais):

```json
{
  "mcpServers": {
    "analytics-mcp": {
      "command": "uvx",
      "args": ["analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/CAMINHO/LOCAL/adc.json",
        "GOOGLE_CLOUD_PROJECT": "SEU_PROJECT_ID"
      }
    }
  }
}
```

Guia oficial: https://developers.google.com/analytics/devguides/MCP

### Google Search Console — MCP comunitário
- Repositório: https://github.com/AminForou/mcp-gsc
- Licença: MIT.
- Python 3.11+; instalação recomendada pelo upstream com `uvx`.
- Ferramentas para propriedades, Search Analytics, comparação de períodos, inspeção de URLs, indexação e sitemaps.
- OAuth read-only ou service account; a permissão de escrita/destruição fica desativada por padrão.
- Não é um servidor oficial do Google. Inspecionar releases e permissões antes de atualizar.

Exemplo de configuração (ajustar caminhos localmente):

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/AminForou/mcp-gsc.git", "mcp-gsc"],
      "env": {
        "GSC_OAUTH_CLIENT_SECRETS_FILE": "/CAMINHO/LOCAL/client_secrets.json"
      }
    }
  }
}
```

Para forçar somente leitura, manter `GSC_ALLOW_DESTRUCTIVE=false` (padrão). Nunca usar o exemplo com arquivos de credenciais dentro do repositório. A configuração OAuth pode variar por versão; conferir README upstream antes de executar.

## 3. Skills e auditorias

### Claude SEO — pacote de skills e subagents
https://github.com/AgriciDaniel/claude-seo

- Licença MIT.
- O repositório atualmente anuncia 26 sub-skills e 19 subagents para SEO técnico, conteúdo, schema, E-E-A-T, GEO/AEO, SEO local, e-commerce, internacional e análise.
- É um pacote grande e orientado a Claude Code, com compatibilidade variável entre runtimes. Usar como fonte upstream; instalar somente os módulos necessários.
- Não tratar número de estrelas, quantidade de subagents ou declarações do README como prova de qualidade/resultado.
- O pacote contém extensões opcionais para fontes de dados externas; não habilitar DataForSEO, Firecrawl ou serviços pagos sem necessidade e aprovação de custo.

### SEOmator Audit
https://github.com/seo-skills/seo-audit-skill

Instalação CLI descrita pelo upstream:

```bash
npm install -g @seomator/seo-audit
seomator audit https://SEU-DOMINIO
```

Para um relatório JSON ou HTML:

```bash
seomator audit https://SEU-DOMINIO --format json -o seo-audit.json
seomator audit https://SEU-DOMINIO --format html -o seo-audit.html
```

- Código MIT, mas instalar via npm exige Node/npm e baixa dependências. Revisar dependências e permissões antes da instalação.
- O modo `--cwv` usa navegador local e é mais lento. O total de regras anunciado varia conforme a revisão do projeto; o README lido nesta curadoria informa 373.
- Os scores são checks técnicos próprios, não um score oficial do Google. Conferir falsos positivos, páginas renderizadas e critérios de negócio.

### JeffLi — Single-page SEO Audit
https://github.com/JeffLi1993/seo-audit-skill

- Licença MIT.
- Instalação Skill CLI: `npx skills add JeffLi1993/seo-audit-skill`.
- Scripts Python cobrem status HTTP, robots/sitemap, title/H1/meta/canonical, schema e fetch de página.
- `seo-audit-full` inclui PageSpeed e outras verificações, mas exige API key do PageSpeed Insights para as medições correspondentes. A skill básica é a opção inicial sem chave.
- Revisar relatórios HTML gerados e não aceitar recomendações sem confirmar intenção de busca e evidência.

## 4. Alternativas não prioritárias

- [Gatescrispy/mcp-ga4-ultimate](https://github.com/Gatescrispy/mcp-ga4-ultimate): alternativa comunitária com amplo conjunto de ferramentas e licença MIT declarada, mas a atividade/release observada é muito menos recente que a do MCP oficial. Não instalar como padrão. A comparação do README do upstream menciona permissões de escrita; exigir auditoria de código e allowlist antes de qualquer conexão.
- [OpenSEO MCP](https://openseo.so/features/mcp): referência de mercado; não substituir as fontes oficiais do Google por métricas estimadas de terceiros.

## 5. Fluxo de trabalho recomendado

1. Consultar `seo-analytics-ops/SKILL.md`.
2. Conectar GA4 e GSC no runtime local, usando OAuth/ADC ou service account com menor privilégio.
3. Consultar primeiro dados agregados e read-only; validar propriedade e período.
4. Rodar auditoria determinística em URLs representativas e, quando necessário, crawl limitado.
5. Cruzar evidências GSC + GA4 + auditoria técnica; explicar diferenças de definição e atraso dos dados.
6. Criar backlog priorizado, com evidência, confiança, impacto, esforço e rollback.
7. Após implementação, repetir auditoria e comparar janelas equivalentes.

## 6. Custos, privacidade e segurança

- Projetos e código são open-source, mas APIs, infraestrutura, quotas, PageSpeed e provedores de IA podem ter limites/custos próprios.
- Começar com ferramentas locais gratuitas e contas de leitura; não contratar extensões pagas.
- Nunca versionar JSON de service account, OAuth client secret, ADC, refresh token, relatórios com dados identificáveis ou exports privados.
- Não habilitar permissões de escrita do GA4 nem `GSC_ALLOW_DESTRUCTIVE=true` em auditoria normal.
- Operações que alteram propriedades, enviam/excluem sitemaps, publicam ou redirecionam páginas exigem autorização explícita.
- Consultar `privacy-by-design/SKILL.md`, `agents/mcp-privacy-auditor.md` e `docs/PRIVACY-TOOLING.md` antes de conectar contas.
- Não alegar que um MCP está conectado porque existe configuração de exemplo ou submódulo.

## Fontes consultadas

- https://developers.google.com/analytics/devguides/MCP
- https://github.com/googleanalytics/google-analytics-mcp
- https://github.com/AminForou/mcp-gsc
- https://github.com/AgriciDaniel/claude-seo
- https://github.com/seo-skills/seo-audit-skill
- https://github.com/JeffLi1993/seo-audit-skill
- https://github.com/Gatescrispy/mcp-ga4-ultimate
