---
name: social-first-art-direction
description: Direção de arte para posts sociais de qualquer marca. Evita aparência de documento/template, define conceito, hierarquia, composição, integração de imagens, validação mobile e entrega.
---

# Social-First Art Direction

Aplicar junto com visual-design/SKILL.md, social-media-creative/SKILL.md e visual-quality-review/SKILL.md sempre que o resultado for post único, Story, capa de Reel, thumbnail ou criativo social estático. É uma skill transversal: não contém paleta, tipografia ou estilo fixo de uma marca específica.

## 1. Distinguir post de documento

Antes de compor, decidir explicitamente qual é o objeto:
- **Post social de impacto:** precisa interromper o scroll, comunicar uma ideia em poucos segundos e funcionar sozinho no feed.
- **Infográfico/editorial:** organiza dados ou explicações que precisam de leitura mais demorada.
- **Carrossel:** distribui uma narrativa ou explicação em várias telas.
- **Documento/apresentação:** prioriza consulta, leitura contínua e organização de informação.

Não entregar uma página de jornal, relatório, slide, ficha biográfica ou mini-dashboard quando o usuário pediu um post de impacto. Se o conteúdo for denso demais para um único post, resumir sem distorcer ou recomendar carrossel; não espremer parágrafos em uma arte vertical.

## 2. Direção de arte antes do layout

Registrar internamente, em poucas linhas:
1. Objetivo e público.
2. Mensagem que deve ser entendida no primeiro olhar.
3. Emoção/energia principal.
4. Gancho/headline.
5. Um ponto focal dominante.
6. Conceito visual/metáfora.
7. Linguagem de composição.
8. Imagem/asset principal e como interage com a tipografia.
9. Hierarquia secundária, CTA e áreas seguras.
10. Identidade da marca e restrições.

Escolher uma linguagem deliberada para a mensagem e a marca: tipográfica, fotográfica, colagem, produto hero, poster, geométrica, minimalista, editorial, documental, lúdica, premium ou outra. Não usar sempre a mesma linguagem nem transformar a estética de uma marca em regra para outras.

## 3. Composição com energia social

- Criar um ponto de atenção reconhecível em thumbnail.
- Usar contraste de escala, pesos tipográficos, posição, recorte, camadas e espaço negativo para criar ritmo.
- Permitir assimetria, diagonais, sobreposição intencional, imagem sangrada/recortada, blocos de cor e tipografia expressiva quando servirem ao conceito.
- Usar uma fotografia ou elemento visual como protagonista quando a história depender dele; não reduzir todos os assets a miniaturas iguais.
- Variar escalas e posições em listas de pessoas, produtos ou ideias. Evitar transformar cada item em um cartão idêntico por padrão.
- Manter alinhamentos, margens, contraste e áreas seguras rigorosos mesmo em composições ousadas.
- A composição deve parecer feita para aquela mensagem, não preenchida por componentes pré-formatados.

## 4. Anti-template e anti-documento

São sinais de alerta — não proibições absolutas:
- título + subtítulo + fileira de cards + parágrafos + rodapé institucional;
- sete retratos em cartões idênticos;
- colunas pequenas e listas numeradas com aparência de catálogo;
- repetição de caixas, bordas, badges e divisórias sem função;
- todas as informações com a mesma escala e peso;
- muito texto explicativo no próprio post;
- fundo e grid de página editorial usados só por serem fáceis de programar.

Cards, grids e layouts editoriais são válidos quando o objetivo é comparar, consultar ou explicar conteúdo. Não são a escolha automática para um post de impacto.

## 5. Copy dimensionada para a tela

- Headline curta e específica; o essencial deve ser entendido sem legenda.
- Uma mensagem principal por peça. Apoio e CTA só entram quando acrescentam algo.
- No post único, preferir palavras/frases de impacto a biografias ou parágrafos.
- Mover contexto, referências, explicações e hashtags para legenda ou carrossel.
- Não remover qualificações importantes, alterar fatos nem inventar promessas para conseguir uma frase mais chamativa.
- Preservar literalmente textos aprovados, nomes, datas e números.

## 6. Marca sem engessar a criação

- Consultar brand-profile/SKILL.md, Brand Kit e peças aprovadas antes de desenhar.
- A marca define logo, paleta, fontes, voz, público, promessas permitidas e restrições.
- A direção de arte define como esses elementos se combinam naquela campanha; não repetir sempre o mesmo layout só para manter consistência.
- Logo oficial deve ser o arquivo original, sem redesenho, distorção, mudança de cor não autorizada ou aplicação ilegível.
- Se não existir identidade confirmada, declarar a direção como provisória; não inventar uma identidade oficial.
- Estas regras são neutras de marca: nunca transportar automaticamente as cores, fontes ou estética de um cliente para outro.

## 7. Imagens, provas e direitos

- Priorizar fotos reais fornecidas pela marca, arquivos oficiais ou assets cuja licença permita o uso pretendido.
- Verificar a permissão separadamente do download. Licença NC não serve para comunicação comercial; atribuição não substitui permissão; domínio público deve ser verificado no território relevante.
- Se um retrato ou imagem não estiver autorizado, não usar só para preencher layout. Encontrar uma fonte com direitos adequados, usar um recurso tipográfico/ilustrativo claramente identificado ou pedir o asset ao cliente.
- Nunca gerar um rosto sintético para representar uma pessoa real identificável quando o pedido exigir fotografia/documento real.
- Não deixar placeholders ou áreas de imagem vazias na entrega final.

## 8. Implementação e QA de imagens

Para SVG/HTML:
- Se a peça precisa ser autocontida, incorporar cada fotografia/logo como data URI Base64; não depender de URL externa.
- Validar Base64 e assinatura binária real conforme o MIME (JPEG, PNG, WebP etc.). Content-Type e HTTP 200, isoladamente, não provam que o arquivo é uma imagem válida.
- Conferir quantidade esperada de imagens, href/src não vazio, inexistência de undefined, dimensões e decodificação.
- Para SVG autocontido, conferir que cada imagem esperada está presente no arquivo e que não sobraram referências externas.
- Renderizar o SVG final em navegador, no formato e na proporção de destino. Inspecionar visualmente cada foto: carregou, está visível, não está vazia, cortada incorretamente ou escondida por clipping/máscara.
- Validar a arte final baixável, não apenas uma prévia diferente ou uma versão anterior.
- Imagem estruturalmente presente não é imagem visualmente aprovada.

## 9. Revisão social

Revisar:
- em thumbnail: assunto e headline são percebidos imediatamente?
- em tela de telefone: headline, nomes essenciais e CTA são legíveis?
- a peça parece um post/campanha ou um documento?
- existe um único ponto focal claro?
- a fotografia principal tem presença e recorte intencional?
- há ritmo e contraste sem poluição?
- logo e textos respeitam safe zones da plataforma?
- todos os assets estão visíveis e licenciados para uso?
- a peça comunica sem depender da legenda?

Se parecer relatório/jornal/template genérico quando a intenção era scroll-stop, mudar a direção de arte — não apenas aumentar fonte ou trocar cor.

## 10. Definition of done

Só concluir quando:
1. o conceito e o formato correspondem ao briefing;
2. a composição é social-first, não um documento disfarçado;
3. texto, marca e fatos foram conferidos;
4. todos os assets passaram validação técnica e visual;
5. a peça final foi renderizada e inspecionada em tamanho de destino e viewport mobile;
6. limitações restantes foram declaradas.

Se a captura/renderização completa não estiver disponível, dizer exatamente o que foi validado e o que não foi; nunca chamar a peça de aprovada visualmente apenas porque o XML/SVG é válido.