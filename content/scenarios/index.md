# Scenario Presets

> **Load Time**: On-demand (~30 tokens)  
> **Budget**: ~500 tokens  
> **Purpose**: Context-specific knowledge presets

---

## Available Scenarios

| Scenario | Path | Tokens | Context |
|----------|------|--------|---------|
| **Python Backend** | `python_backend/` | ~200 | Python web service development |

---

## Python Backend Scenario

**Path**: `python_backend/context.md`

### When to Load
- Building Python web services
- FastAPI/Flask development
- REST API implementation
- Python testing with pytest

### Includes
- Python code style guidelines
- Testing strategies for Python
- API design patterns
- Configuration management

### Auto-Load Triggers
| Keywords | Action |
|----------|--------|
| fastapi, flask, django | Load scenario |
| python backend, web service | Load scenario |
| pytest, python test | Load scenario |

---

## Scenario Structure

Each scenario contains:

```
scenarios/[name]/
├── context.md      # Main scenario context
├── checklist.md    # Optional: task checklist
└── templates/      # Optional: scenario-specific templates
```

### Context File Format

```markdown
# [Scenario Name] Context

> **Purpose**: [brief description]
> **Stack**: [technologies]

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

## Creating New Scenarios

1. Create directory: `scenarios/[name]/`
2. Add `context.md` with scenario context
3. Define auto-load triggers in `config/triggers.yaml`
4. Update this index

### Recommended Scenarios (Future)
- `typescript_frontend/` — React/Vue development
- `data_pipeline/` — Data processing workflows
- `devops/` — CI/CD and infrastructure
- `documentation/` — Technical writing projects

---

## Related

- `guidelines/index.md` — General guidelines
- `practices/index.md` — Implementation practices
- `templates/index.md` — Document templates
- `config/triggers.yaml` — Trigger configuration

---

*Scenarios layer — Context-aware knowledge loading*
