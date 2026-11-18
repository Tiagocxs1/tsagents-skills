# MCP Brasil — Render Free (Docker)

Este é o runtime recomendado para testar o MCP Brasil completo em um host Python/Linux. Usa o pacote publicado `mcp-brasil==0.14.0`, correspondente à versão do submódulo fixado nesta biblioteca, sem modificar os arquivos originais.

## Estado

<badge_placeholder/>

- **CI aprovado em 18/11/2026:** imagem construída, container iniciado sob limite de memória de 512 MiB, health check respondeu, handshake MCP autenticado passou e uma chamada read-only a `listar_features` foi concluída.
- O teste registrou 307 ferramentas internas em 42 features ativas; o BM25 expõe inicialmente sete ferramentas de descoberta para reduzir contexto.
- **Ainda não implantado**: a criação do serviço exige que você conecte o GitHub ao Render e informe um Bearer token no painel.
- Nenhuma credencial de produção foi gravada no Git.

## Plano gratuito e limitações

O Render Free oferece 750 horas de instância por workspace/mês e 512 MB de RAM. O serviço dorme após 15 minutos sem tráfego e pode levar cerca de um minuto para acordar. O filesystem é efêmero e o processo pode reiniciar. É adequado para testes e consultas ocasionais, não para produção ou disponibilidade contínua.

## Implantar pelo Blueprint

1. Abra o painel do Render e selecione **New → Blueprint**.
2. Conecte sua conta GitHub e escolha `Tiagocxs1/tsagents-skills`.
3. O Render detecta o `render.yaml` da raiz e mostra o serviço `tsagents-mcp-brasil`.
4. Quando solicitado, defina `MCP_BRASIL_API_TOKEN` com um valor aleatório forte de pelo menos 32 caracteres. O processo recusa iniciar sem esse segredo.
5. Crie o serviço com o plano **Free**.

O endereço HTTPS será exibido no painel. O endpoint MCP é `/mcp/`. Não compartilhe o Bearer token em chats, issues, logs ou no GitHub.

## Verificação

- Health check: `https://SEU-SERVICO.onrender.com/health`
- MCP Streamable HTTP: `https://SEU-SERVICO.onrender.com/mcp/`

Configuração para um cliente MCP compatível:

```json
{
  "mcpServers": {
    "mcp-brasil": {
      "url": "https://SEU-SERVICO.onrender.com/mcp/",
      "headers": {
        "Authorization": "Bearer SEU_TOKEN"
      }
    }
  }
}
```

Não versione esse JSON com o token preenchido.

## Ferramentas e segurança

- Autenticação estática Bearer é obrigatória; o processo não inicia sem token válido.
- BM25 tool discovery fica ativo para não expor centenas de schemas de uma vez. Use as ferramentas de busca/execução do próprio MCP para descobrir o módulo certo antes de chamar uma ferramenta específica.
- Datasets locais DuckDB ficam desativados; não habilite downloads grandes em filesystem efêmero.
- Nenhuma chave opcional de APIs governamentais está configurada. No primeiro boot, o MCP Brasil registra 42 features ativas e omite algumas integrações que exigem chaves externas.
- Leia `upstream/mcp-brasil/ACCEPTABLE_USE.md` e `SOURCES.md`. A licença MIT cobre o código, não os dados/API de terceiros.
- Não use dados pessoais/sensíveis para perfilamento, marketing ou reidentificação.
- O serviço gratuito pode suspender ou reiniciar; não use para processos críticos.

## Por que este runtime?

O Render roda o pacote Python em Linux comum, então dependências nativas do FastMCP funcionam sem shims Pyodide. O Cloudflare Worker permanece experimental: dependências nativas do extra `fastmcp[code-mode]` não têm wheels compatíveis com o build Python Workers, e o limite de CPU do Workers Free é restritivo para carregar esse catálogo.
