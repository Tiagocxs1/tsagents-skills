# Governança de ferramentas de segurança — TS Digitais

## Regra de ativação

Nenhuma Skill, MCP, CLI, extensão ou agente de pentest de terceiro entra em produção só porque o repositório é popular. Fluxo:

discovered → source_verified → license_checked → static_scanned → dependencies_reviewed → isolated_tested → approved → enabled

Estado padrão: **source pinned, not installed, not enabled**.

## Ferramentas aprovadas para estudo

| Ferramenta | Uso seguro pretendido | Limites atuais |
|---|---|---|
| NVIDIA SkillSpector | Varredura estática de Agent Skills antes de habilitar | Projeto Alpha; Python 3.12–3.15, YARA e dependências nativas; modo semântico pode enviar conteúdo a provider. Começar em modo offline/static e ambiente isolado. |
| Addy Osmani Security and Hardening | Revisão de código, STRIDE/OWASP, segredos, sessões, SSRF e dependências | Skill de revisão, não scanner dinâmico ou certificação. |
| Solo Founder Secure | Checklist de secrets, autorização por objeto, rate/spend limits, webhook e dependências | Complementar com testes reais e auditoria específica do banco/runtime. |
| Strix | Pentest dinâmico com prova de exploração em staging próprio | Requer Docker e uma chave LLM segundo README. Não executar em produção ou domínios de terceiros; não habilitar auto-fix sem revisão. |
| MCP Server Audit | Revisar autenticação, rede, Docker/Kubernetes/CI e controles MCP | Projeto comunitário de escopo limitado; não tratar como análise completa de protocolo ou certificação. |

## Controles antes de executar

1. Fixar commit e preservar LICENSE/NOTICE.
2. Ler código de instalação, scripts, workflow e dependências.
3. Executar em container/VM sem segredos do produto, sem escrita no GitHub e sem credenciais de produção.
4. Desabilitar egress de rede quando suportado; quando necessário, allowlist apenas fontes de advisories.
5. Não transmitir repositórios privados, prompts internos, secrets, dados de clientes, conversas ou assets a modelos externos.
6. Para Strix, usar build efêmero/staging com dados sintéticos e target autorizado.
7. Guardar relatório e hash do commit testado. Correções exigem teste de regressão.
8. Aprovar qualquer pentest que gere tráfego ou modifique estado.

## O que não foi executado

- SkillSpector, Strix e MCP Server Audit não foram instalados nem executados.
- Nenhuma skill foi executada em produção.
- Não foi realizado pentest externo, fuzzing de autenticação ou scan de domínio público.
- As fontes upstream estão pinadas como submodules; após clone, fazer static scan antes de carregar instruções de terceiros num agente.

## Portões técnicos para esta plataforma

- [ ] Segredos que já foram versionados: inventariar, revogar e rotacionar; limpar o histórico somente depois de preservar backup seguro.
- [ ] Conta A não pode ler/listar/alterar/excluir recursos da conta B, inclusive via URLs, IDs, busca, cache, storage, realtime e APIs administrativas.
- [ ] RLS validada com duas contas reais de teste e sem service_role.
- [ ] Chaves BYOK criptografadas em repouso, associadas ao tenant e nunca serializadas ao cliente; testar rotação e revogação.
- [ ] Webhooks validam assinatura, timestamp, idempotência e não concedem acesso por redirect de browser.
- [ ] Rate limits para login, upload, chat, geração, agentes, tools e recursos com custo; quotas por organização e provider.
- [ ] Uploads validam MIME real, tamanho, tipo e ownership; buckets privados e URLs assinadas curtas para conteúdo privado.
- [ ] Logs/traces não contêm prompts privados, mensagens, chaves, URL assinada ou dados pessoais desnecessários.
- [ ] Backup banco + Storage/R2 + configurações, com checksum e restauração ensaiada.
- [ ] Deploy protegido por CI, staging separado de produção e rollback testado.
- [ ] STRIDE, OWASP ASVS/Top 10 e riscos de prompt injection/agent-tool access revisados.

Uma caixa marcada significa teste com evidência arquivada, não apenas configuração presente.
