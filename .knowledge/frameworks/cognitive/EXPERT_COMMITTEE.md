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
- [8. Bias Correction](#8-bias-correction)
- [9. Dynamic Weight Learning](#9-dynamic-weight-learning)
- [10. Decision Effectiveness Tracking](#10-decision-effectiveness-tracking)
- [11. Quick Reference](#11-quick-reference)
- [12. No-Calculator Simplified Method](#12-no-calculator-simplified-method)

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

### 6.1 Basic Formula (Original)

```
S = Σ(wᵢ × sᵢ) / Σwᵢ
```

### 6.2 Enhanced Formula (Required)

```
S_enhanced = S_weighted - λ(n) × σ_corrected

Where:
- S_weighted = Σ(wᵢ × sᵢ) / Σwᵢ           (weighted mean)
- σ_biased = √[Σwᵢ(sᵢ - S)² / Σwᵢ]        (biased weighted std dev)
- σ_corrected = σ_biased × √(n/(n-1))     (Bessel correction)
- λ(n) = lookup from table below          (dynamic penalty coefficient)
```

### 6.3 Dynamic λ(n) Lookup Table

| n (experts) | λ(n) | No-Calculator λ |
|:-----------:|:----:|:---------------:|
| 2-3 | 1.2 | 1.2 |
| 4-5 | 0.9 | 0.9 |
| 6-9 | 0.7 | 0.7 |
| 10-14 | 0.6 | 0.6 |
| 15-19 | 0.5 | 0.5 |
| ≥20 | 0.4 | 0.4 |

**Rationale**: Smaller samples have higher uncertainty; larger λ provides more conservative estimates.

### 6.4 Bessel Correction Factor Table

| n (experts) | Factor √(n/(n-1)) | No-Calculator |
|:-----------:|:-----------------:|:-------------:|
| 2-3 | 1.3 | 1.3 |
| 4-5 | 1.15 | 1.15 |
| 6-10 | 1.1 | 1.1 |
| 11-15 | 1.05 | 1.05 |
| ≥16 | 1.0 | 1.0 |

**Rationale**: Corrects for bias in sample standard deviation estimation.

### 6.5 Calculation Example

**Scenario**: L2 decision, 4 experts

| Expert | Weight | Score |
|--------|--------|-------|
| Architect | 0.9 | 4 |
| Engineer | 0.7 | 4 |
| QA | 0.7 | 3 |
| PM | 0.3 | 5 |

**Step 1: Weighted Mean**
```
S = (0.9×4 + 0.7×4 + 0.7×3 + 0.3×5) / (0.9+0.7+0.7+0.3)
  = (3.6 + 2.8 + 2.1 + 1.5) / 2.6
  = 10.0 / 2.6 = 3.85
```

**Step 2: Weighted StdDev with Bessel Correction**
```
σ_biased = √[(0.9×0.02 + 0.7×0.02 + 0.7×0.72 + 0.3×1.32) / 2.6]
         = √[0.90 / 2.6] = 0.59

n = 4, Bessel factor = 1.15 (from table 6.4)
σ_corrected = 0.59 × 1.15 = 0.68
```

**Step 3: Enhanced Score with Dynamic λ**
```
n = 4, λ(4) = 0.9 (from table 6.3)
S_enhanced = 3.85 - 0.9 × 0.68 = 3.24
```

**Interpretation**: With corrected formulas, score is more conservative (3.24 vs 3.55 old method), better reflecting small-sample uncertainty.

### 6.6 Divergence Reference Table

| Corrected σ | Interpretation | Typical Penalty Range |
|-------------|----------------|----------------------|
| 0 - 0.3 | High consensus | Low |
| 0.3 - 0.6 | Minor divergence | Moderate |
| 0.6 - 1.0 | Moderate divergence | Significant |
| 1.0 - 1.5 | Significant divergence | High |
| > 1.5 | Severe divergence | Very High |

> **Note**: Actual penalty depends on λ(n). Use `Penalty = λ(n) × σ_corrected`.

---

## 7. Uncertainty Quantification

### 7.1 Confidence Interval (Corrected)

**Formula**:
```
CI_95% = [S_enhanced - t(n-1) × SE_corrected, S_enhanced + t(n-1) × SE_corrected]

Where:
- SE_basic = σ_corrected / √n
- SE_corrected = SE_basic × √(1 + (n-1) × ρ)   (correlation correction)
- t(n-1) = t-distribution value for df = n-1   (replaces z=1.96)
- ρ = estimated correlation between experts    (from domain composition)
```

### 7.2 t-Distribution Lookup Table (95% CI)

| n (experts) | df | t_{0.975} | No-Calculator |
|:-----------:|:--:|:---------:|:-------------:|
| 2 | 1 | 12.71 | 12.7 |
| 3 | 2 | 4.30 | 4.3 |
| 4 | 3 | 3.18 | 3.2 |
| 5 | 4 | 2.78 | 2.8 |
| 6 | 5 | 2.57 | 2.6 |
| 7 | 6 | 2.45 | 2.5 |
| 8 | 7 | 2.36 | 2.4 |
| 10 | 9 | 2.26 | 2.3 |
| 15 | 14 | 2.14 | 2.1 |
| 20 | 19 | 2.09 | 2.1 |
| ≥25 | 24+ | ~2.0 | 2.0 |

**No-Calculator Simplified**:

| n | Use t = |
|---|:-------:|
| 2-3 | 4.0 |
| 4-5 | 3.0 |
| 6-9 | 2.4 |
| 10-14 | 2.2 |
| 15-19 | 2.1 |
| ≥20 | 2.0 |

### 7.3 Correlation Estimation Table

| Domain Composition | Estimated ρ | SE Multiplier √(1+(n-1)ρ) for n=10 |
|--------------------|:-----------:|:----------------------------------:|
| All different domains | 0.05 | 1.2 |
| 25% same domain | 0.10 | 1.4 |
| 50% same domain | 0.15 | 1.6 |
| 75% same domain | 0.25 | 1.8 |
| All same domain | 0.35 | 2.1 |

**No-Calculator Simplified**:
| Composition | SE × |
|-------------|:----:|
| Mixed domains | 1.3 |
| Majority same domain | 1.7 |
| All same domain | 2.0 |

### 7.4 Calculation Example (continued from 6.5)

```
From Section 6.5: S_enhanced = 3.24, σ_corrected = 0.68, n = 4

Step 1: Basic SE
SE_basic = 0.68 / √4 = 0.34

Step 2: Correlation Correction (assume mixed domains, ρ ≈ 0.10)
SE_corrected = 0.34 × √(1 + 3×0.10) = 0.34 × 1.14 = 0.39

Step 3: t-Distribution CI (n=4, t=3.18)
CI_95% = [3.24 - 3.18×0.39, 3.24 + 3.18×0.39]
       = [3.24 - 1.24, 3.24 + 1.24]
       = [2.00, 4.48]
```

**Comparison with old method**:
| Method | CI_95% | CI Width |
|--------|--------|:--------:|
| Old (z=1.96, no corrections) | [2.97, 4.13] | 1.16 |
| **New (t-dist, corrected)** | [2.00, 4.48] | 2.48 |

> **Interpretation**: Corrected CI is wider, honestly reflecting small-sample uncertainty.

### 7.5 Enhanced Decision Rules

| Condition | Decision | Action |
|-----------|----------|--------|
| CI_lower > 3.5 | **Strong Approve** | Proceed confidently |
| S > 3.5 AND CI_lower > 2.5 | **Conditional Approve** | Proceed with monitoring |
| CI_upper < 2.5 | **Strong Reject** | Do not proceed |
| CI_width > 2.0 | **Need More Info** | Add experts or discuss |
| Other | **Revise** | Re-evaluate after changes |

### 7.6 Information Sufficiency (IS)

```
IS = max(0, 1 - (CI_width / 4))    # Lower bound at 0

IS > 0.7   → Information sufficient
IS 0.5-0.7 → Basically sufficient
IS < 0.5   → Insufficient, add more experts
IS = 0     → Extreme uncertainty, defer decision
```

**Example** (continued from 7.4):
```
CI_width = 4.48 - 2.00 = 2.48
IS = max(0, 1 - (2.48 / 4)) = max(0, 0.38) = 0.38
→ Insufficient information, add more experts or discuss
```

> **Note**: With corrected formulas, small samples often yield IS < 0.5, correctly signaling need for more experts.

---

## 8. Bias Correction

### 8.1 Three-Step Debiasing Process

```text
Step 1: Independent Scoring (prevents anchoring)
        ↓
Step 2: Anonymous Aggregation (prevents conformity)
        ↓
Step 3: Open Discussion (information sharing)
```

### 8.2 Implementation Requirements

| Phase | Requirement | Reason |
|-------|-------------|--------|
| **Independent Scoring** | Each expert scores without seeing others | Prevent anchoring effect |
| **Anonymous Aggregation** | Show statistics first, not who scored what | Prevent authority suppression |
| **Open Discussion** | Discuss divergence points, allow score revision | Full information sharing |

### 8.3 Random Speaking Order

```python
# Randomize expert speaking order for each decision
import random
experts = ["Architect", "Engineer", "QA", "PM", ...]
random.shuffle(experts)  # Randomize
```

### 8.4 Devil's Advocate Requirements

Each decision **MUST** include:

| Requirement | Count | Assignment Method |
|-------------|-------|-------------------|
| Dissenting opinion | ≥1 | Rotate or assign Risk role |
| Risk enumeration | ≥3 | Each expert contributes ≥1 |
| Alternative approach | ≥1 | Lowest-scoring expert proposes |

---

## 9. Dynamic Weight Learning

### 9.1 Lightweight Implementation

Simple **sliding window accuracy** instead of complex Bayesian updates:

```
Dynamic Weight = Base Weight × Accuracy Adjustment

Accuracy Adjustment = (Correct in last 10 decisions + 5) / 15
```

### 9.2 Example

| Expert | Base Weight | Last 10 Correct | Adjustment | Dynamic Weight |
|--------|-------------|-----------------|------------|----------------|
| Architect | 0.9 | 8 | (8+5)/15=0.87 | 0.78 |
| Engineer | 0.7 | 9 | (9+5)/15=0.93 | 0.65 |
| QA | 0.7 | 10 | (10+5)/15=1.0 | 0.70 |

### 9.3 Cold Start Handling

New experts or new domains: Use base weight, start adjusting after 5 accumulated decisions.

---

## 10. Decision Effectiveness Tracking

### 10.1 Post-Decision Review

| Checkpoint | Timing | Question |
|------------|--------|----------|
| **Immediate** | 1 week | Was implementation smooth? |
| **Short-term** | 1 month | Did expected benefits materialize? |
| **Long-term** | 3 months | Was the decision correct? |

### 10.2 Effectiveness Metrics

| Metric | Formula | Target |
|--------|---------|:------:|
| Decision Accuracy | Correct / Total | >85% |
| Prediction Error | \|Predicted - Actual\| | <20% |
| Reversal Rate | Reversed / Total | <10% |
| Calibration | CI coverage rate | >90% |

### 10.3 Feedback Loop

```text
1. RECORD   → Document decision with predictions
2. SCHEDULE → Set review checkpoints
3. COMPARE  → Actual vs predicted outcomes
4. LEARN    → Update weights if systematic errors
```

### 10.4 Review Template

| Item | Predicted | Actual | Delta | Lesson |
|------|-----------|--------|:-----:|--------|
| Outcome | | | | |
| Timeline | | | | |
| Risk Events | | | | |
| User Impact | | | | |

### 10.5 Continuous Improvement

| Signal | Action |
|--------|--------|
| Accuracy <85% | Review angle coverage |
| Prediction Error >20% | Calibrate expert weights |
| Reversal Rate >10% | Increase committee level |
| CI coverage <90% | Adjust λ parameter |
| Systematic bias | Add/remove expert roles |

---

## 11. Quick Reference

### 11.1 Level Selection Guide

| Question | L1 | L2 | L3 | L4 | L5 |
|----------|:--:|:--:|:--:|:--:|:--:|
| Can we easily undo? | ✓ | ✓ | · | · | · |
| Affects only 1 team? | ✓ | ✓ | · | · | · |
| Low security risk? | ✓ | ✓ | ✓ | · | · |
| Under $10K impact? | ✓ | ✓ | ✓ | · | · |
| Reversible in <1 day? | ✓ | ✓ | · | · | · |

### 11.2 Domain Selection by Problem

| Problem | Primary Domains |
|---------|-----------------|
| Architecture | Build, Strategy |
| Feature | Build, Product |
| Security | Secure, Run |
| Performance | Run, Build |
| Data | Data, Secure |
| Operations | Run |

### 11.3 Summary Statistics

| Metric | Value |
|--------|-------|
| Expert Domains | 6 |
| Expert Roles | 23 |
| Angle Categories | 10 |
| Quality Angles | 37 |
| Committee Levels | 5 |
| Max Matrix Size | 23 × 37 = 851 |

### 11.4 Quick Enhancement Checklist

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

## 12. No-Calculator Simplified Method

> For situations where calculators or spreadsheets are unavailable. Accuracy: ~90% of full method.

### 12.1 Simplified Weight System

Replace decimal weights with integer tiers:

| Original Weight | Simplified Tier | Multiplier |
|-----------------|-----------------|:----------:|
| 0.9 (Primary expertise) | **High** | 3 |
| 0.6-0.7 (Secondary) | **Medium** | 2 |
| 0.2-0.5 (Minimal) | **Low** | 1 |

### 12.2 Quick Score Calculation

**Step 1**: Assign tier multipliers and collect scores

| Expert | Tier | Score |
|--------|:----:|:-----:|
| Expert A | 3 | sₐ |
| Expert B | 2 | sᵦ |
| Expert C | 1 | sᵧ |

**Step 2**: Calculate weighted average (integer math)

```
S = (3×sₐ + 2×sᵦ + 1×sᵧ) / (3+2+1)
```

**Step 3**: Calculate divergence penalty (with dynamic λ)

```
Range = max(scores) - min(scores)
λ = lookup from simplified table below
Penalty = λ × Range / 4
S_final = S - Penalty
```

**Simplified λ(n) for No-Calculator**:
| n (experts) | λ |
|:-----------:|:-:|
| 2-3 | 1.2 |
| 4-5 | 0.9 |
| 6-9 | 0.7 |
| ≥10 | 0.5 |

### 12.3 Range-Based Divergence Table

| Score Range | σ Approximation | Penalty (÷5) | Interpretation |
|:-----------:|:---------------:|:------------:|----------------|
| 0 | ~0 | 0 | Perfect consensus |
| 1 | ~0.4 | 0.2 | Minor divergence |
| 2 | ~0.8 | 0.4 | Moderate divergence |
| 3 | ~1.2 | 0.6 | Significant divergence |
| 4 | ~1.6 | 0.8 | Severe divergence |

### 12.4 Quick Decision Matrix

| S_final | Range ≤1 | Range = 2 | Range ≥3 |
|:--------|:---------|:----------|:---------|
| **≥4.0** | ✅ Strong Approve | ⚠️ Conditional | 🔄 Discuss First |
| **3.5-3.9** | ⚠️ Conditional | 🔄 Revise | 🔄 Revise |
| **3.0-3.4** | 🔄 Revise | 🔄 Revise | ❌ Reject |
| **<3.0** | ❌ Reject | ❌ Reject | ❌ Reject |

### 12.5 Information Sufficiency Quick Check

| Expert Count | Range ≤1 | Range = 2 | Range ≥3 |
|:-------------|:---------|:----------|:---------|
| **≥5** | ✅ Sufficient | ✅ Sufficient | ⚠️ Borderline |
| **3-4** | ✅ Sufficient | ⚠️ Borderline | ❌ Insufficient |
| **2** | ⚠️ Borderline | ❌ Insufficient | ❌ Insufficient |

### 12.6 √n Lookup Table (for CI calculation if needed)

| n (experts) | √n | 2/√n (CI factor) |
|:-----------:|:--:|:----------------:|
| 2 | 1.4 | 1.4 |
| 3 | 1.7 | 1.2 |
| 4 | 2.0 | 1.0 |
| 5 | 2.2 | 0.9 |
| 6 | 2.4 | 0.8 |
| 8 | 2.8 | 0.7 |
| 10 | 3.2 | 0.6 |
| 15 | 3.9 | 0.5 |
| 20 | 4.5 | 0.4 |

**Simplified CI**: `CI ≈ [S_final - Factor×Range/2, S_final + Factor×Range/2]`

### 12.7 Complete No-Calculator Example

**Scenario**: L2 decision with 4 experts

| Expert | Tier | Score |
|--------|:----:|:-----:|
| Architect | 3 | 4 |
| Engineer | 2 | 4 |
| QA | 2 | 3 |
| PM | 1 | 5 |

**Calculation**:
```
Sum of weights = 3 + 2 + 2 + 1 = 8
Weighted sum = 3×4 + 2×4 + 2×3 + 1×5 = 12 + 8 + 6 + 5 = 31
S = 31 / 8 = 3.875 ≈ 3.9

Range = 5 - 3 = 2
n = 4, λ = 0.9 (from simplified table)
Penalty = 0.9 × 2 / 4 = 0.45
S_final = 3.9 - 0.45 = 3.45

Decision: S_final=3.45, Range=2 → "Revise" (from matrix)
Info Sufficiency: 4 experts, Range=2 → "Borderline"
```

**Compare to full method**: S_enhanced=3.24, reasonably close!

### 12.8 One-Page Cheat Sheet

```
┌─────────────────────────────────────────────────────┐
│  NO-CALCULATOR EXPERT COMMITTEE CHEAT SHEET v2.2    │
├─────────────────────────────────────────────────────┤
│  1. WEIGHTS: High=3, Medium=2, Low=1                │
│  2. AVERAGE: S = Σ(tier×score) / Σ(tier)            │
│  3. DYNAMIC λ: 2-3 experts→1.2, 4-5→0.9, 6-9→0.7,   │
│                ≥10→0.5                              │
│  4. PENALTY: λ × Range / 4                          │
│  5. FINAL: S_final = S - Penalty                    │
├─────────────────────────────────────────────────────┤
│  QUICK DECISION:                                    │
│  • S≥4 + Range≤1 → Approve                          │
│  • S≥3.5 + Range≤1 → Conditional                    │
│  • S<3 or Range≥3 → Reject/Discuss                  │
├─────────────────────────────────────────────────────┤
│  INFO CHECK:                                        │
│  • ≥5 experts + Range≤2 → Sufficient                │
│  • 3-4 experts + Range≤1 → Sufficient               │
│  • Otherwise → Add more experts                     │
├─────────────────────────────────────────────────────┤
│  CI QUICK (if needed):                              │
│  • t-value: n≤3→4, n=4-5→3, n=6-9→2.4, n≥10→2.2     │
│  • CI ≈ S ± t × Range / (2×√n)                      │
└─────────────────────────────────────────────────────┘
```

---

## Related

- `.knowledge/templates/EXPERT_COMMITTEE_QUICKSTART.md` — **Quick-Start Guide (5 min)**
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert roles (SSOT)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution
- `.knowledge/guidelines/COGNITIVE.md` — Cognitive guidelines

---

*Expert Committee Framework v2.2*
