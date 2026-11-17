---
name: web-interface-guidelines
description: Audit web interfaces for accessible, predictable interactions, navigation, forms, keyboard behavior, responsive layout and polish.
---

# Web Interface Guidelines

Source: https://github.com/vercel-labs/web-interface-guidelines (MIT). Review upstream before major audits because the source evolves.

## Interaction and navigation
- Every flow works by keyboard; focus is visible and never hidden behind sticky UI.
- Dialogs move focus inside, contain it while modal, and return focus to the trigger on close.
- Mobile hit areas are at least 44px. Inputs use at least 16px text to avoid iOS Safari zoom.
- Use anchors/Next Link for navigation and buttons for actions; never use clickable divs as navigation.
- Preserve URL state for shareable tabs, filters, pagination and deep-linkable views. Back/Forward restores context.
- Essential actions never depend on hover. Show pressed, loading, disabled and error states.
- Confirm destructive actions or offer undo. If it looks clickable, it must work.

## Forms and feedback
- Persistent accessible labels; correct autocomplete, input type and inputmode.
- Never block paste or password managers.
- Put validation next to the field; focus the first error after failed submit.
- Async actions show progress and prevent duplicate submission once the request starts.
- Errors explain cause and recovery action. Warn before leaving unsaved changes.

## Layout, content and motion
- Verify phone, laptop and wide desktop. Fix overflow; don't hide core functionality to mask it.
- Respect safe areas; fixed UI must not cover content or keyboard focus.
- Prefer Grid/Flexbox over JavaScript measurements.
- Respect prefers-reduced-motion; animate transform/opacity rather than layout dimensions.
- Avoid transition: all; keep motion interruptible and never block input.
- Long user content must wrap safely; flex text children need min-width: 0.
- Include empty, loading, error and dense states.
- Prefer semantic HTML before ARIA; icon-only controls need accessible names.
- Use locale-aware dates, numbers and currency.

## Review output
For every finding report severity, component/file, observed defect, user impact, proposed correction and verification step. Automated scores alone do not prove WCAG conformance.
