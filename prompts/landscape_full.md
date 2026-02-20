---
target_tool: "Grok (web search recommended)"
stores_as: "LANDSCAPE_ANALYSIS"
description: "Full landscape analysis for Tier 2/3 projects — exhaustive search for existing solutions before committing to custom development."
---

You are a senior solutions architect performing a comprehensive build-vs-buy analysis. Exhaustively search for existing solutions before the team commits to custom development. Every hour spent building something that already exists is wasted — but every hour spent fighting a tool that doesn't fit is also wasted. Find the right balance.

**Developer context:** Works at an AI-forward company. Language-agnostic; codes on Windows 11 (PowerShell/cmd). Available platforms and tools include:
- **Microsoft 365** (when relevant): SharePoint, Teams, Power Automate, Power Apps, Azure AD, Graph API
- **Zapier**: Connected to most of their SaaS tools
- **Azure**: Available for hosting and cloud services
- **Custom code**: Full dev stack (e.g. Python, .NET, Node) for when low-code or platform tools are too limited

They build internal tools, automations, dashboards, and some customer-facing products. Consider M365/Power Platform when they genuinely fit the use case — but do not favor them by default. Power Automate and similar low-code tools can be limited for complex logic, conditional flows, or non-standard integrations; recommend custom code or other solutions when they are a better fit.

## Project Description

{{PROJECT_DESCRIPTION}}

## Search Instructions

Use web search for every category below. For every claim, provide the source URL. Search thoroughly — check multiple sources per category.

### 1. Commercial SaaS Products
Search for established products that solve this problem. For each, evaluate:
- Feature coverage (what % of requirements does it meet?)
- Pricing model and estimated cost (find the actual pricing page)
- Integration capabilities (especially M365, REST APIs, webhooks)
- Vendor reliability (funding, customer base, years in market)
- Data residency and compliance certifications (SOC 2, GDPR)
- API availability (can we extend it programmatically?)
- Lock-in risk (data export capabilities, API stability)

### 2. Open Source Projects
Search GitHub, GitLab, PyPI, npm, and NuGet for open source solutions. For each, evaluate:
- Maturity (GitHub stars, recent commits, number of contributors, last release date)
- Feature coverage vs requirements
- Maintenance health (open issues vs closed ratio, PR merge velocity, bus factor)
- License compatibility (MIT, Apache 2.0, GPL — note commercial use restrictions)
- Documentation quality (does it have real docs or just a README?)
- Community size (Discord/Slack, Stack Overflow questions)
- Security (known CVEs, dependency audit results)

### 3. Platform Solutions (M365 / Power Platform / Zapier)
Search for:
- Power Automate flow templates that match this use case
- Power Apps templates or components
- SharePoint configurations, lists, or features that solve pieces
- Teams apps or integrations in the Teams app store
- Zapier zap templates or multi-step workflows
- Microsoft Graph API capabilities that handle core operations
- Azure Logic Apps templates

### 4. APIs and SDKs
Search for third-party APIs or SDKs that solve significant portions of the problem:
- REST APIs that provide the core data or functionality
- SDKs in any major language (Python, .NET, Node/JS, etc.) that wrap complex operations
- Services that handle the hardest part of the problem (e.g., PDF generation, email delivery, payment processing)
- Evaluate: pricing per API call, rate limits, reliability SLA, documentation quality

### 5. Hybrid Approaches
Consider combinations: "Use [SaaS] for [X] and build custom [Y] to fill the gap."

## Build-vs-Buy Evaluation Criteria

| Criterion | Weight | Notes |
|-----------|--------|-------|
| Development time vs subscription cost | High | Include maintenance time, not just initial build |
| Maintenance burden | High | Custom code requires ongoing updates, dependency management |
| Customization needs vs out-of-box fit | High | 80% fit with workarounds vs 100% fit custom |
| Integration complexity | Medium | How hard to connect to existing systems? |
| Total cost of ownership (3-year view) | High | License + dev time + maintenance + migration risk |
| Data ownership and security | High | Where does data live? Who has access? Export options? |
| Vendor/project longevity risk | Medium | Will this tool exist in 2 years? |
| Time to value | Medium | How fast can we start using it? |

Consider M365/Power Platform when they meet requirements without heavy workarounds; when they don't (e.g. complex logic, limited connectors, poor fit), prefer custom code or other tools. Do not bias toward M365 by default.

## Uncertainty Rules

- If you cannot verify a product's features or pricing: "UNVERIFIED: [claim] — verify at [URL]"
- If you cannot confirm an open source project is maintained: "CHECK: Last commit date and issue activity at [GitHub URL]"
- If pricing is unclear or requires contacting sales: note "Contact sales — pricing not public"
- Do not recommend tools you cannot verify exist. State what you searched for and what you found.
- If you find conflicting information, cite both sources

## Output Format

# Landscape Analysis

## Executive Summary
[2-3 sentences: what exists, what doesn't, and the preliminary recommendation. Be definitive.]

## Solution Comparison Matrix

The matrix must include at least 3 options per major capability (when they exist). For each option scored but not chosen, include explicit rejection reasoning.

| Solution | Type | Cost | Meets Our Needs | Ease of Adoption | Maintenance Burden | Community/Support | Verdict |
|----------|------|------|-----------------|------------------|--------------------|-------------------|---------|
| [Name] | SaaS/OSS/Platform/Custom | [Breakdown: tiers, $/mo, limits, or Free] | [X]% — [what it covers vs gaps] | [1-5] | [We maintain vs they maintain] | [Active/Declining/Dead] | Adopt / Fork / Pass — [one-sentence reason] |

## Detailed Analysis

### Commercial SaaS
[For each solution: name, URL, what it does well, gaps, pricing (breakdown: tiers/plans, $/mo or $/yr, limits; source URL), integration notes, security/compliance posture, lock-in risk]

### Open Source
[For each: name, GitHub URL, stars/activity, license, what it does well, gaps, maintenance risk, documentation quality, known security issues]

### Platform Solutions (M365 / Power Platform / Zapier)
[For each: what it is, how it would work, limitations, setup complexity, cost within existing licenses]

### APIs and SDKs
[For each: name, docs URL, what it handles, language support, pricing model, rate limits, reliability]

## Build vs Buy Recommendation

### Recommendation: [BUILD CUSTOM / USE EXISTING / HYBRID]

**Reasoning:**
- [Evidence-based point 1 — reference specific evaluation criteria]
- [Evidence-based point 2]
- [Evidence-based point 3]

**If HYBRID, the split is:**
- Use [existing tool] for: [capabilities] — [why this part shouldn't be custom]
- Build custom: [what and why] — [why no existing solution fits]

**If BUILD CUSTOM:**
- Key libraries/SDKs to leverage: [list with docs URLs and versions]
- Estimated development advantage over from-scratch: [X hours saved]
- What NOT to build (use existing for these): [list with tool names and URLs]

**If USE EXISTING:**
- Recommended solution: [name and URL]
- Setup steps: [high-level]
- Known gaps to work around: [list]

## Risk Assessment
- **Biggest risk if building custom**: [risk + mitigation]
- **Biggest risk if using existing**: [risk + mitigation]
- **Supply chain risk**: [dependency on third-party tools/APIs — what if they change or disappear?]

## Sources Consulted
List only sources that directly informed a recommendation or claim. Omit redundant URLs (e.g. multiple listicles saying the same thing), social posts, and tangential pages. Multiple distinct pages from the same domain (e.g. different doc pages) are fine when each is relevant. Prefer official docs and primary references.
- [URL] — [what information was gathered]

## Self-Verification Checklist
Before finalizing this analysis:
- [ ] Every recommended tool/service has a working, verified URL
- [ ] Pricing claims link to actual pricing pages, not blog posts
- [ ] Open source stars/activity data has been checked on the actual GitHub page
- [ ] License compatibility has been verified for commercial/internal use
- [ ] No recommended tool has unpatched critical CVEs
- [ ] Integration claims are based on actual API documentation, not marketing copy
- [ ] At least 3 categories were thoroughly searched (SaaS, OSS, Platform, APIs)
- [ ] The recommendation is supported by specific evidence, not assumptions
