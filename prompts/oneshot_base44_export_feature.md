---
target_tool: "Cursor or Base44 AI"
description: "Extract a complete feature from a Base44 app — all code, entities, and context needed to recreate it elsewhere."
---

You are extracting a feature from a Base44 app for transfer to another app. Base44: `functions/`, `entities/`, `pages/`, `components/`, `api/`, `hooks/`, `lib/`, `utils/`. React + Vite, @base44/sdk. Docs: https://docs.base44.com/llms.txt

## Feature to Extract

{{FEATURE_DESC}}

## Feature Scope

{{FEATURE_TYPE}}

Use scope to focus: backend-only → skip UI sections; UI-only → skip backend; full-stack or unclear → cover everything.

Produce a **complete, self-contained export** so someone can recreate this feature in another Base44 app from your output alone. Only include sections relevant to this feature — no empty or padded sections.

**Sections (include only what applies):** Overview (what it does, layers, how it fits, permissions), Entities (full JSON schema per entity; flag feature-specific vs shared), Backend functions (full path + complete file contents; purpose, trigger, auth, external calls), Pages & routes (path + complete contents; route registration, components used), Components (path + complete contents; props; feature-specific vs shared), Hooks/utils/lib (path + complete contents; feature-specific vs shared), Dependencies (npm, integrations, env/config), Internal wiring (navigation, API calls, shared state, cross-feature refs).

**Constraints:** For every file, provide **complete contents** — no truncation or summaries. End with a short **Transfer Checklist** (entities, functions, pages, components, hooks, npm, env, routing, shared deps) omitting items that don’t apply.
