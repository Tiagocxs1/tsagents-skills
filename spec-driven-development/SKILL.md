---
name: spec-driven-development
description: Turn multi-step feature requests and bug reports into specifications, plans, tasks and verified outcomes. Inspired by GitHub Spec Kit.
---

# Spec-Driven Development

Reference implementation: https://github.com/github/spec-kit

## Feature workflow
1. Specify: user problem, actors, expected outcome, non-goals, acceptance criteria and edge cases.
2. Plan: inspect existing stack/architecture; define minimal compatible implementation and API/data contracts.
3. Tasks: split into small ordered changes, each with a test or observable verification.
4. Implement: change one coherent slice at a time; preserve existing behavior unless requirements explicitly change it.
5. Converge: typecheck, lint/build, focused tests, rendered UI inspection and acceptance-criteria review.
6. Record: changed files, test evidence, deployment state and unresolved gaps.

## Bug workflow
1. Reproduce the original symptom with exact steps and device/context.
2. Trace the visible control through handler, state, API and persisted data.
3. Identify root cause before changing code.
4. Apply the narrowest safe fix.
5. Repeat the original steps and run regression checks.
6. Do not call it fixed until the original symptom is no longer reproducible.

## Non-negotiable quality gates
- A commit is not proof of correctness.
- A successful build is not proof of correct UI behavior.
- A deployment is not complete until the live URL is checked.
- Responsive work requires phone, tablet and desktop inspection.
- If a check cannot be run, state that limitation; never invent evidence.
- Record decisions that affect navigation, shared components or data contracts.

## Spec Kit adoption
Use the official Specify -> Plan -> Tasks -> Implement -> Converge process when the Specify CLI/agent integration is available. For existing repositories, adopt incrementally; never regenerate existing architecture blindly. CLI installation and docs: https://github.com/github/spec-kit
