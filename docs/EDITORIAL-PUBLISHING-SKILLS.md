# Editorial publishing skills — provenance and licensing

Curadoria: 18/11/2026.

## Editorial Design
- Source: https://github.com/sickn33/agentic-awesome-skills/tree/main/plugins/agentic-awesome-skills-claude/skills/design-it/editorial-design
- Upstream file inspected: `SKILL.md`, blob `513129cbe11caff71318b252866422db5dab4ec4`.
- License: MIT, from the upstream repository root. A copy is preserved at `editorial-design/LICENSE`.
- Local file is an adaptation and includes accessibility, responsive behavior and Portuguese-language production rules.

## Digital E-Guide Generator
- Marketplace reference supplied: https://mcpmarket.com/tools/skills/digital-e-guide-generator-1
- Publisher label supplied: bykaranmrn.
- As of this curation, no canonical public GitHub repository, complete source file or verifiable redistribution license could be confirmed.
- No upstream code or full skill text was copied. `digital-eguide-editorial/SKILL.md` is an independent TS Digitais implementation of the high-level requirements: cover, visual contents, editorial spreads, asymmetric columns, exercises, PDF output and QA.
- If the canonical upstream repository/license is later confirmed, review whether to add it as a source reference or replace/adapt the local implementation.

## Frontend Design
- Official reference: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Upstream file and `LICENSE.txt` were inspected. Upstream license: Apache-2.0.
- The local skill is independently written and links to the official source; it does not reproduce the upstream skill text.
- Prefer the official upstream for its full original wording and updates.

## WeasyPrint PDF Skill
- Source: https://github.com/slapash/weasyprint-pdf-skill
- Upstream `SKILL.md` and root `LICENSE` inspected. License: MIT; copyright notice for Omar Benaidy is preserved in `weasyprint-pdf-creation/LICENSE`.
- Local file is an adaptation focused on TS Digitais e-books, HTML/CSS print rules, and repeatable QA. The upstream repository contains additional scripts, templates, sample data, fonts and example PDFs; these are not mirrored here.
- Technical reference for supported CSS and platform dependencies: https://doc.courtbouillon.org/weasyprint/stable/

## Usage notes
These files are instruction modules, not installed runtime services. They do not install WeasyPrint, fonts or native libraries. Each agent/editor must be configured to load the relevant skill directory. Verify current upstream licenses and compatibility before copying any additional assets.
