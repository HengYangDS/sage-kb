# SAGE Project Quick Reference

> Thin reference layer for SAGE project — links to authoritative sources in `.context/` and `.knowledge/`

---

## Quick Navigation

| Topic | Authoritative Source |
|:------|:---------------------|
| **Project Overview** | [`.context/overview/PROJECT_OVERVIEW.md`](../../.context/overview/PROJECT_OVERVIEW.md) |
| **Context Navigation** | [`.context/INDEX.md`](../../.context/INDEX.md) |
| **Naming Conventions** | [`.context/conventions/NAMING.md`](../../.context/conventions/NAMING.md) |
| **Code Patterns** | [`.context/conventions/CODE_PATTERNS.md`](../../.context/conventions/CODE_PATTERNS.md) |
| **Timeout Hierarchy** | [`.context/policies/TIMEOUT_HIERARCHY.md`](../../.context/policies/TIMEOUT_HIERARCHY.md) |
| **AI Calibration** | [`.context/intelligence/calibration/CALIBRATION.md`](../../.context/intelligence/calibration/CALIBRATION.md) |
| **Session Automation** | [`.context/intelligence/automation/SESSION_AUTOMATION_REQUIREMENTS.md`](../../.context/intelligence/automation/SESSION_AUTOMATION_REQUIREMENTS.md) |
| **Expert Committee** | [`.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md`](../../.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md) |
| **Code Style** | [`.knowledge/guidelines/CODE_STYLE.md`](../../.knowledge/guidelines/CODE_STYLE.md) |
| **Python Guidelines** | [`.knowledge/guidelines/PYTHON.md`](../../.knowledge/guidelines/PYTHON.md) |

---

## Tech Stack

| Category | Technology |
|:---------|:-----------|
| Language | Python 3.12+ |
| CLI | Typer + Rich |
| MCP | FastMCP |
| API | FastAPI + Uvicorn |
| Config | PyYAML + Pydantic-Settings |
| Logging | structlog + stdlib logging |
| Testing | pytest + pytest-asyncio |
| Linting | Ruff + MyPy |

---

## Quick Commands

```bash
# Testing
pytest tests/ -v                    # Run all tests
pytest tests/unit/ -v               # Unit tests only
pytest tests/integration/ -v        # Integration tests only

# Services
sage serve                          # Start MCP server
sage get --layer core               # Get core layer content
sage search "timeout"               # Search knowledge base
sage info                           # System information

# Development
ruff check src/                     # Lint check
ruff format src/                    # Format code
mypy src/                           # Type check
```

---

## Key Paths

| Category | Path | Purpose |
|:---------|:-----|:--------|
| **Context** | `.context/` | Project-specific knowledge (SSOT) |
| **Knowledge** | `.knowledge/` | Generic reusable knowledge |
| **Conventions** | `.context/conventions/` | Naming, patterns, structure |
| **Policies** | `.context/policies/` | Timeouts, loading, runtime |
| **ADRs** | `.context/decisions/` | Architecture decisions |
| **AI Patterns** | `.context/intelligence/` | Calibration, learning, optimization |
| **Config** | `config/sage.yaml` | Main configuration |
| **Core Code** | `src/sage/core/` | Core layer |
| **Services** | `src/sage/services/` | CLI, MCP, API |
| **History** | `.history/` | Session records and handoffs |

---

## Key Behaviors

> Full details: `.context/policies/` and `.context/conventions/`

| Behavior | Reference |
|:---------|:----------|
| Architecture patterns | `.context/conventions/CODE_PATTERNS.md` |
| Timeout limits (T1-T5) | `.context/policies/TIMEOUT_HIERARCHY.md` |
| Naming conventions | `.context/conventions/NAMING.md` |
| File structure | `.context/conventions/FILE_STRUCTURE.md` |
| Session records | `.history/` (see `.context/intelligence/automation/`) |

---

## Session End Checklist

> Full checklist: `.history/_SESSION-END-CHECKLIST.md`

| Directory | Purpose | Pattern |
|:----------|:--------|:--------|
| `conversations/` | Key decisions | `YYYYMMDD-TOPIC.md` |
| `handoffs/` | Task continuation | `YYYYMMDD-TASK-HANDOFF.md` |
| `current/` | Active work state | `current-state.md` |

---

## Related

- [Junie Guidelines](../guidelines.md) — Core Junie AI rules
- [Project Config](config.yaml) — Project identity and settings
- [.context/INDEX.md](../../.context/INDEX.md) — Full project context navigation
- [.knowledge/INDEX.md](../../.knowledge/INDEX.md) — Generic knowledge index

---

*This file follows MECE and SSOT principles — detailed knowledge lives in `.context/` and `.knowledge/`*
