# SAGE Naming Conventions

> Project-specific naming standards for SAGE Knowledge Base

---

## Table of Contents

[1. General Rules](#1-general-rules) · [2. Python Elements](#2-python-elements) · [3. SAGE-Specific Patterns](#3-sage-specific-patterns) · [4. Configuration Keys](#4-configuration-keys) · [5. Events](#5-events) · [6. Files & Directories](#6-files--directories)

---

## 1. General Rules

| Principle | Description |
|-----------|-------------|
| Clarity over brevity | Prefer `knowledge_loader` over `kb_ldr` |
| Consistency | Follow existing patterns in the codebase |
| Self-documenting | Names should reveal intent |
| Domain alignment | Use SAGE terminology (Source, Analyze, Generate, Evolve) |

---

## 2. Python Elements

### 2.1 Modules & Packages

| Element | Convention | Example |
|---------|------------|---------|
| Package | `snake_case` | `sage`, `core`, `services` |
| Module | `snake_case.py` | `timeout.py`, `config.py` |
| Sub-package | `snake_case/` | `di/`, `events/`, `memory/` |

### 2.2 Classes

| Type | Convention | Example |
|------|------------|---------|
| Regular class | `PascalCase` | `TimeoutManager`, `KnowledgeLoader` |
| Protocol | `PascalCase` + `Protocol` suffix | `SourceProtocol`, `AnalyzeProtocol` |
| Exception | `PascalCase` + `Error` suffix | `TimeoutError`, `ConfigurationError` |
| Abstract base | `Base` prefix | `BaseAnalyzer`, `BaseChecker` |
| Mixin | `Mixin` suffix | `LoggingMixin`, `EventMixin` |

### 2.3 Functions & Methods

| Type | Convention | Example |
|------|------------|---------|
| Public function | `snake_case` | `load_knowledge()`, `get_config()` |
| Private function | `_snake_case` | `_parse_yaml()`, `_validate_input()` |
| Async function | `snake_case` (no prefix) | `async def load_async()` |
| Property | `snake_case` | `@property def is_loaded()` |
| Factory method | `create_*` or `from_*` | `create_loader()`, `from_config()` |

### 2.4 Variables & Constants

| Type | Convention | Example |
|------|------------|---------|
| Local variable | `snake_case` | `file_path`, `timeout_ms` |
| Instance attribute | `snake_case` | `self.config`, `self._cache` |
| Private attribute | `_snake_case` | `self._internal_state` |
| Constant | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT_MS`, `MAX_RETRIES` |
| Type variable | `PascalCase` or `T` | `T`, `KnowledgeT`, `ConfigT` |

---

## 3. SAGE-Specific Patterns

### 3.1 Protocol Names

SAGE protocols follow the Source-Analyze-Generate-Evolve pattern:

```python
# Core SAGE protocols
class SourceProtocol(Protocol): ...    # S - Knowledge sourcing
class AnalyzeProtocol(Protocol): ...   # A - Processing & analysis
class GenerateProtocol(Protocol): ...  # G - Multi-channel output
class EvolveProtocol(Protocol): ...    # E - Metrics & optimization
```

### 3.2 Service Names

| Service | Class Name | Module |
|---------|------------|--------|
| CLI | `CLIService` | `services/cli.py` |
| MCP | `MCPService` | `services/mcp.py` |
| API | `APIService` | `services/api.py` |

### 3.3 Capability Names

| Type | Class Pattern | Example |
|------|---------------|---------|
| Analyzer | `*Analyzer` | `CodeAnalyzer`, `ContentAnalyzer` |
| Checker | `*Checker` | `HealthChecker`, `ConfigChecker` |
| Monitor | `*Monitor` | `PerformanceMonitor`, `UsageMonitor` |

### 3.4 Domain Models

```python
# Knowledge domain
class KnowledgeAsset: ...      # Base knowledge unit
class KnowledgeLayer: ...      # Layer abstraction (core, frameworks, etc.)
class KnowledgeIndex: ...      # Index/navigation structure

# Session domain
class Session: ...             # User/AI session
class SessionContext: ...      # Session state container
```

---

## 4. Configuration Keys

### 4.1 YAML Configuration

```yaml
# Top-level sections: lowercase
sage:
  version: "0.1.0"

# Nested keys: snake_case
timeout:
  cache_lookup: 100ms
  file_read: 500ms

# Lists: plural nouns
layers:
  - name: core
  - name: frameworks

# Feature flags: is_* or enable_*
features:
  enable_caching: true
  is_debug_mode: false
```

### 4.2 Environment Variables

| Pattern | Example |
|---------|---------|
| `SAGE_` prefix | `SAGE_CONFIG_PATH` |
| `UPPER_SNAKE_CASE` | `SAGE_TIMEOUT_MS` |
| Hierarchical with `__` | `SAGE__TIMEOUT__CACHE_LOOKUP` |

---

## 5. Events

### 5.1 Event Topics

Events follow the pattern: `{domain}.{action}` or `{domain}.{entity}.{action}`

```python
# Domain events
"source.started"           # Source operation started
"source.completed"         # Source operation completed
"source.failed"            # Source operation failed

# Entity events
"knowledge.layer.loaded"   # Specific layer loaded
"knowledge.asset.updated"  # Asset updated

# Lifecycle events
"system.initialized"       # System startup complete
"system.shutdown"          # System shutting down
```

### 5.2 Event Classes

```python
# Event class naming
class SourceStartedEvent: ...
class KnowledgeLoadedEvent: ...
class TimeoutOccurredEvent: ...
```

---

## 6. Files & Directories

### 6.1 Source Files

| Type | Pattern | Example |
|------|---------|---------|
| Module | `snake_case.py` | `timeout_manager.py` |
| Package init | `__init__.py` | Always present |
| Test file | `test_*.py` | `test_timeout.py` |
| Config file | `*.yaml` or `*.yml` | `sage.yaml` |

### 6.2 Documentation Files

| Type | Pattern | Example |
|------|---------|---------|
| Markdown | `kebab-case.md` or `snake_case.md` | `timeout-hierarchy.md` |
| ADR | `ADR-NNNN-title.md` | `ADR-0001-architecture.md` |
| Design doc | `NN-title.md` | `01-architecture.md` |

### 6.3 Directory Structure

| Directory | Purpose | Naming |
|-----------|---------|--------|
| `src/sage/` | Source code | Package name |
| `tests/` | Test suite | Mirrors source |
| `docs/` | Documentation | Categorical |
| `config/` | Configuration | By function |
| `.context/` | Project context | By type |

---

## 7. Anti-Patterns to Avoid

| Avoid | Prefer | Reason |
|-------|--------|--------|
| `kb` abbreviation | `knowledge_base` | Clarity |
| `mgr` suffix | `manager` | Full word |
| `Impl` suffix | Descriptive name | Implementation detail |
| Hungarian notation | Type hints | Python convention |
| `get_*` for properties | `@property` | Pythonic |
| Generic names (`data`, `info`) | Specific names | Self-documenting |

---

## Related

- `.junie/guidelines.md` — General coding guidelines
- `content/practices/engineering/` — Engineering practices
- `docs/design/01-architecture.md` — Architecture patterns

---

*Part of SAGE Knowledge Base - Project Conventions*
