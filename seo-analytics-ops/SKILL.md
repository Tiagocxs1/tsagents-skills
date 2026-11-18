---
name: seo-analytics-ops
description: Planejar e executar auditorias de SEO técnico, conteúdo, GEO/AEO e análise de desempenho usando dados verificáveis do Google Search Console e GA4, ferramentas open-source e revisão humana. Use quando investigar tráfego orgânico, quedas de cliques/impressões, indexação, páginas, consultas, Core Web Vitals, conteúdo ou prontidão para busca por IA.
---

# SEO & Analytics Operations

## Objetivo

Produzir diagnósticos reproduzíveis e planos de ação para sites, separando:
1. evidência observada;
2. hipótese explicativa;
3. recomendação;
4. validação posterior.

Nunca inventar métricas, causas de queda, indexação, posições, conversões ou resultados.

## Fontes e ferramentas

Consultar [docs/SEO-ANALYTICS-STACK.md](../docs/SEO-ANALYTICS-STACK.md) para instalação, compatibilidade e estado dos projetos.

- **GA4:** priorizar o MCP oficial [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp), já listado como submódulo upstream em `upstream/google-analytics-mcp`. Modo padrão read-only. Não habilitar ferramentas de escrita.
- **GSC:** MCP comunitário [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc), MIT. Começar com OAuth read-only ou service account de menor privilégio. Manter `GSC_ALLOW_DESTRUCTIVE=false`.
- **Auditoria técnica determinística:** [SEOmator](https://github.com/seo-skills/seo-audit-skill), MIT, CLI local. O README atual anuncia 373 regras em 20 categorias; esse total pode mudar entre releases. Não tratar score agregado como ranking do Google.
- **Auditoria de página por skill:** [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill), MIT. Arquitetura script + LLM; a auditoria completa pode exigir PageSpeed Insights API key.
- **Orquestração SEO/GEO:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo), MIT. O upstream publica várias skills e subagents. Consultar apenas os módulos necessários e preservar autoria/licença; não copiar a coleção inteira para esta skill.

## Fluxo de auditoria

### 1. Delimitar escopo
- Confirmar domínio, propriedade GA4/GSC, período e fuso horário.
- Distinguir domínio raiz, prefixo URL e propriedades separadas.
- Identificar se a tarefa é diagnóstico de queda, auditoria técnica, conteúdo, conversão ou GEO.
- Registrar data da extração e atraso de processamento das fontes.
- Não presumir que uma URL está indexada porque responde HTTP 200.

### 2. Capturar evidências
- GSC: cliques, impressões, CTR, posição média, consultas, páginas, país, dispositivo e aparência de pesquisa quando aplicável.
- Comparar períodos equivalentes, com mesma duração e dias da semana sempre que possível.
- GA4: sessões/usuários orgânicos, landing pages, eventos e conversões; explicitar a definição de canal e atribuição utilizada.
- SEOmator ou auditor equivalente: HTTP, robots, sitemap, canonical, metadados, headings, links, imagens, dados estruturados, segurança e desempenho.
- PageSpeed/Lighthouse: separar dados de laboratório e de campo (CrUX), mobile e desktop.
- Guardar CSV/JSON/HTML exportado em diretório de trabalho apropriado, nunca no Git se contiver dados de conta ou visitantes.

### 3. Diagnosticar sem confundir correlação e causa
- Queda de impressões pode indicar demanda, cobertura/indexação, sazonalidade, concorrência ou alteração de SERP.
- Queda de cliques com impressões estáveis pode indicar CTR, snippet, posição, SERP features ou mudança de intenção.
- Queda de sessões no GA4 sem queda correspondente no GSC pode envolver consentimento, tags, atribuição, redirecionamentos ou eventos.
- Mudança de posição média é agregada e pode variar com mix de consultas, país, dispositivo e URL.
- Não declarar penalidade, atualização algorítmica ou desindexação sem evidência direta.

### 4. Priorizar correções
Classificar cada achado por:
- impacto provável (alto/médio/baixo);
- confiança da evidência (alta/média/baixa);
- esforço (baixo/médio/alto);
- risco de regressão;
- dependências.

Priorizar problemas que impedem rastreamento/indexação, erros HTTP/canonical, conteúdo duplicado ou páginas sem valor, falhas de mobile/performance e lacunas de intenção de busca. Não recomendar alterações em massa de URLs, redirects, robots ou sitemaps sem plano de rollback.

### 5. GEO/AEO e qualidade editorial
- Avaliar clareza de entidade, autoria, data, fontes primárias, citações, definições, estrutura e respostas completas.
- Usar schema apenas quando refletir conteúdo visível e elegível; dados estruturados não garantem rich results.
- Não produzir páginas artificiais apenas para preencher contagem de palavras.
- Não prometer citações por LLMs, rankings, tráfego ou aprovação AdSense.
- Evitar `llms.txt` como requisito de ranking; tratá-lo como experimento/documentação opcional, não fator comprovado.

### 6. Entregar relatório
Estrutura mínima:
1. Resumo executivo e período analisado.
2. Dados coletados e limitações.
3. Achados com evidência (métrica, URL, consulta, status, screenshot ou trecho).
4. Hipóteses, separadas dos fatos.
5. Ações priorizadas com impacto/confiança/esforço.
6. Plano de implementação e rollback.
7. Métricas e prazo para reavaliar.

## Guardrails

- Consultar `privacy-by-design/SKILL.md` e `agents/mcp-privacy-auditor.md` antes de conectar ferramentas a contas, analytics ou dados de visitantes.
- Nunca versionar tokens, JSON de service account, ADC, OAuth refresh tokens, exports identificáveis ou dados privados.
- Usar contas de serviço com acesso mínimo e preferir OAuth read-only.
- Não habilitar `GSC_ALLOW_DESTRUCTIVE=true`, `--allow-write` ou permissões de edição do GA4 para auditoria comum.
- Submeter ações de escrita (adicionar/remover propriedade, enviar/excluir sitemap, alterar configurações, publicar conteúdo ou redirecionar URLs) à confirmação explícita do usuário.
- Respeitar robots.txt, limites de taxa, termos de APIs e cotas gratuitas.
- Uma auditoria não substitui teste em navegador real, validação de Search Console nem revisão humana.

## Compatibilidade

A skill é um guia de orquestração independente de editor. MCPs só ficam disponíveis se instalados e autenticados no runtime do agente. Ter o código no GitHub não conecta GA4/GSC automaticamente.
