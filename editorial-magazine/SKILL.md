---
name: editorial-magazine
description: Planejar, dirigir e produzir revistas digitais, e-books editoriais, magazines e flipbooks com narrativa visual, grid consistente, tipografia hierárquica, copy dimensionada e revisão página a página. Use antes de qualquer código de layout.
---

# Editorial Magazine — Sistema de produção de revistas

## Missão

Produzir publicações digitais com qualidade editorial: conceito reconhecível, narrativa contínua, páginas visualmente ricas sem poluição, tipografia deliberada, margens consistentes e conteúdo completo. O produto é uma revista; o flipbook é apenas o meio de leitura.

Esta skill aplica-se a revistas, magazines, e-books diagramados, catálogos editoriais e flipbooks. Não confundir com apresentações em slides, páginas de venda ou interfaces em formato de cards.

## Regras obrigatórias antes de produzir

Ler nesta ordem:
1. `AGENTS.md` e `visual-design/SKILL.md`.
2. Esta skill `editorial-magazine/SKILL.md`.
3. `brand-profile` e a ficha em `brands/<marca>/BRAND-PROFILE.md`.
4. `design-driven-copywriter/SKILL.md` para textos que precisam caber numa composição.
5. `editorial-print-design/SKILL.md` somente quando a direção pedir linguagem de impressão, zine ou paleta limitada.
6. `visual-reference-analysis/SKILL.md` quando houver site, revista, screenshot ou referência para estudar.
7. `visual-quality-review/SKILL.md` antes da aprovação final.
8. Consultar `docs/visual-tool-registry.md` antes de escolher ferramentas.

Quando for Guardian Seg, usar `brands/guardianseg/BRAND-PROFILE.md` e `brands/guardianseg/SOCIAL-CONTENT-GUIDELINES.md`. O Brand Profile é a fonte de verdade da identidade, serviços, claims e restrições. Confirmar a atualidade de qualquer indicador antes de publicá-lo.

## 1. Brief editorial

Registar antes de desenhar:
- Objetivo editorial e ação esperada do leitor.
- Público principal e conhecimento prévio.
- Tema, ideia central e promessa editorial verificável.
- Conteúdo obrigatório, fontes, dados, nomes e claims.
- Quantidade estimada de páginas, idioma, formato e destino.
- Assets reais disponíveis, direitos de uso e autorizações.
- Restrições de marca, privacidade, acessibilidade e orçamento.

Não começar com CSS, HTML, componente de página ou gerador de imagens. Se faltar um detalhe que não altera materialmente a solução, inferir a partir do contexto e registrar. Não perguntar novamente o que já está documentado.

## 2. Conceito e direção de arte

O Creative Director / Editorial Art Director deve:
1. Observar o assunto e os assets concretos.
2. Formular uma proposição editorial em uma frase.
3. Criar até três direções realmente distintas quando o briefing estiver aberto. Mudar apenas a cor ou a fonte não constitui uma nova direção.
4. Definir linguagem fotográfica, paleta, tipografia, ritmo, estruturas de página e elemento visual de assinatura.
5. Escolher uma direção e justificar sua adequação ao público e ao conteúdo.
6. Registar decisões em `creative-direction.md` antes da produção.

Uma revista deve ter identidade sem repetir a mesma composição em todas as folhas. Não confundir impacto com excesso de elementos. Não aplicar estética maximalista, papel bege, halftone, colagem ou monocromia por padrão; cada escolha precisa servir ao conceito e à marca.

## 3. Arquitetura editorial e ritmo

Criar `sequence-plan.md` com uma linha por página:
- Número/ID e função editorial.
- Mensagem única que a página precisa deixar.
- Headline, subheadline, deck, body copy e callouts aprovados.
- Estrutura visual e ordem de leitura.
- Fotografia/ilustração/diagrama e origem/licença.
- Relação com a página anterior e seguinte.
- Densidade textual e área visual estimada.
- Folio, legenda, fonte ou CTA, quando necessários.

Planejar a sequência como narrativa, e não como uma coleção aleatória de páginas. Alternar, conforme o conteúdo, abertura, matéria, comparação, página fotográfica, infográfico, destaque, aplicação prática, respiro e fechamento. A intensidade deve ter ritmo; nem todas as páginas devem gritar e nem todas devem ser minimalistas.

Artes de capa, abertura, páginas centrais e encerramento precisam pertencer ao mesmo sistema visual. Criar relações entre páginas adjacentes, mas não exigir que toda dupla seja uma única imagem panorâmica.

## 4. Sistema de página e grid

### Formato-base

A4 vertical: 210 × 297 mm. O formato pode mudar por briefing, mas precisa ser definido antes da composição e permanecer consistente na publicação.

### Margens do padrão A4

Usar como base editorial:
- Superior: 14 mm.
- Inferior: 18 mm.
- Interna: 18 mm.
- Externa: 14 mm.

As margens interna e externa são espelhadas nas páginas pares e ímpares. Capa e contracapa podem ter composição própria, mas respeitam a área segura definida para a publicação.

### Grid

- Grid editorial de 12 colunas por página.
- Gutter inicial de 4 mm, calibrado para o formato e mantido como token.
- Alinhamentos verticais e horizontais ancorados no grid.
- Baseline/ritmo vertical consistente.
- Cabeçalhos, folios e rodapés posicionados em zonas fixas.
- Elementos que cruzam margens só podem fazê-lo por decisão de arte deliberada, nunca por acidente.
- Componentes de página devem respeitar as margens, não criar margens próprias concorrentes.

As medidas são um ponto de partida aprovado para o padrão A4. Registar qualquer exceção em `creative-direction.md`; não alterar margens isoladamente para fazer uma página caber.

## 5. Sistema tipográfico

Usar no máximo duas famílias tipográficas, com funções nomeadas. Preferir famílias com licença e cobertura dos caracteres usados. Não declarar fontes oficiais sem confirmação no Brand Profile.

Escala inicial para A4 digital:
- Headline principal: 30–38 pt.
- Subheadline: 18–22 pt.
- Deck/introdução: 14–18 pt.
- Body copy: 12–14 pt, com entrelinha 1,45–1,55.
- Legendas, notas, fontes, créditos, folios, labels e metadados: mínimo 12 pt.
- Regra vinculante TS Digitais: nenhum texto visível pode ficar abaixo de 12 pt na versão impressa ou 16 CSS px na leitura digital a 100%. Se não couber, reorganizar, simplificar sem perda de informação, redistribuir ou adicionar páginas; nunca reduzir abaixo do limite para encaixar.

Estabelecer pesos, estilos, entrelinha, tracking, alinhamento, largura de coluna e quebras antes de montar a publicação. Manter uma hierarquia clara: título é dominante, subtítulo explica, deck contextualiza, corpo desenvolve, legenda identifica.

Evitar:
- Títulos competindo entre si.
- Muitos pesos, caixas altas ou estilos na mesma página.
- Texto corrido justificado com espaços irregulares.
- Linhas excessivamente longas ou parágrafos sem respiro.
- Viúvas, órfãs e títulos isolados no rodapé.
- Saltos arbitrários de tamanho ou entrelinha entre páginas equivalentes.

## 6. Copy dimensionada para composição

O Design-Driven Copywriter trabalha em conjunto com o Editorial Art Director:
- Uma ideia principal por página.
- Kicker/eyebrow breve, se necessário.
- Headline específica e curta.
- Subheadline que acrescente informação, sem repetir o título.
- Deck de uma ou duas frases quando ajudar a orientar.
- Body copy em parágrafos curtos e progressivos.
- Pull quote apenas quando houver uma frase forte já sustentada pelo conteúdo.
- Caption ligada diretamente à imagem.
- CTA apenas quando houver ação pertinente.

Antes do layout final, determinar orçamento de palavras/linhas para cada zona. Redigir a copy para a função da página; não tentar encaixar um artigo inteiro em qualquer caixa.

Quando houver excesso de conteúdo, seguir esta ordem:
1. Remover repetição e redundância sem perder informação.
2. Reescrever com clareza e especificidade.
3. Redistribuir em colunas ou blocos de leitura, preservando a ordem.
4. Criar uma nova página ou desdobrar o tópico.
5. Só então ajustar microespaçamentos dentro dos tokens aprovados.

É proibido resolver excesso de texto com escala CSS arbitrária, transformações que encolham apenas conteúdo, fonte minúscula, line-height comprimida ou margens diferentes. Nunca cortar conteúdo silenciosamente. Preservar nomes, números, datas, URLs e claims aprovados literalmente.

Copy de resposta direta, gatilhos de urgência e fórmulas de página de vendas não devem comandar uma publicação educativa/institucional. Ativar copy-thief ou copy-engineering apenas quando a peça for realmente uma página/oferta de conversão.

## 7. Composição e linguagem visual

- Cada página tem um foco principal e uma hierarquia de apoios.
- Usar fotografias, diagramas, infográficos, tabelas editoriais, mapas ou ilustrações quando explicarem, provarem ou ampliarem a mensagem.
- Priorizar assets reais e autorizados. Geração por IA é complementar, nunca substituto automático.
- Não usar imagens com texto gerado quando a precisão textual importa.
- Manter texto nativo, selecionável, pesquisável e acessível em HTML/PDF sempre que possível.
- Criar contraste entre imagem e texto, alinhamentos intencionais, espaço negativo e variação de escala.
- Remover enfeites, cards repetidos, badges e ícones que não tenham função editorial.
- Não deixar páginas vazias ou pobres por falha de planejamento; uma página quieta é intencional e tem papel no ritmo.

## 8. Páginas-piloto antes da produção completa

Antes de estender o sistema, desenhar e rever um pequeno conjunto:
1. Capa.
2. Abertura de capítulo/matéria.
3. Página de leitura editorial com corpo de texto.
4. Página visual/infográfico.
5. Página prática ou de destaque/encerramento.

Validar essas páginas em escala real e como miniaturas. Corrigir o sistema — grid, escala, ritmo, componentes e direção de arte — antes de produzir as restantes. Não usar uma página-piloto aprovada como desculpa para não revisar as outras.

## 9. Separar conteúdo do motor de leitura

A publicação e o flipbook são camadas distintas:
- Conteúdo editorial: HTML/CSS ou PDF, com texto nativo e assets organizados.
- Motor: navegação, gesto de virar, zoom, pan, fullscreen e carregamento.
- Interface: toolbar, controles, progresso e comportamento responsivo.

Quando a plataforma escolhida for FlipHTML5, consultar também `fliphtml5/SKILL.md`. No plano Free, o livro é público, pode ser acessado pelo link direto, permite download do PDF original e não oferece senha/bloqueio de indexação. O iframe não herda a autenticação do site hospedeiro. Não usar Free para relatórios privados ou dados reais de clientes. Exportação HTML para hospedagem própria e API convencional não estão incluídas no Free; validar separadamente qualquer disponibilidade do MCP.
O FlipHTML5 converte o documento existente, não corrige composição editorial: resolver tipografia, proporções, fontes, margens e páginas no PDF/HTML de origem antes da conversão.

Não redesenhar uma revista como interface de cartões para adaptar a um motor. Não trocar bibliotecas antes de uma prova de conceito com páginas reais, acessibilidade, responsividade e desempenho. Para projetos React, avaliar StPageFlip como candidato MIT, comparando com o leitor existente. Nunca declarar equivalência a FlipHTML5 sem testar funcionalidades específicas.

## 10. Revisão visual obrigatória

Abrir a renderização final, não apenas o código ou o build. Revisar todas as páginas e todas as aberturas, não só a capa ou algumas amostras.

Viewports de referência para o leitor:
- Desktop: 1440 × 900 e 1366 × 768.
- Mobile: 390 × 844 e 360 × 800.
- Adicionar uma resolução compacta/tablet e testar também o dispositivo real disponível.

Revisar:
- Página inteira visível dentro do seu frame.
- Margens e grid consistentes, incluindo páginas espelhadas.
- Nenhum texto ou elemento fora da folha.
- Nenhuma sobreposição, corte, scroll interno ou conteúdo oculto.
- Hierarquia, fonte, peso, entrelinha, viúvas e quebras.
- Cor, contraste, recorte e resolução de imagem.
- Relação entre páginas vizinhas e ritmo de thumbnails.
- Capa, páginas interiores, formulário/CTA e contracapa.
- Texto fiel ao conteúdo aprovado.

O zoom do leitor deve ampliar a folha inteira, preservando o layout e as quebras de linha. Faixa prevista: 50%–200%. Em ampliações superiores a 100%, fornecer pan/arraste sem cortar o conteúdo nem aplicar zoom apenas ao texto.

Usar screenshots reais em 100% e no tamanho efetivo do leitor. Automatização ajuda a medir overflow, margens e dimensões, mas não substitui inspeção visual humana.

## 11. Gate de qualidade e entrega

Usar `visual-quality-review/SKILL.md` com rubrica de 0–5:
- Conceito e identidade editorial.
- Hierarquia.
- Tipografia.
- Grid/margens.
- Composição/ritmo/espaço negativo.
- Imagem e dados.
- Copy.
- Acessibilidade e leitura.
- Consistência da marca.
- Fidelidade e comportamento do leitor.

Cada critério essencial precisa de nota mínima 4/5. Bloqueadores têm tolerância zero: cortes, sobreposições, conteúdo ausente, fonte ilegível, margens acidentais, claim inventado, identidade incorreta ou screenshot não inspecionada. Nenhum texto visível pode ficar abaixo de 16 CSS px no leitor a 100% ou 12 pt na impressão.

Parecer deve listar: versão testada, páginas cobertas, viewports, screenshots, defeitos corrigidos, limitações e resultado. Build/deploy bem-sucedido não significa design aprovado.

## 12. Entregáveis por publicação

Guardar no projeto:
- `creative-direction.md` — conceito e regras visuais.
- `sequence-plan.md` — mapa página a página e copy aprovada.
- `design-tokens.css` ou equivalente — medidas, grid, tipografia, cores e espaçamento.
- `asset-manifest.md` — arquivo, origem, licença e autorização.
- `visual-review.md` — checklist, evidências e parecer.
- Screenshots de todas as páginas e viewports críticos.

O padrão aprovado deve ser reutilizado como base, sem impedir uma direção visual própria quando o conteúdo exigir.
