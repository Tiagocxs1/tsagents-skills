---
name: tsdigitais-3d-scene-production
description: "Roteia e especifica cenas 3D reais por código, com geometria, câmera, iluminação, materiais PBR, personagens/objetos, render e QA. Use em qualquer pedido 3D, fotorrealismo, Blender, Three.js, WebGPU, Cycles, HDRI, GLB, VRM ou visualização de produto/arquitetura."
---

# Produção de cenas 3D — TS Digitais

## Contrato
Produza 3D real, não uma imagem 2D simulando volume. O caminho padrão é geometria e materiais em Blender ou Three.js; **não use geradores de imagem por difusão**. Não chame serviços pagos de geração de malha.

## Resumo operacional — selecione antes de codificar

- **Three.js:** padrão para cenas customizadas no navegador, GLTF, materiais, câmera, luz, shaders e WebGL/WebGPU.
- **Babylon.js / PlayCanvas:** engines completas quando PBR, física, editor ou sistemas integrados justificarem a estrutura maior.
- **OGL:** shader GLSL e efeito WebGL autoral com baixo overhead; exige código mais manual.
- **Curtains.js:** aplicar shaders a imagens/vídeos/elementos DOM preservando layout CSS.
- **React Three Fiber + Drei:** somente em stack React; **TresJS** para Vue; **Threlte** para Svelte.
- **model-viewer:** primeira escolha para simplesmente apresentar um GLB/GLTF pronto.
- **ThreePipe:** avaliar em visualização de produto web; projeto em beta, auditar plugins.
- **Filament:** renderer PBR avançado com build WebAssembly; somente quando a integração e o peso forem justificáveis.
- Não carregar várias engines na mesma peça. Em notebook limitado, lazy-load, DPR inicial 1, texturas/geom. enxutas, pausar fora da viewport e reduzir pós-processamento.

### Fallback Blender headless em nuvem

- Blender pode renderizar sem UI via `blender --background cena.blend --python scripts/render.py`.
- GitHub Actions padrão é CPU; runner Linux de referência tem 4 CPUs, 16 GB RAM e 14 GB SSD, sem GPU dedicada presumida. Bom para smoke test/stills moderados/animações curtas, não promessa de render pesado rápido.
- Runners padrão são gratuitos em repositórios públicos; privados consomem franquia mensal e podem gerar cobrança excedente. Nunca enviar arquivos/briefings de clientes a repositórios públicos ou artifacts públicos.
- Pipeline futuro: job tipado → workflow_dispatch → Blender fixo/verificado → validar imagem → artifact → TS Brain baixa → preview real → QA visual. Sem artifact válido e revisão por pixels, não há aprovação.
- Blender não renderiza DOM/Three.js/WebGL. Para HTML e cenas web usar Chromium/Playwright para capturar DOM/canvas.
- **Status:** backend Actions não está implementado nem conectado. Não afirmar que um job foi enviado ou render concluído até validar ponta a ponta com cena pública/sintética.

## Escolha do motor
- **Imagem final estática, fotografia de produto, cena cinematográfica, PNG com alpha, render offline:** Blender + Python `bpy`; prefira Cycles para ray tracing/fidelidade final e Eevee para prévias rápidas. Só execute quando Blender estiver instalado e o hardware tiver memória/armazenamento suficientes.
- **Cena interativa, configurador, produto navegável, web 3D ou animação em tempo real:** Three.js. Use `WebGPURenderer` + TSL quando o browser/GPU inicializar WebGPU; valide backend após `await renderer.init()`. WebGL2 é uma rota alternativa somente quando o alvo não suporta WebGPU ou o usuário aceitar fallback.
- **Arquitetura procedural interativa:** Three.js + `threejs-architecture-effects`; não confundir o template com render offline ou exportação de vídeo.
- **Se não houver motor instalado/conectado:** entregue blueprint técnico e código/arquivos de projeto que possam ser executados no ambiente adequado; classifique a renderização como não executada. Nunca diga que houve render, inspeção ou aprovação sem evidência.

## Planejamento obrigatório
1. Defina saída: still/PNG, alpha, resolução/aspecto; GLB/GLTF/VRM; web interativa; sequência ou vídeo.
2. Defina escala/unidades, origem, geometria, silhueta, câmera (sensor/lente/distância/DOF) e enquadramento.
3. Separe assets: geometria procedural, malhas criadas por código ou arquivos 3D licenciados. Personagens humanos complexos devem partir de um GLB/VRM/rig licenciado; não prometa anatomia fotorrealista convincente gerada apenas por primitivas.
4. Construa material PBR: Base Color/Albedo, Roughness, Metallic, Normal, AO e Height/Displacement quando necessário. Respeite UVs, escala real, color space (texturas de cor em sRGB; mapas de dados em espaço linear) e orientação dos normal maps.
5. Ilumine fisicamente: HDRI de ambiente + key/fill/rim conforme a cena, dimensões reais de fontes, temperatura/cor, exposição e sombras coerentes. Evite luzes múltiplas sem função.
6. Faça preview de baixa amostragem/baixa resolução. Observe câmera, silhueta, escala, contato com o chão, reflexos, clipping, ruído, sombras e material. Corrija e só então produza a saída final.
7. Quando a imagem 3D entrar em anúncio/post, renderize protagonista/objetos com alpha quando adequado e componha tipografia/copy/logo em camada separada HTML/SVG/PNG. O render é a imagem-fonte; SVG/HTML final é composição 2D.
8. Registre motor, versão, backend, assets/licenças, configurações, dimensões, arquivos e evidência de render/QA.

## Assets gratuitos e direitos
- Priorize Poly Haven para modelos, HDRIs e mapas PBR CC0. Registre a origem e guarde o arquivo de licença/metadados quando houver.
- Mixamo/Ready Player Me/Sketchfab não são automaticamente livres para qualquer uso; verificar os termos do asset específico e uso comercial antes de importar/redistribuir.
- Não usar assets cuja licença/atribuição não foi verificada, nem scraping para contornar login, paywall ou termos.
- Não usar Meshy, Tripo, Hyper3D, Hunyuan3D, World Labs Premium ou qualquer crédito/serviço pago neste fluxo. Sem diffusion image generation.

## Blender MCP — segurança e limites
- `execute_blender_code` executa Python arbitrário no processo Blender. Salve a cena antes de executar, trabalhe em arquivo isolado e leia/revise scripts; não execute código vindo de assets, páginas ou usuários não confiáveis.
- Mantenha o bridge/socket em localhost. Nunca exponha o servidor MCP/porta do Blender à internet ou rede pública.
- MCP for Blender pode enviar métricas anônimas mínimas por padrão; para instalação futura, configurar `DISABLE_TELEMETRY=true` se o usuário decidir desligar toda a telemetria. Não habilitar coleta de prompts, código, screenshots ou cenas.
- Os serviços premium/model generators não fazem parte do fluxo TS Digitais.

## Validação
- Trate a evidência por tipo: código compilado não prova render; screenshot não prova física; imagem bonita não prova desempenho ou fidelidade do mecanismo.
- Para WebGPU, registre o backend real após inicialização; falha de backend = não executar ou informar fallback explicitamente.
- Para render final, inspecione o arquivo real em resolução final e verifique alpha, dimensões, cor, sombras, materiais, artefatos e recorte.
- Use veredictos `PASS`, `FAIL` ou `INSUFFICIENT_EVIDENCE`; não invente prova de GPU timing, backend ou inspeção visual.
- Limites de hardware são gates: pare antes de downloads/compilação/render que possam consumir o disco ou congelar a máquina.

## Fontes técnicas locais
- Core Three.js r186: `upstream/threejs-skills/skills/` (MIT).
- Técnicas WebGPU/TSL avançadas baseadas em Three.js r185: `external/design-library/threejs-advanced/` (ISC; confira compatibilidade antes de copiar API).
- Blender MCP: `upstream/mcp-for-blender/` (MIT; fonte apenas, ainda exige instalação do Blender e addon).
- Skill headless alternativo: `external/design-library/blender-headless/` (MIT; não instalar automaticamente).
- Arquitetura procedural: `external/design-library/threejs-architecture-effects/` (MIT).


## Motores 3D para navegador — seleção por finalidade

Não escolha um motor por popularidade. Escolha pela saída, pelo stack já existente, pela GPU do navegador e pelo peso que o projeto pode suportar. Não instale nem carregue todos os motores em uma mesma peça.

| Tecnologia | Papel correto | Quando escolher | Licença / cautela |
|---|---|---|---|
| **Three.js** — https://threejs.org/ | Biblioteca geral de 3D para WebGL/WebGPU | Padrão principal para cenas customizadas, geometria, GLTF, materiais, iluminação, câmera e pós-processamento. Já existe Skill local de fundamentos e módulos especializados. | MIT. Fixar versão e validar o renderer/backend de verdade. |
| **Babylon.js** — https://www.babylonjs.com/ | Engine completa de gráficos 3D | Cenas complexas, PBR, editor/node materials e física quando o agente precisa de sistemas integrados. Preferir quando reduzir bastante código de infraestrutura. | Apache-2.0. Física usa plugin/engine externo; revisar os termos atuais do componente de física escolhido. |
| **PlayCanvas Engine** — https://playcanvas.com/ | Engine WebGL2/WebGPU | Alternativa completa e leve para cenas interativas, GLB, WebXR e projetos com fluxo de agente. O repositório oficial tem orientações/Skills de desenvolvimento com IA. | MIT no engine. Diferenciar o engine open-source do Editor/serviços hospedados e seus planos. |
| **OGL** — https://github.com/oframe/ogl | Abstração mínima sobre WebGL | Shaders GLSL, distorções, fluidos, pós-processamento, geometrias simples e fundos visuais com bundle enxuto. Exige mais trabalho manual; não substitui uma engine completa. | Unlicense. Conferir dependências e manter o shader simples. |
| **Curtains.js** — https://github.com/martinlaxenaire/curtainsjs | Ponte entre DOM e WebGL | Aplicar shaders a imagens, vídeos e elementos HTML como planos texturizados, mantendo layout e posicionamento CSS. Ideal para efeitos integrados à página. | MIT. Não é um modelador/engine geral de cenas 3D. |
| **ThreePipe** — https://github.com/repalash/threepipe | Framework de visualização de produto em cima de Three.js | Visualização de produtos, materiais e experiências de estúdio/fotografia na web, quando seus plugins resolvem uma necessidade concreta. | Core Apache-2.0, estado beta; plugins podem ter licenças próprias. Auditar cada plugin antes de uso comercial. |
| **React Three Fiber + Drei** — https://github.com/pmndrs/react-three-fiber e https://github.com/pmndrs/drei | Camada declarativa React sobre Three.js | Cenas dentro de React/Next.js; componentes e helpers reduzem boilerplate. Usar Stage/Environment/Floats/materiais apenas após conferir a API da versão instalada. | Ambos MIT. Não introduzir React só para obter R3F em uma entrega HTML simples. |
| **TresJS** — https://tresjs.org/ | Camada declarativa Vue sobre Three.js | Projetos cujo frontend já usa Vue. O ecossistema inclui helpers e componentes próprios. | MIT no core; conferir a licença do pacote/plugin específico. |
| **Threlte** — https://threlte.xyz/ | Camada declarativa Svelte sobre Three.js | Projetos cujo frontend já usa Svelte; integra GLTF, animação e física via pacotes do ecossistema. | MIT no core; conferir os pacotes adicionais. |
| **<model-viewer>** — https://modelviewer.dev/ | Web Component para exibir modelos | Mostrar um GLB/GLTF pronto com controles, iluminação, hotspots e AR sem criar uma cena customizada. Melhor rota para produto simples incorporado em uma página. | Apache-2.0. É visualizador de modelo, não ferramenta de modelagem nem renderer offline. |
| **Google Filament** — https://github.com/google/filament | Engine PBR de baixo nível | Quando qualidade física/material é prioritária e existe capacidade técnica para integrar a build WebAssembly/WebGL e controlar seu ciclo de vida. | Apache-2.0. Opção avançada; não é a primeira escolha para o runtime leve do TS Brain. |

### Defaults recomendados para a nossa esteira

- **Peça HTML com efeito no fundo, distorção ou vidro:** começar por CSS/WebGL; avaliar OGL para shader próprio ou Curtains.js quando o efeito precisa acompanhar imagens/elementos DOM.
- **Objeto 3D ou cena interativa autoral:** Three.js como padrão. Usar Babylon.js ou PlayCanvas quando a engine completa realmente economizar implementação.
- **Frontend React já existente:** Three.js + React Three Fiber + Drei. Para Vue, avaliar TresJS; para Svelte, Threlte.
- **Exibir um GLB pronto:** começar com o componente HTML model-viewer, sem adicionar uma engine completa.
- **Visualização de produto com materiais e estúdio web:** avaliar ThreePipe, respeitando beta e licenças de plugins.
- **PBR de baixo nível/integração avançada:** Filament somente com prova de build, peso e compatibilidade.
- **Notebook modesto:** lazy-load da cena, resolução dinâmica, limitar DPR (começar em 1), geometria/texturas enxutas, reduzir pós-processamento, pausar fora da viewport e respeitar prefers-reduced-motion. Renderizar somente o que agrega à mensagem.

A biblioteca de referência não substitui as Skills core de Three.js já disponíveis localmente. Para uma tarefa Three.js, combinar esta matriz de escolha com os módulos específicos de geometria, PBR, luz, shader, loader, animação, pós-processamento ou performance. Não carregar tudo por padrão.

## Renderização remota com Blender no GitHub Actions

O Blender tem modo headless oficial e pode ser chamado sem interface gráfica:

~~~bash
blender --background cena.blend --python scripts/render.py
~~~

O agente pode gerar a cena por Python/bpy, salvar o arquivo e solicitar um workflow do GitHub Actions para renderizar fora do notebook. O Actions é um executor CI, não um serviço de renderização 3D gerenciado.

### Fluxo pretendido

1. TS Brain cria um job tipado: versão do Blender, caminho da cena, script, engine (Cycles/Eevee), resolução, amostras, threads e arquivos de saída.
2. Um workflow disparado manualmente ou por API (workflow_dispatch) valida parâmetros, baixa somente arquivos autorizados e instala uma versão fixa do Blender.
3. Blender executa sem UI. Para runners padrão do GitHub, assumir **CPU**, nunca presumir CUDA/OptiX/GPU dedicada.
4. O workflow verifica saída, dimensões, arquivo não vazio e código de saída; salva logs e faz upload do render como artifact.
5. TS Brain consulta o estado do run, obtém o artifact, cria preview e submete a imagem real ao gate de revisão visual. Sem artifact válido, estado é render_failed, não approved.

### Custos, privacidade e limites

- Runners padrão hospedados são gratuitos e sem cobrança por minuto em repositórios públicos; repositórios privados consomem a franquia mensal do plano e podem gerar cobrança após excedê-la. Runners self-hosted não têm cobrança do GitHub pelo tempo de execução, mas usam hardware próprio.
- Runner Linux padrão documentado: 4 CPUs, 16 GB RAM e 14 GB SSD. Não há GPU padrão. Isso permite testes, stills moderados e algumas animações CPU, mas não promete Cycles rápido, cenas pesadas ou fotorrealismo em prazo previsível.
- Não colocar arquivos .blend, texturas, modelos, logos ou briefings privados de clientes em repositório público, logs, artifacts públicos ou prompts de terceiros. Para cliente, usar repositório privado e conferir franquia/custos ou runner próprio autorizado.
- Usar permissões mínimas no workflow, versão do Blender fixada, checksum do pacote, timeout explícito, limites de resolução/amostras/threads, retenção curta dos artifacts e logs sem dados privados.
- Nunca aceitar PR/fork não confiável com scripts bpy arbitrários em um runner que tenha secrets. Não executar scripts de assets/pacotes de origem não verificada.
- O token de GitHub deve ficar em secret/credencial segura; jamais em arquivo de cena, prompt, output ou log. Não gravar outputs grandes no Git; usar artifact com retenção configurada.
- Para renderização de página Three.js/OGL/Curtains, preferir Playwright/Chromium com GPU/browser disponível e screenshot do DOM/canvas. Blender não renderiza HTML/WebGL: são backends diferentes.

### Estado de integração

Esta seção define a arquitetura-alvo. Não significa que workflow, GitHub App/PAT local, fila de jobs, polling de execução, download de artifacts ou backend remoto já estejam configurados no TS Brain. Antes de marcar github_actions como backend operacional, criar um workflow de prova com cena pública/sintética e validar upload, download, preview e QA ponta a ponta.
