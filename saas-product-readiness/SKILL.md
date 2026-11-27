---
name: saas-product-readiness
description: Use for SaaS product validation, market research, interviews, positioning, pricing, security, BYOK, multi-tenancy, privacy, resilience and production readiness.
---

# SaaS Product Readiness — TS Digitais

Esta skill orquestra validação e preparação de um SaaS. Não promete PMF, conformidade, segurança certificada ou prontidão comercial sem evidência.

## 1. Classifique a etapa e o produto

Leia primeiro, quando disponíveis:
- docs/SAAS-PRODUCT-RESEARCH.md
- docs/SECURITY-TOOLS-GOVERNANCE.md
- docs/UPSTREAM-ARSENAL.md
- external/design-library/registry.json
- AGENTS.md, README e implementação atual.

Registre a etapa: hipótese, pesquisa, protótipo, MVP, piloto, receita inicial ou escala. Não confunda deployment com produto pronto.

## 2. Descoberta e validação

Carregue somente os módulos necessários:
- Ideação: upstream/claude-saas-eval-skills/niche-idea-generator/SKILL.md.
- First pass de nicho: upstream/claude-saas-eval-skills/niche-research-first-pass/SKILL.md.
- Scorecard: upstream/claude-saas-eval-skills/niche-success-scorecard/SKILL.md, somente depois de ter dados para pontuar.
- Product discovery: upstream/ultimate-product-discovery/SKILL.md e o bloco de referências pertinente.
- Teste de demanda: upstream/solo-founder-skills/skills/validate/SKILL.md.
- Entrevistas, posicionamento e concorrência: upstream/claude-marketing-research/marketing-research/SKILL.md.
- Posicionamento, CRO e copy: usar o upstream existente upstream/marketing-skills-corey, selecionando product-marketing, cro e copywriting.

Evidência:
- Preferir fontes primárias, preços/documentação oficial e reviews verificáveis.
- Separar fatos, relatos individuais, agregados, hipóteses e inferências.
- TAM/SAM/SOM, willingness to pay e market score permanecem unknown quando faltam dados.
- Interesse, cadastro, elogio ou resposta “eu usaria” não provam compra.
- A validação só avança com comportamento real, custo do problema, compromisso e/ou pagamento.

## 3. Entrevistas e testes

Usar The Mom Test/JTBD: perguntar sobre fluxo passado, último incidente, solução atual, frequência, tempo, custo, workaround e compra anterior. Não ensinar ao entrevistado a resposta nem apresentar protótipo cedo demais.

Experimentos devem definir antes da execução:
- hipótese;
- segmento e amostra;
- uma métrica primária;
- barra de sucesso;
- prazo;
- ação seguinte em cada resultado.

Antes de uma decisão Go, procurar sinais de compra verificáveis, como piloto pago, depósito, migração real ou compromisso formal. Falta de resposta não é evidência positiva.

## 4. Modelo BYOK e economia do produto

Para BYOK por organização:
- cada tenant tem sua própria lista de providers, modelos e chaves;
- chaves nunca são expostas no browser, logs, telemetria ou prompts de outro tenant;
- armazenar ciphertext com envelope encryption e chave de wrapping separada; rotação e exclusão documentadas;
- autenticar o utilizador e verificar permissão do tenant em toda leitura/uso/alteração;
- o cliente paga o provider diretamente; a cobrança da plataforma cobre workspace, colaboração, armazenamento, execução e suporte;
- quotas e rate limits continuam necessários para evitar abuso, mesmo quando o provider é pago pelo cliente;
- exibir custo estimado/medido quando a API oferecer informação, sem inventar preço ou consumo.

Não implementar criptografia própria sem revisão de desenho, threat model, testes e biblioteca aprovada.

## 5. Segurança e privacidade

Carregue:
- upstream/solo-founder-skills/skills/secure/SKILL.md;
- upstream/addyosmani-agent-skills/skills/security-and-hardening/SKILL.md;
- a skill local privacy-by-design/SKILL.md;
- messaging-private-storage/SKILL.md;
- skills oficiais Supabase/Cloudflare quando o stack tocar esses serviços.

Para Supabase:
- RLS habilitada em schemas expostos e policies explicitamente testadas;
- policy por tenant/owner e por objeto/ação, não somente authenticated;
- nunca usar user_metadata para autorização;
- service_role só no backend;
- testar duas contas/tenants sem chave privilegiada.

## 6. Ferramentas de auditoria

Antes de ativar skills/MCPs:
- seguir docs/SECURITY-TOOLS-GOVERNANCE.md;
- usar SkillSpector em cópia isolada, começando sem análise LLM;
- rever os resultados antes de confiar em score automatizado;
- pentest Strix somente em staging autorizado com dados sintéticos;
- MCP Server Audit como orientação/checklist limitada, não como certificação.

Nunca executar comandos de upstream sem leitura. Não instalar dependências, executar scripts, iniciar contêiner, fazer deploy, publicar ou chamar APIs que gerem custos/efeitos externos sem avaliar o impacto.

## 7. Produto e prontidão operacional

Avaliar e demonstrar com teste:
- cadastro, autenticação, recuperação e sessão;
- tenancy e autorização por objeto;
- onboarding, convite de membros e ciclo de vida da organização;
- persistência e recuperação de projetos, mensagens e arquivos;
- versionamento e histórico;
- BYOK por tenant, rotação e revogação;
- fila/retry/idempotência para tarefas demoradas;
- limites, quotas, custos e alertas;
- cobrança, webhook assinado, plano, cancelamento e downgrade;
- backup de banco e storage, checksum e restauração real;
- observabilidade sem dados sensíveis;
- CI, staging, migrações controladas, rollback e smoke tests;
- privacidade, termos, exclusão/exportação, retenção e suporte.

Uma feature não é persistente enquanto não for possível fechar a aba, abrir outra sessão e recuperar o estado do servidor.

## 8. Relatório final

Use a tabela:
| Gate | Estado | Evidência | Risco | Correção | Revalidação |

Estados permitidos: PASS, FAIL, BLOCKED, NOT TESTED. Não marcar PASS com base apenas em leitura estática.

Decisão de lançamento:
- NO-GO: qualquer risco crítico em tenancy, auth, secrets, perda de dados, billing ou abuso de custo.
- PILOT ONLY: nenhum crítico aberto, mas faltam escala, documentação ou validação de mercado.
- GO: todos os gates obrigatórios passaram, há restauração comprovada, pilotos pagantes e operação monitorada.

Não declare que o SaaS está pronto apenas porque o site abre ou o CI passa.
