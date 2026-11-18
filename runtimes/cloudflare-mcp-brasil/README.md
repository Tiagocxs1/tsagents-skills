# MCP Brasil — Cloudflare Python Worker

Este runtime prepara o MCP Brasil como servidor remoto via **Streamable HTTP** em Cloudflare Workers. Ele usa o projeto original fixado em `upstream/mcp-brasil`; não copia nem altera o código upstream.

## Estado atual

- **Status: estrutura criada; CI e deploy ainda pendentes de validação.**
- Adaptador Python Worker, projeto uv, configuração Wrangler, smoke test e workflows adicionados.
- **Ainda não implantado** no Cloudflare.
- Compatibilidade real com Pyodide/Workers depende do resultado do workflow de CI.
- Nenhum token ou credencial foi gravado no Git.

## Arquitetura

- Cloudflare Python Worker recebe o tráfego HTTP.
- Durable Object com SQLite mantém uma instância FastMCP/session manager estável.
- FastMCP `http_app()` publica Streamable HTTP no caminho MCP padrão.
- Autenticação Bearer obrigatória via Worker Secret `MCP_BRASIL_API_TOKEN`.
- BM25 tool discovery evita expor centenas de schemas de uma vez.
- Datasets locais permanecem desligados; primeiro deploy atende consultas às APIs remotas.

## Requisitos

- Clone com submódulos: `git clone --recurse-submodules https://github.com/Tiagocxs1/tsagents-skills.git`.
- Conta Cloudflare com Workers Free e `workers.dev` habilitado.
- Node.js 22+ e [uv](https://docs.astral.sh/uv/).
- Para deploy por Actions: token Cloudflare com permissão de edição de Workers Scripts e leitura da conta.

Workers Free inclui 100.000 requests/dia e 10 ms de CPU por invocação. Durable Objects SQLite têm cotas gratuitas diárias. Ao ultrapassar cotas, operações podem falhar até o reset diário. Consultas grandes ou cargas intensas não são garantidas no free tier.

## Testar localmente

Na raiz do repositório:

```bash
cp runtimes/cloudflare-mcp-brasil/.dev.vars.example runtimes/cloudflare-mcp-brasil/.dev.vars
# Edite .dev.vars com token aleatório (32+ caracteres).
cd runtimes/cloudflare-mcp-brasil
uv sync --all-groups
uv run pywrangler dev
```

Em outro terminal:

```bash
curl -fsS http://127.0.0.1:8787/health
MCP_URL=http://127.0.0.1:8787/mcp/ \
MCP_BRASIL_API_TOKEN='o-mesmo-token-local' \
uv run python scripts/smoke_test.py
```

O smoke test faz handshake MCP e lista ferramentas; não dispara consultas nas fontes governamentais.

## Deploy manual

Na pasta `runtimes/cloudflare-mcp-brasil`:

```bash
uv run pywrangler secret put MCP_BRASIL_API_TOKEN
uv run pywrangler deploy
```

Informe um token aleatório de pelo menos 32 caracteres. O token fica armazenado como Worker Secret, não em `wrangler.jsonc`.

## Deploy por GitHub Actions

O workflow `.github/workflows/deploy-mcp-brasil.yml` exige disparo manual e confirmação. Configure no repositório:

- **Actions Secret:** `CLOUDFLARE_API_TOKEN`
- **Actions Secret:** `MCP_BRASIL_API_TOKEN`
- **Actions Variable:** `CLOUDFLARE_ACCOUNT_ID`

Depois vá a **Actions → Deploy MCP Brasil → Run workflow**, na branch `main`, e marque a confirmação.

O workflow atualiza o Worker Secret e publica o Worker. A URL `workers.dev` aparece no log do deploy; use o sufixo `/mcp/`.

## Operação e segurança

- Endpoint MCP protegido por Bearer token. Nunca coloque o token em issues, logs, prompts ou arquivos versionados.
- `/health` serve apenas como indicador de disponibilidade.
- `MCP_BRASIL_DATASETS` permanece vazio. Não habilite datasets TSE/INEP/SIAPA/ANP sem revisar cache, limites, privacidade e licenças.
- Algumas fontes têm chaves opcionais; nenhuma foi configurada nesta primeira etapa.
- Leia `upstream/mcp-brasil/ACCEPTABLE_USE.md` e `SOURCES.md`.
- Não use dados pessoais/sensíveis para perfilamento, marketing, reidentificação ou segmentação.
- 401/403 geralmente indica token incorreto; 503 indica secret ausente ou configuração incompleta.

## Clientes MCP

O endpoint remoto segue Streamable HTTP e pode ser configurado em clientes compatíveis como Claude Code, Cursor, OpenCode, Gemini CLI ou outros.

Exemplo genérico:

```json
{
  "mcpServers": {
    "mcp-brasil": {
      "url": "https://SEU-WORKER.workers.dev/mcp/",
      "headers": {
        "Authorization": "Bearer SEU_TOKEN"
      }
    }
  }
}
```

O ChatGPT exige suporte do plano/workspace para adicionar MCP personalizado; publicar o endpoint não habilita essa função automaticamente em qualquer conta.
