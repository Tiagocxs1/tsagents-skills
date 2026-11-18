---
name: messaging-private-storage
description: Use when building or reviewing private chat, direct messages, group conversations, media, attachments, file uploads/downloads, object storage, sharing links, retention or deletion in multi-user apps.
---

# Mensageria privada e compartilhamento seguro de arquivos

> Guia técnico. A arquitetura deve ser revisada contra a threat model e obrigações jurídicas reais. Não é certificação de segurança ou parecer jurídico.

## 1. Modelo de autorização
- Derive a identidade do principal de um token validado no servidor. Nunca confie em user_id, tenant_id, owner_id ou sender_id enviados livremente pelo cliente.
- Antes de cada leitura, escrita, listagem, download, alteração ou exclusão, valide no servidor se o usuário atual é membro ativo e tem permissão sobre o recurso.
- Autorização é por objeto e ação, não apenas por rota autenticada.
- Em conversas, confirme a associação entre o principal e conversation_id e a condição de membro ativo. Em grupos, valide papel para ações administrativas.
- Use IDs imprevisíveis para reduzir enumeração, mas nunca trate UUID/IDs aleatórios como controle de acesso.
- Aplique isolamento por tenant no banco, consultas, cache, filas, busca, storage, realtime e APIs administrativas.
- Implemente testes negativos: usuário A não pode consultar, pesquisar, enumerar, editar ou apagar recursos de B.

### Supabase/Postgres (quando usado)
- Ative RLS nas tabelas expostas. Crie políticas explícitas para SELECT, INSERT, UPDATE e DELETE; não dependa de políticas genéricas permissivas.
- Valide associação a conversas por tabela de participantes/membros e compare com o usuário autenticado.
- Em INSERT, force/valide sender_id = auth.uid(); em UPDATE/DELETE, valide autor e/ou papel.
- Configure políticas próprias em storage.objects; pasta com ID do usuário não substitui validação de participação na conversa.
- A chave service_role nunca pode chegar ao browser, mobile app, HTML público ou bundle cliente.
- Teste com dois usuários e tokens distintos; não valide RLS apenas com role administrativa.

## 2. Banco e conteúdo de mensagens
- Defina o que significa apagar: ocultar para um usuário, apagar para todos, expirar, moderar ou remover fisicamente. Não misture semânticas.
- Evite duplicar nome, e-mail, telefone ou perfil em cada mensagem. Prefira relacionamentos internos.
- Não registre corpo da mensagem, anexos, tokens, links assinados ou conversas em logs, traces, analytics ou relatórios de erro.
- Minimize metadados: timestamps, IPs, device IDs, status de leitura/entrega, tamanho, remetente/destinatário e relações entre conversas também podem revelar hábitos e relacionamentos.
- Use retenção por finalidade e categoria. Não mantenha tudo indefinidamente por conveniência.
- Proteja exportações, moderação, busca e suporte com permissões e trilha de auditoria mínima.

## 3. Uploads e downloads
- Use buckets privados por padrão. Não habilite acesso público como atalho para mostrar imagens/documentos.
- Gere caminhos/object keys opacos no servidor; não confie em nomes, paths ou IDs fornecidos pelo cliente para definir propriedade.
- Antes de emitir URL assinada, valide autenticação, membership, permissão, estado de exclusão e expiração.
- Trate URL assinada como bearer credential: TTL curto, escopo para um objeto/ação, sem colocá-la em logs, analytics ou URLs permanentes.
- Valide tamanho, extensão, MIME declarado e assinatura real do arquivo (magic bytes). Defina allowlist.
- Limite quantidade, tamanho, taxa de upload e tipos perigosos. Proteja contra path traversal, polyglots, decompression bombs e abuso de quota.
- Coloque arquivos suspeitos em quarentena e use antivírus/sandbox quando o risco justificar. Não disponibilize antes das verificações relevantes.
- Remova EXIF/geolocalização de imagens quando não forem necessários; proteja previews e thumbnails como cópias adicionais.
- Defina Content-Disposition, Content-Type e cache adequados. Evite cache público de documentos privados.
- Nunca retorne URL pública duradoura para conteúdo que deveria depender de autorização.

## 4. Criptografia e chaves
- Use HTTPS/TLS em todas as conexões, incluindo APIs, storage, realtime e callbacks.
- Confirme criptografia em repouso do banco e object storage, incluindo backups quando disponível.
- Considere criptografia em nível de aplicação para conteúdo de alto risco, com envelope encryption e gestão separada de chaves.
- Rotacione e restrinja acesso às chaves. Mantenha chaves fora do banco de conteúdo e do cliente, salvo chaves de usuário em um desenho E2EE deliberado.
- Criptografia ponta a ponta (E2EE) é decisão arquitetural baseada no threat model, não uma exigência universal automática da LGPD/GDPR. Ela afeta busca, moderação, sincronização, backup e recuperação.
- Não declare E2EE se o servidor consegue descriptografar o conteúdo em operação normal. Documente limites, recuperação e modelo de confiança.

## 5. Ciclo de vida e exclusão
Modele rotina idempotente e observável:
1. Autenticar e verificar direito/escopo do pedido.
2. Tornar o recurso indisponível imediatamente, revogar links e bloquear novas leituras.
3. Criar evento de expurgo em outbox/fila com chave de idempotência.
4. Excluir conteúdo e derivados no banco, storage, versões, previews, thumbnails, cache/CDN, índices, filas e integrações sob controle do sistema.
5. Registrar resultado operacional mínimo sem copiar o conteúdo apagado.
6. Tratar falhas, retries, dead-letter e reconciliar órfãos.
7. Aplicar regras documentadas para backups, snapshots e retenções legais.
8. Permitir verificar conclusão sem revelar dados de terceiros.

Não confunda deleted_at com apagamento concluído. Se o provedor conserva snapshots/versões por um período, documente esse prazo e não prometa eliminação física instantânea. Avalie crypto-erasure apenas se o desenho provar que não há cópia de chave ou plaintext recuperável.

Arquivos temporários precisam de TTL explícito, rotina de limpeza, limite de tamanho e tratamento de órfãos. A retenção de mensagens, anexos e backups deve ser documentada e consistente.

## 6. Threat model mínimo
Considere:
- IDOR/BOLA e enumeração de conversas/arquivos.
- RLS ausente, permissiva ou inconsistente.
- Vazamento por URL assinada, bucket público, cache/CDN ou logs.
- Reutilização de token, conta comprometida e membership revogada.
- Upload malicioso, arquivo enorme, polyglot, malware e decompression bomb.
- Escalada por service_role, RPC, painel administrativo ou MCP.
- Metadados, exportação, busca cross-tenant e backups esquecidos.
- XSS em previews, HTML/Markdown de mensagens e arquivos servidos por domínio confiável.

## 7. Gate de testes
- [ ] Dois usuários em conversas distintas: leitura/escrita/download cruzado negado.
- [ ] Usuário removido: novo acesso e links antigos revogados/expirados conforme desenho.
- [ ] IDs e object keys manipulados: acesso negado.
- [ ] Bucket sem leitura pública e política de storage testada sem service_role.
- [ ] Upload rejeita tamanho, tipo e conteúdo proibidos.
- [ ] Logs, erros e telemetria sem conteúdo privado ou credenciais.
- [ ] Exclusão cobre registros e derivados; backups seguem política documentada.
- [ ] Busca, realtime, previews, notificações e exportação respeitam membership.
- [ ] Segredos ausentes de bundle, Git, fixtures e artefatos de CI.

Se o projeto usa Supabase, Firebase, S3, R2, Cloudflare ou PostgreSQL, confira a documentação atual do fornecedor antes de assumir o comportamento de RLS, URL assinada, criptografia, versionamento ou exclusão.
