---
name: tsdigitais-anatomy
description: "Cria ilustrações técnicas isométricas ricas e explicativas como objetos físicos reais, com peças pequenas precisas, volume, profundidade, animação SVG e efeitos WebGL. Use para máquinas, instrumentos, mecanismos e equipamentos em diagramas/explainers."
---

# Anatomy — adaptação TS Digitais

## O princípio
O objeto é a explicação. Em vez de caixas, setas e rótulos, conceba uma máquina/instrumento que demonstre fisicamente o conceito. Use dezenas de peças sólidas, propósito mecânico, recortes, suportes, juntas, cabos, encaixes, ordem de profundidade e detalhes proporcionais.

## Melhor aplicação
- Ilustrações técnicas isométricas de alarmes, sensores, câmeras, painéis, motores, ferramentas, instrumentos, mecanismos e equipamentos.
- Diagramas explicativos para artigos, páginas de produto, apresentações, catálogos e materiais técnicos.
- Figuras interativas SVG com controles/readouts, movimentos mecânicos e efeitos WebGL como água, fogo, luz, caustics e vapor.
- Impressos técnicos A4/A3 derivados da figura, quando desejado.

## Fluxo de produção
1. Ler primeiro os exemplos mais próximos em upstream/anatomy/examples/ e estudar a composição, peças e lógica do modelo.
2. Ler upstream/anatomy/references/craft.md e references/kit.md antes de modelar; consultar references/motion.md para movimento, references/webgl.md para shaders, references/verify.md para QA, references/3d.md para modo 3D e references/print.md para PDF.
3. Selecionar o objeto metáfora adequado e decompor a montagem em peças com função, suportes, terminais, folgas e relações mecânicas.
4. Construir a geometria e projeção com o kit em upstream/anatomy/kit/. Usar materiais/sombreamento do kit e ordem de profundidade comprovável; não usar wireframes simples nem formas abstratas sem função.
5. Construir uma única página/figura autocontida. Usar SVG como base; incluir WebGL somente quando linhas/vetores não forem suficientes.
6. Rodar auditorias geométricas de interseções, terminais, folgas e ordem de profundidade; capturar screenshots/close-ups das áreas críticas em tema claro e escuro.
7. Verificar legibilidade em tamanho real, em mobile e com movimento reduzido. Corrigir até a figura parecer um objeto físico coerente.
8. Exportar SVG/HTML/React ou PDF conforme briefing. Publicação em galeria comunitária exige pedido explícito e revisão do conteúdo enviado.

## Modo 3D e limites
- O principal resultado é SVG procedural, não malha fotogramétrica nem renderizador PBR.
- Shaders usam WebGL; sem WebGL a figura deve continuar entendível em SVG.
- O modo de peças móveis 3D usa grupos rígidos e é beta, comprovado somente em exemplos/teste e não em figura de produção. Use apenas quando movimento de rotação/hinge em profundidade for a explicação; meça e audite.
- Não é uma biblioteca de charts, nem ferramenta para mapas exatos ou pessoas/rostos. Para personagens ou cenas fotorrealistas gerais, use Blender/Three.js e assets licenciados.
- Requisito upstream: Node.js >=20.10 e Chrome/Chromium para checagens. O host atualmente possui Node.js 18.19.1 no sistema; o comando node aponta para Bun, cuja compatibilidade não foi validada. Não afirmar que a build ou auditoria foi executada até rodar com runtime suportado.
- O modo 3D beta pode ser pesado; evitar cena com muitas partes em mobile sem orçamento de performance.

## QA obrigatório
- Build não basta: rodar auditoria geométrica e inspecionar screenshots.
- Nenhuma linha solta, tubo/cabo atravessando peça, junta flutuando ou cruzamento com profundidade incorreta.
- Cada detalhe precisa pertencer a uma peça. Volume, espessura, acabamento e sombras devem ajudar a compreensão.
- Testar os dois temas, os estados de animação e close-ups; registrar PASS/FAIL/INSUFFICIENT_EVIDENCE.
- Não inventar medições/números no readout: todos devem vir do mesmo modelo que move o desenho.

Fonte original, kit, scripts, exemplos e licença MIT: upstream/anatomy/. Esta adaptação é só roteamento TS Brain; consultar o material upstream completo antes de implementar.
