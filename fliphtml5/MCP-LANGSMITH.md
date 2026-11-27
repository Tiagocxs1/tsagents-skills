# FlipHTML5 MCP — LangSmith Fleet

**Pesquisa:** 27/11/2026  
**Estado da integração:** estudado; autenticação não concluída; não instalado ainda.  
**Agente-alvo observado na sessão Fleet:** `langchain-ai-design-agent`. Configurar somente nesse agente, não como integração global para todos.

## 1. Objetivo

Conectar o servidor MCP remoto oficial do FlipHTML5 ao agente já existente no LangSmith Fleet, para que o agente possa consultar e, sob aprovação, gerenciar flipbooks da conta.

- Endpoint MCP: `https://mcp.fliphtml5.com/mcp`
- Escopo OAuth divulgado: `fliphtml5:books`
- Transporte: MCP remoto via HTTPS / Streamable HTTP.
- Serviço externo: FlipHTML5 mantém o servidor e executa as ferramentas.
- LangSmith Fleet descobre e encaminha ferramentas; não hospeda o servidor FlipHTML5.

Fontes:
- [FlipHTML5 — Conectar seu assistente via MCP](https://help.fliphtml5.com/pt/docs/connect-ai-assistant-to-fliphtml5-with-mcp/)
- [FlipHTML5 — página do servidor MCP](https://fliphtml5.com/features/mcp/)
- [LangSmith Fleet — Remote MCP servers](https://docs.langchain.com/langsmith/fleet/remote-mcp-servers)

## 2. Descobertas da pesquisa técnica

### 2.1 Desafio sem credenciais

Foi enviada uma chamada MCP `initialize` sem autenticação ao endpoint em 27/11/2026.

Resultado:
- HTTP `401`.
- `WWW-Authenticate: Bearer error="invalid_token", error_description="Authentication required"`.
- A resposta indicou o metadata público `https://mcp.fliphtml5.com/.well-known/oauth-protected-resource/mcp`.

Isso confirma que o endpoint exige autenticação; não significa que esteja indisponível.

### 2.2 Metadata público de recurso protegido

GET `https://mcp.fliphtml5.com/.well-known/oauth-protected-resource/mcp` retornou HTTP 200:

```json
{
  "resource": "https://mcp.fliphtml5.com/mcp",
  "authorization_servers": ["https://mcp.fliphtml5.com/"],
  "scopes_supported": ["fliphtml5:books"],
  "bearer_methods_supported": ["header"]
}
```

Interpretação: o recurso MCP aceita token Bearer enviado em cabeçalho HTTP e publica o escopo `fliphtml5:books`.

### 2.3 Metadata do authorization server

GET `https://mcp.fliphtml5.com/.well-known/oauth-authorization-server` retornou HTTP 200:

```json
{
  "issuer": "https://mcp.fliphtml5.com/",
  "authorization_endpoint": "https://mcp.fliphtml5.com/authorize",
  "token_endpoint": "https://mcp.fliphtml5.com/token",
  "registration_endpoint": "https://mcp.fliphtml5.com/register",
  "scopes_supported": ["fliphtml5:books"],
  "response_types_supported": ["code"],
  "grant_types_supported": ["authorization_code", "refresh_token"],
  "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic"],
  "code_challenge_methods_supported": ["S256"]
}
```

**Conclusão técnica:** o servidor anuncia endpoint de registro dinâmico de clientes (DCR), OAuth Authorization Code, refresh token e PKCE S256. Isso torna o modo OAuth 2.1 (Auto) do LangSmith Fleet o primeiro método a testar. Não foi feita inscrição DCR manual nem iniciado fluxo de autorização durante a pesquisa.

### 2.4 O que ainda não foi provado

- Não houve login autorizado no FlipHTML5 durante esta pesquisa.
- Não foi possível completar o OAuth handshake.
- Não foi executada chamada MCP autenticada nem `tools/list`.
- Ainda não conhecemos os nomes exatos, schemas e anotações read-only/destructive das ferramentas que o servidor expõe para esta conta.
- Não confirmamos que o MCP esteja habilitado no plano Free da conta. A página de features e a documentação de conexão descrevem o MCP, mas não estabelecem de modo inequívoco a elegibilidade por plano.
- O endpoint anunciar OAuth DCR não prova que o dashboard do Free exponha todos os recursos MCP ou todos os tipos de operação.

Não registrar integração como ativa até completar autorização, descoberta de ferramentas e teste de leitura.

## 3. Configuração recomendada no LangSmith Fleet

### Agente-alvo

A página aberta na sessão do usuário é o LangSmith Fleet. O contexto da página mostrou o agente existente `langchain-ai-design-agent`. Esse é o alvo apropriado para a primeira integração. Não registrar no Fleet > Integrations globalmente, porque isso poderia disponibilizar as ferramentas para todos os agentes do workspace.

### Passos na interface

1. Abrir o agente `langchain-ai-design-agent`.
2. Expandir o painel lateral **Connections**.
3. Selecionar **Add connection** e **+ Add custom MCP**.
4. Nome: `FlipHTML5`.
5. URL: `https://mcp.fliphtml5.com/mcp`.
6. Tipo de autenticação inicial: **OAuth 2.1 (Auto)**, pois o metadata do servidor anuncia registro dinâmico de cliente.
7. Salvar e seguir o fluxo de autorização/login que o Fleet apresentar.
8. Confirmar a permissão/escopo solicitado e conferir a conta FlipHTML5 correta.
9. Esperar o Fleet descobrir as ferramentas e registrar a lista real.
10. Testar primeiro uma operação de leitura: localizar/ler metadados de um flipbook público de teste. Conferir se título, link e identificador retornados correspondem à publicação.
11. Não usar um relatório real de cliente como primeiro teste.

A documentação atual do Fleet informa que OAuth 2.1 (Auto) registra um cliente para o servidor com DCR e encaminha o usuário para login quando necessário. A criação de servidor remoto requer permissão **MCP Server Create** no workspace.

### Alternativa: API key + Static Headers

A documentação do FlipHTML5 também oferece uma configuração manual:
1. No dashboard FlipHTML5: avatar/perfil → **Settings** → **MCP Server**.
2. Criar uma API key com nome reconhecível, por exemplo `LangSmith Fleet`.
3. Copiar a chave completa imediatamente. A chave completa é exibida apenas uma vez.
4. No LangSmith, criar o Custom MCP com o endpoint acima e autenticação **Static Headers**.
5. Usar o método/header exato indicado pelo prompt de configuração gerado pelo FlipHTML5. Não presumir que o campo tenha o mesmo nome em todos os clientes.

A documentação Fleet mostra o padrão comum `Authorization: Bearer API_KEY`; o endpoint do FlipHTML5 também declara Bearer via header. Mesmo assim, conferir o prompt gerado pelo FlipHTML5 antes de salvar a chave manualmente, pois a documentação de configuração manual não imprime literalmente o nome do cabeçalho.

**Nunca colar a chave neste repositório, em issue, chat, prompt compartilhado, código de frontend ou screenshot.** Inserir apenas no campo de credencial do LangSmith. Preferir OAuth Auto quando o fluxo for compatível, para evitar manuseio de chave estática.

## 4. Segurança e privilégio mínimo

### Começar com leitura

Depois que a descoberta retornar ferramentas:
- Listar os nomes, descrições, input schemas e anotações de cada ferramenta.
- Identificar as operações de leitura e separar das operações de escrita.
- Ativar inicialmente apenas as ferramentas de leitura necessárias, se Fleet permitir seleção por ferramenta.
- Se ferramenta de escrita permanecer habilitada, exigir confirmação/interrupt antes de usar.
- Não permitir criação/publicação, alteração de metadados, mudança de visibilidade, criação de senha, restrição por e-mail ou exclusão sem autorização explícita para a operação e o livro específico.
- Não assumir que o OAuth scope `fliphtml5:books` é read-only; o metadata não descreve granularidade de permissão.

### Risco de publicação pública

Conversão de documento online em flipbook pode criar uma publicação externa na conta. Não fornecer URL pública de relatório privado. No Free, verificar a exposição de cada livro: livro público, anúncios/marca d'água e possibilidade de download do PDF original são limitações documentadas do plano. OAuth MCP não muda automaticamente as restrições do plano contratado.

### Gestão de chaves

A documentação FlipHTML5 informa:
- A chave API completa aparece apenas na criação.
- Máximo de 10 chaves ativas por conta.
- Chaves não expiram automaticamente.
- Excluir uma chave pode levar aproximadamente 10 minutos para revogação completa.

Usar uma chave dedicada ao LangSmith, nomeada e revogável; não reutilizar uma chave de outra integração. Em caso de vazamento, apagar e substituir, esperando a janela de revogação indicada.

## 5. Operações documentadas pelo fornecedor

A documentação do FlipHTML5 descreve estas capacidades MCP:
- Converter documentos online em flipbooks.
- Encontrar detalhes de livros existentes.
- Atualizar título, descrição e palavras-chave.
- Gerenciar acesso público/privado, proteção por senha ou acesso restrito por e-mail.

A lista acima descreve capacidades gerais do produto; não é a lista de ferramentas efetivamente descoberta nesta conta. Nomes e schemas concretos precisam ser registrados após `tools/list` autenticado no LangSmith.

## 6. Teste de aceitação depois de conectar

| Gate | Evidência exigida |
|---|---|
| Autenticação | OAuth concluído ou Static Header validado; sem token em logs |
| Descoberta | Lista real de ferramentas e schemas capturada |
| Escopo | Servidor anexado apenas ao `langchain-ai-design-agent` |
| Read-only | Consultar metadados de um flipbook público de teste |
| Escrita | Interrompida/confirmada antes da primeira alteração |
| Free | Conta e recursos efetivamente disponíveis conferidos no dashboard |
| Revogação | Procedimento para desconectar o agente e revogar token/chave documentado |
| Resultado | ID/link do livro de teste e resposta verificados no dashboard |

**Estado atual:** a pesquisa do endpoint e dos metadados públicos está concluída; integração no LangSmith não foi salva, porque a sessão ainda não demonstrou login/credencial do FlipHTML5 e o painel do agente não pôde ser modificado nesta sessão. Não declarar como instalado.

## 7. Fontes oficiais

- FlipHTML5 MCP: https://help.fliphtml5.com/pt/docs/connect-ai-assistant-to-fliphtml5-with-mcp/
- FlipHTML5 MCP features: https://fliphtml5.com/features/mcp/
- LangSmith Fleet remote MCP: https://docs.langchain.com/langsmith/fleet/remote-mcp-servers
- FlipHTML5 OAuth protected-resource metadata: https://mcp.fliphtml5.com/.well-known/oauth-protected-resource/mcp
- FlipHTML5 OAuth authorization-server metadata: https://mcp.fliphtml5.com/.well-known/oauth-authorization-server

Pesquisa técnica observacional de 27/11/2026. Repetir handshake e discovery após autenticar, porque o servidor e os recursos disponíveis podem mudar.
