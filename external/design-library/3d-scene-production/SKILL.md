---
name: tsdigitais-3d-scene-production
description: "Roteia e especifica cenas 3D reais por código, com geometria, câmera, iluminação, materiais PBR, personagens/objetos, render e QA. Use em qualquer pedido 3D, fotorrealismo, Blender, Three.js, WebGPU, Cycles, HDRI, GLB, VRM ou visualização de produto/arquitetura."
---

# Produção de cenas 3D — TS Digitais

## Contrato
Produza 3D real, não uma imagem 2D simulando volume. O caminho padrão é geometria e materiais em Blender ou Three.js; **não use geradores de imagem por difusão**. Não chame serviços pagos de geração de malha.

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
