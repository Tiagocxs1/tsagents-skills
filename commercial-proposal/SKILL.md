---
name: commercial-proposal
description: Criar propostas comerciais profissionais, apresentações de venda, escopos, cronogramas e orçamentos com dados verificáveis, identidade visual da marca e versão editável mais PDF.
---

# Commercial Proposal — TS Digitais

Skill para propostas comerciais de sites, sistemas, automações, chatbots, conteúdo, design, vídeo, apresentações, marketing e serviços digitais. Produz uma proposta clara, visual e executável, sem promessas ou preços inventados.

## Referências obrigatórias

- Ler presentation-studio/SKILL.md.
- Ler visual-design/SKILL.md e visual-quality-review/SKILL.md.
- Consultar docs/PRESENTATION-TOOLING.md.
- Consultar a ficha de marca em brands/<slug>/, quando existir.
- O upstream alireza-claude-skills/business-growth/skills/contract-and-proposal-writer/SKILL.md pode servir como referência de estrutura documental. Suas cláusulas jurídicas e jurisdições não devem ser copiadas automaticamente para contratos brasileiros.

## 1. Fontes e dados de entrada

Priorizar, nesta ordem:
1. Briefing, mensagens e transcrição fornecidos para este trabalho.
2. Escopo, preços, condições e prazos aprovados pelo usuário.
3. Documentos comerciais atuais e tabelas de preços efetivamente presentes no projeto.
4. Informações públicas verificadas do cliente e da sua marca.

Se faltar um preço, prazo, condição comercial, nome legal, dado de resultado ou compromisso, marcar como **A DEFINIR** ou perguntar o dado essencial. Não reutilizar preços antigos da memória como se fossem uma tabela vigente. Não completar campos legais com suposições.

Preservar moeda, quantidade, unidade, frequência, impostos, validade e condições exatamente como aprovados. Recalcular subtotais e total; se houver divergência entre o total declarado e a soma, sinalizar antes de finalizar.

## 2. Estrutura recomendada

Adaptar o número de páginas ao negócio e à complexidade. Estrutura padrão:
1. **Capa:** nome do cliente, projeto, data e identidade do proponente.
2. **Resumo executivo:** oportunidade e solução em linguagem direta.
3. **Contexto/diagnóstico:** situação atual e necessidades informadas ou verificadas.
4. **Objetivos:** resultados pretendidos, distinguindo metas de garantias.
5. **Solução proposta:** abordagem e por que cada parte responde ao problema.
6. **Escopo e entregáveis:** tabela com item, descrição, quantidade/unidade e critério de conclusão.
7. **Cronograma:** fases, dependências, marcos e responsabilidades.
8. **Investimento:** setup, recorrência, itens opcionais, forma de pagamento e total.
9. **Premissas e exclusões:** o que depende do cliente, o que não está incluído e limites de suporte.
10. **Próximos passos:** aprovação, materiais necessários e início previsto.

Para propostas curtas, condensar sem perder escopo, preço, responsabilidades e condições. Não criar páginas vazias apenas para atingir uma quantidade de slides.

## 3. Tabela de escopo

Para cada entrega, explicitar:
- O que será feito.
- Quantidade ou limite (páginas, telas, peças, integrações, revisões, horas etc.).
- O que o cliente precisa fornecer.
- O que está excluído.
- Como será considerada concluída.
- Dependências, acessos e aprovações.

Distinguir claramente implementação inicial, mensalidade, manutenção, hospedagem, serviços de terceiros, consumo de API/créditos, licenças e trabalho adicional. Não chamar custos de terceiros de gratuitos sem confirmar modalidade e limites.

## 4. Investimento e ROI

- Apresentar valores em tabela legível, com subtotais e total conferidos.
- Separar implantação, recorrência, adicionais opcionais e custos externos.
- Explicitar validade da proposta e condições de pagamento somente quando fornecidas/aprovadas.
- ROI só pode ser calculado quando houver dados e premissas explícitos. Mostrar fórmula, período, custos incluídos e cenário. Chamar projeção de projeção, nunca de resultado garantido.
- Não inventar porcentagens, economias, aumento de leads, conversão, faturamento ou payback.
- Se a proposta precisar de preço ainda não definido, gerar estrutura sem precificação ou deixar o campo pendente.

## 5. Linguagem comercial

- Escrever com precisão, clareza e confiança, sem exagero, urgência artificial ou promessas absolutas.
- Relacionar cada funcionalidade ao benefício do cliente, sem confundir benefício esperado com resultado comprovado.
- Evitar jargões de IA e listas de serviços desconectadas do problema.
- Usar prova social apenas quando houver autorização e fonte real.
- Não inventar portfólio, clientes atendidos, certificações, cases ou depoimentos.

## 6. Apresentação visual

- Preferir PPTX editável mais PDF final, salvo se o cliente solicitar Google Slides ou HTML.
- Aplicar a marca do proponente e, quando adequado, a identidade do cliente sem misturá-las.
- Usar uma ideia principal por slide, headlines informativas, gráficos nativos e tabelas com tipografia legível.
- Variar layouts: capa, diagnóstico, processo, entregáveis, cronograma, investimento e encerramento.
- Não converter todos os slides em imagens achatadas quando a editabilidade for importante.
- Não inserir texto comercial dentro de imagens geradas por IA quando a exatidão for crítica.

## 7. Termos e limites jurídicos

Esta Skill produz propostas comerciais, não parecer jurídico nem contrato pronto. Não inventar cláusulas de propriedade intelectual, multa, juros, garantia, foro, cancelamento, renovação automática, SLA, tratamento de dados ou responsabilidade. Usar placeholders ou solicitar os termos aprovados. Para contrato, DPA, NDA ou SOW com obrigações legais, exigir revisão jurídica local e verificar legislação brasileira vigente em fontes oficiais.

## 8. Conferência final

Antes de entregar:
- Confirmar nomes, datas, URLs, valores e moeda.
- Recalcular subtotais, impostos e total conforme dados fornecidos.
- Conferir coerência entre escopo, cronograma, equipe, investimento e condições.
- Conferir que todas as exclusões e dependências relevantes estão visíveis.
- Renderizar e inspecionar todas as páginas do PPTX/PDF ou todas as telas do HTML.
- Corrigir textos cortados, desalinhamentos, fontes pequenas, imagens de baixa qualidade e inconsistências de marca.
- Entregar a proposta editável e a versão PDF quando disponíveis, sem declarar validação que não ocorreu.
