# Expert Committee Decision Templates

> Ready-to-use decision templates with enhanced aggregation and uncertainty quantification

---

## Table of Contents

- [1. Quick Reference](#1-quick-reference)
- [2. L1 Quick Check](#2-l1-quick-check)
- [3. L2 Standard Review](#3-l2-standard-review)
- [4. L3 Deep Analysis](#4-l3-deep-analysis)
- [5. L4 Comprehensive Review](#5-l4-comprehensive-review)
- [6. L5 Full Committee](#6-l5-full-committee)
- [7. Analysis Templates](#7-analysis-templates)
- [8. Aggregation Calculator](#8-aggregation-calculator)
- [9. Usage Tips](#9-usage-tips)

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

### Enhanced Decision Rules

| Condition | Decision | Action |
|-----------|----------|--------|
| CI_lower > 3.5 | **Strong Approve** | Proceed confidently |
| S > 3.5 AND CI_lower > 2.5 | **Conditional Approve** | Proceed with monitoring |
| CI_upper < 2.5 | **Strong Reject** | Do not proceed |
| CI_width > 2.0 | **Need More Info** | Add experts or discuss |
| Other | **Revise** | Re-evaluate after changes |

---

## 2. L1: Quick Check

**Use for**: Bug fix, config change, routine decisions

**Panel**: Engineer, QA (2-3 experts)

**Template**:

`````markdown
## L1 Quick Check
**Decision**: [What]
**Panel**: Engineer, QA

### Phase 1: Independent Scoring
| Expert | Score | Concerns | (独立填写) |
|--------|:-----:|----------|-----------|
| Engineer | 1-5 | | |
| QA | 1-5 | | |

### Phase 2: Aggregation
| Metric | Value |
|--------|-------|
| Weighted Mean (S) | |
| Weighted StdDev (σ) | |
| Enhanced Score (S - 0.5σ) | |
| 95% CI | [ , ] |
| Information Sufficiency | |

### Decision
| Check | Result |
|-------|:------:|
| CI_lower > 3.5? | ☐ |
| Enhanced Score > 3.5? | ☐ |
| IS > 0.5? | ☐ |

**Verdict**: [Strong Approve / Conditional Approve / Revise / Reject]
**Confidence**: [CI range]
`````

---

## 3. L2: Standard Review

**Use for**: Minor feature, backward-compatible API change

**Panel**: Architect, Engineer, QA, PM (4-6 experts)

**Template**:

`````markdown
## L2 Standard Review
**Decision**: [What]
**Context**: [Background]
**Panel**: Architect, Engineer, QA, PM

### Phase 1: Independent Scoring

> **Weight Formula**: `W = 0.4 × W_domain + 0.6 × W_angle` (see CONFLICT_RESOLUTION.md §4.7)

| Expert | W_domain | W_angle | W_total | Score | Concerns | (独立填写) |
|--------|:--------:|:-------:|:-------:|:-----:|----------|-----------|
| Architect | 0.9 | 0.88 | 0.89 | | | |
| Engineer | 0.7 | 0.88 | 0.81 | | | |
| QA | 0.7 | 0.88 | 0.81 | | | |
| PM | 0.25 | 0.55 | 0.43 | | | |

### Phase 2: Aggregation
| Metric | Value | Formula |
|--------|-------|---------|
| Weighted Mean (S) | | Σ(W_total×s)/Σ(W_total) |
| Weighted StdDev (σ) | | √[Σw(s-S)²/Σw] |
| Enhanced Score | | S - 0.5σ |
| Standard Error (SE) | | σ/√n |
| 95% CI | [ , ] | S ± 1.96×SE |
| CI Width | | |
| Information Sufficiency | | 1 - width/4 |

### Phase 3: Divergence Analysis
**Divergence Level**: [High consensus / Minor / Moderate / Significant / Severe]
**Main Divergence Points**: 
**Devil's Advocate Opinion**:
**Risks Identified** (≥3):
1. 
2. 
3. 

### Risk Summary
| Dimension | Level | Mitigation |
|-----------|-------|------------|
| Technical | Low/Med/High | |
| Business | Low/Med/High | |
| Timeline | Low/Med/High | |

### Decision
| Condition | Check |
|-----------|:-----:|
| CI_lower > 3.5? | ☐ |
| Enhanced Score > 3.5? | ☐ |
| IS > 0.5? | ☐ |

**Verdict**: [Strong Approve / Conditional Approve / Revise / Reject / Need More Info]
**Confidence**: [CI range]
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

### Phase 1: Independent Scoring (Angles 1-23)

> **Weight Formula**: `W = (0.4 × W_domain + 0.6 × W_angle) × 1.05` (L3 factor, see EXPERT_COMMITTEE.md §3.6)

| # | Angle | Expert | Weight | Score | Notes |
|---|-------|--------|:------:|:-----:|-------|
| A1 | Correctness | | | | |
| A2 | Completeness | | | | |
| A3 | Suitability | | | | |
| B1 | Maturity | | | | |
| B2 | Availability | | | | |
| B3 | Fault Tolerance | | | | |
| B4 | Recoverability | | | | |
| C1 | Time Behavior | | | | |
| C2 | Resource Util | | | | |
| C3 | Capacity | | | | |
| D1 | Modularity | | | | |
| D2 | Reusability | | | | |
| D3 | Analyzability | | | | |
| D4 | Modifiability | | | | |
| D5 | Testability | | | | |
| E1 | Adaptability | | | | |
| E2 | Installability | | | | |
| E3 | Replaceability | | | | |
| F1 | Confidentiality | | | | |
| F2 | Integrity | | | | |
| F3 | Non-repudiation | | | | |
| F4 | Accountability | | | | |
| F5 | Authenticity | | | | |

### Phase 2: Category Aggregation
| Category | Angles | Raw Avg | σ | Enhanced |
|----------|--------|:-------:|:-:|:--------:|
| A. Functional (3) | A1-A3 | | | |
| B. Reliability (4) | B1-B4 | | | |
| C. Performance (3) | C1-C3 | | | |
| D. Maintainability (5) | D1-D5 | | | |
| E. Portability (3) | E1-E3 | | | |
| F. Security (5) | F1-F5 | | | |

### Phase 3: Overall Aggregation
| Metric | Value |
|--------|-------|
| Overall Weighted Mean (S) | |
| Overall Weighted StdDev (σ) | |
| Enhanced Score (S - 0.5σ) | |
| 95% CI | [ , ] |
| Information Sufficiency | |

### Phase 4: Expert Votes
| Expert | Vote | Confidence | Key Concern |
|--------|------|:----------:|-------------|
| [Role] | Approve/Reject | H/M/L | |

### Phase 5: Divergence Analysis
**Divergence Level**: [High consensus / Minor / Moderate / Significant / Severe]
**Main Divergence Points**: 
**Devil's Advocate Opinion**:
**Alternative Approach Proposed**:

### Risk Matrix
| Risk | Probability | Impact | Mitigation |
|------|:-----------:|:------:|------------|
| [Risk 1] | H/M/L | H/M/L | [Action] |
| [Risk 2] | H/M/L | H/M/L | [Action] |
| [Risk 3] | H/M/L | H/M/L | [Action] |

### Decision
**Verdict**: [Strong Approve / Conditional Approve / Revise / Reject / Need More Info]
**Enhanced Score**: [X.XX]
**CI_95%**: [X.XX, X.XX]
**IS**: [X.XX]
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

> **Weight Formula**: `W = (0.4 × W_domain + 0.6 × W_angle) × 1.10` (L4 factor, see EXPERT_COMMITTEE.md §3.6)

| Category | Experts | W_domain | W_angle | W_adjusted |
|----------|---------|:--------:|:-------:|:----------:|
| Technical | [List 5-7] | [per role] | [per angle] | [calculated] |
| Domain | [List 3-5] | [per role] | [per angle] | [calculated] |
| Strategic | [List 2-3] | [per role] | [per angle] | [calculated] |

### Phase 1: Independent Scoring (31 angles: A-H)

#### Group: Technical
| Expert | A1-A3 | B1-B4 | C1-C3 | D1-D5 | E1-E3 | F1-F5 | G1-G2 | H1-H6 |
|--------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| [Name] | | | | | | | | |

#### Group: Domain
| Expert | A1-A3 | B1-B4 | C1-C3 | D1-D5 | E1-E3 | F1-F5 | G1-G2 | H1-H6 |
|--------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| [Name] | | | | | | | | |

#### Group: Strategic
| Expert | A1-A3 | B1-B4 | C1-C3 | D1-D5 | E1-E3 | F1-F5 | G1-G2 | H1-H6 |
|--------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| [Name] | | | | | | | | |

### Phase 2: Category Aggregation
| Category | Angles | Raw Avg | σ | Enhanced | CI_95% |
|----------|--------|:-------:|:-:|:--------:|:------:|
| A. Functional (3) | A1-A3 | | | | |
| B. Reliability (4) | B1-B4 | | | | |
| C. Performance (3) | C1-C3 | | | | |
| D. Maintainability (5) | D1-D5 | | | | |
| E. Portability (3) | E1-E3 | | | | |
| F. Security (5) | F1-F5 | | | | |
| G. Compatibility (2) | G1-G2 | | | | |
| H. Usability (6) | H1-H6 | | | | |

### Phase 3: Group Aggregation
| Group | S | σ | Enhanced | CI_95% | IS | Vote |
|-------|:-:|:-:|:--------:|:------:|:--:|:----:|
| Technical | | | | | | Y/N |
| Domain | | | | | | Y/N |
| Strategic | | | | | | Y/N |
| **Overall** | | | | | | |

### Phase 4: Consensus Analysis
| Level | Requirement | Status |
|-------|-------------|:------:|
| Unanimous | 3/3 groups approve | ✓/✗ |
| Strong | 2/3 groups approve | ✓/✗ |
| Conditional | 2/3 with conditions | ✓/✗ |

### Dissenting Opinions
| Expert | Group | Concern | Proposed Mitigation |
|--------|-------|---------|---------------------|
| [Role] | [Group] | [Issue] | [If proceeding] |

### Decision
**Verdict**: [Strong Approve / Conditional Approve / Major Revision / Reject / Need More Info]
**Enhanced Score**: [X.XX]
**CI_95%**: [X.XX, X.XX]
**IS**: [X.XX]
**Confidence**: [Based on CI and IS]
**Binding Conditions**: [Must-meet items]
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

> **Weight Formula**: `W = (0.4 × W_domain + 0.6 × W_angle) × 1.15` (L5 factor, see EXPERT_COMMITTEE.md §3.6)

| Category | Count | Experts | W_domain | W_angle | W_adjusted |
|----------|:-----:|---------|:--------:|:-------:|:----------:|
| Technical | 6-8 | [List] | [per role] | [per angle] | [calculated] |
| Domain | 5-7 | [List] | [per role] | [per angle] | [calculated] |
| Strategic | 5-8 | [List] | [per role] | [per angle] | [calculated] |

### Phase 1: Independent Scoring (All 37 angles: A-J)
> Each expert scores independently. Do NOT view others' scores.

[Use separate scoring sheets per expert, collect anonymously]

### Phase 2: Full Category Aggregation
| Category | Angles | Raw Avg | σ | Enhanced | CI_95% | IS |
|----------|--------|:-------:|:-:|:--------:|:------:|:--:|
| A. Functional (3) | A1-A3 | | | | | |
| B. Reliability (4) | B1-B4 | | | | | |
| C. Performance (3) | C1-C3 | | | | | |
| D. Maintainability (5) | D1-D5 | | | | | |
| E. Portability (3) | E1-E3 | | | | | |
| F. Security (5) | F1-F5 | | | | | |
| G. Compatibility (2) | G1-G2 | | | | | |
| H. Usability (6) | H1-H6 | | | | | |
| I. Data Quality (3) | I1-I3 | | | | | |
| J. AI/ML Quality (3) | J1-J3 | | | | | |

### Phase 3: Group Aggregation
| Group | S | σ | Enhanced | CI_95% | IS | Approval | Key Concerns |
|-------|:-:|:-:|:--------:|:------:|:--:|:--------:|--------------|
| Technical | | | | | | Yes/No | |
| Domain | | | | | | Yes/No | |
| Strategic | | | | | | Yes/No | |
| **Overall** | | | | | | | |

### Phase 4: Consensus Analysis
| Level | Requirement | Status |
|-------|-------------|:------:|
| Unanimous | 3/3 groups approve | ✓/✗ |
| Strong | 2/3 groups approve | ✓/✗ |
| Conditional | 2/3 with conditions | ✓/✗ |

### Phase 5: Divergence Deep-Dive
**Overall Divergence Level**: [High consensus / Minor / Moderate / Significant / Severe]

#### Major Divergence Points
| Point | Groups Affected | Resolution |
|-------|-----------------|------------|
| | | |

#### Devil's Advocate Summary
| Assigned Expert | Key Objection | Counter-argument | Resolution |
|-----------------|---------------|------------------|------------|
| | | | |

#### Alternative Approaches Proposed
| Proposer | Alternative | Pros | Cons | Committee Response |
|----------|-------------|------|------|-------------------|
| | | | | |

### Final Decision
**Verdict**: [Strong Approve / Conditional Approve / Major Revision / Reject / Need More Info]
**Enhanced Score**: [X.XX]
**CI_95%**: [X.XX, X.XX]
**Information Sufficiency**: [X.XX]
**Confidence Level**: [Based on CI, IS, and consensus]
**Binding Conditions**: [Must-meet items before proceeding]

### Post-Decision Actions
- [ ] Document rationale and full deliberation record
- [ ] Communicate decision to all stakeholders
- [ ] Set review checkpoints (1 week, 1 month, 3 months)
- [ ] Prepare rollback plan
- [ ] Schedule effectiveness review
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
**Weight**: [0.3-0.9]
**Assigned Angles**: [List of angle IDs]

| Angle | Score | Assessment |
|-------|:-----:|------------|
| A1 Correctness | 1-5 | [Brief note] |

**Key Concerns**: [Main issues from this perspective]
**Risks Identified**: 
1. [Risk 1]
2. [Risk 2]
**Recommendation**: [Approve/Conditional/Reject]
**Confidence**: [High/Medium/Low]
`````

### 7.3 Dissent Record

`````markdown
**Dissenting Expert**: [Role]
**Domain**: [Domain]
**Position**: [Reject/Major Revision]
**Rationale**: [Why]
**Key Risk**: [Main concern]
**Proposed Mitigation**: [If proceeding anyway]
**Alternative Approach**: [Suggested alternative]
`````

---

## 8. Aggregation Calculator

> **SSOT**: Full formulas and lookup tables in `EXPERT_COMMITTEE.md` §6-7

### 8.1 Step-by-Step Calculation (v2.2 - Corrected)

```markdown
## Aggregation Worksheet v2.2

### Input Data
| Expert | Weight (w) | Score (s) | Domain |
|--------|:----------:|:---------:|--------|
| | | | |
| | | | |
| **Sum** | Σw = | | n = ___ |

### Step 1: Weighted Mean
S = Σ(w × s) / Σw = _____ / _____ = _____

### Step 2: Weighted Variance with Bessel Correction
| Expert | w | s | (s - S)² | w × (s - S)² |
|--------|:-:|:-:|:--------:|:------------:|
| | | | | |
| | | | | |
| **Sum** | | | | Σ = |

σ_biased² = Σ[w × (s - S)²] / Σw = _____ / _____ = _____
σ_biased = √σ² = _____

Bessel factor (from §6.4): n=2-3→1.3, n=4-5→1.15, n=6-10→1.1, n≥11→1.05
σ_corrected = σ_biased × _____ = _____

### Step 3: Enhanced Score with Dynamic λ
λ(n) from §6.3: n=2-3→1.2, n=4-5→0.9, n=6-9→0.7, n=10-14→0.6, n≥15→0.5
λ = _____
S_enhanced = S - λ × σ_corrected = _____ - _____ × _____ = _____

### Step 4: Confidence Interval (t-distribution + correlation)
SE_basic = σ_corrected / √n = _____ / √_____ = _____

Domain composition: □ Mixed  □ Majority same  □ All same
ρ estimate (from §7.3): Mixed→0.05-0.10, Majority→0.15-0.25, Same→0.35
SE_corrected = SE_basic × √(1 + (n-1) × ρ) = _____ × _____ = _____

t-value (from §7.2): n=2-3→4.0, n=4-5→3.0, n=6-9→2.4, n=10-14→2.2, n≥15→2.1
t = _____

CI_95% = [S_enhanced - t×SE_corrected, S_enhanced + t×SE_corrected]
       = [_____ - _____, _____ + _____]
       = [_____, _____]

### Step 5: Information Sufficiency (with lower bound)
CI_width = _____ - _____ = _____
IS = max(0, 1 - (CI_width / 4)) = max(0, 1 - _____) = _____

### Decision Check
| Condition | Value | Check |
|-----------|-------|:-----:|
| CI_lower > 3.5? | | ☐ Strong Approve |
| S > 3.5 AND CI_lower > 2.5? | | ☐ Conditional Approve |
| CI_upper < 2.5? | | ☐ Strong Reject |
| CI_width > 2.0? | | ☐ Need More Info |
| IS > 0.5? | | ☐ Sufficient Info |
```

### 8.2 Quick Reference Tables

#### Dynamic λ(n) Lookup
| n (experts) | λ |
|:-----------:|:-:|
| 2-3 | 1.2 |
| 4-5 | 0.9 |
| 6-9 | 0.7 |
| 10-14 | 0.6 |
| ≥15 | 0.5 |

#### t-Distribution Values (95% CI)
| n | t |
|:-:|:-:|
| 2-3 | 4.0 |
| 4-5 | 3.0 |
| 6-9 | 2.4 |
| 10-14 | 2.2 |
| ≥15 | 2.1 |

#### Bessel Correction Factors
| n | Factor |
|:-:|:------:|
| 2-3 | 1.3 |
| 4-5 | 1.15 |
| 6-10 | 1.1 |
| ≥11 | 1.05 |

#### Correlation SE Multiplier
| Composition | SE × |
|-------------|:----:|
| Mixed domains | 1.3 |
| Majority same | 1.7 |
| All same | 2.0 |

#### Divergence Interpretation
| σ_corrected | Interpretation | Action |
|-------------|----------------|--------|
| 0 - 0.3 | High consensus | Proceed with confidence |
| 0.3 - 0.6 | Minor divergence | Note concerns, proceed |
| 0.6 - 1.0 | Moderate divergence | Discuss before deciding |
| 1.0 - 1.5 | Significant divergence | Resolve conflicts first |
| > 1.5 | Severe divergence | Do not proceed, investigate |

#### Information Sufficiency
| IS Range | Interpretation | Action |
|----------|----------------|--------|
| > 0.7 | Sufficient | Decide confidently |
| 0.5 - 0.7 | Basically sufficient | Decide with caution |
| < 0.5 | Insufficient | Add experts or defer |
| = 0 | Extreme uncertainty | Defer decision |

---

## 9. Usage Tips

| Tip | Description |
|-----|-------------|
| **Independent First** | Always collect scores independently before any discussion |
| **Anonymous Collection** | Show statistics before revealing who scored what |
| **Bessel Correction** | Apply √(n/(n-1)) factor to σ for unbiased estimate |
| **Dynamic λ** | Use λ(n) from lookup table, not fixed 0.5 |
| **t-Distribution** | Use t-values for CI, not z=1.96 (especially for n<15) |
| **Correlation Correction** | Adjust SE for domain composition |
| **Output CI** | Always report confidence interval, not just point estimate |
| **Check IS** | Ensure Information Sufficiency > 0.5 before deciding |
| **Devil's Advocate** | Require at least one dissenting opinion |
| **Document Dissent** | Record all disagreements for future learning |
| **Start Low** | Begin at L1, escalate if complexity emerges |
| **Time-Box** | Set strict time limits per level |

### Pre-Decision Checklist (v2.2)

```markdown
□ Independent scoring completed? (prevents anchoring)
□ Applied Bessel correction to σ? (σ_corrected = σ_biased × factor)
□ Used dynamic λ(n) from lookup table? (not fixed 0.5)
□ Applied divergence penalty? (S_enhanced = S - λ(n) × σ_corrected)
□ Used t-distribution for CI? (not z=1.96)
□ Applied correlation correction to SE? (based on domain composition)
□ Output confidence interval? (uncertainty quantification)
□ Information sufficiency > 0.5? (IS = max(0, 1 - CI_width/4))
□ Devil's advocate opinion recorded? (structural debiasing)
□ All dissenting opinions documented? (traceability)
□ Risks enumerated (≥3)? (risk awareness)
```

---

## Related

- `.knowledge/templates/EXPERT_COMMITTEE_QUICKSTART.md` — **Quick-Start Guide (5 min)**
- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Full framework (SSOT)
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert role definitions (23)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (37)
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution

---

*Expert Committee Templates v2.2*
