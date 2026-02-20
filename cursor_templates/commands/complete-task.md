# complete-task

Finalize the current task — verify, document, and prepare for the next one.

## Process

### 1. Run Verification
Execute the full `/verify-task` checklist if not already done. If any issues are found, fix them before proceeding.

### 2. Confirm Tests Pass
Run the full test suite:
- All unit tests pass
- All integration tests pass (if applicable to this task)
- No regressions introduced in previously passing tests

### 3. Update TASKS.md
- Mark the current task as complete: change `[ ]` to `[x]` in the status
- Add a completion note with the date
- Note any deviations from the original task description
- If tests were added beyond what was specified, note them

### 4. Check Documentation Drift
Compare the implementation against these documents:
- **ARCHITECTURE.md**: Does the code match the documented structure? If not, update the doc.
- **PRD.md**: Are acceptance criteria met as documented? Note any changes.
- **RESEARCH.md**: Were all technologies used as planned? Any version changes?

Update documentation where the implementation is correct but docs have drifted.

### 5. Suggest Commit Message
Generate a commit message in conventional commits format:

```
[type](scope): [description]

- [Key change 1]
- [Key change 2]
- Tests: [what was tested]
- Verified against: [doc references]
```

Types: feat, fix, refactor, docs, test, chore
Scope: the component or feature area

### 6. Identify Next Task
Based on TASKS.md dependency graph:
- What task(s) are now unblocked?
- Which should be done next and why?
- Are there any blockers for the next task?

## Output

1. **Verification**: Summary of verify-task results (pass/fail with details)
2. **Test results**: All tests passing, count of tests added
3. **TASKS.md update**: The specific change made
4. **Documentation updates**: What was updated and why (if anything)
5. **Commit message**: Ready-to-use conventional commit
6. **Next task**: Recommendation with reasoning — "Start with `/start-task [task number]`"
