# Expert Committee Mathematical Methods

> Enhanced aggregation and uncertainty quantification formulas

---

## Table of Contents

- [1. Enhanced Aggregation](#1-enhanced-aggregation)
  - [1.7 Correlation-Adjusted Weights](#17-correlation-adjusted-weights-advanced)
  - [1.8 Winsorized Aggregation](#18-winsorized-aggregation-outlier-handling)
- [2. Uncertainty Quantification](#2-uncertainty-quantification)

---

## 1. Enhanced Aggregation

### 1.1 Basic Formula (Original)

```
S = Σ(wᵢ × sᵢ) / Σwᵢ
```

### 1.2 Enhanced Formula (Required)

```
S_enhanced = S_weighted - λ(n) × σ_corrected

Where:
- S_weighted = Σ(wᵢ × sᵢ) / Σwᵢ           (weighted mean)
- σ_biased = √[Σwᵢ(sᵢ - S)² / Σwᵢ]        (biased weighted std dev)
- σ_corrected = σ_biased × √(n/(n-1))     (Bessel correction)
- λ(n) = lookup from table below          (dynamic penalty coefficient)
```

### 1.3 Dynamic λ(n) Lookup Table

| n (experts) | λ(n) | No-Calculator λ |
|:-----------:|:----:|:---------------:|
| 2-3 | 1.2 | 1.2 |
| 4-5 | 0.9 | 0.9 |
| 6-9 | 0.7 | 0.7 |
| 10-14 | 0.6 | 0.6 |
| 15-19 | 0.5 | 0.5 |
| ≥20 | 0.4 | 0.4 |

**Rationale**: Smaller samples have higher uncertainty; larger λ provides more conservative estimates.

### 1.4 Bessel Correction Factor Table

| n (experts) | Factor √(n/(n-1)) | No-Calculator |
|:-----------:|:-----------------:|:-------------:|
| 2-3 | 1.3 | 1.3 |
| 4-5 | 1.15 | 1.15 |
| 6-10 | 1.1 | 1.1 |
| 11-15 | 1.05 | 1.05 |
| ≥16 | 1.0 | 1.0 |

**Rationale**: Corrects for bias in sample standard deviation estimation.

### 1.5 Calculation Example

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

n = 4, Bessel factor = 1.15 (from table 1.4)
σ_corrected = 0.59 × 1.15 = 0.68
```

**Step 3: Enhanced Score with Dynamic λ**
```
n = 4, λ(4) = 0.9 (from table 1.3)
S_enhanced = 3.85 - 0.9 × 0.68 = 3.24
```

**Interpretation**: With corrected formulas, score is more conservative (3.24 vs 3.55 old method), better reflecting small-sample uncertainty.

### 1.6 Divergence Reference Table

| Corrected σ | Interpretation | Typical Penalty Range |
|-------------|----------------|----------------------|
| 0 - 0.3 | High consensus | Low |
| 0.3 - 0.6 | Minor divergence | Moderate |
| 0.6 - 1.0 | Moderate divergence | Significant |
| 1.0 - 1.5 | Significant divergence | High |
| > 1.5 | Severe divergence | Very High |

> **Note**: Actual penalty depends on λ(n). Use `Penalty = λ(n) × σ_corrected`.

### 1.7 Correlation-Adjusted Weights (Advanced)

When experts from similar domains may have correlated opinions, adjust weights to reduce redundancy:

**Formula**:
```
w'ᵢ = wᵢ / (1 + Σⱼ≠ᵢ ρᵢⱼ × wⱼ)

Where:
- w'ᵢ = adjusted weight for expert i
- wᵢ = original weight for expert i
- ρᵢⱼ = correlation between expert i and j (from domain similarity)
- Σⱼ≠ᵢ = sum over all other experts
```

**Domain Correlation Matrix (ρᵢⱼ)**:

| Domain Pair | ρ | Rationale |
|-------------|:-:|-----------|
| Same domain | 0.35 | High overlap |
| Adjacent domains* | 0.15 | Some overlap |
| Different domains | 0.05 | Minimal overlap |

*Adjacent: Build↔Run, Secure↔Run, Data↔Build, Product↔Strategy

**Simplified Adjustment Table**:

| Expert Composition | Adjustment Factor | Apply to |
|--------------------|:-----------------:|----------|
| All different domains | 1.0 (no adjustment) | Each weight |
| 2 experts same domain | 0.85 | Same-domain experts |
| 3+ experts same domain | 0.75 | Same-domain experts |
| Majority same domain | 0.70 | All same-domain experts |

**Example**:
```
Original: Architect(0.9), Engineer(0.7), QA(0.7) - all Build domain
Adjusted: Architect(0.9×0.75=0.68), Engineer(0.7×0.75=0.53), QA(0.7×0.75=0.53)

Effect: Reduces over-representation of Build perspective
```

### 1.8 Winsorized Aggregation (Outlier Handling)

For robustness against extreme scores:

**Formula**:
```
S_winsorized = Winsorize(scores, α=10%)

Process:
1. Sort scores
2. Replace bottom α% with (α+1)th percentile value
3. Replace top α% with (100-α-1)th percentile value
4. Apply weighted average to winsorized scores
```

**When to Use**:

| Condition | Use Winsorization? |
|-----------|:------------------:|
| n ≥ 5 experts | Yes (α=10%) |
| n = 3-4 experts | Optional (α=20%) |
| n ≤ 2 experts | No |
| Score range ≥ 3 | Recommended |
| Score range ≤ 1 | Not needed |

**Combined Formula (Full Enhancement)**:
```
S_improved = Winsorize(Σ w'ᵢsᵢ / Σ w'ᵢ, α) - λ(n) × σ_corrected

Where:
- w'ᵢ = correlation-adjusted weights
- α = winsorization level (10% default)
- λ(n) = divergence penalty coefficient
- σ_corrected = Bessel-corrected standard deviation
```

---

## 2. Uncertainty Quantification

### 2.1 Confidence Interval (Corrected)

**Formula**:
```
CI_95% = [S_enhanced - t(n-1) × SE_corrected, S_enhanced + t(n-1) × SE_corrected]

Where:
- SE_basic = σ_corrected / √n
- SE_corrected = SE_basic × √(1 + (n-1) × ρ)   (correlation correction)
- t(n-1) = t-distribution value for df = n-1   (replaces z=1.96)
- ρ = estimated correlation between experts    (from domain composition)
```

### 2.2 t-Distribution Lookup Table (95% CI)

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

### 2.3 Correlation Estimation Table

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

### 2.4 Calculation Example (continued from 1.5)

```
From Section 1.5: S_enhanced = 3.24, σ_corrected = 0.68, n = 4

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

### 2.5 Enhanced Decision Rules

| Condition | Decision | Action |
|-----------|----------|--------|
| CI_lower > 3.5 | **Strong Approve** | Proceed confidently |
| S > 3.5 AND CI_lower > 2.5 | **Conditional Approve** | Proceed with monitoring |
| CI_upper < 2.5 | **Strong Reject** | Do not proceed |
| CI_width > 2.0 | **Need More Info** | Add experts or discuss |
| Other | **Revise** | Re-evaluate after changes |

### 2.6 Information Sufficiency (IS)

```
IS = max(0, 1 - (CI_width / 4))    # Lower bound at 0

IS > 0.7   → Information sufficient
IS 0.5-0.7 → Basically sufficient
IS < 0.5   → Insufficient, add more experts
IS = 0     → Extreme uncertainty, defer decision
```

**Example** (continued from 2.4):
```
CI_width = 4.48 - 2.00 = 2.48
IS = max(0, 1 - (2.48 / 4)) = max(0, 0.38) = 0.38
→ Insufficient information, add more experts or discuss
```

> **Note**: With corrected formulas, small samples often yield IS < 0.5, correctly signaling need for more experts.

---

## Related

- `EXPERT_COMMITTEE.md` — Main framework document
- `EXPERT_COMMITTEE_CALIBRATION.md` — Bias correction and weight learning
- `CONFLICT_RESOLUTION.md` — Weight definitions (SSOT)

---

*Expert Committee Mathematical Methods v2.3*
*Updated: 2025-12-01 - Added correlation-adjusted weights (§1.7) and winsorized aggregation (§1.8)*
