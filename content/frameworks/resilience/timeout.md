# Timeout Hierarchy Framework

> **Load Priority**: On-demand  
> **Purpose**: Guarantee response times, prevent hangs, graceful degradation  
> **Principle**: Always return something, never hang

---

## ⏱️ 5-Level Hierarchy

| Level | Timeout | Source | Use Case | Fallback |
|-------|---------|--------|----------|----------|
| **L0** Cache | 100ms | Memory | Hot paths | → L1 |
| **L1** File | 500ms | Local disk | Single file, config | → L2 |
| **L2** Layer | 2s | Multi-file | Chapter, framework | → L3 |
| **L3** Full | 5s | Complete KB | Full search | → L4 |
| **L4** Emergency | 10s | Degraded | System stress | → L∞ |
| **L∞** Embedded | 0ms | Compiled | Hard fallback | Always succeeds |

**Flow**: Cache → File → Layer → Full → Emergency → Embedded

---

## ⚙️ Configuration

> **Source**: `config/timeout.yaml`

### Operations

| Operation | Timeout | Operation | Timeout |
|-----------|---------|-----------|---------|
| cache_lookup | 100ms | analysis | 10s |
| file_read | 500ms | mcp_call | 10s |
| layer_load | 2s | search | 3s |
| full_load | 5s | global_max | 10s |

**Dynamic**: Adjusts for `is_remote` (network) · `system_load > 0.8` (stress) · Capped at `max_timeout_ms`

---

## 🔌 Circuit Breaker

**States**: CLOSED → (failures ≥ threshold) → OPEN → (reset expires) → HALF_OPEN → (test passes) → CLOSED

| Setting | Default | Setting | Default |
|---------|---------|---------|---------|
| enabled | true | failure_threshold | 3 |
| reset_timeout | 30s | half_open_requests | 1 |

---

## 🛡️ Fallback Strategy

> **Source**: `config/timeout.yaml` → `timeout.fallback`

**Strategy**: graceful (graceful/strict/none) · **Cache Stale**: 60s

| Situation | Action | Level Failed | Response |
|-----------|--------|--------------|----------|
| Timeout < 5s | return_partial | Cache miss | Load from file |
| Timeout > 5s | return_core | File timeout | Cached subset |
| File not found | return_error | Layer timeout | Core only |
| Parse error | return_raw | Full timeout | Index + error |
| Network error | use_cache | Emergency | Embedded fallback |

---

## 📊 Monitoring

**Metrics**: timeout_count_by_level · fallback_trigger_count · avg_response_time · cache_hit_rate · emergency_rate

| Metric | Warning | Critical |
|--------|---------|----------|
| L2+ timeouts | >5% | >15% |
| Emergency fallbacks | >1% | >5% |
| Cache hit rate | <80% | <60% |
| Avg response time | >1s | >3s |

---

## 💡 Best Practices

**Do** ✅: Fallback at each level · Log timeouts · Cache hot paths · Return partial over nothing · Include completeness metadata

**Don't** ❌: Unbounded operations · Fail silently · Empty without explanation · Retry infinitely · Block on slow ops

---

**Golden Rule**: Always return something, never hang.

*Part of AI Collaboration Knowledge Base*
