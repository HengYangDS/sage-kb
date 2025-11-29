# Context Management Practices

> **Load Priority**: On-demand
> **Purpose**: Strategies for building and managing shared context in AI collaboration

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Goal** | Maximize effective collaboration within context window limits |
| **Challenge** | Limited window, infinite potential context |
| **Solution** | Strategic context building, layering, and pruning |

---

## Context Window Model

### Capacity Allocation

| Zone | Allocation | Content |
|------|------------|---------|
| **System** | 5-15% | Instructions, persona, constraints |
| **Reference** | 20-40% | Knowledge, docs, code |
| **Working** | 30-50% | Current task, conversation |
| **Reserved** | 10-20% | Response generation buffer |

### Budget Formula

```
Available Context = Total Window - System - Reserved
Effective Capacity = Available × Utilization Rate (~80%)
```

---

## Context Building Strategies

### Layered Loading

| Layer | Priority | Load Trigger | Content Type |
|-------|----------|--------------|--------------|
| **Core** | Always | Session start | Principles, key refs |
| **Task** | On-demand | Task detection | Relevant guides |
| **Detail** | Lazy | Explicit request | Deep documentation |

### Progressive Disclosure

```
Overview (always) → Framework (on topic) → Detail (on request)
```

| Level | When | Content Depth |
|-------|------|---------------|
| **L1 Overview** | Always loaded | 1-2 sentences per concept |
| **L2 Framework** | Topic triggered | Structure + key points |
| **L3 Detail** | Explicit request | Full documentation |

---

## Context Optimization Techniques

### Front-Loading Critical Info

| Position | Content Priority | Retention |
|----------|-----------------|-----------|
| **Early context** | Highest priority | Best recall |
| **Middle context** | Supporting info | Good recall |
| **Late context** | Recent exchanges | Best recall |

**Strategy**: Place critical references early, let conversation flow naturally.

### Selective Inclusion

| Include | Exclude |
|---------|---------|
| Directly relevant code | Unrelated modules |
| Active constraints | Historical decisions |
| Current task context | Completed task details |
| Exception cases | Happy path (if known) |

### Reference vs Inline

| Approach | When to Use | Trade-off |
|----------|-------------|-----------|
| **Inline** | Frequently referenced | Uses tokens, fast access |
| **Reference** | Occasionally needed | Saves tokens, requires lookup |
| **Summary** | Context needed, not details | Balanced |

---

## Context Pruning

### When to Prune

| Trigger | Action |
|---------|--------|
| **Approaching limit** (>70%) | Remove low-priority content |
| **Task transition** | Clear previous task details |
| **Redundant info** | Deduplicate similar content |
| **Stale context** | Remove outdated references |

### Pruning Priority (Remove First → Last)

```
1. Completed task details
2. Verbose explanations (keep summaries)
3. Redundant confirmations
4. Historical context (keep decisions)
5. Supporting references (keep core)
```

### Pruning Techniques

| Technique | Compression | Use Case |
|-----------|-------------|----------|
| **Summarize** | 60-80% | Long discussions |
| **Extract key points** | 70-90% | Detailed explanations |
| **Remove examples** | 40-60% | After understanding confirmed |
| **Collapse history** | 80-95% | Multi-turn exchanges |

---

## Shared Context Building

### Vocabulary Establishment

| Phase | Action | Example |
|-------|--------|---------|
| **Introduction** | Define term explicitly | "Let's call this pattern X" |
| **Reinforcement** | Use consistently | Reference X in context |
| **Compression** | Abbreviate safely | "X" alone sufficient |

### Context Anchors

| Anchor Type | Purpose | Example |
|-------------|---------|---------|
| **Named concepts** | Quick reference | "the 3-layer pattern" |
| **Numbered items** | Precise reference | "option 2 from earlier" |
| **File markers** | Location reference | "in the config section" |

---

## Context Recovery

### After Window Reset

| Priority | Action |
|----------|--------|
| **1** | Re-establish critical constraints |
| **2** | Summarize completed work |
| **3** | State current task clearly |
| **4** | Provide minimal necessary references |

### Handoff Template

```
## Context Recovery

### Completed
- [Key accomplishments]

### Current State  
- [Where we are now]

### Next Steps
- [Immediate actions needed]

### Key References
- [Essential docs/code to reload]
```

---

## Context Quality Metrics

| Metric | Good | Warning | Action |
|--------|------|---------|--------|
| **Utilization** | 60-80% | >85% | Prune |
| **Relevance** | >90% relevant | <70% | Filter |
| **Freshness** | Current task | Stale refs | Update |
| **Redundancy** | <10% overlap | >20% | Dedupe |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Context dumping** | Loading everything | Layer selectively |
| **No pruning** | Window overflow | Prune proactively |
| **Implicit context** | Assumed knowledge fails | Make explicit |
| **Stale references** | Outdated info misleads | Refresh on change |
| **Flat structure** | No priority signal | Layer by importance |

---

## Integration with 信达雅

| Principle | Context Application |
|-----------|---------------------|
| **信 (Faithfulness)** | Context accurately represents current state |
| **达 (Clarity)** | Context organized for easy navigation |
| **雅 (Elegance)** | Minimal context for maximum effectiveness |

---

## Related

- `information_density.md` — Compression within context
- `token_optimization.md` — Efficient token usage
- `workflow.md` — Collaboration workflow patterns
