# Pesquisa — engenharia de prompts, tipografia, camadas e MCPs de imagem

**Revisão:** 23/11/2026  
**Objetivo:** avaliar as sugestões trazidas pelo usuário, separar skills de execução MCP e escolher o que agrega ao stack gratuito/reutilizável da TS Digitais.

## Conclusão operacional

A lacuna não era ausência total de ferramentas. O submódulo upstream/social-media-skills já continha skills/image-prompt, com brief visual, prompt anatomy, espaço negativo e roteamento por tipo de imagem; também contém carousel-writer/references/image-prompt-pack.md. O fluxo social, porém, ainda não convocava a skill de imagem e não exigia que a copy literal, a tipografia e os planos de profundidade fossem entregues juntos.

Foi criado layered-image-prompting/SKILL.md e o perfil agents/image-prompt-art-director.md para preencher essa lacuna. O módulo reúne:
- Foreground, midground e background como planos espaciais, com localização, escala, foco, oclusão e função.
- Hierarquia tipográfica, categorias de fonte, peso, proporção, quebras, tracking, leading, contraste e safe zones.
- Copy literal dentro do próprio prompt, com modo native, editable ou hybrid.
- Camadas gráficas distintas dos planos fotográficos.
- Um bloco único copiável para todos os prompts de carrossel, mas uma imagem independente por slide.
- QA do texto renderizado e da composição final.

## Avaliação das sugestões

| Sugestão | Identificação / evidência | Decisão |
|---|---|---|
| Composition Techniques (SKILL.md) | O texto descreve uma categoria de skill, mas não trouxe URL ou repositório identificável. A TS já tem composition-framework/SKILL.md, orientada a composição codificada, camadas z-index, assets 3D, glassmorphism e componentes. Não equivale a um método de prompt fotográfico. | Não instalar algo sem origem. Aproveitar o conceito, mas criar skill local específica para cena e prompt. A composition-framework recebeu uma nota de escopo para não aplicar efeitos de UI a fotos automaticamente. |
| Image Prompt Engineer | Fonte concreta encontrada: Fei2-Labs/skill-genie/skills/image-prompt-engineer/SKILL.md, licença MIT. Traz sequência de assunto, composição/câmera, materiais, ambiente, luz, estilo e parâmetros; é fortemente orientada a Midjourney, com escolhas versionadas. | Consultada como referência comparativa. Não instalada separadamente porque já temos skill social image-prompt e a skill mcp-image, que são mais adequadas a fluxo multi-modelo e copy em português. Não assumir seus defaults de Midjourney sem documentação atual. |
| Claude-Kit Image-Gen Skill | O nome exato não permitiu identificar um repositório com certeza. Foi encontrado um projeto semelhante, Cleveland-RD/claude-image-gen, MIT, com plugin de skill + MCP de geração para GPT Image e Gemini, exigindo chaves próprias. Não é possível afirmar que seja o item exato citado. | Não instalar como se fosse a mesma sugestão. O projeto semelhante duplica os motores de imagem existentes e acrescenta chamadas de API pagas; reavaliar somente se o usuário fornecer o link exato ou se houver necessidade real de conectar essas APIs. |
| shinpr/mcp-image | Repositório público, MIT. Inclui skills/image-generation/SKILL.md independente do servidor. O servidor gera/edita com Gemini, OpenAI ou Seedream, aceita texto literal, purpose, category, aspectRatio e imageSize. Requer Node.js e chave de um provedor externo. | Incorporar os princípios da skill de prompt na skill local, sem instalar o servidor agora. A chave/API geradora implicaria custos de uso; nosso ambiente já possui geradores e ferramentas conectadas. |
| z23cc/MJ-MCP / z23cc/midjourney-mcp | O README de MJ-MCP aponta para AICloud e compra de créditos; declara MIT no badge, mas o arquivo LICENSE não foi encontrado no caminho consultado. O outro repositório usa GPTNB API com base aiclound.vip e declara GPL-3.0 no README. | Não instalar. São wrappers de terceiros, não integração oficial Midjourney. A documentação oficial atual informa que não há API pública e proíbe automação por ferramentas externas; usar pode gerar risco de conta. |
| RunAPI MCP | runapi-ai/mcp, Apache-2.0. Oferece catálogo, busca de prompts e consulta de preços sem login; criar tarefas e gerar mídia requer login/saldo no serviço RunAPI. | Não instalar agora: não melhora a engenharia da copy/layout, é uma camada comercial de execução e sobrepõe geradores existentes. Poderá ser avaliado depois como catálogo/preço se houver necessidade multi-modelo. |

## Distinção importante: cenas vs camadas de layout

- Foreground / midground / background descrevem profundidade dentro do espaço da imagem: elementos próximos, sujeito principal e contexto distante.
- Z-index/camadas gráficas descrevem sobreposição de fotografia, overlays, máscaras, formas, tipografia, botões e logo.
- Não se deve confundir os dois nem adicionar foreground artificial só para cumprir uma lista.
- composition-framework local é mais útil para páginas, HTML/SVG e composições com componentes; não deve forçar glassmorphism, 3D, gradientes múltiplos e cards em prompts fotográficos.

## Texto dentro de imagens

A skill image-generation do mcp-image recomenda copy literal entre aspas e especificação da tipografia e posicionamento. Mesmo assim, nenhum prompt substitui a inspeção visual: a renderização de texto pelo modelo pode falhar. Para copy comercial exata ou master editável, manter também SVG/Figma/Canva com texto separado em camadas.

## Fontes

- Social Media Skills (MIT): https://github.com/social-media-skills/skills/tree/main/skills/image-prompt
- Carousel Image Prompt Pack (MIT): https://github.com/social-media-skills/skills/tree/main/skills/carousel-writer/references/image-prompt-pack.md
- mcp-image (MIT): https://github.com/shinpr/mcp-image
- mcp-image prompt skill: https://github.com/shinpr/mcp-image/blob/main/skills/image-generation/SKILL.md
- Image Prompt Engineer (MIT): https://github.com/Fei2-Labs/skill-genie
- Cleveland-RD claude-image-gen (MIT, identificação apenas como possível semelhante): https://github.com/Cleveland-RD/claude-image-gen
- z23cc/MJ-MCP: https://github.com/z23cc/MJ-MCP
- z23cc/midjourney-mcp: https://github.com/z23cc/midjourney-mcp
- RunAPI MCP (Apache-2.0): https://github.com/runapi-ai/mcp
- Midjourney Terms of Service: https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service
- Midjourney FAQ source: https://github.com/midjourney/docs/blob/main/data/faq.txt
