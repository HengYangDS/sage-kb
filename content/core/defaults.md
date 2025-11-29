# Default Behaviors and Calibration

> Baseline behaviors and calibration parameters (see `sage.yaml` for values)

---

## 📑 Table of Contents

| Section                                                | Description                    |
|--------------------------------------------------------|--------------------------------|
| [🎯 Default Autonomy](#default-autonomy-settings)      | Context-based autonomy levels  |
| [📋 Default Behaviors](#default-behaviors)             | Communication, code, decisions |
| [⚙️ Configuration Reference](#configuration-reference) | All config modules             |
| [🔄 Calibration Workflow](#calibration-workflow)       | Autonomy adjustment            |
| [🚨 Override Conditions](#override-conditions)         | Force different autonomy       |
| [📊 Response Structure](#default-response-structure)   | Standard format                |
| [⏱️ Fallback Behavior](#fallback-behavior)             | Timeout/error handling         |

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

---

<a id="configuration-reference"></a>

## ⚙️ Configuration Reference

> **Single Source of Truth**: `sage.yaml` (entry) + `config/*.yaml` (modules)

### Timeout → `config/timeout.yaml`

**Levels**: T1:100ms(cache) | T2:500ms(file) | T3:2s(layer) | T4:5s(full) | T5:10s(analysis)

**Other**: mcp=10s | search=3s | global_max=10s | default=5s

**Circuit Breaker**: enabled=true | threshold=3 | reset=30s | half_open=1

**On Timeout**: return_partial · use_fallback · log_warning · never_hang

### Loading → `config/loading.yaml`

**Limits**: max_tokens=4000 | default_layers=[core]

**Always Load**: `index.md` | `content/core/principles.md` | `content/core/quick_reference.md`

### Quality → `config/quality.yaml`

**Code**: coverage≥95% | func≤50lines | file≤500lines | complexity≤10

**Style**: line≤88 | type_hints≥50%

**Docs**: line≤120

### Token Budget → `config/token_budget.yaml`

**Limits**: max=128000 | reserved=4000

**Thresholds**: NORMAL<70% | WARNING=70% | CAUTION=80% | CRITICAL=90% | OVERFLOW=95%

**Auto Actions**: summarize=true | prune=true (at CRITICAL/OVERFLOW)

### Memory → `config/memory.yaml`

**Store**: backend=file | path=`.history/memory`

**Session**: auto_checkpoint=true | interval=300s | max_history=100

### Features → `config/features.yaml`

✓ event_driven_plugins | ✓ memory_persistence | ✓ lazy_expansion | ✓ client_cache

✗ api_service | ✗ differential_loading | ✗ compressed_loading | ✗ context_pruning

### Plugins → `config/plugins.yaml`

**Loader**: cache=true | ttl=300s

**Content Cache**: enabled=true | max=1000 entries | size=50MB | ttl=3600s

**Semantic Search**: enabled=true | min_term=2 | max_results=20 | threshold=0.1 | stemming=false

### Logging → `config/logging.yaml`

level=INFO | format=structured | timestamps=true

### Other Configs (on-demand)

| Config                   | Key Setting    | Details                           |
|--------------------------|----------------|-----------------------------------|
| `config/api.yaml`        | enabled=false  | API service (disabled by default) |
| `config/di.yaml`         | auto_wire=true | Dependency injection              |
| `config/guidelines.yaml` | sections       | Alias mapping                     |
| `config/triggers.yaml`   | triggers       | Keyword-based loading             |

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

**Reset Triggers**: Major errors · New domain · Team change · Extended absence

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

---

<a id="default-response-structure"></a>

## 📊 Default Response Structure

```markdown
## Summary → [Brief outcome]

## Changes Made → [List of modifications]

## Verification → [How to verify]

## Next Steps → [Follow-up actions] (if applicable)
```

---

<a id="fallback-behavior"></a>

## ⏱️ Fallback Behavior

> **Location**: `config/timeout.yaml` → `timeout.fallback`

**Strategy**: graceful (options: graceful/strict/none) | cache_stale=60s

| Situation      | Action                         |
|----------------|--------------------------------|
| Timeout < 5s   | return_partial                 |
| Timeout > 5s   | return_core                    |
| File not found | return_error (helpful message) |
| Parse error    | return_raw                     |
| Network error  | use_cache                      |

**Golden Rule**: Always return something useful, never hang or crash.

---

## 📚 Related Documentation

- `sage.yaml` — Main config entry
- `config/` — Modular configs
- `content/frameworks/autonomy/levels.md` — 6-level autonomy
- `content/frameworks/timeout/hierarchy.md` — Timeout strategies
- `content/practices/ai_collaboration/token_optimization.md` — Token efficiency
- `docs/design/04-timeout-loading.md` — Timeout design
- `docs/design/09-configuration.md` — Configuration system

---

*Part of SAGE Knowledge Base*
