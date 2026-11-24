---
name: external-design-library-router
description: Select up to two relevant, locally checked-out design/content Skills from the TS Digitais external catalog. Use before design, social, slides, diagrams, motion, Open Graph or layout-reference tasks.
---

# External design-library router

Use this Skill as a selector and policy layer. It does not replace the first-party TS Digitais Skills, brand profiles, visual QA or the AGENTS.md rules.

## Source of truth

Read the registry:
`external/design-library/registry.json`

A Skill is loadable only when its entrypoint is present, the resolved local file exists under the checked-out repository root, and the source status is allowlisted by `ts_brain.agent_registry`. The runtime must never fetch, clone, install, login, or enable MCPs automatically.

## Route by task

- Social carousel, cover, story/post: `ext-guizang-social-card`
- PPT/deck/slides: `ext-guizang-ppt` or `ext-design-agent-slideshow`
- Branding and art direction: `ext-huashu-design` or `ext-design-agent-brand-design`
- General visual craft / layout: `ext-design-agent-design-wiki`
- Monochrome / one-ink / two-ink print: `ext-mono-color`
- Diagram / flowchart / architecture map: `ext-diagram-design`
- Charts and data-heavy graphics: `ext-design-agent-data-viz`
- Storyboard / motion / animated scene: `ext-design-agent-storyboard` and/or `ext-design-agent-motion-direction`
- Image editing/operations: `ext-design-agent-image-ops`
- Image synthesis: `ext-design-agent-image-generation`
- Visual verification: `ext-design-agent-visual-verify`
- OG/Open Graph / social preview image: `ext-ogimagecn-code` (code guidance; not a renderer or MCP)
- Search an original layout/composition pattern: `ext-350-layout-reference` (metadata-only search; image binaries are not local)
- Public read-only social/web research: `ext-agent-reach` (Skill instructions are available; CLI and site channels are not installed or authenticated)
- Chinese copy editing only: `ext-humanizer-zh`

The TS Brain currently chooses at most two external Skills from trigger matches. Prefer those two most closely matched to the concrete deliverable. Do not load the entire LangChain Design Agent bundle.

## Upstream projects that are not directly callable Skills

- OpenDesign: full workspace application. A submodule pointer is present; contents are not cloned.
- Open Carrusel: separate Next.js carousel application. It is not started, configured or authenticated.
- DSh Guizang Design: plugin/harness for another environment; do not pretend it is a LangGraph tool.
- AiToEarn: publishing/monetization application and remote MCP with write permissions. MCP is disabled, no credentials exist, and publication is not authorized.
- ogimagecn: reusable React/Satori code. Wrapper Skill gives guidance, but no LangGraph rendering tool has been built yet.
- 350 Layout Compositions: CSV metadata is locally indexed; reference images were intentionally not downloaded.
- Yingzao: no root license was found. Link-only; do not copy or load until usage rights are clarified.

## Licenses, assets and security

- Preserve original license and NOTICE files; AGPL, Apache, MIT and CC BY have different obligations.
- Guizang Social Card and Guizang PPT are AGPL-3.0.
- LangChain Design Agent is Apache-2.0 at the root, with NOTICE/third-party content to preserve.
- Huashu, Agent Reach, Humanizer-zh, Mono Color code/Skill, Diagram Design, ogimagecn and Open Carrusel are MIT; the Mono Color reference images are separately restricted.
- 350 Layout metadata is CC BY 4.0: attribute the source and indicate modifications when it informs a published design. Do not treat the index as an image library.
- Yingzao is link-only while the license is unverified.

The NVIDIA Nemotron runtime must never receive external Skill text, private agent profiles, private references or Obsidian memory. It receives generic role descriptions and public/synthetic briefings only. Do not disable or route around this restriction.

Do not enable Agent Reach login/channel setup, social scraping sessions, AiToEarn MCP, publishing tools, paid model APIs, or app telemetry without an independent privacy/security/cost review and the user's explicit approval.

## Required TS Brain commands

```bash
ts-brain skills --sources
ts-brain skills --all
ts-brain skills --name ext-huashu-design
```

Use the CLI output to check whether a Skill is genuinely loadable. A submodule pointer or a registry record alone does not prove the corresponding checkout, dependencies, MCP or service is operational.
