# Expert Committee Framework

> Multi-perspective analysis using 6 domains × 23 roles × 10 categories × 37 angles

---

## Table of Contents

- [0. Quick Start](#0-quick-start)
- [1. First Principles](#1-first-principles)
- [2. Framework Overview](#2-framework-overview)
- [3. Committee Levels](#3-committee-levels)
- [4. Dynamic Activation](#4-dynamic-activation)
- [5. Analysis Process](#5-analysis-process)
- [6. Enhanced Aggregation](#6-enhanced-aggregation)
- [7. Uncertainty Quantification](#7-uncertainty-quantification)
- [8. Bias Correction & Calibration](#8-bias-correction--calibration)
- [9. Quick Reference](#9-quick-reference)
- [10. No-Calculator Simplified Method](#10-no-calculator-simplified-method)

### Module Files

| Module | Content |
|--------|---------|
| `EXPERT_COMMITTEE_MATH.md` | Aggregation formulas, uncertainty quantification |
| `EXPERT_COMMITTEE_CALIBRATION.md` | Bias correction, weight learning, effectiveness tracking |
| `practices/.../EXPERT_COMMITTEE_SIMPLIFIED.md` | No-calculator method (full details) |

---

## 0. Quick Start

### 30-Second Decision Flow

```text
1. ASSESS RISK    → Select Level (L1-L5)
2. ACTIVATE       → Choose experts by problem domain
3. INDEPENDENT    → Each expert scores independently (防锚定)
4. AGGREGATE      → Enhanced formula: S_enhanced = S - λσ
5. QUANTIFY       → Output confidence interval + information sufficiency
6. DECIDE         → Use enhanced decision rules
7. DOCUMENT       → Use template from templates/EXPERT_COMMITTEE.md
```

### Level Quick Reference

| Problem Type | Level | Experts | Time |
|--------------|:-----:|:-------:|------|
| Bug fix, config | L1 | 2-3 | 15min |
| Minor feature, API | L2 | 4-6 | 30min |
| Refactor, new tech | L3 | 7-10 | 1h |
| Architecture, DB | L4 | 11-15 | 2-3h |
| Platform, security | L5 | 16-23 | Half day |

### Minimal Example (L1)

```markdown
**Decision**: Fix login button bug
**Panel**: Engineer, QA
**Angles**: A1 Correctness, D3 Clarity, D5 Testability
**Scores**: 5, 4, 5 → S=4.7, σ=0.47, S_enhanced=4.47
**CI_95%**: [4.0, 4.9]
**Verdict**: Strong Approve (CI_lower > 3.5)
```

> Templates at `templates/EXPERT_COMMITTEE.md`

---

## 1. First Principles

### 1.1 Why Expert Committee?

| Problem | Solution |
|---------|----------|
| Single perspective → blind spots | Multiple expert viewpoints |
| Ad-hoc quality checks | Structured angle evaluation |
| Static team composition | Dynamic activation by need |
| Overconfident decisions | Uncertainty quantification |
| Cognitive biases | Structural debiasing |

### 1.2 Core Philosophy

| Principle | Application |
|-----------|-------------|
| **信 (Faithfulness)** | Correctness before elegance |
| **MECE** | Mutually exclusive, collectively exhaustive |
| **Dynamic** | Activate experts and angles on-demand |
| **Traceability** | Document all decisions and dissent |
| **Calibrated** | Output uncertainty, not just point estimates |

### 1.3 What This Framework Does

```text
Problem → Select Level → Activate Experts → Independent Scoring → 
Enhanced Aggregation → Uncertainty Quantification → Decide → Document → Feedback
```

---

## 2. Framework Overview

### 2.1 Component Summary

| Component | Count | Source (SSOT) |
|-----------|-------|---------------|
| Expert Domains | 6 | `ROLE_PERSONA.md` |
| Expert Roles | 23 | `ROLE_PERSONA.md` |
| Angle Categories | 10 | `DECISION.md` |
| Quality Angles | 37 | `DECISION.md` |
| Committee Levels | 5 | This document |

### 2.2 Expert Domains (6)

| Domain | Roles | Core Question |
|--------|-------|---------------|
| **Build** | 5 | How to implement correctly? |
| **Run** | 4 | How to operate reliably? |
| **Secure** | 3 | How to protect? |
| **Data** | 3 | How to manage data? |
| **Product** | 4 | How to satisfy users? |
| **Strategy** | 4 | How to create value? |

> Full details: `ROLE_PERSONA.md` Section 2-3

### 2.3 Angle Categories (10)

| Cat | Name | Angles | Core Question |
|-----|------|--------|---------------|
| A | Functional | 3 | Does it work correctly? |
| B | Reliability | 4 | Does it work consistently? |
| C | Performance | 3 | Is it fast enough? |
| D | Maintainability | 5 | Is it easy to change? |
| E | Portability | 3 | Can it be moved? |
| F | Security | 5 | Is it protected? |
| G | Compatibility | 2 | Does it integrate? |
| H | Usability | 6 | Is it user-friendly? |
| I | Data Quality | 3 | Is data trustworthy? |
| J | AI/ML Quality | 3 | Is AI reliable? |

> Full details: `DECISION.md` Section 2

---

## 3. Committee Levels

### 3.1 Level Definitions

| Level | Name | Experts | Angles | Time | Use Case |
|-------|------|---------|--------|------|----------|
| **L1** | Quick Check | 2-3 | 3 | 15 min | Low-risk, routine |
| **L2** | Standard | 4-6 | 12 | 30 min | Normal complexity |
| **L3** | Deep Analysis | 7-10 | 23 | 1 hour | Major changes |
| **L4** | Comprehensive | 11-15 | 31 | 2-3 hours | Critical decisions |
| **L5** | Full Committee | 16-23 | 37 | Half day | Strategic, org-wide |

### 3.2 Problem Type → Level Mapping

| Problem Type | Level | Rationale |
|--------------|:-----:|-----------|
| Bug fix (isolated) | L1 | Low risk, easily reversible |
| Config change | L1 | Routine, single team |
| Minor feature | L2 | Normal complexity |
| API change (compatible) | L2 | Cross-team coordination |
| Significant refactoring | L3 | High impact, hard to reverse |
| New technology adoption | L3 | Department-wide impact |
| Architecture change | L4 | Critical, cross-department |
| Database migration | L4 | Very hard to reverse |
| Platform change | L5 | Strategic, org-wide |
| Security overhaul | L5 | Irreversible implications |

### 3.3 Level Selection Criteria

| Factor | L1 | L2 | L3 | L4 | L5 |
|--------|:--:|:--:|:--:|:--:|:--:|
| Risk | Low | Medium | High | Critical | Strategic |
| Reversibility | Easy | Moderate | Hard | Very Hard | Irreversible |
| Impact scope | 1 team | 2-3 teams | Department | Cross-dept | Org-wide |
| Stakeholders | 1-2 | 3-5 | 6-10 | 10-20 | 20+ |
| Cost impact | <$1K | $1K-$10K | $10K-$100K | $100K-$1M | >$1M |

### 3.4 Default Composition by Level

| Level | Build | Run | Secure | Data | Product | Strategy | Total |
|-------|:-----:|:---:|:------:|:----:|:-------:|:--------:|:-----:|
| L1 | 2-3 | - | - | - | - | - | 2-3 |
| L2 | 2-3 | 2 | - | - | 1 | - | 4-6 |
| L3 | 3-4 | 2-3 | 1-2 | 1 | 1-2 | - | 7-10 |
| L4 | 4 | 3 | 2 | 2 | 3 | 1 | 11-15 |
| L5 | 5 | 4 | 3 | 3 | 4 | 4 | 16-23 |

### 3.5 Default Angles by Level

| Level | Categories | Angles |
|-------|------------|--------|
| **L1** | A | A1-A3 (3) |
| **L2** | A, B, D | A1-A3, B1-B4, D1-D5 (12) |
| **L3** | A-F | A-F all (23) |
| **L4** | A-H | A-H all (31) |
| **L5** | A-J | All 37 |

### 3.6 Level Adjustment Factors

Higher committee levels require enhanced weight precision for critical decisions.

| Level | Factor | Effect | Rationale |
|-------|:------:|--------|-----------|
| **L1** | ×1.00 | Baseline | Routine decisions |
| **L2** | ×1.00 | Baseline | Standard decisions |
| **L3** | ×1.05 | +5% | Major changes need higher precision |
| **L4** | ×1.10 | +10% | Critical decisions amplify expert weight |
| **L5** | ×1.15 | +15% | Strategic decisions maximize expert influence |

**Application Formula**:

```text
W_adjusted = W_total × Level_Factor

Where:
  W_total = 0.4 × W_domain + 0.6 × W_angle
  Level_Factor = {1.00, 1.00, 1.05, 1.10, 1.15} for L1-L5
```

**Example** (L4, Architect evaluating D1 in Build domain):

```text
W_domain = 0.9 (Architect-Build)
W_angle = 0.88 (Architect-D1, Primary)
W_total = 0.4 × 0.9 + 0.6 × 0.88 = 0.36 + 0.528 = 0.888
W_adjusted = 0.888 × 1.10 = 0.977
```

> **SSOT**: Weight values defined in `CONFLICT_RESOLUTION.md` Section 4.7

---

## 4. Dynamic Activation

### 4.1 Expert Activation Protocol

```text
1. IDENTIFY  → Determine problem type and initial level
2. SELECT    → Choose domains based on problem type
3. COMPOSE   → Select specific roles from chosen domains
4. BRIEF     → Present problem with context
5. ADJUST    → Add/remove experts as analysis proceeds
6. DOCUMENT  → Record final composition and rationale
```

### 4.2 Angle Activation Protocol

```text
1. START     → Begin with level-default angles
2. ASSESS    → Evaluate initial findings
3. EXPAND    → Add categories if new concerns emerge
4. FOCUS     → Remove irrelevant angles to save effort
5. COMPLETE  → Ensure minimum coverage maintained
```

### 4.3 Activation Triggers

| Trigger | Expert Action | Angle Action |
|---------|---------------|--------------|
| Security concern | +Security, +Compliance | +F (Security) |
| Performance issue | +SRE, +DBA | +C (Performance) |
| User feedback | +UX, +Support | +H (Usability) |
| Data problem | +Data Eng, +Analyst | +I (Data Quality) |
| AI involved | +ML Eng | +J (AI/ML) |
| Strategic impact | +CTO, +Cost | +All relevant |

### 4.4 Constraints

| Rule | Expert | Angle |
|------|--------|-------|
| **Minimum** | 2 (L1) | A1 (Correctness) |
| **Maximum** | 23 (all) | 37 (all) |
| **Always include** | QA or Tech Lead | A1 |
| **Security-sensitive** | Security + Compliance | F1-F5 |
| **User-facing** | UX + PM | H1-H6 |

---

## 5. Analysis Process

### 5.1 Standard Workflow

```text
1. SCOPE      → Define decision + select committee level
2. ASSEMBLE   → Choose experts based on domains
3. ACTIVATE   → Select angles based on level + problem type
4. BRIEF      → Present problem with context
5. INDEPENDENT → Each expert evaluates independently (NO看他人)
6. COLLECT    → Anonymous collection of scores
7. AGGREGATE  → Apply enhanced aggregation formula
8. QUANTIFY   → Calculate confidence interval + IS
9. DISCUSS    → Share perspectives, identify conflicts (AFTER aggregation)
10. RESOLVE   → Apply conflict resolution (see CONFLICT_RESOLUTION.md)
11. DECIDE    → Use enhanced decision rules
12. DOCUMENT  → Record decision + rationale + dissent
```

### 5.2 Scoring Scale

| Score | Meaning | Action |
|:-----:|---------|--------|
| 5 | Excellent | Proceed |
| 4 | Good | Minor improvements |
| 3 | Acceptable | Address concerns |
| 2 | Poor | Significant changes |
| 1 | Failing | Do not proceed |

---

## 6. Enhanced Aggregation

> **Full details**: See `EXPERT_COMMITTEE_MATH.md` §1

### 6.1 Core Formula

```
S_enhanced = S_weighted - λ(n) × σ_corrected
```

### 6.2 Key Tables (Quick Reference)

| n (experts) | λ(n) | Bessel Factor |
|:-----------:|:----:|:-------------:|
| 2-3 | 1.2 | 1.3 |
| 4-5 | 0.9 | 1.15 |
| 6-9 | 0.7 | 1.1 |
| 10-14 | 0.6 | 1.05 |
| ≥15 | 0.5-0.4 | 1.0 |

---

## 7. Uncertainty Quantification

> **Full details**: See `EXPERT_COMMITTEE_MATH.md` §2

### 7.1 Core Formula

```
CI_95% = [S_enhanced - t(n-1) × SE_corrected, S_enhanced + t(n-1) × SE_corrected]
IS = max(0, 1 - (CI_width / 4))
```

### 7.2 Decision Rules

| Condition | Decision | Action |
|-----------|----------|--------|
| CI_lower > 3.5 | **Strong Approve** | Proceed confidently |
| S > 3.5 AND CI_lower > 2.5 | **Conditional Approve** | Proceed with monitoring |
| CI_upper < 2.5 | **Strong Reject** | Do not proceed |
| CI_width > 2.0 | **Need More Info** | Add experts or discuss |
| Other | **Revise** | Re-evaluate after changes |

### 7.3 Information Sufficiency

| IS Value | Interpretation |
|----------|----------------|
| > 0.7 | Information sufficient |
| 0.5-0.7 | Basically sufficient |
| < 0.5 | Insufficient, add more experts |

---

## 8. Bias Correction & Calibration

> **Full details**: See `EXPERT_COMMITTEE_CALIBRATION.md`

### 8.1 Three-Step Debiasing Process

```text
Step 1: Independent Scoring (prevents anchoring)
        ↓
Step 2: Anonymous Aggregation (prevents conformity)
        ↓
Step 3: Open Discussion (information sharing)
```

### 8.2 Devil's Advocate Requirements

| Requirement | Count |
|-------------|-------|
| Dissenting opinion | ≥1 |
| Risk enumeration | ≥3 |
| Alternative approach | ≥1 |

### 8.3 Dynamic Weight Learning

```
Dynamic Weight = Base Weight × (Correct in last 10 + 5) / 15
```

### 8.4 Effectiveness Metrics

| Metric | Target |
|--------|:------:|
| Decision Accuracy | >85% |
| Prediction Error | <20% |
| Reversal Rate | <10% |
| CI coverage rate | >90% |

---

## 9. Quick Reference

### 9.1 Level Selection Guide

| Question | L1 | L2 | L3 | L4 | L5 |
|----------|:--:|:--:|:--:|:--:|:--:|
| Can we easily undo? | ✓ | ✓ | · | · | · |
| Affects only 1 team? | ✓ | ✓ | · | · | · |
| Low security risk? | ✓ | ✓ | ✓ | · | · |
| Under $10K impact? | ✓ | ✓ | ✓ | · | · |
| Reversible in <1 day? | ✓ | ✓ | · | · | · |

### 9.2 Domain Selection by Problem

| Problem | Primary Domains |
|---------|-----------------|
| Architecture | Build, Strategy |
| Feature | Build, Product |
| Security | Secure, Run |
| Performance | Run, Build |
| Data | Data, Secure |
| Operations | Run |

### 9.3 Summary Statistics

| Metric | Value |
|--------|-------|
| Expert Domains | 6 |
| Expert Roles | 23 |
| Angle Categories | 10 |
| Quality Angles | 37 |
| Committee Levels | 5 |
| Max Matrix Size | 23 × 37 = 851 |

### 9.4 Quick Enhancement Checklist

```markdown
□ Independent scoring? (prevents anchoring)
□ Applied Bessel correction to σ? (σ_corrected = σ_biased × factor from §6.4)
□ Used dynamic λ(n) from table §6.3? (not fixed 0.5)
□ Applied divergence penalty? (S_enhanced = S - λ(n) × σ_corrected)
□ Used t-distribution for CI? (not z=1.96, see §7.2)
□ Applied correlation correction to SE? (see §7.3)
□ Output confidence interval? (uncertainty quantification)
□ Information sufficiency > 0.5? (IS = max(0, 1 - CI_width/4))
□ Devil's advocate opinion? (structural debiasing)
```

---

## 10. No-Calculator Simplified Method

> **Full details**: See `.knowledge/practices/decisions/EXPERT_COMMITTEE_SIMPLIFIED.md`

For situations where calculators are unavailable (~90% accuracy of full method).

### 10.1 Quick Formula

```
Weights: High=3, Medium=2, Low=1
S = Σ(tier×score) / Σ(tier)
Penalty = λ × Range / 4
S_final = S - Penalty
```

### 10.2 Quick Decision

| S_final | Range ≤1 | Range ≥2 |
|:--------|:---------|:---------|
| **≥4.0** | ✅ Approve | ⚠️ Discuss |
| **3.5-3.9** | ⚠️ Conditional | 🔄 Revise |
| **<3.5** | 🔄 Revise/❌ Reject | ❌ Reject |

---

## Related

### Module Files (This Framework)

- `EXPERT_COMMITTEE_MATH.md` — Aggregation formulas, uncertainty quantification (full details)
- `EXPERT_COMMITTEE_CALIBRATION.md` — Bias correction, weight learning, effectiveness tracking
- `.knowledge/practices/decisions/EXPERT_COMMITTEE_SIMPLIFIED.md` — No-calculator method (full details)

### Templates & Guides

- `.knowledge/templates/EXPERT_COMMITTEE_QUICKSTART.md` — **Quick-Start Guide (5 min)**
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates

### Reference Documents

- `ROLE_PERSONA.md` — Expert roles (SSOT)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)
- `CONFLICT_RESOLUTION.md` — Conflict resolution
- `.knowledge/guidelines/COGNITIVE.md` — Cognitive guidelines

---

*Expert Committee Framework v2.2 (Modular)*
