# Expert Committee Calibration

> Bias correction, dynamic weight learning, and effectiveness tracking

---

## Table of Contents

- [1. Bias Correction](#1-bias-correction)
- [2. Dynamic Weight Learning](#2-dynamic-weight-learning)
- [3. Decision Effectiveness Tracking](#3-decision-effectiveness-tracking)

---

## 1. Bias Correction

### 1.1 Three-Step Debiasing Process

```text
Step 1: Independent Scoring (prevents anchoring)
        ↓
Step 2: Anonymous Aggregation (prevents conformity)
        ↓
Step 3: Open Discussion (information sharing)
```

### 1.2 Implementation Requirements

| Phase | Requirement | Reason |
|-------|-------------|--------|
| **Independent Scoring** | Each expert scores without seeing others | Prevent anchoring effect |
| **Anonymous Aggregation** | Show statistics first, not who scored what | Prevent authority suppression |
| **Open Discussion** | Discuss divergence points, allow score revision | Full information sharing |

### 1.3 Random Speaking Order

```python
# Randomize expert speaking order for each decision
import random
experts = ["Architect", "Engineer", "QA", "PM", ...]
random.shuffle(experts)  # Randomize
```

### 1.4 Devil's Advocate Requirements

Each decision **MUST** include:

| Requirement | Count | Assignment Method |
|-------------|-------|-------------------|
| Dissenting opinion | ≥1 | Rotate or assign Risk role |
| Risk enumeration | ≥3 | Each expert contributes ≥1 |
| Alternative approach | ≥1 | Lowest-scoring expert proposes |

---

## 2. Dynamic Weight Learning

### 2.1 Lightweight Implementation

Simple **sliding window accuracy** instead of complex Bayesian updates:

```
Dynamic Weight = Base Weight × Accuracy Adjustment

Accuracy Adjustment = (Correct in last 10 decisions + 5) / 15
```

### 2.2 Example

| Expert | Base Weight | Last 10 Correct | Adjustment | Dynamic Weight |
|--------|-------------|-----------------|------------|----------------|
| Architect | 0.9 | 8 | (8+5)/15=0.87 | 0.78 |
| Engineer | 0.7 | 9 | (9+5)/15=0.93 | 0.65 |
| QA | 0.7 | 10 | (10+5)/15=1.0 | 0.70 |

### 2.3 Cold Start Handling

New experts or new domains: Use base weight, start adjusting after 5 accumulated decisions.

---

## 3. Decision Effectiveness Tracking

### 3.1 Post-Decision Review

| Checkpoint | Timing | Question |
|------------|--------|----------|
| **Immediate** | 1 week | Was implementation smooth? |
| **Short-term** | 1 month | Did expected benefits materialize? |
| **Long-term** | 3 months | Was the decision correct? |

### 3.2 Effectiveness Metrics

| Metric | Formula | Target |
|--------|---------|:------:|
| Decision Accuracy | Correct / Total | >85% |
| Prediction Error | \|Predicted - Actual\| | <20% |
| Reversal Rate | Reversed / Total | <10% |
| Calibration | CI coverage rate | >90% |

### 3.3 Feedback Loop

```text
1. RECORD   → Document decision with predictions
2. SCHEDULE → Set review checkpoints
3. COMPARE  → Actual vs predicted outcomes
4. LEARN    → Update weights if systematic errors
```

### 3.4 Review Template

| Item | Predicted | Actual | Delta | Lesson |
|------|-----------|--------|:-----:|--------|
| Outcome | | | | |
| Timeline | | | | |
| Risk Events | | | | |
| User Impact | | | | |

### 3.5 Continuous Improvement

| Signal | Action |
|--------|--------|
| Accuracy <85% | Review angle coverage |
| Prediction Error >20% | Calibrate expert weights |
| Reversal Rate >10% | Increase committee level |
| CI coverage <90% | Adjust λ parameter |
| Systematic bias | Add/remove expert roles |

---

## Related

- `EXPERT_COMMITTEE.md` — Main framework document
- `EXPERT_COMMITTEE_MATH.md` — Aggregation and uncertainty formulas
- `CONFLICT_RESOLUTION.md` — Conflict resolution methods

---

*Expert Committee Calibration v2.2*
*Extracted from Expert Committee Framework*
