# Essential Checklists (<5KB)

## Pre-Commit
- [ ] Tests pass (`pytest`)
- [ ] Lint passes (`ruff check src/ tests/`)
- [ ] Type check passes (`mypy src/`)
- [ ] No debug code left

## Before Creating PR
- [ ] All tests pass with coverage >= 80%
- [ ] CHANGELOG.md updated
- [ ] Documentation updated
- [ ] Commit messages are clear

## Adding New Feature
- [ ] Spec created in `specs/`
- [ ] Tests written first (TDD)
- [ ] Implementation complete
- [ ] Docs updated
- [ ] CHANGELOG.md updated
