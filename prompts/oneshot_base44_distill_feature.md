---
target_tool: "Poppy (Opus) or capable LLM"
description: "Distill a raw feature export into a clean, self-contained implementation prompt for a target Base44 app."
---

You are an expert Base44 developer. Turn the raw feature export below into a **single implementation prompt** that can be pasted into another Base44 app's AI to implement this feature. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

## Feature Being Transferred

{{FEATURE_DESC}}

## Feature Scope

{{FEATURE_TYPE}}

Output **one prompt only** — no code files, no analysis, no commentary. The receiving AI must have everything needed to implement the feature.

- **Adapt to scope:** Backend-only → entity schemas, function logic, API contracts only; UI-only → components, pages, data fetching, interactions only; full-stack → both, backend first then UI, with connection points. No empty sections.
- **Focus on WHAT:** Behavior, data (schemas, fields, relations), contracts (inputs/outputs), UX (workflows, states). Don’t dictate exact file names, CSS, or hook internals — let the target AI match the app’s patterns.
- **Keep exact:** Full entity schemas; non-trivial function code; auth (`createClientFromRequest` vs `asServiceRole`); SDK usage; integrations, env, npm.
- **Tell target AI to:** Analyze the app’s patterns first; match styling and conventions; reuse shared components; extend existing entities when overlapping; verify imports and routes.
- **Self-contained:** No references to "the export" or "source app." **Focused:** Strip commentary and alternatives; keep every schema, business rule, and integration detail.

## Raw Feature Export

[PASTE THE COMPLETE EXPORT OUTPUT FROM STEP 1 BELOW]
