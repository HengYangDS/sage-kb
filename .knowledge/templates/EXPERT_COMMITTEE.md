# Expert Committee Decision Templates

> Ready-to-use decision prompts for multi-perspective analysis

---

## Table of Contents

- [1. Quick Reference](#1-quick-reference)
- [2. L1 Quick Check](#2-l1-quick-check)
- [3. L2 Standard Review](#3-l2-standard-review)
- [4. L3 Deep Analysis](#4-l3-deep-analysis)
- [5. L4 Comprehensive Review](#5-l4-comprehensive-review)
- [6. L5 Full Committee](#6-l5-full-committee)
- [7. Analysis Templates](#7-analysis-templates)
- [8. Usage Tips](#8-usage-tips)

---

## 1. Quick Reference

> **SSOT**: Full definitions in `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md`

| Level | Experts | Angles | Time | Use Case |
|-------|---------|--------|------|----------|
| L1 | 2-3 | 3 | 15 min | Bug fix, config change |
| L2 | 4-6 | 12 | 30 min | Minor feature, compatible API change |
| L3 | 7-10 | 23 | 1 hour | Refactoring, new tech adoption |
| L4 | 11-15 | 31 | 2-3 hours | Architecture change, DB migration |
| L5 | 16-23 | 37 | Half day | Platform change, security overhaul |

---

## 2. L1: Quick Check

**Use for**: Bug fix, config change, routine decisions

**Panel**: Engineer, QA

**Template**:

`````markdown
## L1 Quick Check
**Decision**: [What]
**Panel**: Engineer, QA

| Angle | Score | Notes |
|-------|:-----:|-------|
| Correctness | 1-5 | |
| Clarity | 1-5 | |
| Maintainability | 1-5 | |

**Verdict**: [Go/No-Go]
**Confidence**: [High/Medium/Low]
`````

---

## 3. L2: Standard Review

**Use for**: Minor feature, backward-compatible API change

**Panel**: Architect, Engineer, QA, PM

**Template**:

`````markdown
## L2 Standard Review
**Decision**: [What]
**Context**: [Background]
**Panel**: Architect, Engineer, QA, PM

### Expert Assessment
| Expert | Score | Concerns | Recommendations |
|--------|:-----:|----------|-----------------|
| Architect | 1-5 | | |
| Engineer | 1-5 | | |
| QA | 1-5 | | |
| PM | 1-5 | | |

### Risk Summary
| Dimension | Level |
|-----------|-------|
| Technical | Low/Med/High |
| Business | Low/Med/High |
| Timeline | Low/Med/High |

**Verdict**: [Approve/Revise/Reject]
**Conditions**: [If any]
**Next Steps**: [Actions]
`````

---

## 4. L3: Deep Analysis

**Use for**: Significant refactoring, new technology adoption

**Panel**: Architect, Engineer, QA, DevOps, Security, PM (7-10 experts)

**Template**:

`````markdown
## L3 Deep Analysis
**Decision**: [What]
**Context**: [Background]
**Stakeholders**: [Who]
**Panel**: [List 7-10 experts]

### Angle Evaluation (1-23)
| # | Angle | Score | Expert | Notes |
|---|-------|:-----:|--------|-------|
| 1 | Correctness | 1-5 | | |
| 2 | Completeness | 1-5 | | |
| ... | ... | ... | ... | ... |

### Dimension Scores
| Dimension | Score | Weight |
|-----------|:-----:|:------:|
| Technical | X/25 | 40% |
| Business | X/25 | 35% |
| Process | X/25 | 25% |
| **Total** | X/100 | |

### Risk Matrix
| Risk | Probability | Impact | Mitigation |
|------|:-----------:|:------:|------------|
| [Risk 1] | H/M/L | H/M/L | [Action] |

### Expert Votes
| Expert | Vote | Confidence | Key Concern |
|--------|------|:----------:|-------------|
| [Role] | Approve/Reject | H/M/L | |

**Verdict**: [Approve/Conditional/Reject]
**Score**: [X/100]
**Conditions**: [Required items]
**Action Items**: [With owners]
`````

---

## 5. L4: Comprehensive Review

**Use for**: Architecture change, database migration

**Groups**: Technical (5-7), Domain (3-5), Strategic (2-3) = 11-15 experts

**Template**:

`````markdown
## L4 Comprehensive Review
**Decision**: [Detailed description]
**Impact Scope**: [Systems, teams, users]
**Timeline**: [Deadline]

### Committee Composition
| Category | Experts |
|----------|---------|
| Technical | [List 5-7] |
| Domain | [List 3-5] |
| Strategic | [List 2-3] |

### Full Angle Assessment (31 angles: A-H)
| Category | Angles | Avg Score |
|----------|--------|:---------:|
| A. Functional (3) | A1-A3 | X/5 |
| B. Reliability (4) | B1-B4 | X/5 |
| C. Performance (3) | C1-C3 | X/5 |
| D. Maintainability (5) | D1-D5 | X/5 |
| E. Portability (3) | E1-E3 | X/5 |
| F. Security (5) | F1-F5 | X/5 |
| G. Compatibility (2) | G1-G2 | X/5 |
| H. Usability (6) | H1-H6 | X/5 |

### Weighted Scoring
| Dimension | Score | Weight | Weighted |
|-----------|:-----:|:------:|:--------:|
| Technical | X/100 | 40% | X |
| Business | X/100 | 35% | X |
| Process | X/100 | 25% | X |
| **Final** | | | **X/100** |

### Dissenting Opinions
| Expert | Concern | Mitigation |
|--------|---------|------------|
| [Role] | [Issue] | [If proceeding] |

**Verdict**: [Approve/Conditional/Major Revision/Reject]
**Confidence**: [High/Medium/Low]
**Implementation**: Phase 1 → Phase 2 → Validation
`````

---

## 6. L5: Full Committee

**Use for**: Platform change, security overhaul, strategic pivot

**Groups**: Technical (6-8), Domain (5-7), Strategic (5-8) = 16-23 experts

**Template**:

`````markdown
## L5 Full Committee Review
**Decision**: [Strategic decision]
**Impact**: [Org-wide implications]
**Urgency**: [Critical/High/Medium]
**Date**: [YYYY-MM-DD]

### Committee Composition (16-23 experts)
| Category | Count | Experts |
|----------|:-----:|---------|
| Technical | 6-8 | [List] |
| Domain | 5-7 | [List] |
| Strategic | 5-8 | [List] |

### Group Assessments
| Group | Approval | Score | Key Concerns | Conditions |
|-------|:--------:|:-----:|--------------|------------|
| Technical | Yes/No | X/100 | | |
| Domain | Yes/No | X/100 | | |
| Strategic | Yes/No | X/100 | | |

### Consensus Level
| Level | Requirement | Status |
|-------|-------------|:------:|
| Unanimous | 3/3 groups approve | ✓/✗ |
| Strong | 2/3 groups approve | ✓/✗ |
| Conditional | 2/3 with conditions | ✓/✗ |

### Final Decision
**Verdict**: [Approved/Conditional/Rejected]
**Score**: [X/100]
**Confidence**: [X%]
**Binding Conditions**: [Must-meet items]

### Post-Decision
- [ ] Document rationale
- [ ] Communicate to stakeholders
- [ ] Set review checkpoints
- [ ] Prepare rollback plan
`````

---

## 7. Analysis Templates

### 7.1 Role Switching Syntax

`````markdown
[Architect] From architecture perspective...
[Security] Security concerns include...
[Synthesis] Combining all perspectives...
`````

### 7.2 Per-Expert Analysis

`````markdown
**Role**: [Expert name]
**Domain**: [Build/Run/Secure/Data/Product/Strategy]
**Assigned Angles**: [List of angle IDs]

| Angle | Score | Assessment |
|-------|:-----:|------------|
| A1 Correctness | 1-5 | [Brief note] |

**Key Concerns**: [Main issues from this perspective]
**Recommendation**: [Approve/Conditional/Reject]
**Confidence**: [High/Medium/Low]
`````

---

## 8. Usage Tips

| Tip | Description |
|-----|-------------|
| **Start Low** | Begin at L1, escalate if complexity emerges |
| **Time-Box** | Set strict time limits per level |
| **Document** | Capture rationale for future reference |
| **Adjust** | Use dynamic adjustment protocol when needed |
| **Dissent** | Always record dissenting opinions |

> **Dynamic Adjustment**: See `EXPERT_COMMITTEE.md` Section 4.6 for adding/removing experts during analysis.

---

## Related

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Full framework (SSOT)
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert role definitions (23)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (37)
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution

---

*AI Collaboration Knowledge Base*
