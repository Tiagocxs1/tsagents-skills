# Arquitetura de runtimes MCP e agentes

**Atualizado em 20/11/2026.** Objetivo: permitir que ferramentas open-source sejam executadas em ambientes remotos, com o menor custo possível, sem confundir execução temporária com serviço persistente e sem expor credenciais.

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

O workflow `.github/workflows/render-mcp-brasil-ci.yml` foi aprovado em 18/11/2026 (execução #44231297710): build Docker, limite de 512 MiB, `/health`, handshake Bearer, descoberta BM25 e chamada read-only `listar_features`. O servidor registrou 42 features ativas e 307 ferramentas internas; sete ferramentas de descoberta são expostas inicialmente. O smoke test não executou consultas nas APIs externas. O serviço ainda não foi criado no Render; falta conectar o repositório e definir o segredo no painel.

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
- A documentação OpenAI atual informa que conexões a servidores MCP personalizados estão disponíveis para Business e Enterprise/Edu; Pro oferece permissões read/fetch. A conta Free não pode criar esta conexão personalizada.
- O endpoint Render continua útil para clientes MCP compatíveis com Streamable HTTP, mas publicar não o conecta automaticamente ao ChatGPT Free. Nesta conversa, os conectores Canva, Adobe, Figma/MagicPath, GitHub e outros já disponíveis continuam sendo o caminho operacional.

## Referências técnicas

- Cloudflare Python Workers: https://developers.cloudflare.com/workers/languages/python/
- Cloudflare MCP remote servers: https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/
- Cloudflare Worker size 64 MiB (free e paid): https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/
- Cloudflare Workers limits: https://developers.cloudflare.com/workers/platform/limits/
- Durable Objects pricing and quotas: https://developers.cloudflare.com/durable-objects/platform/pricing/
- GitHub Actions runners: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
- Render Free web services: https://render.com/docs/free
- Render Docker hosting: https://render.com/hosting/docker
- OpenAI custom MCP connection requirements and plan availability: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt


## Runtime: TS Image Library — Cloudflare R2 + Worker

O runtime `runtimes/cloudflare-image-library/` disponibiliza ingestão de imagens raster por API HTTP autenticada e MCP Streamable HTTP com Bearer token. Recursos exclusivos: bucket R2 `ts-image-assets-temp` e D1 `ts-image-assets-index`; não reutiliza os buckets e Workers preexistentes.

- Endpoint MCP: `https://ts-image-library.tiagocxs-tdb.workers.dev/mcp`
- API: `https://ts-image-library.tiagocxs-tdb.workers.dev`
- Ferramentas: `import_image`, `import_images_batch`, `search_assets`, `get_asset`, `recover_asset`, `delete_asset`.
- Retenção: regra nativa R2 remove objetos em `images/` após 604800 segundos. A exclusão física costuma ocorrer até 24 horas após o timestamp de expiração; não é um SLA de segundo exato.
- Catálogo: D1 preserva metadados de origem/licença e a URL de origem sanitizada para permitir tentativa de recuperação. URLs assinadas que dependam de query string podem não ser recuperáveis sem uma URL nova.
- Sem cópia automática em Cloudinary e sem Cron adicional: a conta já usava os cinco triggers disponíveis no plano Free.
- Segurança: Bearer token armazenado como secret do Worker, R2 privado, UUID imprevisível, URLs de origem validadas, redirecionamentos revalidados, tamanho/tipo verificados e formatos raster permitidos. O link de arquivo é público temporário enquanto ativo, pois foi concebido para inserir imagens em artes que serão públicas.
- Limitação de clientes: endpoint MCP pode ser usado por clientes que suportam Streamable HTTP com Bearer; ChatGPT Free não oferece conexão de MCP personalizado na configuração atual. Consulte `README.md` do runtime antes de configurar um cliente.

