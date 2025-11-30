# Cognitive Framework

> Multi-perspective analysis using 6 domains × 23 roles × 10 categories × 37 angles

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Documents](#2-documents)
- [3. Key Concepts](#3-key-concepts)
- [4. Quick Reference](#4-quick-reference)

---

## 1. Overview

The Cognitive Framework provides structured approaches to complex problem-solving through expert committee simulation,
enabling multi-perspective analysis.

### 1.1 Design Principles

| Principle            | Application                                 |
|----------------------|---------------------------------------------|
| **First Principles** | Back to essence, not tradition              |
| **MECE**             | Mutually exclusive, collectively exhaustive |
| **SSOT**             | Single source of truth for each concept     |
| **Dynamic**          | Activate experts and angles on-demand       |

### 1.2 Framework Statistics

| Component        | Count | Source (SSOT)         |
|------------------|-------|-----------------------|
| Expert Domains   | 6     | `ROLE_PERSONA.md`     |
| Expert Roles     | 23    | `ROLE_PERSONA.md`     |
| Angle Categories | 10    | `DECISION.md`         |
| Quality Angles   | 37    | `DECISION.md`         |
| Committee Levels | 5     | `EXPERT_COMMITTEE.md` |
| Max Matrix Size  | 851   | 23 × 37               |

---

## 2. Documents

### 2.1 Main Documents

| Document                 | Description                             | SSOT For         |
|--------------------------|-----------------------------------------|------------------|
| `EXPERT_COMMITTEE.md`    | Framework integration, levels, process  | Committee Levels |
| `ROLE_PERSONA.md`        | 23 expert roles in 6 domains            | Expert Roles     |
| `CONFLICT_RESOLUTION.md` | Conflict resolution, weights, deadlocks | Weights          |
| `INFORMATION_DENSITY.md` | Information density optimization        | -                |

### 2.2 Module Files (Expert Committee)

| Module | Description |
|--------|-------------|
| `EXPERT_COMMITTEE_MATH.md` | Aggregation formulas, correlation-adjusted weights, uncertainty quantification |
| `EXPERT_COMMITTEE_CALIBRATION.md` | Bias correction, weight learning, effectiveness tracking |
| `EXPERT_COMMITTEE_ROADMAP.md` | v3.0 architecture roadmap, 6-layer design, implementation phases |

### 2.3 Related Practices

| Practice | Location |
|----------|----------|
| No-Calculator Method | `.knowledge/practices/decisions/EXPERT_COMMITTEE_SIMPLIFIED.md` |

**External SSOT**:

| Document       | Location                  | SSOT For  |
|----------------|---------------------------|-----------|
| Quality Angles | `../patterns/DECISION.md` | 37 Angles |

---

## 3. Key Concepts

### 3.1 Expert Domains (6)

| Domain       | Roles | Core Question               |
|--------------|:-----:|-----------------------------|
| **Build**    |   5   | How to implement correctly? |
| **Run**      |   4   | How to operate reliably?    |
| **Secure**   |   3   | How to protect?             |
| **Data**     |   3   | How to manage data?         |
| **Product**  |   4   | How to satisfy users?       |
| **Strategy** |   4   | How to create value?        |

> Details: `ROLE_PERSONA.md` Section 2-3

### 3.2 Quality Angle Categories (10)

| Cat | Name            | Angles | Core Question              |
|-----|-----------------|:------:|----------------------------|
| A   | Functional      |   3    | Does it work correctly?    |
| B   | Reliability     |   4    | Does it work consistently? |
| C   | Performance     |   3    | Is it fast enough?         |
| D   | Maintainability |   5    | Is it easy to change?      |
| E   | Portability     |   3    | Can it be moved?           |
| F   | Security        |   5    | Is it protected?           |
| G   | Compatibility   |   2    | Does it integrate?         |
| H   | Usability       |   6    | Is it user-friendly?       |
| I   | Data Quality    |   3    | Is data trustworthy?       |
| J   | AI/ML Quality   |   3    | Is AI reliable?            |

> Details: `../patterns/DECISION.md` Section 2

### 3.3 Committee Levels (5)

| Level | Experts | Angles | Use Case                   |
|-------|:-------:|:------:|----------------------------|
| L1    |   2-3   |   3    | Bug fix, config change     |
| L2    |   4-6   |   12   | Minor feature, API change  |
| L3    |  7-10   |   23   | Refactoring, new tech      |
| L4    |  11-15  |   31   | Architecture, DB migration |
| L5    |  16-23  |   37   | Platform change, strategic |

> Details: `EXPERT_COMMITTEE.md` Section 3

### 3.4 Dynamic Activation

Both experts and angles are activated dynamically based on:

- Committee level (L1-L5)
- Problem type (Architecture, Feature, Security, etc.)
- Emerging concerns during analysis

| Trigger           | Expert Action          | Angle Action      |
|-------------------|------------------------|-------------------|
| Security concern  | +Security, +Compliance | +F (Security)     |
| Performance issue | +SRE, +DBA             | +C (Performance)  |
| User feedback     | +UX, +Support          | +H (Usability)    |
| Data problem      | +Data Eng, +Analyst    | +I (Data Quality) |
| AI involved       | +ML Eng                | +J (AI/ML)        |

> Details: `EXPERT_COMMITTEE.md` Section 4

### 3.5 Conflict Resolution

| Mechanism        | Purpose                               |
|------------------|---------------------------------------|
| Weighted voting  | Role weights by decision domain       |
| Authority chain  | Escalation path by domain             |
| Devil's advocate | Mandatory dissent requirement         |
| Tiebreaker rules | Reversibility, risk, 信 (faithfulness) |

> Details: `CONFLICT_RESOLUTION.md`

---

## 4. Quick Reference

### 4.1 Expert Roles by Domain

| Domain       | Roles                                           |
|--------------|-------------------------------------------------|
| **Build**    | Architect · Backend · Frontend · QA · Tech Lead |
| **Run**      | DevOps · SRE · DBA · Release                    |
| **Secure**   | Security · Compliance · Privacy                 |
| **Data**     | Data Eng · ML Eng · Analyst                     |
| **Product**  | PM · UX · Domain · Support                      |
| **Strategy** | CTO · Risk · Cost · Change                      |

### 4.2 Angle Categories Quick List

| Core              | Extended        | Domain         |
|-------------------|-----------------|----------------|
| A Functional      | E Portability   | I Data Quality |
| B Reliability     | F Security      | J AI/ML        |
| C Performance     | G Compatibility |                |
| D Maintainability | H Usability     |                |

### 4.3 SSOT Reference

| Concept              | Defined In                | Other Docs     |
|----------------------|---------------------------|----------------|
| Expert Roles (23)    | `ROLE_PERSONA.md`         | Reference only |
| Quality Angles (37)  | `../patterns/DECISION.md` | Reference only |
| Committee Levels (5) | `EXPERT_COMMITTEE.md`     | Reference only |
| Role Weights         | `CONFLICT_RESOLUTION.md`  | Reference only |

---

## Related

- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates
- `.knowledge/guidelines/COGNITIVE.md` — Cognitive guidelines
- `.knowledge/practices/ai_collaboration/` — AI collaboration practices

---

*AI Collaboration Knowledge Base*
