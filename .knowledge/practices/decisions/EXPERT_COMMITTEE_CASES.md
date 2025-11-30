# Expert Committee Case Studies



> Real-world examples of expert committee decisions at different levels



---



## Table of Contents



- [1. Overview](#1-overview)

- [2. L1 Cases: Quick Check](#2-l1-cases-quick-check)

- [3. L2 Cases: Standard Review](#3-l2-cases-standard-review)

- [4. L3 Cases: Deep Analysis](#4-l3-cases-deep-analysis)

- [5. L4 Cases: Comprehensive Review](#5-l4-cases-comprehensive-review)

- [6. L5 Cases: Full Committee](#6-l5-cases-full-committee)

- [7. Lessons Learned](#7-lessons-learned)



---



## 1. Overview



### 1.1 Purpose



| Goal | Description |

|------|-------------|

| **Learn by Example** | Understand framework application through real cases |

| **Pattern Recognition** | Identify when to use which level |

| **Pitfall Avoidance** | Learn from documented mistakes |



### 1.2 Case Structure



Each case includes:

- Context and decision scope

- Committee composition

- Scoring summary

- Decision outcome

- Lessons learned



---



## 2. L1 Cases: Quick Check



### Case L1-1: Login Button Bug Fix



**Context**: Login button unresponsive on mobile Safari



| Aspect | Detail |

|--------|--------|

| **Scope** | Single component fix |

| **Risk** | Low (easily reversible) |

| **Impact** | 1 team |



**Committee**: Engineer, QA (2 experts)



**Scoring**:



| Angle | Engineer | QA | Weighted |

|-------|:--------:|:--:|:--------:|

| A1 Correctness | 5 | 5 | 5.0 |

| D3 Analyzability | 4 | 4 | 4.0 |

| D5 Testability | 5 | 4 | 4.5 |



**Result**: S=4.5, σ=0.41, S_enhanced=4.01, CI=[3.6, 4.4]



**Decision**: ✅ Strong Approve (CI_lower > 3.5)



**Lesson**: Simple bugs with clear fixes are ideal L1 candidates.



---



### Case L1-2: Config Timeout Adjustment



**Context**: Increase API timeout from 30s to 60s



| Aspect | Detail |

|--------|--------|

| **Scope** | Configuration change |

| **Risk** | Low |

| **Impact** | Single service |



**Committee**: Backend, DevOps (2 experts)



**Scoring**:



| Angle | Backend | DevOps | Weighted |

|-------|:-------:|:------:|:--------:|

| A1 Correctness | 5 | 5 | 5.0 |

| B2 Availability | 4 | 5 | 4.5 |

| C1 Time Efficiency | 3 | 4 | 3.5 |



**Result**: S=4.3, σ=0.62, S_enhanced=3.56, CI=[2.9, 3.8]



**Decision**: ⚠️ Conditional Approve — Monitor for performance regression



**Lesson**: Even simple config changes need performance angle review.



---



## 3. L2 Cases: Standard Review



### Case L2-1: New REST Endpoint



**Context**: Add user preferences API endpoint



| Aspect | Detail |

|--------|--------|

| **Scope** | New feature, backward compatible |

| **Risk** | Medium |

| **Impact** | 2 teams (Backend, Frontend) |



**Committee**: Architect, Backend, QA, PM (4 experts)



**Scoring Summary** (12 angles):



| Category | Avg Score | Key Concerns |

|----------|:---------:|--------------|

| A (Functional) | 4.5 | — |

| B (Reliability) | 4.0 | Rate limiting needed |

| D (Maintainability) | 4.2 | — |



**Result**: S=4.2, σ=0.35, S_enhanced=3.89, CI=[3.5, 4.3]



**Decision**: ✅ Conditional Approve — Add rate limiting before release



**Lesson**: API changes benefit from early PM involvement for scope clarity.



---



### Case L2-2: Library Upgrade (Minor Version)



**Context**: Upgrade React 18.2 → 18.3



| Aspect | Detail |

|--------|--------|

| **Scope** | Dependency update |

| **Risk** | Medium (backward compatible) |

| **Impact** | Frontend team |



**Committee**: Frontend, QA, Tech Lead, DevOps (4 experts)



**Scoring Summary**:



| Category | Avg Score | Key Concerns |

|----------|:---------:|--------------|

| A (Functional) | 4.8 | — |

| B (Reliability) | 4.0 | Need regression tests |

| D (Maintainability) | 4.5 | Better debugging |



**Result**: S=4.4, σ=0.31, S_enhanced=4.12, CI=[3.8, 4.6]



**Decision**: ✅ Strong Approve



**Lesson**: Minor version upgrades with good test coverage are low risk.



---



## 4. L3 Cases: Deep Analysis



### Case L3-1: Microservice Extraction



**Context**: Extract payment processing into separate service



| Aspect | Detail |

|--------|--------|

| **Scope** | Major refactoring |

| **Risk** | High |

| **Impact** | Department (3 teams) |



**Committee**: Architect, Backend×2, QA, DevOps, Security, PM (7 experts)



**Scoring Summary** (23 angles):



| Category | Avg | Key Issues |

|----------|:---:|------------|

| A (Functional) | 4.3 | API contract clarity |

| B (Reliability) | 3.8 | Network partition handling |

| C (Performance) | 3.5 | Latency increase concern |

| D (Maintainability) | 4.5 | Better separation |

| E (Portability) | 4.0 | — |

| F (Security) | 4.2 | Token handling |



**Result**: S=4.0, σ=0.45, S_enhanced=3.69, CI=[3.3, 4.1]



**Devil's Advocate** (Security): "Network boundaries increase attack surface"



**Decision**: ⚠️ Conditional Approve with conditions:

1. Implement circuit breaker pattern

2. Add E2E latency monitoring

3. Security review of inter-service auth



**Lesson**: Service extraction needs explicit reliability and security focus.



---



### Case L3-2: New Technology Adoption (Redis → Valkey)



**Context**: Migrate caching layer to open-source alternative



| Aspect | Detail |

|--------|--------|

| **Scope** | Technology change |

| **Risk** | High |

| **Impact** | All services using cache |



**Committee**: Architect, Backend, DBA, DevOps, SRE, QA, Tech Lead (7 experts)



**Scoring Summary**:



| Category | Avg | Key Issues |

|----------|:---:|------------|

| A (Functional) | 4.0 | API compatibility |

| B (Reliability) | 3.5 | Less production track record |

| C (Performance) | 4.2 | Comparable benchmarks |

| D (Maintainability) | 4.0 | Similar operations |

| E (Portability) | 4.5 | Better licensing |

| F (Security) | 4.0 | — |



**Result**: S=4.0, σ=0.38, S_enhanced=3.73, CI=[3.4, 4.1]



**Devil's Advocate** (SRE): "Community support smaller than Redis"



**Decision**: ⚠️ Conditional Approve — Pilot with non-critical service first



**Lesson**: New tech adoption benefits from phased rollout strategy.



---



## 5. L4 Cases: Comprehensive Review



### Case L4-1: Database Migration (PostgreSQL → CockroachDB)



**Context**: Migrate primary database for global distribution



| Aspect | Detail |

|--------|--------|

| **Scope** | Critical infrastructure |

| **Risk** | Very High |

| **Impact** | Cross-department |

| **Cost** | $500K+ |



**Committee**: Architect, Backend×2, DBA×2, DevOps, SRE, Security, PM, Domain Expert, Tech Lead, CTO (12 experts)



**Scoring Summary** (31 angles):



| Category | Avg | Critical Issues |

|----------|:---:|-----------------|

| A (Functional) | 3.8 | Query compatibility 95% |

| B (Reliability) | 4.2 | Better HA |

| C (Performance) | 3.5 | Write latency increase |

| D (Maintainability) | 3.8 | New operational skills |

| E (Portability) | 4.0 | — |

| F (Security) | 4.0 | — |

| G (Compatibility) | 3.5 | ORM adjustments needed |

| H (Usability) | 3.8 | Training required |



**Group Votes**:



| Group | Vote | Confidence | Key Concern |

|-------|------|:----------:|-------------|

| Technical | Conditional | 75% | Migration complexity |

| Domain | Approve | 80% | Business continuity |

| Strategic | Approve | 85% | Long-term scalability |



**Result**: S=3.8, σ=0.32, S_enhanced=3.61, CI=[3.3, 3.9], IS=0.85



**Decision**: ⚠️ Conditional Approve with:

1. 6-month parallel run

2. Automated rollback procedure

3. Query audit completion

4. Team training program



**Lesson**: Database migrations need extended validation periods.



---



## 6. L5 Cases: Full Committee



### Case L5-1: Platform Rewrite (Monolith → Event-Driven)



**Context**: Transform legacy monolith to event-driven architecture



| Aspect | Detail |

|--------|--------|

| **Scope** | Organization-wide |

| **Risk** | Strategic |

| **Impact** | All departments |

| **Timeline** | 18 months |

| **Cost** | $2M+ |



**Committee**: 18 experts across all 6 domains



| Domain | Experts | Count |

|--------|---------|:-----:|

| Build | Architect, Backend×2, Frontend, QA, Tech Lead | 6 |

| Run | DevOps, SRE, DBA, Release | 4 |

| Secure | Security, Compliance | 2 |

| Data | Data Eng, ML Eng | 2 |

| Product | PM, UX | 2 |

| Strategy | CTO, Risk | 2 |



**Scoring Summary** (All 37 angles):



| Category | Avg | Status |

|----------|:---:|:------:|

| A (Functional) | 4.0 | ✓ |

| B (Reliability) | 3.8 | ⚠️ |

| C (Performance) | 4.2 | ✓ |

| D (Maintainability) | 4.5 | ✓ |

| E (Portability) | 4.0 | ✓ |

| F (Security) | 3.8 | ⚠️ |

| G (Compatibility) | 3.5 | ⚠️ |

| H (Usability) | 4.0 | ✓ |

| I (Data Quality) | 4.0 | ✓ |

| J (AI/ML Quality) | 4.2 | ✓ |



**Group Consensus**:



| Group | Vote | Key Position |

|-------|------|--------------|

| Technical | Conditional (4/6) | Phased approach critical |

| Domain | Approve (3/4) | Enables future capabilities |

| Strategic | Approve (2/2) | Strategic necessity |



**Result**: S=4.0, σ=0.28, S_enhanced=3.86, CI=[3.6, 4.1], IS=0.88



**Devil's Advocate Summary**:

- Risk: "Event sourcing complexity underestimated"

- Compliance: "Data lineage requirements"

- SRE: "Observability gaps during transition"



**Decision**: ✅ Conditional Approve



**Binding Conditions**:

1. Phase 1: Non-critical services (3 months)

2. Phase 2: Core services with parallel run (6 months)

3. Phase 3: Full cutover with rollback (9 months)

4. Mandatory architecture review gates

5. Dedicated migration team



**Lesson**: Platform changes require phased execution with clear gates.



---



## 7. Lessons Learned



### 7.1 Level Selection Patterns



| Pattern | Correct Level | Why |

|---------|:-------------:|-----|

| Config change, single team | L1 | Low risk, reversible |

| New feature, 2-3 teams | L2 | Standard coordination |

| Tech stack change | L3 | Requires domain expertise |

| Database migration | L4 | Critical, cross-department |

| Platform rewrite | L5 | Strategic, org-wide |



### 7.2 Common Mistakes



| Mistake | Consequence | Prevention |

|---------|-------------|------------|

| Under-leveling | Missed risks | Use level selection guide |

| Over-leveling | Wasted time | Start low, escalate if needed |

| Skipping devil's advocate | Groupthink | Mandatory assignment |

| Ignoring IS < 0.5 | Unreliable decision | Add experts or angles |



### 7.3 Success Factors



| Factor | Impact |

|--------|--------|

| Independent scoring | Prevents anchoring |

| Cross-domain representation | Comprehensive coverage |

| Clear scope definition | Focused analysis |

| Documented conditions | Actionable outcomes |

| Follow-up scheduling | Accountability |



---



## Related



- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Framework (SSOT)

- `.knowledge/templates/EXPERT_COMMITTEE.md` — Decision templates

- `.knowledge/templates/CASE_STUDY.md` — Case study template

- `.knowledge/practices/decisions/FRAMEWORK_VALIDATION_PLAN.md` — Validation plan

---

*AI Collaboration Knowledge Base*
