# Design Axioms Framework

> **Load Time**: On-demand (~400 tokens)  
> **Purpose**: Core design principles guiding SAGE Knowledge Base architecture  
> **Philosophy**: 信达雅 (Xin-Da-Ya) applied to software design

---

## Overview

The SAGE Knowledge Base is built upon 8 foundational design axioms. These principles ensure consistency, maintainability, and reliability across all components.

---

## 1. MECE Principle

**Mutually Exclusive, Collectively Exhaustive**

### Definition

Every classification system should have:
- **Mutually Exclusive**: No overlap between categories
- **Collectively Exhaustive**: All cases are covered

### Application

| Area | Implementation |
|------|----------------|
| Directory structure | Each file belongs to exactly one directory |
| Configuration | Each setting defined in exactly one place |
| Responsibilities | Each component has clear, non-overlapping duties |
| Documentation | Each topic covered in one authoritative location |

### Anti-Patterns

- ❌ Duplicate content across multiple files
- ❌ Overlapping responsibilities between modules
- ❌ Same configuration in multiple locations

---

## 2. Single Source of Truth (SSOT)

**Each piece of knowledge exists in exactly one place**

### Definition

The Single Source of Truth principle ensures that every piece of information, configuration, or knowledge has exactly one authoritative location. All other references point to this source rather than duplicating it.

### Why SSOT Matters

| Problem Without SSOT | Solution With SSOT |
|---------------------|-------------------|
| Inconsistent data across locations | One authoritative source |
| Update synchronization nightmares | Update once, reflect everywhere |
| Confusion about which version is correct | Clear authoritative reference |
| Maintenance burden multiplied | Single point of maintenance |
| Divergence over time | Guaranteed consistency |

### SSOT in SAGE

| Domain | Single Source | References Point To |
|--------|---------------|---------------------|
| **Configuration** | `sage.yaml` + `config/*.yaml` | All services, loaders, CLI |
| **Timeouts** | `config/timeout.yaml` | loader.py, mcp_server.py, cli.py |
| **Quality Thresholds** | `config/quality.yaml` | analyzers, checkers |
| **Design Principles** | This document | docs/design/, guidelines |
| **Autonomy Levels** | `frameworks/autonomy/levels.md` | All AI collaboration docs |
| **Token Budget** | `config/token_budget.yaml` | memory/, services/ |

### Implementation Patterns

#### Pattern 1: Configuration Reference

```markdown
> **Location**: `config/timeout.yaml` → `timeout.operations`

See configuration file for current values.
```

#### Pattern 2: Cross-Reference

```markdown
See [Autonomy Levels](../autonomy/levels.md) for the complete 6-level framework.
```

#### Pattern 3: Import from Source

```python
from sage.core.config import load_config

config = load_config()
timeout_ms = config.get("timeout", {}).get("operations", {}).get("full_load", 5000)
```

### Anti-Patterns

- ❌ Hardcoding values that exist in configuration
- ❌ Copy-pasting documentation across files
- ❌ Maintaining parallel versions of the same information
- ❌ Duplicating default values in multiple locations

### SSOT Checklist

Before adding information, ask:

1. **Does this information already exist elsewhere?**
   - If yes → reference the existing source
   - If no → create it in the most appropriate location

2. **Is this the right location for this information?**
   - Configuration → `config/*.yaml`
   - Principles → `content/frameworks/`
   - Guidelines → `content/guidelines/`
   - API docs → `docs/api/`

3. **Will this need to be updated in sync with something else?**
   - If yes → consolidate into single source

---

## 3. Progressive Disclosure

**From overview to detail**

### Definition

Information should be organized in layers, from high-level summary to detailed specifics.

### Implementation

```
Level 0: index.md          (~100 tokens) - Navigation entry
Level 1: core/             (~500 tokens) - Core principles
Level 2: guidelines/       (~1,200 tokens) - Engineering guidelines
Level 3: frameworks/       (~2,000 tokens) - Deep frameworks
Level 4: practices/        (~1,500 tokens) - Best practices
```

### Application

- Start with summary, expand on request
- Load minimal context first, add detail as needed
- Use headers to enable scanning

---

## 4. Separation of Concerns

**Content, code, and configuration separated**

### Definition

Different aspects of the system should be isolated into distinct modules with clear boundaries.

### SAGE Layers

| Layer | Responsibility | Cannot Import |
|-------|---------------|---------------|
| Core | Infrastructure, protocols | Services, Capabilities |
| Services | CLI, MCP, API interfaces | Each other |
| Capabilities | Analyzers, Checkers, Monitors | Services |
| Tools | Dev-only utilities | Runtime imports |

### File Type Separation

| Type | Location | Purpose |
|------|----------|---------|
| Content | `content/` | Knowledge markdown files |
| Code | `src/sage/` | Python implementation |
| Config | `config/` | YAML configuration |
| Tests | `tests/` | Test suites |
| Docs | `docs/` | Technical documentation |

---

## 5. Fail-Fast with Timeout

**No operation hangs indefinitely**

### Definition

Every operation must complete within a defined timeout, returning partial results or graceful fallback rather than blocking.

### Timeout Hierarchy

| Level | Timeout | Scope |
|-------|---------|-------|
| T1 | 100ms | Cache lookup |
| T2 | 500ms | Single file read |
| T3 | 2s | Layer load |
| T4 | 5s | Full KB load |
| T5 | 10s | Complex analysis |

### Fallback Strategy

```
Timeout → Return partial → Use fallback → Log warning → Never hang
```

> **Reference**: See `config/timeout.yaml` for configuration and `content/frameworks/timeout/hierarchy.md` for details.

---

## 6. Plugin Extensibility

**15 extension points for customization**

### Definition

The system provides well-defined hooks for extending functionality without modifying core code.

### Hook Categories

| Category | Hooks |
|----------|-------|
| Loader | `pre_load`, `post_load`, `on_timeout` |
| Search | `pre_search`, `post_search` |
| Format | `pre_format`, `post_format` |
| Analyzer | `pre_analyze`, `analyze`, `post_analyze` |
| Lifecycle | `on_startup`, `on_shutdown` |
| Error | `on_error` |
| Cache | `on_cache_hit`, `on_cache_miss` |

> **Reference**: See `docs/design/05-plugin-memory.md` for plugin architecture.

---

## 7. Zero Cross-Import

**Layers communicate via EventBus, no direct dependencies**

### Definition

Components in different layers should not import each other directly. Communication happens through:
- EventBus for async decoupling
- DI Container for dependency injection
- Protocol interfaces for contracts

### Allowed Dependencies

```
✅ Services → Core
✅ Services → Capabilities
✅ Capabilities → Core
❌ Core → Services
❌ Core → Capabilities
❌ Services ↔ Services
```

---

## 8. On-Demand Loading

**Minimal core engine, features loaded as needed**

### Definition

Only load what is needed for the current operation. Defer loading of optional features until requested.

### Implementation

| Content | Load Trigger |
|---------|--------------|
| Core principles | Always |
| Guidelines | Keyword-triggered |
| Frameworks | Task-specific |
| Practices | On request |

### Benefits

- Reduced initial load time
- Lower token consumption
- Faster response times
- Better resource utilization

---

## Quick Reference Card

| Axiom | One-Liner |
|-------|-----------|
| **MECE** | No overlap, no gaps |
| **SSOT** | One source, many references |
| **Progressive Disclosure** | Overview first, detail on demand |
| **Separation of Concerns** | Content, code, config apart |
| **Fail-Fast** | Always return, never hang |
| **Plugin Extensibility** | 15 hooks for customization |
| **Zero Cross-Import** | EventBus for communication |
| **On-Demand Loading** | Load only what's needed |

---

## Axiom Application Matrix

| Axiom | Code | Config | Content | Architecture |
|-------|------|--------|---------|--------------|
| MECE | ✓ | ✓ | ✓ | ✓ |
| SSOT | ✓ | ✓ | ✓ | ✓ |
| Progressive Disclosure | | | ✓ | ✓ |
| Separation of Concerns | ✓ | ✓ | ✓ | ✓ |
| Fail-Fast | ✓ | ✓ | | |
| Plugin Extensibility | ✓ | ✓ | | ✓ |
| Zero Cross-Import | ✓ | | | ✓ |
| On-Demand Loading | ✓ | ✓ | ✓ | |

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| `docs/design/00-overview.md` | Design philosophy overview |
| `docs/design/01-architecture.md` | Architecture implementation |
| `content/core/principles.md` | Xin-Da-Ya philosophy |
| `content/frameworks/timeout/hierarchy.md` | Timeout details |
| `docs/design/05-plugin-memory.md` | Plugin architecture |

---

*These axioms guide all design decisions in the SAGE Knowledge Base.*
