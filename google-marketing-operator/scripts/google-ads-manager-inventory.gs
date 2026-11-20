/**
 * TS Digitais — Google Ads Manager Account Inventory (READ ONLY)
 *
 * Objetivo:
 *   Identificar se a conta atual é uma Manager Account (MCC) e listar até
 *   50 contas cliente ligadas diretamente à hierarquia visível.
 *
 * Segurança:
 *   - Não cria, pausa, ativa ou exclui campanhas.
 *   - Não altera anúncios, palavras-chave, lances ou orçamentos.
 *   - Não envia dados para APIs externas, Sheets ou e-mail.
 *   - Não precisa de API key, developer token ou servidor próprio.
 *
 * Como usar:
 *   Google Ads > Ferramentas > Ações em massa > Scripts > Novo script.
 *   Cole o conteúdo, autorize a execução e clique em Preview.
 *   Compartilhe o resultado dos Logs, ocultando IDs que não queira divulgar.
 *
 * Limite:
 *   withLimit(50) restringe a listagem. Se retornar exatamente 50 contas,
 *   o inventário pode estar incompleto; não interprete 50 como total.
 */

function main() {
  var currentAccount = AdsApp.currentAccount();

  console.log("=== CONTEXTO ATUAL ===");
  console.log("ID: " + currentAccount.getCustomerId());
  console.log("Nome: " + (currentAccount.getName() || "(sem nome)"));
  console.log("Moeda: " + currentAccount.getCurrencyCode());
  console.log("Fuso: " + currentAccount.getTimeZone());

  if (typeof AdsManagerApp === "undefined") {
    console.log("");
    console.log("RESULTADO: este contexto não expõe AdsManagerApp.");
    console.log("A conta atual pode não ser uma Manager Account (MCC).");
    console.log("Nenhum dado foi alterado.");
    return;
  }

  console.log("");
  console.log("=== CONTAS CLIENTE (máximo: 50) ===");
  console.log("customer_id,name,currency,time_zone");

  var iterator = AdsManagerApp.accounts().withLimit(50).get();
  var count = 0;

  while (iterator.hasNext()) {
    var account = iterator.next();
    var values = [
      account.getCustomerId(),
      account.getName() || "",
      account.getCurrencyCode(),
      account.getTimeZone()
    ];

    console.log(values.map(csvCell_).join(","));
    count++;
  }

  console.log("");
  console.log("CONTAS_RETORNADAS: " + count);

  if (count === 50) {
    console.log("ATENÇÃO: o limite de 50 foi atingido.");
    console.log("Pode haver outras contas. Não trate esta amostra como inventário completo.");
  } else if (count === 0) {
    console.log("Nenhuma conta cliente foi retornada nesta hierarquia.");
  } else {
    console.log("A consulta retornou menos de 50 contas.");
  }

  console.log("RESULTADO: somente leitura; nenhuma alteração foi realizada.");
}

function csvCell_(value) {
  var text = String(value == null ? "" : value);
  return '"' + text.replace(/"/g, '""') + '"';
}
