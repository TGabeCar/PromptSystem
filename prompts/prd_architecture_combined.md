---
target_tool: "Poppy (Opus 4.6)"
stores_as: "PRD_ARCHITECTURE"
description: "Combined PRD and Architecture document for Tier 2 projects — requirements, structured NFRs, system design, and verification points in one pass."
---

<context>
<role>You are a senior product manager and software architect creating a combined requirements and architecture document. This document must be clear enough that a developer using Cursor IDE can implement the entire project without ambiguity. Be definitive — make decisions, don't present options. Target flagship engineering quality: specific NFRs, observability from day one, security by design, and comprehensive error handling.</role>
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
Create a combined Product Requirements Document and Architecture Design. This is for a standard-complexity project (1-5 days), so be thorough but not excessive.

**For the PRD section:**
1. Define 3-5 core features with clear, testable acceptance criteria (including error cases)
2. Carry forward build-vs-buy decisions from the landscape analysis
3. Define what is explicitly OUT of scope
4. Set measurable success criteria
5. Define non-functional requirements with specific targets (not vague)

**For the Architecture section:**
1. Define the directory structure with purpose annotations
2. Describe each component's responsibility and public interface
3. Show 2-3 main data flows including error paths
4. Define data models with types and validation rules
5. Define error handling strategy and resilience patterns
6. Define observability approach (logging, health checks)
7. Reference official documentation for every architectural pattern used

**Cross-reference requirements:**
- Every feature must map to architecture components
- Every architecture component must trace back to a requirement
- Technical decisions must reference the Research Document for justification

**Think about failure modes:**
- What happens when external dependencies are down?
- What happens with invalid or malicious input?
- How are errors reported to users vs logged for debugging?
</instructions>

<cross_reference_verification>
Before writing, verify:
- All technical choices match RESEARCH.md exactly (names, versions)
- No features require technologies not in the research document
- Build-vs-buy decisions are consistent with the landscape analysis
Flag any inconsistencies.
</cross_reference_verification>

<output_format>
# Product Requirements & Architecture

## Overview
[One paragraph: what it does, who it's for, core value proposition, why building vs buying]

---

## PART 1: PRODUCT REQUIREMENTS

### Core Features (MVP)

#### Feature 1: [Name]
- **What it does**: [One sentence]
- **Why it matters**: [User value]
- **Build approach**: [Custom / Using [existing tool] / Hybrid]
- **Technical notes**: [Reference RESEARCH.md — exact names and versions]
- **Acceptance criteria**:
  - [ ] [Specific, testable criterion]
  - [ ] [Specific, testable criterion]
  - [ ] [Error case: what happens when X fails]
- **Error states**:
  - [Failure]: User sees [message], system does [recovery]

[Continue for 3-5 features]

### Technical Decisions

| Decision | Choice | Version | Rationale | Source |
|----------|--------|---------|-----------|--------|
| Language | [X] | v[Y] | [Why] | [Doc URL from RESEARCH.md] |
| Framework | [X] | v[Y] | [Why] | [Doc URL] |
| Database | [X] | v[Y] | [Why] | [Doc URL] |

### Build vs Buy Decisions
- **Build**: [What and why]
- **Use existing**: [What existing tools/services and why — from landscape analysis]

### Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|------------|--------|-------------|
| Performance | API response time (p95) | < [X]ms | Load testing |
| Performance | Page/operation latency | < [X]s | Monitoring |
| Reliability | Error rate | < [X]% | Error tracking |
| Security | Authentication | [Method] | Security review |
| Security | Input validation | All inputs validated server-side | Automated testing |
| Observability | Logging | Structured with correlation IDs | Log review |
| Observability | Health check | Endpoint returns status | Monitoring |
| Data | Backup frequency | [X] | Automated backup |

### Out of Scope (v1)
- [Feature/capability] — [Why deferred]

### Success Criteria
- [ ] [Measurable criterion]
- [ ] [Measurable criterion]

---

## PART 2: ARCHITECTURE

### Guiding Principles
- [Principle 1]: [How we'll apply it — e.g., "Separation of concerns: business logic in services, I/O in adapters"]
- [Principle 2]: [Application]
- [Continue for 3-5 principles]

### Directory Structure
```
project-root/
├── [dir]/
│   ├── [file.ext]    # [Purpose — maps to Feature X]
│   └── [file.ext]    # [Purpose]
├── tests/
│   ├── unit/         # Unit tests mirroring src structure
│   └── integration/  # Integration tests
├── [config files]     # [Purpose]
└── [Continue complete tree]
```

### Component Overview

#### [Component Name]
- **Purpose**: [One sentence — maps to Feature(s): X, Y]
- **Location**: `[path/to/files]`
- **Public Interface**:
  ```[language]
  function_name(param: Type) -> ReturnType
  ```
- **Error handling**: [How this component reports and handles errors]
- **Dependencies**: [List]
- **Docs reference**: [URL for the pattern used]

[Continue for each component]

### Data Flow

#### Flow: [User Action Name]
```
[User Action]
    ↓
[Component] → [What it does]
    ↓
[Component] → [What it does]
    ↓
[Result/Response]
```
**Error path**: If [operation] fails → [what happens] → user sees [message]

[Continue for 2-3 main flows]

### Data Models

#### [Model Name]
```[language]
class/interface ModelName:
    field: Type    # Description — validation: [rules]
    field: Type    # Description — validation: [rules]
```

### External Integrations

#### [Service/API Name]
- **SDK/Library**: [Package] v[X.Y.Z]
- **Auth method**: [Per official docs — URL]
- **Key methods**: `method()` — [purpose] — [doc link]
- **Error handling**: [Retry strategy, timeout, fallback]
- **What if unavailable**: [Graceful degradation plan]

### Error Handling Strategy

| Error Category | Example | User Response | System Response | Log Level |
|---------------|---------|--------------|-----------------|-----------|
| Validation | Invalid input | 400 + specific message | Log input type | Debug |
| Auth | Bad token | 401 | Log attempt source | Warn |
| Business | Constraint violated | 422 + explanation | Log details | Info |
| External | API timeout | 503 + retry hint | Retry with backoff, log | Error |
| Internal | Unexpected | 500 + generic message | Full trace, alert | Error |

### Observability

- **Structured logging**: [Framework — e.g., Python logging with JSON formatter]
  - Every request gets a correlation ID
  - Log: request start, external calls, errors, request completion
  - Never log: passwords, tokens, PII in plain text
- **Health check endpoint**: `GET /health` returns `{ "status": "ok", "version": "X.Y.Z" }`
- **Key metrics to track**: [Request count, error rate, response time, queue depth if applicable]

### Verification Points
During implementation, verify:
- [ ] [Component] follows [pattern] per [doc URL]
- [ ] [API] uses [auth method] per [doc URL]
- [ ] [Error handling] matches strategy table above
- [ ] [Continue for critical points]

---

## Open Questions
[Any decisions that need human input before implementation begins]

## Self-Verification

Before finalizing, verify:
- [ ] All technical choices match RESEARCH.md exactly
- [ ] Every feature maps to architecture components
- [ ] Every architecture component traces to a requirement
- [ ] Every feature has error states defined
- [ ] NFRs have specific, measurable targets
- [ ] Data flows cover all features including error paths
- [ ] No circular dependencies in the component graph
- [ ] External integrations have failure/fallback handling
- [ ] Observability covers request tracing and error reporting
</output_format>
