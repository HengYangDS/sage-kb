# Default Behaviors and Calibration

> **Load Priority**: Always Load  
> **Purpose**: Establish baseline behaviors and calibration parameters  
> **Configuration**: See `sage.yaml` for actual values (Single Source of Truth)

---

## 🎯 Default Autonomy Settings

> **Reference**: See `content/frameworks/autonomy/levels.md` for full 6-level framework

| Context             | Default Level       | Rationale             |
|---------------------|---------------------|-----------------------|
| New project         | L2 (Low)            | Build trust gradually |
| Established project | L4 (Medium-High)    | Proven patterns       |
| Critical changes    | L1-L2 (Minimal/Low) | High stakes           |
| Routine maintenance | L4 (Medium-High)    | Low risk              |
| Documentation       | L4-L5               | Well-defined scope    |
| Refactoring         | L3-L4               | Needs verification    |

---

## 📋 Default Behaviors

### Communication

- **Verbosity**: Concise with detail on request
- **Format**: Markdown with code blocks
- **Language**: Match the user’s language (default: English)
- **Uncertainty**: State explicitly when unsure

### Code Changes

- **Scope**: Minimal necessary changes
- **Style**: Follow existing codebase conventions
- **Comments**: Match existing frequency
- **Tests**: Run affected tests when possible

### Decision-Making

- **Ambiguity**: Ask for clarification
- **Risk**: Err on the side of caution
- **Reversibility**: Prefer reversible actions
- **Documentation**: Document significant decisions

---

## ⚙️ Configuration Reference

> **Single Source of Truth**: Configuration is modularized into separate files.
> - Main entry: `sage.yaml`
> - Modular configs: `config/*.yaml`
>
> This section describes the configuration structure and purpose only.

### Timeout Configuration

> **Location**: `config/timeout.yaml` → `timeout`

| Level | Key                       | Purpose                  |
|-------|---------------------------|--------------------------|
| T1    | `operations.cache_lookup` | Cache hit operations     |
| T2    | `operations.file_read`    | Single file operations   |
| T3    | `operations.layer_load`   | Layer/directory loading  |
| T4    | `operations.full_load`    | Complete KB load         |
| T5    | `operations.analysis`     | Complex analysis         |
| -     | `operations.mcp_call`     | MCP tool timeout         |
| -     | `operations.search`       | Search operations        |
| -     | `global_max`              | Absolute maximum timeout |
| -     | `default`                 | Default if not specified |

**Additional Features** (see `config/timeout.yaml`):

- `strategies.on_timeout` - Timeout handling strategies
- `circuit_breaker` - Circuit breaker pattern configuration

### Loading Configuration

> **Location**: `config/loading.yaml` → `loading`

| Key              | Purpose                            |
|------------------|------------------------------------|
| `max_tokens`     | Maximum tokens to load per request |
| `default_layers` | Layers loaded by default           |
| `always`         | Files always pre-cached            |

### Quality Thresholds

> **Location**: `config/quality.yaml` → `quality`

| Category      | Keys                                                                          | Purpose              |
|---------------|-------------------------------------------------------------------------------|----------------------|
| Code Quality  | `min_test_coverage`, `max_function_lines`, `max_file_lines`, `max_complexity` | Code quality metrics |
| Code Style    | `max_line_length`, `min_type_hint_coverage`                                   | Style enforcement    |
| Documentation | `max_doc_line_length`                                                         | Markdown formatting  |

### Token Budget Configuration

> **Location**: `config/token_budget.yaml` → `token_budget`

| Key               | Purpose                                     |
|-------------------|---------------------------------------------|
| `max_tokens`      | Model context window size                   |
| `reserved_tokens` | Reserved for response generation            |
| `thresholds.*`    | Warning level thresholds (CAUTION→OVERFLOW) |
| `auto_actions.*`  | Automatic summarization and pruning         |

**Warning Levels** (see `config/token_budget.yaml` for thresholds):

- NORMAL: No action needed
- CAUTION: Suggest summarization
- WARNING: Recommend summarization
- CRITICAL: Auto-summarize if enabled
- OVERFLOW: Force pruning if enabled

### Memory Configuration

> **Location**: `config/memory.yaml` → `memory`

| Key                           | Purpose                             |
|-------------------------------|-------------------------------------|
| `store.backend`               | Storage backend (file/redis/sqlite) |
| `store.path`                  | Storage location for file backend   |
| `session.auto_checkpoint`     | Auto-checkpoint on critical events  |
| `session.checkpoint_interval` | Checkpoint interval in seconds      |
| `session.max_history`         | Maximum conversation entries        |

### Plugin Configuration

> **Location**: `config/plugins.yaml` → `plugins`

| Key                         | Purpose                         |
|-----------------------------|---------------------------------|
| `loader.cache_enabled`      | Enable content caching          |
| `loader.cache_ttl`          | Cache time-to-live (seconds)    |
| `bundled.content_cache.*`   | Content cache plugin settings   |
| `bundled.semantic_search.*` | Semantic search plugin settings |

### Other Configuration Sections

> **Location**: `config/` directory (modular configuration)

| Config File              | Section               | Purpose                                 |
|--------------------------|-----------------------|-----------------------------------------|
| `config/guidelines.yaml` | `guidelines.sections` | Alias mapping for guidelines            |
| `config/triggers.yaml`   | `triggers`            | Keyword-based context loading           |
| `config/logging.yaml`    | `logging`             | Logging level, format, timestamps       |
| `config/di.yaml`         | `di`                  | Dependency injection container          |
| `config/features.yaml`   | `features`            | Feature flags for optional capabilities |

---

## 🔄 Calibration Workflow

### Initial Session

1. Start at L2-L3 (Low/Medium)
2. Execute small tasks
3. Gather feedback
4. Adjust based on results

### Ongoing Calibration

```
Success Rate    Adjustment
─────────────────────────────
> 95%           +1 level (max L5)
85-95%          Maintain
70-85%          -1 level
< 70%           -2 levels, review
```

### Recalibration Triggers

- Major errors or misunderstandings
- New domain or technology
- Team or project change
- Extended absence

---

## 🚨 Override Conditions

### Force Lower Autonomy (L1-L2)

- Production deployments
- Database migrations
- Security-sensitive operations
- Irreversible actions
- Regulatory compliance

### Allow Higher Autonomy (L5-L6)

- Explicitly granted by the user
- Well-tested, routine operations
- Sandbox/development environments
- Automated pipelines with rollback

---

## 📊 Default Response Structure

```markdown
## Summary

[Brief outcome statement]

## Changes Made

[List of modifications]

## Verification

[How changes to be verified]

## Next Steps (if applicable)

[Recommended follow-up actions]
```

---

## ⏱️ Fallback Behavior

> **Location**: `config/timeout.yaml` → `timeout.fallback`

When a timeout or error occurs, the system applies configured fallback actions.

**Fallback Situations** (see `config/timeout.yaml` for configured actions):

| Situation       | Config Key       |
|-----------------|------------------|
| Timeout (short) | `timeout_short`  |
| Timeout (long)  | `timeout_long`   |
| File not found  | `file_not_found` |
| Parse error     | `parse_error`    |
| Network error   | `network_error`  |

**Golden Rule**: Always return something useful, never hang or crash.

---

## 📚 Related Documentation

| Document                                         | Purpose                         |
|--------------------------------------------------|---------------------------------|
| `sage.yaml`                                      | Main configuration entry point  |
| `config/`                                        | Modular configuration directory |
| `content/frameworks/design/design_axioms.md`     | Design axioms including SSOT    |
| `content/frameworks/autonomy/levels.md`          | 6-level autonomy framework      |
| `content/frameworks/timeout/hierarchy.md`        | Timeout strategies and recovery |
| `content/frameworks/cognitive/expert_committee.md` | Decision-making framework       |
| `docs/design/04-timeout-loading.md`              | Technical timeout design        |
| `docs/design/05-plugin-memory.md`                | Plugin and memory architecture  |

---

*Configuration is modularized: `sage.yaml` (entry point) + `config/*.yaml` (modules).*
