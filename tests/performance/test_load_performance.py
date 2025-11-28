"""Load performance benchmark tests.

This module measures the performance of knowledge loading operations
including cold start, warm cache, and concurrent loading scenarios.

Version: 0.1.0
"""

import asyncio
import statistics
import time
from pathlib import Path
from typing import NamedTuple

import pytest

from sage.core.loader import KnowledgeLoader, Layer


class LoadBenchmark(NamedTuple):
    """Result of a load benchmark."""

    operation: str
    iterations: int
    min_ms: float
    max_ms: float
    mean_ms: float
    median_ms: float
    std_dev_ms: float


def run_sync_benchmark(func, iterations: int = 10) -> LoadBenchmark:
    """Run a synchronous benchmark multiple times."""
    times = []
    operation_name = func.__name__

    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms

    return LoadBenchmark(
        operation=operation_name,
        iterations=iterations,
        min_ms=min(times),
        max_ms=max(times),
        mean_ms=statistics.mean(times),
        median_ms=statistics.median(times),
        std_dev_ms=statistics.stdev(times) if len(times) > 1 else 0,
    )


async def run_async_benchmark(coro_func, iterations: int = 10) -> LoadBenchmark:
    """Run an async benchmark multiple times."""
    times = []
    operation_name = coro_func.__name__

    for _ in range(iterations):
        start = time.perf_counter()
        await coro_func()
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return LoadBenchmark(
        operation=operation_name,
        iterations=iterations,
        min_ms=min(times),
        max_ms=max(times),
        mean_ms=statistics.mean(times),
        median_ms=statistics.median(times),
        std_dev_ms=statistics.stdev(times) if len(times) > 1 else 0,
    )


def print_benchmark(result: LoadBenchmark) -> None:
    """Print benchmark result in a readable format."""
    print(f"\n{'=' * 50}")
    print(f"Benchmark: {result.operation}")
    print(f"{'=' * 50}")
    print(f"  Iterations: {result.iterations}")
    print(f"  Min:        {result.min_ms:.2f} ms")
    print(f"  Max:        {result.max_ms:.2f} ms")
    print(f"  Mean:       {result.mean_ms:.2f} ms")
    print(f"  Median:     {result.median_ms:.2f} ms")
    print(f"  Std Dev:    {result.std_dev_ms:.2f} ms")


class TestLoadPerformance:
    """Performance benchmarks for knowledge loading."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with test content."""
        # Create test content structure
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)
        (core_dir / "principles.md").write_text("# Principles\nTest content " * 100)
        (core_dir / "defaults.md").write_text("# Defaults\nTest defaults " * 100)

        guidelines_dir = tmp_path / "content" / "guidelines"
        guidelines_dir.mkdir(parents=True)
        (guidelines_dir / "python.md").write_text("# Python\nPython guide " * 100)
        (guidelines_dir / "quality.md").write_text("# Quality\nQuality guide " * 100)

        return KnowledgeLoader(kb_path=tmp_path)

    def test_loader_initialization_performance(self, tmp_path: Path) -> None:
        """Benchmark loader initialization time."""

        def init_loader():
            return KnowledgeLoader(kb_path=tmp_path)

        result = run_sync_benchmark(init_loader, iterations=20)
        print_benchmark(result)

        # Initialization should be fast (< 50ms)
        assert result.mean_ms < 50, f"Init too slow: {result.mean_ms:.2f}ms"

    @pytest.mark.asyncio
    async def test_cold_load_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark cold load (no cache) performance."""

        async def cold_load():
            loader.clear_cache()
            return await loader.load_core()

        result = await run_async_benchmark(cold_load, iterations=10)
        print_benchmark(result)

        # Cold load should complete within timeout T3 (2000ms)
        assert result.mean_ms < 2000, f"Cold load too slow: {result.mean_ms:.2f}ms"

    @pytest.mark.asyncio
    async def test_warm_cache_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark warm cache performance."""
        # Prime the cache
        await loader.load_core()

        async def warm_load():
            return await loader.load_core()

        result = await run_async_benchmark(warm_load, iterations=20)
        print_benchmark(result)

        # Cached load should be very fast (< 100ms, ideally < 10ms)
        assert result.mean_ms < 100, f"Cached load too slow: {result.mean_ms:.2f}ms"

    @pytest.mark.asyncio
    async def test_cache_speedup_ratio(self, loader: KnowledgeLoader) -> None:
        """Verify that caching provides significant speedup."""
        # Cold load
        loader.clear_cache()
        cold_start = time.perf_counter()
        await loader.load_core()
        cold_time = (time.perf_counter() - cold_start) * 1000

        # Warm load
        warm_start = time.perf_counter()
        await loader.load_core()
        warm_time = (time.perf_counter() - warm_start) * 1000

        speedup = cold_time / warm_time if warm_time > 0 else float("inf")
        print("\nCache Speedup Analysis:")
        print(f"  Cold load: {cold_time:.2f}ms")
        print(f"  Warm load: {warm_time:.2f}ms")
        print(f"  Speedup:   {speedup:.1f}x")

        # Cache should provide at least 2x speedup
        assert speedup >= 2.0, f"Cache speedup insufficient: {speedup:.1f}x"

    @pytest.mark.asyncio
    async def test_layer_load_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark loading different layers."""
        layers = [Layer.L1_CORE, Layer.L2_GUIDELINES]
        results = []

        for layer in layers:

            async def load_layer(l=layer):
                loader.clear_cache()
                return await loader.load(layer=l)

            result = await run_async_benchmark(load_layer, iterations=5)
            results.append((layer.name, result))
            print_benchmark(result)

        # All layers should load within T3 timeout (2000ms)
        for layer_name, result in results:
            assert result.mean_ms < 2000, (
                f"{layer_name} load too slow: {result.mean_ms:.2f}ms"
            )

    @pytest.mark.asyncio
    async def test_concurrent_load_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark concurrent loading operations."""
        loader.clear_cache()

        async def concurrent_loads():
            tasks = [
                loader.load_core(),
                loader.load_guidelines("python"),
                loader.load(layer=Layer.L2_GUIDELINES),
            ]
            return await asyncio.gather(*tasks)

        result = await run_async_benchmark(concurrent_loads, iterations=5)
        print_benchmark(result)

        # Concurrent loads should complete within T4 timeout (5000ms)
        assert result.mean_ms < 5000, (
            f"Concurrent loads too slow: {result.mean_ms:.2f}ms"
        )

    def test_cache_stats_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark cache statistics retrieval."""

        def get_stats():
            return loader.get_cache_stats()

        result = run_sync_benchmark(get_stats, iterations=100)
        print_benchmark(result)

        # Stats retrieval should be instant (< 5ms)
        assert result.mean_ms < 5, f"Stats too slow: {result.mean_ms:.2f}ms"


class TestMemoryPerformance:
    """Memory usage performance tests."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with larger test content."""
        # Create larger test content
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)

        # Create files with substantial content
        for i in range(5):
            (core_dir / f"file_{i}.md").write_text(f"# File {i}\n" + "Content " * 500)

        return KnowledgeLoader(kb_path=tmp_path)

    @pytest.mark.asyncio
    async def test_memory_efficiency(self, loader: KnowledgeLoader) -> None:
        """Test that repeated loads don't leak memory."""
        import gc

        # Force garbage collection
        gc.collect()

        # Load multiple times
        for _ in range(10):
            loader.clear_cache()
            await loader.load_core()

        # Get cache stats
        stats = loader.get_cache_stats()
        print("\nCache Stats after 10 loads:")
        print(f"  Entries: {stats.get('entries', 'N/A')}")
        print(f"  Hits: {stats.get('hits', 'N/A')}")
        print(f"  Misses: {stats.get('misses', 'N/A')}")

        # Cache shouldn't grow unbounded
        assert stats.get("entries", 0) <= 100, "Cache too large"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
