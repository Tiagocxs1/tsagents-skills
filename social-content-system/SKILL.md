---
name: social-content-system
description: Orquestra pesquisa, estratégia editorial, copywriting, calendário, direção criativa e mensuração de conteúdo social para qualquer marca. Ativar antes de criar ou revisar calendários, pautas, Stories, carrosséis, Reels e campanhas orgânicas.
---

# Social Content System — TS Digitais

Sistema reutilizável e independente de marca para transformar contexto de negócio e evidências de audiência em conteúdo social específico, útil, distinto e mensurável.

## Princípio central

Não começar pelo calendário nem por frases de efeito. Começar pela marca, pelos públicos, pelos problemas reais e pelas provas disponíveis. Skills e agentes especializados devem melhorar decisões editoriais; não produzir volume por volume.

## 1. Resolver o contexto da marca

Para uma marca chamada <slug>, consultar nesta ordem:

1. brands/<slug>/BRAND-PROFILE.md — identidade, serviços, públicos, geografia, provas, claims e restrições.
2. brands/<slug>/SOCIAL-CONTENT-GUIDELINES.md — tom, pilares e regras específicas de redes sociais.
3. Brand Kit, logo, fontes, fotos, campanhas e conteúdos anteriores em fontes autorizadas.
4. Se existirem: AUDIENCE-RESEARCH.md, SOCIAL-STRATEGY.md, CONTENT-PILLARS.md, histórico editorial e métricas.

Se faltar uma informação, não assumir que ela existe. Usar o que estiver confirmado, marcar hipóteses e pedir apenas o dado indispensável. Não copiar a estratégia ou a identidade de uma marca para outra.

## 2. Skills upstream obrigatórias por etapa

Os originais estão preservados no submódulo MIT upstream/social-media-skills/, fixado pelo commit do repositório principal. Consultar somente os módulos pertinentes:

| Etapa | Skill original |
|---|---|
| Público e linguagem real | upstream/social-media-skills/skills/audience-research/SKILL.md |
| Concorrentes e espaço editorial | upstream/social-media-skills/skills/competitor-analysis/SKILL.md |
| Fontes e checagem de fatos | upstream/social-media-skills/skills/content-research-and-sourcing/SKILL.md |
| Estratégia e canais | upstream/social-media-skills/skills/social-strategy/SKILL.md |
| Temas proprietários | upstream/social-media-skills/skills/content-pillars/SKILL.md |
| Cadência recorrente | upstream/social-media-skills/skills/content-calendar/SKILL.md |
| Plano de período e briefs | upstream/social-media-skills/skills/batch-content-plan/SKILL.md |
| Datas e momentos relevantes | upstream/social-media-skills/skills/seasonal-and-moment-marketing/SKILL.md |
| Conteúdo educativo | upstream/social-media-skills/skills/educational-content-and-how-to/SKILL.md |
| Narrativa | upstream/social-media-skills/skills/storytelling-and-narrative/SKILL.md |
| Hooks | upstream/social-media-skills/skills/hook-writer/SKILL.md |
| Legendas | upstream/social-media-skills/skills/caption-writer/SKILL.md |
| Carrosséis | upstream/social-media-skills/skills/carousel-writer/SKILL.md |
| Stories | upstream/social-media-skills/skills/story-writer/SKILL.md |

Complementos do submódulo upstream/marketing-skills-corey/: skills/content-strategy/SKILL.md, skills/customer-research/SKILL.md, skills/copywriting/SKILL.md e skills/social/SKILL.md. Usar como segunda opinião para estratégia/copy, não como substituto do brief da marca ou das skills específicas de formato.

Não carregar todos os módulos em todas as tarefas. Abrir os arquivos exatos da etapa que está sendo executada. Em clone novo, inicializar com git submodule update --init --recursive.

## 3. Ordem de trabalho

### A. Pesquisa
O agente social-intelligence-researcher.md pesquisa audiência, perguntas, objeções, linguagem, concorrentes e fontes. Saída: evidências, lacunas e oportunidades — com URLs, datas e nível de confiança. Fontes públicas apenas; nunca contornar acesso ou usar dados pessoais/sensíveis para segmentação.

### B. Estratégia
O agente social-content-strategist.md define objetivo primário de negócio, públicos/decisores, posicionamento editorial, pilares (temas, não formatos), mix de intenção, canais e cadência compatível com capacidade.

### C. Pautas e calendário
Selecionar pautas que respondam a uma tensão, pergunta ou tarefa concreta de um público. Alternar públicos, etapas de decisão, pilares, formatos e profundidade. Datas comemorativas só entram se houver aderência real e legitimidade. Cada item recebe um brief completo usando templates/social-post-brief.md.

### D. Copy
O agente social-copywriter.md trabalha hooks por mecanismos diferentes, escolhe o melhor, escreve todos os textos por frame/slide e a legenda, adapta o CTA ao objetivo e remove frases genéricas/automatizadas. A copy deve ser específica, natural e verificável.

**Formato obrigatório dos prompts de imagem:** quando a peça for um carrossel, entregar todos os prompts dos slides dentro de um único bloco de texto copiável, com separadores e identificação `SLIDE 01`, `SLIDE 02` etc. Explicitar que devem ser geradas imagens independentes, não uma colagem/prancha única. Em Stories ou posts avulsos, manter um prompt por imagem quando isso facilitar a geração individual.

### E. Direção visual
Executar visual-design/SKILL.md, social-media-creative/SKILL.md, social-first-art-direction/SKILL.md e typography-master/SKILL.md quando houver texto visual. Para carrosséis, seguir carousel-writer. Para Stories, seguir story-writer. Preservar o Brand Profile da marca. Produzir previews reais e revisar com visual-quality-review/SKILL.md e agents/visual-critic.md.

### F. Mensuração
O agente social-performance-analyst.md compara conteúdo com métricas equivalentes, identifica padrões e propõe experimentos. Não atribuir vendas ou leads sem evidência de origem. Métricas ausentes não podem ser inventadas.

## 4. Definition of Done de cada pauta

Uma pauta só está pronta para produção quando contém:

- Público exato e situação reconhecível.
- Objetivo de negócio ou comportamento esperado.
- Insight, pergunta ou problema específico.
- Ângulo editorial distinto e razão para o público se importar.
- Formato recomendado e justificativa.
- Hook/headline e promessa que o conteúdo efetivamente entrega.
- Estrutura completa de slides/frames ou roteiro.
- Legenda pronta, CTA único e hashtags apenas quando úteis.
- Fontes e claims que precisam de validação, quando aplicável.
- Direção visual e requisitos de assets.
- Status de revisão editorial, factual e visual.

Não entregar apenas títulos de pauta, temas amplos ou frases soltas como se fossem conteúdo pronto.

## 5. Regras de qualidade de copy

- Usar português brasileiro natural e vocabulário do público.
- Uma ideia principal por peça; cada slide/frame avança a narrativa.
- Evitar clichês de IA, slogans vazios, perguntas retóricas em série e fórmulas repetidas.
- Evitar estruturas artificiais como “não é X, é Y” e listas de negações.
- Não usar medo, urgência artificial ou clickbait como substituto de informação.
- Não inventar depoimentos, estatísticas, resultados, credenciais, garantias ou comparações.
- Escrever primeiro para a pessoa e seu contexto; mencionar o serviço apenas quando ele for uma solução pertinente.
- Um CTA específico, proporcional à etapa de decisão.

## 6. Regras para calendário

- Distinguir pilares (assuntos que a marca pode possuir), intenções (educar, conectar, provar, converter), formatos e campanhas.
- Não criar uma grade de datas sem tese editorial.
- Variar ângulos, estruturas, ritmo e composição — não apenas trocar a headline do mesmo template.
- Balancear valor, relacionamento, prova e conversão; não transformar o perfil em catálogo.
- Não inventar “melhores horários”; usar dados da conta quando existirem.
- Registrar pauta, versão da copy, asset, status, data planejada, URL publicada e métricas em histórico versionado.

## 7. Multi-marca e reutilização

Este sistema é neutro de marca. Reutilizar o mesmo processo em qualquer cliente, substituindo somente:
- <slug> e arquivos de marca;
- públicos, serviços, região e provas;
- metas, restrições e canais autorizados;
- exemplos, fontes e linguagem real.

Nunca adicionar informação da Guardian ou de outro cliente aos agentes genéricos. Conhecimento específico deve ficar em brands/<slug>/.

## 8. Aprovação e publicação

Planejar, redigir e preparar arquivos não concede autorização para publicar/agendar. Solicitar aprovação expressa antes de qualquer publicação, agendamento, impulsionamento ou gasto.
