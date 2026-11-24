---
name: ogimagecn-code
description: Use ogimagecn as a React/Satori code reference to implement original Open Graph and social preview image components in a compatible web project.
---

# ogimagecn — React/Satori implementation guide

Repository: https://github.com/shadcn-labs/ogimagecn
Pinned local source: `upstream/ogimagecn`
License: MIT. Preserve the upstream copyright/license notice for copied code.

## What it is

A library of reusable Open Graph image components and blocks for React, rendered through Satori and the Next.js `next/og` runtime. It is a component/code library, not a running MCP or a standalone LangGraph image-generation tool.

The upstream README documents blog, changelog, event, product, quote, photo and shadcn registry card patterns. The app uses Next.js 16, React 19 and Satori.

## Integration procedure

1. Confirm the target application uses a compatible React/Next.js runtime and has the required Satori/Next OG dependencies.
2. Inspect the actual exported blocks and their Satori-safe primitives in the pinned submodule before importing or copying code. Do not invent package export names.
3. Copy only the required component(s) into the target project's own source tree, adapting tokens, typography, image dimensions and brand constraints.
4. Use Satori-supported CSS and fonts. Validate the generated OG response as an actual PNG at the intended dimensions; do not assume browser-only CSS works in Satori.
5. Retain the MIT license notice when copying source. Do not add a proprietary font or image without checking its own license.

## Runtime boundary

LangGraph/LangChain can use this Skill as coding guidance. They cannot call ogimagecn directly until a local rendering adapter/tool is built in the target application. Do not install the entire documentation app or its analytics stack just to use the components.
