# Runtimes

Esta pasta reúne adaptadores e configurações para executar projetos upstream como serviços remotos ou tarefas automatizadas. Os repositórios originais ficam preservados em `upstream/`.

## Princípios

- GitHub Actions é uma máquina temporária para build/teste; não é servidor permanente nem desktop remoto.
- Um serviço remoto MCP precisa de transporte HTTP, autenticação, URL pública e cliente compatível.
- Submódulo não significa pacote instalado, MCP executando ou conta autenticada.
- Secrets ficam somente no Secret Store do provedor; nunca em arquivos versionados.
- Não declarar integração como pronta sem build, health check, handshake MCP e uma chamada read-only.

## Runtime MCP Brasil recomendado para teste

- [Render Free Docker](./render-mcp-brasil/README.md) — Linux/Python comum, CI aprovado em 18/11/2026.
- [Checklist de implantação](../docs/RENDER-DEPLOY-CHECKLIST.md) — conectar GitHub/Render e definir o Bearer secret na conta do proprietário.

## Experimento não recomendado para deploy

- [Cloudflare Python Worker](./cloudflare-mcp-brasil/README.md) — dependências do upstream sem wheels compatíveis com Pyodide e limite de CPU do Free; não publicado. O workflow ficou manual-only.

Ver também [Arquitetura de runtimes MCP](../docs/MCP-RUNTIME-ARCHITECTURE.md).
