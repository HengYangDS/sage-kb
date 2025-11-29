# Performance Tuning

> Performance optimization strategies and benchmarks for SAGE Knowledge Base

---

## Table of Contents

[1. Overview](#1-overview) · [2. Loading Performance](#2-loading-performance) · [3. Search Performance](#3-search-performance) · [4. Memory Optimization](#4-memory-optimization) · [5. Benchmarks](#5-benchmarks) · [6. Monitoring](#6-monitoring)

---

## 1. Overview

### 1.1 Performance Goals

| Metric           | Target  | Measured |
|------------------|---------|----------|
| Cold start       | < 2s    | ~1.5s    |
| Warm start       | < 500ms | ~300ms   |
| Single file load | < 100ms | ~50ms    |
| Search (cached)  | < 50ms  | ~30ms    |
| Memory baseline  | < 100MB | ~80MB    |

### 1.2 Key Principles

| Principle        | Description                       |
|------------------|-----------------------------------|
| **Lazy Loading** | Load content only when needed     |
| **Caching**      | Cache frequently accessed content |
| **Timeouts**     | Never let operations hang         |
| **Incremental**  | Process in chunks when possible   |

---

## 2. Loading Performance

### 2.1 Optimization Strategies

| Strategy             | Impact | Implementation                      |
|----------------------|--------|-------------------------------------|
| **Lazy loading**     | High   | Load on first access                |
| **Preloading core**  | Medium | Load core layer at startup          |
| **Parallel loading** | Medium | `asyncio.gather` for multiple files |
| **Caching**          | High   | LRU cache for loaded content        |

### 2.2 Implementation

```python
# Lazy loading with caching
from functools import lru_cache
import asyncio


class ContentLoader:
    def __init__(self):
        self._cache = {}
        self._loading = {}

    async def load(self, path: str) -> str:
        # Return cached
        if path in self._cache:
            return self._cache[path]

        # Await if already loading
        if path in self._loading:
            return await self._loading[path]

        # Start loading
        self._loading[path] = asyncio.create_task(self._load_file(path))
        content = await self._loading[path]

        self._cache[path] = content
        del self._loading[path]

        return content

    async def preload(self, paths: list[str]) -> None:
        """Preload multiple files in parallel."""
        await asyncio.gather(*[self.load(p) for p in paths])
```

### 2.3 Startup Optimization

```python
# Optimized startup sequence
async def startup():
    # 1. Load config (sync, fast)
    config = load_config()

    # 2. Initialize components (no I/O)
    loader = ContentLoader(config)

    # 3. Preload core in background
    asyncio.create_task(loader.preload(CORE_FILES))

    # 4. Return immediately (core loads in background)
    return loader
```

---

## 3. Search Performance

### 3.1 Search Optimization

| Technique             | Use Case         | Speedup |
|-----------------------|------------------|---------|
| **Index**             | Full-text search | 10-100x |
| **Caching**           | Repeated queries | 100x+   |
| **Early termination** | Top-N results    | 2-5x    |
| **Parallel search**   | Multiple layers  | 2-4x    |

### 3.2 Search Implementation

```python
class SearchEngine:
    def __init__(self):
        self._index = {}
        self._cache = LRUCache(maxsize=100)

    def search(self, query: str, limit: int = 10) -> list[Result]:
        # Check cache
        cache_key = f"{query}:{limit}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        # Search with early termination
        results = []
        for doc_id, content in self._index.items():
            if query.lower() in content.lower():
                results.append(Result(doc_id, content))
                if len(results) >= limit:
                    break

        self._cache[cache_key] = results
        return results

    def invalidate_cache(self):
        self._cache.clear()
```

### 3.3 Index Building

```python
# Build search index asynchronously
async def build_index(content_dir: Path) -> dict[str, str]:
    index = {}

    async def index_file(path: Path):
        content = await aiofiles.open(path).read()
        return str(path), content

    tasks = [index_file(f) for f in content_dir.rglob("*.md")]
    results = await asyncio.gather(*tasks)

    for path, content in results:
        index[path] = content

    return index
```

---

## 4. Memory Optimization

### 4.1 Memory Management

| Strategy             | Description         | Savings  |
|----------------------|---------------------|----------|
| **LRU eviction**     | Remove least used   | 30-50%   |
| **Lazy parsing**     | Parse on access     | 20-30%   |
| **String interning** | Deduplicate strings | 10-20%   |
| **Weak references**  | For caches          | Variable |

### 4.2 Token Budget Management

```python
class TokenBudgetManager:
    def __init__(self, total_budget: int = 8000):
        self.total = total_budget
        self.used = 0
        self._allocations = {}

    def allocate(self, key: str, tokens: int) -> bool:
        """Try to allocate tokens."""
        if self.used + tokens > self.total:
            return False

        self._allocations[key] = tokens
        self.used += tokens
        return True

    def release(self, key: str) -> None:
        """Release allocated tokens."""
        if key in self._allocations:
            self.used -= self._allocations[key]
            del self._allocations[key]

    def remaining(self) -> int:
        return self.total - self.used
```

### 4.3 Content Compression

```python
# Compress large content in memory
import zlib


class CompressedCache:
    def __init__(self, threshold: int = 10000):
        self._cache = {}
        self._threshold = threshold

    def set(self, key: str, value: str) -> None:
        if len(value) > self._threshold:
            compressed = zlib.compress(value.encode())
            self._cache[key] = (True, compressed)
        else:
            self._cache[key] = (False, value)

    def get(self, key: str) -> str | None:
        if key not in self._cache:
            return None

        is_compressed, data = self._cache[key]
        if is_compressed:
            return zlib.decompress(data).decode()
        return data
```

---

## 5. Benchmarks

### 5.1 Current Benchmarks

| Operation          | P50   | P95   | P99   |
|--------------------|-------|-------|-------|
| Load core layer    | 150ms | 200ms | 250ms |
| Load single file   | 30ms  | 50ms  | 80ms  |
| Search (indexed)   | 5ms   | 15ms  | 30ms  |
| Search (full scan) | 50ms  | 100ms | 200ms |
| Token counting     | 1ms   | 3ms   | 5ms   |

### 5.2 Running Benchmarks

```bash
# Run performance tests
pytest tests/performance/ -v

# Run specific benchmark
pytest tests/performance/test_load_performance.py -v

# Profile specific operation
python -m cProfile -s cumulative -m pytest tests/performance/
```

### 5.3 Benchmark Code

```python
# tests/performance/test_load_performance.py
import pytest
import time


class TestLoadPerformance:
    @pytest.mark.benchmark
    def test_cold_start(self, benchmark):
        def cold_start():
            loader = ContentLoader()
            return loader.load_layer("core")

        result = benchmark(cold_start)
        assert result is not None

    @pytest.mark.benchmark
    def test_warm_load(self, loader_with_cache, benchmark):
        def warm_load():
            return loader_with_cache.load_layer("core")

        result = benchmark(warm_load)
        assert result is not None
```

---

## 6. Monitoring

### 6.1 Key Metrics

| Metric            | Description            | Alert Threshold |
|-------------------|------------------------|-----------------|
| `load_time_ms`    | Time to load content   | > 2000ms        |
| `search_time_ms`  | Time to execute search | > 500ms         |
| `memory_mb`       | Memory usage           | > 200MB         |
| `cache_hit_ratio` | Cache effectiveness    | < 0.7           |
| `timeout_count`   | Timeout occurrences    | > 10/min        |

### 6.2 Instrumentation

```python
import time
from contextlib import contextmanager
import structlog

log = structlog.get_logger()


@contextmanager
def measure_time(operation: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        log.info(
            "operation_complete",
            operation=operation,
            duration_ms=round(duration_ms, 2)
        )
```

### 6.3 Health Metrics

```python
class PerformanceMetrics:
    def __init__(self):
        self.load_times = []
        self.search_times = []
        self.cache_hits = 0
        self.cache_misses = 0

    def record_load(self, duration_ms: float):
        self.load_times.append(duration_ms)

    def record_search(self, duration_ms: float):
        self.search_times.append(duration_ms)

    def record_cache_hit(self):
        self.cache_hits += 1

    def record_cache_miss(self):
        self.cache_misses += 1

    @property
    def cache_hit_ratio(self) -> float:
        total = self.cache_hits + self.cache_misses
        return self.cache_hits / total if total > 0 else 0.0

    def get_summary(self) -> dict:
        return {
            "avg_load_ms"    : sum(self.load_times) / len(self.load_times) if self.load_times else 0,
            "avg_search_ms"  : sum(self.search_times) / len(self.search_times) if self.search_times else 0,
            "cache_hit_ratio": self.cache_hit_ratio,
        }
```

---

## Tuning Checklist

| Area        | Check                            | Status |
|-------------|----------------------------------|--------|
| **Loading** | ☐ Lazy loading enabled           |        |
|             | ☐ Core preloading configured     |        |
|             | ☐ Parallel loading for batch ops |        |
| **Caching** | ☐ LRU cache configured           |        |
|             | ☐ Cache size appropriate         |        |
|             | ☐ Cache invalidation working     |        |
| **Search**  | ☐ Index built                    |        |
|             | ☐ Query caching enabled          |        |
|             | ☐ Result limits set              |        |
| **Memory**  | ☐ Token budget configured        |        |
|             | ☐ Eviction policy set            |        |
|             | ☐ Memory monitoring active       |        |

---

## Related

- `.context/policies/timeout_hierarchy.md` — Timeout settings
- `tests/performance/` — Performance test suite
- `config/core/memory.yaml` — Memory configuration

---

*Last updated: 2025-11-29*
*Part of SAGE Knowledge Base*
