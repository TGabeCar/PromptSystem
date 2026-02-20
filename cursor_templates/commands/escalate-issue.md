# escalate-issue

Generate a comprehensive issue brief for handoff to a research-focused AI (Poppy/Claude, Grok, etc.) when stuck on a complex problem. The brief must be self-contained — the receiving model should need nothing else to start helping.

## Critical: What Makes a Good Escalation

The #1 reason escalation fails is that the receiving model suggests things already tried. This brief format prevents that by documenting WHAT was tried and WHY it failed.

## Information to Gather

Collect and organize the following from the current codebase and conversation:

### Problem Statement
- What specific behavior is expected?
- What specific behavior is occurring instead?
- When did it start? What changed?
- Is it reproducible? Under what conditions?

### Error Evidence
- Exact error messages, stack traces, console output
- Screenshots of unexpected behavior (if visual)
- Relevant log entries (with correlation IDs if available)

### Reproduction Steps
1. [Step-by-step instructions to reproduce the issue]
2. [Include: environment, input data, sequence of actions]
3. [Note: is it consistent or intermittent?]

### What Has Been Tried (CRITICAL SECTION)
For EACH approach already attempted, document:
- **What**: The specific approach or fix tried
- **Why**: The reasoning behind trying this approach
- **Result**: The exact outcome (new error, partial fix, no change, made it worse)
- **Why it failed**: Your best understanding of WHY this approach didn't work

This section prevents the receiving model from wasting time suggesting things you've already done.

### Relevant Code
- Only the specific files and functions involved — not the whole codebase
- Include file paths as comments in code snippets
- Highlight the lines where the problem manifests

### Constraints
- What can't change (external API behavior, architecture decisions, version requirements)
- What has been verified as working correctly (don't investigate these)

### Documentation References
- Official documentation pages for the technologies involved
- Specific doc sections that seem relevant to the problem
- Any GitHub issues or Stack Overflow threads found during investigation

## Output Format

Generate this markdown brief:

```markdown
# Issue Brief: [Descriptive Title]

## Problem Summary
[2-3 sentences: what should work but doesn't, being very specific about expected vs actual behavior]

## Error Evidence
```
[Exact error message or unexpected behavior — code block format]
```

## Reproduction Steps
1. [Step]
2. [Step]
3. [Observe: specific unexpected behavior]

## Environment
- **Framework**: [name and exact version]
- **Runtime**: [name and version]
- **Key Dependencies**: [relevant packages with versions]
- **OS**: [if relevant]

## Relevant Code

### [path/to/file.ext]
```[language]
[Minimal code showing the problem — annotate the problematic lines]
```

## What Has Been Tried

| # | Approach | Reasoning | Result | Why It Failed |
|---|----------|-----------|--------|---------------|
| 1 | [approach] | [why we tried this] | [exact result] | [why it didn't work] |
| 2 | [approach] | [why we tried this] | [exact result] | [why it didn't work] |
| 3 | [approach] | [why we tried this] | [exact result] | [why it didn't work] |

## What IS Working
- [Parts of the system confirmed working correctly]

## Constraints
- [What can't change and why]
- [External dependencies that are fixed]

## Documentation References
- [URL] — [what it says about this problem area]
- [URL] — [relevant section]

## Current Hypothesis
[Best guess at the root cause based on evidence gathered so far]

## Specific Questions
1. [Targeted question about the root cause]
2. [Question about alternative approaches not yet tried]
3. [Question about documentation accuracy or version-specific behavior]
```

## Instructions for the Receiving Model

Include this at the end of the brief:

---

**INSTRUCTIONS FOR RECEIVING MODEL:**

1. Do NOT guess. Research the specific error/behavior against the documentation links provided above.
2. Do NOT suggest approaches that have already been tried (see "What Has Been Tried" table above). If you believe a previously tried approach could work with modifications, explain SPECIFICALLY what would be different.
3. If you cannot find a documented solution, say so explicitly. Do not make up APIs or methods.
4. State your confidence level: HIGH (documented solution exists), MEDIUM (likely solution based on similar issues), LOW (speculative — needs verification).
5. For each suggestion, provide: the specific change, why it should work (with documentation reference), and how to verify it worked.
6. If the issue might be a bug in the library/framework, provide the GitHub issues search URL and any relevant issues found.

---

## After Generating

Copy the entire brief and paste into a new conversation with the research-focused AI. Their response can then be brought back to Cursor for implementation.
