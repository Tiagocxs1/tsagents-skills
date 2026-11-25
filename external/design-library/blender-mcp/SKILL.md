---
name: tsdigitais-blender-mcp
description: "Cria, controla, valida e exporta cenas Blender por Python bpy via MCP, quando o Blender e o addon estiverem realmente instalados e conectados. Use para Cycles, Eevee, render offline, objetos, materiais PBR, luz, câmeras, GLB e PNG com alpha."
---

# Blender MCP — adaptador TS Digitais

Esta Skill descreve o contrato de integração, não instala nem inicia automaticamente o servidor.

## Pré-requisitos operacionais
- Blender 3.0+ instalado no host que renderiza; validar versão e binário real.
- Python/uv e pacote MCP compatível com o cliente escolhido.
- Addon MCP for Blender instalado e habilitado no Blender, ou modo headless suportado pelo servidor escolhido.
- Verificar handshake MCP e ferramentas expostas antes de marcar como conectado.
- O servidor `ahujasid/mcp-for-blender` requer Blender addon ativo; o MCP sozinho não substitui Blender.
- Alternativa `sandraschi/blender-mcp` oferece modo `blender --background`, mas seu README atual declara Python 3.13+ e o host deste projeto foi encontrado com Python 3.12.3; não presumir compatibilidade sem ambiente isolado.

## Procedimento
1. Confirmar espaço livre, RAM, binário e versão do Blender. Não instalar nem renderizar em máquina sem capacidade.
2. Criar um `.blend` novo de trabalho; nunca sobrescrever a cena original sem backup.
3. Construir cena via `bpy`: unidades, mesh/curvas, UV, câmera, luzes, nodes de material, compositor e configurações do motor.
4. Usar Cycles para imagem de alta qualidade quando o host for capaz; Eevee/viewport para iteração e previews.
5. Importar somente modelos/texturas/HDRIs com licença confirmada. Priorizar Poly Haven CC0.
6. Renderizar primeiro preview; inspecionar imagem/câmera. Ajustar exposição, roughness, normal, escala, sombras, DOF e composição.
7. Renderizar PNG/TIFF/EXR ou sequência. Quando apropriado, configurar RGBA e film transparency para transparência real.
8. Guardar script, `.blend`, saída, logs e resumo de assets/configuração.

## Segurança
- A ferramenta `execute_blender_code` executa Python arbitrário. Revisar código, salvar antes, limitar paths de leitura/escrita a diretório do job e nunca executar código embutido em asset externo sem inspeção.
- Servidor de rede só em localhost; não habilitar bind remoto sem autenticação e túnel seguro.
- Sem serviços premium, API keys, geração de malha paga ou diffusion.
- Marcar o MCP como desconectado até teste real de listagem de ferramentas e execução de uma cena de prova.
