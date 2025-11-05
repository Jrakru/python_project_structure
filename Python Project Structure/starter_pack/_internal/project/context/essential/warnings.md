# Critical Warnings (<5KB)

## Common Pitfalls
1. **Virtual environment**: Always activate before working
2. **Import paths**: Use absolute imports from src/
3. **Test isolation**: Don't share mutable state
4. **Type hints**: Required for all public functions

## Anti-Patterns to Avoid
- ❌ Hardcoding file paths
- ❌ Using `print()` for logging (use `logging` module)
- ❌ Catching generic `Exception` without re-raising
- ❌ Modifying mutable default arguments
- ❌ Missing type hints on public APIs
