const ISSUER = "https://token.actions.githubusercontent.com";
const AUDIENCE = "ts-visual-library";
const REPOSITORY = "Tiagocxs1/tsagents-skills";
const REPOSITORY_ID = "1303307316";
const OWNER = "Tiagocxs1";
const OWNER_ID = "17513166";
const ALLOWED_WORKFLOWS = [
  {
    ref: "refs/heads/main",
    workflow: "Tiagocxs1/tsagents-skills/.github/workflows/visual-library-sync.yml@refs/heads/main"
  }
];
let jwksCache = null;
let jwksExpires = 0;
const VERSION="1.0.0";
const INDEX_KEY="catalog/index.json";
const MAX_UPLOAD_BYTES=25*1024*1024;
let indexCache=null,indexCacheAt=0;
async function j(data,status=200,extra={}) {
 return new Response(JSON.stringify(data),{status,headers:{
  "content-type":"application/json; charset=utf-8","cache-control":"no-store",
  "x-content-type-options":"nosniff","access-control-allow-origin":"*",
  "access-control-allow-methods":"GET,HEAD,POST,PUT,OPTIONS",
  "access-control-allow-headers":"Authorization,Content-Type,MCP-Protocol-Version,X-Asset-Sha256",...extra}});
}
function cors(){return {"access-control-allow-origin":"*","access-control-allow-methods":"GET,HEAD,POST,PUT,OPTIONS","access-control-allow-headers":"Authorization,Content-Type,MCP-Protocol-Version,X-Asset-Sha256","access-control-max-age":"86400"};}
function safeKey(k,prefix){if(typeof k!=="string"||!k||k.length>900||k.startsWith("/")||k.includes("\\")||k.includes("\0"))return false;const p=k.split("/");return k.startsWith(prefix)&&!p.some(x=>!x||x==="."||x==="..");}
async function loadIndex(env){if(indexCache&&Date.now()-indexCacheAt<300000)return indexCache;const o=await env.ASSETS.get(INDEX_KEY);if(!o)throw new Error("Catalog index missing.");const v=await o.json();if(!Array.isArray(v.assets)||!Array.isArray(v.collections))throw new Error("Catalog index invalid.");indexCache=v;indexCacheAt=Date.now();return v;}
function terms(v){return String(v||"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().split(/[^a-z0-9]+/).filter(x=>x.length>1);}
function find(index,p){
 const q=terms(p.q),out=[],collection=String(p.collection||""),style=String(p.style||"").toLowerCase(),license=String(p.license||""),format=String(p.format||"").toUpperCase(),limit=Math.max(1,Math.min(48,Number(p.limit)||24));
 for(const a of index.assets){
  if(collection&&a.collection!==collection)continue;
  if(license&&a.license!==license)continue;
  if(format&&a.format!==format)continue;
  if(style&&!String(a.style||"").toLowerCase().includes(style)&&!(a.tags||[]).some(x=>String(x).toLowerCase().includes(style)))continue;
  if(!["CC0-1.0","MIT"].includes(a.license)||a.commercial_use_confirmed!==true)continue;
  const blob=a.search_blob||String(a.name||"").toLowerCase();
  let score=0;for(const t of q)if(blob.includes(t))score++;
  if(q.length&&score===0)continue;
  out.push({score,asset:a});
 }
 out.sort((a,b)=>b.score-a.score||String(a.asset.name).localeCompare(String(b.asset.name)));
 return out.slice(0,limit).map(x=>x.asset);
}
function expose(a,origin){return {...a,file_url:origin+"/file?key="+encodeURIComponent(a.file_key),preview_url:origin+"/file?key="+encodeURIComponent(a.preview_key||a.file_key)};}
function decodePart(value) {
 const text=value.replace(/-/g,"+").replace(/_/g,"/");
 const padded=text+"=".repeat((4-text.length%4)%4);
 return Uint8Array.from(atob(padded),c=>c.charCodeAt(0));
}
function decodeJson(value){return JSON.parse(new TextDecoder().decode(decodePart(value)));}
async function getJwks(){
 if(jwksCache&&Date.now()<jwksExpires)return jwksCache;
 const r=await fetch(ISSUER+"/.well-known/jwks",{headers:{accept:"application/json"},cf:{cacheTtl:300,cacheEverything:true}});
 if(!r.ok)throw new Error("Unable to retrieve GitHub OIDC signing keys.");
 jwksCache=await r.json();jwksExpires=Date.now()+300000;return jwksCache;
}
async function verifyGithubOidc(request){
 const m=(request.headers.get("authorization")||"").match(/^Bearer\s+([A-Za-z0-9._-]+)$/);
 if(!m)return null;
 const parts=m[1].split(".");if(parts.length!==3)return null;
 let h,c;try{h=decodeJson(parts[0]);c=decodeJson(parts[1]);}catch{return null;}
 if(h.alg!=="RS256"||!h.kid)return null;
 const now=Math.floor(Date.now()/1000),aud=Array.isArray(c.aud)?c.aud:[c.aud];
 if(c.iss!==ISSUER||!aud.includes(AUDIENCE))return null;
 if(c.repository!==REPOSITORY||String(c.repository_id)!==REPOSITORY_ID)return null;
 if(c.repository_owner!==OWNER||String(c.repository_owner_id)!==OWNER_ID)return null;
 const allowed=ALLOWED_WORKFLOWS.some(item=>{
  const expected="repo:"+OWNER+"@"+OWNER_ID+"/"+REPOSITORY.split("/")[1]+"@"+REPOSITORY_ID+":ref:"+item.ref;
  const legacy="repo:"+REPOSITORY+":ref:"+item.ref;
  return c.ref===item.ref && c.workflow_ref===item.workflow && (c.sub===expected || c.sub===legacy);
 });
 if(!allowed)return null;
 if(Number(c.exp)<now||Number(c.iat)>now+60)return null;
 const keys=await getJwks(),key=(keys.keys||[]).find(x=>x.kid===h.kid);if(!key)return null;
 try{
  const publicKey=await crypto.subtle.importKey("jwk",key,{name:"RSASSA-PKCS1-v1_5",hash:"SHA-256"},false,["verify"]);
  const signed=new TextEncoder().encode(parts[0]+"."+parts[1]);
  const ok=await crypto.subtle.verify("RSASSA-PKCS1-v1_5",publicKey,decodePart(parts[2]),signed);
  return ok?c:null;
 }catch{return null;}
}
async function upload(req,env,url){const claims=await verifyGithubOidc(req);if(!claims)return j({error:"Unauthorized GitHub Actions OIDC token"},401,{"www-authenticate":"Bearer"});const key=url.searchParams.get("key")||"";if(!safeKey(key,"assets/v1/")&&!safeKey(key,"catalog/"))return j({error:"Invalid key"},400);const n=Number(req.headers.get("content-length")||0);if(!req.body||n<=0||n>MAX_UPLOAD_BYTES)return j({error:"Upload must be 1 byte–25 MiB"},413);const type=(req.headers.get("content-type")||"application/octet-stream").split(";")[0],sha=req.headers.get("x-asset-sha256")||"";await env.ASSETS.put(key,req.body,{httpMetadata:{contentType:type,cacheControl:key.startsWith("assets/v1/")?"public, max-age=86400":"public, max-age=300"},customMetadata:{sha256:sha,source:"curated-public-library-v1",repository:claims.repository,workflow:claims.workflow_ref,runId:claims.run_id||""}});return j({ok:true,key,size:n,contentType:type},201);}
async function file(req,env,url){const key=url.searchParams.get("key")||"";if(!safeKey(key,"assets/v1/"))return j({error:"Not found"},404);const o=await env.ASSETS.get(key);if(!o)return j({error:"Not found"},404);const h=new Headers();o.writeHttpMetadata(h);h.set("etag",o.httpEtag);h.set("x-content-type-options","nosniff");h.set("cache-control","public, max-age=86400");h.set("access-control-allow-origin","*");if(key.toLowerCase().endsWith(".svg"))h.set("content-security-policy","default-src 'none'; img-src data:; style-src 'unsafe-inline'; object-src 'none'; base-uri 'none';");return new Response(req.method==="HEAD"?null:o.body,{status:200,headers:h});}
function tools(){return [
 {name:"search_visual_assets",description:"Search the online public library of CC0/MIT SVG illustrations, characters, objects, scenes and textures. Returns licence, source and master/preview URLs. Private and licence-pending assets are excluded.",inputSchema:{type:"object",properties:{query:{type:"string"},collection:{type:"string"},style:{type:"string"},license:{type:"string",enum:["CC0-1.0","MIT"]},format:{type:"string",enum:["SVG","PNG","JPG"]},limit:{type:"integer",minimum:1,maximum:20}},required:["query"]}},
 {name:"get_visual_asset",description:"Get metadata and public URLs for one asset ID.",inputSchema:{type:"object",properties:{asset_id:{type:"string"}},required:["asset_id"]}},
 {name:"list_asset_collections",description:"List online public collections and their licenses/counts.",inputSchema:{type:"object",properties:{},additionalProperties:false}}
];}
async function callTool(name,args,index,origin){if(name==="list_asset_collections")return {collections:index.collections,asset_count:index.asset_count,file_count:index.file_count};if(name==="search_visual_assets"){const a=find(index,{q:args.query,collection:args.collection,style:args.style,license:args.license,format:args.format,limit:args.limit||20});return {query:args.query,result_count:a.length,results:a.map(x=>expose(x,origin))};}if(name==="get_visual_asset"){const a=index.assets.find(x=>x.id===String(args.asset_id||""));if(!a)throw new Error("Asset not found");return expose(a,origin);}throw new Error("Unknown read-only tool");}
async function mcp(req,env,origin){let m;try{m=await req.json();}catch{return j({jsonrpc:"2.0",id:null,error:{code:-32700,message:"Parse error"}},400);}const id=Object.prototype.hasOwnProperty.call(m,"id")?m.id:null,method=m.method;if(!method)return j({jsonrpc:"2.0",id,error:{code:-32600,message:"Invalid request"}},400);if(method.startsWith("notifications/")||id===null)return new Response(null,{status:202,headers:cors()});if(method==="initialize")return j({jsonrpc:"2.0",id,result:{protocolVersion:"2025-03-26",capabilities:{tools:{}},serverInfo:{name:"ts-visual-library",version:VERSION}}});if(method==="ping")return j({jsonrpc:"2.0",id,result:{}});if(method==="tools/list")return j({jsonrpc:"2.0",id,result:{tools:tools()}});if(method==="tools/call"){try{const i=await loadIndex(env),r=await callTool(String(m.params?.name||""),m.params?.arguments||{},i,origin);return j({jsonrpc:"2.0",id,result:{content:[{type:"text",text:JSON.stringify(r)}],structuredContent:r,isError:false}});}catch(e){return j({jsonrpc:"2.0",id,result:{content:[{type:"text",text:e.message||"Tool failed"}],isError:true}});}}return j({jsonrpc:"2.0",id,error:{code:-32601,message:"Method not found"}},404);}
export default {async fetch(req,env){const u=new URL(req.url),origin=u.origin;if(req.method==="OPTIONS")return new Response(null,{status:204,headers:cors()});if(u.pathname==="/"&&req.method==="GET"){const o=await env.ASSETS.get("catalog/index.html");if(!o)return j({error:"Catalog UI missing"},503);return new Response(o.body,{headers:{"content-type":"text/html; charset=utf-8","cache-control":"public, max-age=300","x-content-type-options":"nosniff"}});}if(u.pathname==="/health"&&req.method==="GET"){try{const i=await loadIndex(env);return j({ok:true,service:"ts-visual-library",version:VERSION,asset_count:i.asset_count,file_count:i.file_count,collections:i.collections.length});}catch(e){return j({ok:false,error:e.message},503);}}if(u.pathname==="/api/collections"&&req.method==="GET"){const i=await loadIndex(env);return j({collections:i.collections,asset_count:i.asset_count,file_count:i.file_count,total_bytes:i.total_bytes});}if(u.pathname==="/api/search"&&req.method==="GET"){const i=await loadIndex(env),a=find(i,{q:u.searchParams.get("q"),collection:u.searchParams.get("collection"),style:u.searchParams.get("style"),license:u.searchParams.get("license"),format:u.searchParams.get("format"),limit:u.searchParams.get("limit")});return j({result_count:a.length,results:a.map(x=>expose(x,origin))});}if(u.pathname==="/file"&&(req.method==="GET"||req.method==="HEAD"))return file(req,env,u);if(u.pathname==="/upload"&&req.method==="PUT")return upload(req,env,u);if(u.pathname==="/mcp"&&req.method==="POST")return mcp(req,env,origin);if(u.pathname==="/mcp")return new Response("POST required",{status:405,headers:{allow:"POST"}});return j({error:"Not found"},404);}};
