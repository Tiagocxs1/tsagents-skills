# Revisão dos score engines legados — dashboard

> Inspeção de código versionado em 21/11/2026. Esta referência não modifica nem substitui os motores existentes. Usá-la para guiar uma refatoração com testes e comparação de resultados.

## Onde estão

1. \`dashboard/src/components/contents/WpEditorModal.tsx\` importa \`dashboard/src/lib/seo-score-engine.ts\`. É o score exibido no modal WordPress da interface principal.
2. \`dashboard/client-cms/src/lib/seo-score-engine.ts\` contém uma segunda implementação de score para o CMS cliente, com pesos e regras em parte diferentes.
3. \`dashboard/src/lib/webstories-seo-score.ts\` tem avaliador específico de Web Stories.
4. Há testes Vitest para \`src/lib/seo-score-engine.ts\` em \`src/__tests__/lib/seo-score-engine.test.ts\`. A árvore consultada não apresentou suíte equivalente para \`webstories-seo-score.ts\`.

## Pontos aproveitáveis

- Score ponderado com breakdown por critério e indicação de ganhos possíveis.
- Detecção inicial de tipo de conteúdo (artigo, notícia, receita, vaga, produto).
- Avaliação de heading structure, mídia, links, snippet, canonical e dados estruturados.
- Cache por ID/data de modificação e atualização progressiva na interface.
- Painel separado de SEO e dados de Search Console.
- Testes unitários para helpers e critérios.
- A versão CMS contém tratamento de vários tipos de conteúdo e alguns critérios neutros para itens não aplicáveis.

## Problemas a corrigir na implementação principal

| Código/critério | Problema identificado | Direção de correção |
|---|---|---|
| Título 50–60 caracteres | Trata faixa de caracteres como regra universal | Avaliar precisão, clareza, promessa e preview renderizado; caracteres apenas como diagnóstico |
| Descrição 120–160 | Limites rígidos para snippet | Avaliar utilidade, especificidade e adequação ao conteúdo; mostrar comprimento como orientação, não regra fixa |
| Word count | Tiers fixos por tipo ainda premiam chegar a números arbitrários | Comparar completude e extensão com intenção, brief e SERP; não incentivar enchimento |
| Keyword density | 0,5–2,5% é alvo matemático legado | Remover do score; verificar naturalidade, cobertura semântica e repetição artificial |
| Keyword em H2 | Obriga repetição de foco keyword em subtítulo | Exigir headings que organizem o assunto; keyword só quando natural/descritiva |
| Alt da imagem | Dá nota maior quando contém keyword | Alt deve descrever a imagem; não forçar palavra-chave |
| Links internos/externos | Exige até 5 internos e 3 externos por post | Avaliar pertinência, qualidade, necessidade e link text; não impor quota universal |
| Slug | Penaliza stop words e ausência literal da keyword | Priorizar URL curta, descritiva, estável e legível; stop words podem ser necessárias |
| Readability/Flesch-BR | O algoritmo usa apenas palavras por sentença, não Flesch real nem contagem de sílabas | Renomear heurística ou substituir por medição PT-BR validada; combinar com revisão humana |
| Schema | A presença de JSON-LD e campos selecionados não prova conformidade completa | Validar JSON-LD, tipo, propriedades e requisitos atuais do tipo de resultado |
| OG/Twitter | Procura strings em HTML sem validar parsing/campos efetivos | Interpretar tags reais e distinguir propriedade ausente de metadado não acessível |
| Core Web Vitals | Usa PageSpeed/Lighthouse score como se fosse CWV | Separar métricas de campo LCP/INP/CLS de laboratório e PSI performance score |
| Bio do autor | Dá valor máximo por URL externa e sugere LinkedIn como exigência | Avaliar autoria verdadeira, experiência pertinente, bio e fontes; nenhuma rede é obrigatória |
| BLUF | Exige lista com 3 itens nos primeiros 20% | Avaliar se resposta inicial e resumo ajudam o leitor; lista só quando adequada |
| FAQ | Incentiva FAQ schema para “AI Overviews” | FAQ só quando responde a dúvidas reais; nunca prometer rich result nem exigir markup |
| RAG structure | Exige tabela, lista ordenada e blockquote como sinais de extração | Priorizar estrutura semântica e resposta clara; não inserir elementos sem função |
| ToC | Threshold rígido de palavras | Aplicar conforme extensão, complexidade e navegação real |
| YMYL / Reviewed By | Heurística baseada apenas em categorias e regex superficial | Classificar risco pelo conteúdo; exigir revisor real quando o risco justificar |
| Bold definitions / GEO | Premia frases artificiais em negrito com padrão fixo | Remover pontuação; usar definições claras apenas quando úteis |
| Freshness | Premia data recente de modificação sem verificar o que mudou | Avaliar se fatos mudaram e se a revisão foi substancial, registrada e correta |

Também revisar \`extractLinks\`: URLs relativas, \`mailto:\`, \`tel:\`, \`javascript:\` e fragmentos não podem ser todos contados como links internos; normalizar domínio, subdomínios e links absolutos/relativos.

A entrada do modal principal não fornece \`pageSpeedScore\`; por isso o critério de PageSpeed fica sem dado, mas é tratado como zero no score total. A nova implementação deve separar \`unknown\` de falha e exibir cobertura/confiança.

## Problemas no avaliador Web Stories

O motor \`webstories-seo-score.ts\` contém campos que não são avaliados ou recebem defaults presumidos:
- Critério “Título com Keyword” tem score fixo 0; não recebe keyword de entrada.
- “Publisher Name consistente” recebe pontuação total assumida, sem validar o nome.
- \`textToImageRatio\` assume 0,5 quando não informado.
- Categoria desconhecida recebe pontuação mínima positiva sem evidência.
- Schema VideoObject é pontuado como requisito fixo sem verificar se há vídeo.
- O alvo de 13 páginas é pontuado como SEO universal, quando na realidade é requisito deste pacote editorial específico.

Direção:
- Passar os campos reais e validar o resultado.
- Quando dado não existir, marcar \`unknown\` e remover o peso do denominador.
- Manter 13 slides como requisito do workflow solicitado, não como fator de ranking.
- Separar conformidade técnica, qualidade narrativa, legibilidade, acessibilidade e direitos.

## Plano de refatoração

### Fase 1 — Especificação e fixtures
- Adotar \`seo-editorial-scorecard/SKILL.md\` como rubric geral.
- Definir perfis por conteúdo: article, news, recipe, job, product, page e Web Story.
- Criar fixtures reais anonimizadas/representativas para cada perfil.
- Definir critérios automáticos, manuais, unknown e N/A.

### Fase 2 — Biblioteca única
- Criar núcleo puro e compartilhado, com perfis configuráveis.
- Implementar parsers robustos para URL, HTML/head/schema e métricas.
- Manter métricas técnicas de site separadas do score editorial.
- Não hardcode thresholds sem fonte, tipo de conteúdo e justificativa.
- Preservar compatibilidade da UI por adapter até migração concluída.

### Fase 3 — Interface
- Exibir nota, pesos avaliados, cobertura, confiança e evidências.
- Ordenar recomendações por ganho prático e impacto, não apenas peso numérico.
- Mostrar informação de dados ausentes e motivos de N/A.
- Não criar CTA para “corrigir” item irrelevante apenas para melhorar nota.

### Fase 4 — Validação
- Unit tests para todos os critérios.
- Casos de multiword keyword, idiomas com acentos, URL com query/trailing slash, H1 externo ao conteúdo, schema JSON-LD com \`@graph\`, imagens decorativas, imagem sem alt, links tel/mailto e conteúdo sem PageSpeed.
- Comparar scores legado/novo e documentar diferenças.
- Testar o modal no navegador, desktop/mobile, antes de substituir o motor antigo.

## Critério de conclusão

Não remover os motores legados nem integrar a nova nota até:
- testes passarem;
- cobertura de dados ser visível;
- pontuação não ser influenciada por campos presumidos;
- a UI explicar que o score é uma ferramenta de QA, não uma previsão de ranking;
- preview real do modal ser validado visualmente.
