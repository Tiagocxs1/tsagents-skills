const ISSUER = "https://token.actions.githubusercontent.com";
const AUDIENCE = "ts-svg-assets";
const REPOSITORY = "Tiagocxs1/tsagents-skills";
const REPOSITORY_ID = "1303307316";
const OWNER = "Tiagocxs1";
const OWNER_ID = "17513166";
const WORKFLOW = "Tiagocxs1/tsagents-skills/.github/workflows/vector-studio.yml@refs/heads/main";
const EXPECTED_SUBJECT = "repo:Tiagocxs1@17513166/tsagents-skills@1303307316:ref:refs/heads/main";
const LEGACY_SUBJECT = "repo:Tiagocxs1/tsagents-skills:ref:refs/heads/main";
const PREFIX = "images/vector-studio/";
const MAX_BYTES = 20 * 1024 * 1024;
let jwksCache = null;
let jwksExpires = 0;

function json(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "x-content-type-options": "nosniff",
      "access-control-allow-origin": "*"
    }
  });
}

function decodePart(value) {
  const text = value.replace(/-/g, "+").replace(/_/g, "/");
  const padded = text + "=".repeat((4 - text.length % 4) % 4);
  return Uint8Array.from(atob(padded), char => char.charCodeAt(0));
}

function decodeJson(value) {
  return JSON.parse(new TextDecoder().decode(decodePart(value)));
}

async function getJwks() {
  if (jwksCache && Date.now() < jwksExpires) return jwksCache;
  const response = await fetch(ISSUER + "/.well-known/jwks", {
    headers: { accept: "application/json" },
    cf: { cacheTtl: 300, cacheEverything: true }
  });
  if (!response.ok) throw new Error("Unable to retrieve GitHub OIDC signing keys.");
  jwksCache = await response.json();
  jwksExpires = Date.now() + 300000;
  return jwksCache;
}

async function verifyGithubOidc(request) {
  const match = (request.headers.get("authorization") || "").match(/^Bearer\s+([A-Za-z0-9._-]+)$/);
  if (!match) return null;

  const parts = match[1].split(".");
  if (parts.length !== 3) return null;

  let jwtHeader;
  let claims;
  try {
    jwtHeader = decodeJson(parts[0]);
    claims = decodeJson(parts[1]);
  } catch {
    return null;
  }

  if (jwtHeader.alg !== "RS256" || !jwtHeader.kid) return null;

  const now = Math.floor(Date.now() / 1000);
  const audience = Array.isArray(claims.aud) ? claims.aud : [claims.aud];

  if (claims.iss !== ISSUER || !audience.includes(AUDIENCE)) return null;
  if (claims.sub !== EXPECTED_SUBJECT && claims.sub !== LEGACY_SUBJECT) return null;
  if (claims.repository !== REPOSITORY || String(claims.repository_id) !== REPOSITORY_ID) return null;
  if (claims.repository_owner !== OWNER || String(claims.repository_owner_id) !== OWNER_ID) return null;
  if (claims.ref !== "refs/heads/main" || claims.workflow_ref !== WORKFLOW) return null;
  if (Number(claims.exp) < now || Number(claims.iat) > now + 60) return null;

  const jwks = await getJwks();
  const jwk = (jwks.keys || []).find(key => key.kid === jwtHeader.kid);
  if (!jwk) return null;

  try {
    const publicKey = await crypto.subtle.importKey(
      "jwk",
      jwk,
      { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
      false,
      ["verify"]
    );
    const signed = new TextEncoder().encode(parts[0] + "." + parts[1]);
    const valid = await crypto.subtle.verify(
      "RSASSA-PKCS1-v1_5",
      publicKey,
      decodePart(parts[2]),
      signed
    );
    return valid ? claims : null;
  } catch {
    return null;
  }
}

function allowedMime(name) {
  const extension = name.split(".").pop().toLowerCase();
  const types = {
    svg: "image/svg+xml",
    png: "image/png",
    jpg: "image/jpeg",
    jpeg: "image/jpeg",
    json: "application/json",
    txt: "text/plain; charset=utf-8",
    md: "text/markdown; charset=utf-8"
  };
  return types[extension] || null;
}

function safeName(value) {
  return /^[a-z0-9][a-z0-9._-]{0,127}$/i.test(value) && !value.includes("..");
}

function safeRunId(value) {
  return /^[0-9]{1,24}$/.test(value);
}

function cors() {
  return {
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET, PUT, OPTIONS",
    "access-control-allow-headers": "Authorization, Content-Type",
    "access-control-max-age": "86400",
    vary: "Origin"
  };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors() });
    }

    if (url.pathname === "/healthz" && request.method === "GET") {
      return json({
        ok: true,
        service: "ts-svg-assets",
        storage: "Cloudflare R2",
        retention: "7 days via existing images/ lifecycle rule"
      });
    }

    if (url.pathname.startsWith("/upload/") && request.method === "PUT") {
      const claims = await verifyGithubOidc(request);
      if (!claims) return json({ error: "Unauthorized GitHub Actions OIDC token." }, 401);

      const name = decodeURIComponent(url.pathname.slice("/upload/".length));
      const runId = url.searchParams.get("run_id") || "";
      const contentType = request.headers.get("content-type") || "";
      const expectedType = allowedMime(name);
      const length = Number(request.headers.get("content-length") || 0);

      if (!safeName(name) || !safeRunId(runId) || !expectedType) {
        return json({ error: "Invalid asset path, run id, or extension." }, 400);
      }
      if (contentType.split(";")[0].trim().toLowerCase() !== expectedType.split(";")[0].trim().toLowerCase()) {
        return json({ error: "Content-Type does not match file extension." }, 415);
      }
      if (length <= 0 || length > MAX_BYTES) {
        return json({ error: "Asset must be between 1 byte and 20 MB." }, 413);
      }

      const bytes = await request.arrayBuffer();
      if (bytes.byteLength !== length) return json({ error: "Upload length mismatch." }, 400);

      const key = PREFIX + runId + "/" + name;
      await env.ASSETS.put(key, bytes, {
        httpMetadata: {
          contentType: expectedType,
          cacheControl: "public, max-age=300, s-maxage=300"
        },
        customMetadata: {
          pipeline: "ts-svg-assets",
          repository: REPOSITORY,
          workflowRunId: runId,
          createdAt: new Date().toISOString(),
          expiryPolicy: "existing R2 lifecycle under images/ (7 days)"
        }
      });

      const publicUrl = new URL(
        "/file/" + runId + "/" + encodeURIComponent(name),
        url.origin
      ).toString();

      return json({
        ok: true,
        key,
        filename: name,
        bytes: bytes.byteLength,
        url: publicUrl,
        expires_by_policy: "approximately 7 days"
      }, 201);
    }

    if (url.pathname.startsWith("/file/") && request.method === "GET") {
      const parts = url.pathname.slice("/file/".length).split("/");
      if (parts.length !== 2) return new Response("Not found", { status: 404, headers: cors() });

      const runId = parts[0];
      const name = decodeURIComponent(parts[1]);
      if (!safeRunId(runId) || !safeName(name)) {
        return new Response("Not found", { status: 404, headers: cors() });
      }

      const object = await env.ASSETS.get(PREFIX + runId + "/" + name);
      if (!object) return new Response("Not found or expired", { status: 404, headers: cors() });

      const headers = new Headers(cors());
      object.writeHttpMetadata(headers);
      headers.set("etag", object.httpEtag);
      headers.set("x-content-type-options", "nosniff");
      headers.set("cache-control", "public, max-age=300, s-maxage=300");
      headers.set("content-disposition", 'inline; filename="' + name.replace(/["\\\r\n]/g, "_") + '"');
      if (name.toLowerCase().endsWith(".svg")) {
        headers.set("content-security-policy", "default-src 'none'; img-src data:; style-src 'unsafe-inline';");
      }

      return new Response(request.method === "HEAD" ? null : object.body, {
        status: 200,
        headers
      });
    }

    return json({
      service: "TS Digitais SVG Asset Store",
      endpoints: [
        "/healthz",
        "PUT /upload/{filename}?run_id={github_run_id}",
        "GET /file/{github_run_id}/{filename}"
      ],
      upload_auth: "GitHub Actions OIDC restricted to Tiagocxs1/tsagents-skills main workflow"
    });
  }
};