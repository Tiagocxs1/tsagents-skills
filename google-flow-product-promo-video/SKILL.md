---
name: google-flow-product-promo-video
description: Planejar anúncios verticais de produto com Google Flow, referência visual exata, ritmo acelerado e kinetic typography. Usar quando a TS Flow Bridge preparar um vídeo de produto a partir do catálogo.
---

# Google Flow Product Promo Video

Skill especializada para criar um único vídeo publicitário curto de produto usando uma imagem real do catálogo como ingrediente no Google Flow.

## Objetivo

Transformar uma referência de produto em um vídeo vertical publicitário, próprio para Reels/Shorts/Stories, com produto fiel, cortes rápidos, movimentos de câmera, transições marcantes e textos cinéticos curtos.

O estilo pode ser descrito como product promo video, motion-graphics product ad e kinetic typography product showcase. Não é slideshow de fotos nem imagem estática.

## Ordem de prioridade

1. Fidelidade do produto: a imagem anexada é a fonte visual principal. Preservar modelo, carcaça, lente, proporções, acabamento, conexões, inscrições e detalhes visíveis. Não inventar peças, botões, lentes, displays ou acessórios.
2. Fatos confirmados: usar apenas nome, modelo e características presentes no brief ou em fonte oficial fornecida. Não inventar resolução, alcance IR, zoom, certificação, compatibilidade, preço, garantia, performance ou resultado.
3. Conceito publicitário: uma ideia clara, um gancho rápido, demonstração visual do produto e encerramento/CTA simples.
4. Legibilidade: texto curto em português brasileiro, com palavras exatas, poucas palavras por entrada e posição dentro das safe zones.
5. Movimento: cada movimento ou corte deve revelar o produto ou reforçar a mensagem; evitar efeitos aleatórios.

## Formato e execução

- Destino padrão: vídeo vertical 9:16.
- Duração padrão: 8 segundos quando a tarefa não especificar outra. Ajustar apenas quando o modelo de vídeo selecionado permitir e o custo estiver claro.
- Saída padrão: 1 vídeo, nunca múltiplas variações por padrão.
- O prompt de destino precisa dizer explicitamente: gerar vídeo, não imagem estática, não storyboard e não uma coleção de imagens.
- Especificar que a imagem do produto anexada ao campo de prompt é um ingredient/reference image e deve ser usada como identidade visual exata do equipamento.
- Não supor qual modelo está selecionado no Flow. O Flow precisa estar em um modelo de vídeo compatível com Ingredients/References to Video. Não escolher um modelo de imagem.
- Não trocar a referência por uma representação aproximada do equipamento.

## Direção de movimento

Planejar 3 a 5 batidas visuais dentro do mesmo clipe. Exemplo de estrutura, adaptar ao produto e ao conceito:

1. Hook (0–1 s): entrada imediata com macro detalhe, impacto tipográfico ou whip-in; mostrar o protagonista sem demora.
2. Reveal (1–3 s): movimento de câmera controlado — push-in, orbit, lateral tracking ou rack focus — mostrando o produto com proporções reais.
3. Detail (3–5 s): 1 ou 2 cortes rápidos para detalhes reais visíveis na referência. Não simular capacidades técnicas que não foram confirmadas.
4. Brand/message beat (5–7 s): revelar a mensagem principal em tipografia cinética; usar cor e contraste coerentes com a marca.
5. Close (último segundo): plano limpo do produto e CTA curto; deixar área segura para logotipo oficial se ele for aplicado posteriormente.

Movimentos possíveis: fast dolly-in, short orbit, whip-pan transition, tracking move, macro push-in, rack focus e speed ramp curto. Usar 2 a 4 transições no máximo; não empilhar glitch, blur, zoom e flare sem função. O produto deve continuar reconhecível em todos os cortes.

## Kinetic typography

- Copy original em português brasileiro.
- Usar 2 a 4 frases/entradas curtas; ideal de 1 a 4 palavras por entrada.
- Preferir reveal palavra a palavra, stagger, scale emphasis, mask reveal e cortes sincronizados à batida.
- Cada texto deve permanecer tempo suficiente para leitura em telefone; não piscar palavras tão rápido que fiquem ilegíveis.
- Preservar grafia, acentos, modelo e números literalmente.
- Não desenhar logotipo fictício, marca d'água, interface ou selo de certificação.
- Usar o esquema visual da marca quando conhecido; para Guardian: azul escuro, vermelho, branco e ciano apenas como acento; nunca usar verde.
- Não colocar headline, subtítulo ou CTA em áreas normalmente cobertas pelos controles do Instagram.

## Áudio

Quando o modelo suportar áudio, sugerir trilha instrumental eletrônica/percussiva sem voz, com impactos discretos, whooshes e acentos sincronizados aos cortes. Não especificar música comercial protegida nem atribuir artista/canção. O vídeo deve continuar compreensível sem áudio.

## Revisão da marca e claims

- Quando o cliente for Guardian, consultar brands/guardianseg/BRAND-PROFILE.md.
- Tom técnico, claro e confiável; sem medo, alarmismo ou promessas absolutas.
- Não usar verde na identidade Guardian.
- Não inserir estatísticas, certificações, depoimentos, clientes ou instalações sem fonte e autorização.
- Preferir CTA neutro como Conheça na Guardian ou Fale com a Guardian, conforme o briefing.
- Se o brief não contiver uma especificação técnica validada, não inventar texto técnico para preencher o vídeo.

## Contrato de saída para integração com TS Flow Bridge

Retornar exclusivamente JSON válido, sem Markdown, sem cercas de código e sem explicações fora do objeto:

{
  "flowPrompt": "Prompt completo, em inglês, direcionado ao Google Flow. Inclui instrução explícita de VIDEO, not a still image; usa o ingredient anexado como referência exata; define 9:16, uma única saída, duração; descreve beats, movimentos, cortes, textos literais em português, cores e áudio.",
  "aspectRatio": "9:16",
  "durationSeconds": 8,
  "outputCount": 1,
  "onScreenText": ["texto exato 1", "texto exato 2"],
  "verifiedProductFacts": ["somente fatos dados no brief ou em fonte oficial"],
  "omittedClaims": ["características comerciais/técnicas não confirmadas"]
}

Validar antes de retornar:
- flowPrompt tem comprimento suficiente para descrever o clipe e diz explicitamente que é vídeo, não imagem.
- aspectRatio é exatamente 9:16.
- outputCount é exatamente 1.
- durationSeconds é um número entre 5 e 15; usar 8 por padrão.
- onScreenText contém textos curtos em português brasileiro, sem erros de acentuação.
- Nenhuma especificação técnica foi inventada.