---
name: digital-eguide-editorial
description: Planeja e cria e-books, guias digitais, lookbooks e lead magnets com capas, páginas duplas, sumário visual, capítulos, colunas assimétricas, citações e exercícios. Use quando o usuário pedir um e-book, guia, revista digital ou PDF editorial.
---

# Digital E-Guide Editorial — TS Digitais

## Objetivo
Transformar conteúdo útil em uma publicação digital com identidade editorial própria, pronta para leitura em tela e exportação para PDF. O resultado não deve ser apenas uma sequência de páginas com caixas repetidas.

## 1. Brief e arquitetura
Identificar:
- Tema, público, objetivo e ação desejada após a leitura.
- Autor/organização responsável e dados reais de autoria.
- Extensão aproximada, capítulos, profundidade e formato de distribuição.
- Identidade visual, logotipo, paleta, fontes, imagens e referências autorizadas.
- Formato final: PDF A4, A5, carta, tela 16:9 ou dimensões personalizadas.

Propor um conceito editorial, uma estrutura de capítulos e uma direção visual. Não inventar credenciais, estatísticas, testemunhos, resultados ou citações.

## 2. Estrutura recomendada
Adaptar ao conteúdo; não incluir seções apenas para preencher um modelo.

### Capa
- Título específico e memorável, sem promessas exageradas.
- Subtítulo que explique o benefício ou escopo real.
- Autor, organização e data/versão quando pertinentes.
- Imagem ou elemento gráfico com função editorial.
- Evitar excesso de selos, estatísticas decorativas e texto pequeno.

### Abertura
- Nota ao leitor ou introdução curta.
- Contextualização do problema e do que o leitor encontrará.
- Orientação de uso quando houver exercícios ou atividades.

### Sumário
- Capítulos e páginas corretos, atualizados após a paginação final.
- Hierarquia visual clara; usar linhas-guia ou números discretos se ajudarem.
- Links internos clicáveis no PDF quando o formato permitir.

### Páginas internas / spreads
- Alternar páginas de abertura de capítulo, texto corrido, listas, diagramas, imagens, exemplos, tabelas e exercícios.
- Usar colunas assimétricas apenas quando melhorarem a leitura.
- Pull quotes devem vir do conteúdo real e manter atribuição correta.
- Caixas de exercício devem conter instrução clara, espaço/forma de resposta e objetivo.
- Incluir cabeçalhos, rodapés e numeração consistentes, sem competir com o conteúdo.

### Fechamento
- Síntese prática e próximos passos.
- Referências e fontes quando houver informação factual.
- Sobre o autor/organização apenas com dados confirmados.
- CTA claro, funcional e sem links fictícios.

## 3. Sistema visual
- Definir grid, margens, escala tipográfica, cores, estilos de imagem, componentes e regras de espaçamento.
- Combinar serif display e sans-serif de leitura quando fizer sentido; nunca impor essa combinação se a marca pedir outra solução.
- Criar variação entre páginas sem perder consistência.
- Usar capitulares, fios, notas laterais e citações com moderação.
- Preservar contraste, legibilidade e leitura em escala de 100%.
- Não usar uma página dupla simulada como substituto de um PDF multipágina final.

## 4. Conteúdo e fontes
- Escrever para o leitor, com progressão lógica e exemplos úteis.
- Distinguir fatos, recomendações, opiniões e exemplos fictícios.
- Citar fontes verificáveis e registrar datas em temas sujeitos a mudança.
- Não preencher páginas com texto genérico, repetição ou imagens sem relação com o capítulo.
- Revisar português, acentuação, consistência de termos e links.

## 5. Produção HTML e PDF
Para publicações em HTML:
- Usar HTML semântico, CSS organizado e assets locais quando possível.
- Construir componentes reutilizáveis para capa, capítulo, imagem, legenda, tabela, exercício e citação.
- Implementar navegação e sumário sem bloquear seleção de texto, zoom ou acessibilidade.

Para PDF:
- Usar a skill `weasyprint-pdf-creation` quando o documento puder ser renderizado com HTML/CSS e WeasyPrint.
- Definir tamanho de página, margens, cabeçalhos/rodapés, páginas pares/ímpares e quebras.
- Evitar conteúdo cortado, elementos sobrepostos, páginas em branco e títulos órfãos.
- Validar a paginação depois de atualizar fontes, imagens ou conteúdo.

## 6. QA obrigatório
1. Renderizar o documento completo, não apenas a capa ou um spread.
2. Inspecionar visualmente todas as páginas ou uma amostra representativa mais as páginas com tabelas/figuras.
3. Conferir tamanho, orientação, margens, sangria se aplicável, numeração e sumário.
4. Extrair texto do PDF e confirmar que não há conteúdo ausente ou ilegível.
5. Testar links, bookmarks e navegação interna.
6. Conferir leitura em desktop e celular, inclusive zoom.
7. Corrigir e renderizar novamente antes de entregar.

## 7. Entrega
Entregar PDF final e, quando possível, fonte editável HTML/CSS e dados usados para gerar o documento. Informar limitações de fontes, renderização ou validação. Não declarar o e-book pronto sem abrir e inspecionar o arquivo final.

## Curadoria da origem
Esta é uma skill original da TS Digitais baseada nos requisitos editoriais definidos para nossos projetos. O nome “Digital E-Guide Generator” atribuído a bykaranmrn foi citado em https://mcpmarket.com/tools/skills/digital-e-guide-generator-1, mas não foi possível confirmar um repositório canônico, conteúdo integral ou licença de redistribuição. Portanto, nenhum arquivo foi copiado desse fornecedor; esta implementação é independente e deverá ser revista se a origem verificável for identificada.