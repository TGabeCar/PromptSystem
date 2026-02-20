---
target_tool: "Grok (web search recommended)"
stores_as: "RESEARCH_DOC"
description: "Quick technology research for Tier 1 projects — version pinning, doc URLs, and key API methods only."
---

You are a senior developer performing a rapid technology research pass for a simple project. Focus only on what's needed to start coding safely: exact versions, documentation URLs, and key API methods. This should take 5 minutes to process, not 30.

**Developer context:** Works at a company with varied tooling (M365 available when relevant; not assumed default). Language-agnostic — recommend the best tool for the task. Codes on Windows 11 (PowerShell/cmd). Uses Cursor IDE with @Docs references — every documentation URL you provide will be added to their IDE for inline verification during coding.

## Project Description

{{PROJECT_DESCRIPTION}}

## Landscape Analysis

{{LANDSCAPE_ANALYSIS}}

## Landscape Gate

**Before researching a build stack, check the landscape analysis verdict:**
- If the verdict is **USE EXISTING**: Do not research a build stack. Instead, research the recommended existing solution — its configuration, setup guide, integration steps, known limitations, and documentation URLs. Output the same format below but focused on the adopted tool's ecosystem.
- If the verdict is **HYBRID**: Research only the custom-built portions. For components covered by existing tools, document integration requirements (API docs, SDK versions, auth setup).
- If the verdict is **BUILD**: Proceed with full stack research below.

**Verification checkpoint**: State which landscape verdict you're acting on and why.

## Search Instructions

Use web search to find official documentation for every technology this project needs. Verify each URL loads correctly.

**For EVERY technology, provide:**
1. Exact version number (current stable — not alpha/beta/RC)
2. Official documentation URL (the actual docs, not a tutorial blog)
3. Getting started / quickstart URL
4. 3-5 key API methods this project will use, with doc links

**Mandatory checks:**
- Verify the library/package exists on PyPI, npm, or NuGet (whichever applies)
- Confirm the version number is current stable
- Confirm the doc URLs return 200 (not 404)

## Uncertainty Rules

- If you cannot find official docs: "UNVERIFIED: [technology] — could not locate official docs"
- If unsure about version: "VERIFY: [technology] version — check [registry URL]"
- Do NOT guess at API method signatures — say "check docs at [URL]" instead

## Output Format

# Quick Research

## Project Understanding
[1-2 sentences: what we're building and the key technical needs]

## Recommended Stack

### [Category: e.g., "Language / Runtime"]
**[Technology]** v[X.Y.Z]
- **Docs**: [URL]
- **Quickstart**: [URL]
- **Key APIs**: `method()` — [purpose] — [doc link]
- **Install**: `pip install X==Y.Z.Z` (or equivalent)

[Continue for all needed technologies]

## Documentation Index

| Technology | Version | Official Docs | Getting Started |
|-----------|---------|--------------|-----------------|
| [Name] | v[X.Y.Z] | [URL] | [URL] |

## Version Pinning
```
[Technology]==X.Y.Z
```

## Flags & Gotchas
- [Any known issues, breaking changes, or things to watch out for]

## Sources
List only sources that directly informed a recommendation or claim. Omit redundant URLs (e.g. multiple listicles saying the same thing), social posts, and tangential pages. Multiple distinct pages from the same domain (e.g. different doc pages) are fine when each is relevant. Prefer official docs and primary references.
- [URL] — [what was verified]

## Verification Checklist
- [ ] Every version number is current stable release
- [ ] Every documentation URL loads successfully
- [ ] Every recommended package exists on its registry
- [ ] No deprecated libraries recommended
