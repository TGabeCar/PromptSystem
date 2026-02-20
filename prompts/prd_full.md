---
target_tool: "Poppy (Opus 4.6)"
stores_as: "PRD"
description: "Full Product Requirements Document for Tier 3 projects — detailed features, structured NFRs, acceptance criteria, observability requirements, and compliance considerations."
---

<context>
<role>You are a senior product manager creating a comprehensive PRD for a complex project that will be built to flagship engineering standards. This document must be precise enough that developers and AI coding agents can implement without asking clarifying questions. Make definitive decisions — no option menus. Every feature needs clear acceptance criteria that can be tested. Every non-functional requirement needs measurable targets.</role>

<quality_bar>The software built from this PRD should be indistinguishable in quality from what a senior engineering team at Stripe, Linear, or Vercel would produce. That means: specific SLOs, observability from day one, security by design, comprehensive error handling, and accessibility as a requirement — not an afterthought.</quality_bar>
</context>

<research>
{{RESEARCH_DOC}}
</research>

<landscape>
{{LANDSCAPE_ANALYSIS}}
</landscape>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<instructions>
Create a thorough Product Requirements Document for a complex project (1+ weeks of development, potentially customer-facing).

**Requirements for each feature:**
- Clear, unambiguous description of what it does
- Who uses it and when (link to personas)
- Acceptance criteria that are SPECIFIC and TESTABLE (e.g., "User can upload a CSV file up to 50MB and see parsed results within 10 seconds" — not "file upload works")
- Error states: what happens when this feature fails? What does the user see?
- Technical notes referencing the research document
- Priority (P0 = must-have for launch, P1 = important but can follow, P2 = nice to have)

**Build-vs-buy integration:**
- Carry forward all decisions from the landscape analysis
- For each feature, note whether it uses existing tools/APIs or is custom-built
- If the landscape recommended specific SaaS/APIs, reference them in the feature specs

**For customer-facing products, additionally address:**
- User roles and permissions model with explicit access matrix
- Data privacy and compliance requirements (GDPR, CCPA, SOC 2 as applicable)
- Error states with user-facing error messages (not just "something went wrong")
- Loading states and performance expectations per interaction
- Accessibility requirements (WCAG 2.1 AA minimum)

**Non-functional requirements must be specific and measurable — no vague statements.**

**Think about what could go wrong:**
- What are the failure modes for each feature?
- What happens under load?
- What happens with malicious input?
- What happens when external dependencies are down?
</instructions>

<cross_reference_verification>
Before writing the PRD, verify:
- All technologies referenced match RESEARCH.md exactly (names, versions)
- No features require technologies not in the research document
- Build-vs-buy decisions are consistent with the landscape analysis
Flag any inconsistencies rather than silently resolving them.
</cross_reference_verification>

<output_format>
# Product Requirements Document

## Overview
[2-3 paragraphs: what the product does, who it's for, the core value proposition, and why it's being built. Reference the landscape analysis for build-vs-buy justification.]

## User Personas

### [Persona 1: e.g., "Internal Admin"]
- **Who**: [Description]
- **Goals**: [What they want to accomplish]
- **Pain points**: [What's hard today]
- **Technical proficiency**: [Relevant for UI/UX decisions]

[Continue for each persona]

---

## Core Features (MVP — P0)

### Feature 1: [Name]
- **What it does**: [Clear, unambiguous description]
- **User**: [Which persona(s)]
- **Trigger**: [When/how the user initiates this]
- **Build approach**: [Custom / Using [existing tool from landscape] / Hybrid]
- **Technical notes**: [Reference RESEARCH.md technologies — exact names and versions]
- **Acceptance criteria**:
  - [ ] [Specific, testable — include data types, sizes, timing if relevant]
  - [ ] [Specific, testable]
  - [ ] [Error case: what happens when X fails — specific user-facing behavior]
  - [ ] [Edge case: what happens with empty/invalid/oversized input]
- **Error states**:
  - [Failure mode 1]: User sees [specific message], system does [specific recovery]
  - [Failure mode 2]: User sees [specific message], system does [specific recovery]

[Continue for all P0 features]

---

## Important Features (P1)

[Same format as P0, but these ship shortly after MVP]

---

## Future Features (P2)

[Lighter format — name, description, rough technical notes, why deferred]

---

## Technical Decisions

| Decision | Choice | Version | Rationale | Source |
|----------|--------|---------|-----------|--------|
| [Category] | [Tech] | v[X.Y.Z] | [Why — reference project requirements] | [Doc URL from RESEARCH.md] |

## Build vs Buy Summary

| Capability | Approach | Tool/Service | Justification |
|-----------|----------|--------------|---------------|
| [Capability] | Build/Buy/Hybrid | [Name or "Custom"] | [Why — reference landscape analysis] |

---

## Non-Functional Requirements

### Performance
| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| API response time (p95) | < [X]ms | Load testing with [tool] |
| Page load time (initial) | < [X]s | Lighthouse / Web Vitals |
| Throughput | [X] requests/second | Load testing |
| Database query time (p95) | < [X]ms | Query logging |

### Reliability & Availability
| Metric | Target | Notes |
|--------|--------|-------|
| Uptime SLO | [X]% (e.g., 99.9%) | [What counts as downtime] |
| Error budget | [X]% per month | [How errors are counted] |
| Recovery time objective (RTO) | < [X] minutes | [For what failure scenarios] |
| Recovery point objective (RPO) | < [X] minutes of data loss | [Backup strategy] |

### Security & Compliance
- **Authentication**: [Method — e.g., OAuth2 via Azure AD, JWT, session-based]
- **Authorization model**: [RBAC/ABAC with roles defined]
- **Data classification**: [What data is sensitive, PII, confidential]
- **Compliance requirements**: [GDPR, CCPA, SOC 2, HIPAA — whichever apply, or "Internal use only — standard security practices"]
- **Encryption**: [At rest: AES-256, In transit: TLS 1.2+]
- **Secrets management**: [Environment variables / Azure Key Vault / etc.]
- **Audit requirements**: [What events must be logged for compliance]

### Observability
- **Logging**: Structured logging with correlation IDs for request tracing
- **Metrics**: [Key business and technical metrics to collect]
- **Alerting**: [What conditions trigger alerts, who gets notified]
- **Health checks**: [Endpoints for liveness and readiness probes]
- **Error tracking**: [How errors are captured, aggregated, and reported]

### Deployment & Operations
- **Deployment method**: [CI/CD pipeline, container orchestration, serverless, etc.]
- **Environment strategy**: [Development, staging, production]
- **Rollback plan**: [How to revert a bad deployment]
- **Configuration management**: [How config differs between environments]

### Scalability
- **Expected initial load**: [Users, requests, data volume]
- **Growth projection**: [Expected growth over 6-12 months]
- **Scaling strategy**: [Horizontal/vertical, auto-scaling triggers]
- **Known bottlenecks**: [What will break first under load]

### Accessibility
- **WCAG level**: [2.1 AA / 2.1 AAA — or "N/A for API-only"]
- **Specific requirements**: [Keyboard navigation, screen reader support, color contrast, focus management]
- **Testing approach**: [Tools and manual testing plan]

### Data Management
- **Retention policy**: [How long data is kept, what triggers deletion]
- **Backup strategy**: [Frequency, storage, verification]
- **Data export**: [Can users export their data? Format?]
- **Migration plan**: [How data moves between environments or from existing systems]

---

## Out of Scope (v1)
- [Feature/capability] — [Why deferred, when it might be revisited]
- [Continue for 5-8 items — be explicit so scope doesn't creep]

## Success Criteria
- [ ] [Measurable: "X users complete Y workflow within Z minutes"]
- [ ] [Measurable: "Error rate below X% for core operations"]
- [ ] [Measurable: "All P0 acceptance criteria pass automated testing"]
- [ ] [Measurable: "Security scan shows zero critical/high vulnerabilities"]
- [ ] [Continue for 5-8 items]

## Open Questions
[Decisions that need stakeholder input before development]
1. [Question] — [Impact on implementation] — [Default assumption if no answer]

---

## Self-Verification

Before finalizing, verify:
- [ ] All technical choices match RESEARCH.md exactly (names, versions)
- [ ] No features require technologies not in the research document
- [ ] Build-vs-buy decisions are consistent with the landscape analysis
- [ ] Every P0 feature has at least 3 testable acceptance criteria
- [ ] Every P0 feature has error states defined
- [ ] Every NFR has a specific, measurable target (no "should be fast" or "highly available")
- [ ] Success criteria are measurable with specific metrics
- [ ] Out-of-scope items are clearly justified
- [ ] Security requirements are appropriate for the project type (customer-facing vs internal)
- [ ] Observability requirements will enable debugging production issues
</output_format>
