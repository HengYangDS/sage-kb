# Code Style Guidelines

> **Load Time**: On-demand  
> **Purpose**: Consistent, readable, maintainable code

---

## 2.1 General Principles

**Readability First**: Self-documenting code over cryptic shortcuts

```python
# ✅ Self-documenting
def calculate_monthly_payment(principal: float, rate: float, months: int) -> float:
    monthly_rate = rate / 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)

# ❌ Cryptic
def calc(p, r, m):
    return p * r/12 / (1 - (1 + r/12) ** -m)
```

**Consistency**: Follow project style · Use formatters (black, prettier) · Configure linters

---

## 2.2 Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Classes | PascalCase | `UserAccount`, `HttpClient` |
| Functions | snake_case | `get_user()`, `calculate_total()` |
| Variables | snake_case | `user_count`, `max_retries` |
| Constants | SCREAMING_SNAKE | `MAX_CONNECTIONS`, `API_URL` |
| Private | _prefix | `_internal_state`, `_helper()` |
| Type Params | Single uppercase | `T`, `K`, `V` |

**Quality**: Reveals intent · Avoids abbreviations · Uses domain language · Searchable

---

## 2.3 Code Formatting

| Aspect | Python | JS/TS | Markdown |
|--------|--------|-------|----------|
| Line length | 88 | 100 | 120 |
| Indent | 4 spaces | 2 spaces | 2 spaces |

**Blank Lines**: 2 before top-level definitions · 1 between methods

---

## 2.4 Import Organization

```python
# 1. Standard library
import os
from typing import Optional, List

# 2. Third-party
from pydantic import BaseModel

# 3. Local
from .models import User
```

**Best Practices**: Absolute imports · No wildcards · Group related · Sort alphabetically

---

## 2.5 Comments and Documentation

```python
# ✅ Explain WHY
# Using binary search for O(log n) lookup
index = bisect.bisect_left(sorted_items, target)

# ❌ Stating the obvious
counter += 1  # Increment counter
```

**Docstrings**: See `guidelines/python.md` for Google style

---

## 2.6 Error Handling

```python
# ✅ Specific exceptions with context
try:
    user = repository.get(user_id)
except UserNotFoundError:
    logger.warning(f"User {user_id} not found")
    raise
except DatabaseError as e:
    raise ServiceUnavailableError("Unable to fetch user") from e

# ❌ Silent failure
try:
    user = repository.get(user_id)
except Exception:
    pass
```

---

## 2.7 File Structure

```python
"""Module docstring."""

# 1. Imports (organized)
# 2. Constants
MAX_RETRIES = 3

# 3. Type definitions
# 4. Classes
# 5. Functions
# 6. Entry point
if __name__ == "__main__":
    main()
```

---

## 2.8 Quick Checklist

| ✓ | Item |
|---|------|
| [ ] | Names descriptive and consistent |
| [ ] | Formatting follows standards |
| [ ] | Imports organized and minimal |
| [ ] | Comments explain "why" not "what" |
| [ ] | Error handling explicit |
| [ ] | No magic numbers/strings |
| [ ] | Functions focused (<50 lines) |
| [ ] | Classes single responsibility |

---

*Part of AI Collaboration Knowledge Base*
