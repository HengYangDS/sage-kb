# Scenario Presets

> Context-specific knowledge presets for common development scenarios

---

## Table of Contents

- [1. Scenario Selection Guide](#1-scenario-selection-guide)
- [2. Available Scenarios](#2-available-scenarios)
- [3. Scenario Structure](#3-scenario-structure)
- [4. Creating New Scenarios](#4-creating-new-scenarios)

---

## 1. Scenario Selection Guide

### Quick Decision Tree

```
What are you building?
├─ Backend service
│  ├─ Python? → python_backend/
│  └─ Distributed? → microservices/
├─ Frontend application
│  └─ TypeScript/React/Vue? → typescript_frontend/
├─ Infrastructure
│  ├─ CI/CD pipelines? → devops/
│  ├─ Data processing? → data_pipeline/
│  └─ Single repo, multiple projects? → monorepo/
├─ Integration
│  ├─ MCP/AI tools? → mcp_integration/
│  └─ Plugin/extension? → plugin_development/
├─ Modernization
│  └─ Updating legacy system? → legacy_modernization/
└─ Documentation
   ├─ Technical docs? → documentation/
   └─ Knowledge system? → knowledge_management/
```

### Selection by Project Type

| Project Type | Primary Scenario | Often Combined With |
|--------------|------------------|---------------------|
| Web API | python_backend | devops, microservices |
| SPA/PWA | typescript_frontend | devops |
| Full-stack | python_backend + typescript_frontend | devops, monorepo |
| Data platform | data_pipeline | devops, microservices |
| AI integration | mcp_integration | python_backend |
| IDE extension | plugin_development | typescript_frontend |
| System upgrade | legacy_modernization | devops |
| Docs site | documentation | knowledge_management |

### Selection by Team Size

| Team Size | Recommended Scenarios |
|-----------|----------------------|
| Solo/Small (1-3) | python_backend, typescript_frontend |
| Medium (4-10) | + devops, monorepo |
| Large (10+) | + microservices, knowledge_management |

---

## 2. Available Scenarios

| Scenario                 | Path                      | Purpose                           |
|--------------------------|---------------------------|-----------------------------------|
| **Data Pipeline**        | `data_pipeline/`          | ETL and data processing workflows |
| **DevOps**               | `devops/`                 | CI/CD and infrastructure          |
| **Documentation**        | `documentation/`          | Technical writing projects        |
| **Knowledge Management** | `knowledge_management/`   | Knowledge base system development |
| **Legacy Modernization** | `legacy_modernization/`   | Legacy system updates             |
| **MCP Integration**      | `mcp_integration/`        | Model Context Protocol services   |
| **Microservices**        | `microservices/`          | Microservices architecture        |
| **Monorepo**             | `monorepo/`               | Monorepo management               |
| **Plugin Development**   | `plugin_development/`     | Plugin development                |
| **Python Backend**       | `python_backend/`         | Python web service development    |
| **TypeScript Frontend**  | `typescript_frontend/`    | React/Vue frontend development    |

Each scenario contains:
- `INDEX.md` — Scenario navigation
- `CONTEXT.md` — Main scenario context
- `CHECKLIST.md` — Task checklist

---

## 3. Scenario Structure

```text
scenarios/[name]/
├── INDEX.md        # Scenario navigation
├── CONTEXT.md      # Main scenario context
└── CHECKLIST.md    # Task checklist
```
### Context File Format

```markdown
# [Scenario Name] Context
> [Brief description]
## Quick Setup
[Essential setup steps]
## Key Guidelines
[Scenario-specific guidelines]
## Common Tasks
[Frequent operations]
## Pitfalls
[Common mistakes to avoid]
```
---

## 4. Creating New Scenarios

1. Create directory: `.knowledge/scenarios/[name]/`
2. Add `INDEX.md` with scenario navigation
3. Add `CONTEXT.md` with scenario context
4. Add `CHECKLIST.md` with task checklist
5. Define auto-load triggers in `config/knowledge/triggers.yaml`
6. Update this index

---

## Related

- `.knowledge/guidelines/INDEX.md` — General guidelines
- `.knowledge/practices/INDEX.md` — Implementation practices
- `.knowledge/templates/INDEX.md` — Document templates
- `config/knowledge/triggers.yaml` — Trigger configuration

---

*Scenario Presets v1.1*
*Updated: 2025-12-01 - Added scenario selection guide (§1)*

---

*AI Collaboration Knowledge Base*
