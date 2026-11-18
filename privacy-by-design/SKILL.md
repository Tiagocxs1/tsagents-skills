---
name: privacy-by-design
description: Use whenever code, architecture, APIs, databases, authentication, analytics, logs, AI integrations, retention or user-facing workflows process personal data. Applies LGPD/GDPR privacy by design and default with evidence-based engineering checks.
---

# Privacy by Design — engenharia de software

> Guia técnico e procedimental. Não é parecer jurídico, certificação LGPD/GDPR ou substituto de profissional qualificado.

## Quando ativar
Ative ao criar ou alterar cadastro, perfil, autenticação, mensagens, arquivos, uploads, busca, analytics, cookies, telemetria, suporte, pagamentos, integrações externas, exportação ou exclusão de dados. Ative também em revisões de banco, APIs, RLS, storage, logs e backups.

## Processo obrigatório

### 1. Mapeie o tratamento antes do código
Registre, sem presumir respostas:
- Quem é controlador, operador e eventual suboperador.
- Quais jurisdições e tipos de titulares podem estar envolvidos.
- Quais dados são coletados, gerados, inferidos, armazenados, consultados ou compartilhados.
- Finalidade específica de cada campo e evento.
- Origem dos dados, destinatários, terceiros e regiões de processamento.
- Prazo/critério de retenção, descarte e exceções legais.
- Caminhos de acesso, correção, exportação, oposição, portabilidade e exclusão.
- Se há dados sensíveis/especiais, crianças/adolescentes, dados financeiros, autenticação, localização ou comunicações privadas.

Se faltar informação essencial, marque-a como desconhecida e proponha a opção técnica de menor exposição. Não invente base legal, prazo ou finalidade.

### 2. Minimize por padrão
- Cada campo precisa de finalidade documentada. Não coletar “por garantia”.
- Prefira identificadores internos opacos; não use CPF, e-mail, telefone ou nome como chave técnica.
- Evite duplicar dados pessoais entre serviços. Prefira referências e sincronização mínima.
- Não exponha dados pessoais em URL, query string, nomes públicos de arquivos ou mensagens de erro.
- Limite payloads, escopos OAuth, permissões, exportações e campos retornados.
- Use dados sintéticos em desenvolvimento, testes, demonstrações e screenshots.
- Separe produção, staging e desenvolvimento; nunca copie dumps reais para testes.

### 3. Documente base legal e transparência
- Não trate consentimento como base universal. A base depende do propósito, contexto, categoria de dados e jurisdição.
- LGPD: distinguir hipóteses do art. 7º (dados pessoais comuns) e art. 11 (dados sensíveis).
- GDPR: distinguir art. 6º (bases legais) e art. 9º (categorias especiais).
- Registre finalidade, base proposta, necessidade, proporcionalidade, destinatários e retenção por atividade.
- Se a base estiver indefinida, não a escolha em nome do controlador. Marque como decisão pendente.
- Interfaces de consentimento devem permitir escolha livre, específica e informada quando aplicável, revogação e registro de versão/data. Não crie dark patterns.

### 4. Implemente proteção técnica
- Autentique e autorize cada operação no servidor. Um JWT só é confiável após validar assinatura, emissor, audiência, expiração e claims aplicáveis.
- Aplique menor privilégio, isolamento entre usuários/tenants, autorização por recurso e defesa em profundidade.
- Mantenha secrets fora do código, navegador, logs, prompts, fixtures e histórico Git.
- Proteja dados em trânsito com TLS e dados armazenados com criptografia e gestão de chaves adequadas ao risco.
- Não presuma que citar “AES-256” torna o sistema seguro. Avalie geração, armazenamento, rotação, acesso, recuperação e descarte de chaves.
- Redija logs e telemetria: não registrar conteúdo de mensagens, arquivos, tokens, senhas ou PII sem necessidade demonstrada.
- Restrinja administradores, service roles, suporte e operações em lote; registre acessos privilegiados com o mínimo de dados.
- Proteja integrações e MCPs com escopos mínimos, ferramentas explicitamente permitidas e revisão das saídas antes de gravá-las.

### 5. Direitos, retenção e exclusão
- Projete fluxos verificáveis para localizar, acessar, corrigir, exportar, restringir e excluir dados conforme a lei aplicável.
- Exclusão lógica (deleted_at) não comprova remoção de dados, anexos, versões ou cópias.
- Implemente expurgo idempotente que trate banco, object storage, versões, thumbnails, CDN, caches, filas, índices, integrações e backups de acordo com a política.
- Mantenha registro operacional mínimo do pedido sem preservar desnecessariamente o conteúdo excluído.
- Respeite retenções obrigatórias, litígios, obrigações regulatórias e outras exceções válidas.
- Seja explícito sobre backups e replicação: exclusão imediata em todas as mídias pode não ser possível. Documente o ciclo de expiração e não prometa remoção que o provedor não garante.
- TTL é apropriado para arquivos temporários, tokens e dados efêmeros, conforme a finalidade e os requisitos reais.

### 6. Avalie terceiros e IA
Antes de enviar dados a analytics, IA, e-mail, suporte, storage ou MCP:
- Identifique fornecedor, finalidade, categorias, região, suboperadores e mecanismo de transferência.
- Envie o mínimo necessário; mascare ou pseudonimize quando possível.
- Verifique termos, DPA, retenção, uso para treinamento, exclusão e incidentes.
- Não envie segredos, dados reais, mensagens privadas ou dumps para ferramentas externas para facilitar debugging.
- MCP não é automaticamente seguro por ser local ou usar stdio. Revise código, dependências, rede, permissões e ferramentas expostas.

### 7. Teste como requisito de conclusão
Para mudanças relevantes, produza testes positivos e negativos:
- Usuário A não lê, altera, lista ou apaga dados do usuário B.
- Membro removido não continua acessando conversa/arquivo por URL antiga.
- Usuário não autenticado e token expirado são negados.
- Mudança de ID, path, bucket, conversation_id ou tenant_id não contorna autorização.
- Exclusão e retenção respeitam a política.
- Logs e erros não contêm conteúdo privado, tokens ou PII.
- Ferramentas administrativas não podem ser chamadas pelo cliente.
- Consentimento/revogação são respeitados quando aplicáveis.

Não conclua que o sistema está protegido sem executar os testes pertinentes no ambiente disponível.

## Formato da revisão
| Controle | Estado | Evidência (arquivo/linha/teste) | Risco | Correção |
|---|---|---|---|---|
| Controle verificado | PASS / GAP / PARCIAL / NÃO VERIFICADO / N/A | Evidência concreta ou “não localizada” | CRÍTICO / ALTO / MÉDIO / BAIXO | Ação técnica testável |

Finalize com decisões jurídicas pendentes, pressupostos, riscos residuais e testes não executados. Nunca use “100% compliant”, “à prova de vazamentos” ou “certificado” como conclusão de revisão automatizada.
