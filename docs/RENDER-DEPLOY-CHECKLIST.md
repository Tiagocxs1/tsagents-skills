# Checklist de implantação — MCP Brasil no Render Free

**Estado do código:** aprovado pelo GitHub Actions em 18/11/2026.  
**Estado do serviço:** ainda não implantado.  
**Motivo:** o proprietário precisa conectar o repositório à conta Render e definir o segredo privado no painel. Nenhum segredo foi solicitado ou gravado no Git.

## O que já foi validado

Execução: https://github.com/Tiagocxs1/tsagents-skills/actions/runs/44231297710

- Imagem Docker construída.
- Container iniciado com limite de 512 MiB, equivalente ao teto de RAM do serviço Free.
- Endpoint `/health` respondeu.
- Handshake MCP Streamable HTTP com Bearer token passou.
- Descoberta BM25 retornou sete ferramentas de entrada.
- A chamada read-only `listar_features` passou.
- O upstream registrou 42 features ativas e 307 ferramentas internas. O teste não fez chamadas de consulta aos serviços externos governamentais.

## Passos no Render

1. Entrar em https://dashboard.render.com/ e conectar a conta GitHub, caso ainda não esteja conectada.
2. Escolher **New → Blueprint**.
3. Selecionar o repositório `Tiagocxs1/tsagents-skills`.
4. O Render deve localizar o `render.yaml` na raiz e apresentar `tsagents-mcp-brasil`.
5. Definir `MCP_BRASIL_API_TOKEN` como variável secreta no painel. Gere localmente um valor aleatório com 32 bytes ou mais; por exemplo, `openssl rand -hex 32`. **Não envie o token pelo chat e não o grave no Git.**
6. Confirmar o plano Free e criar o Blueprint.
7. Aguardar o build/deploy e verificar o serviço como Healthy.
8. Registrar a URL pública gerada. O endpoint MCP é `https://SEU-SERVICO.onrender.com/mcp/`; health check em `/health`.

## Limites conhecidos do Free

- 750 horas de instância por workspace/mês.
- 512 MB RAM.
- Dorme após 15 minutos sem requisições e pode levar cerca de um minuto para acordar.
- Filesystem efêmero; não guardar banco, cache ou dados persistentes no disco do serviço.
- O Render pode reiniciar o serviço a qualquer momento.
- Não oferece SSH para web services Free.
- Adequado para testes e consultas ocasionais, não para produção ou disponibilidade garantida.

## Como conectar a um cliente MCP compatível

Usar URL `/mcp/` e autenticação HTTP Bearer. Não colocar o token em arquivo versionado nem em screenshot.

## Limite importante no ChatGPT

A documentação atual da OpenAI informa que a conexão de servidores MCP personalizados está disponível para ChatGPT Business e Enterprise/Edu; Pro pode conectar custom MCP com permissões read/fetch, e a experiência completa de escrita é restrita aos planos/workspaces indicados. A conta Free não oferece a configuração de servidor MCP personalizado. Portanto, publicar no Render não faz este chat Free ganhar acesso automático ao MCP.

O endpoint continua utilizável por clientes compatíveis com MCP remoto, como clientes de desenvolvimento que aceitem Streamable HTTP. Para o calendário e as artes da Guardian, não precisamos esperar por esse deploy: os conectores Canva, Adobe, Figma/MagicPath e GitHub já estão disponíveis no ambiente.

## Segurança

- O processo falha ao iniciar sem `MCP_BRASIL_API_TOKEN` com 32+ caracteres.
- Autenticação estática Bearer é forçada antes de importar o servidor upstream.
- BM25 reduz a exposição inicial de schemas.
- Datasets locais estão desligados.
- Não configurar chaves adicionais de fontes sem necessidade e autorização.
- Respeitar `upstream/mcp-brasil/ACCEPTABLE_USE.md`, `SOURCES.md`, LGPD e termos próprios das APIs.
