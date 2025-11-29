# Knowledge Base Navigation

> Entry point for SAGE knowledge content

---

## Layer Overview

| Layer | Path | Budget | Purpose |
|-------|------|--------|---------|
| **Core** | `core/` | ~500 | Principles, defaults, quick reference |
| **Guidelines** | `guidelines/` | ~1200 | Code style, engineering, AI collaboration |
| **Frameworks** | `frameworks/` | ~2000 | Autonomy, timeout, cognitive, design |
| **Practices** | `practices/` | ~1500 | Documentation, engineering, AI workflow |
| **Scenarios** | `scenarios/` | ~500 | Context-specific presets |
| **Templates** | `templates/` | ~300 | Reusable document templates |

---

## Quick Access

### Essential (Always Load)
- `core/principles.md` — 信达雅, 术法道 philosophy
- `core/quick_reference.md` — Critical questions, autonomy quick ref
- `core/defaults.md` — Default behaviors, calibration

### Getting Started
- `guidelines/quick_start.md` — 3-minute introduction
- `guidelines/code_style.md` — Code standards
- `guidelines/python.md` — Python-specific practices

### Deep Reference
- `frameworks/autonomy.md` — 6-level autonomy framework
- `frameworks/timeout.md` — 5-level timeout hierarchy
- `frameworks/design/axioms.md` — Design principles

---

## Load Triggers

| Keyword | Loads |
|---------|-------|
| code, style, format | `guidelines/code_style.md` |
| test, quality | `guidelines/engineering.md`, `practices/engineering/testing/` |
| python, pytest | `guidelines/python.md` |
| timeout, circuit | `frameworks/timeout.md`, `frameworks/resilience/` |
| autonomy, AI | `frameworks/autonomy.md`, `guidelines/ai_collaboration.md` |
| doc, documentation | `guidelines/documentation.md`, `practices/documentation/` |

---

## Navigation Pattern

```
index.md (this file)
    ↓ select layer
[layer]/index.md
    ↓ select topic
[layer]/[topic].md or [layer]/[topic]/index.md
    ↓ need detail
[layer]/[topic]/[detail].md
```

---

*Part of SAGE Knowledge Base*
