# TS Digitais — Vector Studio (remote)

O Vector Studio executa remotamente no GitHub Actions. Nenhuma dependência de Python, Rust, Cairo, VTracer ou renderização SVG precisa ser instalada no computador do usuário.

## O que o pipeline entrega

- SVG híbrido autocontido com fotografia JPEG incorporada em Base64.
- PNG renderizado a partir do SVG final.
- Adaptações para feed 4:5, story 9:16 e quadrado 1:1.
- Vetorização experimental da fotografia com VTracer, separada do master fotográfico.
- PNG renderizado da versão vetorizada.
- Foto de origem, legenda, alt text e relatório técnico/proveniência.
- Publicação temporária de todos os arquivos no Cloudflare R2 por uma API protegida com GitHub Actions OIDC; não há token estático armazenado no GitHub.

**Regra de fidelidade:** para aparência fotográfica real, a fotografia original é preservada no SVG híbrido. A saída VTracer é uma interpretação por regiões/caminhos e não substitui a fotografia nem promete equivalência pixel a pixel.

## Como executar

1. Edite `vector-studio/requests/active.json` com a foto pública e os textos.
2. Faça commit do JSON na branch `main`. Isso inicia automaticamente o workflow.
3. Abra Actions → “Vector Studio — remote SVG pipeline”.
4. Baixe o artefato `vector-studio-N` ou use as URLs temporárias registradas em `remote-assets.json`.

Também é possível executar manualmente em Actions → workflow → Run workflow e selecionar outro JSON dentro de `vector-studio/requests/`.

## Infraestrutura e custos

- Runner: GitHub-hosted Ubuntu 24.04, 4 vCPU / 16 GB RAM.
- O repositório é público; runners padrão hospedados pelo GitHub são gratuitos em repositórios públicos, conforme as regras atuais do GitHub Actions.
- O job não usa GPU, HF Jobs, APIs de imagem pagas nem credenciais persistentes.
- Cloudflare Worker `ts-svg-assets` é apenas API de upload/download; vetorização continua no runner.
- Os resultados ficam no R2 privado e são servidos pelo Worker em URLs públicas temporárias; a regra de lifecycle existente para o prefixo `images/` remove os objetos após 7 dias (a exclusão do R2 é assíncrona).
- O endpoint de upload valida assinatura JWT via GitHub OIDC, restringindo repo, proprietário, branch principal e workflow específico. Nenhum secret fixo de Cloudflare foi adicionado ao GitHub.
- O artefato de Actions expira após 7 dias; faça download se precisar manter cópia.

## Segurança e direitos

- O script aceita imagens apenas de domínios Pexels, com redirecionamentos revalidados.
- A licença é registrada junto com a URL de origem e o fotógrafo. O usuário deve conferir direitos de terceiros retratados e não sugerir que o local/pessoas endossam a marca.
- Não inclua segredos em request JSON ou no repositório.
- Não publica nem agenda conteúdo em redes sociais.

## Desenvolvimento

- Runtime Python 3.12.
- VTracer pinado em 1.0.0-alpha.4 (API Python Config atual).
- Renderização PNG via CairoSVG.
- O job valida a estrutura XML, a imagem embutida, assinatura JPEG e dimensões finais dos PNGs.
