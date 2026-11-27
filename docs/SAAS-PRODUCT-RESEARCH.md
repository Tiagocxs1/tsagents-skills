# SaaS Product Research — TS Digitais Central

**Data da pesquisa:** 27/11/2026  
**Status:** hipótese comercial em validação. **Não é um Go de lançamento.**

## 1. Hipótese de produto

A hipótese inicial mais coerente com a implementação existente é uma central de operações para pequenas agências e profissionais de marketing que administram vários clientes: calendário, briefing, conteúdo, biblioteca de ativos, editor criativo, aprovações, agentes e relatórios. BYOK significa que cada organização usa suas próprias chaves/API accounts de modelos e provedores, enquanto a TS Digitais cobra pelo workspace, colaboração, armazenamento e automação hospedada.

**Comprador inicial a testar:** dono de agência pequena ou consultor de marketing que administra aproximadamente 3–15 marcas/clientes.  
**Usuário diário:** social media, designer, redator ou gestor de tráfego.  
**Problema a provar:** contexto, briefing, conteúdo, assets, aprovações e resultados ficam dispersos entre planilhas, chat, pastas e ferramentas com preço por marca/workspace/assento.

Não assumir que o utilizador quer inserir e manter as próprias chaves. BYOK é hipótese de controlo de custo e portabilidade, mas acrescenta fricção de onboarding, suporte a providers, gestão de segredos, rotação e troubleshooting.

## 2. Concorrência e sinais observáveis

| Produto | Posição observada | Sinal útil para a hipótese | Limitação da evidência |
|---|---|---|---|
| Planable | Planeamento, feedback e aprovação multi-cliente | Capterra mostra 4,5/5 em 331 avaliações em 25/11/2026. Uma avaliação 3/5 critica a qualidade dos uploads de imagem para clientes de fotografia; outras avaliações mencionam custo por cliente/workspace, analytics fora do plano base e limites de integração/edição. | Reviews individuais são qualitativas e não demonstram prevalência. |
| Metricool | Analytics, calendário e gestão multi-marca | Concorrente forte em relatórios e valor por marca; o plano Advanced publica equipa/gestão de clientes e aprovações. | Preços variam por moeda, região e data; confirmar plano oficial no checkout. |
| Buffer | Scheduler simples por canal | A página de reviews G2 resume queixas sobre analytics básicos, custo ao escalar contas e falhas de publicação; oportunidade não é ser apenas mais um scheduler. | Síntese agregada, não amostra controlada exclusiva de 3 estrelas. |
| Publer | Scheduler barato e multi-rede | Planos com workspaces, analytics e API pressionam qualquer produto que tente competir só por agendamento. | Recursos/preços mudam; validar no site do fornecedor. |
| Vista Social, Agorapulse, Sendible e HeyOrca | Gestão de contas, inbox, relatórios e workflows de agência | O mercado já oferece aprovações, multi-workspace de clientes e relatórios. | Comparativos editoriais, não entrevista de comprador nem auditoria contratual. |

**Fontes consultadas**
- Capterra, Planable reviews, atualizado 25/11/2026: https://www.capterra.com/p/171744/Planable/reviews/
  Uma avaliação 3 estrelas identificada em 06/11/2025 menciona qualidade/resolução de upload; outras reviews relatam custo por cliente/workspace, analytics fora do plano base e limites de edição.
- Capterra, Planable pricing: https://www.capterra.com/p/171744/Planable/pricing/
- G2, Planable reviews, atualizado 20/11/2026: https://www.g2.com/products/planable/reviews
  4,6/5 com 1.137 reviews na página consultada; approvals e calendário são valorizados, Social Ads aparece com nota menor na análise da página.
- G2, Buffer pros and cons: https://www.g2.com/pt/products/buffer/reviews?qs=pros-and-cons
  Síntese de queixas sobre analytics básicos, preço ao escalar e falhas de publicação.
- Product Hunt, categoria Social Media Scheduling, atualizada 25/11/2026: https://www.producthunt.com/categories/social-media-scheduling
  Listagem considera 119 produtos e 396 reviews; concorrência ativa e novos entrants.
- Comparativo editorial de agências, outubro 2026: https://www.agencyshed.com/guide/best-social-media-management-tools-for-agencies-2026

**Limite importante:** não foi possível fazer uma amostra estatisticamente válida de todas as reviews de 3 estrelas em G2/Capterra. A evidência acima separa uma review 3/5 identificada de resumos agregados. Não transformar relatos isolados em “dor de mercado comprovada”.

## 3. O que pode diferenciar o produto

O espaço competitivo não está em calendário, legendas ou agendamento isolado. Esses recursos são maduros e baratos.

Possível wedge a testar:
1. Workspace por cliente com briefing, tom de voz, marca, assets, tarefas, aprovações e histórico juntos.
2. Editor criativo com exportação de alta qualidade e armazenamento persistente de projetos/arquivos.
3. Agentes de IA com BYOK por organização, regras de orçamento, seleção de modelos e logs de uso.
4. Relatórios e documentos de cliente que associam conteúdo publicado a resultados medidos.
5. Preço simples por organização/volume de clientes, sem cobrar cada convidado aprovador.

**Nenhum destes diferenciais está validado como motivo de compra.** BYOK não é sozinho moat; pode ser um diferencial de controlo e custo, mas também uma barreira de setup.

## 4. Hipóteses críticas e experimentos

| Hipótese | Evidência necessária | Experimento mais barato | Gate provisório |
|---|---|---|---|
| Agências perdem tempo com contexto fragmentado | 5–8 exemplos recentes, ferramentas e tempo gasto | Entrevistas Mom Test; pedir para mostrar o último fluxo real | 5 de 8 descrevem dor frequente e quantificável |
| A central multi-cliente melhora o trabalho o suficiente para trocar/adicionar ferramenta | Uso repetido numa operação real | Concierge MVP com um cliente por agência, sem migrar todos os dados | 3 pilotos usam semanalmente por 3 semanas |
| BYOK é benefício, não fricção | Preferência espontânea e capacidade de configurar chave | Teste de oferta com/sem BYOK e onboarding observado | 3 compradores preferem BYOK e completam setup sem suporte excessivo |
| Qualidade/persistência de assets importa | Uploads e exports reais, especialmente high-res | Protótipo de projeto persistente e comparação com processo atual | 3 agências aceitam gerir projetos no workspace e pagariam |
| O comprador paga por uma plataforma, não apenas por ferramentas gratuitas | Pagamento ou piloto pago | Landing page + oferta explícita + pedido de pagamento/LOI qualificada | 3 pilotos pagos antes de desenvolver cobrança complexa |

**Prazo sugerido:** 14 dias para entrevistas e teste concierge. Não usar likes, cliques ou cadastros grátis como prova de disposição a pagar. Contar pagamento, tempo investido, migração real ou compromisso operacional verificável.

### Roteiro curto de entrevista

1. Mostre como organizou conteúdo e aprovações do último cliente.
2. O que aconteceu quando o cliente pediu uma mudança? Mostre a sequência real.
3. Quanto tempo gastou na última semana recuperando briefing, arquivos, aprovações e resultados?
4. Que ferramentas já paga para resolver isso? O que tentou substituir?
5. Quando foi a última vez que o processo causou atraso, retrabalho ou perda de cliente?
6. O que já pagou por uma solução semelhante? Mostre contrato/fatura se for confortável.
7. Que parte não deixaria uma nova plataforma armazenar ou processar?
8. Um piloto pago de 30 dias para um cliente, no valor apresentado, resolveria algo que prioriza agora?

Não começar com “você usaria?” nem perguntar preço sem explorar comportamento passado.

## 5. TAM / SAM / SOM

**Não estimado nesta versão.** Não há geografia definida, número confiável de agências elegíveis, receita média demonstrada nem taxa realista de conversão. Uma cifra top-down baseada em “mercado de social media software” seria falsa precisão.

Modelo bottom-up a preencher após validação:
- TAM = número de empresas no segmento definido × receita anual média possível.
- SAM = TAM limitado às regiões, idiomas, canais e necessidades cobertos pela versão que realmente funciona.
- SOM = clientes alcançáveis e suportáveis nos primeiros 24–36 meses × ARPA anual.
- ARPA deve partir de pagamentos reais; não copiar preço de concorrentes.

## 6. Monetização BYOK proposta para testar

**Não lançar tiers ainda.** Começar com uma única oferta paga de piloto para 1 organização, com número delimitado de clientes/marcas, colaboradores, storage e automações; BYOK separado do preço. O cliente paga diretamente aos providers de IA, sem markup oculto de tokens.

Uma eventual estrutura futura pode separar:
- SaaS: workspace, usuários, clientes, storage, automações, versões e suporte.
- BYOK: chamadas com as próprias chaves e contas do cliente.
- Add-ons: armazenamento acima da franquia, domínios/white-label, integrações de publicação e relatórios avançados.

A cobrança não deve depender de tokens inclusos quando o cliente traz suas chaves. Ainda assim, existem custos da plataforma: R2, banco, filas, egress, observabilidade, suporte e execução de agentes. Medir custo bruto por organização antes de fixar preço.

## 7. Veredito

**VALIDATION_REQUIRED — não declarar Go para o mercado ainda.**

- Existe concorrência estabelecida e necessidade de coordenação de trabalhos multi-cliente.
- Há relatos observáveis sobre preço por workspace/cliente, analytics fora do plano base, integrações e qualidade de uploads.
- Ainda não existem entrevistas, pilotos pagos ou dados de retenção desta TS Digitais Central que confirmem procura pelo conjunto proposto.
- A implementação atual ainda não oferece persistência completa do editor, isolamento multi-tenant SaaS independente, BYOK por organização, billing self-service e backups/restauração testados.

**Próximo gate:** três pilotos pagos, uso semanal durante três semanas e todos os gates técnicos de segurança e recuperação aprovados. Só depois avançar para preço público e expansão.
