# Shader, WebGL, 3D UI e referências cinematográficas

Atualizado: 25/11/2026. Curadoria inicial a partir de links fornecidos pelo usuário e verificação de documentação pública. Este documento é um índice de descoberta; não significa que os sites estejam conectados ao TS Brain nem que seus assets estejam liberados para reutilização.

## Implementação e código

| Fonte | Categoria | Situação / licença / limite |
|---|---|---|
| [Shaders engine](https://github.com/shader-effects-inc/shaders) | Engine e componentes WebGPU | MIT para engine/componentes; biblioteca premium continua paga. MCP/CLI oficiais; acesso ao catálogo Pro é pago. |
| [Paper Shaders](https://shaders.paper.design/) | Shaders React | Biblioteca de efeitos; validar licença do pacote e compatibilidade. |
| [Magic UI](https://github.com/magicuidesign/magicui) | Componentes React animados | MIT. |
| [Aceternity UI](https://ui.aceternity.com/components) | Componentes React/Tailwind | Mistura de gratuitos e pagos; checar cada componente. |
| [Skiper UI](https://skiper-ui.com/) | Componentes e microinterações | Gratuitos e pagos; atribuição exigida nos gratuitos conforme documentação. |
| [React Bits](https://reactbits.dev/) | Componentes React animados | Validar licença por componente/repositório. |
| [Vanta.js](https://www.vantajs.com/) | Fundos WebGL interativos | Requer fallback mobile/performance; verificar licença no repositório antes de distribuir. |
| [Codrops](https://tympanus.net/codrops/) / [GitHub](https://github.com/codrops) | Demos experimentais | Licença varia por demo/repositório; não presumir MIT universal. |
| [Three.js Resources](https://threejsresources.com/category/website) | Diretório de demos | Descoberta; usar licença da fonte original. |
| [somnathraz/premium-frontend](https://github.com/somnathraz/premium-frontend) | Templates Next.js/R3F | Candidato; licença, dependências e assets ainda precisam de auditoria. |
| [layerframe/react-three-shader-library](https://github.com/layerframe/react-three-shader-library) | Exemplos GLSL/R3F | Arquivado em 25/07/2023; somente referência educacional. |
| [Shadeon](https://shadeon-chi.vercel.app/) | Editor/biblioteca de shaders | Confirmar repositório canônico e licença antes de incorporar. |

## MCP / CLI para investigar

| Ferramenta | Possibilidade | Acesso |
|---|---|---|
| [Shaders MCP + CLI](https://shaders.com/docs/guide) | Instalar/editar efeitos por agente e CLI | Engine open-source e CLI/MCP básicos gratuitos; biblioteca premium Pro. |
| [21st.dev MCP](https://21st.dev/mcp) | Buscar e instalar componentes | Busca gratuita; Free permite 2 instalações/recuperações por dia somando web, MCP e CLI; requer autenticação. |
| [Aceternity UI](https://ui.aceternity.com/) | Integração com agentes MCP | Verificar endpoint, autenticação e escopos antes de conectar. |
| [Subframe](https://www.subframe.com/) | Canvas + agente + MCP | Ferramenta design/build; Free tem um projeto e créditos limitados; avaliar fluxo de dados. |
| [Mobbin MCP](https://mobbin.com/mcp) | Pesquisa de referências UI por agente | MCP oficial; disponível em planos Pro/Team, OAuth; não é gratuito. |
| [Unicorn Studio MCP](https://www.unicorn.studio/docs/mcp/) | Criar/editar cenas no editor por agente | MCP em todos os planos; Free 250 alterações/mês, mas uso pessoal/não comercial; Legend tem licença comercial. |
| [Magic UI MCP](https://github.com/magicuidesign/mcp) | Busca/instalação de componentes | Servidor oficial MIT; confirmar schema e versão. |

## Referências visuais (não são bibliotecas de código)

- [Scrolltide](https://www.scrolltide.co/) — benchmark de direção visual e efeitos.
- [HorizonX](https://horizonx.so/) — catálogo premium de UI, shaders, texturas e assets; não gratuito como fonte de downloads.
- [Mobbin](https://mobbin.com/) — pesquisa de padrões de produto/UI; screenshots não devem virar assets. MCP oficial existe, mas exige Pro/Team.
- [Refero](https://refero.design/) — inspiração de interfaces.
- [Gogly](https://gogly.design/) — inspiração; licença não verificada.
- [Vanta Supply](https://vanta.supply/) — referência/ativos; validar direito por item.
- [Motionin](https://motionin.design/) — referências de motion, shaders e easing; checar direitos/limites.
- [60fps](https://60fps.design/) — inspiração de motion; licença não verificada.
- [Jiro](https://jiro.build/) — inspiração web; licença não verificada.
- [Landdding](https://landdding.com/) — galeria editorial de landing pages.
- [Unicorn Studio](https://www.unicorn.studio/) — editor WebGL e embeds; Free é pessoal/não comercial, MCP disponível em todos os planos (250 mudanças/mês no Free), JSON export e licença comercial exigem Legend. Não é projeto Three.js.
- [Paper Shaders](https://shaders.paper.design/) — efeitos e pacote React; consultar licença do pacote.
- [Scroll Shaders](https://www.instagram.com/p/DgAOxJbjWZs/) e Backgrounds Supply — referências Instagram enviadas pelo usuário; não são repositórios de código, verificar origem/licença de cada asset.

## Fontes oficiais para licenças

- Shaders.com: https://shaders.com/updates/shaders-is-open-source e https://shaders.com/docs/guide
- Codrops: https://tympanus.net/codrops/licensing/
- React Bits: https://github.com/DavidHDev/react-bits
- Vanta.js: https://github.com/tengbao/vanta
- Unicorn Studio: https://www.unicorn.studio/docs/pricing/

## Política de ingestão

- Não baixar tudo. Priorizar leitura de README, LICENSE, exemplos e documentação oficial.
- Registrar commit/tag e licença por repositório, não por marca/site.
- Sites de inspiração entram como metadados e links, não como scraping massivo nem cópia de screenshots.
- Separar código MIT/Apache/ISC de assets e presets comerciais.
- Nenhum MCP foi ativado por este catálogo. Antes de conectar: auditar endpoint, ferramentas, autenticação, permissões, custos, telemetria e dados enviados. Shaders, Magic UI, 21st.dev, Mobbin e Unicorn Studio têm MCPs oficiais; condições variam, e Mobbin requer Pro/Team.
- Rotas do TS Brain devem consultar esta Skill para tarefas de shader/WebGL/UI; ainda é necessário validar o runtime e a renderização real.


## Correções verificadas em 25/11/2026
- Magic UI possui MCP oficial MIT e CLI oficial: https://github.com/magicuidesign/mcp ; ferramentas de registry, não motor de render 3D.
- 21st.dev: busca gratuita, mas conta Free limita recuperação de código a 2/dia no conjunto web/MCP/CLI; requer autenticação. Geração AI usa créditos separados.
- Shaders engine/componentes MIT e CLI/MCP básico gratuito; biblioteca Pro de presets e seções continua paga. WebGPU-only, sem fallback WebGL.
- React Bits usa MIT + Commons Clause: uso comercial permitido, mas não revender/sublicenciar/redistribuir os componentes isoladamente; preservar notices de terceiros.
- Codrops: demos para download MIT salvo exceção explícita; manter notices e não revender/redistribuir a demo como item isolado ou versão editada.
- Vanta.js upstream declara MIT (https://github.com/tengbao/vanta); não confundir com Vanta Supply.
- Unicorn Studio Free é pessoal/não comercial; uso comercial e export JSON/self-host dependem do plano Legend. Não usar o Free em anúncios de clientes.


## Engines 3D adicionais e rotas de renderização — verificado em 25/11/2026

As tecnologias abaixo foram separadas por função para o seletor não escolher um motor completo quando basta aplicar um shader a um elemento HTML.

| Tecnologia | Uso recomendado | Licença / estado |
|---|---|---|
| [Three.js](https://github.com/mrdoob/three.js) | Padrão geral da esteira para cenas autorais WebGL/WebGPU, GLTF, geometria, PBR, iluminação e shaders. | MIT. Há Skills locais r186 e módulos especializados. |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | Engine completa com WebGL/WebGPU, materiais PBR, editor de materiais e sistema de física plugável. | Apache-2.0. Conferir licença/termos de engines e plugins de física separadamente. |
| [PlayCanvas Engine](https://github.com/playcanvas/engine) | Engine WebGL2/WebGPU para cena interativa, 3D e WebXR; inclui orientação/Skills para agentes de IA. | MIT no engine. Diferenciar engine open-source de Editor/serviços hospedados. |
| [OGL](https://github.com/oframe/ogl) | Biblioteca WebGL mínima para shaders GLSL, efeitos, distorções e cenas pequenas com baixo overhead. | Unlicense. Menos abstração; não é substituta de engine completa. |
| [Curtains.js](https://github.com/martinlaxenaire/curtainsjs) | Liga imagens/vídeos/elementos DOM a planos WebGL com shaders, preservando layout CSS. | MIT. Não é engine geral de modelagem 3D. |
| [ThreePipe](https://github.com/repalash/threepipe) | Toolkit em cima de Three.js para visualização de produto e renderização web com materiais/estúdio. | Apache-2.0 no core; beta; revisar licença de cada plugin. |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) + [Drei](https://github.com/pmndrs/drei) | Componentes declarativos e helpers para cenas Three.js dentro de React/Next.js. | MIT em ambos. Não introduzir React em tarefa HTML simples. |
| [TresJS](https://github.com/Tresjs/tres) | Cenas Three.js declarativas em Vue. | MIT no core; revisar addons. |
| [Threlte](https://github.com/threlte/threlte) | Cenas Three.js declarativas em Svelte. | MIT no core; revisar addons. |
| [Google model-viewer](https://github.com/google/model-viewer) | Elemento HTML para apresentar GLB/GLTF com controles e iluminação, sem construir uma engine de cena. | Apache-2.0. Visualizador, não renderer offline. |
| [Google Filament](https://github.com/google/filament) | Engine de render PBR de baixo nível; rota avançada quando há capacidade para integrar WebAssembly/WebGL. | Apache-2.0. Exige avaliação de build, tamanho e ciclo de vida; não é primeira opção para o runtime leve. |

### Decisão por caso

- **Shader em landing page / fundo / metal líquido / distorção:** OGL para shader próprio; Curtains.js quando o efeito precisa estar preso a imagens e elementos DOM; CSS quando já resolve.
- **Cena 3D customizada na web:** Three.js é o padrão. Babylon.js ou PlayCanvas quando recursos integrados evitarem muito código próprio.
- **Projeto React existente:** R3F + Drei. Projeto Vue: TresJS. Projeto Svelte: Threlte.
- **Exibir um modelo GLB pronto:** model-viewer antes de escolher uma engine completa.
- **Visualização de produto com estúdio web:** avaliar ThreePipe, com cautela para beta e plugins.
- **Notebook com RAM/GPU limitadas:** importação sob demanda, DPR 1 como ponto inicial, limites de texturas/geometria, pausar fora da viewport, reduzir pós-processamento e respeitar prefers-reduced-motion. Não carregar várias engines juntas.

### Blender remoto via GitHub Actions

O Blender suporta modo sem interface gráfica por linha de comando. Uma cena gerada por Python/bpy pode ser renderizada por um runner Linux usando o comando:

~~~bash
blender --background cena.blend --python scripts/render.py
~~~

Arquitetura-alvo:
1. TS Brain prepara um job com versão Blender fixa, cena/script autorizados, Cycles ou Eevee, resolução, amostras, threads e output.
2. Workflow manual/API via workflow_dispatch valida os parâmetros e instala versão/checksum do Blender.
3. Roda em CPU nos runners padrão (não presumir GPU dedicada/CUDA/OptiX).
4. Verifica o arquivo gerado e publica como artifact com retenção curta.
5. TS Brain consulta a execução, baixa artifact, gera preview e roda QA visual real. Falha/ausência do artifact bloqueia aprovação.

Limites e privacidade:
- GitHub documenta runners padrão públicos como gratuitos e sem limite de minutos; repositórios privados consomem franquia mensal e podem gerar cobrança após excedê-la. Self-hosted não cobra tempo de execução do GitHub, mas usa hardware do proprietário.
- Runner Linux padrão: 4 CPUs, 16 GB RAM e 14 GB SSD; assumir CPU sem GPU dedicada. Adequado para teste, still moderado e algumas animações pequenas, não para prometer render pesado rápido.
- Não colocar cenas, marcas, texturas, logos ou briefing privado em repo público, logs ou artifacts públicos. Usar repo privado e acompanhar a franquia, ou infraestrutura própria autorizada.
- Secrets com menor privilégio; nunca aceitar código bpy não confiável em workflow com secrets; fixar versões, limitar amostras/resolução/threads/timeout e evitar registrar dados de clientes.
- Blender renderiza cenas 3D offline; não renderiza DOM/Three.js/WebGL. Para HTML/WebGL usar Chromium/Playwright e capturar o canvas/DOM.

**Status:** arquitetura documentada, não implementada. O TS Brain ainda não dispara workflows, acompanha execuções nem baixa artifacts. Antes de declarar o backend remoto disponível, provar o fluxo completo com uma cena pública/sintética e confirmar que artefato e preview chegam ao Creative Studio.

## Fontes verificadas

- Blender background render: https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
- GitHub Actions runners: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
- GitHub Actions billing: https://docs.github.com/en/actions/concepts/billing-and-usage
- GitHub Actions limits: https://docs.github.com/en/actions/reference/limits
- Three.js: https://github.com/mrdoob/three.js
- Babylon.js: https://github.com/BabylonJS/Babylon.js
- PlayCanvas Engine: https://github.com/playcanvas/engine
- OGL: https://github.com/oframe/ogl
- Curtains.js: https://github.com/martinlaxenaire/curtainsjs
- ThreePipe: https://github.com/repalash/threepipe
- R3F/Drei: https://github.com/pmndrs/react-three-fiber ; https://github.com/pmndrs/drei
- TresJS/Threlte: https://github.com/Tresjs/tres ; https://github.com/threlte/threlte
- model-viewer: https://github.com/google/model-viewer
- Filament: https://github.com/google/filament
