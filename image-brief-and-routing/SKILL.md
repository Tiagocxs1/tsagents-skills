---
name: image-brief-and-routing
description: Criar briefings e prompts de imagem objetivos e escolher a ferramenta visual correta conforme finalidade, estilo, precisão, edição e custo.
---

# Image Brief and Routing

Usar quando a tarefa precisar de fotografia, ilustração, textura, imagem de produto, fundo ou asset gerado por IA. Consultar primeiro visual-design e brand-profile.

## Gate: imagem precisa ser gerada?
Antes de usar IA, avaliar se uma foto real do produto/local/equipe, screenshot, asset licenciado ou gráfico verdadeiro comunicaria melhor. Não fabricar a aparência de uma pessoa, negócio, local ou produto real. Preferir geração quando o elemento não existe, precisa de uma direção visual específica ou uma série consistente não pode ser obtida por assets existentes.

## Brief de imagem
Definir em linguagem natural:
- Função: hero, produto, lifestyle, fundo, ilustração, thumbnail, ad, ícone ou textura.
- Assunto e ação principal.
- Conceito visual/metáfora, assunto focal, ação e ponto de vista.
- Composição, escala, enquadramento, altura/ângulo de câmera, perspectiva, foco, profundidade e espaço negativo.
- Linguagem óptica: distância focal aproximada e profundidade de campo quando mudarem a perspectiva ou a narrativa.
- Desenho de luz: direção, fonte, qualidade, contraste, temperatura, preenchimento, recorte e reflexos, conforme a cena.
- Materiais e microtexturas específicas, com comportamento físico plausível.
- Paleta e tratamento tonal: sombras, highlights, saturação, relação quente/frio e efeitos opcionais.
- Estilo, clima, acabamento e elemento visual distintivo.
- Proporção/resolução e destino.
- Restrições: definir se a imagem deve conter texto ou permanecer sem texto conforme o modo escolhido; não inventar logos, marcas d'água, deformações, produtos, interfaces ou outros elementos não desejados.
- Referências fornecidas e o que cada uma controla.

Evitar prompts recheados de tokens como masterpiece/8k ou listas de câmera sem função. Descrever escolhas visuais que controlem concretamente o resultado: ponto de vista, plano, perspectiva, foco, iluminação, materialidade, cor e acabamento conforme a finalidade.

Para séries, carrosséis e campanhas, definir uma matriz visual por peça: papel narrativo, assunto focal, enquadramento, composição, luz/cor e variação em relação às outras peças. A unidade vem da direção comum e da marca; não de repetir a mesma estrutura de layout. Quando houver referências, indicar exatamente quais atributos devem ser aproveitados e quais devem permanecer diferentes.

Consultar `layered-image-prompting/SKILL.md` como padrão universal de engenharia do prompt. Especificar apenas parâmetros relevantes: não forçar lente, sensor, efeitos, foreground ou grafismos em toda imagem.

## Destino do prompt — obrigatório

Identificar a combinação exata de **plataforma/interface + modelo/versão + modo de uso** antes de escrever o prompt final. Não tratar o nome da plataforma como se fosse sempre o nome do modelo — por exemplo, uma interface pode disponibilizar motores diferentes.

Se o usuário indicar mais de um destino, criar uma versão independente e realmente adaptada para cada um. A mesma cena, direção, copy e identidade devem ser preservadas, mas a estrutura, o idioma das instruções, o nível de detalhe e os controles podem mudar. Não copiar o mesmo prompt e apenas trocar o título.

Se o destino não estiver informado:
1. Reaproveitar o modelo/plataforma que o usuário já estabeleceu no contexto.
2. Se não houver destino claro e isso alterar a forma do prompt, perguntar objetivamente qual modelo/plataforma será usado.
3. Não criar versões para dezenas de ferramentas por padrão e não apresentar briefing neutro como prompt otimizado.

Para cada destino, conferir documentação oficial atual e adaptar:
- gramática, ordem, extensão e linguagem de prompt;
- geração, edição, referência visual, variações e consistência;
- capacidade de renderizar texto no idioma exigido;
- aspect ratio, tamanho, quantidade/batch, seed e demais parâmetros disponíveis;
- existência e sintaxe de campo negative prompt;
- quais ajustes pertencem à interface/API e não ao texto do prompt.

Nunca inventar parâmetros ou capacidades. Se o modelo não suportar texto longo fiel, recomendar tipografia híbrida/editável. Em carrosséis, cada plataforma/modelo recebe seu próprio bloco copiável, contendo os prompts independentes de todos os slides.

Consultar `layered-image-prompting/SKILL.md` como padrão universal de direção e adaptação.

## Roteamento
- Texto tipográfico dentro da imagem: só usar modelo comprovadamente confiável para texto curto; revisar cada caractere. Caso contrário, gerar o fundo/arte e compor texto separadamente.
- Fotografia realista de produto: escolher modelo com controle de referência e luz.
- Ilustração/arte editorial: escolher modelo por linguagem, não pelo nome de marca.
- Edição localizada: escolher ferramenta que preserve pixels não afetados.
- SVG/vetor: preferir Figma/SVG/gerador vetorial e validar edição; não converter bitmap em vetor quando a fidelidade não for suficiente.
- Vídeo: usar um fluxo de vídeo próprio, com storyboard e continuidade.

## Custo e privacidade
Consultar docs/visual-tool-registry.md; verificar créditos, modelo, limite e política de retenção antes da execução. Não assumir que uma API ou plano é gratuito. Usar apenas referência que o usuário tem direito de usar.

## Pós-geração
Conferir assunto, composição, marca, texto, anatomia, detalhes, consistência entre variações, proporção e safe zones. Registrar disclosure de IA quando aplicável e aplicar visual-quality-review.
