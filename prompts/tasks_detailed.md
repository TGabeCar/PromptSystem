---
target_tool: "Poppy (Opus 4.6)"
stores_as: "TASKS"
description: "Detailed task breakdown for Tier 3 projects — granular phases with testing per task, dependency graph, verification prompts, and estimated timeline."
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
Create a detailed implementation plan for a complex project (1+ weeks of development).

**Task granularity requirements:**
- Each task = one focused coding session (1-2 hours)
- Each task produces a testable result with tests included
- Each task touches a limited number of files (ideally 1-3, plus test files)
- No task should require the developer to "figure out" the approach — the task description should be specific enough to start coding immediately
- Before creating a task to build functionality that solves a common problem (auth, file parsing, API clients, data validation, PDF/email/SMS, search, caching, etc.), verify that no existing package from RESEARCH.md or a well-maintained library already handles it. If a library exists, the task should be "integrate and configure [library]" not "implement [feature] from scratch."
- Every task includes specific tests to write

**Phase structure:**
- **Phase 1: Foundation** — Project scaffolding, configuration, core types, shared utilities, test infrastructure
- **Phase 2: Core** — Primary features in dependency order, one feature at a time, each with tests
- **Phase 3: Integration** — Connecting components, external service integration, end-to-end flows, integration tests
- **Phase 4: Polish** — Error handling hardening, observability setup, performance optimization, security review, final testing

**For each task, provide:**
1. Clear objective (one sentence)
2. Specific files to create/modify with what to do in each
3. Specific tests to write with test cases described
4. Dependencies (what must be complete first)
5. Relevant documentation links from the research document
6. Implementation notes (patterns to follow, mistakes to avoid)
7. Acceptance criteria (specific, testable)
8. Verification prompt (what to check after implementing)

**Testing requirements per task:**
- Unit tests for: business logic, data transformations, validation rules, error handling
- Integration tests for: database operations, API endpoints, external service calls
- Each test case should specify: input, expected output, and what failure mode it catches
- Test infrastructure (fixtures, factories, mocks) set up in Phase 1

**Cursor workflow integration:**
Each task is designed to be executed with these Cursor commands:
1. `/start-task` — read context, check dependencies, implement with tests
2. `/verify-task` — check against acceptance criteria, run tests, verify against docs
3. `/complete-task` — mark done, update docs, suggest commit message

**Cross-reference requirements:**
- Every PRD feature must map to at least one task
- Every architecture component must map to at least one task
- Every PRD acceptance criterion must be covered by a test in some task
- Dependencies must form a valid DAG (no cycles)
- Documentation links must be specific (not just homepage URLs)
</instructions>

<output_format>
# Detailed Implementation Tasks

## Summary
- **Total tasks**: [N]
- **Estimated total time**: [X] hours / [Y] days
- **Critical path**: Task [A] → Task [B] → Task [C] → ... (longest dependency chain)
- **Testing approach**: Unit tests per task, integration tests in Phase 3, security tests in Phase 4

---

## Phase 1: Foundation ([N] tasks, ~[X] hours)

### Task 1: [Descriptive Name]
**Objective**: [One sentence]

**Files to create/modify**:
- `[path/file.ext]` — [What to create: types, classes, functions]
- `[path/file.ext]` — [What to modify and how]

**Tests to write**:
- `tests/unit/test_[name].ext`:
  - `test_[valid_case]` — Input: [X], Expected: [Y] — Catches: [failure mode]
  - `test_[edge_case]` — Input: [empty/null/max], Expected: [Y] — Catches: [failure mode]
  - `test_[error_case]` — Input: [invalid], Expected: [error type] — Catches: [failure mode]

**Dependencies**:
- Requires: None
- Blocks: [Task numbers]

**Documentation to reference**:
- [Specific topic]: [URL — specific page, not homepage]

**Implementation notes**:
- [Specific pattern to follow — reference architecture document section]
- [Common mistake to avoid — from research document gotchas]

**Acceptance criteria**:
- [ ] [Specific, testable]
- [ ] [Specific, testable]
- [ ] All tests pass: `[test command for this task's tests]`

**Verification prompt**:
```
After implementing Task 1, verify:
1. [Specific check — e.g., "All type hints pass mypy"]
2. [Specific check — e.g., "Config loads from environment variables"]
3. [Specific check — e.g., "Unit tests pass with X test cases"]
```

---

[Continue for all Phase 1 tasks — include test infrastructure setup as Task 1 or 2]

---

## Phase 2: Core Features ([N] tasks, ~[X] hours)

[Same detailed format — every task includes "Tests to write" section]

---

## Phase 3: Integration ([N] tasks, ~[X] hours)

[Same format — focus on integration tests, end-to-end flows, external service testing]

---

## Phase 4: Polish ([N] tasks, ~[X] hours)

[Same format — error handling hardening, observability, performance, security review tasks]

### Task N: Observability Setup
**Objective**: Add structured logging, health checks, and error tracking

**Files to create/modify**:
- [Logging configuration file]
- [Health check endpoint]
- [Error tracking middleware]

**Tests to write**:
- Health check endpoint returns 200 with expected format
- Structured log output includes correlation_id, timestamp, level
- Error responses include correlation_id for debugging

### Task N+1: Security Review
**Objective**: Verify all security requirements from PRD are met

**Tests to write**:
- Input validation rejects: SQL injection, XSS, oversized input
- Authentication required on all protected endpoints
- Authorization checks prevent cross-user data access
- No secrets in code or logs

---

## Task Dependency Graph
```
Phase 1:
  Task 1 (None)
      ↓
  Task 2 ─────→ Task 3
      ↓              ↓
Phase 2:
  Task 4 ←──── Task 5
      ↓
  Task 6 → Task 7
      ↓       ↓
Phase 3:
  Task 8 ← ─ ─┘
      ↓
Phase 4:
  Task 9 → Task 10
```

## Estimated Timeline

| Phase | Tasks | Est. Time | Cumulative |
|-------|-------|-----------|------------|
| Foundation | 1-[N] | [X]h | [X]h |
| Core | [N+1]-[M] | [X]h | [X]h |
| Integration | [M+1]-[P] | [X]h | [X]h |
| Polish | [P+1]-[End] | [X]h | [X]h |

## PRD Feature → Task Mapping

| PRD Feature | Tasks | Acceptance Criteria Covered |
|-------------|-------|-----------------------------|
| [Feature 1] | Task [A], [B], [C] | [Which PRD criteria each task covers] |
| [Feature 2] | Task [D], [E] | [Which criteria] |

## PRD Acceptance Criteria → Test Mapping

| PRD Criterion | Test Location | Test Name |
|---------------|--------------|-----------|
| [Feature 1, Criterion 1] | `tests/[path]` | `test_[name]` |
| [Feature 1, Criterion 2] | `tests/[path]` | `test_[name]` |
| [Continue for ALL PRD acceptance criteria] |

## Final Verification Checklist
Before considering the project complete:
- [ ] All acceptance criteria across all tasks are met
- [ ] All unit tests pass (`[command]`)
- [ ] All integration tests pass (`[command]`)
- [ ] All security tests pass
- [ ] Error handling covers all external operations and user inputs
- [ ] No hardcoded secrets or credentials
- [ ] Structured logging in place for all key operations
- [ ] Health check endpoint returns correct status
- [ ] Security requirements from PRD are addressed
- [ ] Performance meets NFR targets from PRD
- [ ] Code follows architecture patterns
- [ ] Documentation reflects actual implementation

---

## Self-Verification

Before finalizing this task list:
- [ ] Every PRD feature maps to at least one task
- [ ] Every PRD acceptance criterion maps to a specific test
- [ ] Every architecture component maps to at least one task
- [ ] Every task includes specific tests to write with test cases
- [ ] Dependencies form a valid DAG (no cycles)
- [ ] No task builds functionality that a well-maintained library/package already provides (checked against RESEARCH.md and package registries)
- [ ] Phase 1 includes test infrastructure setup
- [ ] Phase 4 includes observability and security review tasks
- [ ] Documentation URLs reference specific pages from RESEARCH.md
- [ ] Total estimated time is realistic for a complex project
- [ ] Critical path is identified and reasonable
</output_format>
