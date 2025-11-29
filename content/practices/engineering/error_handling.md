# Error Handling Patterns

> **Load Time**: On-demand (~120 tokens)  
> **Purpose**: Universal error handling, degradation, and recovery strategies

---

## 1. Core Principles

| Principle                | Description                                           |
|--------------------------|-------------------------------------------------------|
| **Fail Fast**            | Quickly detect and report failures, don't hide errors |
| **Graceful Degradation** | Return partial results rather than complete failure   |
| **User Feedback**        | Always inform user of error status                    |
| **Recoverability**       | Provide recovery path or alternatives                 |

---

## 2. Timeout Handling

### Timeout Hierarchy Design

| Operation Type      | Recommended Timeout | Fallback Strategy                 |
|---------------------|---------------------|-----------------------------------|
| Cache lookup        | 50-100ms            | Skip cache, continue              |
| Local file          | 200-500ms           | Use default or fallback content   |
| Database query      | 1-3s                | Return cached data or error       |
| External API        | 3-10s               | Return cache or degraded response |
| Complex computation | 10-30s              | Abort and return partial results  |

### Timeout Handling Pattern

```python
import asyncio


async def with_timeout(coro, timeout_sec: float, fallback=None):
    try:
        return await asyncio.wait_for(coro, timeout=timeout_sec)
    except asyncio.TimeoutError:
        return fallback
```

---

## 3. Degradation Strategies

### Strategy Types

| Strategy   | Behavior                      | Use Case                 |
|------------|-------------------------------|--------------------------|
| `graceful` | Return partial/cached results | User experience priority |
| `strict`   | Return explicit error         | Data integrity priority  |
| `silent`   | Log and return default        | Non-critical features    |

### Degradation Decision Tree

```
Error occurs
    │
    ├─ Retryable? → Retry (with backoff)
    │
    ├─ Has cache? → Return cache (mark as stale)
    │
    ├─ Has default? → Return default value
    │
    └─ Critical feature? → Return error : Silent degrade
```

---

## 4. Retry Strategies

### Exponential Backoff

```python
import random


def get_retry_delay(attempt: int, base_ms: int = 100) -> float:
    """Exponential backoff with jitter"""
    delay = base_ms * (2 ** attempt)
    jitter = random.uniform(0, delay * 0.1)
    return min(delay + jitter, 30000)  # Max 30 seconds
```

### Retry Conditions

| Retryable               | Non-Retryable        |
|-------------------------|----------------------|
| Network timeout         | Auth failure         |
| Connection lost         | Invalid parameters   |
| 503 Service unavailable | 404 Not found        |
| 429 Rate limited        | Business logic error |

---

## 5. Circuit Breaker Pattern

### State Machine

```
CLOSED ──(consecutive failures ≥ threshold)──▶ OPEN
   ▲                                             │
   │                                             │(after cooldown)
   │                                             ▼
   └───────(test success)──────── HALF_OPEN
```

### Configuration Parameters

| Parameter          | Typical Value | Description               |
|--------------------|---------------|---------------------------|
| failure_threshold  | 3-5           | Failures before opening   |
| reset_timeout      | 30-60s        | Cooldown before half-open |
| half_open_requests | 1-3           | Test requests allowed     |

### Implementation

```python
from enum import Enum


class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreaker:
    def __init__(self, threshold: int = 5, timeout: int = 30):
        self.threshold = threshold
        self.timeout = timeout
        self.failures = 0
        self.state = CircuitState.CLOSED
        self.last_failure_time = None

    def can_execute(self) -> bool:
        if self.state == CircuitState.CLOSED:
            return True
        if self.state == CircuitState.OPEN:
            if time_since(self.last_failure_time) > self.timeout:
                self.state = CircuitState.HALF_OPEN
                return True
            return False
        return True  # HALF_OPEN allows test
```

---

## 6. Error Response Format

### Standard Error Structure

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {},
    "retry_after": 30
  },
  "meta": {
    "request_id": "abc-123",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

### Error Code Conventions

| Category       | Prefix   | Example              |
|----------------|----------|----------------------|
| Validation     | `VAL_`   | `VAL_INVALID_EMAIL`  |
| Authentication | `AUTH_`  | `AUTH_TOKEN_EXPIRED` |
| Authorization  | `AUTHZ_` | `AUTHZ_FORBIDDEN`    |
| Resource       | `RES_`   | `RES_NOT_FOUND`      |
| System         | `SYS_`   | `SYS_UNAVAILABLE`    |

---

## 7. Logging Best Practices

### What to Log

| Level | When                | Content                      |
|-------|---------------------|------------------------------|
| ERROR | Unexpected failures | Full context, stack trace    |
| WARN  | Degraded operation  | What degraded, fallback used |
| INFO  | Recovery            | What recovered, how long     |
| DEBUG | Retry attempts      | Attempt number, delay        |

### Structured Error Log

```python
logger.error(
    "Operation failed",
    extra={
        "error_code"   : "DB_CONNECTION_FAILED",
        "attempt"      : 3,
        "elapsed_ms"   : 5000,
        "fallback_used": "cache",
        "request_id"   : request_id,
    }
)
```

---

## 8. Quick Checklist

| ✓ Do                         | ✗ Don't                           |
|------------------------------|-----------------------------------|
| Set timeouts on all I/O      | Let operations hang indefinitely  |
| Use specific exception types | Catch bare `Exception`            |
| Include context in errors    | Return generic error messages     |
| Log with request IDs         | Log without traceability          |
| Implement circuit breakers   | Let failures cascade              |
| Provide fallback values      | Fail completely on partial errors |

---

## Related

- `content/frameworks/resilience/timeout_patterns.md` — Timeout patterns
- `content/practices/engineering/api_design.md` — API error responses
- `content/practices/engineering/logging.md` — Logging practices

---

*Part of AI Collaboration Knowledge Base*
