# Project Constitution

**Project**: [PROJECT_NAME]
**Version**: 1.0.0
**Last Updated**: [DATE]
**Status**: Active

This constitution governs all development decisions, patterns, and practices for this project. All team members (human and AI) must adhere to these principles.

---

## 🎯 Project Purpose

### What This Project Does
[1-2 paragraph description of project purpose and goals]

### What This Project Does NOT Do
[Clear boundaries and out-of-scope items]

### Success Criteria
[How we measure success]

---

## 📜 Core Principles

### 1. Code Quality Over Speed
- **Principle**: Always prioritize maintainable, tested code over quick fixes
- **Rationale**: Technical debt compounds; quality code saves time long-term
- **Application**:
  - All code must have tests (80%+ coverage)
  - All code must pass type checking
  - All code must be reviewed

### 2. Explicit Over Implicit
- **Principle**: Be explicit in code, configuration, and communication
- **Rationale**: Reduces cognitive load, prevents assumptions, aids debugging
- **Application**:
  - Use type hints everywhere
  - Explicit error handling (no bare except)
  - Document assumptions in code comments

### 3. Security By Default
- **Principle**: Security is not optional; it's a requirement
- **Rationale**: Security breaches are costly and damage trust
- **Application**:
  - Never commit secrets
  - Validate all inputs
  - Use parameterized queries
  - Follow OWASP guidelines

### 4. Public-First Documentation
- **Principle**: Document as if code will be public
- **Rationale**: Forces clear thinking and helps onboarding
- **Application**:
  - Clear README with examples
  - Docstrings for all public APIs
  - Architecture documentation in docs/

### 5. Fail Fast, Fail Loudly
- **Principle**: Errors should be caught early and reported clearly
- **Rationale**: Silent failures are the hardest to debug
- **Application**:
  - Raise exceptions for error conditions
  - Use assert for invariants
  - Log all errors with context

---

## 🚫 Constraints and Rules

### Immutable Rules (Cannot Be Violated)

#### 1. No Secrets in Code
- **Rule**: Never commit API keys, passwords, or secrets
- **Enforcement**: Pre-commit hook, automated scanning
- **Exceptions**: None
- **Penalty**: Immediate key rotation, security review

#### 2. All Code Must Have Tests
- **Rule**: Minimum 80% test coverage
- **Enforcement**: CI/CD blocks <80% coverage
- **Exceptions**: Scripts in scripts/ (but encouraged)
- **Penalty**: PR blocked until tests added

#### 3. Type Hints Required
- **Rule**: All functions must have type hints
- **Enforcement**: Mypy in strict mode
- **Exceptions**: None in src/, optional in tests/
- **Penalty**: CI/CD failure

#### 4. No Direct Database Access in Views/Routes
- **Rule**: Use service layer or repository pattern
- **Rationale**: Separation of concerns, testability
- **Enforcement**: Code review
- **Exceptions**: None

### Strong Guidelines (Should Follow Unless Exceptional)

#### 1. Keep Functions Small
- **Guideline**: <50 lines per function
- **Rationale**: Easier to test, understand, maintain
- **Exceptions**: Complex algorithms (must document)

#### 2. Single Responsibility Principle
- **Guideline**: Each class/function should do one thing
- **Rationale**: Easier to test, modify, reuse
- **Exceptions**: Rare (must justify in code review)

#### 3. Avoid Global State
- **Guideline**: Minimize mutable global variables
- **Rationale**: Makes testing difficult, hard to reason about
- **Exceptions**: Application config, loggers

#### 4. Composition Over Inheritance
- **Guideline**: Prefer composition to deep inheritance hierarchies
- **Rationale**: More flexible, easier to test
- **Exceptions**: Framework requirements (Django models, etc.)

---

## 🏗️ Architectural Decisions

### Technology Stack
- **Language**: Python 3.9+
- **Environment Manager**: Poetry
- **Framework**: [Django/FastAPI/Flask/None]
- **Database**: [PostgreSQL/MySQL/SQLite]
- **Validation**: Pydantic v2
- **Testing**: Pytest
- **Linting**: Ruff
- **Type Checking**: Mypy

### Architectural Patterns

#### 1. Layered Architecture
```
API/Routes Layer
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
Database/External Services
```

**Rules**:
- API layer never directly accesses database
- Business logic stays in service layer
- Repository layer is only place with database queries

#### 2. Dependency Injection
- **Pattern**: Use dependency injection for external dependencies
- **Why**: Makes testing easier, reduces coupling
- **How**: Function parameters, not globals

#### 3. Error Handling Strategy
```python
# Custom exceptions for domain errors
class UserNotFoundError(Exception):
    """Raised when user doesn't exist."""

# Let unexpected errors propagate
# Catch specific exceptions only
try:
    user = fetch_user(id)
except UserNotFoundError:
    # Handle business logic error
    return {"error": "User not found"}
# Don't catch general Exception
```

---

## 🧪 Testing Philosophy

### Testing Pyramid
```
        E2E (Few)
      /         \
  Integration (Some)
 /                   \
Unit Tests (Many)
```

### Rules
1. **Unit Tests**: Fast (<1s), isolated, no external deps
2. **Integration Tests**: Test component interactions, may use test DB
3. **E2E Tests**: Test full user flows, slower, fewer

### Coverage Requirements
- **Overall**: 80% minimum
- **Critical Paths**: 100% coverage
- **Utils/Helpers**: 95%+ coverage
- **New Features**: 90%+ coverage

### Test Naming
```python
def test_function_scenario_expected():
    """Test function under specific scenario produces expected result."""
```

---

## 📐 Code Style and Conventions

### Naming Conventions
- **Functions/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`
- **Modules**: `lowercase` or `snake_case`

### File Organization
```python
# 1. Imports (grouped: stdlib, third-party, local)
import os
from typing import Optional

import httpx
from pydantic import BaseModel

from my_package import models

# 2. Constants
API_TIMEOUT = 30

# 3. Classes/Functions
class MyClass:
    """Docstring."""
    ...

# 4. Main execution (if applicable)
if __name__ == "__main__":
    main()
```

### Documentation
- **All public functions**: Docstrings with Google style
- **Complex logic**: Inline comments explaining "why"
- **Public APIs**: Usage examples in docstrings

---

## 🔄 Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - New features
- `fix/*` - Bug fixes

### Code Review Requirements
- **Required Reviewers**: 1+ team member
- **Checks**: All CI/CD must pass
- **Review Checklist**:
  - [ ] Tests added/updated
  - [ ] Documentation updated
  - [ ] No security concerns
  - [ ] Follows code style
  - [ ] No unnecessary complexity

### Merge Criteria
1. All CI/CD checks pass
2. Code review approved
3. No merge conflicts
4. Branch up-to-date with target

---

## 🚀 Deployment Practices

### Environments
1. **Local**: Developer machines
2. **Development**: Shared dev environment
3. **Staging**: Production-like testing
4. **Production**: Live environment

### Deployment Rules
1. **Always deploy to staging first**
2. **Run smoke tests after deployment**
3. **Have rollback plan ready**
4. **Announce deployments to team**

### Release Process
1. Create release branch
2. Update version number
3. Update CHANGELOG.md
4. Test in staging
5. Create GitHub release
6. Deploy to production
7. Tag commit

---

## 🤖 AI Agent Guidelines

### Agent Responsibilities
1. **Follow Constitution**: This document is law for agents
2. **Maintain Context**: Use tiered context system
3. **Document Decisions**: Log sessions and learnings
4. **Ask When Uncertain**: Don't assume; ask for clarification
5. **Prioritize Quality**: Never sacrifice quality for speed

### Agent Constraints
- **Cannot**: Violate immutable rules
- **Cannot**: Commit secrets
- **Cannot**: Skip tests
- **Cannot**: Ignore type checking
- **Must**: Follow architectural patterns
- **Must**: Document all changes
- **Must**: Update relevant context files

### Agent Decision Matrix

| Scenario | Agent Can Decide | Requires Human |
|----------|------------------|----------------|
| Add utility function | ✅ Yes | - |
| Add new test | ✅ Yes | - |
| Fix obvious bug | ✅ Yes | - |
| Refactor small function | ✅ Yes | - |
| Change architecture | ❌ No | Human approval |
| Add new dependency | ❌ No | Human approval |
| Change API contract | ❌ No | Human approval |
| Modify database schema | ❌ No | Human approval |

---

## 📊 Performance Guidelines

### Response Time Targets
- **API Endpoints**: <200ms (p95)
- **Database Queries**: <100ms (p95)
- **Background Jobs**: Complete within timeout

### Optimization Rules
1. **Profile first**: Don't optimize without measuring
2. **Optimize hot paths**: Focus on frequently-called code
3. **Document tradeoffs**: Explain why optimization is needed

### Performance Monitoring
- Monitor key metrics (response time, throughput, errors)
- Set up alerts for SLA violations
- Review performance metrics weekly

---

## 🔐 Security Practices

### Security Checklist
- [ ] All inputs validated
- [ ] SQL injection prevention (use parameterized queries)
- [ ] XSS prevention (escape output)
- [ ] CSRF protection (use framework defaults)
- [ ] Authentication required for sensitive operations
- [ ] Authorization checked before data access
- [ ] Secrets in environment variables
- [ ] Dependencies regularly updated and audited

### Incident Response
1. **Immediate**: Contain the issue
2. **Assess**: Determine impact
3. **Communicate**: Notify stakeholders
4. **Fix**: Deploy fix
5. **Review**: Post-mortem, update practices

---

## 📝 Documentation Requirements

### Required Documentation
1. **README.md**: Project overview, setup, usage
2. **CHANGELOG.md**: Version history
3. **API Documentation**: All public APIs
4. **Architecture Docs**: System design (docs/reference/architecture/)
5. **Decision Records**: ADRs in _internal/docs/decisions/

### Documentation Standards
- Keep docs up-to-date with code
- Use examples liberally
- Link related documentation
- Write for your future self

---

## 🎓 Learning and Improvement

### Continuous Improvement
- **Weekly**: Review learnings from sessions
- **Monthly**: Review and update constitution if needed
- **Quarterly**: Retrospective on processes

### Knowledge Capture
1. Log all sessions in `_internal/project/learnings/raw/sessions/`
2. Distill patterns into `_internal/project/context/`
3. Update ADRs for architectural decisions
4. Share learnings with team

---

## 🔧 Exceptions and Overrides

### When to Break Rules
1. **Emergency hotfix**: Security issue, production down
2. **Proof of concept**: Exploring feasibility
3. **Technical debt**: Document as TODO, create ticket

### How to Request Exception
1. Explain why rule doesn't apply
2. Document alternative approach
3. Get team approval
4. Document decision in ADR

---

## 📋 Onboarding Checklist

### New Team Member (Human)
- [ ] Read this constitution
- [ ] Read README.md and setup guides
- [ ] Review architecture documentation
- [ ] Set up local environment
- [ ] Run tests locally
- [ ] Complete first PR with guidance

### New AI Agent
- [ ] Load AGENTS.md (quick reference)
- [ ] Load .github/copilot-instructions.md (comprehensive)
- [ ] Load _internal/project/AGENT_START_HERE.md
- [ ] Load Tier 0 context (essential/)
- [ ] Read this constitution
- [ ] Understand immutable rules

---

## 🎯 Project-Specific Rules

### [Add Your Project-Specific Rules Here]

Example sections:
- Business logic rules
- Domain-specific constraints
- Integration requirements
- Data retention policies
- Compliance requirements

---

## ✅ Amendment Process

### How to Amend Constitution
1. Propose change in PR
2. Explain rationale
3. Get team consensus
4. Update version number
5. Announce change
6. Update AGENT_START_HERE.md if affects agents

### Version History
- **1.0.0** ([DATE]): Initial constitution

---

## 🤝 Agreement

By contributing to this project, you agree to follow this constitution. This applies to:
- All team members (human and AI)
- All code contributions
- All documentation updates
- All decisions and discussions

**This constitution is living document. It evolves with the project.**

---

**Questions or concerns?** Discuss with team or create issue.
