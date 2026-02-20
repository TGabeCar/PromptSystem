# review-code

Perform a code review on the specified files or recent changes, checking against project standards, architecture, security rules, and best practices. This simulates the review a senior engineer at a top-tier company would perform before approving a PR.

## Review Scope

When asked to review code, check each file/change against these categories:

### 1. Architecture Compliance
- Does the code follow the patterns defined in ARCHITECTURE.md?
- Are components properly separated (business logic, I/O, presentation)?
- Do data flows follow the documented paths?
- Are new dependencies justified and documented?
- Is the code in the right location per the directory structure?

### 2. Code Quality
- Are names clear, descriptive, and consistent with the codebase?
- Are functions focused (single responsibility) and reasonably sized?
- Is there unnecessary complexity that could be simplified?
- Are there code duplications that should be extracted?
- Are comments adding value (explaining "why", not "what")?
- Is the code readable to someone unfamiliar with it?

### 3. Error Handling
- Are all external operations (API calls, database, file I/O) wrapped in error handling?
- Are errors specific (not catching all exceptions broadly)?
- Do error messages provide enough context for debugging?
- Are errors propagated correctly (not silently swallowed)?
- Is the error response format consistent with the project's error strategy?
- Are retry/fallback strategies implemented where specified in ARCHITECTURE.md?

### 4. Security
- Is user input validated before use?
- Are there potential injection points (SQL, XSS, command)?
- Are secrets handled correctly (not hardcoded, not logged)?
- Are authentication/authorization checks in place?
- Are there any data exposure risks?
- Is output properly escaped for its context?

### 5. Testing
- Are tests written for the changes?
- Do tests cover: happy path, error cases, edge cases?
- Are mocks appropriate (not over-mocking, not under-mocking)?
- Do test names describe what they verify?
- Do tests run fast (unit tests < 100ms each)?

### 6. Observability
- Are key operations logged with structured logging?
- Do logs include correlation IDs for request tracing?
- Is sensitive data excluded from logs?
- Are performance-relevant operations timed?

### 7. Type Safety
- Are all function signatures fully typed?
- Are there any `any` types or missing type hints?
- Are generic types used correctly?
- Are type assertions justified with comments?

### 8. Performance
- Are there obvious N+1 query issues?
- Are expensive operations cached or debounced?
- Are large datasets handled efficiently (streaming, pagination)?
- Are there blocking operations in async contexts?

## Output Format

## Code Review Results

### Summary
- **Files reviewed**: [count]
- **Issues found**: [count by severity]
- **Overall assessment**: [Approve / Request Changes / Needs Discussion]

### Critical Issues (must fix)
- **[file:line]**: [Issue description] — [Why it's critical] — [Suggested fix]

### Recommendations (should fix)
- **[file:line]**: [Issue description] — [Why it matters] — [Suggested fix]

### Suggestions (nice to have)
- **[file:line]**: [Suggestion] — [Why it would improve the code]

### Positive Notes
- [What's done well — call out good patterns, clean code, thorough error handling]

### Checklist
- [ ] Architecture compliance verified
- [ ] Security checks passed
- [ ] Error handling is comprehensive
- [ ] Tests are present and passing
- [ ] Observability is in place
- [ ] Type safety is maintained
- [ ] No performance concerns
