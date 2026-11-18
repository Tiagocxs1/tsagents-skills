# MCP Brasil — Render Free (Docker)

Este runtime executa o pacote original `mcp-brasil==0.14.0` em Python/Linux, sem modificar o submódulo upstream.

## Estado

**CI aprovado · serviço ainda não publicado**

- [Execução de CI #44231297710](https://github.com/Tiagocxs1/tsagents-skills/actions/runs/44231297710) aprovada em 18/11/2026.
- Build Docker concluído e container iniciado com limite de 512 MiB.
- `/health` respondeu.
- Handshake Streamable HTTP com autenticação Bearer passou.
- Descoberta BM25 retornou sete ferramentas: `call_tool`, `executar_lote`, `listar_datasets_disponiveis`, `listar_features`, `planejar_consulta`, `recomendar_tools` e `search_tools`.
- Chamada read-only `listar_features` passou. O servidor registrou 42 features ativas e 307 ferramentas internas; o smoke test não consultou APIs externas.
- Nenhuma credencial de produção foi gravada no Git.

## Limites do plano gratuito

O Render Free oferece 750 horas de instância por workspace/mês e 512 MB de RAM. O serviço dorme após 15 minutos sem tráfego e pode levar aproximadamente um minuto para acordar. O filesystem é efêmero e o Render pode reiniciar a instância. É adequado para teste e consultas ocasionais, não produção ou disponibilidade contínua.

## Implantação

O único passo ainda pendente depende da sua conta Render:

1. Acesse https://dashboard.render.com/.
2. Conecte a conta GitHub, se ainda não estiver conectada.
3. Selecione **New → Blueprint** e escolha `Tiagocxs1/tsagents-skills`.
4. Confira o serviço `tsagents-mcp-brasil`, definido pelo `render.yaml` na raiz.
5. Defina `MCP_BRASIL_API_TOKEN` como segredo no painel. Gere localmente um valor aleatório com 32 bytes ou mais; exemplo: `openssl rand -hex 32`. Não envie esse valor pelo chat nem o grave no Git.
6. Selecione o plano Free e crie o serviço.
7. Quando estiver Healthy, registre a URL fornecida pelo Render.

O script `start.py` falha ao iniciar sem um token de pelo menos 32 caracteres. Ele força autenticação estática Bearer, BM25 e datasets locais desativados.

## Endpoints

- Health check: `https://SEU-SERVICO.onrender.com/health`
- MCP Streamable HTTP: `https://SEU-SERVICO.onrender.com/mcp/`

Configuração genérica do cliente MCP:

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

Não versione o arquivo de configuração com o token preenchido.

## Observações importantes

- BM25 expõe inicialmente ferramentas de descoberta; use `search_tools` e `call_tool` para localizar módulos e schemas do catálogo completo.
- 42 features foram carregadas no teste. Algumas outras ficam desativadas ou exigem chaves próprias; nenhuma chave adicional foi configurada.
- Datasets locais DuckDB estão desligados; não habilite downloads grandes em filesystem efêmero.
- O teste de CI confirmou inicialização e chamada de metadados, não o funcionamento de cada API externa.
- Leia `upstream/mcp-brasil/ACCEPTABLE_USE.md` e `SOURCES.md`. A licença MIT cobre o código, não os dados/APIs de terceiros.
- Não use dados pessoais/sensíveis para perfilamento, marketing ou reidentificação.

## Limite no ChatGPT

A documentação OpenAI atual informa que servidores MCP personalizados podem ser conectados em ChatGPT Business e Enterprise/Edu; Pro pode conectar com permissões read/fetch. A conta Free não pode criar conexões MCP personalizadas. Publicar no Render não conecta o endpoint automaticamente a este chat. Para o calendário e as peças da Guardian, os conectores já disponíveis (Canva, Adobe, Figma/MagicPath e GitHub) podem ser usados sem esperar esse deploy.
