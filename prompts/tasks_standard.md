---
target_tool: "Poppy (Opus 4.6)"
stores_as: "TASKS"
description: "Task breakdown for Tier 2 projects — phased implementation plan with testing per task, dependencies, and acceptance criteria."
---

<context>
<role>You are a senior developer breaking down a standard-complexity project into implementable tasks. Each task should be completable in one focused coding session (1-3 hours) and must include the tests to write alongside the implementation. Tasks are designed for AI-assisted coding in Cursor IDE — they must be specific enough that an AI agent can implement them correctly without architectural decisions.</role>

<quality_bar>Each task produces a working, tested increment. Tests are not optional or separate — they are part of every task. This mirrors how senior engineering teams at Stripe and Vercel work: every PR includes tests.</quality_bar>
</context>

<research>
{{RESEARCH_DOC}}
</research>

<prd_architecture>
{{PRD_ARCHITECTURE}}
</prd_architecture>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<instructions>
Create an implementation plan for a standard-complexity project (1-5 days total).

**Task requirements:**
- Each task produces a working, testable increment
- Each task includes specific tests to write (not "add tests later")
- Tasks are ordered by dependency (nothing depends on something that comes after it)
- Each task lists the specific files to create or modify
- Each task references relevant documentation URLs from the research document
- Each task has clear acceptance criteria that can be verified
- Tasks should be sized for one focused session — not too granular, not too large

**Phase structure:**
- **Phase 1: Foundation** (2-3 tasks) — project setup, core types/models, configuration, test infrastructure
- **Phase 2: Core** (3-5 tasks) — main functionality in dependency order, with tests
- **Phase 3: Integration & Polish** (2-3 tasks) — connecting components, error handling hardening, observability, final testing

**For each task, think about:**
- **Does an existing library/package handle this?** Before writing an implementation task for a well-known problem (PDF generation, email sending, auth, data parsing, file format handling, etc.), check if a package from the research document or a well-maintained library solves it. If yes, the task becomes "integrate [package]" not "build [feature]."
- What's the simplest version that proves this works?
- What errors could occur and how should they be handled?
- What tests prove this task is done correctly?
- What documentation should the developer reference while coding?
- What existing code patterns should be followed?

**Testing approach per task:**
- Unit tests for business logic, validation, and data transformation
- Integration tests for database operations, API endpoints, external service calls
- Every test should justify its existence by catching a specific failure mode

**Cursor workflow integration:**
Each task is designed to be executed with these Cursor commands in sequence:
1. `/start-task` — read task, check dependencies, implement
2. `/verify-task` — verify against acceptance criteria and docs
3. `/complete-task` — mark done, update docs, commit
</instructions>

<cross_reference_verification>
Before creating the task list, verify:
- Every PRD feature has at least one task
- Every architecture component has at least one task
- All documentation URLs come from RESEARCH.md
- Dependencies form a valid DAG (no cycles)
</cross_reference_verification>

<output_format>
# Implementation Tasks

## Summary
- **Total tasks**: [N]
- **Estimated total time**: [X] hours
- **Testing approach**: Unit tests with every task, integration tests in Phase 3
- **Cursor commands**: Use `/start-task`, `/verify-task`, `/complete-task` for each task

---

## Phase 1: Foundation

### Task 1: [Descriptive Name]
**Objective**: [One sentence — what this accomplishes]

**Files to create/modify**:
- `[path/file.ext]` — [what to create or change]
- `[path/file.ext]` — [what to create or change]

**Tests to write**:
- `tests/unit/test_[name].ext` — [what to test: specific functions, validation rules, edge cases]
- Test cases: [list 3-5 specific test cases with inputs and expected outputs]

**Dependencies**:
- Requires: None (or [task numbers])
- Blocks: [Tasks that depend on this]

**Documentation to reference**:
- [Specific doc section]: [URL from RESEARCH.md]

**Implementation notes**:
- [Key pattern to follow — reference architecture document]
- [Common mistake to avoid — from research document gotchas]

**Acceptance criteria**:
- [ ] [Specific, testable — e.g., "All type definitions compile without errors"]
- [ ] [Specific, testable]
- [ ] [Tests pass: `pytest tests/unit/test_[name].py` or equivalent]

---

[Continue for all Phase 1 tasks]

## Phase 2: Core Features

[Same format — every task includes "Tests to write" section]

## Phase 3: Integration & Polish

[Same format — includes integration tests, error handling verification, observability setup]

---

## Task Dependency Graph
```
Task 1 (None)
    ↓
Task 2 → Task 3
    ↓       ↓
Task 4 ← ─ ┘
    ↓
[Continue]
```

## Estimated Timeline

| Phase | Tasks | Estimated Time |
|-------|-------|----------------|
| Foundation | 1-[N] | [X] hours |
| Core | [N+1]-[M] | [X] hours |
| Integration | [M+1]-[End] | [X] hours |
| **Total** | | **[X] hours** |

## PRD Feature → Task Mapping

| PRD Feature | Tasks | Acceptance Criteria Covered |
|-------------|-------|-----------------------------|
| [Feature 1] | Task [A], [B] | [Which criteria] |
| [Feature 2] | Task [C], [D] | [Which criteria] |

## Verification Checklist
Before considering the project complete:
- [ ] All acceptance criteria across all tasks pass
- [ ] All unit tests pass (`[test command]`)
- [ ] All integration tests pass
- [ ] Error handling is present for all external operations and user inputs
- [ ] No hardcoded secrets or credentials
- [ ] Structured logging is in place for key operations
- [ ] Health check endpoint works (if applicable)
- [ ] Code follows patterns defined in architecture document
- [ ] Documentation reflects actual implementation

---

## Self-Verification

Before finalizing this task list:
- [ ] Every PRD feature maps to at least one task
- [ ] Every architecture component maps to at least one task
- [ ] Every task includes specific tests to write
- [ ] Dependencies form a valid DAG (no cycles)
- [ ] No task builds functionality that a well-maintained library/package already provides (checked against RESEARCH.md and package registries)
- [ ] Documentation URLs reference specific pages from RESEARCH.md
- [ ] Phase 1 includes test infrastructure setup
- [ ] Phase 3 includes integration testing and observability
- [ ] Total estimated time is realistic for the project complexity
</output_format>
