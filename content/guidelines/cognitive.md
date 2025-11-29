# Cognitive Enhancement Guidelines

> Enhanced metacognitive capabilities for AI collaboration

---

## 1. Chain-of-Thought Reasoning

**When**: Architecture decisions · Breaking changes · Trade-offs · Novel problems

**Structure**: Problem → Options (Pros/Cons/Risk) → Decision (Why/Trade-offs) → Steps

| Autonomy | Display |
|----------|---------|
| L2-L3 | Show all reasoning |
| L4 | Key decisions only |
| L5-L6 | Novel problems only |

---

## 2. Iterative Feedback Loop

**Cycle**: Think → Decide → Act → Observe → Learn → [Repeat]

| Phase | Action |
|-------|--------|
| Think | Analyze, explore options |
| Decide | Choose, commit |
| Act | Implement |
| Observe | Measure results |
| Learn | Extract insights |

**Reporting**: L2-L3 each cycle · L4 milestones · L5-L6 completion summary

---

## 3. Multi-Perspective Critique

> **Full Framework**: `content/frameworks/decision/quality_angles.md`

| Category | Angles |
|----------|--------|
| **Functional** | Correctness · Completeness · Safety · Effectiveness |
| **Architectural** | Clarity · Efficiency · Reliability |
| **Evolutionary** | Testability · Observability · Adaptability |

**Quick Critique**: `Angle: [name] · Status: ✅/⚠️/❌ · Notes: [observation]`

---

## 4. Critical Thinking: 5 Questions

| # | Question | Purpose |
|---|----------|---------|
| 1 | What am I assuming? | Surface hidden assumptions |
| 2 | What could go wrong? | Identify failure modes |
| 3 | Is there a simpler way? | Avoid over-engineering |
| 4 | What will maintainers need? | Ensure sustainability |
| 5 | How does this fit the bigger picture? | System coherence |

---

## 5. External Systems Mastery

| Category | Best Practices |
|----------|----------------|
| Code Execution | Validate outputs, handle errors |
| Search & Discovery | Specific queries, verify results |
| File Operations | Validate paths, backup critical |
| Database & APIs | Timeouts, validate responses |

**Do** ✅: Validate · Handle errors · Document · Clean up · Use timeouts

---

## 6. Long-Term Memory

**Hierarchy** (ephemeral → permanent): Session → Experience → Practices → Guidelines → Principles (信达雅)

**Recall**: Guidelines first → Frameworks → Practices → Experiences

---

## 7. Multi-Agent Collaboration

> **Full Framework**: `content/frameworks/cognitive/expert_committee.md`

| Level | Experts | Time |
|-------|---------|------|
| L1 Micro | 2-3 core | 15min |
| L2 Rapid | 3-5 core | 30min |
| L3 Major | 7-10 + ext | 2hrs |
| L4 Strategic | 10 + domain | 4hrs |
| L5 Transformative | 15-25 | 1 day |

**Invocation**: `[EXPERT: Role1, Role2]` or `[EXPERT COMMITTEE: Level N]`

---

## 8. Task Decomposition (SMART)

| Criterion | Description |
|-----------|-------------|
| **S**pecific | Clear, unambiguous |
| **M**easurable | Verifiable completion |
| **A**chievable | Realistic scope |
| **R**elevant | Aligned with goal |
| **T**ime-bound | Estimated duration |

**Size Guide**: <1hr: no split · 1-4hr: 2-4 subtasks · 4-8hr: 4-8 subtasks · >8hr: multiple tasks

---

## 9. Learning & Adaptation

| Trigger | Action |
|---------|--------|
| Task completed | Extract lessons |
| Mistake made | Document, prevent |
| Pattern discovered | Propose guideline update |
| User feedback | Adjust behavior |
| New domain | Study before acting |

**Levels**: Immediate → Session → Cross-session → Systematic (guideline changes)

---

## Summary

| Dimension | Key Output |
|-----------|------------|
| Chain-of-Thought | Visible reasoning |
| Iterative Loop | Documented cycles |
| Multi-Perspective | Angle-based critique |
| Critical Thinking | Validated assumptions |
| External Systems | Verified results |
| Long-Term Memory | Persistent learnings |
| Multi-Agent | Expert consensus |
| Task Decomposition | SMART subtasks |
| Learning | Experience extraction |

**Golden Rule**: Make thinking visible, iterate on feedback, learn from every interaction.

---

*Part of SAGE Knowledge Base*
