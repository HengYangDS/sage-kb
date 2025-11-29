# Engineering Practices Guidelines

> Configuration, testing, performance, change control, maintainability

---

## 3.1 Configuration Management

**Priority** (high→low): CLI args → Env vars → Local config → Project config → Code defaults

```python
# ✅ Typed configuration with defaults
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///default.db"
    debug: bool = False
    max_connections: int = 10
    class Config:
        env_prefix = "APP_"
```

**Secrets**: ❌ Never commit · ✅ Env vars or secret managers · ✅ Document required vars · ✅ Provide `.env.example`

---

## 3.2 Testing Practices

**Test Pyramid**: Unit (many, fast) → Integration (moderate) → E2E (few, slow)

**Structure**: `tests/unit/` · `tests/integration/` · `tests/e2e/` · `tests/fixtures/` · `conftest.py`

| Criterion | Description |
|-----------|-------------|
| **Fast** | Unit < 100ms |
| **Isolated** | No external deps |
| **Repeatable** | Same result |
| **Self-validating** | Pass/fail only |

```python
# AAA Pattern
def test_user_creation():
    # Arrange
    service = UserService(mock_repository)
    # Act
    result = service.create_user({"name": "Alice"})
    # Assert
    assert result.name == "Alice"
```

---

## 3.3 Performance Guidelines

**Principles**: Measure first → Optimize hot paths (20/80) → Cache wisely → Async for I/O

```python
# ✅ Batch operations (1 query)
users = repository.get_many(user_ids)

# ❌ N+1 queries
users = [repository.get(id) for id in user_ids]
```

**Checklist**: Optimized queries · Pagination · Timeouts · Caching · Bounded memory

---

## 3.4 Change Control

### Commit Format

```
<type>(<scope>): <subject>
```

**Types**: `feat` · `fix` · `docs` · `style` · `refactor` · `test` · `chore`

### Branch Strategy

`main` (prod) → `develop` (integration) → `feature/*` · `bugfix/*`

### Code Review

✓ Style · ✓ Tests pass · ✓ Docs updated · ✓ Security · ✓ Performance · ✓ Breaking changes documented

---

## 3.5 Maintainability

### Technical Debt Priority

| Priority | Timeline |
|----------|----------|
| Critical | Immediate |
| High | Next sprint |
| Medium | Roadmap |
| Low | As time allows |

### Code Health

```python
# ✅ Low complexity, clear flow
def process_order(order: Order) -> Result:
    if not order.is_valid():
        return Result.invalid("Validation failed")
    if not check_inventory(order.items).available:
        return Result.unavailable()
    return complete_order(order)
```

**Refactoring Triggers**: Duplicate code · Long methods (>50 lines) · Large classes (>300 lines) · Complex conditionals · Feature envy

---

## 3.6 Engineering Checklist

| Phase | Checks |
|-------|--------|
| **Before** | Requirements · Design reviewed · Dependencies identified |
| **During** | Tests alongside code · Style guide · Incremental changes |
| **Merge** | Tests pass · Review approved · Docs updated · Performance OK |

---

*Part of SAGE Knowledge Base*
