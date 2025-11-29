# Timeout Design Patterns

> **Load Priority**: On-demand
> **Purpose**: Universal timeout and resilience patterns for system design

---

## Overview

| Aspect        | Description                                     |
|---------------|-------------------------------------------------|
| **Goal**      | Ensure systems never hang indefinitely          |
| **Principle** | Always return something within bounded time     |
| **Strategy**  | Hierarchical timeouts with graceful degradation |

---

## Timeout Hierarchy Pattern

### Five-Level Model

| Level  | Scope           | Typical Range | Use Case                        |
|--------|-----------------|---------------|---------------------------------|
| **L1** | Cache/Memory    | 50-200ms      | Hot path lookups, in-memory ops |
| **L2** | Single I/O      | 200-1000ms    | File read, DB query, API call   |
| **L3** | Batch Operation | 1-5s          | Multiple files, batch queries   |
| **L4** | Full Operation  | 5-15s         | Complex workflows, aggregations |
| **L5** | Background Task | 15s-5min      | Analysis, indexing, reports     |

### Level Selection Guide

```
Single item, cached?     → L1
Single item, I/O?        → L2
Multiple items?          → L3
Full workflow?           → L4
Background/async?        → L5
```

### Timeout Calculation

| Factor             | Impact         | Example              |
|--------------------|----------------|----------------------|
| **Base operation** | Starting point | File read: 200ms     |
| **Item count**     | Linear scale   | 10 files: 200ms × 10 |
| **Network**        | +50-200%       | Remote: 400ms        |
| **Complexity**     | +100-300%      | With parsing: 600ms  |
| **Buffer**         | +20-50%        | Safety margin: 750ms |

---

## Circuit Breaker Pattern

### States

```
       ┌─────────────┐
       │   CLOSED    │◄─────────────┐
       │ (normal)    │              │
       └──────┬──────┘              │
              │ failures > threshold│
              ▼                     │
       ┌─────────────┐              │
       │    OPEN     │              │ success
       │ (fail-fast) │              │
       └──────┬──────┘              │
              │ reset timeout       │
              ▼                     │
       ┌─────────────┐              │
       │ HALF-OPEN   │──────────────┘
       │  (probing)  │
       └─────────────┘
              │ failure
              └──────► back to OPEN
```

### Configuration

| Parameter             | Typical Value | Purpose             |
|-----------------------|---------------|---------------------|
| **Failure threshold** | 3-5 failures  | Trigger to open     |
| **Reset timeout**     | 30-60s        | Time before probing |
| **Half-open limit**   | 1-3 requests  | Probe attempts      |
| **Success threshold** | 1-2 successes | Close condition     |

### Implementation Checklist

- ✓ Track failure count per resource/endpoint
- ✓ Fast-fail when open (no actual attempt)
- ✓ Automatic reset timer
- ✓ Probe with limited requests
- ✓ Log state transitions

---

## Graceful Degradation

### Response Priority Chain

```
Complete → Partial → Cached → Fallback → Error
```

| Level        | Response Type   | When to Use            |
|--------------|-----------------|------------------------|
| **Complete** | Full result     | Normal operation       |
| **Partial**  | Subset of data  | Timeout mid-operation  |
| **Cached**   | Previous result | Fresh data unavailable |
| **Fallback** | Default/static  | No cached data         |
| **Error**    | Error message   | All options exhausted  |

### Degradation Strategies

| Strategy               | Description         | Example                  |
|------------------------|---------------------|--------------------------|
| **Partial results**    | Return what's ready | 8/10 items loaded        |
| **Stale cache**        | Serve old data      | Last successful response |
| **Reduced fidelity**   | Simpler response    | Summary vs full detail   |
| **Alternative source** | Backup data source  | Secondary API            |
| **Static fallback**    | Pre-defined default | Default configuration    |

---

## Timeout Handling Patterns

### Immediate Actions

| Scenario       | Action                     | User Communication |
|----------------|----------------------------|--------------------|
| **L1 timeout** | Use fallback               | Silent (internal)  |
| **L2 timeout** | Retry once, then fallback  | Brief notice       |
| **L3 timeout** | Return partial             | Show progress      |
| **L4 timeout** | Checkpoint + resume option | Clear status       |
| **L5 timeout** | Background retry           | Async notification |

### Retry Strategy

| Attempt  | Delay           | Action              |
|----------|-----------------|---------------------|
| **1st**  | 0ms             | Immediate retry     |
| **2nd**  | 100-500ms       | Short delay         |
| **3rd**  | 1-5s            | Exponential backoff |
| **4th+** | Circuit breaker | Stop retrying       |

### Exponential Backoff Formula

```
delay = min(base × 2^attempt, max_delay) + jitter
```

| Parameter      | Typical Value |
|----------------|---------------|
| **Base delay** | 100-500ms     |
| **Max delay**  | 30-60s        |
| **Jitter**     | 0-20% random  |

---

## Cascading Timeout Prevention

### Problem

```
Service A (10s timeout)
    └─► Service B (10s timeout)
            └─► Service C (10s timeout)
                    └─► Total possible: 30s!
```

### Solution: Budget-Based Timeouts

```
Service A: 10s budget
    └─► Service B: remaining - buffer (e.g., 8s)
            └─► Service C: remaining - buffer (e.g., 6s)
```

### Implementation

| Level            | Budget Allocation | Buffer              |
|------------------|-------------------|---------------------|
| **Entry point**  | Full budget       | 10-20% for response |
| **Mid-tier**     | Remaining × 80%   | Processing time     |
| **Leaf service** | Remaining × 80%   | Minimal buffer      |

---

## Monitoring and Alerting

### Key Metrics

| Metric                    | Formula                       | Alert Threshold |
|---------------------------|-------------------------------|-----------------|
| **Timeout rate**          | Timeouts / Total requests     | >1%             |
| **P95 latency**           | 95th percentile response time | >80% of timeout |
| **Circuit breaker trips** | Open state transitions        | >0 per hour     |
| **Degraded responses**    | Partial + Cached / Total      | >5%             |

### Health Indicators

| Indicator         | Healthy      | Warning | Critical |
|-------------------|--------------|---------|----------|
| **Response time** | <50% timeout | 50-80%  | >80%     |
| **Success rate**  | >99%         | 95-99%  | <95%     |
| **Retry rate**    | <1%          | 1-5%    | >5%      |

---

## Anti-Patterns

| Anti-Pattern                 | Problem                      | Fix                       |
|------------------------------|------------------------------|---------------------------|
| **No timeout**               | Infinite hang possible       | Always set timeout        |
| **Same timeout everywhere**  | Cascade risk                 | Hierarchical timeouts     |
| **Timeout = expected time**  | No buffer                    | Add 20-50% margin         |
| **Silent failure**           | User confusion               | Communicate degradation   |
| **Retry storms**             | Overwhelm recovering service | Circuit breaker + backoff |
| **Ignoring partial success** | Lose available data          | Return what's ready       |

---

## Implementation Checklist

### Minimum Viable Resilience

- ✓ Timeout on every external call
- ✓ Fallback for every timeout
- ✓ Logging of all timeouts
- ✓ User-facing status on degradation

### Production-Ready Resilience

- ✓ Hierarchical timeout levels
- ✓ Circuit breaker per dependency
- ✓ Graceful degradation chain
- ✓ Budget-based cascading prevention
- ✓ Metrics and alerting
- ✓ Retry with exponential backoff

---

## Integration with 信达雅

| Principle            | Timeout Application                   |
|----------------------|---------------------------------------|
| **信 (Faithfulness)** | Honor time contracts, never hang      |
| **达 (Clarity)**      | Clear degradation communication       |
| **雅 (Elegance)**     | Graceful handling, not abrupt failure |

---

## Related

- `../design/design_axioms.md` — Fail-Fast principle
- `persistence_patterns.md` — Data durability under failures
- `../../practices/engineering/patterns.md` — Implementation patterns
