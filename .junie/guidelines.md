# SAGE Knowledge Base - Project Guidelines

> **Purpose**: Primary entry point for JetBrains Junie AI collaboration.
> **Last Updated**: 2025-11-30
> **Version**: 0.1.0
> **Status**: Alpha - Under active development and testing

---

## 📋 Project Overview

**SAGE Knowledge Base (sage-kb)** is a production-grade knowledge management system designed for
AI-human collaboration. It provides structured knowledge via CLI, MCP, and API services with built-in timeout protection
and smart loading.

### Design Philosophy

- **信 (Xin/Faithfulness)**: Accurate, reliable, testable
- **达 (Da/Clarity)**: Clear, maintainable, structured
- **雅 (Ya/Elegance)**: Refined, balanced, sustainable

---

## 🛠️ Tech Stack

| Category     | Technology                 |
|--------------|----------------------------|
| **Language** | Python 3.12+               |
| **CLI**      | Typer + Rich               |
| **MCP**      | FastMCP                    |
| **API**      | FastAPI + Uvicorn          |
| **Config**   | PyYAML + Pydantic-Settings |
| **Logging**  | structlog + stdlib logging |
| **Testing**  | pytest + pytest-asyncio    |
| **Linting**  | Ruff + MyPy                |

---

## 📁 Project Structure

```
sage-kb/
├── .backups/        # Backup files (git-ignored)
├── .junie/          # JetBrains Junie configuration (this directory)
├── .context/        # Project-specific knowledge base
├── .history/        # AI session history and handoffs
├── .archive/        # Historical archives
├── .logs/           # Runtime log files (git-ignored)
├── .outputs/        # Intermediate process files (git-ignored)
├── config/          # Runtime configuration (modular YAML)
├── docs/            # User-facing documentation
├── content/         # Generic knowledge (distributable)
├── src/sage/        # Source code (3-layer architecture)
├── tools/           # Development tools
└── tests/           # Test suite
```

### Key Directories Explained

| Directory   | Purpose                                        | Visibility |
|-------------|------------------------------------------------|------------|
| `.backups/` | Backup files                                   | Hidden     |
| `.junie/`   | AI client config for JetBrains Junie           | Hidden     |
| `.context/` | Project-specific knowledge (ADRs, conventions) | Hidden     |
| `.history/` | AI session records and task handoffs           | Hidden     |
| `.archive/` | Historical/deprecated content                  | Hidden     |
| `.logs/`    | Runtime log files                              | Hidden     |
| `.outputs/` | Intermediate process files                     | Hidden     |
| `config/`   | Runtime configuration (modular YAML structure) | Visible    |
| `docs/`     | User-facing documentation                      | Visible    |
| `content/`  | Generic, distributable knowledge               | Visible    |

---

## 📐 Coding Standards

### Python Style

- **Formatter**: Ruff (line-length: 88)
- **Type Hints**: Required for all public functions
- **Docstrings**: Google style
- **Imports**: Sorted by ruff (isort compatible)

### Naming Conventions

| Element   | Convention         | Example              |
|-----------|--------------------|----------------------|
| Files     | `snake_case.py`    | `timeout_manager.py` |
| Classes   | `PascalCase`       | `TimeoutLoader`      |
| Functions | `snake_case`       | `load_with_timeout`  |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT_MS` |

### Architecture Rules

- **Three-Layer Model**: Core → Services → Capabilities
- **Dependency Direction**: Services depend on Core, never reverse
- **Protocol-First**: Use `typing.Protocol` for interfaces
- **Zero Cross-Import**: Layers communicate via EventBus

---

## 📄 Important Files

| File                 | Purpose                                          |
|----------------------|--------------------------------------------------|
| `config/sage.yaml`   | Main configuration (timeouts, triggers, loading) |
| `docs/design/`       | Design documents (architecture, services, etc.)  |
| `src/sage/core/`     | Core layer (loader, timeout, config)             |
| `src/sage/services/` | Service layer (CLI, MCP, API)                    |
| `pyproject.toml`     | Python project configuration                     |
| `index.md`           | Knowledge base navigation entry                  |

---

## 🤖 AI Collaboration Rules

### Autonomy Levels

> **Reference**: See `content/frameworks/autonomy/levels.md` for full 6-level autonomy framework

| Level | Name                        | Description           | Example Tasks                                        |
|-------|-----------------------------|-----------------------|------------------------------------------------------|
| L1-L2 | Minimal/Low (0-40%)         | Ask before changes    | Breaking changes, new dependencies, critical systems |
| L3-L4 | Medium/Medium-High (40-80%) | Proceed, report after | Bug fixes, refactoring, routine development ⭐        |
| L5-L6 | High/Full (80-100%)         | High autonomy         | Formatting, comments, docs, trusted patterns         |

**Default**: L4 (Medium-High) for mature collaboration.

### Key Behaviors

1. **Always respect timeout limits** (T1:100ms → T5:10s)
2. **Use English** for code and documentation
3. **Follow existing patterns** in the codebase
4. **Run tests** before committing changes
5. **Update relevant documentation** when modifying features
6. **Output files to `.outputs/`** — All temporary/intermediate files must go to `.outputs/`, never project root
7. **Create session records** for significant work sessions (see Session History below)

### Session History Management

At the end of significant work sessions, create appropriate records in `.history/`:

| Record Type | When to Create | Location | Template |
|-------------|----------------|----------|----------|
| **Session State** | Active work in progress | `.history/current/` | `_example-session-*.md` |
| **Conversation** | Important decisions/outcomes | `.history/conversations/` | `_example-*-review.md` |
| **Handoff** | Task continuation needed | `.history/handoffs/` | `_example-*-handoff.md` |

**Session End Checklist:**

1. ☐ Summarize completed tasks and key decisions
2. ☐ Document any pending items or blockers
3. ☐ Note important findings or lessons learned
4. ☐ If work continues: create handoff document
5. ☐ If significant decisions made: create conversation record
6. ☐ Clear `.history/current/` of completed session files

**Naming Convention:**
- Conversations: `YYYY-MM-DD-topic.md` (e.g., `2025-11-30-knowledge-reorganization.md`)
- Handoffs: `YYYY-MM-DD-task-handoff.md` (e.g., `2025-11-30-api-refactor-handoff.md`)
- Sessions: `session-YYYYMMDD-HHMM.md` (e.g., `session-20251130-0010.md`)

> **Reference**: See `.history/index.md` for detailed usage guidelines and retention policies.

### Expert Committee Pattern

For complex decisions, simulate a **Level 5 Expert Committee** review with:

- **Architecture Group** (6 experts): System design, scalability
- **Knowledge Engineering Group** (6 experts): Content structure, taxonomy
- **AI Collaboration Group** (6 experts): Human-AI interaction patterns
- **Engineering Practice Group** (6 experts): Code quality, testing

---

## ⏱️ Timeout Hierarchy

| Level | Timeout | Scope            | Action on Timeout      |
|-------|---------|------------------|------------------------|
| T1    | 100ms   | Cache lookup     | Return cached/fallback |
| T2    | 500ms   | Single file      | Use partial/fallback   |
| T3    | 2s      | Layer load       | Load partial + warning |
| T4    | 5s      | Full KB load     | Emergency core only    |
| T5    | 10s     | Complex analysis | Abort + summary        |

---

## 🔗 References

- **Design Documents**: @file:docs/design/00-overview.md
- **Documentation Index**: @file:docs/index.md
- **Configuration**: @file:config/sage.yaml
- **Project Context**: @file:.context/index.md
- **Knowledge Content**: @file:content/index.md
- **Directory Conventions**: @file:content/practices/documentation/project_directory_structure.md
- **Timeout Hierarchy**: @file:.context/policies/timeout_hierarchy.md
- **Core Principles**: @file:content/core/principles.md

---

## 📝 Quick Commands

```bash
# Run tests
pytest tests/ -v

# Start MCP server
sage serve

# CLI usage
sage get --layer core
sage search "timeout"
sage info
```

---

*This guideline follows the SAGE design philosophy: 信达雅 (Xin-Da-Ya)*
