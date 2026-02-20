# debug

Systematically diagnose and fix a bug or unexpected behavior. Follow a structured approach instead of guessing — this prevents the common AI agent failure mode of trying random things that compound the problem.

## Debugging Process

### Step 1: Understand the Problem
Before changing any code:
- **What is the expected behavior?** (Reference PRD.md or TASKS.md for the correct specification)
- **What is the actual behavior?** (Exact error message, unexpected output, or incorrect state)
- **When does it happen?** (Always? Sometimes? Under specific conditions?)
- **What changed recently?** (New code, dependency update, configuration change?)

### Step 2: Gather Evidence
Collect concrete evidence before forming hypotheses:
- Read the exact error message and stack trace
- Check application logs (search by correlation ID if available)
- Check the relevant test results — are tests failing? Which ones?
- Reproduce the issue with a minimal test case if possible

### Step 3: Form a Hypothesis
Based on the evidence:
- **Most likely cause**: [What the evidence points to]
- **Supporting evidence**: [What specifically suggests this cause]
- **What to check**: [How to confirm or disprove this hypothesis]

Do NOT start changing code yet. Verify the hypothesis first.

### Step 4: Verify the Hypothesis
Test the hypothesis without modifying production code:
- Add a focused test case that reproduces the bug
- Add temporary debug logging (clearly marked for removal)
- Check documentation: does the API/library actually work the way we assumed? (Verify against @Docs)
- Check version compatibility: is this a known issue with the specific version we're using?

### Step 5: Implement the Fix
Once the root cause is confirmed:
- Make the minimal change that fixes the issue
- Don't refactor unrelated code in the same fix
- Ensure the fix addresses the root cause, not just the symptom
- Verify the fix doesn't break existing tests

### Step 6: Verify the Fix
- The reproduction test case now passes
- All existing tests still pass
- The original reported behavior is fixed
- No new issues introduced (check related functionality)
- Remove any temporary debug logging

### Step 7: Document the Fix
- Explain the root cause (not just "changed X to Y", but WHY)
- Note if documentation needs updating
- Suggest a commit message

## Anti-Patterns to Avoid

- **Shotgun debugging**: Changing multiple things at once hoping something works. Change ONE thing, verify, then proceed.
- **Hypothesizing without evidence**: "Maybe it's X" without checking. Always look at the actual error first.
- **Fixing symptoms**: Adding a try/catch around a crash instead of fixing why it crashes.
- **Scope creep**: Refactoring or improving unrelated code while debugging. Fix the bug, commit, then improve separately.
- **Ignoring tests**: If tests pass but the bug exists, the tests are incomplete. Add the missing test first.
- **Overwriting state**: Adding workarounds that mask the underlying issue.

## Output Format

## Debug Report

### Problem
- **Expected**: [behavior]
- **Actual**: [behavior]
- **Reproducible**: [Always / Sometimes / Specific conditions]

### Evidence Gathered
- **Error**: [exact message and stack trace]
- **Logs**: [relevant log entries]
- **Related tests**: [which tests pass/fail]

### Root Cause
[Explanation of WHY the bug occurs — not just what's wrong, but the chain of events]

### Fix Applied
- **File(s) changed**: [list]
- **Change description**: [what was changed and why this fixes the root cause]
- **Minimal change**: [confirmation this is the smallest fix that addresses the issue]

### Verification
- [ ] Reproduction test case added and passes
- [ ] All existing tests still pass
- [ ] Original behavior is corrected
- [ ] No regressions in related functionality
- [ ] Temporary debug logging removed

### Commit Message
```
fix(scope): [description of what was fixed]

Root cause: [brief explanation]
```

### Follow-up
- [Any documentation that needs updating]
- [Any related issues that should be investigated]
- [Any tests that should be added beyond the reproduction case]
