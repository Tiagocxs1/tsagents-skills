---
name: visual-quality-review
description: Revisão visual independente de artes, anúncios, posts, imagens, SVG, HTML/CSS, JSON, vetores, apresentações e motion antes da entrega.
---

# Visual Quality Review

Aplicar depois da primeira versão e antes da entrega. Atuar como diretor de arte e revisor técnico, procurando problemas concretos.

## 1. Abrir a saída real
- Inspecionar a renderização, screenshot, preview ou export final.
- Não aprovar apenas pela leitura do código ou por retorno de sucesso da ferramenta.
- Conferir versão e formato exatos da entrega.
- Em peças responsivas, testar o tamanho-alvo e uma viewport menor.
- Em carrosséis, revisar todos os slides, não apenas a capa.

## 2. Rubrica de 0 a 5
1. Conceito: relevância, originalidade e adequação ao objetivo.
2. Hierarquia: leitura natural entre mensagem principal, apoio e CTA.
3. Tipografia: escolha, escala, peso, entrelinha, quebra e legibilidade.
4. Composição: grid, alinhamento, margens, ritmo e espaço negativo.
5. Cor: contraste, paleta, função e consistência.
6. Imagem: resolução, recorte, luz, integridade e licença.
7. Marca: logo, cores, fontes e voz corretos.
8. Texto: grafia, nomes, números, URLs, preço, data e pontuação exatos.
9. Canal: proporção, safe zones, cortes e especificações.
10. Técnica: export, transparência, fontes, SVG, HTML, JSON e links.

Corrigir qualquer nota abaixo de 4 nos itens essenciais antes de entregar.

## 3. Bloqueadores
Não entregar sem corrigir:
- Texto cortado, ilegível, incorreto ou sobreposto.
- Logo deformado ou identidade incorreta.
- CTA ou informação principal coberta pela interface da plataforma.
- Contraste insuficiente em texto essencial.
- Elementos fora de margem ou sangria.
- Dados, depoimentos, selos ou promessas inventados.
- Export corrompido, dimensões erradas ou código que não renderiza.
- Slides com estilos inconsistentes sem intenção.

## 4. Crítica contra estética genérica
Perguntar:
- A arte tem uma ideia própria ou apenas efeitos da moda?
- Existe um elemento de assinatura?
- A composição tem ritmo ou tudo está centralizado e igual?
- A tipografia foi escolhida ou é padrão automático?
- O que pode ser removido para aumentar clareza?
- A peça conversa com a marca e o público?

## 5. Corrigir e validar
Registrar problemas, priorizar os de maior impacto, aplicar correções direcionadas, reabrir a renderização e revisar novamente. Não reconstruir tudo quando uma correção pontual resolver.

## 6. Parecer
Indicar aprovado ou precisa de ajustes, principais correções, o que foi realmente testado e limitações que permaneceram. Não usar elogios genéricos como evidência.


## 7. Teste social-first / anti-documento

Para posts únicos, Stories, capas e thumbnails, avaliar:
- Em thumbnail, o assunto e a headline são reconhecidos de imediato?
- Existe um único ponto focal dominante?
- A peça tem ritmo visual e uma assinatura própria, ou é apenas um template de cards, colunas e rodapé?
- Ela parece campanha/post social ou um documento/jornal/relatório comprimido em 9:16?
- A quantidade de texto é compatível com uma tela única? Conteúdo denso deveria estar na legenda ou em carrossel?
- A direção visual é própria da marca e da mensagem, sem copiar automaticamente o estilo de outro cliente?

Quando a intenção era impacto social e o resultado parecer documento, nota de conceito/composição não deve passar: refazer a direção de arte, não apenas trocar cores ou ampliar fontes.

## 8. Verificação real de imagens incorporadas

Para cada SVG/HTML com fotografia, logo ou ilustração:
- conferir a lista de assets esperados versus os encontrados;
- decodificar Base64/data URI e validar assinatura binária coerente com o MIME e dimensões plausíveis;
- detectar href/src vazios, undefined, URLs externas inesperadas e recursos que falham ao carregar;
- abrir o arquivo final em navegador e confirmar visualmente, item por item, que cada imagem está realmente visível e com enquadramento correto;
- verificar se clipPath, máscara, viewBox, dimensões e posicionamento não escondem ou deslocam a fotografia;
- inspecionar a exportação efetivamente entregue, não só outra prévia/cache anterior.

HTTP 200, Content-Type, XML válido ou uma tag de imagem presente não contam como prova visual. Se só a estrutura foi testada, declarar que a revisão visual não foi concluída.


## 9. Gate de direção fotográfica e imagem gerada

Quando houver fotografia, imagem gerada ou produto/ambiente realista, avaliar:
- O conceito tem uma ideia e um protagonista visual claros, além de simplesmente representar o tema?
- O ponto de vista, escala do plano, ângulo, perspectiva e distância focal escolhida (quando declarada) favorecem a cena ou geram distorções?
- O plano de foco e a profundidade de campo guiam o olhar sem apagar o contexto necessário?
- A iluminação tem direção e lógica? Luz principal, preenchimento, recorte, luz ambiente, contraste e temperatura são coerentes entre os objetos?
- Materiais, superfícies, pele, vidro, metal, madeira, água e reflexos parecem fisicamente plausíveis?
- Cor, sombras, highlights, saturação e atmosfera formam um tratamento tonal intencional?
- Efeitos como grain, bloom, haze, flare, glow ou vinheta são controlados e justificáveis, ou apenas decorativos?
- A interação entre pessoas e objetos é natural e anatomicamente/fisicamente coerente?
- Produtos, modelos, logotipos, interfaces e instalações respeitam as referências reais disponíveis?
- Em uma série, há variedade planejada de enquadramento, escala, ponto focal e composição, sem perder a unidade da marca?

Não aprovar descrições que dependam apenas de palavras como “cinematográfico”, “realista” ou “premium”. A revisão deve apontar escolhas visuais observáveis e problemas concretos. Não exigir lente, sensor ou esquema de luz específico quando a peça não depende disso.

## 10. Gate específico de tipografia publicitária

Para posts, anúncios e pôsteres, a nota de tipografia não pode passar apenas por legibilidade. Avaliar também desenho e direção de arte:
- A família display foi escolhida por personalidade ou é fallback de sistema/documento?
- A headline tem presença e uma silhueta própria?
- Cada quebra é intencional e semântica?
- As linhas equilibram peso, largura e ritmo sem uniformidade mecânica?
- A entrelinha foi ajustada pelas formas reais dos glifos, incluindo acentos e descendentes?
- Tracking e kerning são específicos para fonte, caixa e tamanho?
- Tipografia, fotografia e grafismos parecem uma composição única, não camadas independentes?
- O bloco funciona isolado, em thumbnail e integrado na arte?
- O arquivo exportado usa exatamente a mesma família e os mesmos pesos do preview?

**Bloqueadores:** headline com fonte genérica escolhida por conveniência; fonte substituída silenciosamente; texto deformado por compressão/estiramento; quebra automática sem revisão; linhas visivelmente desequilibradas; entrelinha que cola ou separa o bloco; acentos cortados.

Se qualquer bloqueador ocorrer, refazer o bloco tipográfico e recompor a peça antes da entrega.


## Gate obrigatório — contexto do cliente, território e protagonista em primeiro plano
Antes de selecionar imagens, consultar `client-contextual-visual-assets/SKILL.md`: estudar nicho, público, produtos/serviços, catálogo oficial e regiões atendidas; construir mapa de contexto visual; pesquisar assets locais com licença adequada; não usar fotografia estrangeira/genérica para representar campanha regional. Planejar protagonista real em foreground (produto autêntico, pessoa, objeto ou cena isolada em PNG/foto/3D) quando o conceito comportar. Definir background/midground/foreground e integrar perspectiva, escala, luz, foco, oclusão e sombras. Registrar proveniência e direitos. Reprovar wallpaper fotográfico + texto quando a narrativa exigir presença visual, produto falso, localidade errada ou asset sem permissão.
