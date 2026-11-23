# Métricas sociais no Google Sheets — arquitetura direta

## Objetivo
Manter histórico próprio e de baixo custo para decisões editoriais, sem tornar o Metricool ou outro agregador uma dependência obrigatória.

## Situação de integração
- Neste ambiente não há conector nativo de Google Sheets disponível; o conector Google Drive/Sheets aparece indisponível por política administrativa.
- A conexão Windsor.ai está disponível para outras fontes, mas é um intermediário de terceiros e não é a arquitetura preferida para este projeto.
- Caminho recomendado: Google Apps Script dentro da própria planilha, chamando APIs oficiais Google Analytics Data API e Search Console API com OAuth do proprietário. Para métricas Instagram/Facebook, avaliar depois a Meta Graph API oficial e suas permissões; não inventar acesso ou usar scraping.
- A criação/autorização da planilha e do projeto Apps Script ainda precisa ser feita na conta Google proprietária. Nenhuma conta foi conectada nem script executado por este documento.

## Estrutura sugerida da planilha

| Aba | Granularidade | Campos principais |
|---|---|---|
| CONTENT_LOG | 1 linha por publicação | content_id, marca, plataforma, formato, pilar, público, campanha, hook, CTA, data planejada, data publicada, URL, UTM, status |
| SOCIAL_DAILY | 1 linha por conta/dia | date, platform, account_id, followers, reach, impressions, profile_visits, link_clicks, source |
| SOCIAL_POSTS | 1 linha por publicação/dia de coleta | content_id, post_id, date, reach, impressions, views, likes, comments, shares, saves, watch_time, profile_actions, source |
| SOCIAL_STORIES | 1 linha por frame/dia de coleta | content_id, story_id, date, reach, impressions, exits, replies, taps_forward, taps_back, link_clicks, source |
| GA4_LANDING_PAGES | data × landing page | date, landing_page, sessions, engaged_sessions, engagement_rate, key_events, conversions, source |
| GSC_QUERIES | data × query | date, query, clicks, impressions, ctr, position, source |
| GSC_PAGES | data × page | date, page, clicks, impressions, ctr, position, source |
| SYNC_LOG | 1 linha por execução | started_at, source, date_range, rows_written, status, error |

Não assumir que todas as plataformas disponibilizam todas as métricas ou histórico. Usar campos nulos quando ausentes, nunca zero artificial.

## Regras de histórico
1. Guardar snapshots com data de coleta e período dos dados.
2. Fazer upsert com chave estável por fonte, data, conta, dimensão e conteúdo, sem duplicar a mesma linha em cada sincronização.
3. Preservar a resposta bruta ou uma cópia versionada dos dados quando os termos e a capacidade permitirem.
4. Solicitar o maior intervalo acessível na primeira carga, paginar conforme o limite oficial e gravar checkpoints.
5. Não prometer dados anteriores à retenção da API. Search Console tem janela histórica limitada; históricos mais antigos só existem se já tiverem sido arquivados.
6. Manter timezone e moeda da propriedade explícitos.
7. Separar métricas nativas de cada rede; não criar comparações entre denominadores diferentes.

## Próxima implementação técnica
Criar um projeto Apps Script vinculado à planilha com:
- GA4_PROPERTY_ID e GSC_SITE_URL em Script Properties;
- escopos somente leitura para Analytics e Search Console;
- funções syncGA4LandingPages(), syncGSCQueries(), syncGSCPages();
- paginação, retry com backoff, logs e upsert idempotente;
- gatilho diário/semanal instalável pelo proprietário;
- nenhuma chave de API, token ou dado sensível no GitHub.

A API oficial precisa ser habilitada no projeto Google e o usuário que executa o script deve ter acesso às propriedades. A planilha deve ter acesso restrito aos responsáveis.

## Não fazer agora
Não conectar um terceiro agregador como requisito, não criar credenciais em repositório, não importar dados pessoais de DMs/comentários e não ativar publicação automática. Primeiro validar a extração de GA4 e Search Console em modo somente leitura; depois ampliar para métricas sociais.
