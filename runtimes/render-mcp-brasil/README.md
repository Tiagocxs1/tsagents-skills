# MCP Brasil — Render Free (Docker)

Este é o runtime recomendado para testar o MCP Brasil completo em um host Python/Linux, sem o limite de 10 ms de CPU do Workers Free. Usa o pacote publicado `mcp-brasil==0.14.0`, que corresponde à versão do submódulo fixado nesta biblioteca.

## Estado

- Blueprint e Dockerfile preparados no repositório.
- CI local do container ainda precisa passar.
- **Não implantado**: a criação do serviço exige que o usuário conecte o GitHub ao Render e informe um Bearer token no painel.
- Nenhuma credencial foi gravada no Git.

## Plano gratuito e limitações

O Render Free oferece 750 horas de instância por workspace/mês (suficiente para um web service simples por mês inteiro), 512 MB de RAM e sem cartão de crédito. Porém, o serviço dorme após 15 minutos sem tráfego e pode levar cerca de um minuto para acordar. O filesystem é efêmero, então não usamos banco ou cache local persistente. Não é indicado para produção nem para uso com exigência de disponibilidade contínua.

## Implantar pelo Blueprint

1. Abra o painel do Render e selecione **New → Blueprint**.
2. Conecte sua conta GitHub e escolha `Tiagocxs1/tsagents-skills`.
3. O Render detecta o `render.yaml` da raiz e mostra o serviço `tsagents-mcp-brasil`.
4. Quando solicitado, defina `MCP_BRASIL_API_TOKEN` com um valor aleatório forte de pelo menos 32 caracteres.
5. Crie o serviço com o plano **Free** e aguarde o primeiro build.

O endereço HTTPS será exibido no painel, normalmente como `https://tsagents-mcp-brasil.onrender.com`. O endpoint MCP é `/mcp/`. Não compartilhe o Bearer token em chats, issues, logs ou no GitHub.

## Verificação

- Health check: `https://SEU-SERVICO.onrender.com/health`
- MCP Streamable HTTP: `https://SEU-SERVICO.onrender.com/mcp/`

Configuração genérica de cliente MCP:

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

## Dados, segurança e limites

- Usa autenticação estática Bearer; sem token válido não há acesso às ferramentas.
- BM25 tool discovery fica ativo para não expor centenas de schemas de uma vez.
- Datasets locais DuckDB ficam desativados. Isso evita tentar manter arquivos grandes no filesystem efêmero.
- Nenhuma chave opcional de APIs governamentais está configurada.
- Leia `upstream/mcp-brasil/ACCEPTABLE_USE.md` e `SOURCES.md`. A licença MIT cobre o código, não os dados/API de terceiros.
- Não use dados pessoais/sensíveis para perfilamento, marketing ou reidentificação.
- O serviço gratuito pode reiniciar ou suspender; não o use para processos críticos.

## Por que este runtime?

O Render roda o pacote Python em Linux comum, então as dependências nativas declaradas pelo upstream não precisam ser substituídas por shims Pyodide. O Cloudflare Worker permanece experimental: no Workers Free, o limite de 10 ms por invocação e a ausência de wheels Pyodide para dependências opcionais do FastMCP tornam a coleção Python completa uma combinação pouco confiável.
