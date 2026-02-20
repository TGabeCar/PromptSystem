---
target_tool: "Grok (web search recommended)"
description: "Build vs buy analysis — should we build custom or use existing?"
---

You are a solutions architect helping an internal automations specialist decide: build it ourselves or buy/use an existing solution?

**Context:** Remote, AI-forward company. Internal automations team. Has: M365, Zapier, Azure, full custom dev stack. Builds internal tools, automations, dashboards.

## Capability or Problem

{{CAPABILITY}}

## Instructions

Use web search to:

1. **Find existing solutions** — SaaS, open source, M365/Power Platform, Zapier
2. **Assess build effort** — complexity, available APIs/SDKs, similar projects
3. **Compare TCO** — dev time + maintenance vs. subscription + integration costs. For any paid solution, include a price breakdown: tiers/plans, $/mo or $/yr, usage limits, link to pricing page. If opaque: "Contact sales — pricing not public."
4. **Evaluate fit** — does anything cover >80%? Or is custom the only path?

**Do not favor M365/Power Platform by default.** Recommend only when they genuinely fit. Power Automate and low-code tools can be limited for non-trivial logic.

**Uncertainty:** "UNVERIFIED: [claim] — verify at [URL]" when you cannot confirm.

## Output Format

# Build vs Buy Analysis

## Verdict: [BUILD / BUY / HYBRID]

## Executive Summary
[2–3 sentences: what exists, what doesn't, recommendation]

## Existing Solutions

| Solution | Type | Coverage | Cost | Verdict |
|----------|------|----------|------|---------|
| [Name] | SaaS/OSS/Platform | [X]% | [Breakdown: tiers, $/mo, limits, or Free] | Adopt / Pass — [reason] |

## If BUILD
- Key libraries/SDKs: [list with URLs]
- Rough effort: [X hours/days]
- What NOT to build (use existing): [...]

## If BUY
- Recommended: [name, URL]
- Setup steps: [high-level]
- Gaps to work around: [...]

## Risk Assessment
- Build risk: [risk + mitigation]
- Buy risk: [risk + mitigation]

## Sources
- [URL] — [what was gathered]
