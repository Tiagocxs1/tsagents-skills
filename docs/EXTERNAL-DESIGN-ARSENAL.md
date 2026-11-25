# Arsenal externo de Design, Conteúdo e Agents — 24/11/2026

Este catálogo registra os 15 repositórios solicitados, com commit fixado, licença verificada, classificação, disponibilidade e limites operacionais. Os originais ficam em `upstream/` como Git submodules, separados das adaptações da TS Digitais.

**Não execute `git submodule update --init --recursive` indiscriminadamente.** Os repositórios OpenDesign, AiToEarn e 350 Layout Compositions são grandes; seus ponteiros estão no Git, mas os arquivos binários não foram baixados. Yingzao é link-only por falta de licença identificada.

Machine-readable registry: [`external/design-library/registry.json`](../external/design-library/registry.json).
Router Skill: [`external-design-library-router/SKILL.md`](../external-design-library-router/SKILL.md).
Layout index: [`external/design-library/data/350-layout-catalog.csv`](../external/design-library/data/350-layout-catalog.csv).

## Repositórios e decisões

| # | Projeto | Licença observada | Classe | Estado nesta branch |
|---:|---|---|---|---|
| 1 | [Guizang Social Card](https://github.com/op7418/guizang-social-card-skill) | AGPL-3.0 | Skill para carrosséis, capas WeChat e Live Photo | Checkout local; roteável |
| 2 | [OpenDesign](https://github.com/nexu-io/open-design) | Apache-2.0 | Workspace/aplicação de design | Submodule pointer; não baixado (≈3,5 GB) |
| 3 | [LangChain Design Agent](https://github.com/langchain-ai/design-agent) | Apache-2.0 na raiz; NOTICE separa componentes | Aplicação + Skills | Checkout local; 10 Skills selecionadas roteáveis; Managed Deep Agents não instalado |
| 4 | [Huashu Design](https://github.com/alchaincyf/huashu-design) | MIT | Skill de protótipos HTML, slides, motion, infográficos e crítica | Checkout local; roteável |
| 5 | [ogimagecn](https://github.com/shadcn-labs/ogimagecn) | MIT | Biblioteca React/Satori para OG images | Código local + wrapper Skill `ext-ogimagecn-code`; ainda não é renderer/MCP |
| 6 | [Open Carrusel](https://github.com/Hainrixz/open-carrusel) | MIT | Aplicação Next.js independente para carrosséis | Submodule pointer; não lançada nem autenticada |
| 7 | [Guizang PPT](https://github.com/op7418/guizang-ppt-skill) | AGPL-3.0 | Skill para decks HTML estilo editorial/Swiss | Submodule existente e checkout local; roteável |
| 8 | [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | MIT | Skill editorial em chinês | Checkout local; usar somente em texto chinês |
| 9 | [DSh Guizang Design](https://github.com/op7418/dsh-guizang-design) | AGPL-3.0 | Plugin DeepSeek Harness que agrupa Skills | Submodule pointer; referência apenas, evita duplicar originais |
| 10 | [Agent Reach](https://github.com/Panniantong/Agent-Reach) | MIT | CLI/Skill de pesquisa pública somente leitura | Skill local; CLI não instalado, canais não autenticados |
| 11 | [AiToEarn](https://github.com/yikart/AiToEarn) | MIT | Plataforma de conteúdo/monetização e MCP remoto | Submodule pointer; MCP desativado, sem API key |
| 12 | [Mono Color Skill](https://github.com/yanliudesign/mono-color-skill) | MIT para Skill/código; imagens de referência têm termos separados | Skill editorial one-ink/two-ink | Checkout local; roteável, assets de terceiros não redistribuídos |
| 13 | [Diagram Design](https://github.com/cathrynlavery/diagram-design) | MIT | Skill para 52 tipos de diagramas | Checkout local; roteável |
| 14 | [350 Layout Compositions](https://github.com/nevertoday/350-layout-compositions) | CC BY 4.0 | Biblioteca de referências de composição | Submodule pointer; CSV de 350 registros disponível; imagens grandes não baixadas |
| 15 | [Yingzao](https://github.com/op7418/guizang-yingzao-skill) | Não foi encontrado LICENSE no root | Skill de cartaz editorial a partir de fotos | Apenas link; sem cópia, distribuição ou carregamento até esclarecer os direitos |

Todos os commits e caminhos completos estão no registry JSON. A branch mantém as origens em submodules separados e não altera os arquivos dos autores.

## O que o LangGraph/LangChain consegue carregar

A camada `ts_brain.agent_registry` foi preparada para ler nomes de Skills do catálogo e carregar apenas o `SKILL.md` selecionado, a partir do checkout local em `upstream/`. O grafo `agency-creative` escolhe no máximo duas Skills externas por tarefa, usando palavras-chave do briefing; o texto só entra no prompt quando a política do provider permite.

Rotas configuradas:
- Social/carrossel → Guizang Social Card.
- PPT/deck → Guizang PPT +, quando necessário, Slideshow do LangChain Design Agent.
- Design/protótipo geral → Huashu Design + Brand Design do Design Agent.
- Monocromia/one-ink/two-ink → Mono Color.
- Diagramas e fluxos → Diagram Design; gráficos podem adicionar Data Viz.
- Motion/storyboard → Motion Direction/Storyboard do Design Agent.
- Pesquisa/read de links → Agent Reach, respeitando a política read-only.
- Texto chinês → Humanizer-zh. Não usar para português ou espanhol.

OpenDesign, Open Carrusel, ogimagecn, AiToEarn, DSh Guizang e o conjunto de 350 composições são aplicações/bibliotecas/coleções; não são todos Skills invocáveis. Estão catalogados para referência ou uso futuro específico, mas não foram apresentados falsamente como ferramentas MCP conectadas.

## Limite de privacidade do provider atual

**O NVIDIA Nemotron ativo no TS Brain não recebe conteúdo destas Skills externas.** O runtime continua enviando apenas descrições genéricas de papéis e tarefas públicas/sintéticas. Os arquivos de Skill, perfis privados, referências locais e memória Obsidian permanecem no PC. Esta integração não altera a barreira de privacidade existente.

O carregamento de Skill em prompt externo só é possível com outro provider e a opção de divulgação privada já existente, após verificar termos e consentimento. Gemini segue desativado; OpenRouter não foi considerado operacional. Não ativar outro provider só para contornar esta política.

## Segurança, publicação e contas

- Agent Reach é leitura: não publicar, comentar, curtir, enviar DMs nem contornar rate limits. A instalação de canais, login e qualquer sincronização de sessão permanecem manuais e autorizados pelo usuário.
- AiToEarn tem capacidade de publicação/gestão de contas. Seu MCP fica desabilitado até revisão de permissões por conta, chave/API, custos e confirmação de cada escrita. Não há credencial configurada.
- OpenDesign pode enviar métricas e conteúdo de conversas/ferramentas à PostHog, conforme os controles de privacidade. Não iniciar a aplicação sem rever e desligar os fluxos opcionais de telemetria.
- Diagram Design não possui backend/analytics próprios segundo seu PRIVACY.md, mas as fontes do Google Fonts expõem IP, navegador e página referenciadora ao Google. Pode-se substituir por fontes locais/sistema.
- Humanizer-zh é específico para chinês.
- Imagens de referência da Mono Color não são cobertas automaticamente pela licença MIT do código.
- O dataset 350 Layout exige crédito, link CC BY 4.0 e indicação de alterações. Não incorporar as imagens como assets de marca; usar composição como referência.
- Yingzao permanece apenas como link porque não foi encontrada licença de redistribuição.

Nenhum post foi publicado, nenhuma conta conectada, nenhum login realizado e nenhuma API key criada.

## Recuperar submodules de forma seletiva

Para baixar somente Skills/aplicações leves necessárias:

```bash
cd /caminho/tsagents-skills
git submodule update --init --depth 1 upstream/guizang-social-card-skill upstream/guizang-ppt-skill upstream/huashu-design upstream/diagram-design upstream/mono-color-skill upstream/agent-reach
```

Para OpenDesign, AiToEarn, Open Carrusel e o dataset inteiro de 350 layouts, só inicializar o submodule depois de uma decisão específica. Não usar `--recursive` para todos.

## Uso local pelo TS Brain

O runtime consulta o registry em `external/design-library/registry.json` e os paths em `upstream/`. Verifique com:

```bash
cd /home/tiago/meu-agente
.venv/bin/python -m ts_brain.cli skills --all
.venv/bin/python -m ts_brain.cli skills --name ext-huashu-design
```

A disponibilidade é por checkout local. Ter um ponteiro de Git submodule no catálogo não quer dizer que os arquivos foram baixados, as dependências instaladas ou o app/MCP autenticado.


## Estado final da integração LangGraph/LangChain — 24/11/2026

O registry contém 15 fontes e agora disponibiliza **19 IDs carregáveis**: as Skills autênticas, 10 Skills selecionadas de LangChain Design Agent e os wrappers locais de OG image e 350 Layouts. O índice 350 é consultável por metadados, sem carregar as imagens de referência.

`agent_registry.py` lê apenas o manifesto local e resolve paths que permanecem dentro do checkout do repositório. O seletor usa os gatilhos do briefing e limita a escolha a duas Skills. `agency_graph.py` chama esse seletor na etapa de direção; o CLI `skills --sources` apresenta licenças e estados; a bridge envia apenas metadados sanitizados.

Os testes finais do runtime passaram: 11/11, incluindo roteamento social/PPT/OG/layout, busca do catálogo 350, carregamento local e garantia de que nem Skills privadas nem memória aparecem no prompt NVIDIA. `pip check` sem dependências quebradas.

A integração não autentica sites, não ativa MCP de publicação e não instala serviços externos. NVIDIA permanece com a política de não receber texto das Skills externas.

## Especialização 3D e revisão de interface — 25/11/2026

Foram acrescentadas oito fontes/coleções ao registro: quatro fontes para produção 3D, Anatomy, Impeccable e duas coleções técnicas (core Three.js e avançada). Os originais preservados por submodule e as adaptações compactas continuam separados.

| Projeto | Licença | Escopo | Estado real |
|---|---|---|---|
| [MCP for Blender](https://github.com/ahujasid/mcp-for-blender) | MIT | Blender Python, cena, materiais, câmera/luz, inspeção e exportação | Fonte local; Blender/addon/MCP não instalados nem conectados |
| [Blender MCP headless](https://github.com/sandraschi/blender-mcp) | MIT | Referências para batch/headless, exports e automação | Duas Skills selecionadas; sem servidor instalado; requer Python 3.13+ no README atual |
| [CloudAI-X Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | MIT | Fundamentos r186, PBR, luz, texturas, rigging, GLTF, TSL, pós e performance | Submodule fonte + 13 wrappers locais de roteamento |
| [Three.js Complete Set](https://github.com/linegel/threejs-complete-set-of-skill) | ISC | WebGPU/TSL avançado, materiais PBR, geometria, criaturas, arquitetura, sombras e validação | 10 Skills selecionadas e referências; upstream documenta r185, confirmar compatibilidade |
| [Three.js Architecture Effects](https://github.com/lhlGitHub/threejs-architecture-effects) | MIT | Arquitetura procedural interativa e animação de montagem | Skill, references e scaffold copiados; aplicação não iniciada |
| [Anatomy](https://github.com/wheresryan22/anatomy) | MIT | Ilustração técnica isométrica densa, SVG, WebGL e peças móveis 3D | Submodule local e Skill completa disponível; Node compatível ainda não disponível no host |
| [Impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 | Direção/revisão de UI, critique, audit, polish, responsividade e detector | Skill + 16 referências selecionadas; repo integral (~933 MB), CLI, hooks, Live mode e engine não instalados |
| [TS Digitais 3D Scene Production](../external/design-library/3d-scene-production/SKILL.md) | Guia first-party | Roteia Blender/Three.js, PBR, licenças, QA e política sem diffusion | Local e roteável pelo TS Brain |

### Rotas práticas

- Still cinematográfico/produto transparente → Blender + bpy/Cycles quando houver host apto.
- Cena interativa/configurador/arquitetura web → Three.js WebGPU/TSL, validando o backend real após inicialização.
- Ilustração técnica isométrica de máquinas/equipamentos → Anatomy; não é render PBR geral nem ferramenta para retratos humanos.
- Revisão de site/landing/dashboard → Impeccable; não é uma skill de render 3D.
- Peça publicitária com protagonista 3D → render com alpha + composição e tipografia HTML/SVG em camadas separadas.

### Restrições e situação do host

Não usar diffusion nem serviços pagos de geração de malha. Blender MCP permite execução de Python arbitrário: requer scripts revisados, arquivo de trabalho isolado e localhost. Desativar telemetria do MCP se instalado, conforme a política e a decisão do usuário.

Verificação em 25/11/2026: Blender ausente; Python 3.12.3; Node.js do sistema 18.19.1 (Anatomy pede >=20.10; starter da arquitetura Three.js pede >=22.13); Chrome presente; disco 99% ocupado (~2.2 GB livres), pouca RAM disponível. Portanto nenhum renderizador está ativo/conectado e nenhum render foi executado nesta etapa. Não instalar nem inicializar render pesado antes de liberar espaço e preparar host compatível.

O catálogo atual passa a incluir 23 fontes e 49 entrypoints. O seletor local limita tarefas 3D a até três Skills e tarefas normais a duas. Para NVIDIA, a barreira permanece: conteúdo de Skill externo, perfis e memória Obsidian não são enviados ao provider; a execução usa somente briefing público/sintético e papéis genéricos.
