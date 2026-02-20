---
target_tool: "Cursor or Poppy"
description: "Generate overall technical documentation for a Base44 app — by reading the codebase and including code, database, and function details."
---

You are documenting a Base44 app as a whole. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

**Scope:** Entire app.

Read the codebase first, then produce a technical doc grounded in the code. Include code snippets, entity definitions, and function logic — no assumptions.

**Sections:** Purpose, Overview (what the app does, entry points, tech stack), Project structure, Architecture (diagram + data flow; reference files), Data model (entities, schemas, visibility), Backend functions (path, trigger, auth, snippet per function), API surface, Integrations (outbound calls), Security notes (validation, permissions, secrets), Setup & run, Common tasks. Then add the doc to the app’s admin panel in a copy-able block (create a "Technical Documentation" section if missing).

**Constraints:** Ground in actual code; prefer code and file references over prose; keep it scannable; state security/compliance purpose when relevant.
