# Runtimes

Esta pasta reúne configurações para executar os projetos upstream como serviços ou tarefas automatizadas. Ela não substitui os originais em `upstream/`.

## Princípios

- Um submódulo guarda a fonte original; um runtime contém somente o adaptador/deploy necessário.
- Um serviço remoto precisa de transporte HTTP, autenticação e um endereço acessível.
- Um workflow do GitHub Actions é efêmero: instala, executa e termina. Não é servidor permanente.
- Nunca colocar tokens em arquivos versionados. Usar Cloudflare Secrets, GitHub Actions Secrets ou variáveis locais ignoradas pelo Git.
- Não considerar um MCP operacional até passar por build, teste de saúde, handshake MCP e validação das permissões.

## Runtime inicial

- [Cloudflare MCP Brasil](./cloudflare-mcp-brasil/README.md) — adaptador Python Worker + Durable Object para servir o MCP Brasil via Streamable HTTP com autenticação Bearer.

Ver também [Arquitetura de runtimes MCP](../docs/MCP-RUNTIME-ARCHITECTURE.md).


## Runtime recomendado para MCP Brasil

- [Render Free Docker](./render-mcp-brasil/README.md) — caminho de teste do MCP Python completo em Linux comum; cold start após 15 minutos ocioso.
- [Cloudflare Python Worker](./cloudflare-mcp-brasil/README.md) — experimento stateless; ainda bloqueado por dependências nativas do upstream no bundle Pyodide.
