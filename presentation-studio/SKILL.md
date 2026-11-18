---
name: presentation-studio
description: Planejar, produzir e revisar apresentações profissionais em PowerPoint editável, HTML ou Google Slides. Roteia para as ferramentas e skills corretas, preserva a marca e exige validação visual antes da entrega.
---

# Presentation Studio — TS Digitais

Skill de orquestração para apresentações comerciais, institucionais, educacionais, relatórios, pitch decks, propostas e materiais de treinamento. Prioriza ferramentas gratuitas/open-source, formatos editáveis e qualidade visual verificável.

## Consulta obrigatória

Antes de produzir:
1. Ler o AGENTS.md da raiz.
2. Ler visual-design/SKILL.md e visual-quality-review/SKILL.md.
3. Ler docs/PRESENTATION-TOOLING.md para verificar ferramentas, licenças, atualização, custo e instalação.
4. Para estratégia narrativa, consultar slides/references/slide-strategies.md, slides/references/layout-patterns.md e slides/references/copywriting-formulas.md.
5. Se for proposta comercial, ler também commercial-proposal/SKILL.md.
6. Se houver marca de cliente, consultar os arquivos em brands/<slug>/ e usá-los como fonte oficial.

## 1. Definir o formato e o propósito

Distinguir o formato final antes de escolher a ferramenta:
- **PPTX editável:** slides nativos, formas, caixas de texto, gráficos e elementos que o cliente possa alterar.
- **Google Slides:** edição colaborativa na nuvem, comentários e atualização de apresentações existentes.
- **HTML:** apresentação web com animações, navegação e opção de hospedar ou abrir no navegador.
- **PDF:** versão fechada para leitura, envio ou impressão. Não substitui o arquivo-fonte editável quando este foi solicitado.

Se o usuário não tiver especificado o formato e a escolha alterar materialmente a execução, perguntar apenas: “Você prefere PowerPoint editável (.pptx), Google Slides ou HTML para apresentar no navegador?”. Para propostas, oferecer PPTX editável e PDF final como padrão, salvo orientação diferente.

Identificar objetivo, público, contexto, idioma, duração, quantidade aproximada de slides, CTA, dados obrigatórios, fontes e restrições. Reaproveitar toda informação já fornecida; não criar questionário longo.

## 2. Selecionar a estratégia narrativa

Escolher a estrutura conforme a finalidade:
- Venda/proposta: contexto do cliente → problema → impacto → solução → escopo → prova real → investimento → próximos passos.
- Pitch de produto: problema → oportunidade → solução → demonstração → diferencial → modelo → chamada para ação.
- Relatório: objetivo → período/base → indicadores → leitura dos dados → riscos → decisões → plano.
- Treinamento: objetivo de aprendizagem → conceitos → demonstração → prática → síntese.
- Palestra: gancho → contexto → desenvolvimento → mudança de perspectiva → conclusão memorável.

Cada slide deve ter uma função clara e uma mensagem principal. Evitar parágrafos extensos, listas intermináveis e conteúdo repetido entre tela e notas do apresentador. Mostrar dados com gráficos quando existir uma série real e legível; nunca inventar números para preencher layouts.

## 3. Roteamento de ferramentas

Consultar o inventário atualizado em docs/PRESENTATION-TOOLING.md. Roteamento padrão:

### PowerPoint nativo (.pptx)
- **Primeira opção:** ppt-master (hugohe3/ppt-master), Skill MIT de geração, reconstrução e edição de PPTX nativo. A instalação recomendada é somente da Skill via CLI, pois o clone integral do upstream é pesado.
- Instalação local opcional no computador do usuário:
  npx skills add https://github.com/hugohe3/ppt-master --skill ppt-master
- A Skill upstream tem seu próprio fluxo de integridade, roteamento e dependências. Seguir o SKILL.md original sem pular o attribution guard ou substituir seus caminhos por suposições.
- Se a ferramenta não estiver instalada ou não houver runtime de arquivos, não afirmar que o PPTX foi gerado. Usar um gerador disponível e validável, ou explicar a limitação.

### HTML para navegador
- Usar frontend-slides/SKILL.md e STYLE_PRESETS.md para apresentações autossuficientes e animadas.
- Usar o upstream upstream/frontend-slides/ como referência canônica, sem editar seus arquivos.
- Para apresentações editoriais ou Swiss Style, considerar upstream/guizang-ppt-skill/. É HTML, não um gerador de PPTX nativo. Respeitar AGPL-3.0 e revisar a licença antes de redistribuir modificações.

### Editar PowerPoint existente
- Considerar upstream/pptx-tools/ para ler slides, layouts, masters, atualizar textos, inserir imagens, preencher dados em lote e duplicar layouts.
- Exige .NET 10 SDK e build local. É ferramenta de manipulação/atualização; não substitui um motor de direção de arte e não cria gráficos do zero nem altera masters/temas complexos.
- Não instalar ou ativar MCP que exija API paga sem autorização explícita.

### Google Slides e Canva
- Preferir o conector oficial Google Slides quando disponível e autenticado. O MCP remoto oficial do Google está em Developer Preview e exige elegibilidade, projeto Google Cloud e OAuth preparado para agente. Não alegar que está conectado apenas por existir documentação.
- O Canva já consta no catálogo de conectores da TS Digitais. Reutilizar a integração existente; não instalar um segundo Canva MCP comunitário sem necessidade demonstrada. Verificar autenticação, permissões e recursos do plano.
- Não gravar Client IDs, Client Secrets, refresh tokens ou credenciais em GitHub.

### Serviços por créditos
- 2Slides é opcional e depende de API key e créditos por página/operação. Não escolher por padrão para a TS Digitais. Só usar após o usuário autorizar o serviço e compreender o consumo previsto.
- Gamma, Presentations.AI e Manus são serviços SaaS, não bibliotecas open-source a serem instaladas neste repositório. Não os tratar como ferramentas gratuitas ilimitadas.

## 4. Direção visual

- Usar proporção 16:9 como padrão para apresentações widescreen, salvo requisito diferente.
- Construir identidade visual deliberada com tipografia, cores, hierarquia, grid, margens e ritmo consistentes.
- Variar layouts conforme a função do slide: abertura, seção, comparação, métrica, processo, prova, cronograma, preço e encerramento.
- Preferir gráficos, diagramas e formas nativas quando forem editáveis e os dados forem reais.
- Usar imagens licenciadas, fornecidas pelo usuário ou geradas quando acrescentarem valor. Não colocar imagens decorativas apenas para preencher espaços.
- Não usar screenshots de sites, logos, depoimentos, números de clientes ou resultados sem fonte verificável.
- Manter notas do apresentador separadas do texto visível, quando aplicável.

## 5. Validação visual obrigatória

A apresentação não está pronta apenas porque o arquivo foi salvo ou o código compilou.

### PPTX
- Abrir/renderizar o arquivo final em visualizador compatível.
- Verificar todas as páginas em tamanho real: texto cortado, sobreposição, alinhamento, margens, fontes substituídas, gráficos, imagens e contraste.
- Conferir que objetos nativos continuam editáveis quando essa for a exigência.
- Revisar abertura, páginas intermediárias e encerramento em conjunto para garantir unidade.

### HTML
- Validar no navegador em 1920×1080, 1280×720, 768×1024, 375×667 e 667×375.
- Garantir navegação por teclado, toque e redução de movimento; conferir que cada slide cabe no viewport sem barras de rolagem internas.
- Não reduzir tipografia a tamanhos ilegíveis para acomodar texto; dividir o conteúdo quando necessário.

### PDF
- Conferir cada página após exportação, não apenas o HTML ou PPTX de origem.
- Revisar quebras, margens, fontes, imagens, links, legibilidade e páginas em branco.
- Se não houver ferramenta de renderização/inspeção disponível, declarar que a validação visual ficou pendente.

## 6. Entrega

Informar formato, quantidade de páginas, ferramenta utilizada, arquivos editáveis e exportações. Entregar fonte editável quando solicitada e PDF como versão de leitura. Identificar limitações reais, fontes de dados e itens que dependem de aprovação.

## Restrições

- Priorizar alternativas gratuitas, open-source e conectores já disponíveis.
- Nunca gastar créditos, criar assinaturas ou conectar contas sem autorização.
- Nunca inventar fatos, resultados, avaliações, estatísticas, clientes, preços, ROI, prazos ou garantias.
- Não inserir informação confidencial do cliente em serviços externos sem necessidade e autorização.
- Não declarar um MCP como instalado/conectado, nem uma Skill como disponível em runtime, sem teste no cliente em que será usada.
