---
name: line-art-animation
description: Planejar ilustrações animadas em SVG e TypeScript com desenho de linha, personagens, movimento natural e cenas vetoriais responsivas.
---

# Line Art Animation

Use quando o pedido envolver ilustração vetorial animada, personagens caminhando, objetos em movimento, cenas com vento, água ou variação de iluminação. Não usar para toda arte estática.

## Linguagem visual
- Preferir traços de tinta com espessura consistente, curvas orgânicas e poucos detalhes bem escolhidos.
- Planejar silhueta, pose, peso e direção do movimento.
- Manter paleta reduzida e fundo que favoreça a leitura.
- Animar por partes com ritmo natural; evitar movimentos mecânicos ou tremores.
- Preservar viewBox, responsividade e nitidez em diferentes escalas.

## Implementação
- Usar SVG editável e TypeScript quando a cena precisar de interação ou ciclos de movimento.
- Separar primitivas de desenho, solver de movimento e estado da cena.
- Verificar frame a frame quando gerar vídeo ou ciclos.
- Respeitar prefers-reduced-motion para interfaces.
- Preferir código sem dependências quando suficiente.

## Referência de implementação
https://github.com/JDhruv14/line-art-animation

O projeto upstream é MIT e o README dos exemplos indica Node 22.18+. Instalar a skill upstream quando o runtime suportar; não copiar a biblioteca para o projeto sem necessidade. Para SVG estático, a skill visual-design é suficiente.
