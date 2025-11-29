# Data Persistence Patterns

> **Load Priority**: On-demand
> **Purpose**: Universal patterns for data lifecycle, retention, and cleanup

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Goal** | Manage data durably across sessions and failures |
| **Challenge** | Balance retention vs storage, consistency vs performance |
| **Solution** | Lifecycle-based persistence with tiered strategies |

---

## Data Lifecycle Model

### Five Stages

```
Create → Active → Archive → Expire → Delete
   │        │         │        │        │
   ▼        ▼         ▼        ▼        ▼
 Write   Access    Cold     Aged    Purged
```

| Stage | Duration | Access Pattern | Storage Tier |
|-------|----------|----------------|--------------|
| **Create** | Instant | Write-once | Hot |
| **Active** | Hours-Days | Frequent R/W | Hot |
| **Archive** | Days-Months | Rare read | Warm |
| **Expire** | Months-Years | Almost never | Cold |
| **Delete** | End | Never | Removed |

---

## Retention Strategies

### Time-Based Retention

| Policy | Retention | Use Case |
|--------|-----------|----------|
| **Session** | Until session end | Temp state |
| **Short** | 1-7 days | Recent activity |
| **Medium** | 7-30 days | Working history |
| **Long** | 30-365 days | Audit trail |
| **Permanent** | Forever | Legal/compliance |

### Count-Based Retention

| Policy | Keep | Behavior |
|--------|------|----------|
| **Last N** | N most recent | Rolling window |
| **Top N** | N highest priority | Priority queue |
| **First N** | N oldest | Historical record |

### Hybrid Retention

```
Keep = max(Time-based, Count-based)
```

| Example | Rule | Keeps |
|---------|------|-------|
| Activity log | 30 days OR last 1000 | Whichever is more |
| Checkpoints | 7 days AND last 10 | Intersection |
| Decisions | 90 days OR last 100, priority > medium | Complex filter |

---

## Storage Tiers

### Three-Tier Model

| Tier | Speed | Cost | Use For |
|------|-------|------|---------|
| **Hot** | <10ms | $$$ | Active data, cache |
| **Warm** | 10-100ms | $$ | Recent archives |
| **Cold** | 100ms-1s | $ | Long-term storage |

### Tier Transition Triggers

| Trigger | Action | Example |
|---------|--------|---------|
| **Age** | Hot → Warm after N days | 7 days old → warm |
| **Access** | Promote on read | Cold accessed → warm |
| **Size** | Compress when large | >1MB → compress |
| **Priority** | Keep high-priority hot | Priority=high stays |

---

## Cleanup Strategies

### Cleanup Triggers

| Trigger | When | Action |
|---------|------|--------|
| **Scheduled** | Cron/timer | Batch cleanup |
| **Threshold** | Storage > X% | Emergency cleanup |
| **Event** | Session end | Session cleanup |
| **Manual** | User request | On-demand |

### Cleanup Priority (Delete First → Last)

```
1. Temporary/session data
2. Expired items
3. Low-priority items
4. Oldest items (within policy)
5. Largest items (if space critical)
```

### Safe Cleanup Protocol

| Step | Action | Validation |
|------|--------|------------|
| 1 | Identify candidates | Match retention policy |
| 2 | Check dependencies | No active references |
| 3 | Backup if needed | Archive before delete |
| 4 | Delete | Actual removal |
| 5 | Verify | Confirm freed space |

---

## Consistency Patterns

### Write Patterns

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Write-through** | Write to all tiers | Slow write, fast read |
| **Write-back** | Write hot, sync later | Fast write, risk loss |
| **Write-ahead log** | Log before apply | Durable, recoverable |

### Read Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Read-through** | Cache miss loads from source | Transparent caching |
| **Cache-aside** | App manages cache | Fine control |
| **Refresh-ahead** | Preemptive refresh | Predictable access |

---

## Priority System

### Priority Levels

| Level | Value | Retention Modifier |
|-------|-------|-------------------|
| **Critical** | 100 | 4× base retention |
| **High** | 70 | 2× base retention |
| **Medium** | 50 | 1× base retention |
| **Low** | 30 | 0.5× base retention |
| **Temporary** | 10 | Session only |

### Priority Assignment

| Factor | Priority Boost |
|--------|----------------|
| User-created | +20 |
| Referenced by other data | +10 per ref |
| Recently accessed | +10 |
| Large size | -10 (encourage cleanup) |
| Error/incomplete | -20 |

---

## Recovery Patterns

### Failure Scenarios

| Failure | Impact | Recovery |
|---------|--------|----------|
| **Process crash** | In-memory loss | Restore from disk |
| **Disk failure** | Local data loss | Restore from replica |
| **Corruption** | Data unusable | Restore from backup |
| **Accidental delete** | User data loss | Restore from trash/backup |

### Recovery Strategies

| Strategy | Description | RPO/RTO |
|----------|-------------|---------|
| **Checkpoint** | Periodic full state | RPO: checkpoint interval |
| **WAL replay** | Replay transaction log | RPO: last committed |
| **Replica failover** | Switch to replica | RTO: seconds |
| **Backup restore** | Restore from backup | RTO: minutes-hours |

---

## Implementation Checklist

### Minimum Viable Persistence

- ✓ Define retention policy per data type
- ✓ Implement cleanup trigger (at least scheduled)
- ✓ Add logging for all deletions
- ✓ Basic backup/restore capability

### Production-Ready Persistence

- ✓ Tiered storage with auto-transition
- ✓ Priority-based retention
- ✓ Multiple cleanup triggers
- ✓ Write-ahead logging
- ✓ Automated backup verification
- ✓ Retention policy monitoring

---

## Configuration Template

```yaml
persistence:
  retention:
    default: 30d
    by_type:
      session: 0  # End of session
      activity: 7d
      decision: 90d
      checkpoint: 10 count
  
  cleanup:
    schedule: "0 2 * * *"  # 2 AM daily
    threshold: 80%  # Emergency at 80% full
    batch_size: 1000
  
  priority:
    default: 50
    boost:
      user_created: 20
      referenced: 10
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Keep everything** | Storage explosion | Define retention policy |
| **Delete immediately** | No recovery option | Soft delete with grace period |
| **No cleanup** | Gradual slowdown | Scheduled cleanup |
| **Single tier** | Cost inefficiency | Tiered storage |
| **No backup** | Data loss risk | Regular backups |
| **Inconsistent policy** | Unpredictable behavior | Centralized config |

---

## Metrics

### Health Indicators

| Metric | Healthy | Warning | Action |
|--------|---------|---------|--------|
| **Storage usage** | <70% | 70-85% | Plan expansion |
| **Cleanup success** | >99% | <95% | Investigate failures |
| **Recovery time** | <target | >target | Optimize process |
| **Data age distribution** | Per policy | Anomalies | Review retention |

---

## Integration with 信达雅

| Principle | Persistence Application |
|-----------|------------------------|
| **信 (Faithfulness)** | Data integrity, no silent loss |
| **达 (Clarity)** | Clear retention policies |
| **雅 (Elegance)** | Efficient lifecycle management |

---

## Related

- `../resilience/timeout_patterns.md` — Handling persistence timeouts
- `../../practices/engineering/batch_optimization.md` — Batch cleanup
- `../../practices/engineering/incremental_improvement.md` — Gradual migration
