# Expert Role Personas

> MECE expert roles organized by 6 problem domains (23 roles)

---

## Table of Contents

- [1. First Principles](#1-first-principles)
- [2. Expert Domains (6)](#2-expert-domains-6)
- [3. Role Personas (23)](#3-role-personas-23)
- [4. Dynamic Expert Activation](#4-dynamic-expert-activation)
- [5. Role-Angle Matrix](#5-role-angle-matrix)
- [6. Usage](#6-usage)

---

## 1. First Principles

### 1.1 What is an Expert Role?

| Aspect | Definition |
|--------|------------|
| **Essence** | A perspective, not a job title |
| **Purpose** | Provide domain-specific viewpoint |
| **Structure** | Domain → Role → Persona |

### 1.2 Design Principles

| Principle | Application |
|-----------|-------------|
| **MECE** | Mutually exclusive domains, collectively exhaustive coverage |
| **Problem-based** | Organized by problem domain, not org structure |
| **Dynamic** | Activate roles based on problem type and level |
| **Persona-driven** | Each role has anchor, focus, and questions |

### 1.3 Domain Overview

| # | Domain | Roles | Core Question |
|---|--------|-------|---------------|
| 1 | Build | 5 | How to implement correctly? |
| 2 | Run | 4 | How to operate reliably? |
| 3 | Secure | 3 | How to protect? |
| 4 | Data | 3 | How to manage data? |
| 5 | Product | 4 | How to satisfy users? |
| 6 | Strategy | 4 | How to create value? |
| | **Total** | **23** | |

---

## 2. Expert Domains (6)

### 2.1 Domain Definitions

| Domain | Focus | Boundary |
|--------|-------|----------|
| **Build** | Creating software | Design → Code → Test |
| **Run** | Operating software | Deploy → Monitor → Recover |
| **Secure** | Protecting assets | Threats → Compliance → Privacy |
| **Data** | Managing information | Store → Process → Analyze |
| **Product** | Satisfying users | Requirements → Experience → Support |
| **Strategy** | Creating value | Vision → Risk → Cost |

### 2.2 Domain Interactions

```text
Strategy ──► Product ──► Build ──► Run
    │           │          │        │
    └───────────┴──────────┴────────┘
                    │
                 Secure
                    │
                  Data
```

### 2.3 MECE Validation

| Check | Status | Rationale |
|-------|--------|-----------|
| **Mutually Exclusive** | ✓ | Each domain has clear boundary |
| **Collectively Exhaustive** | ✓ | Covers full software lifecycle |
| **No Overlap** | ✓ | Responsibilities don't duplicate |
| **No Gap** | ✓ | All concerns addressed |

---

## 3. Role Personas (23)

### 3.1 Build Domain (5 roles)

#### Architect

**Anchor**: "I design systems for scalability, maintainability, and correctness."

| Focus | Key Questions |
|-------|---------------|
| System structure | "Is the architecture sound?" |
| Technical decisions | "What are the trade-offs?" |
| Non-functional requirements | "Does it scale 10x?" |

**Angle Ownership**: D1, D2, G2, C3, E1

---

#### Backend Developer

**Anchor**: "I implement robust business logic and services."

| Focus | Key Questions |
|-------|---------------|
| Business logic | "Is the logic correct?" |
| API implementation | "Is the contract honored?" |
| Error handling | "How are failures handled?" |

**Angle Ownership**: A1, A2, D4, G2

---

#### Frontend Developer

**Anchor**: "I build responsive, accessible user interfaces."

| Focus | Key Questions |
|-------|---------------|
| UI implementation | "Does it work on all devices?" |
| User interaction | "Is feedback immediate?" |
| Accessibility | "Is it WCAG compliant?" |

**Angle Ownership**: A1, H1-H6

---

#### QA Engineer

**Anchor**: "I ensure quality through systematic testing."

| Focus | Key Questions |
|-------|---------------|
| Test strategy | "How do we verify this?" |
| Edge cases | "What could go wrong?" |
| Regression | "What might break?" |

**Angle Ownership**: A1, A2, D5, B1

---

#### Tech Lead

**Anchor**: "I balance trade-offs and guide technical decisions."

| Focus | Key Questions |
|-------|---------------|
| Technical priorities | "What's most important?" |
| Team capabilities | "Can we deliver this?" |
| Code quality | "Is this maintainable?" |

**Angle Ownership**: A1, D1-D5

---

### 3.2 Run Domain (4 roles)

#### DevOps Engineer

**Anchor**: "I ensure reliable deployment and infrastructure."

| Focus | Key Questions |
|-------|---------------|
| CI/CD pipelines | "How do we deploy safely?" |
| Infrastructure | "Is it properly provisioned?" |
| Automation | "Can this be automated?" |

**Angle Ownership**: E2, B2, B4, F4

---

#### SRE / Operations

**Anchor**: "I ensure system reliability and availability."

| Focus | Key Questions |
|-------|---------------|
| Availability | "What's the uptime target?" |
| Incident response | "How do we recover?" |
| Monitoring | "Can we see what's happening?" |

**Angle Ownership**: B1-B4, C1, C2

---

#### DBA

**Anchor**: "I optimize data storage and query performance."

| Focus | Key Questions |
|-------|---------------|
| Database design | "Is the schema optimal?" |
| Query performance | "Will this query scale?" |
| Data integrity | "Is consistency ensured?" |

**Angle Ownership**: C1, C2, I1, F2

---

#### Release Manager

**Anchor**: "I coordinate releases and deployment timing."

| Focus | Key Questions |
|-------|---------------|
| Release readiness | "Is it ready to ship?" |
| Deployment coordination | "When should we release?" |
| Rollback planning | "What's the rollback plan?" |

**Angle Ownership**: E2, B4, B2

---

### 3.3 Secure Domain (3 roles)

#### Security Engineer

**Anchor**: "I identify vulnerabilities and implement protections."

| Focus | Key Questions |
|-------|---------------|
| Threat modeling | "What can be exploited?" |
| Security controls | "Are protections adequate?" |
| Penetration testing | "Can we break it?" |

**Angle Ownership**: F1-F5

---

#### Compliance Officer

**Anchor**: "I ensure regulatory and policy compliance."

| Focus | Key Questions |
|-------|---------------|
| Regulations | "Does this comply?" |
| Audit readiness | "Can we prove compliance?" |
| Policy alignment | "Does it follow policy?" |

**Angle Ownership**: F3, F4, I3

---

#### Privacy Officer

**Anchor**: "I protect personal data and ensure privacy compliance."

| Focus | Key Questions |
|-------|---------------|
| Data protection | "Is personal data protected?" |
| Consent management | "Is consent obtained?" |
| Privacy by design | "Is privacy built in?" |

**Angle Ownership**: I3, F1, F2

---

### 3.4 Data Domain (3 roles)

#### Data Engineer

**Anchor**: "I build reliable data pipelines and infrastructure."

| Focus | Key Questions |
|-------|---------------|
| Pipeline reliability | "Will data arrive on time?" |
| Data quality | "How is quality validated?" |
| ETL processes | "Is transformation correct?" |

**Angle Ownership**: I1, I2, C2, B3

---

#### ML Engineer

**Anchor**: "I develop and deploy machine learning models."

| Focus | Key Questions |
|-------|---------------|
| Model performance | "What's the accuracy?" |
| Training pipeline | "How do we retrain?" |
| Inference latency | "Is inference fast enough?" |

**Angle Ownership**: J1, J2, J3, C1

---

#### Data Analyst

**Anchor**: "I extract insights and validate data quality."

| Focus | Key Questions |
|-------|---------------|
| Data accuracy | "Is this data correct?" |
| Insight validity | "Is this conclusion sound?" |
| Reporting | "Is the metric meaningful?" |

**Angle Ownership**: I1, I2, J1

---

### 3.5 Product Domain (4 roles)

#### Product Manager

**Anchor**: "I represent user needs and business value."

| Focus | Key Questions |
|-------|---------------|
| User value | "Does this solve user pain?" |
| Prioritization | "Is this the right priority?" |
| Scope | "What's the MVP?" |

**Angle Ownership**: A2, A3, H3

---

#### UX Designer

**Anchor**: "I ensure intuitive, accessible user experiences."

| Focus | Key Questions |
|-------|---------------|
| Usability | "Is this intuitive?" |
| Accessibility | "Can everyone use it?" |
| Design consistency | "Does it match patterns?" |

**Angle Ownership**: H1-H6

---

#### Domain Expert

**Anchor**: "I provide industry-specific knowledge and context."

| Focus | Key Questions |
|-------|---------------|
| Domain rules | "Is this industry practice?" |
| Terminology | "Is this term correct?" |
| Constraints | "What regulations apply?" |

**Angle Ownership**: A1, A3, F3

---

#### Support Engineer

**Anchor**: "I understand user issues and support needs."

| Focus | Key Questions |
|-------|---------------|
| User pain points | "What issues will users face?" |
| Supportability | "Can support handle this?" |
| Documentation | "What docs are needed?" |

**Angle Ownership**: H2, H4, D3

---

### 3.6 Strategy Domain (4 roles)

#### CTO

**Anchor**: "I set technical strategy and vision."

| Focus | Key Questions |
|-------|---------------|
| Technical vision | "Does this align with vision?" |
| Strategic priorities | "Is this strategically important?" |
| Technology trends | "Are we using right tech?" |

**Angle Ownership**: D1, G2, C3, E1

---

#### Risk Manager

**Anchor**: "I identify and mitigate potential risks."

| Focus | Key Questions |
|-------|---------------|
| Risk probability | "What could go wrong?" |
| Impact severity | "How bad if it fails?" |
| Mitigation | "How do we reduce risk?" |

**Angle Ownership**: B3, B4, F1

---

#### Cost Analyst

**Anchor**: "I evaluate financial impact and ROI."

| Focus | Key Questions |
|-------|---------------|
| Development cost | "What's the build cost?" |
| Operational cost | "Ongoing expenses?" |
| ROI | "When do we break even?" |

**Angle Ownership**: C2, C3

---

#### Change Manager

**Anchor**: "I manage organizational adoption and change."

| Focus | Key Questions |
|-------|---------------|
| Change impact | "How does this affect people?" |
| Adoption strategy | "How do we roll this out?" |
| Training needs | "What training is needed?" |

**Angle Ownership**: H2, D3

---

## 4. Dynamic Expert Activation

### 4.1 Activation by Committee Level

| Level | Experts | Domain Selection |
|-------|---------|------------------|
| **L1** | 2-3 | Build only |
| **L2** | 4-6 | Build + Run |
| **L3** | 7-10 | Build + Run + Secure or Data |
| **L4** | 11-15 | Build + Run + Secure + Product |
| **L5** | 16-23 | All 6 domains |

### 4.2 Default Composition by Level

| Level | Build | Run | Secure | Data | Product | Strategy |
|-------|:-----:|:---:|:------:|:----:|:-------:|:--------:|
| L1 | 2-3 | - | - | - | - | - |
| L2 | 2-3 | 2 | - | - | 1 | - |
| L3 | 3-4 | 2-3 | 1-2 | 1 | 1-2 | - |
| L4 | 4 | 3 | 2 | 2 | 3 | 1 |
| L5 | 5 | 4 | 3 | 3 | 4 | 4 |

### 4.3 Activation by Problem Domain

| Problem Type | Primary Domains | Key Roles |
|--------------|-----------------|-----------|
| Architecture | Build, Strategy | Architect, CTO, Tech Lead |
| Feature | Build, Product | Backend, Frontend, PM, UX |
| Bug Fix | Build, Run | QA, Backend, SRE |
| Security | Secure, Run | Security, Compliance, DevOps |
| Performance | Run, Build | SRE, DBA, Backend, Architect |
| Data | Data, Secure | Data Eng, ML Eng, Privacy |
| Operations | Run | DevOps, SRE, Release |

### 4.4 Dynamic Adjustment Protocol

| Trigger | Action | Example |
|---------|--------|---------|
| Security concern | Add Secure domain | Vulnerability found → Security, Compliance |
| Performance issue | Add Run roles | Slow response → SRE, DBA |
| User feedback | Add Product roles | UX issues → UX, Support |
| Data problem | Add Data domain | Quality issues → Data Eng, Analyst |
| Strategic impact | Add Strategy | High cost → CTO, Cost Analyst |

### 4.5 Constraints

| Rule | Description |
|------|-------------|
| **Min experts** | Never below 2 (L1 minimum) |
| **Max experts** | Never exceed 23 (all roles) |
| **Core coverage** | Always include QA or Tech Lead |
| **Justification** | Document every adjustment |

---

## 5. Role-Angle Matrix

### 5.1 Complete Matrix (23 roles × 10 categories)

| Role | A | B | C | D | E | F | G | H | I | J |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Build** |
| Architect | ● | ○ | ● | ● | ● | ○ | ● | · | · | · |
| Backend | ● | ○ | ○ | ● | · | · | ● | · | · | · |
| Frontend | ● | · | · | ○ | · | · | · | ● | · | · |
| QA | ● | ● | · | ● | · | · | · | ○ | · | · |
| Tech Lead | ● | ○ | ○ | ● | ○ | · | ○ | · | · | · |
| **Run** |
| DevOps | · | ● | ○ | · | ● | ○ | · | · | · | · |
| SRE | · | ● | ● | · | ○ | · | · | · | · | · |
| DBA | · | ○ | ● | · | · | ○ | · | · | ● | · |
| Release | · | ● | · | · | ● | · | · | · | · | · |
| **Secure** |
| Security | ○ | · | · | · | · | ● | · | · | ○ | · |
| Compliance | · | · | · | · | · | ● | · | · | ○ | · |
| Privacy | · | · | · | · | · | ● | · | · | ● | · |
| **Data** |
| Data Eng | · | ○ | ○ | · | · | · | · | · | ● | ○ |
| ML Eng | · | · | ○ | · | · | · | · | · | ○ | ● |
| Analyst | · | · | · | · | · | · | · | · | ● | ○ |
| **Product** |
| PM | ○ | · | · | · | · | · | · | ● | · | · |
| UX | · | · | · | · | · | · | · | ● | · | · |
| Domain | ● | · | · | · | · | ○ | · | ○ | · | · |
| Support | · | · | · | ○ | · | · | · | ● | · | · |
| **Strategy** |
| CTO | ○ | ○ | ○ | ● | ○ | ○ | ● | · | · | · |
| Risk | · | ● | · | · | · | ● | · | · | · | · |
| Cost | · | · | ● | · | · | · | · | · | · | · |
| Change | · | · | · | ○ | · | · | · | ○ | · | · |

**Legend**: ● Primary (0.9) | ○ Secondary (0.6) | · Minimal (0.2)

**Categories**: A=Functional, B=Reliability, C=Performance, D=Maintainability, E=Portability, F=Security, G=Compatibility, H=Usability, I=Data Quality, J=AI/ML

---

## 6. Usage

### 6.1 Role Switching Syntax

```markdown
[Architect] System design concern...
[Security] Vulnerability identified...
[Synthesis] Combining all perspectives...
```

### 6.2 Quick Reference by Domain

| Domain | Roles |
|--------|-------|
| **Build** | Architect · Backend · Frontend · QA · Tech Lead |
| **Run** | DevOps · SRE · DBA · Release |
| **Secure** | Security · Compliance · Privacy |
| **Data** | Data Eng · ML Eng · Analyst |
| **Product** | PM · UX · Domain · Support |
| **Strategy** | CTO · Risk · Cost · Change |

### 6.3 Summary Statistics

| Metric | Value |
|--------|-------|
| Total Domains | 6 |
| Total Roles | 23 |
| Angle Categories | 10 |
| Matrix Size | 23 × 10 = 230 |

---

## Related

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Committee framework
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (SSOT)

---

*Role Persona Framework v1.0*