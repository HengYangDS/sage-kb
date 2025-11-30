# SAGE Four Layer Model

> SAGE-specific implementation of the Four-Layer Architecture Pattern

---

## Generic Pattern Reference

For the universal Four-Layer Architecture Pattern (definitions, dependency rules, stability levels), see:

**→ `.knowledge/frameworks/design/FOUR_LAYER_PATTERN.md`**

This document contains SAGE-specific directory mappings and implementation details.

---

## Table of Contents

- [1. SAGE Layer Mapping](#1-sage-layer-mapping)
- [2. Directory Structure](#2-directory-structure)
- [3. Capability Families](#3-capability-families)
- [4. Script Categories](#4-script-categories)
- [5. SAGE Validation Checklist](#5-sage-validation-checklist)

---

## 1. SAGE Layer Mapping

| Layer | Generic Name | SAGE Implementation | Directory |
|-------|--------------|---------------------|-----------|
| **L1** | Extension | plugins | `src/sage/core/plugins/` |
| **L2** | Interface | capabilities | `src/sage/capabilities/` |
| **L3** | Implementation | tools | `tools/{family}/` |
| **L4** | Auxiliary | scripts | `scripts/{category}/` |

### 1.1 Layer Diagram (SAGE-specific)

```
Abstract ▲
         │  ┌─────────────────────────────────────────┐
         │  │ plugins (L1: Extension Layer)           │
         │  │ · src/sage/core/plugins/                │
         │  │ · docs/design/plugins/                  │
         │  └─────────────────────────────────────────┘
         │                    │
         │                    ▼
         │  ┌─────────────────────────────────────────┐
         │  │ capabilities (L2: Interface Layer)      │
         │  │ · src/sage/capabilities/                │
         │  │ · docs/design/capabilities/             │
         │  └─────────────────────────────────────────┘
         │                    │
         │                    ▼
         │  ┌─────────────────────────────────────────┐
         │  │ tools (L3: Implementation Layer)        │
         │  │ · tools/{analyzers,checkers,...}        │
         │  │ · docs/guides/TOOLS.md                  │
         │  └─────────────────────────────────────────┘
         │                    │
         ▼                    ▼
Concrete   ┌─────────────────────────────────────────┐
           │ scripts (L4: Auxiliary Layer)           │
           │ · scripts/{dev,check,hooks,ci}          │
           │ · scripts/README.md                     │
           └─────────────────────────────────────────┘
```

---

## 2. Directory Structure

| Layer | Source Code | Documentation |
|-------|-------------|---------------|
| plugins | `src/sage/core/plugins/` | `docs/design/plugins/` |
| capabilities | `src/sage/capabilities/` | `docs/design/capabilities/` |
| tools | `tools/{family}/` | `docs/guides/TOOLS.md` |
| scripts | `scripts/{category}/` | `scripts/README.md` |

---

## 3. Capability Families

SAGE organizes tools by capability family (L3 layer):

| Family | Responsibility | Representative Tools |
|--------|---------------|---------------------|
| **analyzers** | Analysis, diagnosis, graph | knowledge_graph |
| **checkers** | Check, validate, verify | knowledge_validator |
| **monitors** | Monitor, observe, alert | timeout_manager |
| **converters** | Convert, migrate, adapt | migration_toolkit |
| **generators** | Generate, build, create | index_generator |

---

## 4. Script Categories

SAGE organizes scripts by category (L4 layer):

| Category | Purpose | Examples |
|----------|---------|----------|
| **dev** | Development setup | setup_dev.py, new_file.py |
| **check** | Validation scripts | check_architecture.py |
| **hooks** | Git hooks | pre_commit.py, pre_push.py |
| **ci** | CI/CD pipelines | build.py, test.py, release.py |

---

## 5. SAGE Validation Checklist

- [ ] Each SAGE component belongs to exactly one layer
- [ ] No downward dependencies in SAGE codebase
- [ ] Tools are organized by capability family
- [ ] Scripts are organized by category
- [ ] Documentation exists in designated locations

---

## Related

- `.knowledge/frameworks/design/FOUR_LAYER_PATTERN.md` — **Authoritative** Four-Layer Architecture Pattern
- `.knowledge/practices/engineering/MECE.md` — MECE categorization principle
- `.context/conventions/DIRECTORY_STRUCTURE.md` — Full SAGE directory layout
- `docs/design/architecture/INDEX.md` — SAGE architecture documentation

---

*AI Collaboration Knowledge Base*
