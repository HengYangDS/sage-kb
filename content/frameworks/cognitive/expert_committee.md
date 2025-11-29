# Expert Committee Framework

> **Load Priority**: On-demand  
> **Purpose**: Multi-perspective analysis using 35+ expert roles  
> **Philosophy**: Taoist "One → Two → Three → All Things" (dynamic composition)

---

## 👥 Expert Role Pool

**Structure**: Core (10) + Extended (15) + Domain (10+) = 35+ roles · **Core covers 90%**

### Core Layer: 10 Fundamental Roles

| Role | Responsibility | NOT Responsible For |
|------|----------------|---------------------|
| 🏗️ **Architect** | System architecture, tech selection, evolution | Concrete coding, ops |
| 💻 **Engineer** | Code implementation, quality, design patterns | Architecture, deployment |
| 🔬 **QA** | Test strategy, quality assurance, defects | Code writing, architecture |
| 🛠️ **DevOps** | CI/CD, monitoring, release, ops automation | Code, business logic |
| 🔒 **Security** | Security architecture, vulnerabilities, threats | Features, performance |
| 🧠 **AI Engineer** | AI/ML integration, training, model deployment | Research, traditional SW |
| 🔬 **AI Researcher** | Algorithm innovation, experiments, frontier | Engineering, production |
| 🎯 **TPM** | Project progress, risk, resource coordination | Tech decisions, product |
| 📚 **Knowledge Eng** | Doc architecture, knowledge preservation | Tech implementation |
| 💼 **Product Mgr** | Business value, requirements, product roadmap | Tech implementation |

### Extended & Domain Layers

| Category | Roles |
|----------|-------|
| **Tech Specialization** | Frontend Architect · Database · Infrastructure · Mobile · Performance · Integration · Data Scientist · Algorithm |
| **Quality & Process** | Chaos Engineer · Compliance · Accessibility · Localization |
| **User & Business** | UX Designer · Business Analyst · Cost Optimizer |
| **Domain** | Healthcare IT · FinTech · IoT · Gaming · Automotive · Defense · Enterprise · Web3 · Robotics · Telecom |

**Activation**: L1: 2-3 core | L2: 3-5 core | L3: 7-10 + 2-4 ext | L4: 10 + 5-8 ext + domain | L5: all (15-25)

---

## 🎯 Decision Patterns (9 Basic = 90% coverage)

| Pattern | Roles | Angles | Time |
|---------|-------|--------|------|
| **Quick Fix** | Engineer + QA | Correctness + Testability | 30min |
| **Feature Dev** | Architect + Engineer + QA | Correctness + Completeness + Clarity | 1hr |
| **Architecture** | Architect + Engineer + Security | Clarity + Reliability + Adaptability | 2hr |
| **Performance** | Engineer + DevOps + QA | Efficiency + Reliability + Observability | 1.5hr |
| **Security** | Security + Architect + DevOps | Safety + Reliability + Auditability | 2hr |
| **Release** | DevOps + TPM + QA | Reliability + Completeness + Observability | 1hr |
| **Product** | Product Mgr + Architect + TPM | Effectiveness + Completeness + Adaptability | 2hr |
| **AI Deploy** | AI Engineer + Engineer + DevOps | Effectiveness + Efficiency + Observability | 2hr |
| **Knowledge** | Knowledge Eng + Engineer + QA | Clarity + Completeness + Maintainability | 1hr |

**Extended**: Frontend (3) · Data (3) · Cloud (3) · Mobile (3) · HA (3) · Compliance (3) · i18n (3) · UX (3) · Business (3) = 27 scenarios

---

## 📊 Decision Levels (5-Level Ladder)

| Level | Name | Time | Roles | Scenarios |
|-------|------|------|-------|-----------|
| **L1** | Micro | 15min | 2-3 core | Bug fixes, docs, small features |
| **L2** | Rapid | 30min | 3-5 core | Feature dev, perf optimization |
| **L3** | Major | 2hr | 7-10 core + ext | Architecture, tech stack, refactoring |
| **L4** | Strategic | 4hr | 10 core + ext + domain | Product direction, tech selection |
| **L5** | Transformative | 1day | All relevant (15-25) | Strategy, disruptive changes |

**Level Selection**:

| Factor | L1 | L2 | L3 | L4 | L5 |
|--------|----|----|----|----|----| 
| Code Impact | <100 lines | <1K | <10K | <100K | System-wide |
| Team Impact | 1 person | 2-3 | Team | Multi-team | Organization |
| Timeline | Days | 1-2 weeks | 1-2 months | Quarter | Year+ |
| Risk Level | Low | Medium | High | Very High | Critical |

**Scale Up**: Novel · Cross-domain · No consensus · Stakeholder request  
**Scale Down**: Consensus · Simpler · Strong precedent · Time constraints

---

## 🔗 Role-Angle Matrix (Primary ●)

| Role | Correct | Complete | Safety | Clarity | Efficient | Reliable | Testable | Observable | Adaptable |
|------|:-------:|:--------:|:------:|:-------:|:---------:|:--------:|:--------:|:----------:|:---------:|
| Architect | | | | ● | | ● | | | ● |
| Engineer | ● | ● | | ● | | | ● | | |
| QA | ● | | ● | | | ● | ● | | |
| DevOps | | | | | ● | ● | | ● | |
| Security | | | ● | | | | | | |
| AI Engineer | | | | | ● | | | | |
| TPM | | ● | | | | | | | |
| Knowledge Eng | | | | ● | | | | | ● |
| Product Mgr | | ● | | | | | | | |

---

## 📝 Usage

### Invocation

```markdown
## L1-L2: [EXPERT: Architect, Engineer] Question: <decision>
## L3: [EXPERT COMMITTEE: L3] Context: <bg> | Question: <decision> | Constraints: <limits>
## L4-L5: [EXPERT COMMITTEE: L5] Context: <comprehensive> | Stakeholders: <parties>
```

### Output Structure

```markdown
## Expert Committee Deliberation
**Config**: Level [1-5] · Roles: [list] · Duration: [time]
### Perspectives → [Role]: Assessment · Observations · Concerns · Recommendations
### Synthesis → Agreement · Concerns · Trade-offs
### Recommendation → Decision · Rationale · Risk Mitigation · Next Steps
```

### Autonomy Integration

| Autonomy | Committee Size | Report Frequency |
|----------|----------------|------------------|
| L2-L3 | 2-3 experts | Each cycle |
| L4 | 3-5 experts | Milestones |
| L5-L6 | Full for major | Completion |

---

**Summary**: 35+ roles × 35+ angles = 1,200+ combinations · 9 patterns cover 90% · 5 levels scale 15min→1day

*Part of AI Collaboration Knowledge Base*
