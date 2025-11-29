# AI Autonomy Levels Framework

> 6-level autonomy spectrum for human-AI collaboration

---

## 🎚️ Level Spectrum

**Default**: L4 (Medium-High) · **Principle**: Adapt dynamically based on context, risk, maturity

| Level    | Name        | Authority | Characteristics                                         | When to Use                                          |
|----------|-------------|-----------|---------------------------------------------------------|------------------------------------------------------|
| **L1**   | Minimal     | 0-20%     | Ask before every decision · No architectural changes    | Onboarding · Critical systems · Unfamiliar domains   |
| **L2**   | Low         | 20-40%    | Execute defined tasks · Ask on implementation choices   | New phases · Learning codebase · After major changes |
| **L3**   | Medium      | 40-60%    | Complete tasks autonomously · Ask for breaking changes  | Routine dev · Well-documented systems                |
| **L4** ⭐ | Medium-High | 60-80%    | Multi-task initiatives · Proactive issue identification | Mature collaboration (3+ weeks) · High trust         |
| **L5**   | High        | 80-95%    | Strategic decisions · Proactive refactoring             | Very mature (6+ months) · Trusted production         |
| **L6**   | Full        | 95-100%   | All decisions independent · Auto-deploy                 | ⚠️ Rarely recommended · Non-critical only            |

---

## 🎯 Decision Matrix

| Scenario              | Level | Scenario              | Level |
|-----------------------|-------|-----------------------|-------|
| New project start     | L2    | Documentation work    | L4    |
| Routine development   | L3    | Security changes      | L2    |
| Mature collaboration  | L4 ⭐  | Refactoring           | L3-4  |
| Critical systems      | L2-3  | Production deployment | L2-3  |
| Experimental features | L4-5  |                       |       |

**Calibration Signals**:

- "Let me see first" → L2-3 | "You decide" → L4-5 | "Don't stop" → L4-5
- "Production-ready" → L3 | "Full autonomy" → L5

---

## ⚡ Dynamic Adjustment

**Increase** ✅: Clear guidelines · Established patterns · Positive feedback · Low-risk ops · Strong test coverage

**Decrease** ⚠️: New domain/tech · User concerns · High-risk ops · Repeated mistakes · Ambiguous requirements

---

## 🔒 Level 4 Boundaries (Default)

| ✅ Autonomous               | ⚠️ Requires Approval       | ❌ Never Autonomous     |
|----------------------------|----------------------------|------------------------|
| Doc organization           | File deletion              | Deleting user data     |
| File moves/new dirs        | Breaking API changes       | Bypassing security     |
| Naming enforcement         | Major architectural shifts | Ignoring test failures |
| Health checks              | Production deployment      | Committing secrets     |
| Test additions             | Security/DB schema mods    | Untested prod changes  |
| Non-breaking optimizations | Cost-increasing infra      | Disabling monitoring   |

---

## 🎲 Quick Selector

Answer 3 questions, average the results:

| Factor                     | Low (L2)             | Medium (L3)             | High (L4-5)        |
|----------------------------|----------------------|-------------------------|--------------------|
| **Collaboration maturity** | New (0-2 weeks)      | Established (3-8 weeks) | Mature (2+ months) |
| **Guideline clarity**      | Minimal docs         | Basic guidelines        | Comprehensive      |
| **Risk level**             | High (prod/security) | Medium (features)       | Low (docs/tests)   |

---

## 🔄 Feedback Loop

```
Execute → Self-Check → Proactive Scan → Report → Extract Experience → Submit → Next
```

**Self-Check**: Validate constraints (files, naming, structure, references)
**Proactive Scan**: Identify issues, optimization opportunities, patterns
**Extract**: Identify patterns, propose guideline updates

---

## 📊 Success Metrics

| 1 Month                    | 3 Months                  | 6 Months                   |
|----------------------------|---------------------------|----------------------------|
| Self-check every delivery  | Automated health checks   | User rarely reminds        |
| 10+ proactive issues found | 5+ guideline updates      | Issues prevented early     |
| Zero constraint violations | Doc health >90/100        | AI as true partner         |
| 95%+ completion w/o rework | User rarely gives details | Committee pattern standard |

---

## 💡 Calibration Examples

| Scenario            | Risk   | Reversibility   | → Level                          |
|---------------------|--------|-----------------|----------------------------------|
| DB Schema Migration | High   | Difficult       | **L2** - Present plan, await     |
| Adding Unit Tests   | Low    | Easy            | **L5** - Proceed, report         |
| Refactoring Module  | Medium | Medium (git)    | **L4** - Proceed, test, report   |
| Production Config   | High   | Easy (rollback) | **L3** - Propose, explain, await |

---

**Golden Rule**: Start conservative (L2-3), increase gradually based on demonstrated success.

---

*Part of SAGE Knowledge Base*
