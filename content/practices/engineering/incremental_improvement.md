# Incremental Improvement Practices

> **Load Priority**: On-demand
> **Purpose**: Systematic approach to continuous, low-risk enhancement

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Goal** | Steady progress through small, validated changes |
| **Philosophy** | Many small steps > few large leaps |
| **Benefit** | Lower risk, easier rollback, continuous delivery |

---

## Core Principles

### The Incremental Mindset

| Principle | Description | Anti-Pattern |
|-----------|-------------|--------------|
| **Small steps** | Each change is minimal | Big bang releases |
| **Continuous validation** | Test after every step | Test only at end |
| **Always shippable** | Main branch deployable | Long-lived branches |
| **Learn and adapt** | Adjust based on feedback | Rigid plan adherence |

### Step Size Guidelines

| Change Type | Recommended Size | Validation |
|-------------|------------------|------------|
| **Bug fix** | Single issue | Unit test |
| **Refactor** | One pattern | Existing tests |
| **Feature** | Minimal viable slice | Feature test |
| **Optimization** | One metric improvement | Benchmark |

---

## Improvement Cycle

### Four-Step Loop

```
Plan → Do → Check → Adjust
  │     │      │       │
  ▼     ▼      ▼       ▼
Scope  Apply  Verify  Learn
```

| Step | Duration | Output |
|------|----------|--------|
| **Plan** | 10-20% | Clear scope, success criteria |
| **Do** | 40-50% | Implemented change |
| **Check** | 20-30% | Validation results |
| **Adjust** | 10-20% | Lessons, next iteration |

### Cycle Frequency

| Context | Cycle Duration | Batch Size |
|---------|----------------|------------|
| **Rapid iteration** | Minutes-Hours | 1-2 changes |
| **Standard development** | Hours-Days | 3-5 changes |
| **Careful migration** | Days-Weeks | 5-10 changes |

---

## Risk Management

### Risk Assessment Matrix

| Impact ↓ / Likelihood → | Low | Medium | High |
|-------------------------|-----|--------|------|
| **High** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Minimal | Low | Medium |

### Risk Mitigation by Level

| Risk Level | Step Size | Validation | Rollback |
|------------|-----------|------------|----------|
| **Minimal** | Normal | Automated | Standard |
| **Low** | Normal | +Spot check | Standard |
| **Medium** | Smaller | +Peer review | Prepared |
| **High** | Minimal | +Staging test | Ready |
| **Critical** | Atomic | +Manual QA | Instant |

---

## Validation Strategy

### Continuous Validation

| After | Validation Type | Scope |
|-------|-----------------|-------|
| **Each edit** | Syntax/lint | Changed files |
| **Each commit** | Unit tests | Affected modules |
| **Each PR** | Integration tests | Full suite |
| **Each deploy** | Smoke tests | Critical paths |

### Quality Gates

```
Edit → Lint ✓ → Commit → Tests ✓ → PR → Review ✓ → Merge → Deploy
```

| Gate | Criteria | Block on Failure |
|------|----------|------------------|
| **Lint** | No errors | Yes |
| **Unit tests** | 100% pass | Yes |
| **Integration** | 100% pass | Yes |
| **Review** | Approved | Yes |
| **Coverage** | ≥ baseline | Warning |

---

## Progress Measurement

### Velocity Metrics

| Metric | Formula | Healthy Range |
|--------|---------|---------------|
| **Cycle time** | Start → Done | 1-3 days |
| **Change frequency** | Deploys / Week | 5-20 |
| **Change size** | Lines / Change | 10-100 |
| **Success rate** | Successful / Total | >95% |

### Quality Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Defect rate** | Bugs / Changes | <5% |
| **Rollback rate** | Rollbacks / Deploys | <2% |
| **Recovery time** | Detection → Fix | <1 hour |

---

## Handling Setbacks

### When Things Go Wrong

| Situation | Action | Learning |
|-----------|--------|----------|
| **Test failure** | Fix immediately | Add test case |
| **Unexpected behavior** | Rollback, investigate | Improve validation |
| **Performance regression** | Rollback, profile | Add benchmark |
| **User complaint** | Quick fix | Add monitoring |

### Recovery Protocol

```
Detect → Assess → Decide → Act → Document
```

| Step | Time Budget | Output |
|------|-------------|--------|
| **Detect** | ASAP | Issue identified |
| **Assess** | 5-15 min | Impact understood |
| **Decide** | 1-5 min | Rollback or fix forward |
| **Act** | Minutes | Issue resolved |
| **Document** | After resolution | Lessons captured |

---

## Incremental Patterns

### Feature Flags

| State | Behavior | Use Case |
|-------|----------|----------|
| **Off** | Old behavior | Default/safe |
| **Canary** | % of users | Testing |
| **On** | New behavior | Rolled out |

### Strangler Fig Pattern

```
Old System ────────────────────────►
     ↓          ↓          ↓
  New Part 1  Part 2    Part N
     └──────────┴──────────┘
              New System
```

| Phase | Old System | New System |
|-------|------------|------------|
| **Start** | 100% | 0% |
| **Midpoint** | 50% | 50% |
| **End** | 0% | 100% |

### Parallel Run

| Mode | Description | When |
|------|-------------|------|
| **Shadow** | New runs, results discarded | Testing logic |
| **Compare** | Both run, compare results | Validation |
| **Failover** | New primary, old backup | Safe cutover |

---

## Documentation

### Change Log Entry

```markdown
## [Date] Change: [Brief Description]

### What
- [Specific change made]

### Why  
- [Problem solved / improvement gained]

### Validation
- [Tests run, results]

### Impact
- [Affected areas, metrics change]
```

### Improvement Backlog

| Priority | Item | Effort | Impact | Status |
|----------|------|--------|--------|--------|
| P1 | [Item] | S/M/L | High/Med/Low | ○/*/✓ |
| P2 | [Item] | S/M/L | High/Med/Low | ○/*/✓ |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Perfectionism** | Never ships | Good enough, then iterate |
| **Scope creep** | Growing changes | Strict scope boundaries |
| **Skipping validation** | Hidden defects | Always validate |
| **Ignoring feedback** | Repeated mistakes | Learn and adjust |
| **Big merges** | Conflict hell | Frequent small merges |
| **No rollback plan** | Stuck with problems | Always have escape route |

---

## Decision Framework

### When to Proceed

| Signal | Action |
|--------|--------|
| Tests pass | Proceed |
| Clear improvement | Proceed |
| Low risk | Proceed |
| Reversible | Proceed |

### When to Pause

| Signal | Action |
|--------|--------|
| Tests fail | Fix first |
| Unclear benefit | Re-evaluate |
| High risk | Reduce scope |
| Irreversible | Extra validation |

---

## Integration with 信达雅

| Principle | Incremental Application |
|-----------|------------------------|
| **信 (Faithfulness)** | Each step maintains correctness |
| **达 (Clarity)** | Clear progress and status |
| **雅 (Elegance)** | Smooth, sustainable pace |

---

## Related

- `batch_optimization.md` — Batch processing approach
- `patterns.md` — Engineering patterns
- `../../frameworks/resilience/timeout_patterns.md` — Resilience patterns
