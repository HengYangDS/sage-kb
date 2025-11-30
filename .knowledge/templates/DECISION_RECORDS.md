# Decision Records Templates

> Ready-to-use templates for recording decisions and dissenting opinions

---

## Table of Contents

- [1. Quick Reference](#1-quick-reference)
- [2. Dissent Record](#2-dissent-record)
- [3. Decision Record](#3-decision-record)
- [4. Attribution Summary](#4-attribution-summary)

---

## 1. Quick Reference

> **SSOT**: Full definitions in `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md`

| Template | Use Case | When |
|----------|----------|------|
| Dissent Record | Record opposing views | During analysis |
| Decision Record | Document final decision | After consensus |
| Attribution Summary | Track decision ownership | Post-decision |

---

## 2. Dissent Record

**Use for**: Recording opposing opinions during committee analysis

`````markdown
## Dissenting Opinion
**Role**: [Expert]
**Domain**: [Build/Run/Secure/Data/Product/Strategy]
**Position**: [Alternative view]
**Rationale**: [Why this matters]
**Risk if ignored**: [Consequence]
**Recommended mitigation**: [If proceeding anyway]
`````

---

## 3. Decision Record

**Use for**: Documenting final decisions with full attribution

`````markdown
## Decision Record
**Decision**: [What was decided]
**Domain**: [Build/Run/Secure/Data/Product/Strategy]
**Committee**: [Participating roles by domain]
**Score**: [Weighted average]
**Confidence**: [Percentage]
**Key supporters**: [Roles + rationale]
**Dissenting views**: [Roles + concerns]
**Final authority**: [Who made final call]
**Date**: [YYYY-MM-DD]
`````

---

## 4. Attribution Summary

**Use for**: Quick attribution tracking in decision logs

`````markdown
## Attribution Summary
| Decision Point | Supporters | Dissenters | Weight | Deciding Factor |
|----------------|------------|------------|:------:|-----------------|
| [Decision 1] | [Roles] | [Roles] | 0.X | [Key reason] |
| [Decision 2] | [Roles] | [Roles] | 0.X | [Key reason] |
`````

---

## Related

- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution (SSOT)
- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Expert committee framework
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Committee decision templates

---

*Decision Records Template v1.0*