---
target_tool: "Cursor"
description: "Refactor and clean up Base44 app code — dead code, consistency, patterns."
---

You are refactoring a Base44 app. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

## What to Clean Up

{{SCOPE}}

Produce a cleanup plan and concrete edits. Preserve behavior; do not remove functionality unless explicitly requested.

**Flow:** Audit (dead code, inconsistent patterns, unused exports, duplication) → ordered plan (breaking vs safe; note dependencies) → edits by file. Apply Base44 patterns: error boundaries, SDK usage, function structure (`createClientFromRequest`, `asServiceRole` for HTTP). Verify: run locally, test key flows, check Activity Monitor.

**Constraints:** Stay within Base44 conventions; small, incremental changes; no over-engineering.
