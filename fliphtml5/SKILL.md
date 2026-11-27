---
name: fliphtml5
description: Pesquisar, configurar, publicar, incorporar e diagnosticar flipbooks usando FlipHTML5, com foco no plano Free, conversão fiel de PDFs, leitor responsivo e limites de privacidade.
---

# FlipHTML5 — operação especializada com foco no plano Free

> Pesquisa documental oficial verificada em 27/11/2026. Esta skill registra capacidades documentadas, restrições conhecidas e pontos que ainda exigem teste na conta. Não confundir documentação pública com recursos já autenticados ou testados na conta do usuário.

## 1. Quando usar

Consultar esta skill antes de:
- Criar ou publicar uma revista, catálogo, e-book ou relatório no FlipHTML5.
- Configurar aparência, navegação, toolbar, painéis ou comportamento mobile.
- Incorporar um flipbook em Astro, React, WordPress ou outro site.
- Avaliar conversão PDF, legibilidade, fontes, qualidade de imagem e busca.
- Investigar API, MCP, automação ou exportação para hospedagem própria.

## 2. Princípio central

**O PDF de origem é a publicação; o FlipHTML5 é o conversor e leitor.**

O FlipHTML5 transforma o documento carregado em uma experiência digital com páginas, navegação e controles. Não é um diagramador editorial capaz de corrigir um PDF mal composto. Antes de subir o arquivo, a publicação precisa estar correta: formato homogêneo, fontes incorporadas, textos legíveis, margens, imagens e quebras aprovadas.

Nunca concluir que a tipografia foi corrigida apenas porque o leitor parece nítido. Validar o PDF original e a versão convertida separadamente.

## 3. Plano Free: capacidades e limites documentados

O plano Free é adequado para experimentar e publicar conteúdo público, não para distribuir documentos privados de clientes.

| Recurso | Plano Free documentado |
|---|---|
| Preço | US$ 0 / sem cartão de crédito |
| Criação | Até 5 flipbooks por dia |
| Armazenamento | 20 GB |
| Arquivo de origem | PDF até 100 MB |
| Tamanho da publicação | Até 500 páginas por livro |
| Conta/equipe | 1 usuário; não é plano de equipe |
| Estantes | 1 bookshelf |
| Templates | Mais de 90 templates; 6 layouts pré-prontos citados na página de preços |
| Compartilhamento | Link público e incorporação em site por iframe |
| Dispositivos | Leitor compatível com dispositivos móveis |
| Marca da plataforma | Anúncios e marca d'água FlipHTML5 |
| Descoberta | Não há bloqueio de indexação por mecanismo de busca no Free |
| Segurança | Não há proteção por senha para o livro no Free |
| Download | O leitor pode baixar o PDF original; não é possível desativar essa opção no Free |
| Exportação HTML | Não incluída no Free |
| Hospedagem própria | Exportação HTML para hospedagem no próprio site requer plano pago |
| API convencional | Listada como recurso Enterprise, não presumir acesso no Free |
| Domínio próprio do leitor | Não incluído no Free |
| Detecção/importação avançada de links | Recursos documentados como pagos |
| Índice importado do PDF | Importação de TOC é Pro ou superior |

**Implicação prática:** incorporar um livro no nosso site não torna o livro privado. O iframe apenas exibe conteúdo hospedado pelo FlipHTML5. O endereço público do livro pode ser aberto diretamente fora do nosso domínio, e a sessão autenticada do nosso site não protege o arquivo hospedado na plataforma.

Não usar o Free para relatórios reais de clientes, métricas de negócio, analytics, dados pessoais, documentos internos, informações comerciais confidenciais ou conteúdo cuja distribuição dependa de login. Não usar como contorno de autenticação em área restrita. Usar apenas material público, demonstrações sintéticas ou material cuja publicação aberta tenha sido autorizada.

### Exportação e hospedagem: distinção obrigatória

Não prometer que o plano Free permite baixar o pacote HTML e hospedar em Cloudflare Pages/R2. A documentação oficial informa que a exportação HTML/EXE/aplicativo não está disponível no Free. O plano Free permite incorporar o livro hospedado no FlipHTML5.

A página de preços lista API convencional no Enterprise. A existência de um servidor MCP oficial separado não significa que os recursos de API ou todos os controles de publicação estejam disponíveis no Free.

## 4. Preparar o PDF antes do upload

Aplicar também `editorial-magazine/SKILL.md`, `typography-master/SKILL.md` e `privacy-by-design/SKILL.md` quando aplicáveis.

### Preflight obrigatório

- Usar páginas com a mesma dimensão e proporção em todo o PDF. O conversor pode usar a primeira página como referência e reduzir/esticar páginas de dimensões diferentes, gerando espaços em branco ou escalas inconsistentes.
- Incorporar as fontes ao PDF e confirmar que os caracteres acentuados, símbolos, números e pesos aparecem corretamente.
- Manter texto nativo/selecionável sempre que possível; não rasterizar o corpo editorial para “melhorar” a aparência.
- Respeitar o mínimo TS Digitais: texto visível ≥16 CSS px no leitor a 100% e ≥12 pt na versão para impressão, inclusive legendas, notas, créditos, fontes, folios, labels e metadados.
- Conferir margens, alinhamentos, entrelinha, viúvas, órfãs, cortes, tabelas e imagens no PDF original antes do upload.
- Remover páginas vazias acidentais e revisar capa/contracapa.
- Não depender de OCR. O FlipHTML5 extrai texto que já existe como texto no PDF; texto dentro de imagem/scanner não vira automaticamente texto pesquisável pelo mecanismo documentado.
- Não depender do conversor para corrigir fontes desproporcionais, tracking, espaçamento, escala ou distribuição ruim. Corrigir no arquivo-fonte.
- Não usar formulários PDF preenchíveis como requisito da experiência: o suporte não é garantido pelo leitor.
- Não enviar PDF privado por URL pública de origem para usar o fluxo de upload via URL. Para material público, conferir se a URL está acessível sem autenticação.

## 5. Escolher o modo de conversão

A documentação descreve cinco mecanismos. O padrão indicado é Full Vector (Vetor Completo).

| Modo | O que prioriza | Quando testar |
|---|---|---|
| Full Vector | Vetoriza textos e imagens, permitindo ampliar sem a mesma perda de nitidez de um raster | Primeira escolha para publicação mista com texto, gráficos e imagens |
| HD Text | Vetoriza o texto | Publicação predominantemente textual; comparar quando o texto for a prioridade |
| HD Image | Renderização com foco em imagem | Publicação dominada por fotografias ou quando os outros modos apresentam problemas |
| Internal Library | Conversão pela biblioteca interna | Alternativa de compatibilidade/velocidade |
| GhostScript | Nitidez e contraste | Alternativa comparativa para documentos que precisem de contraste |

Não afirmar que um modo é universalmente superior. Fazer um teste com um PDF público representativo, comparar as mesmas páginas e registrar resultado, tamanho, nitidez, comportamento de zoom e tempo de carregamento.

### Qualidade de renderização

A documentação lista:
- Very High / Highest: 260 DPI, dimensão máxima informada de 3000 × 3000.
- High: 200 DPI, máximo 2800 × 2800.
- Medium: 150 DPI.
- Low: 110 DPI.
- Lower: 85 DPI.
- Lowest: 65 DPI.

Maior qualidade tende a aumentar tamanho do livro e tempo de carregamento. Para o Free, a documentação informa que High/Highest pode ser selecionado nas primeiras cinco conversões de livro; depois de cinco livros convertidos, essa escolha deixa de estar disponível. Tratar esse limite como uma franquia inicial da conta e não gastar em testes descartáveis. Antes de usar, conferir o seletor real da conta, pois limites e interface podem mudar.

Orientação:
1. Em teste representativo, experimentar Full Vector e a maior qualidade que estiver liberada, desde que o arquivo não fique excessivamente pesado.
2. Comparar a leitura em escala 100%, zoom ampliado e dispositivos móveis.
3. Se o documento for quase todo texto, comparar HD Text.
4. Se for muito visual, comparar HD Image.
5. Registrar o modo e a qualidade escolhidos junto do nome/versão do PDF.
6. Se a conversão ficar ruim, voltar ao PDF-fonte antes de tentar dezenas de combinações.

### Separação das páginas

- Auto: opção inicial para PDFs com páginas individuais; normalmente trata primeira página como capa, última como contracapa e as demais como páginas internas.
- None: considerar quando cada página do arquivo já representa a página individual pretendida e o Auto estiver interpretando a publicação incorretamente.
- Modos de corte/split: usar apenas quando o arquivo foi diagramado em spreads ou folhas de imposição. Conferir o sentido de leitura.
- Para publicação em português, selecionar leitura da esquerda para a direita.
- Nunca presumir que um PDF de páginas individuais deve ser dividido como spread.

### Extração de texto, índice e links

- Quando a opção estiver disponível, habilitar extração de texto para permitir pesquisa, seleção e cópia; conferir também os botões de busca/cópia na interface do leitor.
- Texto presente apenas como fotografia ou imagem escaneada não será automaticamente convertido em texto selecionável pelo mecanismo descrito.
- Importação de TOC/índice e importação/detecção de links têm restrições de plano; não pressupor que estejam disponíveis no Free.
- Quando TOC automático não estiver disponível, incluir no próprio PDF uma página de sumário bem composta. Links clicáveis no PDF devem ser testados após a conversão; não assumir que serão importados.
- Não gastar os pontos de IA mensais automaticamente. Preferir título, descrição, palavras-chave e sumário revisados manualmente.

## 6. Fluxo operacional Free

### A. Preparar a edição

1. Aprovar o PDF e aplicar o preflight da seção 4.
2. Confirmar que o conteúdo é público e não confidencial.
3. Guardar o PDF-fonte versionado no armazenamento apropriado do projeto, respeitando a política de privacidade.
4. Definir título e descrição que não revelem dados pessoais nem informação interna.
5. Escolher um PDF público de teste; não usar relatório privado real.

### B. Criar o flipbook

1. Entrar na conta FlipHTML5 e iniciar upload do PDF.
2. Conferir limite de tamanho, páginas e armazenamento na interface.
3. Configurar split mode, direção de leitura, motor e qualidade conforme a seção 5.
4. Se a página indicar que o upload está em andamento, não fechar nem atualizar a aba até o upload concluir. A conversão iniciada pode continuar depois que o arquivo foi recebido, mas confirmar o estado antes de sair.
5. Aguardar o processamento e abrir o preview do livro.
6. Conferir capa, primeiras páginas, páginas centrais, páginas com tabelas/imagens e contracapa.
7. Não publicar/compartilhar antes de passar nos gates de qualidade e privacidade.

### C. Completar metadados

Na área Book Info/Informações do livro, preencher manualmente:
- Título factual e específico.
- Descrição objetiva.
- Palavras-chave realmente relacionadas.
- Categoria/labels adequados.
- Identificação e data somente quando necessários e autorizados.

Não inserir palavras-chave irrelevantes, promessas inventadas ou informação privada. Não consumir créditos de IA apenas para preencher metadados.

### D. Personalizar o leitor

- Explorar as opções efetivamente mostradas na conta Free. A documentação de interface apresenta controles de toolbar, painéis, tema, cor, opacidade e toolbar mobile, mas não presumir que toda opção esteja liberada em todos os planos.
- Pré-visualizar desktop e mobile após cada ajuste importante.
- Priorizar navegação clara: virar página, zoom, miniaturas, busca/seleção de texto quando disponível, tela cheia e compartilhamento.
- Retirar controles supérfluos apenas quando a interface Free permitir.
- Não prometer remoção de anúncio ou marca d'água; são limitações do Free.
- Não injetar CSS ou JavaScript do site hospedeiro para tentar modificar conteúdo dentro do iframe. O conteúdo é cross-origin e não pode ser estilizado livremente pelo CSS do site pai.

### E. Publicar e incorporar

1. Usar a opção de compartilhamento/incorporação fornecida no painel do próprio livro.
2. Copiar o iframe gerado pelo FlipHTML5; preservar o URL/ID exato da publicação.
3. No site, definir `title` acessível, dimensões responsivas e `allowfullscreen` quando fornecido.
4. Usar `loading="lazy"` somente se o leitor não estiver no primeiro viewport.
5. Em layouts Astro, reservar uma área de leitura suficiente e responsiva; não usar altura fixa pequena que recorte o leitor.
6. Permitir fallback com link direto “Abrir publicação em nova aba”.
7. Se houver Content-Security-Policy, liberar em `frame-src` somente os hosts reais necessários após verificar o domínio usado pelo iframe.
8. Testar tela cheia, rolagem, teclado, zoom, controles, mobile e carregamento em janela privada.
9. Confirmar que a URL direta da publicação é pública. Esse é o comportamento esperado do Free e deve ser aceito conscientemente antes de publicar.

Exemplo estrutural (substituir pelo iframe exato copiado no painel; não inventar o URL do livro):

```html
<iframe
  src="URL_EXATA_FORNECIDA_PELO_FLIPHTML5"
  title="Título da publicação"
  loading="lazy"
  allowfullscreen
  referrerpolicy="strict-origin-when-cross-origin"
  style="display:block;width:100%;height:min(85vh,900px);border:0"
></iframe>
<p><a href="URL_EXATA_FORNECIDA_PELO_FLIPHTML5" target="_blank" rel="noopener noreferrer">
  Abrir publicação em nova aba
</a></p>
```

Não adicionar `sandbox` ao iframe por padrão: pode bloquear funcionalidades necessárias; se houver requisito de sandbox, identificar e testar explicitamente os tokens necessários.

## 7. Segurança, privacidade e direitos

**Gate obrigatório: o plano Free é para conteúdo aberto.**

Antes de cada upload:
- Identificar se o material contém dados pessoais, dados sensíveis, informação financeira, relatório de desempenho, analytics, contratos, credenciais, dados de clientes, informações internas ou segredos comerciais.
- Se houver qualquer conteúdo que não deva ser público, interromper a publicação no Free.
- Não confiar em login do site que contém o iframe como proteção do livro.
- Considerar que o livro pode ser acessado pelo link direto e encontrado por mecanismos de busca.
- Considerar o download do PDF original pelo leitor.
- Obter autorização para publicar materiais e imagens de terceiros; a possibilidade técnica de upload não concede direitos autorais.
- Usar dados sintéticos em demonstrações.
- Evitar publicar nomes completos, contatos, endereços e identificadores sem necessidade e autorização.

Para relatórios individuais de clientes, usar solução sob controle próprio com autorização server-side por recurso, ou avaliar plano que ofereça controles adequados e verificar os termos antes de contratar. Não apresentar o Free como solução segura para conteúdo restrito.

## 8. MCP e automação: não confundir com API

O FlipHTML5 oferece servidor MCP remoto em `https://mcp.fliphtml5.com/mcp`. A documentação descreve conversão de documentos online, busca de detalhes de livros, atualização de título/descrição/palavras-chave e gestão de acesso.

### Autenticação: resultado prático no LangSmith

Pesquisa técnica em 27/11/2026:
- A chamada MCP `initialize` sem credenciais retornou HTTP 401 `Authentication required`.
- O metadata público do recurso declara escopo `fliphtml5:books` e Bearer token via header.
- O authorization-server metadata anuncia endpoint de registro dinâmico (DCR), Authorization Code, refresh token e PKCE S256.
- **Teste real no LangSmith Fleet:** o usuário tentou `OAuth 2.1 (Auto)` e recebeu: `This MCP server isn't supported yet. This server's OAuth provider rejected LangSmith's client registration. LangSmith Managed Tools currently supports servers that register OAuth clients automatically.`
- Assim, embora os metadados anunciem DCR, o fluxo automático do LangSmith foi rejeitado pelo provedor FlipHTML5. Não continuar insistindo em OAuth Auto nesta integração sem mudança documentada no upstream.

**Método recomendado para LangSmith: Static Headers com API key do MCP FlipHTML5.**

1. No FlipHTML5, abrir perfil → Settings → MCP Server.
2. Em API Key List, clicar **Create API key** e nomear de forma identificável, por exemplo `LangSmith Fleet - langchain-ai-design-agent`.
3. Copiar a chave completa imediatamente; ela só aparece uma vez. Não copiar a versão mascarada.
4. No agente `langchain-ai-design-agent`, abrir Connections → Add connection → + Add custom MCP.
5. Nome: `FlipHTML5`.
6. URL exata: `https://mcp.fliphtml5.com/mcp`.
7. Authentication type: **Static Headers**.
8. Adicionar um único header:
   - Key: `Authorization`
   - Value: `Bearer SUA_API_KEY_COMPLETA` (substituir pelo segredo; nunca incluir aspas)
9. Salvar e aguardar o Fleet executar a descoberta de ferramentas.
10. Começar com uma consulta read-only sobre um flipbook público de teste e conferir o resultado no dashboard FlipHTML5.

A recomendação de header combina as duas documentações: o FlipHTML5 manda configurar API-key authentication e divulga Bearer via header no resource metadata; o LangSmith documenta `Authorization: Bearer API_KEY` como padrão de Static Headers. Nunca enviar a API key no chat, no prompt do agente, em screenshots, commits, issue, arquivo de skill ou frontend. Inserir somente no campo de credencial do LangSmith.

### Segurança e escopo

- Criar uma chave dedicada apenas a este agente.
- Não cadastrar em Fleet > Integrations nem workspace global na primeira etapa: manter a conexão só em `langchain-ai-design-agent`.
- O Fleet requer permissão **MCP Server Create** no workspace.
- Começar com ferramentas read-only e revisar nomes, descrições, schemas e anotações depois da descoberta.
- Escrita, conversão/criação de livro, atualização de metadados, alteração de visibilidade/acesso e exclusão exigem autorização explícita para o livro e a operação específica.
- O escopo `fliphtml5:books` não deve ser tratado como read-only; o metadata não confirma granularidade.
- API keys FlipHTML5 não expiram automaticamente; cada conta pode ter até 10 chaves ativas; a chave completa é mostrada apenas uma vez; revogação após exclusão pode levar cerca de 10 minutos.
- OAuth ou API key não altera limites nem recursos do plano Free.

### O que conta como instalado

Não marcar MCP como conectado só porque o servidor foi salvo. Exigir:
- Static Headers salvo e aceito.
- Descoberta `tools/list` bem-sucedida.
- Lista real de ferramentas documentada.
- Consulta read-only validada no dashboard FlipHTML5.
- Agente e escopo de acesso confirmados.
- Nenhum segredo presente nos arquivos ou logs versionados.

Detalhes técnicos e histórico de tentativa OAuth em `fliphtml5/MCP-LANGSMITH.md`.
## 9. Validação visual e funcional

Build concluído, iframe HTTP 200 ou mensagem “conversion successful” não significam que a publicação está aprovada.

### Revisão da conversão

- Conferir PDF original e flipbook lado a lado.
- Revisar todas as páginas quando o livro for curto; em livros longos, amostrar capa, início, meio, fim e todas as páginas de maior complexidade, mantendo plano de inspeção integral antes de publicação importante.
- Verificar caracteres acentuados, hífens, símbolos, fontes, sub/sobrescritos, tabelas, transparências, gráficos e imagens.
- Verificar margens, corte, alinhamento, orientação, páginas em branco e ordem.
- Comparar a página a 100% e com zoom; texto vetorial deve manter nitidez, mas o tamanho visual ainda depende do PDF-fonte.
- Testar pesquisa, seleção e cópia de texto quando habilitadas.
- Testar navegação em desktop e celular, orientação retrato/paisagem, fullscreen e retorno ao site.
- Testar link direto numa janela privada, para entender a exposição pública real.
- Conferir os anúncios e a marca d'água, que são esperados no Free.
- Verificar o comportamento de download do PDF original.
- Guardar capturas representativas e registrar data, conta/plano, configurações, tamanho do arquivo e resultado.

### Viewports mínimos

- Desktop: 1440 × 900 e 1366 × 768.
- Mobile: 390 × 844 e 360 × 800.
- Incluir tablet se o público usar esse formato.
- Não afirmar revisão visual quando nenhuma captura real foi aberta e inspecionada.

### Critérios de aprovação

- Nenhum texto cortado ou deformado.
- Nenhuma página com proporção divergente.
- Nenhuma fonte/caractere incorreto.
- Tipografia dentro do mínimo de 16px/12pt.
- Busca e seleção funcionam quando habilitadas.
- Leitor utilizável em mobile e desktop.
- Privacidade/publicidade do conteúdo foi aceita pelo responsável.
- O iframe e o link direto abrem a publicação correta.
- Limitações do Free (anúncios, watermark, exposição e download do PDF) foram aceitas.

## 10. Diagnóstico rápido

| Sintoma | Causa provável | Verificação/correção |
|---|---|---|
| Texto minúsculo ou deformado | PDF-fonte com escala, fonte ou dimensões incorretas | Abrir e corrigir o PDF original; conferir fontes incorporadas e tamanho de página |
| Texto borrado no zoom | Conversão raster ou qualidade baixa | Comparar Full Vector e HD Text; conferir qualidade liberada no Free |
| Imagem borrada | PDF já contém imagem raster de baixa resolução | Substituir asset no arquivo-fonte; HD Image não cria detalhe ausente |
| Espaço branco em páginas específicas | Dimensões/proporções diferentes no PDF ou split mode errado | Padronizar todas as páginas e revisar Auto/None/split |
| Texto não pesquisável | Texto foi convertido em imagem ou está escaneado | Verificar camada de texto do PDF; não pressupor OCR automático |
| Índice não aparece como painel | TOC import pode ser Pro+ | Criar página de sumário no PDF; não prometer importação automática no Free |
| Links não funcionam | Links não foram importados/detectados | Testar no PDF-fonte e no livro; importação de links pode ser paga |
| Fullscreen não funciona dentro do site | atributo `allowfullscreen`, Permissions Policy ou integração do iframe | Conferir código original de embed e políticas do host |
| CSP bloqueia o livro | domínio do iframe ausente de `frame-src` | Inspecionar URL real e liberar somente o host necessário |
| Iframe aparece vazio | URL errada, bloqueio do navegador, publicação removida ou restrição do host | Abrir URL direta, testar janela privada e verificar status no painel |
| Publicação continua aparecendo depois do logout do site | livro hospedado é público | Comportamento esperado no Free; não usar para conteúdo privado |

## 11. Atualização desta skill

Ao aprender algo novo na conta Free:
1. Registrar data, plano, contexto e passos reproduzíveis.
2. Separar fato da documentação oficial, fato observado na conta e hipótese.
3. Não promover uma hipótese a regra.
4. Atualizar esta skill e o registro de ferramentas com a limitação/descoberta.
5. Incluir link oficial que sustenta a mudança.
6. Não registrar URL privada de publicação, dado de cliente, token, e-mail ou outro segredo.
7. Se uma opção mudar de plano ou desaparecer, registrar a conta/região/data de verificação e rever recomendações anteriores.

## 12. Fontes oficiais consultadas

- [Planos e preços FlipHTML5](https://fliphtml5.com/pt/fliphtml5-pricing.php)
- [Central de ajuda: download e exportação](https://help.fliphtml5.com/pt/docs/download/)
- [Modos de divisão e qualidade de renderização](https://help.fliphtml5.com/pt/docs/page-split-modes-and-page-rendering-quality/)
- [Incorporar flipbook em um site](https://help.fliphtml5.com/docs/embed-a-flipbook/)
- [Personalizar interface e toolbar](https://help.fliphtml5.com/docs/customize-interface/)
- [Configurações de privacidade e proteção do livro](https://help.fliphtml5.com/docs/book-privacy-settings/)
- [Conectar assistente de IA ao FlipHTML5 por MCP](https://help.fliphtml5.com/pt/docs/connect-ai-assistant-to-fliphtml5-with-mcp/)

Rever os links e a página de preços antes de novas decisões comerciais: planos, quotas e recursos podem mudar.
