# Batch Optimization Practices

> **Load Priority**: On-demand
> **Purpose**: Systematic approach to optimizing multiple items efficiently

---

## Overview

| Aspect        | Description                                       |
|---------------|---------------------------------------------------|
| **Goal**      | Apply consistent improvements across many items   |
| **Challenge** | Scale, consistency, verification, rollback        |
| **Solution**  | Structured batch processing with validation loops |

---

## Batch Processing Framework

### Three-Phase Model

```
Analyze → Transform → Verify
   │          │          │
   ▼          ▼          ▼
 Scope    Changes    Quality
```

| Phase         | Input             | Output            | Gate              |
|---------------|-------------------|-------------------|-------------------|
| **Analyze**   | Raw items         | Categorized set   | Scope confirmed   |
| **Transform** | Categorized items | Modified items    | Changes applied   |
| **Verify**    | Modified items    | Validated results | Quality confirmed |

---

## Batch Sizing Strategy

### Size Selection

| Batch Size      | Use Case              | Risk        | Recovery          |
|-----------------|-----------------------|-------------|-------------------|
| **1-3 items**   | High-risk changes     | Low         | Easy rollback     |
| **5-10 items**  | Standard optimization | Medium      | Moderate effort   |
| **10-20 items** | Low-risk, uniform     | Medium-High | Checkpoint needed |
| **20+ items**   | Automated, tested     | High        | Full automation   |

### Sizing Formula

```
Optimal Batch Size = min(
    Confidence Level × 10,
    Items with Same Pattern,
    Verification Capacity
)
```

| Factor         | Low Confidence | High Confidence |
|----------------|----------------|-----------------|
| **Multiplier** | 1-3            | 5-10            |
| **Example**    | 3-9 items      | 15-30 items     |

---

## Pattern-Based Batching

### Grouping Strategy

| Group By         | When              | Benefit                   |
|------------------|-------------------|---------------------------|
| **Pattern type** | Similar changes   | Consistent transformation |
| **Risk level**   | Mixed criticality | Prioritized verification  |
| **Dependency**   | Related items     | Atomic changes            |
| **Location**     | Same module/dir   | Localized impact          |

### Priority Order

```
1. Quick wins (high impact, low risk)
2. Dependencies (enable other changes)
3. Standard items (bulk of work)
4. Complex cases (need special handling)
5. Edge cases (individual attention)
```

---

## Transformation Patterns

### Uniform Transformation

| Step | Action                     | Validation     |
|------|----------------------------|----------------|
| 1    | Define transformation rule | Test on 1 item |
| 2    | Apply to batch             | Spot check 10% |
| 3    | Run automated checks       | 100% coverage  |
| 4    | Review edge cases          | Manual review  |

### Progressive Transformation

```
Pilot (1-2) → Small Batch (5) → Full Batch → Cleanup
```

| Stage           | Size          | Purpose           | Gate                 |
|-----------------|---------------|-------------------|----------------------|
| **Pilot**       | 1-2           | Validate approach | Manual approval      |
| **Small batch** | 5-10          | Test at scale     | Automated tests pass |
| **Full batch**  | All remaining | Complete work     | Spot check           |
| **Cleanup**     | Exceptions    | Handle edge cases | Final review         |

---

## Verification Strategy

### Multi-Level Verification

| Level              | Coverage     | Method            | When              |
|--------------------|--------------|-------------------|-------------------|
| **L1 Syntax**      | 100%         | Automated linting | After each change |
| **L2 Unit**        | 100%         | Unit tests        | After batch       |
| **L3 Integration** | Key paths    | Integration tests | After all batches |
| **L4 Manual**      | 5-10% sample | Human review      | Before commit     |

### Verification Checklist

- ✓ No syntax errors introduced
- ✓ All existing tests pass
- ✓ New behavior matches expected
- ✓ No unintended side effects
- ✓ Edge cases handled
- ✓ Documentation updated (if needed)

---

## Progress Tracking

### Metrics Dashboard

| Metric            | Formula            | Target         |
|-------------------|--------------------|----------------|
| **Completion**    | Done / Total       | 100%           |
| **Success rate**  | Passed / Attempted | >95%           |
| **Rollback rate** | Reverted / Applied | <5%            |
| **Efficiency**    | Items / Hour       | Baseline × 1.5 |

### Status Categories

| Status          | Symbol | Meaning                   |
|-----------------|--------|---------------------------|
| **Completed**   | ✓      | Successfully processed    |
| **In Progress** | *      | Currently being processed |
| **Failed**      | ✗      | Failed, needs attention   |
| **Skipped**     | ○      | Intentionally excluded    |
| **Pending**     | ·      | Not yet started           |

---

## Rollback Strategy

### Rollback Triggers

| Trigger                    | Action                 | Scope          |
|----------------------------|------------------------|----------------|
| **Single failure**         | Fix and retry          | One item       |
| **Pattern failure** (>10%) | Pause, analyze         | Current batch  |
| **Critical failure**       | Full rollback          | All changes    |
| **Test regression**        | Rollback + investigate | Affected items |

### Rollback Checklist

1. ✓ Identify affected items
2. ✓ Revert changes (version control)
3. ✓ Verify rollback success
4. ✓ Document failure reason
5. ✓ Update approach before retry

---

## Efficiency Techniques

### Parallelization

| Approach               | When Safe       | Caution          |
|------------------------|-----------------|------------------|
| **Independent items**  | No dependencies | Verify isolation |
| **Different modules**  | No cross-refs   | Check imports    |
| **Read-only analysis** | Always          | N/A              |

### Automation Opportunities

| Task               | Automate When          | Keep Manual When        |
|--------------------|------------------------|-------------------------|
| **Detection**      | Pattern is clear       | Nuanced judgment needed |
| **Transformation** | Rule is precise        | Context-dependent       |
| **Verification**   | Criteria are objective | Subjective quality      |
| **Rollback**       | Always automate        | N/A                     |

---

## Documentation

### Batch Log Template

```markdown
## Batch: [Name/ID]

### Scope

- Items: [count]
- Pattern: [description]
- Risk: [Low/Medium/High]

### Results

- Completed: [count] ✓
- Failed: [count] ✗
- Skipped: [count] ○

### Issues

-

[Issue 1]: [resolution]
-

[Issue 2]: [resolution]

### Lessons

- [What worked]
- [What to improve]
```

---

## Anti-Patterns

| Anti-Pattern          | Problem                    | Fix                    |
|-----------------------|----------------------------|------------------------|
| **Big bang**          | All at once, hard to debug | Incremental batches    |
| **No verification**   | Silent failures            | Multi-level checks     |
| **No rollback plan**  | Stuck with bad changes     | Version control + plan |
| **Ignoring failures** | Accumulating debt          | Fix before proceeding  |
| **Over-batching**     | Mixed patterns             | Group by similarity    |

---

## Integration with 信达雅

| Principle            | Batch Application                  |
|----------------------|------------------------------------|
| **信 (Faithfulness)** | Each item correctly transformed    |
| **达 (Clarity)**      | Clear progress and status tracking |
| **雅 (Elegance)**     | Efficient, systematic approach     |

---

## Related

- `incremental_improvement.md` — Iterative enhancement approach
- `patterns.md` — Engineering patterns
- `../../frameworks/resilience/timeout_patterns.md` — Handling timeouts in batch
