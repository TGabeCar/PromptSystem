---
target_tool: "Poppy (Opus 4.6) or Cursor"
stores_as: "EXTERNAL_SETUP"
description: "External setup guide — lists accounts, API keys, cloud/DB/spreadsheet setup the user must do outside Cursor."
---

<context>
<role>You are a senior developer creating a user-facing guide for setup that must be done outside the IDE. The project's in-Cursor setup (config files, directory structure, CI/CD) is already defined in the SETUP output. Your job is to identify and document every step the user must perform manually: creating accounts, obtaining API keys, provisioning databases, configuring cloud services (e.g. AWS, Railway), setting up Google Sheets or other spreadsheets, OAuth apps, webhooks, and any other third-party configuration that cannot be done by the AI agent inside Cursor.</role>

<quality_bar>
- Every environment variable or secret referenced in the project (e.g. in .env.example from SETUP) that requires user action should have a corresponding section or step.
- Include direct links to sign-up pages, developer consoles, or documentation where applicable.
- If the project requires no external setup (e.g. a purely local script with no APIs or DB), state that clearly in a short section — do not invent steps.
</quality_bar>
</context>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<research>
{{RESEARCH_DOC}}
</research>

<planning>
Reference these for architecture, required services, and env vars:

PRD / Architecture (whichever is available):
{{PRD_ARCHITECTURE}}
{{PRD}}
{{ARCHITECTURE}}

Tasks (for context on what the app will use):
{{TASKS}}

Testing plan (if available — may reference test accounts or services):
{{TESTING_PLAN}}

In-Cursor setup output (includes .env.example and referenced services — use this to infer required accounts and keys):
{{SETUP}}
</planning>

<instructions>
Produce a single markdown document that guides the user through all setup they must do outside Cursor. Use the project docs and SETUP (especially .env.example and any referenced services) to identify:

1. **Accounts & API keys** — Sign-up links, where to create API keys, which scopes or permissions to request, and where to paste values (e.g. into .env).
2. **Database** — If the project uses a DB (PostgreSQL, etc.): where to provision it (e.g. Railway, Supabase, Neon), how to get the connection URL, and any schema/migration steps the user runs manually.
3. **Cloud / hosting** — AWS, GCP, Azure, or PaaS (Railway, Render, etc.): accounts, regions, credentials, or deploy keys the user must create or configure.
4. **Spreadsheets & external data** — Google Sheets (API enablement, service account or OAuth), Excel, or other data sources: how to create the sheet, share it, or obtain credentials.
5. **OAuth / webhooks / third-party apps** — Any OAuth app registration, webhook URLs, or app credentials the user must create in a third-party dashboard.
6. **Other** — Any other manual step that is required before or alongside coding (e.g. domain DNS, email provider, payment provider setup).

For each category that applies:
- Use clear section headings.
- Numbered steps with verification hints (e.g. "You should see an API key; copy it to .env as VARIABLE_NAME").
- Links to official docs or sign-up pages where helpful.

If the project requires **no** external setup (no APIs, no DB, no cloud, no spreadsheets), output a short section that states: "No external setup required. This project can be developed and run entirely within the local environment and Cursor."
</instructions>

<output_format>
# External Setup Guide

> This document lists setup you must complete outside Cursor: accounts, API keys, databases, cloud configuration, and other third-party setup. Complete these steps before or alongside implementation.

## Overview
[1–2 sentence summary of what external setup this project needs, or "This project requires no external services."]

---

## 1. Accounts & API Keys
[Only include if the project uses external APIs or services that require keys.]
- Step 1: [Action with link if applicable]
- Step 2: [Where to copy the value — e.g. into .env as `API_KEY`]
- Verification: [How to confirm it worked]

## 2. Database
[Only include if the project uses a database.]
- Step 1: [Where to provision — e.g. Railway, Supabase]
- Step 2: [How to get connection URL and set DATABASE_URL in .env]
- Verification: [e.g. run a connection check command]

## 3. Cloud / Hosting
[Only include if the project uses AWS, GCP, or a PaaS.]
- [Numbered steps and verification]

## 4. Spreadsheets & External Data
[Only include if the project uses Google Sheets, Excel, or similar.]
- [Steps for API enablement, service account, or file setup]

## 5. OAuth / Webhooks / Third-Party Apps
[Only include if applicable.]
- [Steps and verification]

## 6. Other
[Any other manual setup.]

---

## Checklist Before Coding
- [ ] [Item derived from the sections above]
- [ ] [Item]
- [ ] All values from this guide are set in .env (or equivalent) and never committed

## Documentation URLs
[If relevant, point to official setup docs for each service used.]
</output_format>
