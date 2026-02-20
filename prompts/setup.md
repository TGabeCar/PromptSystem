---
target_tool: "Poppy (Opus 4.6) or Cursor"
stores_as: "SETUP"
description: "Project setup prompt — generates configuration files, directory structure, CI/CD pipeline, pre-commit hooks, skeleton files, and Cursor rules with pinned versions."
---

<context>
<role>You are a senior developer setting up a project for implementation to flagship engineering standards. Generate complete, ready-to-use configuration files — not templates or placeholders. Every version number must be pinned. Every configuration must be production-appropriate. The setup should include CI/CD from the first commit, test infrastructure, and observability foundations. This is the last planning step before the developer opens Cursor and starts building.</role>

<quality_bar>
The project setup should mirror how top engineering teams start projects:
- CI/CD pipeline running on first commit (lint, typecheck, test)
- Pre-commit hooks to catch issues before they're committed
- Test infrastructure ready to write the first test
- Structured logging configured
- Configuration validated at startup
- Secrets management via environment variables with documented .env.example
</quality_bar>

<user_context>
The developer uses Cursor IDE with @Docs references. Every documentation URL from the research document will be added to Cursor's Docs feature for inline verification during coding. The Cursor rules you generate will be active for every file the developer works on.
</user_context>
</context>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<research>
{{RESEARCH_DOC}}
</research>

<planning>
The following planning documents have been created for this project. Reference them for architecture decisions, feature requirements, and task structure.

PRD / Architecture (whichever is available):
{{PRD_ARCHITECTURE}}
{{PRD}}
{{ARCHITECTURE}}

Tasks:
{{TASKS}}
</planning>

<instructions>
Generate everything needed to start coding immediately with production-grade foundations:

**1. Configuration Files**
- Package manager config with ALL dependencies pinned to exact versions from the research document
- Runtime/language configuration (tsconfig.json, pyproject.toml, .csproj, etc.)
- Environment variable template (.env.example) with every required variable listed and documented
- Linter/formatter configuration matching the project's code style decisions
- Git ignore file appropriate for the tech stack

**2. Directory Structure**
- Create the complete directory tree from the architecture document
- Include skeleton files for Phase 1 tasks (types, interfaces, main entry point)
- Each skeleton file should have: imports, type definitions, function signatures with docstrings, and TODO comments referencing the task number
- Include test directory structure with shared fixtures/helpers

**3. CI/CD Pipeline**
- GitHub Actions workflow (or equivalent for the stack) with fail-fast stages:
  - Stage 1: Lint + Type Check (< 1 min)
  - Stage 2: Unit Tests with coverage (< 2 min)
  - Stage 3: Integration Tests (< 3 min)
  - Stage 4: Security audit (dependency vulnerability check)
- Pipeline should run on: push to main, pull requests
- Cache dependencies for speed

**4. Pre-commit Hooks**
- Linting and formatting on staged files
- Type checking
- Secret detection (prevent committing API keys, passwords, tokens)
- Commit message format validation (conventional commits)

**5. Test Infrastructure**
- Test framework configuration
- Shared fixtures/helpers file
- Test data factory pattern
- Coverage configuration with thresholds

**6. Observability Foundations**
- Structured logging configuration (JSON format with correlation ID support)
- Health check endpoint skeleton (if applicable)

**7. Cursor Configuration**
Generate a project-specific `.cursor/rules/general.mdc` that includes:
- Project name and stack summary (with exact versions)
- Documentation URLs to reference with @Docs
- Core coding principles from the architecture document
- What NOT to do (anti-patterns specific to this project)
- Verification requirements (check @Docs before using external APIs)
- Testing requirements (write tests with every implementation task)

**8. Setup Commands**
- Step-by-step commands to initialize, install, configure, and verify the project
- Include verification steps (e.g., "run this command — you should see this output")
- Include: "run the CI pipeline locally to verify everything works"

**9. Post-Setup Checklist**
- Everything to verify before starting Task 1
</instructions>

<cross_reference_verification>
Before generating setup files:
- All dependency versions must match RESEARCH.md exactly
- Directory structure must match ARCHITECTURE.md
- .env.example must cover all secrets/config referenced in the architecture
- Test infrastructure must use the tools specified in TESTING_PLAN.md (if available)
</cross_reference_verification>

<output_format>
# Project Setup

## Configuration Files

### [Primary config file — e.g., pyproject.toml / package.json]
```[format]
[Complete configuration with pinned versions from RESEARCH.md]
```

### [Secondary config — e.g., tsconfig.json / .editorconfig]
```[format]
[Complete configuration]
```

### .env.example
```
# [Project Name] Environment Variables
# Copy to .env and fill in values
# NEVER commit .env to version control

# [Category — e.g., "Database"]
VARIABLE_NAME=        # [Description — what this is, where to get it]
VARIABLE_NAME=        # [Description]

# [Category — e.g., "External APIs"]
VARIABLE_NAME=        # [Description]
```

### .gitignore
```
[Comprehensive gitignore for the tech stack]
.env
*.pyc
__pycache__/
node_modules/
.coverage
htmlcov/
dist/
[Continue for stack-specific patterns]
```

### [Linter/Formatter Config — e.g., ruff.toml / .eslintrc]
```[format]
[Complete linter/formatter configuration]
```

---

## CI/CD Pipeline

### .github/workflows/ci.yml
```yaml
[Complete GitHub Actions workflow with:
  - Fail-fast stages: lint → typecheck → unit tests → integration tests → security audit
  - Dependency caching
  - Coverage reporting
  - Triggered on: push to main, pull requests]
```

---

## Pre-commit Configuration

### [Pre-commit config — e.g., .pre-commit-config.yaml / husky config]
```[format]
[Complete pre-commit configuration with:
  - Linting/formatting
  - Type checking (optional — may be slow)
  - Secret detection
  - Conventional commit message validation]
```

---

## Directory Structure

```
project-name/
├── [Complete tree matching architecture document]
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── conftest.[ext]
│   └── factories.[ext]
├── .github/workflows/ci.yml
├── .env.example
├── [config files]
└── README.md
```

---

## Skeleton Files

### [path/file.ext]
```[language]
"""[Description] — Task [N]
@see [Official doc URL for this pattern]
"""

[imports]

[type/class definitions with full signatures]

# TODO: Implement — Task [N]: [Task name]
[function signatures with docstrings but pass/NotImplementedError bodies]
```

[Continue for each Phase 1 file]

### tests/conftest.[ext]
```[language]
"""Shared test fixtures and helpers."""

[Test fixtures for: database connection, authenticated client, mock external services, test data factories]
```

---

## Observability Setup

### [Logging config file]
```[language]
[Structured logging configuration with:
  - JSON format
  - Correlation ID support
  - Log levels: DEBUG (dev), INFO (production)
  - Redaction of sensitive fields]
```

### [Health check endpoint — if applicable]
```[language]
[Health check that returns: status, version, dependency connectivity]
```

---

## Cursor Rules

### .cursor/rules/general.mdc
```yaml
---
description: "Core project rules — always active"
alwaysApply: true
---

# Project: [Name]
# Stack: [Technologies with exact versions from RESEARCH.md]

## Documentation Sources
Reference these with @Docs:
- [Technology]: [URL]
- [Technology]: [URL]

## Architecture
[Key architectural decisions and patterns from ARCHITECTURE.md]

## Code Standards
[Project-specific standards]

## Testing Requirements
- Write tests alongside every implementation (not after)
- Follow test patterns in tests/conftest.[ext]
- Run tests before committing: [command]

## Verification Requirements
- Before using any external API: verify against @Docs
- Flag uncertainty with: `// TODO: VERIFY — [concern]`
- No hallucinated methods — if unsure, check docs first

## What NOT To Do
[Anti-patterns specific to this project — from architecture doc and research gotchas]
```

---

## Setup Commands

```bash
# 1. Clone and enter project directory
[commands]

# 2. Create virtual environment / install runtime
[commands]

# 3. Install dependencies
[commands]

# 4. Set up environment
cp .env.example .env
# Edit .env with your values

# 5. Set up pre-commit hooks
[commands]

# 6. Verify installation
[command — expected output: ...]

# 7. Run the CI pipeline locally
[lint command — expected: no errors]
[typecheck command — expected: no errors]
[test command — expected: X tests pass]

# 8. Verify health check (if applicable)
[command — expected output: ...]
```

---

## Post-Setup Checklist
- [ ] All dependencies installed without errors
- [ ] Configuration files created and valid
- [ ] .env file created from .env.example with values filled in
- [ ] Pre-commit hooks installed and working
- [ ] Linter passes on all files
- [ ] Type checker passes
- [ ] Test infrastructure works (can run empty test suite)
- [ ] CI pipeline config is valid (validated with act or similar)
- [ ] .cursor/rules/ directory populated
- [ ] Documentation URLs added to Cursor (Settings → Features → Docs)
- [ ] Health check endpoint responds (if applicable)
- [ ] Ready to begin Task 1

## Documentation URLs for Cursor @Docs
Add these in Cursor Settings → Features → Docs:
| Name | URL |
|------|-----|
| [Technology] | [Docs URL from RESEARCH.md] |
| [Continue for all technologies] |

---

## Self-Verification

Before finalizing this setup:
- [ ] All dependency versions match RESEARCH.md exactly
- [ ] Directory structure matches ARCHITECTURE.md
- [ ] .env.example covers all secrets/config from the architecture
- [ ] CI/CD pipeline includes: lint, typecheck, unit tests, integration tests, security audit
- [ ] Pre-commit hooks include: formatting, linting, secret detection
- [ ] Test infrastructure is ready for the first test
- [ ] Cursor rules reference the correct documentation URLs
- [ ] Setup commands work in order and include verification steps
</output_format>
