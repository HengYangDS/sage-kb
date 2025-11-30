# Quality Angles Framework

> Hierarchical quality evaluation based on ISO 25010 + extensions (10 categories × 37 angles)

---

## Table of Contents

- [1. First Principles](#1-first-principles)
- [2. Quality Model (10 Categories)](#2-quality-model-10-categories)
- [3. Complete Angle Reference](#3-complete-angle-reference)
- [4. Dynamic Angle Activation](#4-dynamic-angle-activation)
- [5. Angle-Role Mapping](#5-angle-role-mapping)
- [6. Evaluation Templates](#6-evaluation-templates)

---

## 1. First Principles

### 1.1 What is a Quality Angle?

| Aspect | Definition |
|--------|------------|
| **Essence** | A dimension for evaluating quality |
| **Purpose** | Ask the right questions |
| **Structure** | Hierarchical: Category → Angle |

### 1.2 Design Principles

| Principle | Application |
|-----------|-------------|
| **MECE** | Mutually exclusive, collectively exhaustive |
| **ISO 25010** | International standard foundation |
| **Hierarchical** | 10 categories containing 37 angles |
| **Dynamic** | Activate angles based on problem type and level |

### 1.3 Category Overview

| # | Category | Angles | Core Question |
|---|----------|--------|---------------|
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
| | **Total** | **37** | |

---

## 2. Quality Model (10 Categories)

### A. Functional Quality (3 angles)

> Does it do what it should?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| A1 | **Correctness** | Does it work as specified? | Logic, calculations, behavior |
| A2 | **Completeness** | Are all requirements met? | Coverage, edge cases |
| A3 | **Appropriateness** | Does it fit the purpose? | Fitness for use |

### B. Reliability (4 angles)

> Does it work consistently over time?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| B1 | **Maturity** | How stable is it? | Defect density, failure rate |
| B2 | **Availability** | Is it accessible when needed? | Uptime, SLA compliance |
| B3 | **Fault Tolerance** | Does it handle failures? | Graceful degradation |
| B4 | **Recoverability** | Can it recover from failures? | Recovery time, data loss |

### C. Performance (3 angles)

> Is it fast and efficient?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| C1 | **Time Efficiency** | How fast is it? | Response time, throughput |
| C2 | **Resource Efficiency** | Does it use resources wisely? | CPU, memory, storage |
| C3 | **Capacity** | Can it handle the load? | Scalability, limits |

### D. Maintainability (5 angles)

> Is it easy to understand and change?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| D1 | **Modularity** | Is it well-structured? | Coupling, cohesion |
| D2 | **Reusability** | Can components be reused? | Abstraction, generality |
| D3 | **Analyzability** | Is it easy to understand? | Clarity, documentation |
| D4 | **Modifiability** | Is it easy to change? | Impact of changes |
| D5 | **Testability** | Is it easy to test? | Test coverage, isolation |

### E. Portability (3 angles)

> Can it work in different environments?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| E1 | **Adaptability** | Can it adapt to new environments? | Configuration, flexibility |
| E2 | **Installability** | Is it easy to deploy? | Setup complexity |
| E3 | **Replaceability** | Can components be substituted? | Interface stability |

### F. Security (5 angles)

> Is it protected from threats?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| F1 | **Confidentiality** | Is data protected from exposure? | Encryption, access control |
| F2 | **Integrity** | Is data protected from tampering? | Validation, checksums |
| F3 | **Non-repudiation** | Can actions be proven? | Audit trails, signatures |
| F4 | **Accountability** | Can actions be traced? | Logging, attribution |
| F5 | **Authenticity** | Is identity verified? | Authentication, authorization |

### G. Compatibility (2 angles)

> Does it work with other systems?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| G1 | **Co-existence** | Can it run alongside others? | Resource sharing, isolation |
| G2 | **Interoperability** | Can it exchange data? | APIs, protocols, standards |

### H. Usability (6 angles)

> Is it easy and pleasant to use?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| H1 | **Recognizability** | Is purpose clear? | First impressions, clarity |
| H2 | **Learnability** | Is it easy to learn? | Onboarding, documentation |
| H3 | **Operability** | Is it easy to operate? | Workflow efficiency |
| H4 | **Error Protection** | Does it prevent mistakes? | Validation, confirmation |
| H5 | **Aesthetics** | Is it visually appealing? | Design quality |
| H6 | **Accessibility** | Can everyone use it? | WCAG, inclusive design |

### I. Data Quality (3 angles)

> Is the data trustworthy?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| I1 | **Accuracy** | Is data correct? | Validation, verification |
| I2 | **Freshness** | Is data current? | Update frequency, staleness |
| I3 | **Privacy** | Is personal data protected? | GDPR, consent, anonymization |

### J. AI/ML Quality (3 angles)

> Is AI behavior reliable and ethical?

| # | Angle | Key Question | Evaluation Focus |
|---|-------|--------------|------------------|
| J1 | **Model Accuracy** | Are predictions correct? | Metrics, validation |
| J2 | **Fairness** | Is it free from bias? | Bias detection, mitigation |
| J3 | **Explainability** | Can decisions be explained? | Interpretability, transparency |

---

## 3. Complete Angle Reference

### 3.1 All 37 Angles by Category

| Cat | # | Angle | Cat | # | Angle |
|-----|---|-------|-----|---|-------|
| A | 1 | Correctness | F | 1 | Confidentiality |
| A | 2 | Completeness | F | 2 | Integrity |
| A | 3 | Appropriateness | F | 3 | Non-repudiation |
| B | 1 | Maturity | F | 4 | Accountability |
| B | 2 | Availability | F | 5 | Authenticity |
| B | 3 | Fault Tolerance | G | 1 | Co-existence |
| B | 4 | Recoverability | G | 2 | Interoperability |
| C | 1 | Time Efficiency | H | 1 | Recognizability |
| C | 2 | Resource Efficiency | H | 2 | Learnability |
| C | 3 | Capacity | H | 3 | Operability |
| D | 1 | Modularity | H | 4 | Error Protection |
| D | 2 | Reusability | H | 5 | Aesthetics |
| D | 3 | Analyzability | H | 6 | Accessibility |
| D | 4 | Modifiability | I | 1 | Accuracy |
| D | 5 | Testability | I | 2 | Freshness |
| E | 1 | Adaptability | I | 3 | Privacy |
| E | 2 | Installability | J | 1 | Model Accuracy |
| E | 3 | Replaceability | J | 2 | Fairness |
| | | | J | 3 | Explainability |

### 3.2 Angle ID Format

Format: `[Category Letter][Number]` (e.g., A1, B2, F3)

| Category | Letter | Angles |
|----------|--------|--------|
| Functional | A | A1-A3 |
| Reliability | B | B1-B4 |
| Performance | C | C1-C3 |
| Maintainability | D | D1-D5 |
| Portability | E | E1-E3 |
| Security | F | F1-F5 |
| Compatibility | G | G1-G2 |
| Usability | H | H1-H6 |
| Data Quality | I | I1-I3 |
| AI/ML Quality | J | J1-J3 |

---

## 4. Dynamic Angle Activation

### 4.1 Activation by Committee Level

| Level | Categories | Angles | Selection Rule |
|-------|------------|--------|----------------|
| **L1** | A | 3 | Functional only |
| **L2** | A, B, D | 12 | + Reliability, Maintainability |
| **L3** | A-F | 23 | + Performance, Portability, Security |
| **L4** | A-H | 31 | + Compatibility, Usability |
| **L5** | A-J | 37 | All categories |

### 4.2 Activation by Problem Domain

| Domain | Required Categories | Key Angles |
|--------|---------------------|------------|
| **Architecture** | A, B, C, D, E, G | A1, B2, C3, D1, E1, G2 |
| **Feature** | A, H | A1, A2, H1-H6 |
| **Security** | A, F, I | A1, F1-F5, I3 |
| **Performance** | A, B, C | A1, B2, C1-C3 |
| **Data** | A, F, I, J | A1, F2, I1-I3, J1-J3 |
| **Operations** | A, B, E | A1, B1-B4, E2 |

### 4.3 Dynamic Adjustment Protocol

| Trigger | Action | Example |
|---------|--------|---------|
| **Security concern** | Add F (Security) | Data exposure found → F1-F5 |
| **Performance issue** | Add C (Performance) | Slow response → C1-C3 |
| **User feedback** | Add H (Usability) | Confusion reported → H1-H6 |
| **Data problem** | Add I (Data Quality) | Stale data → I1-I3 |
| **AI involved** | Add J (AI/ML) | Model used → J1-J3 |

### 4.4 Minimum Coverage Rules

| Rule | Requirement |
|------|-------------|
| **Always include** | A1 (Correctness) |
| **L2+ include** | B2 (Availability), D5 (Testability) |
| **Security-sensitive** | F1-F5 (all Security) |
| **User-facing** | H1-H6 (all Usability) |

---

## 5. Angle-Role Mapping

### 5.1 Primary Ownership

| Category | Primary Expert Roles |
|----------|----------------------|
| A (Functional) | QA, Developer, Domain Expert |
| B (Reliability) | SRE, DevOps, Operations |
| C (Performance) | Architect, Backend, DBA |
| D (Maintainability) | Architect, Tech Lead, Developer |
| E (Portability) | DevOps, Architect |
| F (Security) | Security, Compliance, Privacy |
| G (Compatibility) | Architect, Backend |
| H (Usability) | UX, PM, Support |
| I (Data Quality) | Data Engineer, Privacy, DBA |
| J (AI/ML Quality) | ML Engineer, Data Analyst |

### 5.2 Role-Category Weight Matrix

| Role | A | B | C | D | E | F | G | H | I | J |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Architect | ● | ○ | ● | ● | ● | ○ | ● | · | · | · |
| Backend | ● | ○ | ● | ● | · | · | ● | · | · | · |
| Frontend | ● | · | · | ○ | · | · | · | ● | · | · |
| QA | ● | ○ | · | ● | · | · | · | ○ | · | · |
| DevOps | · | ● | ○ | · | ● | ○ | · | · | · | · |
| Security | ○ | · | · | · | · | ● | · | · | ○ | · |
| PM | ○ | · | · | · | · | · | · | ● | · | · |
| UX | · | · | · | · | · | · | · | ● | · | · |
| Data Eng | · | · | · | · | · | · | · | · | ● | ○ |
| ML Eng | · | · | · | · | · | · | · | · | ○ | ● |

Legend: ● Primary (0.9) | ○ Secondary (0.6) | · Minimal (0.2)

---

## 6. Evaluation Templates

> **SSOT**: All evaluation templates → `.knowledge/templates/EXPERT_COMMITTEE.md`

### 6.1 Available Templates

| Level | Angles | Template |
|-------|--------|----------|
| L1 | 3 | Quick Check — A1-A3 |
| L2 | 12 | Standard — A + B + D |
| L3 | 23 | Deep — A-H selective |
| L4 | 31 | Comprehensive — A-H full |
| L5 | 37 | Full — All categories |

### 6.2 Usage

1. **Select Level** — Match problem complexity to angle count
2. **Get Template** — Copy from `templates/EXPERT_COMMITTEE.md`
3. **Score Angles** — Use 1-5 scale per Section 4
4. **Record** — Document per Section 5 mapping

---

## Related

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Expert committee framework
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert role personas (SSOT)
- `.knowledge/guidelines/QUALITY.md` — Quality guidelines

---

*AI Collaboration Knowledge Base*
