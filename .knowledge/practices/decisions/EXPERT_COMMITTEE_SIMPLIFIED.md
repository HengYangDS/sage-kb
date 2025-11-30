# Expert Committee Simplified Method

> No-calculator method for quick expert committee decisions (~90% accuracy)

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Simplified Weight System](#2-simplified-weight-system)
- [3. Quick Score Calculation](#3-quick-score-calculation)
- [4. Decision Tables](#4-decision-tables)
- [5. Complete Example](#5-complete-example)
- [6. One-Page Cheat Sheet](#6-one-page-cheat-sheet)

---

## 1. Overview

For situations where calculators or spreadsheets are unavailable. This method provides approximately 90% accuracy compared to the full mathematical method.

**When to Use**:
- Quick meetings without tools
- Initial screening decisions
- Sanity checks on full calculations

---

## 2. Simplified Weight System

Replace decimal weights with integer tiers:

| Original Weight | Simplified Tier | Multiplier |
|-----------------|-----------------|:----------:|
| 0.9 (Primary expertise) | **High** | 3 |
| 0.6-0.7 (Secondary) | **Medium** | 2 |
| 0.2-0.5 (Minimal) | **Low** | 1 |

---

## 3. Quick Score Calculation

### 3.1 Step 1: Assign Tiers and Collect Scores

| Expert | Tier | Score |
|--------|:----:|:-----:|
| Expert A | 3 | sₐ |
| Expert B | 2 | sᵦ |
| Expert C | 1 | sᵧ |

### 3.2 Step 2: Calculate Weighted Average

```
S = (3×sₐ + 2×sᵦ + 1×sᵧ) / (3+2+1)
```

### 3.3 Step 3: Calculate Divergence Penalty

```
Range = max(scores) - min(scores)
λ = lookup from table below
Penalty = λ × Range / 4
S_final = S - Penalty
```

**Simplified λ(n) Table**:

| n (experts) | λ |
|:-----------:|:-:|
| 2-3 | 1.2 |
| 4-5 | 0.9 |
| 6-9 | 0.7 |
| ≥10 | 0.5 |

### 3.4 Range-Based Divergence Reference

| Score Range | σ Approximation | Penalty (÷5) | Interpretation |
|:-----------:|:---------------:|:------------:|----------------|
| 0 | ~0 | 0 | Perfect consensus |
| 1 | ~0.4 | 0.2 | Minor divergence |
| 2 | ~0.8 | 0.4 | Moderate divergence |
| 3 | ~1.2 | 0.6 | Significant divergence |
| 4 | ~1.6 | 0.8 | Severe divergence |

---

## 4. Decision Tables

### 4.1 Quick Decision Matrix

| S_final | Range ≤1 | Range = 2 | Range ≥3 |
|:--------|:---------|:----------|:---------|
| **≥4.0** | ✅ Strong Approve | ⚠️ Conditional | 🔄 Discuss First |
| **3.5-3.9** | ⚠️ Conditional | 🔄 Revise | 🔄 Revise |
| **3.0-3.4** | 🔄 Revise | 🔄 Revise | ❌ Reject |
| **<3.0** | ❌ Reject | ❌ Reject | ❌ Reject |

### 4.2 Information Sufficiency Quick Check

| Expert Count | Range ≤1 | Range = 2 | Range ≥3 |
|:-------------|:---------|:----------|:---------|
| **≥5** | ✅ Sufficient | ✅ Sufficient | ⚠️ Borderline |
| **3-4** | ✅ Sufficient | ⚠️ Borderline | ❌ Insufficient |
| **2** | ⚠️ Borderline | ❌ Insufficient | ❌ Insufficient |

### 4.3 √n Lookup Table (for CI if needed)

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

---

## 5. Complete Example

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

**Comparison**: Full method gives S_enhanced=3.24, reasonably close!

---

## 6. One-Page Cheat Sheet

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

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Full framework with mathematical details
- `.knowledge/templates/EXPERT_COMMITTEE_QUICKSTART.md` — Quick-start guide
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates

---

*Expert Committee Simplified Method v2.2*
*Extracted from Expert Committee Framework*
