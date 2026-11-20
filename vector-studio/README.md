# TS Digitais — Vector Studio (remote)

O Vector Studio executa remotamente no GitHub Actions. Nenhuma dependência de Python, Rust, Cairo, VTracer ou renderização SVG precisa ser instalada no computador do usuário.

## O que o pipeline entrega

- SVG híbrido autocontido com fotografia JPEG incorporada em Base64.
- PNG renderizado a partir do SVG final.
- Adaptações para feed 4:5, story 9:16 e quadrado 1:1.
- Vetorização experimental da fotografia com VTracer, separada do master fotográfico.
- PNG renderizado da versão vetorizada.
- Foto de origem, legenda, alt text e relatório técnico/proveniência.

**Regra de fidelidade:** para aparência fotográfica real, a fotografia original é preservada no SVG híbrido. A saída VTracer é uma interpretação por regiões/caminhos e não substitui a fotografia nem promete equivalência pixel a pixel.

## Como executar

1. Edite `vector-studio/requests/active.json` com a foto pública e os textos.
2. Faça commit do JSON na branch `main`. Isso inicia automaticamente o workflow.
3. Abra Actions → “Vector Studio — remote SVG pipeline”.
4. Baixe o artefato `vector-studio-N` gerado pelo job.

Também é possível executar manualmente em Actions → workflow → Run workflow e selecionar outro JSON dentro de `vector-studio/requests/`.

## Infraestrutura e custos

- Runner: GitHub-hosted Ubuntu 24.04, 4 vCPU / 16 GB RAM.
- O repositório é público; runners padrão hospedados pelo GitHub são gratuitos em repositórios públicos, conforme as regras atuais do GitHub Actions.
- O job não usa GPU, HF Jobs, APIs de imagem pagas nem credenciais.
- O artefato expira após 7 dias; baixe os arquivos para manter uma cópia.
- Cloudflare Workers não faz a vetorização pesada. O limite de CPU do plano Free torna-o inadequado; R2/Worker podem ser usados depois como storage/API, respeitando as cotas da conta.

## Segurança e direitos

- O script só baixa imagens de domínios Pexels, com redirecionamentos revalidados.
- A licença é registrada junto com a URL de origem e o fotógrafo. O usuário deve conferir direitos de terceiros retratados e não sugerir que o local/pessoas endossam a marca.
- Não inclua segredos em request JSON ou no repositório.
- Não publica nem agenda conteúdo em redes sociais.

## Desenvolvimento

- Runtime Python 3.12.
- VTracer pinado em 1.0.0-alpha.4 (API Python Config atual).
- Renderização PNG via CairoSVG.
- O job valida a estrutura XML, a imagem embutida, assinatura JPEG e dimensões finais dos PNGs.
