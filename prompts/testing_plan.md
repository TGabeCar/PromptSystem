---
target_tool: "Poppy (Opus 4.6)"
stores_as: "TESTING_PLAN"
description: "Comprehensive testing plan for Tier 3 projects — unit, integration, acceptance, security, accessibility, contract, and performance testing with CI/CD integration."
---

<context>
<role>You are a senior QA architect designing a comprehensive testing strategy for a complex project. Your plan must be practical — focused on high-value tests that catch real bugs, not theoretical coverage metrics. Every test should justify its existence by protecting against a specific category of failure. The testing plan should produce the same level of confidence as what Stripe, Linear, or Vercel maintain in their production systems.</role>

<quality_bar>
The test suite should:
- Catch regressions before they reach production
- Run fast enough that developers actually run tests (unit tests < 30s, full suite < 5min)
- Cover all PRD acceptance criteria with traceable tests
- Include security testing that catches OWASP Top 10 vulnerabilities
- Integrate into CI/CD with fail-fast ordering (lint → typecheck → unit → integration → e2e)
</quality_bar>
</context>

<prd>
{{PRD}}
</prd>

<architecture>
{{ARCHITECTURE}}
</architecture>

<tasks>
{{TASKS}}
</tasks>

<instructions>
Design a testing strategy for this complex project. The plan should be implementable by a developer using AI-assisted coding (Cursor IDE), so be specific about what to test and how.

**Testing layers (follow the testing pyramid — 70/20/10):**

1. **Unit Tests (70%)** — Test individual functions/methods in isolation
   - Focus on: business logic, data transformations, validation rules, error handling
   - Mock: external services, databases, file systems
   - Cover: happy path, edge cases (empty, null, max, special chars), error cases
   - Speed target: entire unit suite runs in < 30 seconds

2. **Integration Tests (20%)** — Test component boundaries
   - Focus on: database operations, API endpoints, service interactions
   - Use: test databases, mock external APIs, test fixtures
   - Cover: data flow between components, error propagation, transaction handling

3. **End-to-End / Acceptance Tests (10%)** — Test against PRD criteria
   - Map each PRD acceptance criterion to a specific test
   - Test complete user workflows, not individual operations
   - These are the "did we build the right thing?" tests

4. **Security Tests** — Must-have for all projects, expanded for customer-facing
   - Input validation: SQL injection, XSS, path traversal, command injection
   - Authentication: invalid tokens, expired sessions, missing credentials
   - Authorization: privilege escalation, cross-user data access, role boundary testing
   - Rate limiting: verify limits are enforced
   - Supply chain: dependency audit for known vulnerabilities

5. **Contract Tests** (if applicable — APIs consumed by other services)
   - Verify API response shapes match documented contracts
   - Catch breaking changes before they affect consumers
   - Test backward compatibility for versioned endpoints

6. **Accessibility Tests** (if applicable — UI components)
   - Keyboard navigation for all interactive elements
   - Screen reader compatibility
   - Color contrast ratios meet WCAG requirements
   - Focus management and ARIA attributes

7. **Performance Tests** (if relevant based on PRD NFRs)
   - Response time for key operations under expected load
   - Resource usage (memory, CPU) under sustained operation
   - Identify bottlenecks before they hit production

**For each test category, specify:**
- What testing framework/library to use (from the research document)
- Directory structure for test files
- Naming conventions
- Setup/teardown patterns
- What to mock and how
- CI/CD stage where these tests run
</instructions>

<output_format>
# Testing Plan

## Testing Strategy Overview
[2-3 paragraphs: overall approach, priorities, what we're optimizing for, how this aligns with the testing pyramid]

## Test Infrastructure

### Framework & Tools
| Tool | Purpose | Version | Docs | CI Stage |
|------|---------|---------|------|----------|
| [Framework] | Unit/Integration tests | v[X.Y] | [URL] | All |
| [Mock library] | Mocking external deps | v[X.Y] | [URL] | Unit/Integration |
| [Coverage tool] | Coverage reporting | v[X.Y] | [URL] | All |
| [Security scanner] | Dependency audit | v[X.Y] | [URL] | CI |
| [Linter] | Static analysis | v[X.Y] | [URL] | Pre-commit + CI |

### Directory Structure
```
tests/
├── unit/
│   ├── [test_component.ext]
│   └── ...
├── integration/
│   ├── [test_flow.ext]
│   └── ...
├── acceptance/
│   └── ...
├── security/
│   └── ...
├── conftest.[ext]     # Shared fixtures
├── factories.[ext]    # Test data factories
└── helpers.[ext]      # Test utilities
```

### Shared Fixtures & Helpers
[Key fixtures that multiple tests need — database connections, mock services, test data factories, authenticated client helpers]

### Test Data Strategy
- [How test data is created: factories, fixtures, seed files]
- [How test data is cleaned up: transaction rollback, database reset, etc.]
- [Sensitive data handling: never use real PII in tests]

---

## Unit Tests

### [Component Name]
**File**: `tests/unit/test_[component].ext`
**Speed target**: < [X]ms for all tests in this file

| Test Name | What It Tests | Input | Expected Output | Failure Mode Caught |
|-----------|--------------|-------|-----------------|---------------------|
| test_[name] | [Specific behavior] | [Input] | [Expected result] | [What bug this catches] |
| test_[name]_empty | [Edge case] | Empty/null | [Expected handling] | [Failure mode] |
| test_[name]_invalid | [Error case] | [Bad input] | [Expected error] | [Failure mode] |
| test_[name]_max | [Boundary] | [Max size/value] | [Expected behavior] | [Failure mode] |

[Continue for each component with business logic]

---

## Integration Tests

### [Flow/Boundary Name]
**File**: `tests/integration/test_[flow].ext`
**Setup**: [What needs to be running — test DB, mock server, etc.]

| Test Name | What It Tests | Components Involved | Failure Mode Caught |
|-----------|--------------|---------------------|---------------------|
| test_[flow]_happy_path | [End-to-end flow] | [A → B → C] | [Verifies full flow works] |
| test_[flow]_db_error | [Database failure] | [A → B → DB] | [Error propagation] |
| test_[flow]_external_timeout | [Timeout handling] | [A → External] | [Resilience/retry logic] |
| test_[flow]_concurrent | [Race conditions] | [A + A → B] | [Data integrity] |

[Continue for each integration boundary]

---

## Acceptance Tests (PRD Mapping)

| PRD Feature | PRD Criterion | Test Name | Test Description | File |
|-------------|---------------|-----------|-----------------|------|
| [Feature 1] | [Criterion 1] | test_[name] | [How to verify] | [path] |
| [Feature 1] | [Criterion 2] | test_[name] | [How to verify] | [path] |
| [Continue for ALL PRD acceptance criteria — 100% coverage required] |

---

## Security Tests

### Input Validation
| Attack Vector | Test | Input | Expected Result | OWASP Ref |
|--------------|------|-------|-----------------|-----------|
| SQL Injection | test_sql_injection_[field] | `'; DROP TABLE--` | Rejected/parameterized | A03:2021 |
| XSS (Reflected) | test_xss_reflected_[field] | `<script>alert(1)</script>` | Escaped in output | A07:2025 |
| XSS (Stored) | test_xss_stored_[field] | `<img onerror=alert(1)>` | Sanitized before storage | A07:2025 |
| Path Traversal | test_path_traversal_[field] | `../../etc/passwd` | Rejected | A01:2021 |
| Command Injection | test_cmd_injection_[field] | `; rm -rf /` | Rejected | A03:2021 |
| Oversized Input | test_oversized_[field] | [10x max size] | Rejected with 413/400 | A05:2021 |

### Authentication
| Scenario | Test | Expected Result |
|----------|------|-----------------|
| Invalid token | test_auth_invalid_token | 401 Unauthorized |
| Expired token | test_auth_expired_token | 401 + clear error message |
| Missing auth | test_auth_missing | 401 |
| Malformed auth header | test_auth_malformed | 401 |

### Authorization
| Scenario | Test | Expected Result |
|----------|------|-----------------|
| [Role A] accessing [Role B resource] | test_authz_[scenario] | 403 Forbidden |
| Direct object reference manipulation | test_authz_idor | 403 or 404 |
| [Continue for each role boundary] |

### Supply Chain Security
| Check | Tool | When | Expected |
|-------|------|------|----------|
| Known vulnerabilities | [audit tool] | Every CI run | Zero critical/high CVEs |
| License compliance | [license checker] | Weekly / pre-release | No GPL in proprietary code |
| Lockfile integrity | [lockfile check] | Every CI run | Lockfile matches manifest |

---

## Contract Tests (if applicable)

### [API Endpoint]
| Contract | Test | Consumer | Expected |
|----------|------|----------|----------|
| Response shape | test_contract_[endpoint]_shape | [Consumer] | Matches documented schema |
| Required fields | test_contract_[endpoint]_required | [Consumer] | All required fields present |
| Backward compatibility | test_contract_[endpoint]_v1 | [Consumer] | Old format still works |

---

## Accessibility Tests (if applicable)

| Requirement | Test | Tool | WCAG Ref |
|-------------|------|------|----------|
| Keyboard navigation | test_a11y_keyboard_[component] | [Tool] | 2.1.1 |
| Screen reader labels | test_a11y_labels_[component] | [Tool] | 1.1.1 |
| Color contrast | test_a11y_contrast | [Tool] | 1.4.3 |
| Focus management | test_a11y_focus_[flow] | [Tool] | 2.4.3 |

---

## Performance Tests (if applicable)

| Operation | Target (from PRD NFRs) | Test Approach | Tool |
|-----------|------------------------|--------------|------|
| [Key operation] | < [X]ms p95 | [Load test with N concurrent] | [Tool] |
| [Bulk operation] | [X] records/sec | [Benchmark] | [Tool] |
| [Startup time] | < [X]s | [Cold start measurement] | [Tool] |

---

## Test Execution

### Running Tests
```bash
# All unit tests (fast — should complete in < 30s)
[command]

# All integration tests
[command]

# Specific test file
[command]

# With coverage report
[command]

# Security audit
[command]
```

### CI/CD Integration (fail-fast ordering)
```
Stage 1 (< 1 min): Lint + Type Check + Security Audit
    ↓ (fail = stop)
Stage 2 (< 2 min): Unit Tests with Coverage
    ↓ (fail = stop)
Stage 3 (< 3 min): Integration Tests
    ↓ (fail = stop)
Stage 4 (< 5 min): Acceptance + E2E Tests
    ↓ (fail = stop)
Stage 5 (periodic): Performance + Accessibility Tests
```

---

## Coverage Goals
| Category | Target | Rationale |
|----------|--------|-----------|
| Unit (business logic) | > [X]% | [Why — e.g., "Core logic has highest regression risk"] |
| Integration (boundaries) | > [X]% | [Why — e.g., "Boundary errors are most common production bugs"] |
| Acceptance (PRD criteria) | 100% | Every PRD criterion must have a traceable test |
| Security (attack vectors) | All OWASP Top 10 relevant | [Which items are relevant and why] |

## Testing Priority Order
1. [Highest risk area] — because [reason]
2. [Next highest] — because [reason]
3. [Continue — ordered by blast radius of failure]

---

## Self-Verification

Before finalizing this testing plan:
- [ ] Every PRD acceptance criterion maps to a specific test
- [ ] Every security test references a specific OWASP item or threat
- [ ] Test infrastructure uses tools and versions from RESEARCH.md
- [ ] CI/CD stages are ordered fail-fast (cheapest/fastest checks first)
- [ ] Unit test suite has a realistic speed target (< 30s)
- [ ] Integration tests cover all external integration boundaries from ARCHITECTURE.md
- [ ] Supply chain security checks are included
- [ ] Test data strategy handles sensitive data appropriately
- [ ] Coverage goals are realistic and justified
</output_format>
