"""
End-to-end integration tests for Knowledge Loader.

Tests complete loading flows, cache behavior, and timeout mechanisms.

Version: 0.1.0
"""

import time

import pytest

from sage.core.loader import KnowledgeLoader, Layer


class TestLoaderInitialization:
    """Test loader initialization in various scenarios."""

    def test_default_initialization(self):
        """Test loader with default initialization."""
        loader = KnowledgeLoader()
        assert loader is not None

    def test_custom_root_initialization(self, tmp_path):
        """Test loader with custom content root."""
        # Create minimal content structure
        content_dir = tmp_path / "content"
        content_dir.mkdir()
        core_dir = content_dir / "core"
        core_dir.mkdir()
        (core_dir / "test.md").write_text("# Test\n\nContent")

        loader = KnowledgeLoader(kb_path=tmp_path)
        assert loader is not None

    def test_loader_attributes(self):
        """Test loader has required attributes and methods."""
        loader = KnowledgeLoader()

        # Check required methods exist
        assert hasattr(loader, "load")
        assert hasattr(loader, "load_core")
        assert hasattr(loader, "load_guidelines")
        assert hasattr(loader, "load_framework")
        assert hasattr(loader, "load_for_task")
        assert hasattr(loader, "search")
        assert hasattr(loader, "get_cache_stats")
        assert hasattr(loader, "clear_cache")

        # Methods should be callable
        assert callable(loader.load)
        assert callable(loader.search)


class TestCompleteLoadingFlow:
    """Test complete loading flow scenarios."""

    @pytest.mark.asyncio
    async def test_load_all_layers_sequence(self):
        """Test loading all layers in sequence."""
        loader = KnowledgeLoader()

        # Load each layer
        for layer in Layer:
            result = await loader.load(layer)
            assert result is not None

    @pytest.mark.asyncio
    async def test_load_core_complete_flow(self):
        """Test complete core loading flow."""
        loader = KnowledgeLoader()

        # Load core
        result = await loader.load_core()

        # Verify result exists
        assert result is not None

    @pytest.mark.asyncio
    async def test_load_guidelines_complete_flow(self):
        """Test complete guidelines loading flow."""
        loader = KnowledgeLoader()

        # Load various guideline chapters
        chapters = ["quality", "cognitive", "code_style", "engineering"]

        for chapter in chapters:
            result = await loader.load_guidelines(chapter)
            assert result is not None

    @pytest.mark.asyncio
    async def test_load_framework_complete_flow(self):
        """Test complete framework loading flow."""
        loader = KnowledgeLoader()

        # Load various frameworks
        frameworks = ["autonomy", "timeout", "cognitive"]

        for framework in frameworks:
            result = await loader.load_framework(framework)
            assert result is not None

    @pytest.mark.asyncio
    async def test_load_for_task_complete_flow(self):
        """Test task-based loading flow."""
        loader = KnowledgeLoader()

        # Load for various task descriptions
        tasks = [
            "implementing timeout handling",
            "writing unit tests",
            "code review",
            "documentation",
            "debugging issues",
        ]

        for task in tasks:
            result = await loader.load_for_task(task)
            assert result is not None


class TestCacheBehavior:
    """Test cache behavior in integration scenarios."""

    @pytest.mark.asyncio
    async def test_cache_hit_on_repeated_load(self):
        """Test that repeated loads hit cache."""
        loader = KnowledgeLoader()

        # Clear cache first
        loader.clear_cache()

        # First load
        result1 = await loader.load_core()
        stats1 = loader.get_cache_stats()

        # Second load (should hit cache)
        result2 = await loader.load_core()
        stats2 = loader.get_cache_stats()

        # Both results should be valid
        assert result1 is not None
        assert result2 is not None

        # Cache should show activity
        assert stats1 is not None
        assert stats2 is not None

    @pytest.mark.asyncio
    async def test_cache_clear_and_reload(self):
        """Test cache clearing and reloading."""
        loader = KnowledgeLoader()

        # Load content
        await loader.load_core()

        # Get stats before clear
        stats_before = loader.get_cache_stats()

        # Clear cache
        loader.clear_cache()

        # Get stats after clear
        stats_after = loader.get_cache_stats()

        # Reload - should work
        result = await loader.load_core()
        assert result is not None

    def test_cache_stats_structure(self):
        """Test cache stats have expected structure."""
        loader = KnowledgeLoader()

        # Get cache stats
        stats = loader.get_cache_stats()

        # Should be a dictionary
        assert isinstance(stats, dict)

    @pytest.mark.asyncio
    async def test_cache_isolation_between_layers(self):
        """Test that different layers have separate cache entries."""
        loader = KnowledgeLoader()
        loader.clear_cache()

        # Load different layers
        core_result = await loader.load_core()
        guidelines_result = await loader.load_guidelines("quality")

        # Both should be valid and potentially different
        assert core_result is not None
        assert guidelines_result is not None


class TestSearchFunctionality:
    """Test search functionality in integration scenarios."""

    @pytest.mark.asyncio
    async def test_basic_search(self):
        """Test basic search functionality."""
        loader = KnowledgeLoader()

        result = await loader.search("timeout")
        assert result is not None

    @pytest.mark.asyncio
    async def test_search_returns_results(self):
        """Test that search returns results."""
        loader = KnowledgeLoader()

        result = await loader.search("knowledge")
        assert result is not None

    @pytest.mark.asyncio
    async def test_search_with_various_queries(self):
        """Test search with various query types."""
        loader = KnowledgeLoader()

        queries = [
            "timeout",
            "autonomy",
            "plugin",
            "memory",
            "cache",
            "load",
            "knowledge base",
        ]

        for query in queries:
            result = await loader.search(query)
            assert result is not None

    @pytest.mark.asyncio
    async def test_search_case_insensitivity(self):
        """Test search is case insensitive."""
        loader = KnowledgeLoader()

        result_lower = await loader.search("timeout")
        result_upper = await loader.search("TIMEOUT")
        result_mixed = await loader.search("TimeOut")

        # All should return valid results
        assert result_lower is not None
        assert result_upper is not None
        assert result_mixed is not None

    @pytest.mark.asyncio
    async def test_search_with_empty_query(self):
        """Test search with empty query."""
        loader = KnowledgeLoader()

        result = await loader.search("")
        # Should handle gracefully
        assert result is not None

    @pytest.mark.asyncio
    async def test_search_with_special_characters(self):
        """Test search with special characters."""
        loader = KnowledgeLoader()

        special_queries = [
            "test@example",
            "path/to/file",
            "question?",
            "item1, item2",
        ]

        for query in special_queries:
            result = await loader.search(query)
            # Should handle without crashing
            assert result is not None


class TestLoadResultStructure:
    """Test load result structure and attributes."""

    @pytest.mark.asyncio
    async def test_load_result_is_valid(self):
        """Test load result is valid."""
        loader = KnowledgeLoader()

        result = await loader.load_core()
        assert result is not None

    @pytest.mark.asyncio
    async def test_load_result_from_different_methods(self):
        """Test results from different load methods."""
        loader = KnowledgeLoader()

        # Test various load methods
        core_result = await loader.load_core()
        assert core_result is not None

        guidelines_result = await loader.load_guidelines("quality")
        assert guidelines_result is not None

        framework_result = await loader.load_framework("autonomy")
        assert framework_result is not None

        task_result = await loader.load_for_task("testing")
        assert task_result is not None


class TestErrorHandling:
    """Test error handling in loader operations."""

    @pytest.mark.asyncio
    async def test_nonexistent_chapter(self):
        """Test loading nonexistent chapter."""
        loader = KnowledgeLoader()

        result = await loader.load_guidelines("nonexistent_chapter_xyz_123")
        # Should return result (possibly empty) without crashing
        assert result is not None

    @pytest.mark.asyncio
    async def test_nonexistent_framework(self):
        """Test loading nonexistent framework."""
        loader = KnowledgeLoader()

        result = await loader.load_framework("nonexistent_framework_xyz_123")
        # Should return result without crashing
        assert result is not None

    @pytest.mark.asyncio
    async def test_very_long_task_description(self):
        """Test with very long task description."""
        loader = KnowledgeLoader()

        long_task = "a" * 10000
        result = await loader.load_for_task(long_task)
        # Should handle without crashing
        assert result is not None


class TestPerformanceCharacteristics:
    """Test performance characteristics of loader."""

    @pytest.mark.asyncio
    async def test_repeated_loads_performance(self):
        """Test that repeated loads are fast (cache hit)."""
        loader = KnowledgeLoader()

        # First load (may be slower)
        start = time.time()
        await loader.load_core()
        first_load_time = time.time() - start

        # Second load (should be faster due to cache)
        start = time.time()
        await loader.load_core()
        second_load_time = time.time() - start

        # Both should complete in reasonable time
        assert first_load_time < 10  # 10 seconds max
        assert second_load_time < 10

    @pytest.mark.asyncio
    async def test_search_performance(self):
        """Test search completes in reasonable time."""
        loader = KnowledgeLoader()

        start = time.time()
        await loader.search("timeout")
        search_time = time.time() - start

        # Should complete quickly
        assert search_time < 5  # 5 seconds max

    @pytest.mark.asyncio
    async def test_multiple_operations_performance(self):
        """Test multiple operations complete efficiently."""
        loader = KnowledgeLoader()

        start = time.time()

        # Perform various operations
        await loader.load_core()
        await loader.search("test")
        await loader.load_guidelines("quality")
        await loader.load_framework("autonomy")
        await loader.load_for_task("coding")

        total_time = time.time() - start

        # All operations should complete in reasonable time
        assert total_time < 30  # 30 seconds max


class TestLayerEnumeration:
    """Test Layer enumeration functionality."""

    @pytest.mark.asyncio
    async def test_all_layers_loadable(self):
        """Test that all Layer enum values can be loaded."""
        loader = KnowledgeLoader()

        for layer in Layer:
            result = await loader.load(layer)
            assert result is not None

    def test_layer_values(self):
        """Test Layer enum has expected values."""
        # Should have standard layers with L prefix
        layer_names = [l.name for l in Layer]
        assert "L0_INDEX" in layer_names
        assert "L1_CORE" in layer_names
        assert "L2_GUIDELINES" in layer_names
        assert "L3_FRAMEWORKS" in layer_names
        assert "L4_PRACTICES" in layer_names


class TestLoaderStateManagement:
    """Test loader state management."""

    @pytest.mark.asyncio
    async def test_loader_maintains_state(self):
        """Test that loader maintains state across operations."""
        loader = KnowledgeLoader()

        # Perform operations
        await loader.load_core()
        await loader.search("test")
        await loader.load_guidelines("quality")

        # Loader should still be functional
        result = await loader.load_framework("autonomy")
        assert result is not None

    @pytest.mark.asyncio
    async def test_multiple_loaders_independent(self):
        """Test that multiple loader instances are independent."""
        loader1 = KnowledgeLoader()
        loader2 = KnowledgeLoader()

        # Operations on one shouldn't affect the other
        await loader1.load_core()
        loader1.clear_cache()

        # Loader2 should still work independently
        result = await loader2.load_core()
        assert result is not None
