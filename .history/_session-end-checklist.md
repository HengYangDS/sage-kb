# Session End Checklist

> Template for AI session conclusion - Copy relevant sections when ending a session

---

## Quick Reference

Use this checklist at the end of significant work sessions to ensure proper documentation and handoff.

---

## Pre-Completion Checks

### Work Verification
- [ ] All planned tasks completed or documented as pending
- [ ] Code changes tested (if applicable)
- [ ] No broken functionality introduced
- [ ] Documentation updated for changed features

### Quality Checks
- [ ] Code follows project conventions (`.context/conventions/`)
- [ ] No temporary debug code left in place
- [ ] Error handling implemented appropriately
- [ ] Timeout limits respected (T1-T5)

---

## Session Documentation

### For Conversation Record (`.history/conversations/`)

Create when: Important decisions made, significant problems solved, or notable learnings

```markdown
# [Topic] - YYYY-MM-DD

## Context
[What prompted this session/discussion]

## Key Decisions
- Decision 1: [description] - Rationale: [why]
- Decision 2: [description] - Rationale: [why]

## Outcomes
- [What was accomplished]
- [What changed]

## Learnings
- [Insights gained]
- [Patterns discovered]

## References
- [Related files/docs]
```

---

### For Handoff Document (`.history/handoffs/`)

Create when: Work needs to continue in future session

```markdown
# [Task] Handoff - YYYY-MM-DD

## Current State
[Where things stand now]

## Completed
- [x] Task 1
- [x] Task 2

## Pending
- [ ] Remaining task 1
- [ ] Remaining task 2

## Blockers
- [Any issues preventing progress]

## Context Needed
- [Files to review]
- [Decisions to understand]
- [Dependencies to be aware of]

## Next Steps
1. [First action to take]
2. [Second action to take]

## Notes
[Any additional context for the next session]
```

---

### For Session State (`.history/current/`)

Create when: Pausing mid-task, need to preserve state

```markdown
# Session State - YYYYMMDD-HHMM

## Active Task
[What's being worked on]

## Progress
- [Current step in process]
- [What's been done so far]

## Open Files/Context
- [Files being edited]
- [Relevant references]

## Immediate Next Action
[Exactly what to do when resuming]
```

---

## Cleanup Actions

After creating appropriate records:

1. [ ] Move completed session files from `.history/current/` to appropriate location
2. [ ] Archive old conversations (>30 days) to `.archive/`
3. [ ] Delete temporary working files from `.outputs/`
4. [ ] Commit changes if significant milestone reached

---

## Quick Decision Guide

| Situation | Action |
|-----------|--------|
| Significant decisions made | Create conversation record |
| Work incomplete, will continue | Create handoff document |
| Pausing mid-task | Create session state |
| Routine completion, no decisions | No record needed |
| Bug fix or minor change | Commit message sufficient |

---

*Part of SAGE Knowledge Base - Session Management*
