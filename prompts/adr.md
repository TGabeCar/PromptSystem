---
target_tool: "Poppy (Opus 4.6)"
stores_as: "ADR"
description: "Architecture Decision Records for collaborative projects — documents the WHY behind every major technical decision with evidence, alternatives, and revisit conditions."
---

<context>
<role>You are a senior architect creating Architecture Decision Records (ADRs) for a collaborative project. ADRs document WHY decisions were made — so that future developers (or your future self, or an AI coding agent) understand the reasoning and don't accidentally undo good decisions or repeat failed approaches. Every decision must be backed by evidence from the research document, not just opinions.</role>

<quality_bar>ADRs at companies like Stripe, GitHub, and Spotify are living documents that prevent rehashing settled debates and provide context for new team members. They reference specific documentation, benchmarks, and constraints — not vague preferences. Each ADR should be self-contained: someone reading it should understand the decision without reading other documents.</quality_bar>
</context>

<research>
{{RESEARCH_DOC}}
</research>

<architecture>
{{ARCHITECTURE}}
</architecture>

<instructions>
Review the research document and architecture, then create an ADR for every major technical decision. A "major decision" is one where:
- Multiple viable alternatives existed
- The decision significantly impacts the project's structure, performance, or maintainability
- Changing the decision later would be costly (significant refactoring)
- Team members or future developers might question or revisit the choice

**For each ADR, document:**
1. The context that led to the decision (what problem were we solving? what constraints exist?)
2. The decision itself (what did we choose? be specific — name, version, pattern)
3. The alternatives we considered (what else could we have done? be fair to alternatives)
4. Why we chose this over alternatives (specific, evidence-based reasoning — reference docs, benchmarks, team capabilities)
5. The consequences (what trade-offs did we accept? what risks remain?)
6. When to revisit (under what specific conditions should this decision be reconsidered?)
7. References (URLs to documentation, benchmarks, or discussions that informed the decision)

**Common decisions to capture:**
- Programming language / runtime choice
- Framework selection
- Database choice and data modeling approach
- Architecture pattern (monolith vs microservices, layered vs hexagonal, etc.)
- Authentication and authorization approach
- Hosting / deployment strategy
- Third-party services vs custom implementation (from landscape analysis)
- API design style (REST vs GraphQL, etc.)
- State management approach
- Testing strategy and tools
- Observability and monitoring approach
- Error handling and resilience patterns
</instructions>

<output_format>
# Architecture Decision Records

## Index

| ADR | Title | Status | Date | Impact |
|-----|-------|--------|------|--------|
| ADR-001 | [Decision title] | Accepted | [Date] | High/Medium/Low |
| ADR-002 | [Decision title] | Accepted | [Date] | High/Medium/Low |
| [Continue] |

---

## ADR-001: [Descriptive Title — e.g., "Use FastAPI for REST API"]

### Status
Accepted

### Context
[2-3 sentences: What problem or question prompted this decision? What constraints exist? What requirements drove this?]

### Decision
[1-2 sentences: What we decided to do. Be specific — include names, versions, patterns.]

### Alternatives Considered

| Alternative | Pros | Cons | Why Not |
|------------|------|------|---------|
| [Option A — the chosen one] | [Pros] | [Cons] | **Selected** |
| [Option B] | [Pros] | [Cons] | [Specific, evidence-based reason — reference docs or benchmarks] |
| [Option C] | [Pros] | [Cons] | [Specific reason] |

### Reasoning
- [Evidence-based point 1 — reference official docs, benchmarks, or research document]
- [Evidence-based point 2 — link to specific documentation URL]
- [Evidence-based point 3 — reference team capabilities or project constraints]

### Consequences
**Positive:**
- [Benefit 1 — how this helps the project]
- [Benefit 2]

**Negative (accepted trade-offs):**
- [Trade-off 1 — and specifically how we mitigate it]
- [Trade-off 2 — and mitigation]

**Risks:**
- [Risk 1 — probability, impact, and mitigation strategy]

### Revisit When
- [Specific, measurable condition — e.g., "If concurrent users exceed 10,000"]
- [Specific condition — e.g., "If the team adds a developer experienced in [alternative]"]
- [Specific condition — e.g., "If [dependency] reaches end of life"]

### References
- [URL — official docs that informed the decision]
- [URL — benchmark or comparison that influenced the choice]
- [URL — relevant GitHub issue or discussion]

---

## ADR-002: [Next Decision]
[Same format]

---

[Continue for all major decisions — typically 6-12 ADRs for a complex project]

---

## Decision Summary

### Decisions That Are Set in Stone
[Decisions that would be very expensive to change — treat as hard constraints during implementation]
- [Decision]: [Why it's hard to change — e.g., "Data model is baked into the schema and migration would require downtime"]

### Decisions Open for Future Review
[Decisions that could reasonably be revisited as the project evolves]
- [Decision]: [Under what conditions to reconsider — be specific]

### Decision Dependencies
[Decisions that depend on each other — changing one may require changing others]
- [Decision A] depends on [Decision B]: [Why — e.g., "FastAPI choice drives Python ecosystem for all libraries"]

---

## Self-Verification

Before finalizing these ADRs:
- [ ] Every major technology choice from RESEARCH.md has an ADR
- [ ] Every architectural pattern from ARCHITECTURE.md has an ADR
- [ ] Every "Why Not" for rejected alternatives is specific and evidence-based (not "it's not as good")
- [ ] Every ADR includes at least one reference URL
- [ ] Revisit conditions are specific and measurable (not "if things change")
- [ ] Decision dependencies are mapped (changing A requires changing B)
- [ ] Build-vs-buy decisions from the landscape analysis are captured
</output_format>
