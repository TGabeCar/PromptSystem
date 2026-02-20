---
target_tool: "Cursor"
description: "Debug and fix bugs in a Base44 app with framework-aware guidance."
---

You are working in a Base44 app. Base44: React + Vite, `functions/` (Deno), `entities/` (JSON schema), `api/` (SDK), `base44.functions.invoke()`, `createClientFromRequest`. Docs: https://docs.base44.com/llms.txt

## Bug

{{BUG_DESC}}

Investigate end-to-end: either confirm the feature works and show evidence, or find the root cause and implement the fix. Base44 patterns: SDK uses logged-in user permissions; HTTP/webhook functions need `asServiceRole`; trace full chain (frontend → invoke → entity); check Activity Monitor for failed calls; use `createClientFromRequest(req)` and explicit error handling — silent failures often come from swallowed errors.

Reference Base44 docs when relevant. Explain what you found and why the fix works.
