# Timeout Hierarchy

> T1-T5 timeout levels for operation classification

---

## 1. Overview

SAGE uses a five-tier timeout hierarchy (T1-T5) to classify operations by expected duration and set appropriate timeout values.

---

## 2. Timeout Levels

| Level | Name | Timeout | Use Case |
|-------|------|---------|----------|
| **T1** | Instant | 50ms | Cache lookup, memory access |
| **T2** | Fast | 200ms | File read, local I/O |
| **T3** | Normal | 1s | Complex processing |
| **T4** | Slow | 5s | External API calls |
| **T5** | Batch | 30s | Batch operations |

---

## 3. Timeout Diagram

```
Timeout Duration (log scale)
    │
    │                                         ████████ T5 (30s)
    │                                         Batch
    │
    │                           ████ T4 (5s)
    │                           External API
    │
    │                 ██ T3 (1s)
    │                 Processing
    │
    │           █ T2 (200ms)
    │           File I/O
    │
    │         █ T1 (50ms)
    │         Cache
    │
    └─────────────────────────────────────────────────►
              Operation Type
```

---

## 4. T1: Instant (50ms)

### 4.1 Description

Operations that should complete almost instantly, typically in-memory operations.

### 4.2 Operations

| Operation | Expected | Max |
|-----------|----------|-----|
| Cache lookup | < 10ms | 50ms |
| Memory read | < 5ms | 50ms |
| Hash computation | < 20ms | 50ms |
| Config access | < 10ms | 50ms |

### 4.3 On Timeout

```python
# T1 timeout indicates system problem
if operation_time > T1_TIMEOUT:
    logger.error("T1 operation exceeded timeout - system issue")
    raise TimeoutError("cache_lookup", T1_TIMEOUT)
```

---

## 5. T2: Fast (200ms)

### 5.1 Description

Local I/O operations that should be fast but involve disk access.

### 5.2 Operations

| Operation | Expected | Max |
|-----------|----------|-----|
| File read | < 100ms | 200ms |
| Directory scan | < 150ms | 200ms |
| Local DB query | < 100ms | 200ms |
| File write | < 100ms | 200ms |

### 5.3 On Timeout

```python
# T2 timeout may indicate I/O issue
if operation_time > T2_TIMEOUT:
    logger.warning("T2 operation slow - possible I/O issue")
    # Try fallback or cached version
```

---

## 6. T3: Normal (1s)

### 6.1 Description

Operations involving significant processing but no external dependencies.

### 6.2 Operations

| Operation | Expected | Max |
|-----------|----------|-----|
| Document parsing | < 500ms | 1s |
| Knowledge indexing | < 800ms | 1s |
| Template rendering | < 300ms | 1s |
| Validation | < 500ms | 1s |

### 6.3 On Timeout

```python
# T3 timeout - provide partial results
if operation_time > T3_TIMEOUT:
    logger.warning("T3 operation timeout - returning partial")
    return partial_result
```

---

## 7. T4: Slow (5s)

### 7.1 Description

Operations involving external services or network calls.

### 7.2 Operations

| Operation | Expected | Max |
|-----------|----------|-----|
| External API call | < 2s | 5s |
| Remote file fetch | < 3s | 5s |
| Database query (remote) | < 2s | 5s |
| Authentication | < 2s | 5s |

### 7.3 On Timeout

```python
# T4 timeout - use circuit breaker
if operation_time > T4_TIMEOUT:
    circuit_breaker.record_failure()
    logger.error("T4 operation timeout - external service issue")
    return cached_or_default()
```

---

## 8. T5: Batch (30s)

### 8.1 Description

Long-running batch operations that process multiple items.

### 8.2 Operations

| Operation | Expected | Max |
|-----------|----------|-----|
| Full knowledge load | < 15s | 30s |
| Batch validation | < 20s | 30s |
| Index rebuild | < 25s | 30s |
| Export operation | < 20s | 30s |

### 8.3 On Timeout

```python
# T5 timeout - checkpoint and resume
if operation_time > T5_TIMEOUT:
    save_checkpoint(progress)
    logger.error("T5 operation timeout - checkpointed")
    raise TimeoutError("batch_operation", T5_TIMEOUT)
```

---

## 9. Implementation

### 9.1 Timeout Decorator

```python
from functools import wraps

def with_timeout(level: str):
    timeouts = {
        "T1": 50, "T2": 200, "T3": 1000, 
        "T4": 5000, "T5": 30000
    }
    
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            timeout_ms = timeouts[level]
            try:
                return await asyncio.wait_for(
                    func(*args, **kwargs),
                    timeout=timeout_ms / 1000
                )
            except asyncio.TimeoutError:
                raise TimeoutError(func.__name__, timeout_ms)
        return wrapper
    return decorator

# Usage
@with_timeout("T2")
async def read_file(path: str) -> str:
    ...
```

### 9.2 Configuration

```yaml
timeout:
  t1_cache_lookup: 50
  t2_file_read: 200
  t3_processing: 1000
  t4_external_api: 5000
  t5_batch: 30000
```

---

## 10. Monitoring

### 10.1 Metrics

| Metric | Description |
|--------|-------------|
| `operation_duration_ms` | Actual operation time |
| `timeout_violations` | Count by level |
| `timeout_percentage` | % of operations timing out |

### 10.2 Alerting

| Level | Threshold | Alert |
|-------|-----------|-------|
| T1 | > 1% | Critical |
| T2 | > 5% | Warning |
| T3 | > 10% | Info |
| T4 | > 20% | Warning |
| T5 | > 30% | Info |

---

## Related

- `CIRCUIT_BREAKER.md` — Failure handling
- `GRACEFUL_DEGRADATION.md` — Degradation strategies
- `../core_engine/EXCEPTIONS.md` — Timeout errors

---

*Part of SAGE Knowledge Base*
