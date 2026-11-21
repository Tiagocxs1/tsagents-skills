---
name: article-writing
description: Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance. Use when the user wants polished written content longer than a paragraph, especially when voice consistency, structure, and credibility matter.
origin: claude-fulcrum
---

# Article Writing

Write long-form content that sounds like a real person or brand, not generic AI output.

## When to Activate

- drafting blog posts, essays, launch posts, guides, tutorials, or newsletter issues
- turning notes, transcripts, or research into polished articles
- matching an existing founder, operator, or brand voice from examples
- tightening structure, pacing, and evidence in already-written long-form copy

## Core Rules

1. Lead with the concrete thing: example, output, anecdote, number, screenshot description, or code block.
2. Explain after the example, not before.
3. Prefer short, direct sentences over padded ones.
4. Use specific numbers when available and sourced.
5. Never invent biographical facts, company metrics, or customer evidence.

## Voice Capture Workflow

If the user wants a specific voice, collect one or more of:
- published articles
- newsletters
- X / LinkedIn posts
- docs or memos
- a short style guide

Then extract:
- sentence length and rhythm
- whether the voice is formal, conversational, or sharp
- favored rhetorical devices such as parentheses, lists, fragments, or questions
- tolerance for humor, opinion, and contrarian framing
- formatting habits such as headers, bullets, code blocks, and pull quotes

If no voice references are given, default to a direct, operator-style voice: concrete, practical, and low on hype.

## Banned Patterns

Delete and rewrite any of these:
- generic openings like "In today's rapidly evolving landscape"
- filler transitions such as "Moreover" and "Furthermore"
- hype phrases like "game-changer", "cutting-edge", or "revolutionary"
- vague claims without evidence
- biography or credibility claims not backed by provided context

## Writing Process

1. Clarify the audience and purpose.
2. Build a skeletal outline with one purpose per section.
3. Start each section with evidence, example, or scene.
4. Expand only where the next sentence earns its place.
5. Remove anything that sounds templated or self-congratulatory.

## Structure Guidance

### Technical Guides
- open with what the reader gets
- use code or terminal examples in every major section
- end with concrete takeaways, not a soft summary

### Essays / Opinion Pieces
- start with tension, contradiction, or a sharp observation
- keep one argument thread per section
- use examples that earn the opinion

### Newsletters
- keep the first screen strong
- mix insight with updates, not diary filler
- use clear section labels and easy skim structure

## Quality Gate

Before delivering:
- verify factual claims against provided sources
- remove filler and corporate language
- confirm the voice matches the supplied examples
- ensure every section adds new information
- check formatting for the intended platform

## Universal Article Structure Standard

Before drafting, revising, auditing, or implementing an article or a reusable article-page template, read `references/estrutura-de-artigo.md` in full. This is the shared editorial and page-structure standard for all TS Digitais projects, websites, and clients.

### Apply the priority levels correctly

- **Essential:** baseline for every article. If an item cannot be met, record the limitation instead of silently ignoring it.
- **Recommended:** apply when the article is strategic, competitive, a pillar, or tied to revenue, provided the feature fits the project.
- **Optional / experimental:** use only when the niche, audience, maintenance capacity, and budget justify testing it. Do not turn optional items into default requirements.

### Workflow

1. Identify search intent, reader, purpose, format, and the article's role in its content cluster.
2. Adapt the checklist to the client and niche. Record items as applicable / not applicable; respect specialist-review needs for YMYL and content-type-specific requirements such as product schema for e-commerce.
3. Plan the complete article hierarchy and page components before writing or implementing the template.
4. Keep content requirements distinct from optional interface features. An index, audio player, reading-progress bar, comments, share bar, or downloadable PDF must not be forced into every page simply because it appears in the checklist.
5. Use only verified sources, real author credentials, actual first-hand experience, and authorized proof. Never invent an author, reviewer, test, metric, testimonial, certification, result, or citation.
6. Validate copy, links, semantic HTML, metadata, structured data, mobile readability, accessibility, SSR/initial HTML, and technical performance against the reference before delivery. Do not promise rankings, rich results, or AI citations.

Keep the supplied checklist intact as the canonical reference. Improve or extend it only through an explicit, versioned update; do not silently rewrite its priorities or notes.

