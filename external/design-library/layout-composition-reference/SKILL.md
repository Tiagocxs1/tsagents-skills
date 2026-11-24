---
name: layout-composition-reference
description: Find and adapt a visual layout pattern from the locally mirrored 350 Layout Compositions index. Use when a task needs a composition system, not an existing image.
---

# 350 Layout Compositions — searchable reference index

The local catalog is `external/design-library/data/350-layout-catalog.csv`. It contains the names, categories, subcategories and original repository-relative image paths for 350 composition references. It does **not** include the reference image binaries.

## Use in the TS Brain runtime

The LangGraph registry exposes `search_layout_compositions(query, limit=8)`. Use the returned IDs and category/subcategory metadata to choose a layout logic. Do not claim to have viewed the example image unless its original binary has been fetched and inspected.

## How to adapt

1. Choose the underlying composition principle (e.g. golden ratio, diagonal, hierarchy/contrast, columns, modular grid, frame-within-frame, visual balance, repetition/rhythm), not the screenshot's exact design.
2. Adapt geometry and spacing to the requested ratio and real content. Preserve the brand's own colour palette, type system, logo and voice.
3. Produce an original layout. Do not trace, recreate or redistribute the source reference image.
4. Keep the result legible at the actual delivery size; do not shrink text to force content into the frame.
5. When the catalogue materially informs a public deliverable, attribute **350 Layout Compositions** with a link to https://github.com/nevertoday/350-layout-compositions and https://creativecommons.org/licenses/by/4.0/ and indicate that the selected composition was adapted.

## Data and license boundary

The catalog metadata is made available under the repository's CC BY 4.0 notice. Attribution is required. The 350 source images are not downloaded here; their authors, depicted works or embedded third-party rights may require separate permission. This is a layout research index, not a royalty-free image bank. Paid offerings mentioned by the upstream project are outside this integration and are not required.
