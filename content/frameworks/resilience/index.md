# Resilience Framework

> Fault tolerance and graceful degradation patterns

---

## Overview

The Resilience Framework provides patterns for building fault-tolerant systems that gracefully handle failures, timeouts, and degraded conditions while maintaining useful functionality.

---

## Documents

| Document              | Description                                    |
|-----------------------|------------------------------------------------|
| `timeout_patterns.md` | Timeout handling and fallback strategies       |

---

## Key Concepts

### Timeout Hierarchy (T1-T5)

| Level | Timeout | Scope            | Action on Timeout      |
|-------|---------|------------------|------------------------|
| T1    | 100ms   | Cache lookup     | Return cached/fallback |
| T2    | 500ms   | Single file      | Use partial/fallback   |
| T3    | 2s      | Layer load       | Load partial + warning |
| T4    | 5s      | Full KB load     | Emergency core only    |
| T5    | 10s     | Complex analysis | Abort + summary        |

### Resilience Principles

- **Never hang**: Always return within timeout
- **Graceful degradation**: Partial results over no results
- **Circuit breaker**: Prevent cascade failures
- **Fallback chains**: Multiple fallback strategies

---

## Related

- `.context/policies/timeout_hierarchy.md` — Timeout configuration
- `.context/decisions/ADR-0003-timeout-hierarchy.md` — Timeout ADR
- `config/core/timeout.yaml` — Timeout settings

---

*Part of SAGE Knowledge Base - Frameworks*
