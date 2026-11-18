---
name: weasyprint-pdf-creation
description: Cria PDFs profissionais a partir de HTML/CSS com WeasyPrint, incluindo mídia impressa, margens, páginas pares/ímpares, cabeçalhos, rodapés, paginação, templates e QA. Use para e-books, relatórios, propostas, guias e documentos multipágina.
---

# WeasyPrint PDF Creation — TS Digitais

## Objetivo e limites
Usar HTML semântico, CSS de impressão e dados separados para gerar PDFs reproduzíveis. É indicado para documentos próprios e templates controlados. Não usar como método padrão para editar PDFs arbitrários ou capturar páginas web dependentes de JavaScript complexo.

## 1. Stack gratuita
- Python 3 e ambiente virtual.
- WeasyPrint instalado conforme documentação oficial e dependências nativas do sistema.
- Jinja2 para templates quando necessário.
- pypdf para inspeção/combinação de PDFs quando necessário.
- pdfinfo e pdftotext (Poppler) para verificações auxiliares.

Antes de instalar, verificar sistema operacional, versões suportadas e dependências nativas na documentação oficial: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html. Não presumir que a instalação é apenas `pip install`.

## 2. Estrutura de projeto recomendada
```text
pdf-project/
  templates/
    base.html
    cover.html
    chapter.html
  assets/
    css/print.css
    images/
    fonts/
  data/
    content.json
  scripts/
    render_pdf.py
  outputs/
```

Separar conteúdo, template, CSS, imagens e saída. Não misturar dados do cliente com o código do template.

## 3. CSS para impressão
- Definir explicitamente `@page` com tamanho, orientação e margens.
- Usar unidades físicas (`mm`, `cm`, `pt`) para geometria de página e tipografia de impressão.
- Definir regras `@media print` e estilos de tela quando também houver preview HTML.
- Usar `:left`, `:right` e `:first` em `@page` quando margens espelhadas ou primeira página especial forem necessárias.
- Usar contadores CSS para numeração e elementos de margem quando suportados pela versão escolhida.
- Aplicar `break-before`, `break-after`, `break-inside` e `orphans`/`widows` conscientemente.
- Usar `box-sizing: border-box`, grid/flex apenas conforme suporte real do WeasyPrint.
- Reservar espaço de cabeçalhos, rodapés, números, tabelas e elementos decorativos.
- Tratar strings longas com `overflow-wrap: anywhere`; validar tabelas e colunas com dados extensos.

Exemplo de base:
```css
@page {
  size: A4;
  margin: 20mm 18mm 22mm;
  @bottom-center {
    content: counter(page);
    font-size: 9pt;
  }
}

@page :left { margin-left: 22mm; margin-right: 16mm; }
@page :right { margin-left: 16mm; margin-right: 22mm; }

h1, h2, h3 { break-after: avoid; }
figure, table, blockquote { break-inside: avoid; }
p { orphans: 3; widows: 3; }
```

Validar o suporte das regras com a versão fixada. Não presumir paridade completa com Chrome.

## 4. Renderização reproduzível
- Fixar versão do WeasyPrint e dependências do projeto.
- Definir base_url para resolver imagens, CSS e fontes locais.
- Usar autoescape em templates Jinja2.
- Registrar warnings em arquivo e corrigir problemas inesperados.
- Não carregar recursos remotos sem necessidade; preferir assets locais e licenças verificadas.
- Manter os dados de entrada separados e validar o schema antes de renderizar.

Exemplo mínimo:
```python
from pathlib import Path
from weasyprint import HTML

source = Path("build/index.html")
output = Path("outputs/guide.pdf")
output.parent.mkdir(parents=True, exist_ok=True)
HTML(filename=str(source), base_url=str(source.parent.resolve())).write_pdf(output)
```

## 5. QA obrigatório
1. Confirmar que o processo terminou sem erro e guardar o log de warnings.
2. Verificar quantidade de páginas, dimensões e orientação com `pdfinfo`.
3. Extrair texto com `pdftotext` e conferir títulos, parágrafos, tabelas e acentos.
4. Renderizar páginas para imagem e inspecionar visualmente todas as páginas relevantes.
5. Conferir margens, conteúdo cortado, sobreposição, páginas vazias, quebras, rodapés e numeração.
6. Testar URLs, bookmarks e links internos quando existirem.
7. Repetir a renderização depois de qualquer alteração em fonte, conteúdo, imagem ou CSS.

Um screenshot bonito não substitui validação do PDF real; texto extraído sem erro também não prova que a composição está correta.

## 6. Fontes e direitos
- Preferir fontes livres com licença compatível e manter os arquivos de licença junto aos assets.
- Fontes alteram métricas e paginação: validar novamente após troca.
- Não incorporar fontes comerciais ou assets sem permissão.
- Garantir que o texto continue selecionável e pesquisável, salvo necessidade explícita de rasterização.

## 7. Limitações e alternativas
- JavaScript de navegador não é executado como em Chrome.
- Alguns recursos CSS têm suporte parcial ou diferente; consultar a documentação da versão.
- Para documentos altamente interativos, formulários complexos ou fidelidade exata a um site JS-heavy, avaliar Chromium/Playwright ou outra ferramenta, sem misturar engines sem necessidade.
- Para edição de PDF existente, usar ferramenta específica de PDF em vez de reconstruir o documento automaticamente.

## Fonte e atribuição
Adaptação TS Digitais inspirada no projeto https://github.com/slapash/weasyprint-pdf-skill, licenciado sob MIT. A licença MIT está preservada em LICENSE. Consulte o upstream para scripts, templates, exemplos e mudanças recentes. A documentação oficial do WeasyPrint é a fonte técnica para compatibilidade CSS e instalação.