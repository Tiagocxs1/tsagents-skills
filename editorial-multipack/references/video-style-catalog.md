# Catálogo inicial de estilos de vídeo editorial

> Status: revisão local concluída em 21-11-2026. Foram inspecionadas as pastas e referências em `/home/tiago/Documentos/Estilos de Vídeos/` e as skills correspondentes em `~/.ia-config`. A existência dos arquivos foi confirmada; a disponibilidade dos renderers, MCPs, licenças de assets e APIs deve ser verificada por tarefa.

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

Observação: o brief antigo `docs/guardian-video-graphics-brief.md` contém exemplos ilustrativos de números como “98% eficácia” e “12 seg resposta”, além de uma sugestão de verde em comparação. Não reutilizar tais números como fatos nem a cor verde como elemento de marca sem revisão/aprovação.


## Padrões e ferramentas já descritos no pipeline de vídeo da .ia-config

O documento versionado `ia-config/docs/video-pipeline.md` contém também referências práticas que não devem ser perdidas. Elas ampliam o catálogo acima, mas são tratadas como **configuração histórica documentada**, não como prova de que a pasta local ou os MCPs continuam ativos. O diretório ainda precisa ser inspecionado diretamente no PC.

### Estilos técnicos adicionais para testar

| ID | Padrão | Uso | Cuidados |
|---|---|---|---|
| V18 | Face-tracked presenter / portrait overlay | Apresentador em recorte/overlay, com acompanhamento facial, para vídeo vertical | Manter rosto natural e máscara limpa; não inventar tracking se o rosto não estiver visível |
| V19 | Ken Burns vertical slideshow | Fotografias e imagens documentais com movimento lento, pan e zoom | Usar fotos licenciadas/autorizações; movimentos não devem mudar o sentido da imagem |
| V20 | Split-screen / stacked comparison | Comparar etapas, dois cenários ou A/B com a mesma escala visual | Só comparar cenas compatíveis; identificar quando datas/contextos são diferentes |
| V21 | Presenter cutout / person overlay | Apresentador recortado sobre ambiente, screenshot ou infográfico | Não fabricar aparência de pessoas reais; revisar cabelo, bordas, sombras e recortes |
| V22 | Speech-aware jump-cut / silence edit | Conteúdo falado gravado, tutoriais, depoimentos e aulas | Não cortar pausas que alteram intenção/clareza; rever o áudio completo |

Esses estilos se relacionam aos templates descritos no pipeline: `track_faces`, `render_mask`, `bg_slideshow`, `split_screen` e `person_overlay`. O documento registra um projeto vertical GuardianPromo de 1080×1920, 30fps, cerca de 65 s e 10 cenas como referência histórica de composição; verificar se os arquivos de projeto continuam disponíveis antes de clonar.

### Stack de vídeo referenciada pela .ia-config

| Camada | Recursos documentados | Aplicação no pacote |
|---|---|---|
| Composição/render | Remotion, FFmpeg, FFprobe | Criar cenas, exportar MP4 e verificar streams, resolução, duração e áudio |
| Motion/roteiro visual | `animatic-mcp`, templates de Remotion, GSAP/animações web | Brief → storyboard → animatic → cenas e motion |
| Edição de vídeo/áudio | `mcp-video`, MoviePy, PySceneDetect, auto-editor, trimmy | Cortes, montagem, detecção de cenas e pós |
| Imagem/vídeo/áudio com IA | `artificer-mcp` | Gerar assets quando houver justificativa e créditos/custo aprovados |
| Voz e transcrição | Edge TTS, Kokoro TTS, Whisper/faster-whisper | Narração PT-BR, legendas, transcrição e revisão |
| Som | Freesound, sfx-bfxr | Efeitos e ambientação; validar licença e credencial antes de usar |
| Captura e assets | Kap, MediaPipe, rembg | Captura de tela, tracking e remoção de fundo |
| Automação/pipelines | SwiftClip, AutoCast | Storyboard JSON e slideshow vertical/automação |

A tabela representa recursos registrados em `docs/video-pipeline.md`. Antes de uso, consultar runtime real, arquivo de configuração local e repositório/commit; não assumir que um status “ativo” de documento antigo continua correto. Serviços de geração de IA podem consumir créditos e não são automaticamente gratuitos. Preferir render local com FFmpeg/Remotion enquanto o hardware permitir; Lambda ou outros serviços cloud são opção, não padrão.

### Princípios de seleção por artigo

- **Definições/conceitos:** V01 kinetic typography ou V16 technical animation.
- **Reportagem/localidade:** V02/V10 + V11 mapa.
- **Demonstração de site ou procedimento:** V04 e, se apresentar pessoa, V03/V18/V21.
- **Dados e comparação:** V05/V06/V20.
- **História, memória e acervo fotográfico:** V08/V19.
- **Conteúdo falado gravado:** V03/V15 com V22 apenas quando a edição ajudar.
- **Assunto técnico:** V16, eventualmente com V07.

Para o arquivo final: além de still previews, assistir a exportação completa e executar FFprobe. Renderização em nuvem depende de credenciais e custos; não selecionar automaticamente.


## Estilos confirmados na biblioteca local (21-11-2026)

A revisão de `/home/tiago/Documentos/Estilos de Vídeos/` e das skills locais revelou estilos visuais adicionais. Eles devem ser selecionados pelo assunto e pelo material disponível, não transformados em preset obrigatório para todo artigo.

| ID | Estilo local | Melhor uso | DNA visual e recursos técnicos | Estrutura sugerida |
|---|---|---|---|---|
| V23 | **Netflix / Blockbuster cinematic reel** | Histórias de marcas, negócios, mudanças de mercado e narrativas de virada em vídeo vertical | Seis cenas, portal zoom, personagens e cenários em cut-outs, parallax, sombras que viram personagens/objetos, brilho de luminária, film grain, scanlines e posterize/stop-motion irregular | Cold open → oferta/situação → oposição → queda → payoff → conclusão |
| V24 | **VOX / Fern paper-collage documentary** | História, investigações, fatos e explicações documentais com fontes | Newsprint e mapas de arquivo, fotos halftone P&B recortadas, fita, carimbos, barbante vermelho, pins e um acento vermelho/mustarda; composição editorial matte com espaço negativo | Narração contínua → beats visuais → montagem de recortes → pôster editorial final |
| V25 | **3D documentary mannequin** | Explicar papéis, organizações, relações institucionais e reconstruções não gráficas quando atores reais não forem necessários | Figuras 3D sem rosto em branco, vermelho e preto; void branco ou cenário realista esparso; luz volumétrica, profundidade de campo e props realistas | Cold open → contexto → ação por beats → consequência; travar identidade das figuras em character sheets |
| V26 | **Glass SaaS / 3D product showcase** | Demonstração de plataformas, dashboards, funcionalidades, apps e lançamentos de produto | Cards translúcidos com frost, bordas iluminadas, travelling light, cursor-esfera refrativo, widgets com dados sincronizados e foley de interação | Ação de entrada → interface se revela → funcionalidades → interação → zoom no benefício |
| V27 | **Animated documentary map** | Localização, geografia, deslocamentos, cobertura territorial, infraestrutura e acontecimentos com dimensão espacial | Dados geográficos reais (World Atlas/TopoJSON/D3 Geo), outlines, rotas e câmera contínua; transições entre cenas devem casar no mesmo frame | Mapa amplo → foco na região → movimento/rota → consequência espacial → volta ao contexto |
| V28 | **VOX paper-chart data storytelling** | Indicadores, tendências, eleições, finanças, pesquisas e comparações quantitativas | Base de papel, contornos marker, textura/grain, barras, assentos em lattice e linhas animadas; ruído determinístico por frame, eixo/texto sempre legíveis | Pergunta → dado citado → comparação → mudança ao longo do tempo → leitura |
| V29 | **Paper-collage stop-motion** | Narrativas editoriais, processos, campanhas sazonais e histórias que combinam fotos/objetos com uma linguagem artesanal | Recortes PNG com bordas rasgadas, textura de fibra, camadas de papel, parallax, movimento stepped e holds assimétricos; personagem pode ficar entre duas partes do mesmo objeto (sandwich) | Storyboard em painéis → contact sheet de assets → cena em camadas → foley sincronizado |

### Métodos de produção e kits de motion (não são estilos editoriais)

| Método / kit | Quando usar | Princípios reaproveitáveis |
|---|---|---|
| **Starter Kit Overlays (Remotion)** | Quando o vídeo precisa de títulos, lower thirds, callouts, kinetic type, badges ou gráficos com transparência para montar no editor | Toda peça deve ter entrada e saída completas, props/schema reutilizáveis, stagger, antecipação/overshoot/settle, safe zones e export MP4/ProRes alpha/PNG sequence |
| **Build Guide Motion Explainer (9 fases)** | Explainer complexo que exige consistência e várias cenas | Setup → direção de arte → roteiro/timeline → inventário de assets → SVG → motion primitives → arquitetura → código → montagem; testar cena a cena antes de ampliar |
| **CopyVideoStile / reverse-engineering de referência** | Quando o usuário fornece um vídeo para analisar e replicar sua gramática visual, sem copiar conteúdo | Decompor cada corte por timecode, fala, enquadramento, crop, ritmo, transição e SFX; extrair regras reutilizáveis e validar com material próprio |
| **Video Director Pipeline** | Vídeos com geração de imagem/vídeo por IA | Verificar custo/créditos primeiro; criar character/motif sheets; aprovar frames do storyboard antes de gerar takes; montar e revisar áudio separadamente |

### Salvaguardas específicas para as referências locais

- **Não tratar assets incluídos nos practice kits como banco de imagens liberado para uso comercial.** O kit de mapa informa expressamente que as imagens, clipes e áudios fornecidos são para prática pessoal; recriações publicáveis devem usar mídia própria ou licenciada.
- Não copiar prompts, roteiros, branding ou identidade de canais de terceiros como se fossem nossos. Reaproveitar técnicas e gramática visual, criando roteiro, dados, assets e composições originais.
- Para o estilo mannequin, personagens sem rosto são uma escolha estética; não usar para insinuar que pessoas reais cometeram atos ou participaram de eventos sem evidência.
- Mapas e gráficos devem usar dados reais, rastreáveis e com fonte. Não usar números ilustrativos do tutorial como estatísticas editoriais.
- Glassmorphism e efeitos 3D devem servir à clareza do produto; se o efeito prejudicar texto ou interface, reduzir blur, glow e movimento.
- O áudio dos kits, músicas e efeitos precisa de verificação independente de licença/atribuição. Um arquivo presente localmente não prova autorização de publicação.
- Esses kits foram produzidos com Remotion/Claude e algumas referências mencionam serviços pagos (por exemplo, ElevenLabs, Magnific, Replicate ou Seedance). Isso não torna a produção dependente desses serviços: preferir assets próprios/licenciados, FFmpeg/Remotion local, Edge TTS/Kokoro e efeitos livres quando a qualidade for adequada.

### Mapeamento inicial por assunto

- **Notícia factual com dados:** V17 + V28; mapa V27 apenas se a localização for central.
- **História / investigação:** V02 + V24 ou V25, conforme a necessidade de fontes visuais e reconstrução.
- **História de marca / caso de negócio:** V23 ou V24; V13 se houver evidência verificável de resultado.
- **Produto digital / software:** V04 + V26; V23 só quando houver narrativa de transformação.
- **Explicação territorial:** V11 + V27.
- **Campanha ou história artesanal:** V29, com assets de uso autorizado.
- **Artigo com indicadores:** V05 + V28; manter eixo, escala, recorte temporal e fonte visíveis.

A seleção final deve considerar também o canal: WebStory 13 telas, vídeo, carrossel 7 telas e post estático terão versões adaptadas da mesma tese, não cópias literais do mesmo layout.
