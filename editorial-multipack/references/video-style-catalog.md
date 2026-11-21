# Catálogo inicial de estilos de vídeo editorial

> Status: catálogo provisório. Foi elaborado a partir das skills e referências versionadas de \`.ia-config\`, incluindo o pipeline Remotion, mcp-video, artificer-mcp, animatic-mcp, Kokoro/Edge TTS, A12 (roteiros), A13 (motion) e A14 (edição). Ainda precisa ser comparado aos projetos locais em \`/home/tiago/Documentos/Estilos de Vídeos/\`, que não estavam acessíveis durante esta revisão.

## Como escolher o estilo

O artigo define a informação e o público; o estilo define a forma de explicar. Não usar um estilo fixo em todos os assuntos. Antes de escolher, responder:

- O que o público precisa entender, sentir ou fazer depois de assistir?
- O assunto depende mais de demonstração, explicação, evidência, localização, experiência ou atmosfera?
- Há imagens reais e autorizadas? Existe necessidade de apresentador, captura de tela, motion ou narração?
- O estilo consegue explicar sem recorrer a exageros, dados inventados ou imagens que simulem acontecimentos reais?

## Biblioteca de estilos

| ID | Estilo | Melhor uso | Linguagem visual | Estrutura-base |
|---|---|---|---|---|
| V01 | Explainer editorial / kinetic typography | Conceitos, definições, temas abstratos, explicações rápidas | Tipografia cinética, formas e ícones com hierarquia clara | Pergunta → conceito → 2–3 ideias → síntese |
| V02 | Mini-documentário narrado | Temas que exigem contexto, fontes, imagens e encadeamento | Voz off, B-roll documental, cortes por ideia, dados com fonte | Contexto → evidência → análise → conclusão |
| V03 | Apresentador + B-roll | Dicas, opinião especializada e explicações com presença humana | Apresentador em plano médio/close intercalado com apoio visual | Hook → explicação → exemplo → conclusão |
| V04 | Tutorial / screen walkthrough | Sistemas, sites, aplicativos, procedimentos e demonstrações | Captura de tela, zoom, callouts, cursor/realces e capítulos | Objetivo → passos → resultado → ressalvas |
| V05 | Motion infographic / data story | Indicadores, comparações, processos e dados quantitativos comprovados | Gráficos, números, mapas, timelines e legendas de fonte | Pergunta → dado → comparação → significado |
| V06 | Comparação lado a lado | Diferenças, alternativas, antes/depois documentado | Split screen, wipe ou comparação sequencial | Critério → cenário A → cenário B → diferenças |
| V07 | Timeline / processo em etapas | Fluxos, cronologias e explicações operacionais | Linha do tempo, etapas animadas, progressão de estado | Início → passos → ponto de decisão → resultado |
| V08 | Photo essay / Ken Burns | Temas com bom acervo fotográfico, história, lugares e memória | Fotografias com movimento suave, recortes e legendas | Sequência visual → contexto → interpretação |
| V09 | Demonstração POV | Produtos e serviços que podem ser mostrados em uso real | Primeira pessoa, detalhes de operação e som ambiente | Situação → uso → detalhe → benefício verificável |
| V10 | Mini-reportagem local | Assuntos geográficos, comunitários, negócios e eventos | Cenas reais, contexto de local, entrevistas autorizadas | Local → questão → vozes/evidências → conclusão |
| V11 | Mapa / geografia explicada | Cobertura, localização, deslocamentos, áreas e eventos | Mapa com escala, marcadores, trajetos e rótulos | Onde → relação espacial → impacto → leitura |
| V12 | Mito versus fato | Dúvidas e equívocos comuns com resposta comprovável | Pares visuais, rótulos, pausa para explicação | Mito/pergunta → evidência → correção → resumo |
| V13 | Caso real / estudo de caso | Resultados, processos e experiências com autorização e prova | Narrativa de caso, depoimento autorizado, documentos e contexto | Cenário → desafio → ação → resultado verificável |
| V14 | Curta cinematográfico de marca | Conteúdo institucional/manifesto em que atmosfera tem função | Fotografia, ritmo, som, movimento de câmera e identidade | Imagem-âncora → ideia → progressão → assinatura |
| V15 | FAQ rápido / resposta direta | Perguntas frequentes e objeções pontuais | Apresentador ou texto em tela, pergunta como capítulo | Pergunta → resposta → explicação → próximo passo |
| V16 | Animação de processo técnico | Segurança, engenharia, software e equipamentos | Diagramas, camadas, circuitos e estados de operação | Sistema → mecanismo → interação → limite |
| V17 | Recorte editorial / comentário sobre notícia | Notícias e mudanças atuais com fontes verificáveis | Headline, timeline, mapa, tela com fonte e contexto | O que aconteceu → o que sabemos → impacto → o que falta saber |

## Combinações híbridas

- V02 + V05: mini-documentário apoiado por dados.
- V03 + V04: apresentador introduz um tutorial real.
- V08 + V01: foto-ensaio com definições em tipografia.
- V10 + V11: reportagem local com mapa.
- V16 + V07: sistema técnico explicado em sequência.
- V17 + V03: análise editorial com apresentador e fontes na tela.

Combinar somente quando os estilos tiverem função clara. Não adicionar motion apenas para preencher cenas.

## Estilos por formato e duração

- **15–20 s:** uma pergunta ou uma ideia, V01, V12 ou V15. Evitar encaixar um artigo inteiro.
- **30–45 s:** explicação com 2–3 pontos, V03, V04, V05, V07 ou V16.
- **45–60 s:** V02, V03, V10, V11 ou V17 com contexto e conclusão.
- **60–90 s:** mini-documentário, tutorial ou caso quando a informação exigir. Não cortar ressalvas essenciais apenas para caber em 60 s.

Duração é decisão editorial, não requisito fixo. Sempre que o usuário pedir uma duração específica, respeitá-la e dimensionar o roteiro.

## Regras universais de produção

1. Roteiro cena a cena com fala/narração, texto em tela, ação visual, enquadramento, duração e asset.
2. Cada cena deve ter propósito: informar, demonstrar, contextualizar, comprovar ou conectar.
3. Legendas sincronizadas, boa mixagem, ducking de música e safe zones em formatos verticais.
4. Usar J-cuts/L-cuts e efeitos sonoros quando reforçarem a continuidade; não aplicar whoosh/pop em toda transição.
5. Variar ritmo e enquadramento com intenção, sem transformar todo vídeo em cortes rápidos.
6. Não usar áudio, música, footage ou fotos sem direitos compatíveis.
7. Pré-visualizar stills de cada cena crítica, assistir ao vídeo final e validar streams/duração/áudio com FFprobe.
8. Manter projeto editável, fontes, assets, licença e versão no manifesto do pacote.

## Stack gratuita prioritária do ecossistema

- Remotion para composição com React e render local.
- FFmpeg/FFprobe para processamento e QA.
- Edge TTS ou Kokoro TTS para voz, se a voz sintética fizer sentido.
- mcp-video / artificer-mcp / animatic-mcp quando realmente disponíveis e sem custo por geração que exceda a necessidade.
- Freesound e outras bibliotecas de áudio apenas com licença/atribuição conferida.

Serviços de geração de vídeo/imagem com crédito não são considerados gratuitos ilimitados; verificar custo por tarefa e não consumir créditos sem necessidade.

## Restrições específicas Guardian

Quando o conteúdo for da Guardian:
- Seguir o perfil visual vigente: azul escuro, vermelho, azul/cinza e cyan conforme identidade; **não usar verde**.
- Usar somente equipamentos e tecnologias Intelbras quando mostrar produtos.
- Não criar números de tempo de resposta, eficácia, clientes, alarmes, sensores ou câmeras sem fonte documental atual e aprovação.
- Não simular roubo, invasão ou uma ocorrência real como se fosse footage documental.
- Não prometer segurança absoluta ou resultado garantido.
- Dar preferência a demonstrações reais autorizadas, gráficos explicativos e processos efetivamente praticados pela empresa.

Observação: o brief antigo \`docs/guardian-video-graphics-brief.md\` contém exemplos ilustrativos de números como “98% eficácia” e “12 seg resposta”, além de uma sugestão de verde em comparação. Não reutilizar tais números como fatos nem a cor verde como elemento de marca sem revisão/aprovação.
