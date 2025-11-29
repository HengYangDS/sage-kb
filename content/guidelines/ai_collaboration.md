# AI Collaboration Guidelines

> Human-AI interaction patterns, autonomy levels, execution modes

---

## 6.1 Instruction Types

| Type            | Description        | Example                              |
|-----------------|--------------------|--------------------------------------|
| **Direct**      | Explicit command   | "Create user registration endpoint"  |
| **Contextual**  | Implied by context | Fixing similar bugs                  |
| **Conditional** | With constraints   | "Refactor only if tests pass"        |
| **Exploratory** | Open-ended         | "Investigate performance bottleneck" |

**Quality Checklist**: Clear objective · Scope boundaries · Success criteria · Constraints · Priority

---

## 6.2 Autonomy Levels

> **Full Reference**: `content/frameworks/autonomy/levels.md`

| Level   | Authority | When to Use                               |
|---------|-----------|-------------------------------------------|
| L1-L2   | 0-40%     | Critical/production, new features         |
| L3-L4 ⭐ | 40-80%    | Bug fixes, refactoring, routine [DEFAULT] |
| L5-L6   | 80-100%   | Docs, formatting, trusted patterns        |

**Increase**: Well-understood · Low risk · Clear rollback · Past success

**Decrease**: Novel/complex · High-stakes · Uncertain requirements · Previous errors

---

## 6.3 Execution Modes

| Mode        | Behavior                    | Use Case        |
|-------------|-----------------------------|-----------------|
| **Plan**    | Create plan, await approval | Complex tasks   |
| **Execute** | Run with progress updates   | Standard tasks  |
| **Review**  | Analyze without changes     | Code review     |
| **Explain** | Teach concepts              | Learning        |
| **Debug**   | Investigate issues          | Troubleshooting |

**Flow**: Plan → Analyze → Create steps → Present → Await | Execute → Confirm → Run → Report → Summarize

---

## 6.4 Communication Patterns

### Status Update Template

```
Status: [In Progress/Blocked/Complete] ([N]/[M] steps)
Completed: [list] | In Progress: [current] | Remaining: [list]
Blockers: [None/description] | ETA: [time]
```

### Error Report Template

```
Type: [class] · Location: [file:line] · Severity: [L/M/H/C]
Description: [what] · Root Cause: [why] · Proposed Fix: [how]
Action: [ ] Approve [ ] Alternative [ ] More context
```

---

## 6.5 Default Behaviors

| Behavior        | Default            | Rationale                  |
|-----------------|--------------------|----------------------------|
| Autonomy        | L2-L3              | Balance control/efficiency |
| Error Handling  | Stop and report    | Prevent cascading          |
| Scope Expansion | Ask first          | Avoid scope creep          |
| Assumptions     | State explicitly   | Ensure alignment           |
| Testing         | Run affected tests | Verify changes             |

### Override Syntax

```
[L4] Complete all formatting fixes in src/
[MODE:REVIEW] Check this PR for security issues
[IF tests pass] Merge to develop branch
```

---

## 6.6 Anti-Patterns

| ❌ Anti-Pattern      | Problem              | ✅ Better            |
|---------------------|----------------------|---------------------|
| Vague instructions  | Misaligned execution | Specific goals      |
| No success criteria | Unknown completion   | Define "done"       |
| Implicit scope      | Over/under delivery  | Explicit boundaries |
| Ignoring warnings   | Cascading errors     | Address concerns    |
| Micro-management    | Inefficient          | Trust autonomy      |

---

## 6.7 Calibration Signals

| Positive ✅                  | Negative ⚠️                |
|-----------------------------|----------------------------|
| Tasks completed as expected | Frequent misunderstandings |
| Few clarifications needed   | Unexpected changes         |
| Results match intent        | Missed requirements        |
| Efficient execution         | Excessive back-and-forth   |

**Actions**:

- Too many assumptions → Lower autonomy, more checkpoints
- Too many questions → More context, raise autonomy
- Consistently good → Higher autonomy for similar tasks
- Repeated errors → Update guidelines, add rules

---

## 6.8 Quick Reference

| Phase      | Actions                                               |
|------------|-------------------------------------------------------|
| **Start**  | Objective · Scope · Autonomy · Priority · Constraints |
| **During** | Monitor · Respond · Approve/reject · Feedback         |
| **After**  | Review · Feedback · Update calibration · Document     |

---

*Part of SAGE Knowledge Base*
