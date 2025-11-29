# Design Axioms Framework

> 8 foundational design principles (信达雅 applied to software design)

---

## Overview

| # | Axiom                      | Principle                        |
|---|----------------------------|----------------------------------|
| 1 | **MECE**                   | No overlap, no gaps              |
| 2 | **SSOT**                   | One source, many references      |
| 3 | **Progressive Disclosure** | Overview first, detail on demand |
| 4 | **Separation of Concerns** | Content, code, config apart      |
| 5 | **Fail-Fast**              | Always return, never hang        |
| 6 | **Plugin Extensibility**   | 15 hooks for customization       |
| 7 | **Zero Cross-Import**      | EventBus for communication       |
| 8 | **On-Demand Loading**      | Load only what's needed          |

---

## 1. MECE Principle

**Mutually Exclusive, Collectively Exhaustive** — No overlap, all cases covered

| Area             | Implementation                     |
|------------------|------------------------------------|
| Directory        | Each file in exactly one directory |
| Config           | Each setting defined once          |
| Responsibilities | Clear, non-overlapping duties      |
| Documentation    | One authoritative location         |

**Anti-patterns**: Duplicate content · Overlapping responsibilities · Config in multiple locations

---

## 2. Single Source of Truth (SSOT)

**Each knowledge piece exists in exactly one place** — Update once, reflect everywhere

| Domain          | Single Source                   |
|-----------------|---------------------------------|
| Configuration   | `sage.yaml` + `config/*.yaml`   |
| Timeouts        | `config/timeout.yaml`           |
| Quality         | `config/quality.yaml`           |
| Autonomy Levels | `frameworks/autonomy/levels.md` |

**Before adding**: Exists elsewhere? → Reference. Right location? Needs sync? → Consolidate.

---

## 3. Progressive Disclosure

**From overview to detail** — Start with summary, expand on request

| Level | Location      | Depth           |
|-------|---------------|-----------------|
| L0    | `index.md`    | Navigation      |
| L1    | `core/`       | Principles      |
| L2    | `guidelines/` | Guidelines      |
| L3    | `frameworks/` | Deep frameworks |
| L4    | `practices/`  | Best practices  |

---

## 4. Separation of Concerns

**Content, code, configuration separated**

| Layer        | Responsibility            | Cannot Import          |
|--------------|---------------------------|------------------------|
| Core         | Infrastructure, protocols | Services, Capabilities |
| Services     | CLI, MCP, API             | Each other             |
| Capabilities | Analyzers, Checkers       | Services               |

| Type    | Location    |
|---------|-------------|
| Content | `content/`  |
| Code    | `src/sage/` |
| Config  | `config/`   |
| Tests   | `tests/`    |
| Docs    | `docs/`     |

---

## 5. Fail-Fast with Timeout

**No operation hangs** — Return partial or fallback

| Level | Timeout | Scope    |
|-------|---------|----------|
| T1    | 100ms   | Cache    |
| T2    | 500ms   | File     |
| T3    | 2s      | Layer    |
| T4    | 5s      | Full KB  |
| T5    | 10s     | Analysis |

**Strategy**: Timeout → Partial → Fallback → Log → Never hang

---

## 6. Plugin Extensibility

**15 extension points** — Well-defined hooks without core modification

| Category    | Hooks                                       |
|-------------|---------------------------------------------|
| Loader      | `pre_load`, `post_load`, `on_timeout`       |
| Search      | `pre_search`, `post_search`                 |
| Format      | `pre_format`, `post_format`                 |
| Analyzer    | `pre_analyze`, `analyze`, `post_analyze`    |
| Lifecycle   | `on_startup`, `on_shutdown`                 |
| Error/Cache | `on_error`, `on_cache_hit`, `on_cache_miss` |

---

## 7. Zero Cross-Import

**Layers communicate via EventBus**

**Allowed**: Services → Core · Services → Capabilities · Capabilities → Core

**Forbidden**: Core → Services · Core → Capabilities · Services ↔ Services

**Via**: EventBus (async) · DI Container · Protocol interfaces

---

## 8. On-Demand Loading

**Minimal core, features loaded as needed**

| Content         | Load Trigger      |
|-----------------|-------------------|
| Core principles | Always            |
| Guidelines      | Keyword-triggered |
| Frameworks      | Task-specific     |
| Practices       | On request        |

**Benefits**: Reduced load · Lower tokens · Faster response

---

## 📊 Axiom Application Matrix

| Axiom                  | Code | Config | Content | Arch |
|------------------------|:----:|:------:|:-------:|:----:|
| MECE                   |  ✓   |   ✓    |    ✓    |  ✓   |
| SSOT                   |  ✓   |   ✓    |    ✓    |  ✓   |
| Progressive Disclosure |      |        |    ✓    |  ✓   |
| Separation of Concerns |  ✓   |   ✓    |    ✓    |  ✓   |
| Fail-Fast              |  ✓   |   ✓    |         |      |
| Plugin Extensibility   |  ✓   |   ✓    |         |  ✓   |
| Zero Cross-Import      |  ✓   |        |         |  ✓   |
| On-Demand Loading      |  ✓   |   ✓    |    ✓    |      |

---

**Related**: `docs/design/00-overview.md` · `docs/design/01-architecture.md` · `content/core/principles.md`

*Part of SAGE Knowledge Base*
