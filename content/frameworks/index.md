# Frameworks Reference

> Deep conceptual frameworks and patterns

---

## Contents

| Topic | Path | Tokens | Purpose |
|-------|------|--------|---------|
| **Autonomy** | `autonomy.md` | ~150 | 6-level AI autonomy framework |
| **Timeout** | `timeout.md` | ~100 | 5-level timeout hierarchy |
| **Design** | `design/` | ~150 | Design axioms and principles |
| **Cognitive** | `cognitive/` | ~300 | Expert committee, information density |
| **Resilience** | `resilience/` | ~250 | Timeout patterns, circuit breaker |
| **Patterns** | `patterns/` | ~400 | Collaboration, persistence, decision |

---

## Framework Categories

### Core Frameworks
- `autonomy.md` — L1-L6 autonomy levels with calibration
- `timeout.md` — T1-T5 timeout hierarchy with fallbacks

### Design & Architecture
- `design/axioms.md` — MECE, SSOT, separation of concerns

### Cognitive Enhancement
- `cognitive/expert_committee.md` — 24-expert committee pattern
- `cognitive/information_density.md` — Token efficiency strategies

### Resilience Patterns
- `resilience/timeout_basics.md` — Timeout implementation
- `resilience/circuit_breaker.md` — Failure isolation

### Integration Patterns
- `patterns/collaboration.md` — AI-human collaboration patterns
- `patterns/persistence.md` — Data persistence strategies
- `patterns/decision.md` — Quality angles for decisions

---

## Quick Reference

### Autonomy Levels (L1-L6)
| Level | Name | Range | Behavior |
|-------|------|-------|----------|
| L1 | Minimal | 0-20% | Ask before all changes |
| L2 | Low | 20-40% | Ask before significant |
| L3 | Medium | 40-60% | Routine proceed, novel ask |
| L4 | Medium-High | 60-80% | Proceed, report after |
| L5 | High | 80-95% | High autonomy |
| L6 | Full | 95-100% | Full autonomy |

### Timeout Levels (T1-T5)
| Level | Timeout | Scope | Fallback |
|-------|---------|-------|----------|
| T1 | 100ms | Cache | Skip, proceed |
| T2 | 500ms | File | Use fallback |
| T3 | 2s | Layer | Partial + warning |
| T4 | 5s | Full | Emergency core |
| T5 | 10s | Complex | Abort + summary |

---

## Load by Topic

| Topic | Load |
|-------|------|
| AI autonomy | `autonomy.md` |
| Timeout, performance | `timeout.md`, `resilience/` |
| Design principles | `design/axioms.md` |
| Expert review | `cognitive/expert_committee.md` |
| Collaboration | `patterns/collaboration.md` |

---

## Related

- `core/index.md` — Core principles
- `guidelines/index.md` — Practical guidelines
- `practices/index.md` — Implementation practices

---

*Part of SAGE Knowledge Base*
