# sync-docs

Analyze the current codebase and compare it against planning documents. Identify drift, update documentation, and keep everything aligned.

## Process

### 1. Analyze Current Codebase
Read the current state of the codebase:
- Directory structure and file organization
- Implemented features and components
- Technology versions actually in use (from config files, lockfiles)
- Public interfaces and data models
- Test coverage and test organization

### 2. Compare Against Planning Documents

**docs/PRD.md:**
- Which features are implemented, partially implemented, or not started?
- Do acceptance criteria still match what was built?
- Are there features in the code that aren't in the PRD (scope creep)?
- Are there PRD features that were deliberately changed during implementation?

**docs/ARCHITECTURE.md:**
- Does the actual directory structure match the documented one?
- Do component interfaces match what's documented?
- Have data flows changed from the original design?
- Are there new components not in the architecture doc?
- Have external integrations changed?
- Does the error handling match the documented strategy?

**docs/TASKS.md:**
- Which tasks are complete? Mark them.
- Which tasks are in progress?
- Do remaining tasks still make sense given what's been built?
- Are there new tasks that need to be added?
- Has the dependency graph changed?

**docs/RESEARCH.md:**
- Are the actual dependency versions matching the documented ones?
- Were any technologies swapped during implementation?
- Are documentation URLs still valid and relevant?
- Have any dependencies released security patches since research was done?

**docs/TESTING_PLAN.md** (if exists):
- Does the actual test structure match the planned one?
- Are all planned test categories implemented?
- Does coverage meet the targets?

### 3. Check Dependency Versions
- Compare pinned versions in RESEARCH.md against actual versions in lockfiles
- Flag any discrepancies
- Check if any dependencies have released security patches since the project started

### 4. Determine Drift Type

For each deviation found, classify it:

| Type | Meaning | Action |
|------|---------|--------|
| **Code is correct, docs are stale** | Implementation improved on the plan | Update docs to match code |
| **Code went off-track** | Implementation deviated unintentionally | Flag for review — may need code fix |
| **Deliberate change** | Conscious decision during implementation | Update docs and note the reason |
| **Scope creep** | Features added without planning | Flag for discussion |
| **Version drift** | Dependencies updated or swapped | Update RESEARCH.md if intentional |

### 5. Update Documentation

Apply updates to bring docs in line with the actual implementation. For each update:
- State what changed and why
- Preserve the document's structure and format
- Add a note about when the update was made

### 6. Update README.md

Ensure README.md reflects:
- Current setup instructions (do they still work?)
- Accurate project description
- Current technology stack with correct versions
- Working usage examples
- Any new environment variables or configuration

## Output

Provide a sync report:

### Documentation Sync Report

**Files analyzed**: [list]
**Deviations found**: [count]

| Document | Section | Drift Type | Change Made |
|----------|---------|------------|-------------|
| [doc] | [section] | Stale/Off-track/Deliberate/Version | [description] |

**Dependency version check**:
| Dependency | Documented | Actual | Status |
|-----------|-----------|--------|--------|
| [name] | v[X.Y.Z] | v[A.B.C] | Match/Updated/Security patch available |

**Action items** (if any code issues were found):
- [ ] [Issue]: [What needs attention]
