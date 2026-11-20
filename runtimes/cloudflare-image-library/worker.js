const MAX_IMAGE_BYTES = 15 * 1024 * 1024;
const MAX_BATCH_ITEMS = 5;
const RETENTION_MS = 7 * 24 * 60 * 60 * 1000;
const MIME_EXT = {
  "image/jpeg": "jpg",
  "image/png": "png",
  "image/webp": "webp",
  "image/gif": "gif",
  "image/avif": "avif"
};

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "x-content-type-options": "nosniff"
    }
  });
}

function corsHeaders() {
  return {
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET, HEAD, POST, DELETE, OPTIONS",
    "access-control-allow-headers": "Authorization, Content-Type, Accept, MCP-Protocol-Version",
    "access-control-max-age": "86400"
  };
}

async function verifyBearer(request, env) {
  const expected = env.ASSET_API_TOKEN;
  const header = request.headers.get("authorization") || "";
  const match = header.match(/^Bearer\s+(.+)$/i);
  if (!expected || !match) return false;
  const encoder = new TextEncoder();
  const values = await Promise.all([
    crypto.subtle.digest("SHA-256", encoder.encode(match[1].trim())),
    crypto.subtle.digest("SHA-256", encoder.encode(expected))
  ]);
  return crypto.subtle.timingSafeEqual(values[0], values[1]);
}

function blockedIPv4(host) {
  const parts = host.split(".");
  if (parts.length !== 4 || parts.some(p => !/^\d+$/.test(p) || Number(p) > 255)) return false;
  const a = Number(parts[0]), b = Number(parts[1]), c = Number(parts[2]);
  return a === 0 || a === 10 || a === 127 || a >= 224 ||
    (a === 100 && b >= 64 && b <= 127) ||
    (a === 169 && b === 254) ||
    (a === 172 && b >= 16 && b <= 31) ||
    (a === 192 && (b === 168 || (b === 0 && c === 0) || (b === 0 && c === 2))) ||
    (a === 198 && (b === 18 || b === 19 || (b === 51 && c === 100))) ||
    (a === 203 && b === 0 && c === 113);
}

function validateRemoteUrl(raw) {
  let url;
  try {
    url = new URL(raw);
  } catch {
    throw new Error("URL de imagem inválida.");
  }
  if (url.protocol !== "https:" && url.protocol !== "http:") {
    throw new Error("A origem precisa usar HTTP ou HTTPS.");
  }
  if (url.username || url.password) throw new Error("URLs com credenciais embutidas não são aceitas.");
  if (url.port && url.port !== "80" && url.port !== "443") {
    throw new Error("Porta de origem não permitida.");
  }
  const host = url.hostname.toLowerCase().replace(/^\[|\]$/g, "");
  if (!host || host === "localhost" || host.endsWith(".localhost") ||
      host.endsWith(".local") || host.endsWith(".internal") ||
      host.endsWith(".test") || host.endsWith(".invalid") ||
      host === "metadata.google.internal") {
    throw new Error("Host local ou reservado não permitido.");
  }
  if (host.includes(":")) throw new Error("IP IPv6 literal não permitido.");
  if (/^\d{1,3}(\.\d{1,3}){3}$/.test(host) && blockedIPv4(host)) {
    throw new Error("Endereço IP privado ou reservado não permitido.");
  }
  url.hash = "";
  return url;
}

function safeStoredUrl(raw) {
  const url = validateRemoteUrl(raw);
  const hadQuery = Boolean(url.search);
  url.search = "";
  url.hash = "";
  return { value: url.toString(), queryRemoved: hadQuery };
}

function cleanText(value, maxLength, fallback) {
  if (typeof value !== "string") return fallback || null;
  const text = value.trim().slice(0, maxLength);
  return text || (fallback || null);
}

function sourceFilename(url, extension) {
  let candidate = "";
  try {
    const parsed = new URL(url);
    candidate = decodeURIComponent(parsed.pathname.split("/").filter(Boolean).pop() || "");
  } catch {
    candidate = "";
  }
  candidate = candidate.normalize("NFKD").replace(/[\u0300-\u036f]/g, "");
  candidate = candidate.replace(/[^a-zA-Z0-9._-]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 100);
  if (!candidate || candidate === "." || candidate === "..") candidate = "image";
  candidate = candidate.replace(/\.(jpe?g|png|webp|gif|avif)$/i, "");
  return candidate + "." + extension;
}

function sniffImage(bytes) {
  if (bytes.length >= 8 &&
      bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4e && bytes[3] === 0x47 &&
      bytes[4] === 0x0d && bytes[5] === 0x0a && bytes[6] === 0x1a && bytes[7] === 0x0a) {
    return "image/png";
  }
  if (bytes.length >= 3 && bytes[0] === 0xff && bytes[1] === 0xd8 && bytes[2] === 0xff) return "image/jpeg";
  if (bytes.length >= 12 &&
      String.fromCharCode(...bytes.slice(0, 4)) === "RIFF" &&
      String.fromCharCode(...bytes.slice(8, 12)) === "WEBP") return "image/webp";
  if (bytes.length >= 6) {
    const sig = String.fromCharCode(...bytes.slice(0, 6));
    if (sig === "GIF87a" || sig === "GIF89a") return "image/gif";
  }
  if (bytes.length >= 12 && String.fromCharCode(...bytes.slice(4, 8)) === "ftyp") {
    const brand = String.fromCharCode(...bytes.slice(8, 12));
    if (brand === "avif" || brand === "avis") return "image/avif";
  }
  return null;
}

async function readBoundedBody(response) {
  if (!response.body) throw new Error("A origem retornou um corpo vazio.");
  const length = Number(response.headers.get("content-length") || 0);
  if (length > MAX_IMAGE_BYTES) throw new Error("Imagem excede o limite de 15 MB.");
  const reader = response.body.getReader();
  const chunks = [];
  let total = 0;
  try {
    while (true) {
      const part = await reader.read();
      if (part.done) break;
      total += part.value.byteLength;
      if (total > MAX_IMAGE_BYTES) {
        await reader.cancel();
        throw new Error("Imagem excede o limite de 15 MB.");
      }
      chunks.push(part.value);
    }
  } finally {
    try { reader.releaseLock(); } catch {}
  }
  const result = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    result.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return result;
}

async function fetchSourceImage(rawUrl) {
  let current = validateRemoteUrl(rawUrl);
  for (let hop = 0; hop <= 4; hop++) {
    const response = await fetch(current.toString(), {
      method: "GET",
      redirect: "manual",
      headers: {
        "accept": "image/avif,image/webp,image/png,image/jpeg,image/gif;q=0.9,*/*;q=0.1",
        "user-agent": "TS-Digitais-Image-Library/1.0"
      }
    });
    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const location = response.headers.get("location");
      if (!location || hop === 4) throw new Error("Redirecionamento de imagem inválido ou excessivo.");
      current = validateRemoteUrl(new URL(location, current).toString());
      continue;
    }
    if (!response.ok) throw new Error("A origem recusou o download (HTTP " + response.status + ").");
    const bytes = await readBoundedBody(response);
    const contentType = sniffImage(bytes);
    if (!contentType) throw new Error("O arquivo não foi reconhecido como JPEG, PNG, WebP, GIF ou AVIF. SVG e HTML não são aceitos.");
    return {
      bytes,
      contentType,
      extension: MIME_EXT[contentType],
      sourceHost: current.hostname
    };
  }
  throw new Error("Não foi possível obter a imagem da origem.");
}

async function getAsset(env, id) {
  return await env.DB.prepare("SELECT * FROM assets WHERE id = ?1").bind(id).first();
}

function presentAsset(row, origin) {
  if (!row) return null;
  const active = row.status === "active" && Number(row.expires_at) > Date.now();
  return {
    id: row.id,
    project: row.project,
    filename: row.filename,
    content_type: row.content_type,
    size_bytes: row.size_bytes,
    source_url: row.source_url,
    source_page_url: row.source_page_url,
    license: row.license,
    attribution: row.attribution,
    created_at: new Date(Number(row.created_at)).toISOString(),
    expires_at: new Date(Number(row.expires_at)).toISOString(),
    status: active ? "active" : (row.status === "deleted" ? "deleted" : "expired"),
    file_url: active ? origin + "/file/" + row.id : null,
    recovery_note: row.recovery_note,
    recovered_from: row.recovered_from
  };
}

async function markExpired(env, id) {
  await env.DB.prepare("UPDATE assets SET status = 'expired' WHERE id = ?1 AND status = 'active'").bind(id).run();
}

async function importImage(env, origin, input, recoveredFrom) {
  if (!input || typeof input.url !== "string") throw new Error("Informe a URL pública da imagem.");
  const stored = safeStoredUrl(input.url);
  const project = cleanText(input.project, 80, "general");
  const license = cleanText(input.license, 160, "unknown");
  const attribution = cleanText(input.attribution, 240, null);
  const sourcePage = input.source_page_url ? safeStoredUrl(input.source_page_url).value : null;

  const existing = await env.DB.prepare(
    "SELECT * FROM assets WHERE project = ?1 AND source_url = ?2 AND status = 'active' AND expires_at > ?3 ORDER BY created_at DESC LIMIT 1"
  ).bind(project, stored.value, Date.now()).first();
  if (existing) {
    const item = presentAsset(existing, origin);
    item.reused = true;
    return item;
  }

  const remote = await fetchSourceImage(input.url);
  const id = crypto.randomUUID();
  const objectKey = "images/" + id + "." + remote.extension;
  const now = Date.now();
  const expiresAt = now + RETENTION_MS;
  const filename = sourceFilename(input.url, remote.extension);
  const recoveryNote = stored.queryRemoved
    ? "A query string original foi removida do registro por segurança; se a origem usar URL assinada, talvez seja necessário fornecer um novo link para recuperar."
    : null;

  await env.ASSETS.put(objectKey, remote.bytes, {
    httpMetadata: {
      contentType: remote.contentType,
      cacheControl: "public, max-age=300, s-maxage=300"
    },
    customMetadata: {
      assetId: id,
      project: project,
      createdAt: String(now),
      expiresAt: String(expiresAt),
      sourceHost: remote.sourceHost
    }
  });

  try {
    await env.DB.prepare(
      "INSERT INTO assets (id, project, source_url, source_page_url, filename, content_type, size_bytes, license, attribution, created_at, expires_at, object_key, status, recovered_from, recovery_note) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, 'active', ?13, ?14)"
    ).bind(
      id, project, stored.value, sourcePage, filename, remote.contentType,
      remote.bytes.byteLength, license, attribution, now, expiresAt,
      objectKey, recoveredFrom || null, recoveryNote
    ).run();
  } catch (error) {
    await env.ASSETS.delete(objectKey);
    throw error;
  }

  const row = await getAsset(env, id);
  return presentAsset(row, origin);
}

async function searchAssets(env, origin, args) {
  const now = Date.now();
  await env.DB.prepare("UPDATE assets SET status = 'expired' WHERE status = 'active' AND expires_at <= ?1").bind(now).run();
  let sql = "SELECT * FROM assets WHERE 1 = 1";
  const params = [];
  if (args.project) {
    sql += " AND project = ?";
    params.push(cleanText(args.project, 80, "general"));
  }
  if (args.status) {
    if (args.status === "active") {
      sql += " AND status = 'active' AND expires_at > ?";
      params.push(now);
    } else {
      sql += " AND status = ?";
      params.push(args.status);
    }
  }
  if (args.q) {
    sql += " AND (LOWER(filename) LIKE ? OR LOWER(source_url) LIKE ? OR LOWER(attribution) LIKE ?)";
    const term = "%" + String(args.q).toLowerCase().slice(0, 120) + "%";
    params.push(term, term, term);
  }
  const limit = Math.max(1, Math.min(50, Number(args.limit) || 20));
  sql += " ORDER BY created_at DESC LIMIT ?";
  params.push(limit);
  const result = await env.DB.prepare(sql).bind(...params).all();
  return (result.results || []).map(row => presentAsset(row, origin));
}

async function deleteAsset(env, id) {
  const row = await getAsset(env, id);
  if (!row) throw new Error("Asset não encontrado.");
  if (row.object_key) await env.ASSETS.delete(row.object_key);
  await env.DB.prepare("UPDATE assets SET status = 'deleted' WHERE id = ?1").bind(id).run();
  return { id: id, status: "deleted", file_removed: true };
}

async function recoverAsset(env, origin, id) {
  const row = await getAsset(env, id);
  if (!row) throw new Error("Referência não encontrada.");
  if (row.status === "active" && Number(row.expires_at) > Date.now()) {
    return presentAsset(row, origin);
  }
  const recovered = await importImage(env, origin, {
    url: row.source_url,
    project: row.project,
    source_page_url: row.source_page_url,
    license: row.license,
    attribution: row.attribution
  }, row.id);
  return recovered;
}

function toolDefinitions() {
  return [
    {
      name: "import_image",
      description: "Baixa uma imagem raster pública e a guarda temporariamente por 7 dias no R2. Informe a licença/atribuição apenas quando verificadas; nunca presuma autorização comercial.",
      inputSchema: {
        type: "object",
        properties: {
          url: { type: "string", description: "URL direta da imagem pública." },
          project: { type: "string", description: "Projeto/pasta lógica, por exemplo guardian, tsdigitais ou general." },
          source_page_url: { type: "string", description: "Página editorial de origem e contexto/crédito." },
          license: { type: "string", description: "Licença verificada ou unknown." },
          attribution: { type: "string", description: "Crédito exigido pelo autor/fonte, se conhecido." }
        },
        required: ["url"]
      },
      annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true }
    },
    {
      name: "import_images_batch",
      description: "Importa até 5 imagens públicas raster em uma única chamada; cada cópia expira em 7 dias.",
      inputSchema: {
        type: "object",
        properties: {
          items: {
            type: "array",
            minItems: 1,
            maxItems: 5,
            items: {
              type: "object",
              properties: {
                url: { type: "string" },
                project: { type: "string" },
                source_page_url: { type: "string" },
                license: { type: "string" },
                attribution: { type: "string" }
              },
              required: ["url"]
            }
          }
        },
        required: ["items"]
      },
      annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true }
    },
    {
      name: "search_assets",
      description: "Pesquisa referências de assets, inclusive expirados. O catálogo conserva apenas metadados e URLs de origem; não mantém a fotografia após a expiração.",
      inputSchema: {
        type: "object",
        properties: {
          project: { type: "string" },
          status: { type: "string", enum: ["active", "expired", "deleted"] },
          q: { type: "string" },
          limit: { type: "integer", minimum: 1, maximum: 50 }
        }
      },
      annotations: { readOnlyHint: true, destructiveHint: false }
    },
    {
      name: "get_asset",
      description: "Obtém os metadados de um asset e a URL temporária, quando ainda disponível.",
      inputSchema: { type: "object", properties: { id: { type: "string" } }, required: ["id"] },
      annotations: { readOnlyHint: true, destructiveHint: false }
    },
    {
      name: "recover_asset",
      description: "Tenta baixar novamente a imagem pela URL de origem guardada. Só funciona se a origem ainda estiver pública e disponível; cria uma nova cópia com novo prazo de 7 dias.",
      inputSchema: { type: "object", properties: { id: { type: "string" } }, required: ["id"] },
      annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true }
    },
    {
      name: "delete_asset",
      description: "Exclui imediatamente o arquivo do R2 e marca a referência como apagada.",
      inputSchema: { type: "object", properties: { id: { type: "string" } }, required: ["id"] },
      annotations: { readOnlyHint: false, destructiveHint: true }
    }
  ];
}

async function callTool(env, origin, name, args) {
  if (name === "import_image") return await importImage(env, origin, args);
  if (name === "import_images_batch") {
    const items = Array.isArray(args.items) ? args.items : [];
    if (!items.length || items.length > MAX_BATCH_ITEMS) throw new Error("O lote precisa conter entre 1 e 5 imagens.");
    const results = [];
    for (const item of items) {
      try {
        results.push({ ok: true, asset: await importImage(env, origin, item) });
      } catch (error) {
        results.push({ ok: false, error: error instanceof Error ? error.message : "Falha na importação." });
      }
    }
    return { results: results, imported: results.filter(x => x.ok).length, failed: results.filter(x => !x.ok).length };
  }
  if (name === "search_assets") return await searchAssets(env, origin, args);
  if (name === "get_asset") {
    const row = await getAsset(env, String(args.id || ""));
    if (!row) throw new Error("Asset não encontrado.");
    if (row.status === "active" && Number(row.expires_at) <= Date.now()) await markExpired(env, row.id);
    const refreshed = await getAsset(env, row.id);
    return presentAsset(refreshed, origin);
  }
  if (name === "recover_asset") return await recoverAsset(env, origin, String(args.id || ""));
  if (name === "delete_asset") return await deleteAsset(env, String(args.id || ""));
  throw new Error("Ferramenta MCP desconhecida: " + name);
}

async function handleMcp(request, env, origin) {
  if (!await verifyBearer(request, env)) {
    return new Response(JSON.stringify({ error: "Unauthorized" }), {
      status: 401,
      headers: { "content-type": "application/json", "www-authenticate": "Bearer" }
    });
  }
  let message;
  try {
    message = await request.json();
  } catch {
    return json({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } }, 400);
  }
  const id = message && Object.prototype.hasOwnProperty.call(message, "id") ? message.id : null;
  const method = message && message.method;
  if (!method) return json({ jsonrpc: "2.0", id: id, error: { code: -32600, message: "Invalid Request" } }, 400);
  if (method === "notifications/initialized" || method.startsWith("notifications/")) {
    return new Response(null, { status: 202 });
  }
  if (method === "initialize") {
    const requested = message.params && message.params.protocolVersion;
    return json({
      jsonrpc: "2.0",
      id: id,
      result: {
        protocolVersion: requested || "2025-03-26",
        capabilities: { tools: {} },
        serverInfo: { name: "ts-image-library", version: "1.0.0" },
        instructions: "Asset library temporária da TS Digitais. Imagens são removidas do R2 após 7 dias; metadados mínimos e URLs de origem ficam no catálogo."
      }
    });
  }
  if (method === "ping") return json({ jsonrpc: "2.0", id: id, result: {} });
  if (method === "tools/list") {
    return json({ jsonrpc: "2.0", id: id, result: { tools: toolDefinitions() } });
  }
  if (method === "tools/call") {
    const name = message.params && message.params.name;
    const args = (message.params && message.params.arguments) || {};
    try {
      const data = await callTool(env, origin, name, args);
      return json({
        jsonrpc: "2.0",
        id: id,
        result: { content: [{ type: "text", text: JSON.stringify(data) }], isError: false }
      });
    } catch (error) {
      return json({
        jsonrpc: "2.0",
        id: id,
        result: {
          content: [{ type: "text", text: error instanceof Error ? error.message : "Erro na ferramenta." }],
          isError: true
        }
      });
    }
  }
  return json({ jsonrpc: "2.0", id: id, error: { code: -32601, message: "Method not found" } }, 404);
}

async function handleFile(request, env, id) {
  if (!/^[0-9a-f-]{36}$/i.test(id)) return new Response("Not found", { status: 404 });
  const row = await getAsset(env, id);
  if (!row || row.status !== "active") return new Response("Not found", { status: 404 });
  if (Number(row.expires_at) <= Date.now()) {
    await markExpired(env, id);
    return new Response("Asset expired", { status: 410 });
  }
  const object = await env.ASSETS.get(row.object_key);
  if (!object) {
    await markExpired(env, id);
    return new Response("Asset expired", { status: 410 });
  }
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", row.content_type);
  headers.set("content-length", String(object.size));
  headers.set("etag", object.httpEtag);
  headers.set("cache-control", "public, max-age=300, s-maxage=300");
  headers.set("access-control-allow-origin", "*");
  headers.set("x-content-type-options", "nosniff");
  headers.set("content-disposition", 'inline; filename="' + row.filename.replace(/["\\\r\n]/g, "_") + '"');
  return new Response(request.method === "HEAD" ? null : object.body, { status: 200, headers: headers });
}

async function handleApi(request, env, origin, url) {
  if (!await verifyBearer(request, env)) {
    return json({ error: "Unauthorized" }, 401);
  }
  if (request.method === "POST" && url.pathname === "/api/import") {
    const body = await request.json();
    return json({ asset: await importImage(env, origin, body) }, 201);
  }
  if (request.method === "POST" && url.pathname === "/api/import-batch") {
    const body = await request.json();
    const items = Array.isArray(body.items) ? body.items : [];
    if (!items.length || items.length > MAX_BATCH_ITEMS) return json({ error: "O lote precisa conter entre 1 e 5 imagens." }, 400);
    const results = [];
    for (const item of items) {
      try { results.push({ ok: true, asset: await importImage(env, origin, item) }); }
      catch (error) { results.push({ ok: false, error: error instanceof Error ? error.message : "Falha na importação." }); }
    }
    return json({ results: results, imported: results.filter(x => x.ok).length, failed: results.filter(x => !x.ok).length });
  }
  if (request.method === "GET" && url.pathname === "/api/assets") {
    const assets = await searchAssets(env, origin, {
      project: url.searchParams.get("project"),
      status: url.searchParams.get("status"),
      q: url.searchParams.get("q"),
      limit: Number(url.searchParams.get("limit") || 20)
    });
    return json({ assets: assets });
  }
  const match = url.pathname.match(/^\/api\/assets\/([0-9a-f-]{36})$/i);
  if (match && request.method === "GET") {
    const row = await getAsset(env, match[1]);
    if (!row) return json({ error: "Asset não encontrado." }, 404);
    if (row.status === "active" && Number(row.expires_at) <= Date.now()) await markExpired(env, row.id);
    return json({ asset: presentAsset(await getAsset(env, row.id), origin) });
  }
  if (match && request.method === "DELETE") return json(await deleteAsset(env, match[1]));
  const recoverMatch = url.pathname.match(/^\/api\/recover\/([0-9a-f-]{36})$/i);
  if (recoverMatch && request.method === "POST") {
    return json({ asset: await recoverAsset(env, origin, recoverMatch[1]) }, 201);
  }
  return json({ error: "Endpoint não encontrado." }, 404);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = url.origin;
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders() });
    if (url.pathname === "/healthz" && request.method === "GET") {
      return json({ ok: true, service: "ts-image-library", retention_days: 7, max_image_bytes: MAX_IMAGE_BYTES });
    }
    if (url.pathname === "/mcp" && request.method === "POST") return await handleMcp(request, env, origin);
    if (url.pathname === "/mcp") return new Response("POST required", { status: 405, headers: { allow: "POST" } });
    if (url.pathname.startsWith("/file/") && (request.method === "GET" || request.method === "HEAD")) {
      return await handleFile(request, env, url.pathname.slice("/file/".length));
    }
    if (url.pathname.startsWith("/api/") && (request.method === "GET" || request.method === "POST" || request.method === "DELETE")) {
      try {
        return await handleApi(request, env, origin, url);
      } catch (error) {
        console.error(JSON.stringify({
          message: "asset API request failed",
          route: url.pathname,
          error: error instanceof Error ? error.message : "unknown"
        }));
        return json({ error: error instanceof Error ? error.message : "Erro interno." }, 400);
      }
    }
    return json({ error: "Not found" }, 404);
  }
};