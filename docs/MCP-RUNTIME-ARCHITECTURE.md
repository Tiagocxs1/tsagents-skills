# Arquitetura de runtimes MCP e agentes

**Atualizado em 18/11/2026.** Objetivo: permitir que ferramentas open-source sejam executadas em ambientes remotos, com o menor custo possível, sem confundir execução temporária com serviço persistente e sem expor credenciais.

## Resposta direta: GitHub Actions ou Cloudflare Workers?

São ambientes complementares:

| Ambiente | Natureza | Bom para | Não serve para |
|---|---|---|---|
| GitHub Actions — runner hospedado | Máquina virtual nova por job, descartada no fim | Instalar submódulos, rodar testes, executar MCPs por stdio durante uma automação, validar build e deploy | Hospedar um MCP permanentemente ou funcionar como desktop sempre ligado |
| Cloudflare Workers — HTTP remoto | Serviço distribuído e persistente, executado sob demanda | Hospedar MCP compatível com Streamable HTTP, receber chamadas de clientes remotos, guardar segredos em bindings | Executar qualquer binário de desktop ou assumir que todo MCP stdio é compatível |
| Cloudflare Durable Objects | Estado por instância, com SQLite | Manter sessão e estado de um servidor MCP que precise ser consistente entre requisições | Servidor geral com processo de sistema operacional e shell permanente |
| Runtime local (Codex CLI, Claude Code, OpenCode etc.) | Processo local e transitório | MCPs stdio, ferramentas de terminal e edição de arquivos locais | Ser acessível remotamente sem túnel ou host adicional |

GitHub-hosted runners são máquinas novas por job; para repositórios públicos os runners padrão Linux são gratuitos. Workers Free oferece 100.000 chamadas por dia, 10 ms de CPU por invocação e bundle de 64 MiB; Durable Objects SQLite também têm quotas gratuitas diárias. Os limites podem ser alterados pelo provedor, portanto verificar antes de ampliar o uso.

## Arquitetura adotada

1. **Originais** continuam em `upstream/` como Git submodules fixados em commits.
2. **Runtimes** ficam em `runtimes/`, em projetos isolados por MCP, sem editar os arquivos upstream.
3. **CI** roda smoke tests e valida compatibilidade.
4. **Deploy** é iniciado pelo usuário no painel do provedor, com secrets definidos diretamente no Secret Store.
5. **Cliente MCP** conecta-se ao endpoint remoto Streamable HTTP; se o cliente só aceitar stdio, usar o runtime local ou um bridge específico.
6. **ChatGPT** precisa suportar a modalidade de conexão MCP personalizada na conta/plano/workspace. Um endpoint remoto, por si só, não habilita a função no ChatGPT.

## Primeiro runtime: MCP Brasil

O projeto [MCP Brasil](https://github.com/Mcp-Brasil/mcp-brasil) foi selecionado porque concentra fontes públicas brasileiras em um servidor FastMCP Python e oferece suporte HTTP.

O runtime experimental em `runtimes/cloudflare-mcp-brasil/` usa Cloudflare Python Workers e Streamable HTTP stateless, mas o CI confirmou que o bundle Pyodide não consegue resolver `pydantic-monty` e `pydantic-monty-client`, puxados pelo extra `fastmcp[code-mode]` do upstream. O limite de CPU de 10 ms por invocação no Workers Free também é restritivo para inicializar o catálogo de 70 fontes. **Esse runtime não está pronto para deploy** e não vamos modificar ou mutilar o submódulo original para forçar a instalação.

### Render Free — caminho de teste recomendado para o MCP Brasil completo

O runtime `runtimes/render-mcp-brasil/` usa Docker e instala o pacote publicado `mcp-brasil==0.14.0` em Python/Linux comum. Isso mantém o código upstream completo e permite usar as wheels nativas requeridas pelo FastMCP/Code Mode. O arquivo `render.yaml` da raiz permite criar o Web Service pelo Blueprint do Render.

Limitações verificadas do plano Free: 750 horas de instância por workspace/mês, 512 MB RAM, suspensão após 15 minutos sem tráfego e cerca de um minuto para acordar. O filesystem é efêmero e o serviço pode reiniciar. É adequado para testes e consultas ocasionais, não produção ou disponibilidade garantida. O primeiro deploy ainda exige que o usuário conecte o GitHub ao Render e defina `MCP_BRASIL_API_TOKEN` como segredo no painel. O script `start.py` valida o token antes de importar o upstream, força autenticação estática Bearer e mantém BM25/datasets locais limitados.

O workflow `.github/workflows/render-mcp-brasil-ci.yml` faz build da imagem Docker, verifica `/health` e executa handshake MCP autenticado + descoberta de ferramentas. Só depois de CI verde faz sentido criar o Blueprint no Render.

### Segurança

- O token MCP fica apenas no Secret Store do Render (ou, em runtimes futuros, no secret store do host); nunca no código, em `.dev.vars.example`, no `wrangler.jsonc` ou no Dockerfile.
- Não criar endpoint público sem autenticação.
- Não habilitar datasets locais grandes no primeiro deploy.
- Não configurar chaves opcionais das fontes sem necessidade real.
- Nunca usar dados pessoais/sensíveis para perfilamento, marketing, reidentificação ou segmentação.
- O MCP Brasil é comunitário, não é serviço oficial do governo. A licença MIT cobre o código, não os dados/API de terceiros. Leia `ACCEPTABLE_USE.md` e `SOURCES.md` no upstream.

## Outros MCPs do arsenal: próxima fila

| Projeto | Caminho provável | Estado / observação |
|---|---|---|
| Google Analytics MCP | Python remoto ou runtime gerenciado com OAuth/ADC | Não implantar sem definir conta Google, propriedade GA4 e autenticação por usuário. Começar read-only; write tools são opt-in. |
| MCP Dev LATAM | Node/TypeScript em Cloudflare Worker ou cliente HTTP remoto | Selecionar primeiro um pacote estável; o catálogo marca vários packages alpha. |
| Asaas MCP | Runtime remoto isolado ou bridge; API token do Asaas | Não conectar antes de definir sandbox, escopos e política de confirmação para cobranças/estornos. |
| Hotmart MCP | Runtime remoto isolado ou bridge; OAuth/credenciais da Hotmart | Leitura primeiro; cupons, cancelamentos, estornos e assinaturas exigem confirmação. |
| Marketing/UX Skills | Git submodule + skills CLI no agente/editor | São arquivos de instrução, não MCPs nem serviços persistentes. Não precisam de Worker. |
| Superpowers | Plugin/skills no runtime de desenvolvimento | Metodologia de engenharia, não MCP. Não é executado como API remota. |

## Como o ChatGPT poderá usar

- Em clientes compatíveis com MCP remoto, configurar a URL HTTPS do servidor e o header Bearer.
- No ChatGPT, a conexão com um MCP personalizado depende das permissões e dos planos suportados pela OpenAI; atualmente o suporte completo de escrita está restrito aos planos Business e Enterprise/Edu, e o suporte nos outros planos é mais limitado.
- Enquanto a conta não oferecer conexão customizada, o runtime continua útil para Codex CLI, Claude Code, Cursor, OpenCode, Gemini CLI e para testes/automação de CI. Nesta conversa, os conectores já disponíveis continuam sendo a forma de acesso a ferramentas externas.

## Referências técnicas

- Cloudflare Python Workers: https://developers.cloudflare.com/workers/languages/python/
- Cloudflare MCP remote servers: https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/
- Cloudflare Worker size 64 MiB (free e paid): https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/
- Cloudflare Workers limits: https://developers.cloudflare.com/workers/platform/limits/
- Durable Objects pricing and quotas: https://developers.cloudflare.com/durable-objects/platform/pricing/
- GitHub Actions runners: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
- OpenAI custom MCP connection requirements: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt
