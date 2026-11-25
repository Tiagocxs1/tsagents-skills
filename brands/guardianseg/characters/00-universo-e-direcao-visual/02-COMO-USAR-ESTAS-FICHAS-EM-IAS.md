# Como usar as fichas em ferramentas de IA

## 1. Arquivos que devem acompanhar cada geração

Sempre enviar:
1. `00-DIRECAO-VISUAL-MESTRE.md`;
2. a ficha individual do personagem escolhido;
3. a imagem de referência aprovada, quando já existir.

Não enviar todas as 51 fichas para uma geração simples. Use apenas o personagem necessário e, em cenas de grupo, as fichas dos participantes.

## 2. Primeira geração: prancha de identidade

Use o bloco **Prompt A — Prancha principal** da ficha. O objetivo é criar a referência visual oficial do personagem, não uma cena publicitária.

Verifique:
- silhueta e anatomia;
- vistas frontal, 3/4, perfil e traseira;
- consistência de cores e padrões;
- rosto, olhos, mãos/patas/nadadeiras;
- materialidade;
- detalhe surreal e acessório de identidade.

Peça correção antes de aprovar qualquer variação anatômica.

## 3. Segunda geração: expressões e poses

Depois de aprovar a prancha principal:
- anexe a imagem aprovada como referência;
- use o **Prompt B — Expressões e poses**;
- mantenha o mesmo modelo, proporções, cores, materiais, acessórios e assimetrias;
- peça apenas mudanças de expressão, postura ou ação.

Não tente obter identidade estável apenas repetindo o nome do personagem.

## 4. Imagens narrativas

Somente depois da identidade aprovada, criar:
- cenas individuais;
- interação entre personagens;
- situações em condomínio;
- histórias educativas;
- cenas de cultura local;
- peças sociais e vídeos.

A cada nova cena, preservar a identidade com a imagem aprovada como referência. Criar variações de câmera, cenário e composição sem redesenhar o personagem.

## 5. Texto, marca e equipamentos

- Não pedir ao modelo que invente o logotipo Guardian. Inserir o arquivo oficial separadamente.
- Não inventar uniforme, equipamento, central, tela, sensor, câmera, instalação ou interface que possa ser confundida com operação real.
- Para uma campanha institucional com equipamento Intelbras, selecionar e conferir antes o modelo real no catálogo e validar o uso da imagem.
- Character sheets devem sair sem palavras, títulos, códigos, legendas, marcas d'água ou pseudo-letras. Acrescentar rótulos depois em um editor.

## 6. Prompt neutro e adaptação

Os prompts deste pacote definem conceito, anatomia, materialidade, composição e restrições. Eles não usam parâmetros específicos de gerador. Ao escolher uma IA, adaptar:
- modelo e versão;
- modo de referência/edição;
- proporção e resolução;
- seed e variações, se existirem;
- campo de negative prompt, somente quando suportado;
- quantidade de imagens por lote.

Não inventar parâmetros nem considerar uma interface como se fosse o próprio modelo. A documentação atual do destino escolhido é que determina a sintaxe.

## 7. Registro de versão

Para cada personagem, mantenha:
- código e nome;
- data da prancha aprovada;
- nome/modelo/versão da IA usada;
- parâmetros externos relevantes;
- imagem-mestra aprovada;
- mudanças intencionais;
- falhas observadas e correções.

Não sobrescreva a imagem-mestra quando uma geração nova for apenas uma variação exploratória.