# Documentation Guidelines

> Clear, maintainable, useful documentation

---

## Table of Contents

- [1. Documentation Philosophy](#1-documentation-philosophy)
- [2. Document Types](#2-document-types)
- [3. Structure Standards](#3-structure-standards)
- [4. Writing Style](#4-writing-style)
- [5. Code Examples](#5-code-examples)
- [6. Diagrams](#6-diagrams)
- [7. Maintenance](#7-maintenance)

---

## 1. Documentation Philosophy

| Principle              | Application              |
|------------------------|--------------------------|
| Audience-first         | Write for the reader     |
| Progressive disclosure | Overview → details       |
| DRY                    | Single source of truth   |
| Up-to-date             | Update with code changes |

---

## 2. Document Types

| Type          | Purpose                | Update Frequency |
|---------------|------------------------|------------------|
| README        | Project entry point    | Per release      |
| API Reference | Function/class docs    | Per API change   |
| Guides        | How-to content         | As needed        |
| ADRs          | Architecture decisions | Per decision     |
| Changelog     | Release history        | Per release      |

---

## 3. Structure Standards

### 3.1 File Format

```markdown
# Title

> Single-line purpose

---

## 1. Section

### 1.1 Subsection

---

## Related

- `path/FILE.md` — Description

---

*AI Collaboration Knowledge Base*
```

### 3.2 Heading Rules

| Level | Use For             | Numbering  |
|-------|---------------------|------------|
| H1    | Document title      | None       |
| H2    | Main sections       | 1., 2., 3. |
| H3    | Subsections         | 1.1, 1.2   |
| H4    | Details (sparingly) | 1.1.1      |

---

## 4. Writing Style

| Rule          | ❌ Avoid            | ✓ Prefer            |
|---------------|--------------------|---------------------|
| Active voice  | "File is read"     | "Loader reads file" |
| Present tense | "This will create" | "This creates"      |
| Specific      | "Configure system" | "Set `MAX=100`"     |
| Concise       | "In order to"      | "To"                |

---

## 5. Code Examples

**Good examples are**: Complete · Minimal · Commented · Runnable

```python
# ✓ Shows input and output
result = process("input")
print(result)  # Output: "processed"
```

---

## 6. Diagrams

| Rule | Requirement |
|------|-------------|
| **Tool** | Must use Mermaid |
| **Simplicity** | Clear, minimal styling |
| **Consistency** | Uniform style across project |
| **Compatibility** | GitHub/GitLab native support |

### 6.1 Mermaid Diagram Types (21 Total)

| Type | Syntax | Use Case | Priority |
|------|--------|----------|----------|
| **Flowchart** | `flowchart TD/LR` | Process flows, workflows, decision trees | ⭐ Primary |
| **Sequence** | `sequenceDiagram` | API calls, system interactions | ⭐ Primary |
| **Class** | `classDiagram` | Data models, OOP structures | Common |
| **State** | `stateDiagram-v2` | State machines, lifecycle | Common |
| **ER** | `erDiagram` | Database schemas, entity relationships | Common |
| **User Journey** | `journey` | User experience, customer journey | Common |
| **Timeline** | `timeline` | Historical events, version history | Common |
| **C4** | `C4Context` | Software architecture (C4 model) | Common |
| **Gantt** | `gantt` | Project timelines, schedules | Occasional |
| **Pie** | `pie` | Proportions, distributions | Occasional |
| **Quadrant** | `quadrantChart` | Priority matrix, SWOT analysis | Occasional |
| **XY Chart** | `xychart-beta` | Line/bar charts, data visualization | Occasional |
| **Block** | `block-beta` | System components, module relationships | Occasional |
| **Architecture** | `architecture-beta` | Cloud architecture, infrastructure | Occasional |
| **Mindmap** | `mindmap` | Brainstorming, concept mapping | Rare |
| **Git Graph** | `gitGraph` | Branch strategies, commit flows | Rare |
| **Requirement** | `requirementDiagram` | Requirement tracking, specs | Rare |
| **Sankey** | `sankey-beta` | Flow analysis, energy/resource flow | Rare |
| **Kanban** | `kanban` | Task boards, workflow status | Rare |
| **Packet** | `packet-beta` | Network protocols, packet structure | Rare |
| **Radar** | `radar-beta` | Multi-dimensional comparison | Rare |

**Priority Guide**:
- ⭐ **Primary**: Recommended for most documentation needs (2 types)
- **Common**: Use when specifically applicable (6 types)
- **Occasional**: Use for specialized scenarios (6 types)
- **Rare**: Use sparingly, often beta features (7 types)

### 6.2 Selection Guide

| Scenario | Recommended Type |
|----------|------------------|
| Bootstrap/startup process | Flowchart (LR with subgraphs) |
| API request/response | Sequence diagram |
| Domain model | Class diagram |
| Object lifecycle | State diagram |
| Database design | ER diagram |
| User experience flow | User Journey |
| Version/release history | Timeline |
| Software architecture | C4 diagram |
| Project roadmap | Gantt chart |
| Priority/risk matrix | Quadrant chart |
| Metrics over time | XY Chart |
| System modules | Block diagram |
| Cloud infrastructure | Architecture diagram |

### 6.3 Basic Rules

- **Direction**: Use `TD` (top-down) or `LR` (left-right) consistently
- **Nodes**: Max 15 nodes per diagram
- **Nesting**: Max 2 levels of subgraphs
- **Labels**: Concise, descriptive text

### 6.4 Design Principles

Apply 信达雅 (Xin-Da-Ya) philosophy:
- **信 (Faithfulness)**: Accurate representation
- **达 (Clarity)**: Clear communication
- **雅 (Elegance)**: Refined simplicity

> **Full Standards**: See `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md`

---

## 7. Maintenance

### 7.1 Update Triggers

| Event         | Action               |
|---------------|----------------------|
| Code change   | Update affected docs |
| API change    | Update reference     |
| User question | Improve clarity      |

### 7.2 Quality Checklist

- [ ] Links verified
- [ ] Examples tested
- [ ] Sections numbered
- [ ] Footer present

---

## Related

- `.knowledge/practices/documentation/DOCUMENTATION_STANDARDS.md` — Full documentation standards (SSOT)
- `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md` — Diagram creation standards (SSOT)
- `config/capabilities/documentation.yaml` — TOC configuration

---

*AI Collaboration Knowledge Base*
