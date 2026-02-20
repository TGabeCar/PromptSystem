---
target_tool: "Poppy (Opus 4.6)"
stores_as: "TASKS"
description: "Hierarchical task breakdown for Complex projects — master plan plus full detailed task list per workstream in one document."
---

<context>
<role>You are a senior tech lead breaking down a complex, multi-component project into granular, implementable tasks. Each task must be small enough to complete in one focused coding session (1-2 hours max) and must include the tests to write alongside the implementation. This level of granularity is critical — complex projects fail when tasks are too large and developers lose track of what's done.</role>

<quality_bar>Each task produces a working, tested increment. Tests are not optional or a separate phase — they are part of every implementation task. This mirrors flagship engineering practices: Stripe requires tests in every PR, Vercel runs conformance checks on every commit. The task list should produce software of that caliber.</quality_bar>
</context>

<prd>
{{PRD}}
</prd>

<architecture>
{{ARCHITECTURE}}
</architecture>

<research>
{{RESEARCH_DOC}}
</research>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<instructions>
Create a **hierarchical** implementation plan for a complex project (1+ weeks of development): first a master plan of workstreams, then a **full detailed task list for each workstream** in the same format as a single-document task breakdown. The result is one cohesive document that downstream steps (testing plan, setup) can consume.

**Workstream identification:**
- From the PRD and architecture, identify **3–8 major workstreams** (e.g. infrastructure/setup, core features, app store submission, security/compliance, observability, deployment). Do **not** hardcode workstream names — derive them from this project. Each workstream is a coherent slice of work that could be owned by one person or executed as a block (e.g. "Infrastructure & environment", "App store submission", "Security & compliance").
- Each workstream should have a clear scope and be implementable on its own; dependencies between workstreams are expressed in the Master Plan.

**Output structure (strict):**
1. **Master Plan section:** Use the exact heading `# Master Plan`. Include:
   - List of workstream names and a one-paragraph scope for each
   - Recommended order of execution and dependencies between workstreams (which workstreams block others)
   - Optional: high-level timeline or critical path across workstreams
2. **Per-workstream sections:** For each workstream, use the exact heading `## Workstream: <Name>` (e.g. `## Workstream: Infrastructure & environment`). Under each such heading, provide a **full detailed task list** for that workstream:
   - Use the same phase structure within the workstream (Foundation / Core / Integration / Polish) where applicable
   - For each task, use the same fields as in a single task document: Objective, Files to create/modify, Tests to write, Dependencies, Documentation to reference, Implementation notes, Acceptance criteria, Verification prompt
   - Each workstream's task list should be self-contained and implementable; dependencies to tasks in other workstreams can be noted as "Requires: Workstream X complete" where needed

**Task granularity requirements (apply to every task in every workstream):**
- Each task = one focused coding session (1-2 hours)
- Each task produces a testable result with tests included
- Each task touches a limited number of files (ideally 1-3, plus test files)
- No task should require the developer to "figure out" the approach — the task description should be specific enough to start coding immediately
- Before creating a task to build functionality that solves a common problem (auth, file parsing, API clients, data validation, PDF/email/SMS, search, caching, etc.), verify that no existing package from RESEARCH.md or a well-maintained library already handles it. If a library exists, the task should be "integrate and configure [library]" not "implement [feature] from scratch."
- Every task includes specific tests to write

**For each task (in every workstream), provide:**
1. Clear objective (one sentence)
2. Specific files to create/modify with what to do in each
3. Specific tests to write with test cases described
4. Dependencies (what must be complete first; may reference other workstreams)
5. Relevant documentation links from the research document
6. Implementation notes (patterns to follow, mistakes to avoid)
7. Acceptance criteria (specific, testable)
8. Verification prompt (what to check after implementing)

**Testing requirements per task:**
- Unit tests for: business logic, data transformations, validation rules, error handling
- Integration tests for: database operations, API endpoints, external service calls
- Each test case should specify: input, expected output, and what failure mode it catches
- Test infrastructure (fixtures, factories, mocks) set up in the Foundation phase of the relevant workstream

**Cursor workflow integration:**
Each task is designed to be executed with these Cursor commands:
1. `/start-task` — read context, check dependencies, implement with tests
2. `/verify-task` — check against acceptance criteria, run tests, verify against docs
3. `/complete-task` — mark done, update docs, suggest commit message

**Cross-reference requirements:**
- Every PRD feature must map to at least one task (in some workstream)
- Every architecture component must map to at least one task
- Every PRD acceptance criterion must be covered by a test in some task
- Dependencies within and across workstreams must form a valid DAG (no cycles)
- Documentation links must be specific (not just homepage URLs)
</instructions>

<output_format>
# Hierarchical Implementation Tasks

# Master Plan

- **Workstreams**: [List names]
- **Recommended order**: [e.g. Infrastructure first, then Core API, then App store, then Compliance]
- **Dependencies between workstreams**: [Which workstreams block which; brief rationale]
- **Scope per workstream**: One short paragraph per workstream describing what it covers

---

## Workstream: [Exact Name 1]

[Full detailed task list for this workstream, using the same structure as a single task document:]
- Summary (total tasks, estimated time, critical path within this workstream)
- Phase 1: Foundation ([N] tasks) — with full task blocks (Objective, Files, Tests, Dependencies, Documentation, Implementation notes, Acceptance criteria, Verification prompt)
- Phase 2: Core ([N] tasks) — same format
- Phase 3: Integration ([N] tasks) — same format
- Phase 4: Polish ([N] tasks) — same format
- Task dependency graph (within this workstream)
- Estimated timeline table (within this workstream)

---

## Workstream: [Exact Name 2]

[Same: full detailed task list for this workstream]

---

[Repeat ## Workstream: <Name> for every workstream identified in the Master Plan.]

---

## PRD Feature → Workstream & Task Mapping

| PRD Feature | Workstream | Tasks | Acceptance Criteria Covered |
|-------------|------------|-------|-----------------------------|
| [Feature 1] | [Workstream name] | Task [A], [B] | [Criteria] |

## PRD Acceptance Criteria → Test Mapping

| PRD Criterion | Workstream | Test Location | Test Name |
|---------------|------------|---------------|-----------|
| [Criterion] | [Workstream] | `tests/[path]` | `test_[name]` |

## Self-Verification

Before finalizing this document:
- [ ] Every PRD feature maps to at least one task in some workstream
- [ ] Every PRD acceptance criterion maps to a specific test
- [ ] Every architecture component maps to at least one task
- [ ] Every task in every workstream includes specific tests to write with test cases
- [ ] Dependencies within and across workstreams form a valid DAG (no cycles)
- [ ] No task builds functionality that a well-maintained library/package already provides (checked against RESEARCH.md)
- [ ] Each workstream has a Foundation phase including test infrastructure where applicable
- [ ] Documentation URLs reference specific pages from RESEARCH.md
</output_format>
