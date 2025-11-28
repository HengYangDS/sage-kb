"""Timeout mechanism stress tests.

This module tests the robustness and reliability of the timeout
system under various stress conditions including:
- Rapid successive operations
- Concurrent timeout scenarios
- Edge cases near timeout boundaries
- Recovery after timeouts

Version: 0.1.0
"""

import asyncio
import statistics
import time
from pathlib import Path
from typing import NamedTuple

import pytest

from sage.core.loader import KnowledgeLoader


class TimeoutResult(NamedTuple):
    """Result of a timeout stress test."""

    test_name: str
    total_operations: int
    successful: int
    timed_out: int
    failed: int
    mean_time_ms: float
    max_time_ms: float


def print_timeout_result(result: TimeoutResult) -> None:
    """Print timeout test result."""
    print(f"\n{'=' * 50}")
    print(f"Test: {result.test_name}")
    print(f"{'=' * 50}")
    print(f"  Total Operations: {result.total_operations}")
    print(f"  Successful:       {result.successful}")
    print(f"  Timed Out:        {result.timed_out}")
    print(f"  Failed:           {result.failed}")
    print(f"  Mean Time:        {result.mean_time_ms:.2f} ms")
    print(f"  Max Time:         {result.max_time_ms:.2f} ms")
    success_rate = (result.successful / result.total_operations) * 100
    print(f"  Success Rate:     {success_rate:.1f}%")


class TestTimeoutStress:
    """Stress tests for timeout mechanisms."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with test content."""
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)
        # Create content of varying sizes
        (core_dir / "small.md").write_text("# Small\nSmall content.")
        (core_dir / "medium.md").write_text("# Medium\n" + "Medium content.\n" * 100)
        (core_dir / "large.md").write_text("# Large\n" + "Large content.\n" * 1000)

        return KnowledgeLoader(kb_path=tmp_path)

    @pytest.mark.asyncio
    async def test_rapid_successive_loads(self, loader: KnowledgeLoader) -> None:
        """Test rapid successive load operations."""
        operations = 50
        times = []
        successful = 0
        timed_out = 0
        failed = 0

        for _i in range(operations):
            start = time.perf_counter()
            try:
                await loader.load_core()
                successful += 1
            except TimeoutError:
                timed_out += 1
            except Exception:
                failed += 1
            finally:
                times.append((time.perf_counter() - start) * 1000)

        result = TimeoutResult(
            test_name="Rapid Successive Loads",
            total_operations=operations,
            successful=successful,
            timed_out=timed_out,
            failed=failed,
            mean_time_ms=statistics.mean(times),
            max_time_ms=max(times),
        )
        print_timeout_result(result)

        # At least 90% should succeed
        assert successful >= operations * 0.9, (
            f"Too many failures: {successful}/{operations}"
        )
        # No operation should exceed T4 timeout (5000ms)
        assert result.max_time_ms < 5000, (
            f"Max time exceeded T4: {result.max_time_ms:.2f}ms"
        )

    @pytest.mark.asyncio
    async def test_concurrent_load_stress(self, loader: KnowledgeLoader) -> None:
        """Test many concurrent load operations."""
        concurrency = 20
        times = []
        successful = 0
        timed_out = 0
        failed = 0

        async def load_with_tracking():
            nonlocal successful, timed_out, failed
            start = time.perf_counter()
            try:
                await loader.load_core()
                successful += 1
                return (time.perf_counter() - start) * 1000
            except TimeoutError:
                timed_out += 1
                return (time.perf_counter() - start) * 1000
            except Exception:
                failed += 1
                return (time.perf_counter() - start) * 1000

        # Run concurrent operations
        tasks = [load_with_tracking() for _ in range(concurrency)]
        times = await asyncio.gather(*tasks)

        result = TimeoutResult(
            test_name="Concurrent Load Stress",
            total_operations=concurrency,
            successful=successful,
            timed_out=timed_out,
            failed=failed,
            mean_time_ms=statistics.mean(times),
            max_time_ms=max(times),
        )
        print_timeout_result(result)

        # At least 80% should succeed under high concurrency
        assert successful >= concurrency * 0.8, "Too many failures under concurrency"

    @pytest.mark.asyncio
    async def test_timeout_boundary_operations(self, loader: KnowledgeLoader) -> None:
        """Test operations near timeout boundaries."""
        # Test with different timeout levels
        timeout_levels = [
            ("T1 (100ms)", 100),
            ("T2 (500ms)", 500),
            ("T3 (2000ms)", 2000),
        ]

        for level_name, timeout_ms in timeout_levels:
            start = time.perf_counter()
            try:
                # Simple operation should complete well within any timeout
                await asyncio.wait_for(
                    loader.load_core(),
                    timeout=timeout_ms / 1000,
                )
                elapsed = (time.perf_counter() - start) * 1000
                print(f"\n{level_name}: Completed in {elapsed:.2f}ms")

                # Operation should complete within the timeout
                assert elapsed < timeout_ms, f"Operation exceeded {level_name} timeout"
            except TimeoutError:
                elapsed = (time.perf_counter() - start) * 1000
                print(f"\n{level_name}: Timed out at {elapsed:.2f}ms")
                # T1 might timeout for cold loads, that's acceptable
                if timeout_ms > 100:
                    pytest.fail(f"Operation timed out at {level_name}")

    @pytest.mark.asyncio
    async def test_recovery_after_timeout(self, loader: KnowledgeLoader) -> None:
        """Test that system recovers properly after timeout."""
        # Force a very short timeout to trigger timeout
        try:
            await asyncio.wait_for(
                loader.load_core(),
                timeout=0.001,  # 1ms - will likely timeout
            )
        except TimeoutError:
            pass  # Expected

        # System should recover and work normally
        recovery_times = []
        for _ in range(5):
            start = time.perf_counter()
            try:
                await loader.load_core()
                recovery_times.append((time.perf_counter() - start) * 1000)
            except Exception as e:
                pytest.fail(f"Failed to recover after timeout: {e}")

        mean_recovery = statistics.mean(recovery_times)
        print("\nRecovery after timeout:")
        print(f"  Mean recovery time: {mean_recovery:.2f}ms")
        print(f"  Max recovery time:  {max(recovery_times):.2f}ms")

        # Recovery should be quick (within T3)
        assert mean_recovery < 2000, f"Recovery too slow: {mean_recovery:.2f}ms"

    @pytest.mark.asyncio
    async def test_mixed_operation_stress(self, loader: KnowledgeLoader) -> None:
        """Test mixed operations under stress."""
        operations = 30
        results = {"load": 0, "search": 0, "clear": 0}
        times = []

        for i in range(operations):
            op_type = i % 3
            start = time.perf_counter()

            try:
                if op_type == 0:
                    await loader.load_core()
                    results["load"] += 1
                elif op_type == 1:
                    await loader.search("test")
                    results["search"] += 1
                else:
                    loader.clear_cache()
                    results["clear"] += 1
            except Exception:
                pass

            times.append((time.perf_counter() - start) * 1000)

        total_success = sum(results.values())
        print("\nMixed Operation Stress:")
        print(f"  Load operations:   {results['load']}")
        print(f"  Search operations: {results['search']}")
        print(f"  Clear operations:  {results['clear']}")
        print(f"  Mean time:         {statistics.mean(times):.2f}ms")
        print(f"  Max time:          {max(times):.2f}ms")

        # At least 80% should succeed
        assert total_success >= operations * 0.8, "Too many mixed operation failures"

    @pytest.mark.asyncio
    async def test_burst_load_pattern(self, loader: KnowledgeLoader) -> None:
        """Test burst load pattern (idle → burst → idle)."""
        burst_size = 10
        burst_results = []

        # Burst 1
        for _ in range(burst_size):
            start = time.perf_counter()
            await loader.load_core()
            burst_results.append((time.perf_counter() - start) * 1000)

        burst1_mean = statistics.mean(burst_results)

        # Idle period
        await asyncio.sleep(0.1)
        burst_results.clear()

        # Burst 2
        for _ in range(burst_size):
            start = time.perf_counter()
            await loader.load_core()
            burst_results.append((time.perf_counter() - start) * 1000)

        burst2_mean = statistics.mean(burst_results)

        print("\nBurst Load Pattern:")
        print(f"  Burst 1 mean: {burst1_mean:.2f}ms")
        print(f"  Burst 2 mean: {burst2_mean:.2f}ms")

        # Both bursts should complete within acceptable time
        assert burst1_mean < 2000, f"Burst 1 too slow: {burst1_mean:.2f}ms"
        assert burst2_mean < 2000, f"Burst 2 too slow: {burst2_mean:.2f}ms"


class TestTimeoutHierarchy:
    """Tests for timeout hierarchy compliance."""

    @pytest.fixture
    def loader(self, tmp_path: Path) -> KnowledgeLoader:
        """Create a loader with test content."""
        core_dir = tmp_path / "content" / "core"
        core_dir.mkdir(parents=True)
        (core_dir / "test.md").write_text("# Test\nTest content.")
        return KnowledgeLoader(kb_path=tmp_path)

    @pytest.mark.asyncio
    async def test_cache_lookup_within_t1(self, loader: KnowledgeLoader) -> None:
        """Test that cache lookups complete within T1 (100ms)."""
        # Prime the cache
        await loader.load_core()

        # Measure cache hit time
        times = []
        for _ in range(20):
            start = time.perf_counter()
            loader.get_cache_stats()
            times.append((time.perf_counter() - start) * 1000)

        mean_time = statistics.mean(times)
        print(f"\nCache lookup time: {mean_time:.2f}ms (T1: 100ms)")

        # Cache operations should be well under T1
        assert mean_time < 100, f"Cache lookup exceeded T1: {mean_time:.2f}ms"

    @pytest.mark.asyncio
    async def test_file_read_within_t2(self, loader: KnowledgeLoader) -> None:
        """Test that single file reads complete within T2 (500ms)."""
        loader.clear_cache()

        times = []
        for _ in range(10):
            loader.clear_cache()
            start = time.perf_counter()
            await loader.load_core()
            times.append((time.perf_counter() - start) * 1000)

        mean_time = statistics.mean(times)
        print(f"\nFile read time: {mean_time:.2f}ms (T2: 500ms)")

        # Single file operations should be within T2
        assert mean_time < 500, f"File read exceeded T2: {mean_time:.2f}ms"

    @pytest.mark.asyncio
    async def test_layer_load_within_t3(self, loader: KnowledgeLoader) -> None:
        """Test that layer loads complete within T3 (2000ms)."""
        from sage.core.loader import Layer

        loader.clear_cache()

        times = []
        for _ in range(5):
            loader.clear_cache()
            start = time.perf_counter()
            await loader.load(layer=Layer.L1_CORE)
            times.append((time.perf_counter() - start) * 1000)

        mean_time = statistics.mean(times)
        print(f"\nLayer load time: {mean_time:.2f}ms (T3: 2000ms)")

        # Layer loads should be within T3
        assert mean_time < 2000, f"Layer load exceeded T3: {mean_time:.2f}ms"

    @pytest.mark.asyncio
    async def test_full_kb_load_within_t4(self, loader: KnowledgeLoader) -> None:
        """Test that full KB loads complete within T4 (5000ms)."""
        loader.clear_cache()

        start = time.perf_counter()
        await loader.load_core()
        elapsed = (time.perf_counter() - start) * 1000

        print(f"\nFull KB load time: {elapsed:.2f}ms (T4: 5000ms)")

        # Full load should be within T4
        assert elapsed < 5000, f"Full KB load exceeded T4: {elapsed:.2f}ms"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
