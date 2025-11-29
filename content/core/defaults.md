# Default Behaviors and Calibration

> **Load Priority**: Always Load  
> **Purpose**: Establish baseline behaviors and calibration parameters  
> **Configuration**: See `sage.yaml` for actual values (Single Source of Truth)

---

<a id="toc"></a>
## 📑 Table of Contents

| Section                                                       | Description                                  |
|---------------------------------------------------------------|----------------------------------------------|
| [🎯 Default Autonomy Settings](#default-autonomy-settings)    | Context-based autonomy levels                |
| [📋 Default Behaviors](#default-behaviors)                    | Communication, code changes, decision-making |
| [⚙️ Configuration Reference](#configuration-reference)        | All config modules with defaults             |
| [🔄 Calibration Workflow](#calibration-workflow)              | Autonomy adjustment process                  |
| [🚨 Override Conditions](#override-conditions)                | When to force different autonomy             |
| [📊 Default Response Structure](#default-response-structure)  | Standard response format                     |
| [⏱️ Fallback Behavior](#fallback-behavior)                    | Timeout and error handling                   |
| [📚 Related Documentation](#related-documentation)            | Links to detailed docs                       |

---

<a id="default-autonomy-settings"></a>
## 🎯 Default Autonomy Settings

> **Reference**: `content/frameworks/autonomy/levels.md`

| Context             | Level | Rationale             |
|---------------------|-------|-----------------------|
| New project         | L2    | Build trust gradually |
| Established project | L4    | Proven patterns       |
| Critical changes    | L1-L2 | High stakes           |
| Routine maintenance | L4    | Low risk              |
| Documentation       | L4-L5 | Well-defined scope    |
| Refactoring         | L3-L4 | Needs verification    |

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="default-behaviors"></a>
## 📋 Default Behaviors

| Area                | Aspect        | Default                          |
|---------------------|---------------|----------------------------------|
| **Communication**   | Verbosity     | Concise with detail on request   |
|                     | Format        | Markdown with code blocks        |
|                     | Language      | Match user's (default: English)  |
|                     | Uncertainty   | State explicitly when unsure     |
| **Code Changes**    | Scope         | Minimal necessary changes        |
|                     | Style         | Follow existing conventions      |
|                     | Comments      | Match existing frequency         |
|                     | Tests         | Run affected tests when possible |
| **Decision-Making** | Ambiguity     | Ask for clarification            |
|                     | Risk          | Err on side of caution           |
|                     | Reversibility | Prefer reversible actions        |
|                     | Documentation | Document significant decisions   |

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="configuration-reference"></a>
## ⚙️ Configuration Reference

> **Single Source of Truth**: `sage.yaml` (entry) + `config/*.yaml` (modules)

### Timeout (`config/timeout.yaml`)

| Level | Key                       | Default  | Purpose          |
|-------|---------------------------|----------|------------------|
| T1    | `operations.cache_lookup` | 100ms    | Cache hit        |
| T2    | `operations.file_read`    | 500ms    | Single file      |
| T3    | `operations.layer_load`   | 2s       | Layer/directory  |
| T4    | `operations.full_load`    | 5s       | Complete KB      |
| T5    | `operations.analysis`     | 10s      | Complex analysis |
| -     | `operations.mcp_call`     | 10s      | MCP tool         |
| -     | `operations.search`       | 3s       | Search           |
| -     | `global_max` / `default`  | 10s / 5s | Max / default    |

**Circuit Breaker**: `enabled`=true, `failure_threshold`=3, `reset_timeout`=30s, `half_open_requests`=1

**Strategies** (`on_timeout`): `return_partial` · `use_fallback` · `log_warning` · `never_hang`

### Loading (`config/loading.yaml`)

| Key              | Default                                                                     | Purpose                |
|------------------|-----------------------------------------------------------------------------|------------------------|
| `max_tokens`     | 4000                                                                        | Max tokens per request |
| `default_layers` | `[core]`                                                                    | Default layers         |
| `always`         | `index.md`, `content/core/principles.md`, `content/core/quick_reference.md` | Pre-cached             |

### Quality (`config/quality.yaml`)

| Category | Key                                     | Default  |
|----------|-----------------------------------------|----------|
| Code     | `min_test_coverage`                     | 95%      |
| Code     | `max_function_lines` / `max_file_lines` | 50 / 500 |
| Code     | `max_complexity`                        | 10       |
| Style    | `max_line_length`                       | 88       |
| Style    | `min_type_hint_coverage`                | 50%      |
| Docs     | `max_doc_line_length`                   | 120      |

### Token Budget (`config/token_budget.yaml`)

| Key               | Default                                                          | Purpose                           |
|-------------------|------------------------------------------------------------------|-----------------------------------|
| `max_tokens`      | 128000                                                           | Context window                    |
| `reserved_tokens` | 4000                                                             | Response reserve                  |
| `thresholds`      | NORMAL<70%, WARNING=70%, CAUTION=80%, CRITICAL=90%, OVERFLOW=95% | Action triggers                   |
| `auto_actions`    | `summarize`=true, `prune`=true                                   | Auto-actions at CRITICAL/OVERFLOW |

### Memory (`config/memory.yaml`)

| Key                            | Default                    | Purpose             |
|--------------------------------|----------------------------|---------------------|
| `store.backend` / `store.path` | `file` / `.history/memory` | Storage config      |
| `session.auto_checkpoint`      | true                       | Auto-checkpoint     |
| `session.checkpoint_interval`  | 300s                       | Checkpoint interval |
| `session.max_history`          | 100                        | Max entries         |

### Plugins (`config/plugins.yaml`)

| Component           | Key                                                                                | Default                     |
|---------------------|------------------------------------------------------------------------------------|-----------------------------|
| **Loader**          | `cache_enabled` / `cache_ttl`                                                      | true / 300s                 |
| **Content Cache**   | `enabled` / `max_entries` / `max_size_bytes` / `ttl_seconds`                       | true / 1000 / 50MB / 3600s  |
| **Semantic Search** | `enabled` / `min_term_length` / `max_results` / `score_threshold` / `use_stemming` | true / 2 / 20 / 0.1 / false |

### Logging (`config/logging.yaml`)

`level`=INFO · `format`=structured · `include_timestamps`=true

### Features (`config/features.yaml`)

| Feature                | Default | Feature                | Default |
|------------------------|---------|------------------------|---------|
| `event_driven_plugins` | true    | `differential_loading` | false   |
| `memory_persistence`   | true    | `compressed_loading`   | false   |
| `api_service`          | false   | `client_cache`         | true    |
| `lazy_expansion`       | true    | `context_pruning`      | false   |

### DI (`config/di.yaml`)

`auto_wire`=true

| Service          | Lifetime  | Implementation  |
|------------------|-----------|-----------------|
| `EventBus`       | singleton | `AsyncEventBus` |
| `SourceProtocol` | singleton | `TimeoutLoader` |
| `MemoryStore`    | singleton | `MemoryStore`   |
| `TokenBudget`    | singleton | `TokenBudget`   |

### API (`config/api.yaml`) – disabled by default

| Key                     | Default          | Key                        | Default          |
|-------------------------|------------------|----------------------------|------------------|
| `enabled`               | false            | `cors.enabled` / `origins` | true / `["*"]`   |
| `host` / `port`         | `0.0.0.0` / 8080 | `docs.enabled` / `path`    | true / `/docs`   |
| `rate_limit.enabled`    | false            | `health.enabled` / `path`  | true / `/health` |
| `request.max_body_size` | 1MB              | `request.timeout_ms`       | 30s              |

### Other Configs

| File                     | Section               | Purpose               |
|--------------------------|-----------------------|-----------------------|
| `config/guidelines.yaml` | `guidelines.sections` | Alias mapping         |
| `config/triggers.yaml`   | `triggers`            | Keyword-based loading |

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="calibration-workflow"></a>
## 🔄 Calibration Workflow

**Initial**: L2-L3 → small tasks → feedback → adjust

| Success Rate | Adjustment  |
|--------------|-------------|
| > 95%        | +1 (max L5) |
| 85-95%       | Maintain    |
| 70-85%       | -1          |
| < 70%        | -2, review  |

**Triggers**: Major errors · New domain · Team change · Extended absence

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="override-conditions"></a>
## 🚨 Override Conditions

| Force Lower (L1-L2)    | Allow Higher (L5-L6)     |
|------------------------|--------------------------|
| Production deployments | Explicitly granted       |
| Database migrations    | Routine + tested         |
| Security-sensitive     | Sandbox/dev environments |
| Irreversible actions   | Pipelines with rollback  |
| Regulatory compliance  |                          |

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="default-response-structure"></a>
## 📊 Default Response Structure

```markdown
## Summary → [Brief outcome]

## Changes Made → [List of modifications]

## Verification → [How to verify]

## Next Steps → [Follow-up actions] (if applicable)
```

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="fallback-behavior"></a>
## ⏱️ Fallback Behavior

> **Location**: `config/timeout.yaml` → `timeout.fallback`

| Key / Situation  | Default / Action | Description                |
|------------------|------------------|----------------------------|
| `strategy`       | `graceful`       | Mode: graceful/strict/none |
| `cache_stale_ms` | 60000            | Max stale cache age (60s)  |
| Timeout < 5s     | `return_partial` | Return partial results     |
| Timeout > 5s     | `return_core`    | Return core principles     |
| File not found   | `return_error`   | Helpful error message      |
| Parse error      | `return_raw`     | Return raw content         |
| Network error    | `use_cache`      | Use cached content         |

**Golden Rule**: Always return something useful, never hang or crash.

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

<a id="related-documentation"></a>
## 📚 Related Documentation

- `sage.yaml` — Main config entry
- `config/` — Modular configs
- `content/frameworks/autonomy/levels.md` — 6-level autonomy
- `content/frameworks/timeout/hierarchy.md` — Timeout strategies
- `content/frameworks/design/design_axioms.md` — Design axioms (SSOT)
- `content/frameworks/cognitive/expert_committee.md` — Decision framework
- `docs/design/04-timeout-loading.md` — Timeout design
- `docs/design/05-plugin-memory.md` — Plugin/memory architecture
- `docs/design/09-configuration.md` — Configuration system

<p align="right"><sub><a href="#toc">📑 ↑ TOC</a></sub></p>

---

*Config: `sage.yaml` (entry) + `config/*.yaml` (modules)*
