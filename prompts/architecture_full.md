---
target_tool: "Poppy (Opus 4.6)"
stores_as: "ARCHITECTURE"
description: "Full Architecture document for Tier 3 projects — system design with observability, resilience, deployment, security architecture, and verification points linked to official documentation."
---

<context>
<role>You are a senior software architect designing a system that developers (human and AI) can implement correctly. Your architecture must be specific enough to code against — use actual file names, function signatures, and types. Every pattern must reference official documentation. The quality bar is flagship engineering: this architecture should produce software indistinguishable from what a senior team at Stripe, Linear, or Vercel would build.</role>

<quality_bar>
Production-grade architecture means:
- Every external call has a failure mode and recovery strategy
- Observability is a first-class architectural concern, not an afterthought
- Security is designed in, not bolted on
- The system degrades gracefully under failure
- Configuration, deployment, and operations are considered from the start
</quality_bar>
</context>

<research>
{{RESEARCH_DOC}}
</research>

<prd>
{{PRD}}
</prd>

<project_description>
{{PROJECT_DESCRIPTION}}
</project_description>

<step_back>
Before designing, think through these foundational questions:

1. **What architectural principles matter most for THIS project?** (Not all principles apply equally — identify the top 3-5 that will most impact success)
2. **What patterns does the official documentation recommend for this type of application?** (Don't impose patterns the framework wasn't designed for)
3. **What are common architectural mistakes for this type of project?** (Learn from others' failures)
4. **Where will complexity concentrate?** (Data transformations? External integrations? User interactions? State management? Concurrency?)
5. **What needs to be easy to change later?** (Design for flexibility where uncertainty is highest)
6. **What are the failure domains?** (Which components can fail independently? What's the blast radius of each failure?)
7. **How will we know if the system is healthy?** (What signals indicate problems before users report them?)
8. **For each major component, could a managed service or existing tool provide this capability?** (Don't build what you can buy/adopt — check the landscape analysis for components that should use existing solutions rather than custom code. Every "build custom" component needs justification.)

Document your reasoning before proceeding to the architecture.
</step_back>

<instructions>
Design the complete system architecture. This is for a complex project, so be thorough.

**Requirements:**
- Use actual file names, function signatures, and types from the chosen tech stack
- Every architectural pattern must reference official documentation
- Show explicit verification points that link back to docs
- Address error handling, security, observability, and performance at the architecture level
- Include integration architecture for all external services with failure handling
- Include deployment and configuration architecture
- For customer-facing products: include security architecture with threat modeling

**Cross-reference with PRD:**
- Every PRD feature must map to architecture components
- Every non-functional requirement must be addressed in the architecture
- Data models must support all features
- Error handling must cover all error states defined in the PRD

**Think about what could go wrong:**
- For every external dependency: what if it's down, slow, or returns errors?
- For every data store: what if it's corrupted, full, or unreachable?
- For every user input: what if it's malicious, oversized, or malformed?
- For every background process: what if it crashes, hangs, or processes duplicates?
</instructions>

<uncertainty_handling>
- If an architectural decision depends on information not in the PRD or Research doc: "ASSUMPTION: [assumption] — verify with stakeholder"
- If a pattern is recommended but you're uncertain it's the best fit: "ALTERNATIVE: [other pattern] may be better if [condition]"
- If a technology choice has a risk: "RISK: [what could go wrong] — MITIGATION: [how to handle it]"
</uncertainty_handling>

<output_format>
# Architecture Document

## Architectural Reasoning

### Key Principles for This Project
- **[Principle]**: [Why it matters here and how we'll apply it]
- [Continue for 3-5 principles]

### Patterns Considered

Include "Use existing service/tool" as one pattern option when the landscape analysis identified viable alternatives for any component. If the landscape recommended HYBRID, the Patterns Considered table must show which components use existing tools and which are custom.

| Pattern | Pros | Cons | Fits This Project? |
|---------|------|------|-------------------|
| [Pattern A] | [List] | [List] | Yes/No — [reason] |
| [Pattern B] | [List] | [List] | Yes/No — [reason] |

**Verification checkpoint**: For every custom-built component in the architecture, confirm: "No existing managed service, SaaS product, or well-maintained library provides this capability at acceptable cost and quality." Reference the landscape analysis or state what additional search was performed.

### Selected Architecture: [Pattern Name]
**Reasoning**: [Why this pattern fits best — reference PRD requirements and team capabilities]

### Common Mistakes to Avoid
- [Mistake 1]: [How we'll prevent it — reference docs or prior experience]
- [Mistake 2]: [How we'll prevent it]

### Failure Domain Analysis
| Domain | Components | Failure Impact | Blast Radius | Recovery Strategy |
|--------|-----------|----------------|-------------|-------------------|
| [Database] | [Components that depend on it] | [What breaks] | [How far it spreads] | [How to recover] |
| [External API] | [Components] | [Impact] | [Radius] | [Recovery] |
| [Auth service] | [Components] | [Impact] | [Radius] | [Recovery] |

---

## Directory Structure
```
project-root/
├── src/ (or appropriate for stack)
│   ├── [dir]/
│   │   ├── [file.ext]    # [Purpose — maps to Feature X from PRD]
│   │   └── [file.ext]    # [Purpose]
│   └── [dir]/
│       └── ...
├── tests/
│   ├── unit/              # Unit tests mirroring src structure
│   ├── integration/       # Integration tests for boundaries
│   └── conftest.[ext]     # Shared test fixtures
├── [config files]          # [Purpose]
├── .github/workflows/     # CI/CD pipeline
├── docs/                  # Planning documents
└── [Continue complete tree]
```

---

## Component Architecture

### [Component Name]
- **Purpose**: [One sentence — maps to PRD Feature(s): X, Y]
- **Location**: `[path/to/directory/]`
- **Responsibilities**:
  - [Responsibility 1]
  - [Responsibility 2]
- **Public Interface**:
  ```[language]
  class ClassName:
      def method_name(self, param: Type) -> ReturnType:
          """Description."""
          ...
  ```
- **Internal Dependencies**: [Other components this depends on]
- **External Dependencies**: [Libraries/services with versions]
- **Error Handling**:
  - [Operation]: catches [exception type], returns [error response], logs [context]
  - [Operation]: retries [N times] with [backoff strategy], falls back to [fallback]
- **Docs reference**: [Official doc URL for the pattern used]

[Continue for each component]

---

## Data Flow Diagrams

### Flow 1: [Primary User Action — e.g., "User Creates a New Widget"]
```
[User Action]
    ↓
[Component A] → validates input (rejects: 400 + specific error)
    ↓
[Component B] → applies business logic (fails: 422 + explanation)
    ↓
[Component C] → persists to database (fails: 503 + retry guidance)
    ↓
[Component D] → returns response to user (logs: request duration, status)
    ↓
[Success Response with correlation ID in headers]
```
**Happy path timing budget**: [X]ms total = [Y]ms validation + [Z]ms logic + [W]ms persistence
**Error paths:**
- If validation fails: return 400 immediately, log at DEBUG, no downstream calls
- If business logic fails: return 422, log at INFO with input context
- If database write fails: return 503, log at ERROR with full context, include retry-after header
- If external service is unavailable: [graceful degradation strategy]

[Continue for 3-5 key flows]

---

## Data Models

### [Model Name]
```[language]
class ModelName:
    id: str              # Unique identifier — format: [UUID v4 / ULID / etc.]
    field_name: Type     # Description — validation: [min/max/pattern/required]
    field_name: Type     # Description — validation: [rules]
    created_at: datetime # Auto-generated, UTC, ISO 8601
    updated_at: datetime # Auto-updated on modification
```
**Relationships**: [How this connects to other models]
**Validation rules**: [Business rules enforced at the model level]
**Indexes**: [Which fields need indexes for query performance]

[Continue for each model]

---

## External Integrations

### [Service/API Name]
- **Purpose**: [What capability it provides]
- **SDK/Library**: [Package name] v[X.Y.Z] — [doc URL]
- **Authentication**: [Method — e.g., "API key in header per [doc URL]"]
- **Key Endpoints/Methods**:
  - `method(params)` — [Purpose] — [Exact doc link]
  - `method(params)` — [Purpose] — [Exact doc link]
- **Rate Limits**: [Per docs — requests/minute, daily cap]
- **Resilience Strategy**:
  - **Timeout**: [X]ms per request
  - **Retry**: [N] retries with exponential backoff (initial: [X]ms, max: [Y]ms)
  - **Circuit breaker**: Open after [N] consecutive failures, half-open after [X]s
  - **Fallback**: [What the system does when this integration is unavailable]
- **Data Format**: [Request/response format, serialization]
- **Monitoring**: [What to alert on — error rate > X%, latency > Yms]

[Continue for each external integration]

---

## Security Architecture

### Authentication
- **Method**: [e.g., JWT, session, OAuth2]
- **Implementation**: [Library and pattern — doc URL]
- **Token lifecycle**: [Creation, validation, refresh, expiry durations]

### Authorization
- **Model**: [RBAC, ABAC, etc.]
- **Roles and Permissions**:
  | Role | Permissions | Data Access |
  |------|------------|-------------|
  | [Role] | [What they can do] | [What data they can see] |
- **Enforcement point**: [Where in the request pipeline — middleware, decorator, etc.]

### Input Validation
- **Strategy**: [Validate at boundary with allowlists]
- **Library**: [Validation library — doc URL]
- **Patterns**: [What's validated: type, length, range, format, allowed characters]

### Threat Model (for customer-facing products)
| Threat | Attack Vector | Mitigation | Implementation |
|--------|--------------|------------|----------------|
| Injection | User input in queries | Parameterized queries, input validation | [Specific library/pattern] |
| XSS | User content rendering | Output encoding, CSP headers | [Specific library/pattern] |
| CSRF | Cross-site form submission | CSRF tokens, SameSite cookies | [Framework feature] |
| Broken access control | Direct object reference | Authorization checks on every endpoint | [Middleware/decorator] |
| Dependency vulnerability | Supply chain | Lockfile, dependency scanning in CI | [Tool name] |

### Secrets Management
- **Approach**: [Environment variables / secrets manager]
- **Required secrets**: [List of env vars — NOT values]
- **Rotation policy**: [How and when secrets are rotated]

---

## Observability Architecture

### Structured Logging
- **Framework**: [Logging library — e.g., Python logging, Serilog, Winston]
- **Format**: JSON with fields: `timestamp`, `level`, `message`, `correlation_id`, `component`, `duration_ms`
- **Correlation**: Every request gets a unique correlation ID, propagated to all downstream calls
- **What to log**:
  - Request start (method, path, user_id) — INFO
  - External service calls (service, method, duration) — INFO
  - Errors with full context (error type, message, stack trace, input that caused it) — ERROR
  - Security events (auth failures, permission denials, suspicious input) — WARN
  - Performance anomalies (requests > 2x normal duration) — WARN
- **What NOT to log**: Passwords, tokens, API keys, PII in plain text, full request/response bodies in production

### Health Checks
- **Liveness**: `GET /health` — returns 200 if process is running
- **Readiness**: `GET /health/ready` — returns 200 if all dependencies are reachable
  - Checks: database connection, external API connectivity, cache availability

### Metrics (if applicable)
- Request count by endpoint and status code
- Response time histograms (p50, p95, p99)
- Error rate by category
- External service call duration and error rate
- Queue depth and processing time (if applicable)

### Alerting Triggers
| Condition | Severity | Action |
|-----------|----------|--------|
| Error rate > [X]% for [Y] minutes | Critical | Page on-call |
| Response time p95 > [X]ms | Warning | Notify channel |
| External service down | Warning | Log + graceful degradation |
| Health check failing | Critical | Auto-restart + page |

---

## Error Handling Strategy

### Error Categories
| Category | Example | HTTP Status | User Message | Log Level | Alert |
|----------|---------|-------------|-------------|-----------|-------|
| Validation | Invalid input | 400 | Specific field errors | Debug | No |
| Authentication | Bad/expired token | 401 | "Please sign in again" | Warn | Rate > threshold |
| Authorization | Insufficient permissions | 403 | "You don't have access" | Warn | Always |
| Business Logic | Constraint violated | 409/422 | Specific explanation | Info | No |
| Rate Limit | Too many requests | 429 | "Try again in X seconds" | Info | Rate > threshold |
| External Service | API timeout/error | 503 | "Temporarily unavailable, retrying" | Error | Yes |
| Internal | Unexpected exception | 500 | "Something went wrong (ref: [correlation_id])" | Error + trace | Yes |

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable explanation",
    "details": [{"field": "email", "issue": "Invalid format"}],
    "correlation_id": "uuid-for-debugging"
  }
}
```

### Error Propagation Rules
- Validation errors: return immediately, do not call downstream services
- External service errors: retry with backoff, then return 503 with retry-after
- Internal errors: catch at boundary, log full context, return generic message with correlation ID
- Never expose: stack traces, internal paths, database details, or dependency names to users

---

## Deployment Architecture

### Environments
| Environment | Purpose | Data | Access |
|------------|---------|------|--------|
| Development | Local development | Seed/mock data | Developer only |
| Staging | Pre-production testing | Anonymized production clone | Team |
| Production | Live system | Real data | Users + monitoring |

### Configuration Management
- Environment-specific config via environment variables
- `.env.example` with all required variables documented
- No secrets in code, config files, or version control
- Configuration validation at startup — fail fast if required vars are missing

### CI/CD Pipeline
```
Push to branch → Lint + Type Check → Unit Tests → Build → Integration Tests → Deploy to Staging → Smoke Tests → Deploy to Production
```
- Fast feedback: lint + type check + unit tests complete in < 3 minutes
- Integration tests run against test infrastructure
- Deploy with zero-downtime strategy (blue-green or rolling)
- Automatic rollback on health check failure

---

## Verification Points
During implementation, verify these against official documentation:
- [ ] [Component A] follows [pattern] per [doc URL]
- [ ] [External API] authentication uses [method] per [doc URL]
- [ ] [Database queries] use [pattern — e.g., parameterized] per [doc URL]
- [ ] [Error handling] follows [framework recommendation] per [doc URL]
- [ ] [Logging] uses [structured format] per [library docs URL]
- [ ] [Health checks] follow [framework pattern] per [doc URL]
- [ ] [Continue for all critical verification points]

---

## Open Questions & Assumptions
- **ASSUMPTION**: [What we assumed] — verify with: [who/what]
- **DECISION NEEDED**: [What needs deciding] — impacts: [which components]
- **RISK**: [Identified risk] — mitigation: [strategy]

---

## Self-Verification

Before finalizing, verify:
- [ ] Every PRD feature maps to at least one architecture component
- [ ] Every PRD non-functional requirement is addressed (performance, security, observability, etc.)
- [ ] Every external integration has a resilience strategy (timeout, retry, fallback)
- [ ] Every data flow includes error paths
- [ ] Error handling covers all PRD-defined error states
- [ ] Data models support all features with appropriate validation
- [ ] No circular dependencies in the component graph
- [ ] Observability covers: request tracing, error reporting, health checks, performance metrics
- [ ] Security architecture addresses authentication, authorization, input validation, and secrets management
- [ ] Deployment architecture supports the defined environments and CI/CD pipeline
- [ ] All doc URLs reference the exact versions from RESEARCH.md
</output_format>
