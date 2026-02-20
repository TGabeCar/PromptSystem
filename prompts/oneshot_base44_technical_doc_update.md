---
target_tool: "Cursor"
description: "Update existing technical documentation to match the current codebase — by re-reading the code and including code, database, and function details."
---

You are updating technical documentation for a Base44 app. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

## Existing documentation (to update)

(Paste the existing technical documentation here when you use this prompt.)

Re-read the codebase and compare to the doc above. Produce an updated doc grounded in the current code. Start with a short **"Changes from previous"** summary (new/removed entities, functions, routes; breaking or notable changes). Then update the body from code, not from the old doc.

**Sections:** Purpose, Architecture (diagram + data flow; reference files), Data model (entities, schemas, visibility), Backend functions (path, trigger, auth, snippet per function), API surface, Integrations (outbound calls), Security notes (validation, permissions, secrets), Setup & run, Common tasks. Then add the updated doc to the app’s admin panel in a copy-able block (replace or append in "Technical Documentation" section).

**Constraints:** Verify everything against current files; prefer code and file references over prose; keep it scannable.
