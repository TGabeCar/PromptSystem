---
target_tool: "Cursor"
description: "Analyze a Base44 app codebase — structure, dependencies, and recommendations."
---

You are analyzing a Base44 app codebase. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

## Scope

{{SCOPE}}

Produce a structured report for onboarding or refactor planning. Ground it in the code you read.

**Sections:** Overview (structure, entry points, how pieces connect), Entities (data models, relationships, visibility), Functions (purpose, triggers, auth), Frontend (page flow, components, SDK usage), Dependencies (npm, SDK, integrations), Findings (red flags: auth, error handling, duplication, performance), Recommendations (refactors, tests, docs, Base44 best practices).

**Constraints:** Be concrete; call out file/function names where it helps.
