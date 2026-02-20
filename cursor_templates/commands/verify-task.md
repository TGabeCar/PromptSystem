# verify-task

Perform a comprehensive verification of the most recently implemented task. This is a quality gate — do not skip any section.

## Verification Checklist

### 1. API Accuracy
Review every external API, method, or function call used in the implementation:
- For each external method: state "According to @Docs [library], `method(params)` exists with signature: [signature]"
- If you cannot verify a method against official documentation: "UNVERIFIED: `method()` — could not confirm in @Docs"
- Check that all method parameters match the documented signatures
- Verify return types match what the code expects

### 2. Type Safety
- Are there any `any` types (TypeScript), missing type hints (Python), or loose typing that could hide bugs?
- Are there unsafe type assertions or casts?
- Do all function signatures have complete type annotations?
- Are generic types used correctly?

### 3. Error Handling
- For each external operation (API call, database query, file I/O): what happens if it fails?
- Are errors caught at appropriate levels (not too broad, not too narrow)?
- Do error messages provide enough context for debugging (operation, input, correlation ID)?
- Are errors propagated correctly (not silently swallowed)?
- Do user-facing errors hide internal implementation details?
- Is the error response format consistent with ARCHITECTURE.md error handling strategy?

### 4. Edge Cases
Test mentally with these inputs:
- **Empty input**: Empty strings, empty arrays, zero values
- **Null/undefined/None**: Missing optional parameters
- **Very large input**: Maximum realistic data sizes
- **Special characters**: Unicode, SQL metacharacters, HTML tags, path separators
- **Concurrent access**: If applicable — what happens with simultaneous operations?
- **Boundary values**: First item, last item, max int, date boundaries

### 5. Architecture Compliance
- Does the implementation match the patterns defined in ARCHITECTURE.md?
- Are components properly separated (business logic, I/O, presentation)?
- Do data flows follow the documented paths?
- Are dependencies in the correct direction?
- Is this component's public interface consistent with the architecture?

### 6. Security
- Is all user input validated before use?
- Are there any injection vulnerabilities (SQL, XSS, command injection)?
- Are secrets handled correctly (env vars, not hardcoded)?
- Are authentication/authorization checks in place (if applicable)?
- Is sensitive data handled appropriately (not logged, properly encrypted)?

### 7. Test Coverage
- Are tests written for this task as specified in TASKS.md?
- Do all tests pass?
- Do tests cover:
  - Happy path (basic functionality works)?
  - Error cases (failures are handled correctly)?
  - Edge cases (boundary values, empty input, special characters)?
- Are external dependencies properly mocked in unit tests?
- Do test names clearly describe what they verify?

### 8. Observability
- Are key operations logged with structured logging?
- Do log messages include correlation IDs where applicable?
- Are errors logged with sufficient context (operation, input, stack trace)?
- Is sensitive data excluded from logs (passwords, tokens, PII)?

## Output Format

## Verification Results

### Passed
- [Item]: [Evidence — e.g., "Confirmed `requests.get()` signature in @Docs requests"]

### Concerns
- [Item]: [Issue description and recommended fix]

### Fixes Applied
[If issues were found and corrected, describe each fix]

### Test Results
- Tests run: [count]
- Tests passed: [count]
- Tests failed: [count — with details]

### Acceptance Criteria Status
- [ ] [Criterion from TASKS.md]: [PASS/FAIL — evidence]

### Next Step
Run `/complete-task` to finalize, update documentation, and commit.
