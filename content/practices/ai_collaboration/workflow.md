# AI Collaboration Workflow Practices

> **Load Time**: On-demand (~120 tokens)  
> **Purpose**: Practical workflows for effective human-AI collaboration

---

## Daily Workflow Pattern

### Session Start (3 steps)

| Step | Action | Duration |
|------|--------|----------|
| 1. Context | State project/task, recent changes, autonomy level | 2 min |
| 2. Goal | Clear objective, success criteria, time constraints | 1 min |
| 3. Begin | AI confirms understanding, work proceeds per level | — |

**Example**:
```
Project: AI Collaboration KB | Recent: Completed guidelines 01-09 | Autonomy: L3
Goal: Create framework docs (autonomy/levels.md, cognitive/expert_committee.md)
Success: All files created | Time: 2 hours
```

---

## Task Handoff Patterns

| Type | Format | Use Case |
|------|--------|----------|
| **Simple** | "Create X" → AI executes → Reports | Clear, small tasks |
| **Detailed** | Requirements + Constraints + Autonomy | Complex features |
| **Batch** | Task list + Completion criteria | Multiple related tasks |

**Detailed Handoff Template**:
```
Task: [Name] | Autonomy: L[n]
Requirements: [bullet list]
Constraints: [bullet list]
Success: [criteria]
```

---

## Progress Reporting

### Report Types

| Type | When | Key Fields |
|------|------|------------|
| **Checkpoint** | Mid-task | Progress (n/m), Status, Completed, Current, Remaining, Questions |
| **Completion** | Task done | Summary, Changes Made, Testing, Notes, Next Steps |
| **Error** | Issue found | Type, Severity, Location, Analysis, Proposed Solutions |

**Checkpoint Format**: `Progress: n/m | Status: [On track/Blocked/Delayed] | Current: [item] | Questions: [if any]`

**Completion Format**: `Summary → Changes → Testing (pass/fail) → Next Steps`

**Error Format**: `Type: [X] | Severity: [H/M/L] | Location: [path] | Root Cause: [X] | Solutions: [1,2,3] | Recommendation: [n]`

---

## Error Handling Workflow

**Steps**: Stop → Document → Analyze → Propose → Wait (unless L4+)

| Severity | Action | Autonomy Override |
|----------|--------|-------------------|
| High | Stop, report immediately | Always wait |
| Medium | Document, propose solutions | L4+ may proceed |
| Low | Note, continue if clear fix | L3+ may proceed |

---

## Context Preservation

### Session Summary (End of Day)

```
Date: [YYYY-MM-DD]
Accomplished: [list] | In Progress: [list] | Pending: [list]
Key Decisions: [list] | Tomorrow: [priorities] | Notes: [if any]
```

### Context for New Session

```
Project: [name, version, % complete]
Recent Changes: [list]
Branch: [name] | Known Issues: [list]
```

---

## Collaboration Anti-Patterns

| Pattern | Problem | Better Approach |
|---------|---------|-----------------|
| Vague requests | "Make it better" | Specific criteria |
| No context | Starting from scratch | Provide background |
| Micro-managing | Approving every line | Trust autonomy levels |
| Ignoring updates | Missed important info | Review checkpoints |
| Scope creep | Endless expansion | Define boundaries |

**Warning Signs**: Frequent misunderstandings · Repeated clarifications · Unexpected changes · Slow progress

**Recovery**: Pause → Align goals → Adjust autonomy → Add context → Simplify scope

---

## Quick Reference Checklists

| Session Start | Task Handoff | Review |
|---------------|--------------|--------|
| ✓ Context provided | ✓ Requirements clear | ✓ Results match goals |
| ✓ Goals defined | ✓ Success criteria set | ✓ Quality acceptable |
| ✓ Autonomy set | ✓ Time expectations | ✓ Tests included |
| ✓ Constraints stated | ✓ Questions answered | ✓ Docs updated |

---

## Related

- `content/frameworks/autonomy/levels.md` — Autonomy framework
- `content/core/quick_reference.md` — Quick reference card
- `token_optimization.md` — Token efficiency principles

---

*Part of AI Collaboration Knowledge Base*
