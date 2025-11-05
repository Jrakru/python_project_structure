# Project Constitution

**Project**: [PROJECT_NAME]
**Version**: 2.0.0
**Last Updated**: [DATE]
**Status**: Active
**Philosophy**: Spec-Driven Development with Test-Driven Design

> "This constitution establishes the immutable principles that govern how specifications become code. These are non-negotiable constraints that ensure quality, maintainability, and excellence."

---

## 🎯 Project Purpose

### What This Project Does
[1-2 paragraph description of project purpose and goals]

### What This Project Does NOT Do
[Clear boundaries and out-of-scope items]

### Success Criteria
[How we measure success - must be measurable and tied to specifications]

---

## 📜 Core Philosophy: Spec-Driven Development

### The Specification-First Principle

**All development begins with a specification.** Code is an implementation of specifications, not the other way around.

```
Specification → Contract → Tests → Implementation → Validation
```

**Why Spec-First?**
- Specifications are the source of truth
- Tests validate conformance to specifications
- Implementations fulfill contracts defined in specifications
- Changes start with specification updates
- Documentation is generated from specifications

### The Contract-First Approach

**Every public interface must have a contract before implementation.**

**Contracts Define:**
- Input requirements (types, validation, constraints)
- Output guarantees (types, structure, invariants)
- Behavior specifications (what it does, edge cases)
- Error conditions (what can fail, how it fails)
- Performance characteristics (time/space complexity)

**Contract Evolution:**
1. **Analyze Existing**: Review existing contracts for reuse
2. **Extend Minimally**: Add only what's necessary
3. **Maintain Compatibility**: Preserve existing contracts
4. **Version Explicitly**: Breaking changes require new versions

---

## 🔒 Immutable Principles

**These principles cannot be violated under any circumstance.**

### 1. Specification Precedes Implementation

**Rule**: No code is written without a specification.

**What Qualifies as a Specification:**
- Product Requirements Document (PRD) for features
- API contract (OpenAPI, JSON Schema, etc.)
- Test specification (BDD scenarios, property tests)
- Data model specification (schema, constraints)

**Enforcement**:
- PRs without linked specifications are rejected
- Code reviews verify spec conformance
- CI fails if specifications are missing

**No Exceptions.**

---

### 2. Test-Driven Development (TDD) Mandatory

**Rule**: Tests are written before implementation.

**TDD Cycle (Red-Green-Refactor):**
```python
# 1. RED: Write failing test that defines behavior
def test_user_creation_with_valid_email_succeeds():
    """Given valid user data, user is created successfully."""
    user_data = {"email": "test@example.com", "name": "Test User"}

    user = create_user(user_data)  # This doesn't exist yet

    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.id is not None

# 2. GREEN: Write minimum code to make test pass
def create_user(data: dict) -> User:
    return User(
        id=generate_id(),
        email=data["email"],
        name=data["name"]
    )

# 3. REFACTOR: Improve code while keeping tests green
def create_user(data: dict) -> User:
    validate_user_data(data)  # Add validation
    return User(
        id=generate_id(),
        email=normalize_email(data["email"]),
        name=data["name"]
    )
```

**Test Types (In Order of Writing):**
1. **Contract Tests**: Verify API contract compliance
2. **Unit Tests**: Test individual functions/classes
3. **Integration Tests**: Test component interactions
4. **End-to-End Tests**: Test complete user flows

**Enforcement**:
- Coverage must be ≥95% for new code
- PRs must include tests for all changes
- Tests must pass before merge
- Code without tests is automatically rejected

**No Exceptions.**

---

### 3. Ruff Is The Standard

**Rule**: Ruff is the only linting and formatting tool.

**Configuration** (non-negotiable):
```toml
[tool.ruff]
target-version = "py39"
line-length = 88

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ANN",    # flake8-annotations
    "S",      # flake8-bandit (security)
    "T20",    # flake8-print
    "SIM",    # flake8-simplify
    "RUF",    # Ruff-specific rules
]
ignore = [
    "ANN101",  # Missing type annotation for self
    "ANN102",  # Missing type annotation for cls
]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN"]  # Allow assert, relaxed annotations in tests

[tool.ruff.lint.isort]
known-first-party = ["your_package"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

**Enforcement**:
- Ruff check runs in pre-commit hook
- Ruff format runs automatically on save
- CI fails on any Ruff violations
- No other linters/formatters permitted

**No Exceptions.**

---

### 4. Quality Gates Are Mandatory

**Rule**: Code must pass ALL quality gates before merge.

**Quality Gate Pipeline:**

#### Gate 1: Specification Validation
- [ ] Feature has linked specification
- [ ] Specification reviewed and approved
- [ ] Contracts defined and validated
- [ ] Test scenarios documented

**Automated Check**: PR must link to spec document
**Blocker**: Yes

---

#### Gate 2: Code Quality (Ruff)
```bash
ruff check src/ tests/
ruff format --check src/ tests/
```

**Criteria**:
- Zero Ruff violations
- All code formatted

**Automated Check**: CI runs Ruff
**Blocker**: Yes

---

#### Gate 3: Type Safety (Mypy)
```bash
mypy src/ --strict
```

**Criteria**:
- Zero type errors in src/
- All functions have type hints
- All public APIs fully typed

**Automated Check**: CI runs Mypy
**Blocker**: Yes

---

#### Gate 4: Test Coverage
```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=95
```

**Criteria**:
- ≥95% line coverage for new code
- ≥90% branch coverage
- All critical paths have tests
- All edge cases tested

**Automated Check**: CI runs pytest with coverage
**Blocker**: Yes

---

#### Gate 5: Contract Validation
```bash
# For API contracts
openapi-spec-validator openapi.yaml

# For data contracts
python scripts/validate_contracts.py
```

**Criteria**:
- API contracts valid (OpenAPI/JSON Schema)
- Data models conform to contracts
- Request/response validation passes
- Contract breaking changes flagged

**Automated Check**: CI validates contracts
**Blocker**: Yes

---

#### Gate 6: Security Scan
```bash
ruff check --select=S  # Security rules
bandit -r src/
safety check
```

**Criteria**:
- No security vulnerabilities
- No hardcoded secrets
- Dependencies have no known CVEs
- SQL injection patterns detected

**Automated Check**: CI security scan
**Blocker**: Yes

---

#### Gate 7: Integration Tests
```bash
pytest tests/integration/ -v
```

**Criteria**:
- All integration tests pass
- External dependencies mocked/stubbed
- Contract conformance validated
- Performance within SLA

**Automated Check**: CI runs integration tests
**Blocker**: Yes

---

#### Gate 8: Code Review
**Human Review Required:**
- [ ] Specification alignment verified
- [ ] Code follows architectural patterns
- [ ] No unnecessary complexity
- [ ] Documentation updated
- [ ] Breaking changes documented

**Reviewers**: Minimum 1 (2 for architectural changes)
**Blocker**: Yes

---

### 5. Breaking Changes Require Versioning

**Rule**: API/Contract breaking changes require explicit versioning.

**What Constitutes a Breaking Change:**
- Removing or renaming fields
- Changing field types
- Adding required fields
- Changing validation rules (stricter)
- Changing error codes
- Modifying behavior semantics

**Process**:
1. Document breaking change in spec
2. Create new version (v2, v3, etc.)
3. Maintain old version for deprecation period
4. Update all contracts
5. Migration guide required

**Enforcement**:
- Contract validator detects breaking changes
- CI fails without version bump
- Deprecation timeline enforced

**No Exceptions.**

---

## 🏗️ Development Workflow

### Spec-Driven Development Cycle

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SPECIFY                                                  │
│    Write specification (PRD, API contract, test scenarios)  │
│    Review and approve specification                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 2. CONTRACT                                                 │
│    Define contracts (inputs, outputs, errors)               │
│    Create OpenAPI/JSON Schema                               │
│    Validate contract completeness                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 3. TEST (RED)                                               │
│    Write contract tests (API conformance)                   │
│    Write unit tests (behavior)                              │
│    Write integration tests (component interaction)          │
│    All tests fail (no implementation yet)                   │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 4. IMPLEMENT (GREEN)                                        │
│    Write minimum code to pass tests                         │
│    Follow contracts exactly                                 │
│    Run tests continuously                                   │
│    Stop when all tests pass                                 │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 5. REFACTOR                                                 │
│    Improve code quality                                     │
│    Extract functions/classes                                │
│    Optimize performance                                     │
│    Keep tests green                                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 6. VALIDATE (Quality Gates)                                 │
│    Run all quality gates                                    │
│    Fix any failures                                         │
│    Get code review approval                                 │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│ 7. MERGE                                                    │
│    Squash commits                                           │
│    Update CHANGELOG                                         │
│    Deploy to staging                                        │
│    Monitor for issues                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📐 Architectural Principles

### Layered Architecture (Enforced)

```
┌─────────────────────────────────────────────┐
│ API Layer (FastAPI/Flask/Django)           │
│ - Routes/Controllers                         │
│ - Request/Response validation                │
│ - OpenAPI contract enforcement               │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│ Service Layer (Business Logic)             │
│ - Use cases                                  │
│ - Business rules                             │
│ - Transaction management                     │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│ Repository Layer (Data Access)              │
│ - Database queries                           │
│ - External API calls                         │
│ - Data mapping                               │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│ Domain Layer (Models)                       │
│ - Pydantic models                            │
│ - Business entities                          │
│ - Value objects                              │
└─────────────────────────────────────────────┘
```

**Rules**:
- API layer never directly accesses repositories
- Service layer contains ALL business logic
- Repository layer is ONLY place with database/API calls
- Domain models are pure (no dependencies)

**Enforcement**: Architectural tests verify layer boundaries

---

### Dependency Injection (Required)

**Rule**: Use dependency injection for all external dependencies.

**Good** (Testable):
```python
def create_user(data: dict, db: Database, email_service: EmailService) -> User:
    """Dependencies injected, easy to mock in tests."""
    user = User(**data)
    db.save(user)
    email_service.send_welcome_email(user.email)
    return user
```

**Bad** (Hard to test):
```python
def create_user(data: dict) -> User:
    """Global dependencies, hard to test."""
    user = User(**data)
    DB.save(user)  # Global database connection
    send_email(user.email)  # Global email service
    return user
```

---

## 🧪 Testing Standards

### Test Pyramid (Enforced Ratios)

```
        E2E (5%)
       /        \
  Integration (15%)
 /                 \
Unit Tests (80%)
```

**Mandatory Ratios**:
- **80%** Unit Tests (fast, isolated, many)
- **15%** Integration Tests (moderate, dependencies)
- **5%** E2E Tests (slow, full stack, few)

**Enforcement**: CI calculates test distribution and fails if ratios violated

---

### Test Naming Convention (Mandatory)

```python
def test_<function>_<scenario>_<expected_result>():
    """Test description in Given-When-Then format.

    Given: Initial conditions
    When: Action taken
    Then: Expected outcome
    """
    # Arrange
    ...
    # Act
    ...
    # Assert
    ...
```

**Examples**:
```python
def test_user_creation_with_valid_email_succeeds():
    """Given valid user data, when creating user, then user is created successfully."""

def test_user_creation_with_invalid_email_raises_validation_error():
    """Given invalid email, when creating user, then ValidationError is raised."""

def test_user_lookup_with_nonexistent_id_returns_none():
    """Given non-existent user ID, when looking up user, then None is returned."""
```

---

### Contract Testing (Mandatory for APIs)

**Rule**: All API endpoints must have contract tests.

```python
from pydantic import BaseModel, Field, validator
import pytest

# 1. Define contract
class UserCreateRequest(BaseModel):
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    name: str = Field(..., min_length=1, max_length=100)

    @validator('email')
    def email_must_be_lowercase(cls, v):
        return v.lower()

class UserCreateResponse(BaseModel):
    id: str
    email: str
    name: str
    created_at: str

# 2. Contract test
def test_create_user_contract_valid_request():
    """Contract test: Valid request returns valid response."""
    # Arrange
    request_data = {
        "email": "TEST@example.com",
        "name": "Test User"
    }

    # Act
    response = client.post("/users", json=request_data)

    # Assert: Response conforms to contract
    assert response.status_code == 201
    response_data = UserCreateResponse(**response.json())
    assert response_data.email == "test@example.com"  # Normalized
    assert response_data.name == "Test User"

def test_create_user_contract_invalid_email():
    """Contract test: Invalid email returns 422 with error details."""
    # Arrange
    request_data = {
        "email": "invalid-email",
        "name": "Test User"
    }

    # Act
    response = client.post("/users", json=request_data)

    # Assert: Error response conforms to contract
    assert response.status_code == 422
    error_data = response.json()
    assert "email" in error_data["detail"][0]["loc"]
```

---

### Property-Based Testing (Encouraged)

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1), st.integers(min_value=0))
def test_string_manipulation_properties(text: str, repeat: int):
    """Property: Repeating string N times creates string of length N*len(original)."""
    result = repeat_string(text, repeat)
    assert len(result) == len(text) * repeat
```

---

## 🎯 Quality Metrics

### Required Metrics (Tracked in CI)

| Metric | Threshold | Blocker |
|--------|-----------|---------|
| **Line Coverage** | ≥95% | Yes |
| **Branch Coverage** | ≥90% | Yes |
| **Ruff Violations** | 0 | Yes |
| **Mypy Errors** | 0 | Yes |
| **Security Issues** | 0 | Yes |
| **Contract Violations** | 0 | Yes |
| **Cyclomatic Complexity** | ≤10 per function | Yes |
| **Function Length** | ≤50 lines | Warning |
| **File Length** | ≤500 lines | Warning |

---

## 🚀 CI/CD Pipeline

### Continuous Integration (Every PR)

```yaml
name: Quality Gates

on: [pull_request]

jobs:
  quality-gates:
    runs-on: ubuntu-latest
    steps:
      # Gate 1: Specification Check
      - name: Verify Specification Linked
        run: python scripts/check_spec_link.py

      # Gate 2: Ruff (Linting + Formatting)
      - name: Run Ruff Check
        run: ruff check src/ tests/
      - name: Run Ruff Format Check
        run: ruff format --check src/ tests/

      # Gate 3: Type Checking
      - name: Run Mypy
        run: mypy src/ --strict

      # Gate 4: Tests + Coverage
      - name: Run Tests
        run: |
          pytest \
            --cov=src \
            --cov-report=term-missing \
            --cov-report=xml \
            --cov-fail-under=95 \
            -v

      # Gate 5: Contract Validation
      - name: Validate Contracts
        run: python scripts/validate_contracts.py

      # Gate 6: Security Scan
      - name: Security Check
        run: |
          ruff check --select=S src/
          bandit -r src/ -f json -o bandit-report.json
          safety check --json

      # Gate 7: Test Distribution
      - name: Verify Test Pyramid
        run: python scripts/check_test_distribution.py

      # Gate 8: Code Metrics
      - name: Check Code Metrics
        run: |
          radon cc src/ -a -nb
          radon mi src/ -nb
```

---

## 🤖 AI Agent Guidelines

### Agent Constraints (Immutable)

**AI agents MUST:**
1. ✅ Read specification before writing code
2. ✅ Write tests before implementation
3. ✅ Follow TDD cycle (Red-Green-Refactor)
4. ✅ Validate against contracts
5. ✅ Run all quality gates
6. ✅ Document breaking changes
7. ✅ Update specifications when behavior changes

**AI agents CANNOT:**
1. ❌ Write code without specification
2. ❌ Skip tests
3. ❌ Violate Ruff rules
4. ❌ Ignore type errors
5. ❌ Break contracts without versioning
6. ❌ Commit secrets
7. ❌ Bypass quality gates

### Agent Decision Matrix

| Action | Agent Can Decide | Requires Human | Forbidden |
|--------|------------------|----------------|-----------|
| Write unit test | ✅ | - | - |
| Implement tested function | ✅ | - | - |
| Refactor with green tests | ✅ | - | - |
| Add new endpoint | - | ✅ Spec required | - |
| Change contract | - | ✅ Versioning required | - |
| Skip test | - | - | ❌ Never |
| Bypass quality gate | - | - | ❌ Never |
| Commit without spec | - | - | ❌ Never |

---

## 📊 Performance Standards

### Response Time Targets (SLA)

| Operation Type | p50 | p95 | p99 |
|----------------|-----|-----|-----|
| API Endpoint | <50ms | <200ms | <500ms |
| Database Query | <10ms | <50ms | <100ms |
| External API Call | <100ms | <500ms | <1s |

**Enforcement**:
- Performance tests in CI
- SLA violations trigger alerts
- Optimize only after profiling

---

## 🔐 Security Standards

### Security Checklist (Every PR)

- [ ] No hardcoded secrets (enforced by Ruff S rule)
- [ ] All inputs validated (Pydantic models)
- [ ] SQL injection prevention (parameterized queries/ORM)
- [ ] XSS prevention (output escaping)
- [ ] CSRF protection (framework defaults)
- [ ] Authentication required (specified in contract)
- [ ] Authorization checked (RBAC/ABAC)
- [ ] Dependencies audited (safety check)
- [ ] Error messages don't leak info

**Enforcement**: Security gate in CI

---

## 📝 Documentation Requirements

### Required Documentation

1. **Specification** (Before Implementation)
   - Feature specification (PRD)
   - API contract (OpenAPI)
   - Data models (JSON Schema)
   - Test scenarios (BDD)

2. **Code** (During Implementation)
   - Docstrings (Google style, type hints)
   - Inline comments (why, not what)
   - Examples in docstrings

3. **API** (Auto-generated)
   - OpenAPI from code
   - Request/response examples
   - Error codes

4. **Architecture** (Decision Records)
   - ADRs for architectural decisions
   - Contract breaking changes
   - Migration guides

---

## ✅ Definition of Done

**A task is done when:**

- [ ] Specification approved
- [ ] Contracts defined
- [ ] Tests written (TDD: Red phase)
- [ ] Implementation complete (TDD: Green phase)
- [ ] Code refactored (TDD: Refactor phase)
- [ ] All quality gates pass:
  - [ ] Ruff check (0 violations)
  - [ ] Mypy check (0 errors)
  - [ ] Tests pass (≥95% coverage)
  - [ ] Contract validation pass
  - [ ] Security scan pass
  - [ ] Integration tests pass
- [ ] Code review approved
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] Deployed to staging
- [ ] Smoke tests pass in staging

**Anything less is NOT done.**

---

## 🔧 Exception Process

### When to Request Exception

Exceptions to immutable rules are **extremely rare** and require:

1. **Technical Justification**
   - Why rule doesn't apply
   - Alternative approach
   - Risk assessment

2. **Approval Process**
   - Team discussion
   - Tech lead approval
   - Document in ADR

3. **Temporary Only**
   - Specify time limit
   - Remediation plan
   - Follow-up tracking

**Emergency exceptions** (security, production down):
- Tech lead can grant temporary exception
- Must be remediated within 48 hours
- Post-mortem required

---

## 📋 Onboarding Checklist

### New Team Member (Human)

- [ ] Read this constitution (non-negotiable)
- [ ] Understand spec-driven development
- [ ] Practice TDD cycle (pair programming)
- [ ] Set up Ruff in IDE
- [ ] Run quality gates locally
- [ ] Review sample specifications
- [ ] Complete first PR with guidance
- [ ] Shadow code review

### New AI Agent

- [ ] Load AGENTS.md
- [ ] Load .github/copilot-instructions.md
- [ ] Load this constitution
- [ ] Understand immutable rules
- [ ] Understand TDD workflow
- [ ] Understand quality gates
- [ ] Test spec-driven cycle
- [ ] Verify cannot bypass gates

---

## 🔄 Amendment Process

### How to Amend Constitution

1. **Propose Change**
   - Create issue with rationale
   - Link to problems/patterns
   - Suggest alternative

2. **Team Discussion**
   - Review impact
   - Consider exceptions
   - Vote on change

3. **Approval Requirements**
   - 75% team agreement
   - Tech lead sign-off
   - Document in ADR

4. **Implementation**
   - Update constitution
   - Update CI/CD
   - Update tooling
   - Announce to team
   - Training if needed

### Version History

- **2.0.0** ([DATE]): Added spec-driven development, TDD, quality gates
- **1.0.0** ([DATE]): Initial constitution

---

## 🎓 Learning Resources

### Spec-Driven Development
- GitHub Spec Kit: https://github.com/github/spec-kit
- Spec-Driven AI Coding patterns
- OpenAPI Specification: https://swagger.io/specification/

### Test-Driven Development
- "Test-Driven Development by Example" - Kent Beck
- pytest documentation: https://docs.pytest.org/
- hypothesis (property testing): https://hypothesis.readthedocs.io/

### Contract-First
- OpenAPI: https://www.openapis.org/
- JSON Schema: https://json-schema.org/
- Pydantic: https://docs.pydantic.dev/

### Tools
- Ruff: https://docs.astral.sh/ruff/
- Mypy: https://mypy.readthedocs.io/
- pytest: https://docs.pytest.org/

---

## 🤝 Agreement

By contributing to this project, you agree to follow this constitution. This applies to:
- All team members (human and AI)
- All code contributions
- All documentation updates
- All decisions and discussions

**This constitution is law. These principles are immutable. Quality is non-negotiable.**

---

**Questions or concerns?** Create an issue for discussion.
