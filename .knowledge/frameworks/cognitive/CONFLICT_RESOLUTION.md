# Expert Committee Conflict Resolution

> Protocols for resolving disagreements in multi-expert analysis (6 domains × 23 roles)

---

## Table of Contents

- [1. Conflict Types](#1-conflict-types)
- [2. Resolution Protocol](#2-resolution-protocol)
- [3. Voting Weights by Domain](#3-voting-weights-by-domain)
- [4. Complete Role Weight Matrix](#4-complete-role-weight-matrix)
- [5. Deadlock Breakers](#5-deadlock-breakers)
- [6. Devil's Advocate](#6-devils-advocate)
- [7. Decision Attribution](#7-decision-attribution)

---

## 1. Conflict Types

### 1.1 Domain-Based Conflicts

| Type | Description | Authority | Veto Power |
|------|-------------|-----------|------------|
| **Build** | Implementation, architecture | Architect | Tech Lead |
| **Run** | Operations, deployment | DevOps | SRE |
| **Secure** | Security, compliance | Security | Compliance |
| **Data** | Data quality, ML | Data Eng | Privacy |
| **Product** | Features, UX | PM | UX |
| **Strategy** | Vision, cost | CTO | Risk |

### 1.2 Cross-Domain Conflicts

| Conflict | Domains | Resolution |
|----------|---------|------------|
| Tech vs Product | Build ↔ Product | PM + Architect joint decision |
| Security vs UX | Secure ↔ Product | Security wins, UX mitigates |
| Cost vs Quality | Strategy ↔ Build | CTO decides based on context |
| Speed vs Compliance | Run ↔ Secure | Compliance wins |
| Data vs Privacy | Data ↔ Secure | Privacy wins |

---

## 2. Resolution Protocol

### 2.1 Standard Process

```text
1. Identify   → State conflicting positions clearly
2. Classify   → Determine conflict type (domain or cross-domain)
3. Gather     → Collect affected quality angles
4. Weight     → Apply role weights from Section 3-4
5. Vote       → Calculate weighted scores
6. Decide     → Apply threshold or authority
7. Record     → Document rationale + dissent
```

### 2.2 Escalation Triggers

| Trigger | Action |
|---------|--------|
| 50/50 split | Apply deadlock breaker (Section 5) |
| Security concern | Security veto applies |
| Compliance issue | Compliance veto applies |
| No clear winner | Escalate to higher authority |
| Cross-domain conflict | Form mini-committee |

### 2.3 Vote Thresholds

| Score | Decision | Action |
|-------|----------|--------|
| >0.7 | **Approve** | Proceed |
| 0.5-0.7 | **Conditional** | Address concerns first |
| 0.3-0.5 | **Revise** | Significant changes needed |
| <0.3 | **Reject** | Do not proceed |

---

## 3. Voting Weights by Domain

### 3.1 Build Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | Architect, Tech Lead |
| **0.7** | Backend, QA |
| **0.5** | Frontend, DevOps |
| **0.3** | PM, UX |

### 3.2 Run Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | DevOps, SRE |
| **0.7** | DBA, Release, Security |
| **0.5** | Backend, Architect |
| **0.3** | PM, Frontend |

### 3.3 Secure Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | Security, Compliance, Privacy |
| **0.7** | DevOps, Risk, CTO |
| **0.5** | Architect, DBA |
| **0.3** | PM, UX |

### 3.4 Data Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | Data Eng, ML Eng, Analyst |
| **0.7** | DBA, Privacy, Backend |
| **0.5** | Architect, Security |
| **0.3** | PM, UX |

### 3.5 Product Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | PM, UX, Domain |
| **0.7** | Support, Frontend, QA |
| **0.5** | Tech Lead, Backend |
| **0.3** | DevOps, DBA |

### 3.6 Strategy Decisions

| Weight | Roles |
|--------|-------|
| **0.9** | CTO, Risk, Cost |
| **0.7** | Change, PM, Architect |
| **0.5** | Tech Lead, Security |
| **0.3** | Individual contributors |

---

## 4. Complete Role Weight Matrix

### 4.1 Build Domain (5 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| Architect | 0.9 | 0.5 | 0.5 | 0.5 | 0.3 | 0.7 |
| Backend | 0.7 | 0.5 | 0.3 | 0.7 | 0.5 | 0.3 |
| Frontend | 0.5 | 0.3 | 0.3 | 0.3 | 0.7 | 0.3 |
| QA | 0.7 | 0.5 | 0.3 | 0.3 | 0.7 | 0.3 |
| Tech Lead | 0.9 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |

### 4.2 Run Domain (4 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| DevOps | 0.5 | 0.9 | 0.7 | 0.5 | 0.3 | 0.3 |
| SRE | 0.5 | 0.9 | 0.5 | 0.5 | 0.3 | 0.3 |
| DBA | 0.5 | 0.7 | 0.5 | 0.9 | 0.3 | 0.3 |
| Release | 0.5 | 0.7 | 0.5 | 0.3 | 0.5 | 0.3 |

### 4.3 Secure Domain (3 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| Security | 0.5 | 0.7 | 0.9 | 0.5 | 0.3 | 0.5 |
| Compliance | 0.3 | 0.5 | 0.9 | 0.5 | 0.3 | 0.5 |
| Privacy | 0.3 | 0.3 | 0.9 | 0.9 | 0.3 | 0.5 |

### 4.4 Data Domain (3 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| Data Eng | 0.3 | 0.5 | 0.5 | 0.9 | 0.3 | 0.3 |
| ML Eng | 0.3 | 0.5 | 0.3 | 0.9 | 0.5 | 0.5 |
| Analyst | 0.3 | 0.3 | 0.3 | 0.9 | 0.5 | 0.5 |

### 4.5 Product Domain (4 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| PM | 0.3 | 0.3 | 0.3 | 0.3 | 0.9 | 0.7 |
| UX | 0.3 | 0.3 | 0.3 | 0.3 | 0.9 | 0.3 |
| Domain | 0.5 | 0.3 | 0.5 | 0.5 | 0.9 | 0.5 |
| Support | 0.3 | 0.5 | 0.3 | 0.3 | 0.7 | 0.3 |

### 4.6 Strategy Domain (4 roles)

| Role | Build | Run | Secure | Data | Product | Strategy |
|------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| CTO | 0.7 | 0.7 | 0.7 | 0.5 | 0.7 | 0.9 |
| Risk | 0.3 | 0.5 | 0.7 | 0.5 | 0.5 | 0.9 |
| Cost | 0.3 | 0.5 | 0.3 | 0.3 | 0.5 | 0.9 |
| Change | 0.3 | 0.3 | 0.3 | 0.3 | 0.5 | 0.7 |

### 4.7 Role-Angle Weight Matrix (Sparse)

> Default weight = 0.2. Only weights ≥0.5 listed below.

| Role | Primary Angles (0.9) | Secondary Angles (0.6) |
|------|----------------------|------------------------|
| Architect | D1, D2, E1, G2 | C3, A1 |
| Backend | A1, A2, D4 | G2, C1 |
| Frontend | H1-H6 | A1 |
| QA | A1, A2, D5 | B1 |
| Tech Lead | D1-D5 | A1 |
| DevOps | E2, B2, B4 | F4 |
| SRE | B1-B4 | C1, C2 |
| DBA | C1, C2, I1 | F2 |
| Release | E2, B4 | B2 |
| Security | F1-F5 | — |
| Compliance | F3, F4, I3 | — |
| Privacy | I3, F1, F2 | — |
| Data Eng | I1, I2, B3 | C2 |
| ML Eng | J1-J3 | C1 |
| Analyst | I1, I2, J1 | — |
| PM | A2, A3, H3 | — |
| UX | H1-H6 | — |
| Domain | A1, A3, F3 | — |
| Support | H2, H4, D3 | — |
| CTO | D1, G2, C3, E1 | — |
| Risk | B3, B4, F1 | — |
| Cost | C2, C3 | — |
| Change | D4, H2, H3 | — |

**Matrix Statistics**:

| Category | Cells | Percentage |
|----------|:-----:|:----------:|
| Primary (0.9) | ~92 | 11% |
| Secondary (0.6) | ~46 | 5% |
| Default (0.2) | ~713 | 84% |
| **Total** | **851** | **100%** |

---

## 5. Deadlock Breakers

### 5.1 Authority Chain by Domain

| Domain | Final Authority | Escalation Path |
|--------|-----------------|-----------------|
| Build | Architect | → Tech Lead → CTO |
| Run | DevOps | → SRE → CTO |
| Secure | Security | → Compliance → CTO |
| Data | Data Eng | → Privacy → CTO |
| Product | PM | → Domain → CTO |
| Strategy | CTO | → Risk → Board |

### 5.2 Tiebreaker Rules (Priority Order)

| Priority | Rule | Rationale |
|----------|------|-----------|
| 1 | **Reversibility** | Prefer reversible option |
| 2 | **Risk** | Prefer lower-risk option |
| 3 | **信 (Faithfulness)** | Prefer correctness over elegance |
| 4 | **Security** | Security concerns take precedence |
| 5 | **Minimal change** | Prefer smaller scope |
| 6 | **User impact** | Minimize negative user impact |

### 5.3 Cross-Domain Resolution

| Conflict | Resolution Method |
|----------|-------------------|
| Build ↔ Product | Joint PM + Architect decision |
| Secure ↔ Product | Security wins, Product mitigates |
| Strategy ↔ Build | CTO decides with Architect input |
| Run ↔ Secure | Compliance wins |
| Data ↔ Secure | Privacy wins |

---

## 6. Devil's Advocate

### 6.1 Mandatory Opposition

Every committee analysis **must** include:

| Requirement | Count | Purpose |
|-------------|-------|---------|
| Explicit dissent | 1+ | Ensure alternatives considered |
| Potential risks | 3+ | Force risk awareness |
| Worst-case scenario | 1 | Prepare for failure |
| Alternative approach | 1+ | Avoid tunnel vision |

### 6.2 Devil's Advocate Assignment

| Committee Size | DA Count | Selection |
|----------------|----------|-----------|
| 2-5 | 1 | Rotate among members |
| 6-10 | 2 | Include Risk |
| 11-23 | 3 | Risk + Security + Domain |

### 6.3 Dissent Recording

> **Template**: `.knowledge/templates/DECISION_RECORDS.md#2-dissent-record`

Each dissent record must include: Role, Domain, Position, Rationale, Risk, Mitigation.

---

## 7. Decision Attribution

### 7.1 Record Template

| Decision Point | Supporters | Dissenters | Weight Score | Deciding Factor |
|----------------|------------|------------|:------------:|-----------------|
| [Decision] | [Roles] | [Roles] | 0.0-1.0 | [Key reason] |

### 7.2 Confidence Levels

| Consensus | Confidence | Interpretation | Action |
|-----------|:----------:|----------------|--------|
| Unanimous | 95%+ | Strong agreement | Proceed confidently |
| Strong (>80%) | 80-95% | Clear direction | Proceed, monitor |
| Majority (60-80%) | 60-80% | General agreement | Proceed with caution |
| Split (40-60%) | 40-60% | Divided opinion | Seek more input |
| Contested (<40%) | <40% | No agreement | Escalate or defer |

### 7.3 Attribution Tracking

> **Templates**: `.knowledge/templates/DECISION_RECORDS.md`
> - Decision Record → Section 3
> - Attribution Summary → Section 4

---

## Related

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Committee framework
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert personas (SSOT)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)
- `.knowledge/frameworks/autonomy/LEVELS.md` — Autonomy levels

---

*AI Collaboration Knowledge Base*
