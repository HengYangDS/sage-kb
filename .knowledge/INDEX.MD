---
version: "1.0"
last_updated: "2025-11-30"
status: published
tokens: ~800
---

# Knowledge Base Navigation

> Entry point for SAGE knowledge content

---

## Table of Contents

- [1. Directory Structure](#1-directory-structure)
- [2. Layer Overview](#2-layer-overview)
- [3. Complete File List](#3-complete-file-list)
- [4. Navigation Pattern](#4-navigation-pattern)

---

## 1. Directory Structure

| Layer          | Path          | Purpose                                   | Files |
|----------------|---------------|-------------------------------------------|-------|
| **Core**       | `core/`       | Principles, defaults, quick reference     | 4     |
| **Guidelines** | `guidelines/` | Code style, engineering, AI collaboration | 15    |
| **Frameworks** | `frameworks/` | Autonomy, timeout, cognitive patterns     | 24    |
| **Practices**  | `practices/`  | Documentation, engineering, decisions     | 43    |
| **References** | `references/` | Quick reference guides and checklists     | 4     |
| **Scenarios**  | `scenarios/`  | Context-specific guides                   | 23    |
| **Templates**  | `templates/`  | Reusable document templates               | 17    |

**Total**: ~132 knowledge files

---

## 2. Layer Overview

### 2.1 Core (4 files)

Foundation knowledge loaded on every session:

| File                 | Purpose                         |
|----------------------|---------------------------------|
| `PRINCIPLES.MD`      | 信达雅 + 术法道 philosophy            |
| `QUICK_REFERENCE.MD` | 5 questions + autonomy levels   |
| `DEFAULTS.MD`        | Default behaviors + calibration |

### 2.2 Guidelines (15 files)

Code style and collaboration standards:

| File                  | Purpose                       |
|-----------------------|-------------------------------|
| `QUICK_START.MD`      | 3-minute productivity guide   |
| `CODE_STYLE.MD`       | Code style standards          |
| `AI_COLLABORATION.MD` | Human-AI interaction patterns |
| `PYTHON.MD`           | Python-specific guidelines    |
| `TYPESCRIPT.MD`       | TypeScript guidelines         |
| `SQL.MD`              | SQL conventions               |
| `SHELL.MD`            | Shell scripting standards     |
| `DOCUMENTATION.MD`    | Documentation standards       |
| `ENGINEERING.MD`      | Engineering practices         |
| `SECURITY.MD`         | Security guidelines           |
| `QUALITY.MD`          | Quality assurance             |
| `COGNITIVE.MD`        | Cognitive patterns            |
| `PLANNING.MD`         | Planning guidelines           |
| `SUCCESS.MD`          | Success metrics               |

### 2.3 Frameworks (24 files)

Reusable patterns and strategies across 7 categories:

| Subdirectory   | Files | Purpose                          |
|----------------|-------|----------------------------------|
| `autonomy/`    | 2     | AI autonomy levels (L1-L6)       |
| `cognitive/`   | 3     | Expert committee, info density   |
| `design/`      | 2     | Design axioms and principles     |
| `patterns/`    | 5     | Collaboration, decision patterns |
| `performance/` | 4     | Caching, optimization, profiling |
| `resilience/`  | 2     | Timeout patterns, fallbacks      |
| `security/`    | 5     | Auth, secrets, security checks   |

### 2.4 Practices (43 files)

Real-world implementation guidance:

| Subdirectory        | Files | Purpose                      |
|---------------------|-------|------------------------------|
| `ai_collaboration/` | 11    | Context, session, token mgmt |
| `decisions/`        | 1     | Autonomy case studies        |
| `documentation/`    | 7     | Knowledge org, standards     |
| `engineering/`      | 23    | API, testing, CI/CD, logging |

### 2.5 Scenarios (23 files)

Context-specific project guides:

| Subdirectory            | Files | Purpose                    |
|-------------------------|-------|----------------------------|
| `data_pipeline/`        | 2     | Data pipeline projects     |
| `devops/`               | 2     | DevOps workflows           |
| `documentation/`        | 2     | Documentation projects     |
| `knowledge_management/` | 1     | Knowledge management       |
| `legacy_modernization/` | 1     | Legacy system updates      |
| `mcp_integration/`      | 1     | MCP integration            |
| `microservices/`        | 1     | Microservices architecture |
| `monorepo/`             | 1     | Monorepo management        |
| `plugin_development/`   | 1     | Plugin development         |
| `python_backend/`       | 2     | Python backend projects    |
| `typescript_frontend/`  | 2     | TypeScript frontend        |

### 2.6 References (2 files)

Quick reference guides and checklists:

| File                       | Purpose                         |
|----------------------------|---------------------------------|
| `KNOWLEDGE_QUICK_REF.MD`   | Knowledge organization patterns |
| `PERFORMANCE_CHECKLIST.MD` | Performance optimization checks |

### 2.7 Templates (14 files)

Reusable document templates:

| File                       | Purpose                      |
|----------------------------|------------------------------|
| `ADR.MD`                   | Architecture Decision Record |
| `API_SPEC.MD`              | API specification            |
| `CASE_STUDY.MD`            | Case study template          |
| `CONVERSATION_RECORD.MD`   | Conversation logging         |
| `EXPERT_COMMITTEE.MD`      | Expert committee review      |
| `MEETING_NOTES.MD`         | Meeting notes template       |
| `POSTMORTEM.MD`            | Incident postmortem          |
| `PROJECT_SETUP.MD`         | Project setup checklist      |
| `RELEASE_NOTES.MD`         | Release notes format         |
| `RUNBOOK.MD`               | Operational runbook          |
| `SESSION_STATE.MD`         | AI session state             |
| `TASK_HANDOFF.MD`          | Task handoff document        |
| `TROUBLESHOOTING_GUIDE.MD` | Troubleshooting template     |

---

## 3. Complete File List

### Core

- `.knowledge/core/INDEX.MD` — Core layer navigation
- `.knowledge/core/PRINCIPLES.MD` — 信达雅 philosophy
- `.knowledge/core/QUICK_REFERENCE.MD` — Quick reference guide
- `.knowledge/core/DEFAULTS.MD` — Default configurations

### Guidelines

- `.knowledge/guidelines/INDEX.MD` — Guidelines navigation
- `.knowledge/guidelines/QUICK_START.MD` — Quick start guide
- `.knowledge/guidelines/CODE_STYLE.MD` — Code style standards
- `.knowledge/guidelines/AI_COLLABORATION.MD` — AI collaboration patterns
- `.knowledge/guidelines/PYTHON.MD` — Python guidelines
- `.knowledge/guidelines/TYPESCRIPT.MD` — TypeScript guidelines
- `.knowledge/guidelines/SQL.MD` — SQL conventions
- `.knowledge/guidelines/SHELL.MD` — Shell scripting
- `.knowledge/guidelines/DOCUMENTATION.MD` — Documentation standards
- `.knowledge/guidelines/ENGINEERING.MD` — Engineering practices
- `.knowledge/guidelines/SECURITY.MD` — Security guidelines
- `.knowledge/guidelines/QUALITY.MD` — Quality assurance
- `.knowledge/guidelines/COGNITIVE.MD` — Cognitive patterns
- `.knowledge/guidelines/PLANNING.MD` — Planning guidelines
- `.knowledge/guidelines/SUCCESS.MD` — Success metrics

### Frameworks

- `.knowledge/frameworks/INDEX.MD` — Frameworks navigation
- `.knowledge/frameworks/autonomy/INDEX.MD` — Autonomy framework
- `.knowledge/frameworks/autonomy/LEVELS.MD` — L1-L6 autonomy levels
- `.knowledge/frameworks/cognitive/INDEX.MD` — Cognitive framework
- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.MD` — Expert committee pattern
- `.knowledge/frameworks/cognitive/INFORMATION_DENSITY.MD` — Information density
- `.knowledge/frameworks/design/INDEX.MD` — Design framework
- `.knowledge/frameworks/design/AXIOMS.MD` — Design axioms
- `.knowledge/frameworks/patterns/INDEX.MD` — Patterns framework
- `.knowledge/frameworks/patterns/COLLABORATION.MD` — Collaboration patterns
- `.knowledge/frameworks/patterns/DECISION.MD` — Decision patterns
- `.knowledge/frameworks/patterns/INTEGRATION.MD` — Integration patterns
- `.knowledge/frameworks/patterns/PERSISTENCE.MD` — Persistence patterns
- `.knowledge/frameworks/performance/INDEX.MD` — Performance framework
- `.knowledge/frameworks/performance/CACHING_PATTERNS.MD` — Caching strategies
- `.knowledge/frameworks/performance/OPTIMIZATION_STRATEGIES.MD` — Optimization
- `.knowledge/frameworks/performance/PROFILING_GUIDE.MD` — Profiling guide
- `.knowledge/frameworks/resilience/INDEX.MD` — Resilience framework
- `.knowledge/frameworks/resilience/TIMEOUT_PATTERNS.MD` — Timeout patterns
- `.knowledge/frameworks/security/INDEX.MD` — Security framework
- `.knowledge/frameworks/security/AUTHENTICATION.MD` — Authentication
- `.knowledge/frameworks/security/AUTHORIZATION.MD` — Authorization
- `.knowledge/frameworks/security/SECRETS_MANAGEMENT.MD` — Secrets management
- `.knowledge/frameworks/security/SECURITY_CHECKLIST.MD` — Security checklist

### References

- `.knowledge/references/KNOWLEDGE_QUICK_REF.MD` — Knowledge organization patterns
- `.knowledge/references/PERFORMANCE_CHECKLIST.MD` — Performance optimization checks

*Note: Practices, Scenarios, and Templates files are listed in their respective INDEX.MD files.*

---

## 4. Navigation Pattern

```
[layer]/INDEX.MD → [layer]/[topic].md → [layer]/[topic]/[detail].md
```

Each layer has an `INDEX.MD` for navigation. Use layer indexes for discovery, specific files for detailed guidance.

---

## Related

- `config/sage.yaml` — Main configuration
- `docs/design/00-OVERVIEW.MD` — Design overview
- `.context/INDEX.MD` — Project context
- `./INDEX.MD` — Root navigation

---

*Part of SAGE Knowledge Base*
