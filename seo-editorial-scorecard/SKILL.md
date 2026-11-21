---
name: seo-editorial-scorecard
description: Avalie conteúdo web com um scorecard editorial e técnico contextual, baseado em intenção, utilidade, confiabilidade, on-page e elegibilidade técnica. Use para revisar artigos, páginas, notícias e conteúdos derivados; não o trate como previsão de ranking.
---

# SEO Editorial Scorecard

## Objetivo

Reaproveitar e modernizar os critérios que já existem nos motores SEO do projeto \`dashboard\` (26 critérios para WP) e no avaliador de Web Stories, removendo regras arbitrárias e falsos positivos. O score deve orientar melhorias, não simular um algoritmo de Google.

A referência principal é conteúdo útil, confiável e feito para pessoas. O próprio Google recomenda conteúdo people-first e uso natural de termos que as pessoas pesquisam; não define densidade de keyword ou contagem universal de palavras como requisito de ranking.

## Como pontuar

- Usar perfil adequado: artigo, notícia, receita, vaga, produto ou landing page. Não transportar os mesmos pesos para formatos diferentes.
- Cada critério recebe estado \`pass\`, \`warning\`, \`fail\`, \`unknown\` ou \`not_applicable\`.
- Anexar evidência: elemento medido, URL/fonte, trecho, ferramenta e data quando possível.
- Dados não disponíveis são \`unknown\`, não zero.
- Critérios não aplicáveis saem do denominador.
- Exibir cobertura e confiança junto ao resultado. Um score de 95 com 40% de cobertura não é “95% aprovado”.
- Calcular a nota normalizada apenas sobre pesos aplicáveis e avaliados. Informar quais pesos ficaram desconhecidos/não avaliados.
- Separar automação objetiva (meta, links, indexabilidade, schema parseável) de julgamento editorial (intenção, originalidade, qualidade de fontes, utilidade).
- O score final mede qualidade da execução e da auditoria. Não prevê ranking, indexação, elegibilidade para rich results nem tráfego.

## Domínios de avaliação — artigos

Usar 100 pontos como distribuição inicial, ajustável por perfil:

| Domínio | Peso inicial | O que avaliar |
|---|---:|---|
| Intenção e cobertura | 20 | Responde à intenção principal; cobre subperguntas importantes; conteúdo completo sem digressões |
| Valor, evidência e confiança | 30 | Originalidade/informação adicional; fontes primárias; precisão factual; autoria/experiência comprovável; limitações e atualização relevante |
| Estrutura e legibilidade | 20 | Hierarquia coerente; resposta rápida; clareza; escaneabilidade; exemplos/etapas que realmente ajudam |
| On-page e mídia | 15 | Título e snippet descritivos; slug compreensível; links internos contextuais; fontes externas apropriadas; imagem pertinente e alt descritivo |
| Elegibilidade técnica | 15 | Indexabilidade/canonical; dados estruturados aplicáveis e válidos; metadados sociais; experiência mobile e Core Web Vitals de campo quando disponíveis |

Os pesos são uma referência de QA editorial, não fatores oficiais de ranking.

## Regras para não repetir os problemas antigos

1. **Contagem de palavras:** não pontuar por atingir 1.500, 2.500 ou outro número universal. Comparar com intenção, formato, SERP e completude. Se o briefing tiver meta justificada, medir em relação a ela, mas não premiar parágrafos de enchimento.
2. **Densidade de keyword:** não impor faixa de 0,5–2,5%. Verificar uso natural da expressão e cobertura semântica; penalizar repetição artificial, não baixa densidade matemática.
3. **Título/meta:** não tratar 50–60/120–160 caracteres como limites universais. Avaliar clareza, correspondência com a página, promessa honesta e truncamento estimado na prévia do snippet; pixels e dispositivo importam.
4. **Keyword:** avaliar presença natural em locais descritivos úteis (title/H1/URL quando apropriado), não forçar repetição em todos os H2, alt e conclusão.
5. **H1:** verificar o documento renderizado; não penalizar só porque o conteúdo bruto do WordPress não contém o H1 que o tema adiciona pelo título.
6. **Links:** avaliar pertinência, texto âncora, confiabilidade e relação com o tópico; não exigir quotas fixas de links internos/externos.
7. **Alt text:** descrever a imagem para quem não a vê; não inserir keyword sem necessidade. Imagens decorativas podem ter alt vazio de forma correta.
8. **Schema:** validar JSON-LD, tipo adequado e propriedades aplicáveis. A simples existência de \`<script type="application/ld+json">\` não prova validade. Não adicionar FAQ/HowTo/Review/Product markup sem conteúdo real e requisitos específicos.
9. **FAQ:** só criar quando houver perguntas genuínas da audiência. Não exigir FAQPage nem prometer rich results.
10. **E-E-A-T:** avaliar sinais reais de experiência, expertise, autoria, fonte e responsabilidade editorial; não exigir LinkedIn como única prova.
11. **Core Web Vitals:** separar LCP, INP e CLS de campo do score Lighthouse/PageSpeed. Não chamar um score PSI isolado de Core Web Vitals.
12. **Freshness:** avaliar se fatos, preços, leis, pessoas, softwares, estatísticas e orientações ainda estão atuais; data de modificação sem revisão real não recebe pontos.
13. **ToC/listas/tabelas:** adicionar quando melhorarem navegação ou compreensão; não exigir estruturas sem função.
14. **YMYL:** exigir evidência e revisão apropriada ao risco do tema, sem forjar selo, revisor, credencial ou schema.
15. **GEO/RAG:** clareza de entidades, definições, fontes e respostas ajuda a leitura/extratividade; não pontuar marcações artificiais como “O termo é...” em negrito.

## Camadas técnicas e editoriais

- **Camada de página:** robots/noindex, status HTTP, canonical, sitemap, hreflang quando relevante, rendering, mobile, CWV e segurança. Auditar separadamente do texto.
- **Camada de post:** title, description, slug, headings renderizados, linkagem, mídia, schema, autoria.
- **Camada editorial:** intenção, cobertura, originalidade, valor, fontes, factualidade, clareza, atualidade.
- **Camada de distribuição:** Open Graph/Twitter Cards, imagem social, URL, CTA e adequação do formato.
- **Camada de métricas:** GSC/GA4 após publicação; métricas são observações posteriores, não pontuação pré-publicação.

## Avaliação de Web Stories e formatos derivados

Não usar o SEO score do artigo como se fosse score de Story ou vídeo. Criar score específico por formato:
- Web Story: validade técnica e metadados; narrativa slide a slide; precisão e proveniência; composição/legibilidade; acessibilidade/safe zones; publisher/branding verificados; link/CTA pertinente.
- Vídeo: clareza de ideia e hook; progressão/payoff; precisão; narrativa e ritmo; qualidade de imagem; voz/áudio; legendas; safe zones; direitos de imagem, música e fontes.
- Carrossel: progressão; uma ideia por slide; precisão; legibilidade; continuidade visual; utilidade; fechamento/CTA.
- Post estático: foco único; clareza imediata; hierarquia visual; legibilidade mobile; claim rastreável; legenda/CTA coerentes.

## Migração dos engines existentes

Na revisão de \`dashboard/src/lib/seo-score-engine.ts\`:
- Manter detecção de tipo de conteúdo como ponto de partida, mas validar manualmente categorias ambíguas.
- Remover densidade fixa e thresholds universais de tamanho como alvos de score.
- Corrigir extração de links para não contar \`mailto:\`, \`tel:\`, \`javascript:\` e fragmentos como links internos.
- Não usar URL editável do autor como atalho de validação de identidade/credenciais.
- Validar schema parseável, tipo e propriedades, preferencialmente com validador compatível.
- Analisar dados de Core Web Vitals separados de PSI/Lighthouse score.
- Evitar pontuar FAQ, TOC, tabelas, blockquote ou negrito só pela presença.
- Não inferir freshness apenas de \`post.modified\`.
- Incluir target editorial do briefing e avaliação de cobertura/informação original.
- Tratar valores não fornecidos como unknown; nunca atribuir zero ou pontuação máxima por default.

No avaliador \`dashboard/src/lib/webstories-seo-score.ts\`:
- Corrigir keyword-title para usar a palavra-chave real em vez de score fixo 0.
- Remover a pontuação automática de publisher-name quando não há dado de entrada validado.
- Não presumir \`textToImageRatio = 0.5\` nem categoria alta/média sem análise; usar unknown.
- Validar de fato o total de páginas, dimensões, alt, poster, logo, metadados e implementação técnica.
- Tratar o alvo de 13 slides como requisito deste workflow, não como exigência universal de SEO.

A integração no dashboard deve manter os motores legados até a nova versão ser comparada com fixtures reais e testes. Não migrar/mesclar componentes nem alterar a interface sem testes e validação visual próprios.


## Auditoria dos motores existentes

Consultar `references/legacy-engine-review.md` para a análise concreta dos motores principal, client-cms e Web Stories no repositório dashboard. O documento é um plano de migração, não uma alteração de código; manter engines legados até fixtures, testes de regressão e validação visual aprovarem a nova implementação.
