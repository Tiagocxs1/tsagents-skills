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
