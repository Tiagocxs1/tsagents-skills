---
name: responsive-web-adaptation
description: Adapt existing web applications across desktop, tablet and mobile. Use for responsive layouts, app shells, navigation, touch interactions, viewport defects and mobile UI audits.
---

# Responsive Web Adaptation

Adaptation means rethinking the experience for each context, not shrinking desktop pixels.

## Assess before coding
- Inspect the rendered UI and current assumptions: viewport, pointer, hover, keyboard, scroll model, density and navigation.
- Identify core user tasks and contexts: phone portrait/landscape, tablet, laptop and wide desktop.
- Preserve the same information architecture across devices; simplify presentation, never remove core capability.
- Reproduce each reported defect and locate its component/state before editing.

## App-shell patterns
- Desktop: keep primary navigation/sidebar persistent. Open contextual work in the main workspace, side panel, drawer or dialog without losing the current context.
- Tablet: use master-detail where space allows; collapse secondary navigation when it does not.
- Mobile: show one primary surface at a time with clear back/close behavior. Use a compact top bar or bottom navigation for a small number of top-level destinations.
- Deep-link shareable destinations, but don't force every action into a full-page navigation.
- Preserve filters, draft input, scroll position and parent context when opening and closing detail views.
- Choose the correct primitive: links navigate; buttons perform actions; dialogs/sheets support focused tasks; detail panels keep the user in their current workflow.

## Responsive implementation
- Start mobile-first; introduce breakpoints where content breaks, not solely for device labels.
- Prefer Grid, Flexbox, container queries and fluid sizing (clamp) over JavaScript measurements.
- Avoid fixed widths beyond viewport. Text-bearing flex/grid children need min-width: 0 and resilient wrapping.
- Use min-height: 100dvh where mobile browser chrome makes 100vh unreliable.
- Respect env(safe-area-inset-*) for fixed headers, bottom bars and sheets.
- Never rely on hover for essential actions. Use hover/pointer queries only as enhancements.
- Mobile targets >=44x44 CSS px; mobile text inputs >=16px to avoid iOS focus zoom.
- Avoid accidental nested scroll traps and horizontal page overflow.
- Design empty, loading, error, long-content and dense states in addition to the happy path.

## Verification
Inspect at 320, 375, 390, 768, 1024 and 1440 CSS px; include portrait and landscape. Verify touch and keyboard, back/close, focus, long labels, long URLs, keyboard appearance, safe areas and reduced motion. Test a real phone when available; label emulation-only evidence honestly.

## Sources
Adapted for TS projects from https://github.com/pbakaus/impeccable (Apache-2.0), https://www.ui-skills.com/skills/frontend and https://github.com/vercel-labs/web-interface-guidelines.
