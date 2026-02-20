# start-task

Begin implementing a specific task from the project's task list.

## Process

1. **Read TASKS.md** — Find the specified task, understand its objective, dependencies, acceptance criteria, and required tests
2. **Check dependencies** — Verify all required prerequisite tasks are complete
3. **Load architecture context** — Read the relevant section of ARCHITECTURE.md (or PRD.md) for this task's component
4. **Reference documentation** — Check RESEARCH.md for the documentation URLs relevant to this task's technologies
5. **Check for existing packages** — Before implementing core functionality, search package registries (PyPI, npm, NuGet) for well-maintained libraries that solve this task's problem. If one exists and isn't already in RESEARCH.md, flag it: "EXISTING PACKAGE FOUND: [package] — consider using instead of custom implementation." Prefer packages already documented in RESEARCH.md.
6. **Review existing code** — Search the codebase for existing patterns to follow and code to reuse
7. **Implement** — Write the code following these rules:
   - Follow existing patterns in the codebase
   - Verify external APIs against @Docs before using them
   - Flag uncertainty with `// TODO: VERIFY — [concern]` rather than guessing
   - Handle errors explicitly — every external call, every file operation, every user input
   - Add structured logging for key operations (request handling, external calls, errors)
   - Add comments only for non-obvious logic
   - Use types/type hints on all function signatures
8. **Write tests** — Implement the tests specified in TASKS.md for this task:
   - Follow test patterns in tests/conftest and tests/factories
   - Test happy path, error cases, and edge cases as specified
   - Run the tests to confirm they pass

## Implementation Checklist

Before considering the task complete:
- [ ] All files listed in the task are created/modified
- [ ] Code follows patterns established in ARCHITECTURE.md
- [ ] External API usage verified against @Docs
- [ ] Error handling present for all failure points
- [ ] No hardcoded secrets or credentials
- [ ] Type hints/annotations on all function signatures
- [ ] Structured logging added for key operations
- [ ] Tests written as specified in TASKS.md
- [ ] All tests pass
- [ ] Acceptance criteria from the task description are met

## Output

After implementing, provide:
1. **Files changed**: List of files created or modified
2. **Tests written**: List of test functions and what they cover
3. **Key decisions**: Any non-obvious implementation choices and why
4. **Verification**: Status of each acceptance criterion
5. **Concerns**: Any uncertainties or items that need follow-up
6. **Next step**: Run `/verify-task` to perform comprehensive verification
