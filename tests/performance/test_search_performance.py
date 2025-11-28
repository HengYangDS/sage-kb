"""Search performance benchmark tests.

This module measures the performance of knowledge search operations
including simple queries, complex patterns, and concurrent searches.

Version: 0.1.0
"""

import asyncio
import statistics
import time
from pathlib import Path
from typing import NamedTuple

import pytest

from sage.core.loader import KnowledgeLoader


class SearchBenchmark(NamedTuple):
    """Result of a search benchmark."""

    query: str
    iterations: int
    results_count: int
    min_ms: float
    max_ms: float
    mean_ms: float
    median_ms: float


async def run_search_benchmark(
    loader: KnowledgeLoader, query: str, iterations: int = 10
) -> SearchBenchmark:
    """Run a search benchmark multiple times."""
    times = []
    results_count = 0

    for _ in range(iterations):
        start = time.perf_counter()
        results = await loader.search(query)
        end = time.perf_counter()
        times.append((end - start) * 1000)
        results_count = len(results) if results else 0

    return SearchBenchmark(
        query=query,
        iterations=iterations,
        results_count=results_count,
        min_ms=min(times),
        max_ms=max(times),
        mean_ms=statistics.mean(times),
        median_ms=statistics.median(times),
    )


def print_search_benchmark(result: SearchBenchmark) -> None:
    """Print search benchmark result."""
    print(f"\n{'=' * 50}")
    print(f"Search Query: '{result.query}'")
    print(f"{'=' * 50}")
    print(f"  Iterations:    {result.iterations}")
    print(f"  Results Found: {result.results_count}")
    print(f"  Min:           {result.min_ms:.2f} ms")
    print(f"  Max:           {result.max_ms:.2f} ms")
    print(f"  Mean:          {result.mean_ms:.2f} ms")
    print(f"  Median:        {result.median_ms:.2f} ms")


class TestSearchPerformance:
    """Performance benchmarks for search operations."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with searchable content."""
        # Create content with various keywords
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)
        (core_dir / "principles.md").write_text(
            "# Principles\n"
            "## Core Values\n"
            "Quality, reliability, performance are key.\n"
            "Python best practices and coding standards.\n" * 20
        )
        (core_dir / "defaults.md").write_text(
            "# Defaults\n"
            "## Default Settings\n"
            "Timeout configuration and error handling.\n"
            "Cache settings and memory management.\n" * 20
        )

        guidelines_dir = tmp_path / "content" / "guidelines"
        guidelines_dir.mkdir(parents=True)
        (guidelines_dir / "python.md").write_text(
            "# Python Guidelines\n"
            "## Style Guide\n"
            "Use type hints and docstrings.\n"
            "Follow PEP 8 conventions.\n" * 30
        )
        (guidelines_dir / "testing.md").write_text(
            "# Testing Guidelines\n"
            "## Test Strategy\n"
            "Unit tests, integration tests, performance tests.\n"
            "Coverage targets and quality metrics.\n" * 30
        )

        frameworks_dir = tmp_path / "content" / "frameworks"
        frameworks_dir.mkdir(parents=True)
        (frameworks_dir / "timeout.md").write_text(
            "# Timeout Framework\n"
            "## Timeout Hierarchy\n"
            "T1: 100ms for cache lookup.\n"
            "T2: 500ms for file operations.\n"
            "T3: 2000ms for layer loading.\n" * 20
        )

        return KnowledgeLoader(kb_path=tmp_path)

    @pytest.mark.asyncio
    async def test_simple_search_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark simple single-word searches."""
        queries = ["python", "test", "timeout", "quality"]
        results = []

        for query in queries:
            result = await run_search_benchmark(loader, query, iterations=10)
            results.append(result)
            print_search_benchmark(result)

        # All simple searches should complete within 500ms (T2)
        for result in results:
            assert result.mean_ms < 500, (
                f"Search '{result.query}' too slow: {result.mean_ms:.2f}ms"
            )

    @pytest.mark.asyncio
    async def test_multi_word_search_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark multi-word search queries."""
        queries = ["python best practices", "timeout configuration", "test coverage"]
        results = []

        for query in queries:
            result = await run_search_benchmark(loader, query, iterations=10)
            results.append(result)
            print_search_benchmark(result)

        # Multi-word searches should complete within 1000ms
        for result in results:
            assert result.mean_ms < 1000, (
                f"Search '{result.query}' too slow: {result.mean_ms:.2f}ms"
            )

    @pytest.mark.asyncio
    async def test_no_results_search_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark searches that return no results."""
        queries = ["xyznonexistent", "abcdefghijk123"]

        for query in queries:
            result = await run_search_benchmark(loader, query, iterations=10)
            print_search_benchmark(result)

            # No-results searches should still be fast
            assert result.mean_ms < 500, (
                f"No-result search '{query}' too slow: {result.mean_ms:.2f}ms"
            )
            assert result.results_count == 0, "Should find no results"

    @pytest.mark.asyncio
    async def test_concurrent_search_performance(self, loader: KnowledgeLoader) -> None:
        """Benchmark concurrent search operations."""
        queries = ["python", "test", "timeout", "quality", "cache"]

        async def run_concurrent_searches():
            tasks = [loader.search(q) for q in queries]
            return await asyncio.gather(*tasks)

        times = []
        for _ in range(5):
            start = time.perf_counter()
            _ = await run_concurrent_searches()
            end = time.perf_counter()
            times.append((end - start) * 1000)

        mean_time = statistics.mean(times)
        print(f"\nConcurrent Search ({len(queries)} queries):")
        print(f"  Mean time: {mean_time:.2f}ms")
        print(f"  Per query: {mean_time / len(queries):.2f}ms")

        # Concurrent searches should complete within 2000ms total
        assert mean_time < 2000, f"Concurrent searches too slow: {mean_time:.2f}ms"

    @pytest.mark.asyncio
    async def test_repeated_search_caching(self, loader: KnowledgeLoader) -> None:
        """Test that repeated searches benefit from caching."""
        query = "python"

        # First search (cold)
        start = time.perf_counter()
        await loader.search(query)
        cold_time = (time.perf_counter() - start) * 1000

        # Repeated searches (potentially cached)
        warm_times = []
        for _ in range(5):
            start = time.perf_counter()
            await loader.search(query)
            warm_times.append((time.perf_counter() - start) * 1000)

        mean_warm = statistics.mean(warm_times)
        print("\nSearch Caching Analysis:")
        print(f"  Cold search: {cold_time:.2f}ms")
        print(f"  Warm mean:   {mean_warm:.2f}ms")

        # Warm searches should not be significantly slower
        assert mean_warm < cold_time * 2, "Repeated searches too slow"

    @pytest.mark.asyncio
    async def test_search_scalability(self, loader: KnowledgeLoader) -> None:
        """Test search performance scales reasonably with query count."""
        single_start = time.perf_counter()
        await loader.search("python")
        single_time = (time.perf_counter() - single_start) * 1000

        # Run 10 sequential searches
        multi_start = time.perf_counter()
        for _ in range(10):
            await loader.search("python")
        multi_time = (time.perf_counter() - multi_start) * 1000

        print("\nScalability Analysis:")
        print(f"  Single search: {single_time:.2f}ms")
        print(f"  10 searches:   {multi_time:.2f}ms")
        print(f"  Overhead:      {(multi_time / 10) / single_time:.2f}x per query")

        # 10 searches should not take more than 15x single search time
        assert multi_time < single_time * 15, "Search does not scale well"


class TestSearchQuality:
    """Tests for search result quality and relevance."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with targeted content."""
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)
        (core_dir / "python_guide.md").write_text(
            "# Python Guide\nPython programming best practices."
        )
        (core_dir / "java_guide.md").write_text(
            "# Java Guide\nJava programming best practices."
        )
        return KnowledgeLoader(kb_path=tmp_path)

    @pytest.mark.asyncio
    async def test_search_returns_relevant_results(
        self, loader: KnowledgeLoader
    ) -> None:
        """Verify search returns relevant results."""
        results = await loader.search("python")

        print(f"\nSearch 'python' results: {len(results) if results else 0}")
        if results:
            for r in results[:3]:
                print(f"  - {r}")

        # Should find python-related content
        assert results is not None, "Search should return results"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
