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
- [6. Output Templates](#6-output-templates)
- [7. Quick Reference](#7-quick-reference)
- [8. Decision Effectiveness Tracking](#8-decision-effectiveness-tracking)

---

## 0. Quick Start

### 30-Second Decision Flow

```text
1. ASSESS RISK → Select Level (L1-L5)
2. ACTIVATE EXPERTS → By problem domain
3. EVALUATE ANGLES → By level requirement
4. REACH CONSENSUS → Weighted voting
5. DOCUMENT → Use template
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
**Scores**: 5, 4, 5 → Avg 4.7
**Verdict**: Approve
```

> For full details, see sections below. Templates at `templates/EXPERT_COMMITTEE.md`.

---

## 1. First Principles

### 1.1 Why Expert Committee?

| Problem | Solution |
|---------|----------|
| Single perspective → blind spots | Multiple expert viewpoints |
| Ad-hoc quality checks | Structured angle evaluation |
| Static team composition | Dynamic activation by need |

### 1.2 Core Philosophy

| Principle | Application |
|-----------|-------------|
| **信 (Faithfulness)** | Correctness before elegance |
| **MECE** | Mutually exclusive, collectively exhaustive |
| **Dynamic** | Activate experts and angles on-demand |
| **Traceability** | Document all decisions and dissent |

### 1.3 What This Framework Does

```text
Problem → Select Level → Activate Experts → Activate Angles → Analyze → Decide → Document
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
1. SCOPE    → Define decision + select committee level
2. ASSEMBLE → Choose experts based on domains
3. ACTIVATE → Select angles based on level + problem type
4. BRIEF    → Present problem with context
5. ANALYZE  → Each expert evaluates assigned angles
6. DISCUSS  → Share perspectives, identify conflicts
7. RESOLVE  → Apply conflict resolution (see CONFLICT_RESOLUTION.md)
8. DECIDE   → Calculate weighted consensus
9. DOCUMENT → Record decision + rationale + dissent
```

### 5.2 Role Switching Syntax

> **Template**: `.knowledge/templates/EXPERT_COMMITTEE.md` Section 7.1

### 5.3 Per-Expert Analysis Template

> **Template**: `.knowledge/templates/EXPERT_COMMITTEE.md` Section 7.2

### 5.4 Scoring Scale

| Score | Meaning | Action |
|:-----:|---------|--------|
| 5 | Excellent | Proceed |
| 4 | Good | Minor improvements |
| 3 | Acceptable | Address concerns |
| 2 | Poor | Significant changes |
| 1 | Failing | Do not proceed |

---

## 6. Output Templates

> **SSOT**: All decision templates → `.knowledge/templates/EXPERT_COMMITTEE.md`

### 6.1 Available Templates

| Level | Template | Use Case |
|-------|----------|----------|
| L1 | Quick Check | Bug fix, config change |
| L2 | Standard Review | Minor feature, compatible API |
| L3 | Deep Analysis | Refactoring, new tech adoption |
| L4 | Comprehensive Review | Architecture, DB migration |
| L5 | Full Committee | Platform change, security overhaul |

### 6.2 Usage Guide

1. **Select Level** — Use Section 3 criteria
2. **Copy Template** — From `templates/EXPERT_COMMITTEE.md`
3. **Activate Experts** — Apply Section 4 dynamic rules
4. **Analyze** — Follow Section 5 process
5. **Document** — Record per CONFLICT_RESOLUTION.md

---

## 7. Quick Reference

### 7.1 Level Selection Guide

| Question | L1 | L2 | L3 | L4 | L5 |
|----------|:--:|:--:|:--:|:--:|:--:|
| Can we easily undo? | ✓ | ✓ | · | · | · |
| Affects only 1 team? | ✓ | ✓ | · | · | · |
| Low security risk? | ✓ | ✓ | ✓ | · | · |
| Under $10K impact? | ✓ | ✓ | ✓ | · | · |
| Reversible in <1 day? | ✓ | ✓ | · | · | · |

### 7.2 Domain Selection by Problem

| Problem | Primary Domains |
|---------|-----------------|
| Architecture | Build, Strategy |
| Feature | Build, Product |
| Security | Secure, Run |
| Performance | Run, Build |
| Data | Data, Secure |
| Operations | Run |

### 7.3 Summary Statistics

| Metric | Value |
|--------|-------|
| Expert Domains | 6 |
| Expert Roles | 23 |
| Angle Categories | 10 |
| Quality Angles | 37 |
| Committee Levels | 5 |
| Max Matrix Size | 23 × 37 = 851 |

---

## 8. Decision Effectiveness Tracking

### 8.1 Post-Decision Review

| Checkpoint | Timing | Question |
|------------|--------|----------|
| **Immediate** | 1 week | Was implementation smooth? |
| **Short-term** | 1 month | Did expected benefits materialize? |
| **Long-term** | 3 months | Was the decision correct? |

### 8.2 Effectiveness Metrics

| Metric | Formula | Target |
|--------|---------|:------:|
| Decision Accuracy | Correct / Total | >85% |
| Prediction Error | \|Predicted - Actual\| | <20% |
| Reversal Rate | Reversed / Total | <10% |

### 8.3 Feedback Loop

```text
1. RECORD   → Document decision with predictions
2. SCHEDULE → Set review checkpoints
3. COMPARE  → Actual vs predicted outcomes
4. LEARN    → Update framework if systematic errors
```

### 8.4 Review Template

| Item | Predicted | Actual | Delta | Lesson |
|------|-----------|--------|:-----:|--------|
| Outcome | | | | |
| Timeline | | | | |
| Risk Events | | | | |
| User Impact | | | | |

### 8.5 Continuous Improvement

| Signal | Action |
|--------|--------|
| Accuracy <85% | Review angle coverage |
| Prediction Error >20% | Calibrate expert weights |
| Reversal Rate >10% | Increase committee level |
| Systematic bias | Add/remove expert roles |

---

## Related

- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert roles (SSOT)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates
- `.knowledge/guidelines/COGNITIVE.md` — Cognitive guidelines

---

*AI Collaboration Knowledge Base*
