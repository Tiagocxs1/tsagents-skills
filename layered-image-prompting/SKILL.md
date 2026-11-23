---
name: layered-image-prompting
description: Engenharia de prompts visuais para imagens com copy, direção tipográfica e profundidade em camadas. Use antes de gerar qualquer arte social, anúncio, capa, cartaz, thumbnail ou peça gráfica com texto.
---

# Layered Image Prompting — TS Digitais

Skill neutra de marca para transformar uma copy aprovada e uma direção visual em prompts prontos para modelos de imagem. Combina direção de arte, planos de profundidade, composição tipográfica, integração imagem-texto, camadas gráficas e revisão de saída.

## 1. Consultar as fontes corretas

Antes de escrever o prompt:

1. Ler o Brand Profile e os guias visuais da marca em brands/<slug>/.
2. Ler visual-design/SKILL.md, social-first-art-direction/SKILL.md e typography-master/SKILL.md quando a peça tiver texto.
3. Ler image-brief-and-routing/SKILL.md.
4. Para redes sociais, ler o módulo upstream upstream/social-media-skills/skills/image-prompt/SKILL.md e a referência references/prompt-anatomy.md. Para carrossel, complementar com carousel-writer/references/image-prompt-pack.md.
5. Chamar o perfil agents/image-prompt-art-director.md quando houver composição complexa, texto dentro da imagem ou conjunto de peças.

O Brand Profile é a fonte de verdade para cores, serviços, provas, logo e restrições. Não inventar fonte oficial, produto, equipamento, instalação, pessoa ou claim.

## 2. Escolher como a copy será aplicada

Definir um modo por peça:

### A. Native typography — texto renderizado pelo modelo
Usar quando o pedido é gerar a arte pronta, com texto dentro da própria imagem, e o modelo escolhido oferece boa aderência tipográfica.

- Incluir a copy exata, entre aspas, no próprio prompt.
- Especificar cada bloco textual e sua função: kicker, headline, apoio, body e CTA.
- Determinar posição, alinhamento, hierarquia, escala relativa, peso, largura de linha, entrelinha e tracking.
- Informar que cada trecho deve aparecer exatamente uma vez, no idioma original, com acentos e pontuação.
- Proibir qualquer texto adicional, pseudo-letras, marcas d'água ou logos inventados.
- Não reescrever, resumir nem completar a copy aprovada.

### B. Editable typography — texto aplicado fora do gerador
Usar quando a prioridade é precisão literal, editabilidade, corpo extenso, informação legal, dados ou CTA que não pode conter erro.

- O prompt descreve a imagem e reserva regiões adequadas para os blocos de texto.
- O prompt registra a copy exata e o mapa tipográfico como instrução de layout, mas deixa explícito que os textos serão adicionados depois.
- Aplicar cada bloco como objeto editável em SVG, HTML, Figma, Canva ou Adobe.
- Não deixar o modelo inventar letras falsas como textura.

### C. Hybrid
Usar quando a headline faz parte do conceito visual, mas o apoio, detalhes, preço, telefone, CTA ou texto longo precisam ser editáveis. Dizer claramente ao modelo o que deve ser renderizado e o que deve permanecer como área reservada.

**Regra quando o usuário pede “prompt já com a copy”:** incluir sempre a copy integral no prompt. Não omitir o texto só porque a renderização final poderá ser feita em SVG. Indicar quais trechos o modelo deve desenhar e quais ficam como overlay editável.

## 3. Planejar profundidade da cena

Separar profundidade fotográfica de camadas gráficas. Não confundir planos de espaço com z-index de layout.

### Foreground — primeiro plano
Elementos próximos à câmera que podem emoldurar, conduzir o olhar ou criar escala. Especificar:
- objeto e posição no quadro;
- quanto ocupa da imagem;
- nitidez, desfoque, crop e relação com o assunto;
- se sobrepõe ou não ao sujeito principal.

Usar apenas quando acrescentar profundidade ou narrativa. Um foreground discreto é melhor do que folhas, objetos ou brilhos aleatórios. Nunca bloquear o rosto, o produto, o ponto focal ou a área de leitura.

### Midground — plano principal
É o plano de ação e foco. Definir:
- sujeito/objeto principal e ação;
- posição e escala relativa;
- orientação, pose, silhueta e interação com o ambiente;
- plano de foco e luz principal.

O midground deve carregar a informação visual que torna a imagem relevante para a mensagem.

### Background — plano de fundo
Estabelece local, contexto, clima e escala. Definir:
- ambiente e detalhes que identificam o contexto;
- distância, perspectiva e nível de detalhe;
- luz ambiente, cor e atmosfera;
- região de baixo ruído que sustentará a tipografia.

O fundo deve apoiar o assunto, com menor contraste/detalhe quando houver copy sobreposta. Não torná-lo tão desfocado que perca o contexto.

### Relação entre os planos
Descrever distâncias, escala, sobreposição, linhas de perspectiva, oclusão, profundidade de campo e continuidade de iluminação. Usar perspectiva atmosférica quando adequada. Não exigir os três planos em toda imagem: um fundo limpo ou um close tipográfico pode funcionar melhor sem foreground.

## 4. Composição e hierarquia

Antes do prompt final, decidir:

- Formato e proporção exatos do destino (feed 4:5, Stories 9:16, quadrado etc.).
- Ponto focal dominante e direção de leitura.
- Ângulo e altura de câmera; plano geral, médio, close ou detalhe.
- Distribuição de peso visual, assimetria, equilíbrio e espaço negativo.
- Área de texto e safe zones da plataforma; não colocar informação essencial nas bordas.
- Interação entre imagem e tipografia: texto pode ocupar espaço negativo, sobrepor parte da imagem ou entrar numa placa de contraste, desde que isso tenha intenção.
- Ritmo entre peças de uma série: manter paleta, contraste e tratamento coerentes, mas variar enquadramentos e composições.

Não criar uma grade de cards, molduras, badges, gradientes ou glassmorphism apenas para cumprir um checklist. Uma técnica só entra quando sustenta a mensagem.

## 5. Direção tipográfica

Para cada bloco, documentar:

| Papel | O que especificar |
|---|---|
| Kicker/eyebrow | Pequeno, função contextual, caixa e tracking |
| Headline | Família de display, peso, escala, largura, alinhamento, quebras de linha e leading |
| Subheadline | Relação de tamanho com a headline, largura e espaçamento |
| Body | Família de apoio, corpo, largura de coluna, leading, contraste e número de linhas |
| CTA | Peso, cor, contraste, formato e distância dos outros elementos |
| Logo/assinatura | Área reservada para inserir o arquivo oficial; não pedir ao modelo para redesenhar |

### Regras
- Usar no máximo duas famílias tipográficas por peça, salvo justificativa.
- Se a fonte oficial não estiver no Brand Profile, definir somente uma categoria tipográfica (ex.: grotesca condensada, sans geométrica, serif editorial) e marcar a escolha como direção provisória.
- Especificar peso e personalidade, não apenas “fonte bonita”.
- Desenhar quebras de linha intencionais; não permitir quebra automática arbitrária.
- Descrever contraste, tracking, leading e largura de bloco conforme o papel do texto.
- Não usar stretching horizontal/vertical de glifos.
- Não fazer o texto competir com a ação principal ou com o rosto/produto.
- Não aplicar gradiente em toda headline por padrão; contraste simples costuma ser mais legível.
- Não diminuir a tipografia para forçar conteúdo demais em um slide. Encurtar a copy somente com autorização ou dividir a informação em mais telas.

## 6. Camadas gráficas e ordem de composição

Quando a imagem precisar ser uma arte completa, explicitar a relação das camadas gráficas, além dos planos fotográficos:

1. Base de cor/ambiente.
2. Background da cena.
3. Midground — assunto principal.
4. Foreground — moldura/objeto próximo, se usado.
5. Tratamento atmosférico, luz, sombra e textura, apenas se justificável.
6. Máscara, placa de contraste ou área de suporte tipográfico, se necessária.
7. Kicker, headline, apoio, body e CTA, em ordem de leitura.
8. Área reservada para logo oficial inserido manualmente.

O modelo pode renderizar essas camadas como uma única imagem. Se o usuário precisar de edição independente, entregar também a especificação para reconstruir a tipografia e os elementos gráficos em SVG/Figma/Canva.

## 7. Anatomia do prompt final

Usar os campos abaixo como plano de construção. O prompt final pode ser escrito como prosa natural ou blocos curtos, conforme o gerador:

- Purpose & format: finalidade, canal, proporção e área segura.
- Visual concept: conceito visual em uma frase.
- Camera & framing: ângulo, distância, lente aproximada e enquadramento.
- Foreground: elemento próximo, posição, foco e função; ou “sem foreground deliberado”.
- Midground: sujeito principal, ação, posição, escala e foco.
- Background: ambiente, profundidade, luz ambiente e espaço negativo.
- Lighting & palette: direção da luz, contraste, cores oficiais e restrições.
- Typography: família/categoria, peso, hierarquia, escala, alinhamento, leading, tracking, quebras e posicionamento.
- Exact copy: cada bloco literal entre aspas, com instrução “render exactly, once”.
- Graphic layers: overlays, shapes, masks e logo placeholder.
- Constraints: itens proibidos, claims, assets e marca.

Usar inglês para descrever a cena se isso ajudar o modelo escolhido, mas preservar a copy em seu idioma original, literalmente e entre aspas. Não traduzir frases da arte.

## 8. Pacotes de prompts

### Carrossel
- Entregar um prompt autossuficiente por slide.
- Todos os prompts do carrossel devem ficar em um único bloco de texto copiável, identificados por SLIDE 01, SLIDE 02 etc.
- Declarar no topo do bloco: gerar arquivos de imagem independentes; não criar colagem, grid, storyboard ou mosaico.
- Repetir as regras de estilo e marca necessárias em cada prompt, porque cada geração pode ocorrer sem o contexto anterior.
- Se uma imagem de referência for usada, explicar o que ela controla (estilo, cenário, personagem, material) e o que deve variar.
- Não repetir a mesma composição em todos os slides; preservar sistema visual, variar enquadramento e ritmo.

### Stories
- Um prompt completo por frame, normalmente 9:16.
- Reservar safe zones de interface.
- Incluir a copy exata do frame.
- Polls, quizzes, link stickers e outros stickers nativos devem ser identificados como elementos a inserir na plataforma, não falsificados dentro da imagem.

### Post único / anúncio
- Um prompt autossuficiente com copy, hierarquia, CTA e área do logo.
- Variar direção visual de acordo com a mensagem, não usar template automático.
- Confirmar preço, condições e claims antes de incluí-los.

## 9. Roteamento do gerador

- Verificar ferramentas já disponíveis e o registro docs/visual-tool-registry.md.
- Para texto dentro da imagem, preferir modelos com capacidade demonstrada de composição tipográfica e texto no idioma desejado; fazer teste pequeno antes de lote.
- O skill upstream image-prompt oferece o roteamento entre ferramentas text-first e image-first. Consultar suas instruções atuais em vez de assumir uma vencedora universal.
- mcp-image tem uma skill de prompt independente de seu servidor, mas o MCP de geração exige chave de API de um provedor externo. Não instalar nem chamar o servidor sem validar credenciais, preços, Node e custo do modelo.
- Midjourney MCPs de terceiros não devem ser usados como integração automatizada: verificar API oficial e termos do serviço antes de qualquer sugestão.

## 10. QA obrigatório do resultado

Após gerar:
1. Conferir cada palavra, acento, pontuação e repetição da copy.
2. Conferir tipografia, tamanho, hierarquia, contraste, alinhamento e quebras.
3. Conferir foreground, midground e background: profundidade coerente, foco e ausência de oclusões ruins.
4. Conferir que a imagem não inventou logo, equipamento, interface, uniforme, certificação ou dado.
5. Conferir formato, safe zones, cortes e legibilidade em tamanho real/mobile.
6. Se o texto estiver errado ou ilegível, não declarar aprovado. Corrigir com geração orientada ou reconstruir os blocos como texto vetorial/editável.
7. Para peças finais com texto comercial exato, preferir master editável em SVG/Figma/Canva mesmo que a geração inicial já traga a copy.

## 11. Multi-marca

Esta skill não contém paleta, fontes, serviços ou tom de uma marca específica. Sempre recebe esses dados de brands/<slug>/. Não transportar identidade, cenários ou equipamentos de um cliente para outro.

## Referências e proveniência

- upstream/social-media-skills/skills/image-prompt/ — MIT; briefing visual social, prompt anatomy, negative space e roteamento.
- upstream/social-media-skills/skills/carousel-writer/references/image-prompt-pack.md — MIT; prompts coordenados por slide e consistência de série.
- shinpr/mcp-image/skills/image-generation/SKILL.md — MIT; prompt natural em Subject/Context/Style, relações foreground/midground/background e texto literal. Adaptado para o fluxo TS; o servidor MCP externo não é requisito.
- Fei2-Labs/skill-genie/skills/image-prompt-engineer/SKILL.md — MIT; consultado como referência comparativa para estrutura, câmera e constraints; não copiado como skill canônica por seu foco em parâmetros específicos de Midjourney.
