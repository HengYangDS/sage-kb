# Quality Angles Framework

> **Load Priority**: On-demand  
> **Purpose**: Multi-perspective quality evaluation using 35+ quality angles  
> **Basis**: ISO/IEC 25010 + Practical Extensions

---

**Structure**: Core (10) → Extended (15) → Domain (10+) = 35+ angles · Dynamic composition

---

## 🎯 Core Layer: 10 Fundamental Dimensions

| Category | Angle | Definition | Key Questions |
|----------|-------|------------|---------------|
| **Functional** | **Correctness** | Functions meet requirements | Edge cases? Production-ready? |
| | **Completeness** | All features present | Docs complete? Tests sufficient? |
| | **Safety** | Data security, vulnerabilities | Input validated? Vulnerabilities? |
| | **Effectiveness** | Achieves business goals | Goal achieved? Problem solved? |
| **Architectural** | **Clarity** | Readable, clear architecture | Readable? Well-named? |
| | **Efficiency** | Performance, resources | Fast enough? Resources OK? |
| | **Reliability** | Stability, fault tolerance | Fault-tolerant? Graceful degradation? |
| **Evolutionary** | **Testability** | Easy to test, mockable | Mockable? Coverage possible? |
| | **Observability** | Logging, monitoring | Logging? Metrics? Debuggable? |
| | **Adaptability** | Extensible, configurable | Extensible? Migratable? |

---

## 🔧 Extended Layer: 15 Specialized Dimensions

| Category | Angles | When to Activate |
|----------|--------|------------------|
| **User Experience** | Usability · Accessibility · Responsiveness · Aesthetics | User-intensive, public services |
| **Technical Depth** | Scalability · Performance · Portability · Interoperability · Resilience | Large-scale, HA systems |
| **Maintenance** | Maintainability · Reproducibility · Upgradability | Long-term, multi-version |
| **Compliance** | Auditability · Compliance · Privacy | Regulated industries |

---

## 🏭 Domain Layer: 10+ Industry Dimensions

| Angle | Scenario | Angle | Scenario |
|-------|----------|-------|----------|
| Medical Safety | Healthcare (FDA/HIPAA) | Financial Security | FinTech (PCI-DSS) |
| Real-time Perf | Embedded/IoT | Gaming Experience | Gaming (FPS) |
| Automotive Safety | Vehicles (ISO 26262) | Defense Grade | Defense systems |
| Enterprise Integration | ERP/SOA | Decentralization | Blockchain |
| Energy Efficiency | IoT/Mobile | Network Reliability | Telecom |

---

## 🎲 Angle Selection by Scenario

| Scenario | Core Angles | Extended | Domain |
|----------|-------------|----------|--------|
| Bug Fix | Correctness, Testability | - | - |
| New Feature | Correctness, Completeness, Clarity | Usability | - |
| Refactoring | Clarity, Testability, Maintainability | - | - |
| Performance | Efficiency, Reliability | Performance, Scalability | - |
| Security | Safety, Reliability | Auditability, Compliance | - |
| Architecture | Clarity, Adaptability, Reliability | Scalability, Interoperability | - |
| Healthcare App | Safety, Reliability, Completeness | Privacy, Compliance | Medical Safety |
| Financial System | Safety, Reliability, Auditability | Compliance | Financial Security |

### Quick Evaluation

```
Angle: [name] · Score: [1-5] · Notes: [observations]
Summary: Strengths · Concerns · Recommendations · Overall: [X]/50
```

---

## 🔗 Expert Integration

| Angle Category | Primary Expert | Secondary |
|----------------|----------------|-----------|
| Functional | QA, Engineer | Product Manager |
| Architectural | Architect, Engineer | DevOps |
| Evolutionary | QA, DevOps | Architect |
| User Experience | UX Designer | Product Manager |
| Technical Depth | Performance Engineer | Architect |
| Compliance | Compliance Officer | Security |

---

## 📊 Summary

| Layer | Count | Coverage |
|-------|-------|----------|
| Core | 10 | 90% |
| Extended | 15 | 95% |
| Domain | 10+ | 100% |

**Golden Rule**: Start with core 10, add extended/domain as needed.

*Part of AI Collaboration Knowledge Base*
