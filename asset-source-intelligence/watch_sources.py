#!/usr/bin/env python3
"""Cloud-only visual source watcher. Uses public GitHub and Poly Haven APIs only."""
from __future__ import annotations
import json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/"reports/source-watch/state.json"
OUT=Path(os.environ.get("RUNNER_TEMP","/tmp"))/"visual-source-watch"
OUT.mkdir(parents=True,exist_ok=True)
REPORT=OUT/"latest.md"
UA="TS-Digitais-Visual-Source-Watcher/1.0 (https://github.com/Tiagocxs1/tsagents-skills)"
REPOS=[
 {"name":"Remix Icon","repo":"Remix-Design/RemixIcon","branch":"master","release":True},
 {"name":"RemixIcon MCP","repo":"Remix-Design/RemixIcon-MCP","branch":"main","release":True},
 {"name":"Tabler Icons","repo":"tabler/tabler-icons","branch":"main","release":True},
 {"name":"Iconoir","repo":"iconoir-icons/iconoir","branch":"main","release":True},
 {"name":"IRA Design","repo":"ira-design/ira-illustrations","branch":"master","release":False},
 {"name":"Kitbitz Assets","repo":"CaptExcellent/kits-library-assets","branch":"main","release":False},
]
def get_json(url):
    last=None
    for attempt in range(4):
        req=Request(url,headers={"User-Agent":UA,"Accept":"application/vnd.github+json"})
        try:
            with urlopen(req,timeout=30) as r:
                return json.loads(r.read().decode("utf-8")),r.headers.get("ETag")
        except HTTPError as e:
            if e.code==404:return None,None
            if e.code in (403,429,500,502,503,504):
                last=f"HTTP {e.code}: {e.read(500).decode('utf-8','replace')}"
                time.sleep(min(2**attempt,8));continue
            raise
        except (URLError,TimeoutError) as e:
            last=str(e);time.sleep(min(2**attempt,8))
    raise RuntimeError(f"Request failed: {url}: {last}")

old=json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
new={"schema":1,"repos":{},"polyhaven":{}}
changes=[];errors=[];baselining=not bool(old.get("repos"))
for cfg in REPOS:
    repo=cfg["repo"]; previous=old.get("repos",{}).get(repo,{})
    record={"name":cfg["name"],"repo":repo,"branch":cfg["branch"]}
    if cfg["release"]:
        try:
            release,_=get_json(f"https://api.github.com/repos/{repo}/releases/latest")
            snap=None if not release else {
                "tag":release.get("tag_name"),"published_at":release.get("published_at"),
                "html_url":release.get("html_url"),"name":release.get("name")}
            record["release"]=snap
            if previous and previous.get("release")!=snap and snap:
                changes.append({"type":"release","name":cfg["name"],"old":previous.get("release",{}).get("tag") if previous.get("release") else None,
                    "new":snap.get("tag"),"url":snap.get("html_url")})
        except Exception as e:
            errors.append({"repo":repo,"endpoint":"release","error":str(e)})
            record["release"]=previous.get("release")
    try:
        commit,_=get_json(f"https://api.github.com/repos/{repo}/commits/{cfg['branch']}")
        if not commit:raise RuntimeError("No commit response")
        c=commit.get("commit",{})
        snap={"sha":commit.get("sha"),"short_sha":(commit.get("sha") or "")[:12],
              "date":c.get("committer",{}).get("date"),
              "message":(c.get("message") or "").splitlines()[0][:180],
              "html_url":commit.get("html_url")}
        record["commit"]=snap
        if previous.get("commit",{}).get("sha") and previous["commit"]["sha"]!=snap["sha"]:
            changes.append({"type":"upstream commit","name":cfg["name"],
                "old":previous["commit"].get("short_sha"),"new":snap["short_sha"],
                "date":snap["date"],"message":snap["message"],"url":snap["html_url"]})
    except Exception as e:
        errors.append({"repo":repo,"endpoint":"commit","error":str(e)})
        record["commit"]=previous.get("commit")
    new["repos"][repo]=record

try:
    textures,_=get_json("https://api.polyhaven.com/assets?type=textures")
    if not isinstance(textures,dict):raise RuntimeError("Unexpected Poly Haven texture catalogue.")
    ids=sorted(textures.keys())
    prev=set(old.get("polyhaven",{}).get("texture_ids",[])); curr=set(ids)
    added=sorted(curr-prev);removed=sorted(prev-curr)
    for aid in added:
        changes.append({"type":"new Poly Haven texture","name":textures[aid].get("name",aid),"id":aid,"url":f"https://polyhaven.com/a/{aid}"})
    for aid in removed:
        changes.append({"type":"removed Poly Haven texture","id":aid,"url":f"https://polyhaven.com/a/{aid}"})
    new["polyhaven"]={"texture_count":len(ids),"texture_ids":ids}
except Exception as e:
    errors.append({"source":"Poly Haven API","error":str(e)})
    new["polyhaven"]=old.get("polyhaven",{})

now=datetime.now(timezone.utc)
weekday=now.weekday()
lines=["# Visual source watch — cloud run","",f"Checked: {now.isoformat()}","",
 "Source access: public GitHub REST API + Poly Haven public API only.",
 "No scraping of marketplaces, no account login, no automated freebie claiming and no downloads in this watcher.",
 "",f"## Changes detected ({len(changes)})",""]
if changes:
    for x in changes:
        if x["type"]=="release":lines.append(f"- **{x['name']} release:** {x.get('old') or 'baseline'} → {x.get('new')} · {x.get('url')}")
        elif x["type"]=="upstream commit":lines.append(f"- **{x['name']} commit:** {x.get('old')} → {x.get('new')} ({x.get('date')}) · {x.get('message')} · {x.get('url')}")
        else:lines.append(f"- **{x['type']}:** {x.get('name',x.get('id'))} · {x.get('url')}")
else:lines.append("- No release/commit or texture catalogue additions/removals detected.")
lines += ["","## Current source versions",""]
for repo,r in new["repos"].items():
    lines.append(f"- **{r['name']}** — release: {(r.get('release') or {}).get('tag','n/a')}; commit: {(r.get('commit') or {}).get('short_sha','n/a')}")
lines += ["",f"- **Poly Haven textures:** {new['polyhaven'].get('texture_count','n/a')} IDs.",
          "","## Manual-only promotional sources","",
          "- Creative Market Weekly Free Goods: inspect the official page manually; most goods have Personal License, so verify product-specific rights.",
          "- Creative Fabrica Daily Gifts: inspect and claim manually; preserve the designer's licence and order record.",
          "- unDraw, ManyPixels, Storyset, DrawKit, Figma Community and SVG Repo: open individual item pages and confirm exact licence before use."]
# Tuesday in São Paulo is Tuesday UTC as well; scheduled run at 12:00 UTC maps to 09:00 local.
if weekday==1:
    lines += ["","## Tuesday manual reminder","","Review the four Creative Market Weekly Free Goods manually. This automation does not access or download marketplace content."]
if errors:
    lines += ["","## API errors",""]+[f"- {e}" for e in errors]
REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")

changed = new!=old
if changed:
    STATE.parent.mkdir(parents=True,exist_ok=True)
    STATE.write_text(json.dumps(new,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if os.environ.get("GITHUB_OUTPUT"):
    with open(os.environ["GITHUB_OUTPUT"],"a",encoding="utf-8") as f:f.write(f"state_changed={'true' if changed else 'false'}\n")
if os.environ.get("GITHUB_STEP_SUMMARY"):
    with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as f:f.write(REPORT.read_text(encoding="utf-8"))
print(json.dumps({"changed":changed,"repos_checked":len(new["repos"]),
 "polyhaven_textures":new["polyhaven"].get("texture_count"),
 "changes":changes,"errors":errors,"report":str(REPORT)},ensure_ascii=False))
if errors:
    raise SystemExit("At least one source check failed; report saved for review.")
