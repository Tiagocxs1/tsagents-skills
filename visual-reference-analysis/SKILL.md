---
name: visual-reference-analysis
description: Analisar imagem, screenshot, website ou arquivo Figma e extrair um sistema visual reutilizável, tokens, componentes e orientação de reconstrução.
---

# Visual Reference Analysis

Use quando o usuário fornece uma referência e deseja estudar, documentar, adaptar ou reconstruir sua linguagem visual. Esta skill é inspirada em práticas abertas de análise de design como AnyDesign; não copia automaticamente artes de terceiros.

## Fontes
- Imagem: analisar diretamente a composição, cores, tipografia, hierarquia, textura, recorte e proporção.
- Site: observar página real e, quando possível, HTML/CSS, variáveis e screenshot em desktop/mobile.
- Figma: usar contexto de design, variáveis, metadados e screenshot via Figma MCP.
- Conjunto de referências: separar o que é padrão recorrente do que é uma escolha isolada.

## Procedimento
1. Confirmar o objetivo: inspiração, auditoria, reprodução de sistema ou reconstrução de um componente.
2. Recolher evidência visual e técnica adequada à fonte.
3. Produzir uma leitura curta: público, intenção, personalidade, direção estética.
4. Extrair tokens: paleta, papéis de cor, famílias tipográficas, escala, espaçamento, radius, stroke, sombras e motion.
5. Inventariar componentes, padrões de layout, grid, alinhamento, densidade e estados.
6. Marcar cada conclusão como observada, inferida ou desconhecida; atribuir confiança alta/média/baixa.
7. Gerar design.md e design-tokens.json quando o usuário precisar de artefatos de implementação.
8. Usar a referência como aprendizado visual; não copiar logo, ilustração protegida, imagem proprietária ou composição distintiva sem autorização.
9. Para uma peça individual, extrair apenas o elemento relevante e explicar como reinterpretá-lo de forma original.

## Verificação
Comparar o resultado com a referência em uma viewport equivalente. Não tratar uma screenshot única como prova de comportamento responsivo. Conferir legibilidade, contraste e tokens no contexto real.

## Ferramentas
- Browser para páginas públicas.
- Figma MCP para arquivos e variáveis Figma; carregar figma-use antes de qualquer chamada use_figma.
- SVG/HTML/CSS para protótipos próprios.
- Consultar docs/visual-tool-registry.md para outras ferramentas.
