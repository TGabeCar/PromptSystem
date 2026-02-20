# explain

Explain how the specified code, feature, or component works. The goal is to help the developer understand the implementation — not just what it does, but WHY it was built this way.

## What to Explain

When asked to explain code or a feature:

### 1. What It Does
- High-level purpose in plain language
- What problem it solves
- Where it fits in the overall system (reference ARCHITECTURE.md)

### 2. How It Works
- Walk through the implementation step by step
- Explain the flow of data through the component
- Highlight key functions/methods and their roles
- Explain important data structures and why they were chosen
- Note any non-obvious logic and why it exists

### 3. Why It Was Built This Way
- Reference architectural decisions from ARCHITECTURE.md and ADR.md
- Explain the design pattern used and why it fits
- Note alternatives that were considered (reference ADRs or RESEARCH.md if available)
- Explain trade-offs that were made
- Point out where official documentation influenced the approach (reference @Docs)

### 4. Key Dependencies
- What external libraries or services this code depends on
- How those dependencies are used (reference RESEARCH.md for API details)
- What happens if a dependency is unavailable (resilience strategy)

### 5. Error Handling & Resilience
- What can go wrong
- How errors are handled at each level
- What the user sees when something fails
- Retry/fallback strategies
- How to debug common issues (what logs to check, what correlation IDs to search)

### 6. Testing
- How this code is tested (reference test files)
- What edge cases are covered
- How to run the relevant tests

### 7. How to Modify It
- If you needed to change this code, what would you need to understand?
- What other components would be affected?
- What tests would need to be updated?
- What documentation would need to change?

## Explanation Style

- Use plain language first, then show code
- Start with the big picture, then zoom into details
- Use analogies when explaining complex concepts
- Reference the project's planning documents to explain the "why"
- If the code follows a well-known pattern, name it and explain how it's applied here
- Point out particularly clever or non-obvious techniques and explain them clearly
- Be honest about complexity — if something is complicated, explain why it needs to be

## Context Sources

Reference these documents to provide context:
- **docs/ARCHITECTURE.md** — For why the component exists and how it fits
- **docs/PRD.md** — For what user need this code serves
- **docs/RESEARCH.md** — For why specific technologies or APIs were chosen
- **docs/TASKS.md** — For what task created this code
- **docs/ADR.md** — For why specific decisions were made
- **.cursor/rules/** — For coding standards this code follows
