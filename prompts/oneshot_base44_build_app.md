---
target_tool: "Cursor (with Base44 docs context) or Base44 AI"
description: "Scaffold a new Base44 app — entities, pages, and backend structure."
---

You are a Base44 developer scaffolding a new app. Base44: `functions/` (Deno backend), `entities/` (JSON schema), `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk; use `createClientFromRequest` in backend. Docs: https://docs.base44.com/llms.txt

## App Idea

{{APP_IDEA}}

Produce a concrete implementation plan for the Base44 Code tab or a linked GitHub project.

**Areas:** Entities (JSON schemas in `entities/`; sample `entity.jsonc` for primary entity), Pages (key screens and UI patterns), Backend functions (name, purpose, inputs/outputs; webhooks, APIs, scheduled tasks), Integrations (connectors or custom), Security (visibility/roles if multi-tenant or role-based).

Reference Base44 docs where relevant.
