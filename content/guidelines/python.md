# Python-Specific Guidelines

> Python best practices, type hints, decorators, patterns

---

## 📑 Table of Contents

| Section | Topics |
|---------|--------|
| [Type Hints](#type-hints) | Basic, advanced, generics, protocols |
| [Docstrings](#docstrings) | Google-style format |
| [Import Organization](#import-organization) | Order and anti-patterns |
| [Decorator Patterns](#decorator-patterns) | Basic, with args, registry |
| [Context Managers](#context-managers) | Function and class-based |
| [Async Patterns](#async-patterns) | Concurrent I/O |

---

<a id="type-hints"></a>
## Type Hints

```python
from typing import Optional, List, Dict, TypeVar, Generic, Protocol

# Basic
def greet(name: str) -> str: ...
def find_user(user_id: str) -> Optional[User]: ...
def process(items: List[str]) -> Dict[str, int]: ...

# Generic Repository
T = TypeVar('T')
class Repository(Generic[T]):
    def get(self, id: str) -> Optional[T]: ...
    def save(self, entity: T) -> T: ...

# Protocol (structural typing)
class Comparable(Protocol):
    def __lt__(self, other: Self) -> bool: ...
```

**Best Practices**: ✅ Type hints on all public APIs · ✅ `Optional[X]` for Python 3.9 compatibility · ✅ `TypeVar` for generics · ❌ Avoid `Any`

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

<a id="docstrings"></a>
## Docstrings (Google Style)

```python
def calculate_total(items: List[Item], discount: float = 0.0) -> float:
    """Calculate total price with discount and tax.
    
    Args:
        items: List of items to calculate total for.
        discount: Discount percentage (0.0 to 1.0).
        
    Returns:
        Final total amount after discount and tax.
        
    Raises:
        ValueError: If discount is negative or > 1.0.
        
    Example:
        >>> calculate_total([Item(100), Item(50)], discount=0.1)
        148.5
    """

class UserService:
    """Service for user management operations.
    
    Attributes:
        repository: User data repository.
        cache: Optional cache backend.
    """
```

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

<a id="import-organization"></a>
## Import Organization

```python
# Order: 1. Future → 2. Stdlib → 3. Third-party → 4. Local absolute → 5. Local relative
from __future__ import annotations

import os
from typing import Optional, List

import httpx
from pydantic import BaseModel

from myproject.models import User
from .utils import helper_function
```

**Anti-patterns**: ❌ Wildcard imports (`from x import *`) · ❌ Unused imports · ❌ Circular imports

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

<a id="decorator-patterns"></a>
## Decorator Patterns

### Basic (with functools.wraps)

```python
import functools
from typing import Callable, TypeVar, ParamSpec
P, R = ParamSpec('P'), TypeVar('R')

def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### With Arguments

```python
def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1: raise
                    time.sleep(delay)
        return wrapper
    return decorator
```

### Registry Pattern

```python
class HandlerRegistry:
    _handlers: Dict[str, Type] = {}
    
    @classmethod
    def register(cls, name: str):
        def decorator(handler_class: Type[T]) -> Type[T]:
            cls._handlers[name] = handler_class
            return handler_class
        return decorator

@HandlerRegistry.register("json")
class JsonHandler: pass
```

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

<a id="context-managers"></a>
## Context Managers

```python
from contextlib import contextmanager

# Function-based
@contextmanager
def timed_operation(name: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{name} took {time.perf_counter() - start:.3f}s")

# Class-based
class DatabaseConnection:
    def __enter__(self) -> 'DatabaseConnection':
        self._connection = create_connection(self.connection_string)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._connection: self._connection.close()
        return False  # Don't suppress exceptions
```

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

<a id="async-patterns"></a>
## Async Patterns

```python
import asyncio

async def fetch_all(urls: List[str]) -> List[dict]:
    """Fetch multiple URLs concurrently."""
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]

async def fetch_with_timeout(url: str, timeout: float = 30.0) -> dict:
    async with httpx.AsyncClient(timeout=timeout) as client:
        return (await client.get(url)).json()
```

<p align="right"><sub><a href="#📑-table-of-contents">↑ TOC</a></sub></p>

---

## ✅ Python Checklist

- [ ] Type hints on all public functions
- [ ] Google-style docstrings
- [ ] Imports organized (stdlib → third-party → local)
- [ ] Decorators use `functools.wraps`
- [ ] Context managers for resource cleanup
- [ ] Async for I/O-bound operations
- [ ] No mutable default arguments

---

*Part of SAGE Knowledge Base*
