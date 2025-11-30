# Expert Committee Quick-Start Guide

> Get started in 5 minutes. No prior knowledge required.

---

## 🚀 5-Minute Quick Start

### Step 1: Determine Committee Level (30 seconds)

| If your decision is... | Use Level |
|------------------------|:---------:|
| Bug fix, config change, easily reversible | **L1** |
| Minor feature, normal complexity | **L2** |
| Refactoring, new technology | **L3** |
| Architecture change, database migration | **L4** |
| Platform change, security overhaul | **L5** |

### Step 2: Assemble Panel (1 minute)

| Level | Who to Include |
|:-----:|----------------|
| L1 | Engineer + QA (2-3 people) |
| L2 | + Architect + PM (4-6 people) |
| L3 | + DevOps + Security (7-10 people) |
| L4 | + Data + Domain experts (11-15 people) |
| L5 | Full committee (16-23 people) |

### Step 3: Collect Independent Scores (2 minutes)

**CRITICAL**: Each expert scores independently (1-5). Do NOT show others' scores!

| Score | Meaning |
|:-----:|---------|
| 5 | Excellent - Proceed |
| 4 | Good - Minor improvements |
| 3 | Acceptable - Address concerns |
| 2 | Poor - Significant changes |
| 1 | Failing - Do not proceed |

### Step 4: Calculate Final Score (1 minute)

**Simple Method v2.1** (no calculator needed):

```
1. Assign weights: High=3, Medium=2, Low=1
2. S = Σ(weight × score) / Σ(weight)
3. Range = max(scores) - min(scores)
4. Dynamic λ: 2-3 experts→1.2, 4-5→0.9, 6-9→0.7, ≥10→0.5
5. S_final = S - λ × Range / 4
```

### Step 5: Make Decision (30 seconds)

| S_final | Range ≤1 | Range ≥2 |
|:-------:|:--------:|:--------:|
| ≥4.0 | ✅ Approve | ⚠️ Discuss |
| 3.5-3.9 | ⚠️ Conditional | 🔄 Revise |
| <3.5 | 🔄 Revise | ❌ Reject |

---

## 📋 Copy-Paste Templates

### Minimal L1 Template

```markdown
## L1 Quick Check
**Decision**: [What are we deciding?]
**Panel**: Engineer, QA

| Expert | Weight | Score |
|--------|:------:|:-----:|
| Engineer | 3 | |
| QA | 2 | |

**S_final**: ___  **Range**: ___
**Verdict**: [Approve / Conditional / Revise / Reject]
```

### Standard L2 Template

```markdown
## L2 Standard Review
**Decision**: [What]
**Context**: [Why]
**Panel**: Architect, Engineer, QA, PM

| Expert | Weight | Score | Concern |
|--------|:------:|:-----:|---------|
| Architect | 3 | | |
| Engineer | 2 | | |
| QA | 2 | | |
| PM | 1 | | |

**Calculation**:
- Sum weights: ___
- Weighted sum: ___
- S = ___ / ___ = ___
- Range = ___ - ___ = ___
- n = ___, λ = ___ (2-3→1.2, 4-5→0.9, 6-9→0.7, ≥10→0.5)
- S_final = ___ - ___ × ___ / 4 = ___

**Decision Check**:
- [ ] S_final > 3.5?
- [ ] Range < 3?
- [ ] Devil's advocate heard?

**Verdict**: ___
**Conditions**: ___
**Next Steps**: ___
```

---

## 🎯 Common Scenarios

### Scenario A: Bug Fix Review

```
Level: L1
Panel: Engineer (High=3), QA (Medium=2)
Scores: 5, 4
S = (3×5 + 2×4) / 5 = 23/5 = 4.6
Range = 1, n = 2, λ = 1.2
Penalty = 1.2 × 1 / 4 = 0.3
S_final = 4.3 → ✅ Strong Approve
```

### Scenario B: New Feature

```
Level: L2
Panel: Architect(3), Engineer(2), QA(2), PM(1)
Scores: 4, 4, 3, 4
S = (12+8+6+4) / 8 = 30/8 = 3.75
Range = 1, n = 4, λ = 0.9
Penalty = 0.9 × 1 / 4 = 0.225
S_final = 3.53 → ⚠️ Conditional Approve
```

### Scenario C: Architecture Change

```
Level: L3
Panel: 8 experts
Scores: 4,4,3,4,3,4,2,4
S = 3.5 (weighted)
Range = 2, n = 8, λ = 0.7
Penalty = 0.7 × 2 / 4 = 0.35
S_final = 3.15 → 🔄 Revise needed
Key concern: Security expert scored 2
```

---

## ⚡ One-Page Cheat Sheet

```
┌─────────────────────────────────────────────────────────┐
│         EXPERT COMMITTEE CHEAT SHEET v2.1               │
├─────────────────────────────────────────────────────────┤
│  LEVEL SELECTION:                                       │
│  • Easy to undo? → L1-L2                                │
│  • Cross-team impact? → L3+                             │
│  • Security/compliance? → L4+                           │
│  • Strategic/org-wide? → L5                             │
├─────────────────────────────────────────────────────────┤
│  WEIGHT TIERS:                                          │
│  • Primary expert in domain → High (3)                  │
│  • Related expertise → Medium (2)                       │
│  • General input → Low (1)                              │
├─────────────────────────────────────────────────────────┤
│  DYNAMIC λ:                                             │
│  • n=2-3 → λ=1.2                                        │
│  • n=4-5 → λ=0.9                                        │
│  • n=6-9 → λ=0.7                                        │
│  • n≥10  → λ=0.5                                        │
├─────────────────────────────────────────────────────────┤
│  FORMULA:                                               │
│  S_final = (Σ weight×score / Σ weight) - λ×Range/4      │
├─────────────────────────────────────────────────────────┤
│  QUICK DECISION:                                        │
│  • S≥4.0 + Range≤1 → Approve                            │
│  • S≥3.5 + Range≤1 → Conditional                        │
│  • S<3.0 or Range≥3 → Reject/Discuss                    │
├─────────────────────────────────────────────────────────┤
│  MUST-DO CHECKLIST:                                     │
│  □ Independent scoring (no peeking!)                    │
│  □ Look up dynamic λ for your expert count              │
│  □ Calculate penalty: λ × Range / 4                     │
│  □ Record at least 1 dissenting opinion                 │
│  □ Document the decision                                │
└─────────────────────────────────────────────────────────┘
```

---

## 🔍 Troubleshooting

| Problem | Solution |
|---------|----------|
| Experts can't agree | Check if level is high enough; add more experts |
| Range ≥ 3 | Significant divergence - discuss before deciding |
| Not sure about weights | Use role-domain matrix in CONFLICT_RESOLUTION.md |
| Need more precision | Use full formula in EXPERT_COMMITTEE.md §6-7 |
| Complex decision | Escalate to higher committee level |

---

## 📚 Learn More

| Topic | Reference |
|-------|-----------|
| Full framework | `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` |
| Detailed templates | `.knowledge/templates/EXPERT_COMMITTEE.md` |
| Weight matrices | `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` |
| Expert roles | `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` |
| Quality angles | `.knowledge/frameworks/patterns/DECISION.md` |

---

## ✅ Pre-Decision Checklist

```markdown
□ Committee level selected?
□ Panel assembled (right experts)?
□ Independent scoring completed?
□ Dynamic λ looked up for expert count?
□ Penalty calculated (λ × Range / 4)?
□ Decision matrix consulted?
□ Dissenting opinion recorded?
□ Next steps documented?
```

---

*Expert Committee Quick-Start Guide v2.1*
