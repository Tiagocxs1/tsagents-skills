---
name: visual-design
description: Direção de arte e produção de peças visuais profissionais. Consultar antes de criar qualquer arte estática, ilustração, post, anúncio, apresentação, ícone, SVG, HTML/CSS ou JSON de design.
---

# Visual Design — direção de arte e produção

Esta é a skill principal para qualquer trabalho visual. O objetivo é transformar um briefing em uma peça deliberada, memorável, legível, editável e apropriada ao canal.

## 1. Classificar o resultado

Identificar o tipo de saída antes de escolher a ferramenta:
- Arte estática: pôster, flyer, capa, banner, infográfico, material impresso ou thumbnail.
- Social: feed, story, reel cover, carrossel, pin ou post profissional.
- Publicidade: anúncio de performance, campanha, oferta, UGC ou variações A/B.
- Vetorial: símbolo, ilustração, ícone, diagrama ou SVG.
- Visual em código: banner HTML, landing visual, componente, gráfico, Canvas ou composição CSS/SVG.
- Motion: vídeo curto, animação, lettering, vinheta ou sequência.
- Interface: site, dashboard, produto web/mobile ou componente interativo.

Um post não é um dashboard; um SVG não é uma fotografia; um anúncio de conversão não é apenas uma imagem bonita. Cada categoria exige um processo próprio.

## 2. Extrair o briefing

Usar o contexto disponível e identificar:
- Objetivo: informar, vender, gerar contato, captar lead, construir marca ou educar.
- Público e contexto de consumo.
- Marca, produto, serviço, oferta e provas verificáveis.
- Canal, placement, dimensões, proporção e destino final.
- Texto obrigatório, texto que pode ser criado e CTA.
- Materiais: logo, fotos, paleta, fontes, referências e versões anteriores.
- Restrições: legais, acessibilidade, impressão, orçamento e ferramentas.

Não criar um questionário longo. Inferir o que já estiver claro. Fazer no máximo uma pergunta quando a falta de informação mudar materialmente o resultado.

## 3. Definir direção de arte antes de executar

Planejar:
1. Conceito visual em uma frase.
2. Primeiro ponto de atenção e hierarquia entre headline, apoio e CTA.
3. Composição, grid, alinhamentos, equilíbrio, ritmo e espaço negativo.
4. Tipografia: personalidade, escala, pesos, espaçamento e quantidade de famílias.
5. Paleta: função das cores, contraste e vínculo com a marca.
6. Imagem: fotografia, ilustração, vetor, textura, recorte, luz e tratamento.
7. Um elemento distintivo memorável, em vez de vários enfeites.
8. Se houver imagem fotográfica ou gerada, direção de fotografia coerente com o conceito: ponto de vista, enquadramento, perspectiva, foco/profundidade, iluminação, materialidade, cor e acabamento.
9. Em campanhas/séries, sistema visual comum com variação deliberada de cena, escala, recorte, composição e ritmo por peça.

Selecionar uma linguagem adequada: editorial, tipográfica, geométrica, fotográfica, minimalista, brutalista, premium, retrô, lúdica ou outra que faça sentido. Não usar sempre a mesma estética.

### Direção de imagem e acabamento fotográfico

Quando a imagem for protagonista, não aceitar apenas uma descrição do assunto. Consultar `layered-image-prompting/SKILL.md` e definir os controles que realmente importam:
- câmera/ponto de vista, escala do plano, ângulo, perspectiva e foco;
- luz principal, preenchimento/recorte, fontes do ambiente, contraste e temperatura;
- comportamento realista de materiais, superfícies, pele e reflexos;
- tratamento de cor, distribuição de sombras/highlights e efeitos com intensidade controlada;
- integração da fotografia com tipografia e grafismos, quando a peça contiver texto.

Não preencher o prompt com jargão técnico irrelevante, valores aleatórios de lente ou efeitos da moda. Parâmetros devem resolver problemas reais de composição, realismo ou narrativa.

## 4. Padrões de acabamento

- Criar uma hierarquia visual evidente. Nem tudo deve ter o mesmo peso.
- Usar grid, alinhamentos ópticos, margens consistentes e espaçamento intencional.
- Tratar o espaço negativo como parte da composição.
- Preferir imagens próprias, fornecidas ou com licença adequada.
- Não distorcer logos, não trocar suas cores sem autorização e preservar a área de proteção.
- Evitar clichês visuais e efeitos decorativos sem função.
- Cuidar de quebras de linha, largura, entrelinha, kerning, peso e contraste.
- Em campanhas, manter unidade visual sem repetir exatamente a mesma composição em todas as peças.

## 5. Escolher o fluxo

Consultar docs/visual-tool-registry.md:
- Canva ou Adobe Express: composição de peças editáveis, templates, texto, imagens e redimensionamento.
- Figma: vetores editáveis, ilustrações por camadas, sistemas visuais e peças que exigem precisão.
- SVG/HTML/CSS/Canvas: controle preciso, automatização, banners e composições sob medida.
- Superdesign: exploração de direções e moodboards quando a CLI estiver realmente disponível.
- Comfy Cloud, fal.ai, Adobe ou ElevenLabs: geração/edição de mídia quando a tarefa exigir e o custo estiver claro.
- MagicPath: interfaces, páginas e componentes web/mobile; não escolher automaticamente para um flyer.
- Cloudinary: biblioteca, busca e transformação de assets, não direção de arte.

Usar geradores de imagem para fotografia, textura ou ilustração base. Para textos precisos, construir tipografia em ferramenta de layout ou em camadas separadas de SVG/HTML/Figma.

## 6. Regras para arte feita com código

### SVG
- Definir viewBox e proporções coerentes.
- Nomear e agrupar elementos para facilitar edição.
- Manter stroke-linecap, stroke-linejoin, espessuras e alinhamentos consistentes.
- Conferir legibilidade em tamanhos pequenos.
- Evitar excesso de filtros, sombras pesadas e coordenadas arbitrárias.
- Renderizar em navegador e validar o tamanho final.

### HTML/CSS/Canvas
- Compor especificamente para o formato de saída.
- Usar tokens, layout consistente e fontes com licença adequada.
- Conferir overflow, corte, carregamento das fontes e escalonamento.
- Abrir screenshot ou preview real antes de aprovar.
- Para impressão, conferir sangria, margens, resolução e perfil de cor com a gráfica.

### JSON de design ou prompts
- Separar dados, instruções de geração e conteúdo textual.
- Validar sintaxe, tipos, dimensões, cores e referências de assets.
- Manter texto exato em campos próprios quando necessário.
- Renderizar o resultado: JSON correto não garante arte correta.

## 7. Entrega

Informar o que foi criado, formato/proporção, ferramenta, arquivo editável e exports. Quando aplicável, entregar master e versões finais. Não afirmar que está pronto sem conferir a renderização.

## Escolha consciente entre asset real e imagem gerada

Antes de gerar uma imagem, consultar image-brief-and-routing/SKILL.md. Uma fotografia verdadeira, screenshot, imagem licenciada ou gráfico com dados reais pode ser melhor do que uma imagem criada por IA. A geração é uma opção quando cria um elemento inexistente ou uma série controlada, não a etapa automática de todo trabalho.

## 8. Social-first não é documento editorial

Quando a saída for um post social de impacto, projetar primeiro para interrupção do scroll e leitura em poucos segundos. Não assumir que uma composição em página, matéria, ficha, relatório ou dashboard serve como post apenas porque está em 9:16.

- Definir um ponto focal dominante e uma ideia principal por arte.
- Usar escala, contraste, recorte fotográfico, tipografia, camadas, assimetria e espaço negativo para criar ritmo quando isso servir ao conceito.
- Evitar como padrão fileiras de cartões iguais, pequenas biografias, colunas de catálogo, divisórias e rodapés informativos. São válidos quando o objetivo realmente for consulta/comparação, não como solução automática.
- Se há informação demais para uma tela, mover explicações para a legenda ou estruturar um carrossel; não reduzir a tipografia até perder impacto e legibilidade.
- A composição pode ser ousada, mas margens, alinhamentos ópticos, hierarquia e safe zones continuam rigorosos.
- A estética deve nascer da mensagem e da marca. Não transportar a mesma linguagem visual de uma empresa para outra.

Consultar também `social-first-art-direction/SKILL.md` para o processo completo e a revisão anti-template.

## 9. Prova visual de assets em SVG/HTML

Quando uma arte tiver fotografias, logotipos ou ilustrações incorporados:
- validar os bytes e a assinatura do arquivo, não apenas MIME/HTTP status;
- em SVG autocontido, conferir cada data URI, Base64 decodificável, MIME coerente e ausência de href/src vazios ou `undefined`;
- contabilizar os assets esperados e abrir/renderizar o arquivo final;
- verificar visualmente que cada imagem aparece, tem o recorte correto e não foi escondida por clipping, máscara ou coordenadas erradas.

A presença de uma tag `<image>` não prova que o retrato está aparecendo. Código válido não equivale a resultado visual aprovado.

## Gate obrigatório — contexto do cliente, território e protagonista em primeiro plano
Antes de selecionar imagens, consultar `client-contextual-visual-assets/SKILL.md`: estudar nicho, público, produtos/serviços, catálogo oficial e regiões atendidas; construir mapa de contexto visual; pesquisar assets locais com licença adequada; não usar fotografia estrangeira/genérica para representar campanha regional. Planejar protagonista real em foreground (produto autêntico, pessoa, objeto ou cena isolada em PNG/foto/3D) quando o conceito comportar. Definir background/midground/foreground e integrar perspectiva, escala, luz, foco, oclusão e sombras. Registrar proveniência e direitos. Reprovar wallpaper fotográfico + texto quando a narrativa exigir presença visual, produto falso, localidade errada ou asset sem permissão.
