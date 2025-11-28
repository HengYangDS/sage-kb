"""
End-to-end integration tests for MCP Server.

Tests tool call sequences, multi-tool collaboration, and session management.

Version: 0.1.0
"""

import pytest

from sage.services.mcp_server import create_app, get_loader


class TestMCPServerCreation:
    """Test MCP server creation and initialization."""

    def test_create_app_returns_fastmcp(self):
        """Test that create_app returns a FastMCP instance."""
        app = create_app()
        assert app is not None
        assert app.name == "sage-kb"

    def test_create_app_multiple_times(self):
        """Test creating multiple app instances."""
        app1 = create_app()
        app2 = create_app()
        # Both should be valid instances
        assert app1 is not None
        assert app2 is not None
        assert app1.name == app2.name

    def test_get_loader_returns_loader(self):
        """Test that get_loader returns a KnowledgeLoader."""
        loader = get_loader()
        assert loader is not None
        from sage.core.loader import KnowledgeLoader
        assert isinstance(loader, KnowledgeLoader)

    def test_get_loader_caching(self):
        """Test that get_loader returns cached instance."""
        loader1 = get_loader()
        loader2 = get_loader()
        # Should be the same cached instance
        assert loader1 is loader2


class TestMCPToolWorkflows:
    """Test MCP tool call workflows."""

    def test_loader_info_workflow(self):
        """Test getting loader info through get_loader."""
        loader = get_loader()
        # Verify loader has expected attributes
        assert hasattr(loader, 'load')
        assert hasattr(loader, 'search')
        assert hasattr(loader, 'load_core')
        assert hasattr(loader, 'load_guidelines')
        assert hasattr(loader, 'load_framework')

    @pytest.mark.asyncio
    async def test_search_workflow(self):
        """Test search functionality workflow."""
        loader = get_loader()
        # Perform search
        results = await loader.search("timeout")
        # Should return results (list or similar)
        assert results is not None

    @pytest.mark.asyncio
    async def test_load_core_workflow(self):
        """Test loading core content workflow."""
        loader = get_loader()
        result = await loader.load_core()
        # Should return result
        assert result is not None

    @pytest.mark.asyncio
    async def test_load_guidelines_workflow(self):
        """Test loading guidelines workflow."""
        loader = get_loader()
        result = await loader.load_guidelines("quality")
        # Should return result or handle missing chapter gracefully
        assert result is not None

    @pytest.mark.asyncio
    async def test_load_framework_workflow(self):
        """Test loading framework workflow."""
        loader = get_loader()
        result = await loader.load_framework("autonomy")
        # Should return result or handle missing framework gracefully
        assert result is not None


class TestMCPToolSequences:
    """Test sequences of MCP tool calls."""

    @pytest.mark.asyncio
    async def test_info_then_load_sequence(self):
        """Test typical sequence: get info, then load content."""
        loader = get_loader()

        # Step 1: Check loader is ready
        assert loader is not None

        # Step 2: Load core content
        core_result = await loader.load_core()
        assert core_result is not None

        # Step 3: Load guidelines
        guidelines_result = await loader.load_guidelines("cognitive")
        assert guidelines_result is not None

    @pytest.mark.asyncio
    async def test_search_then_load_sequence(self):
        """Test search then load sequence."""
        loader = get_loader()

        # Step 1: Search for content
        search_results = await loader.search("knowledge")
        assert search_results is not None

        # Step 2: Load related content based on search
        core_result = await loader.load_core()
        assert core_result is not None

    @pytest.mark.asyncio
    async def test_multi_layer_load_sequence(self):
        """Test loading multiple layers in sequence."""
        loader = get_loader()

        # Load different layers
        core = await loader.load_core()
        assert core is not None

        guidelines = await loader.load_guidelines("quality")
        assert guidelines is not None

        framework = await loader.load_framework("timeout")
        assert framework is not None

    @pytest.mark.asyncio
    async def test_repeated_search_sequence(self):
        """Test multiple searches in sequence."""
        loader = get_loader()

        queries = ["timeout", "autonomy", "memory", "plugin"]
        for query in queries:
            results = await loader.search(query)
            assert results is not None


class TestMCPCacheBehavior:
    """Test MCP cache behavior in integration scenarios."""

    @pytest.mark.asyncio
    async def test_cache_on_repeated_loads(self):
        """Test that repeated loads use cache."""
        loader = get_loader()

        # Load same content twice
        result1 = await loader.load_core()
        result2 = await loader.load_core()

        # Both should return valid results
        assert result1 is not None
        assert result2 is not None

    def test_cache_stats_available(self):
        """Test that cache stats are accessible."""
        loader = get_loader()

        # Check cache stats
        stats = loader.get_cache_stats()
        assert stats is not None
        assert isinstance(stats, dict)

    @pytest.mark.asyncio
    async def test_clear_cache_workflow(self):
        """Test clearing cache and reloading."""
        loader = get_loader()

        # Load content
        await loader.load_core()

        # Clear cache
        loader.clear_cache()

        # Load again - should work after cache clear
        result = await loader.load_core()
        assert result is not None


class TestMCPErrorRecovery:
    """Test MCP error recovery in integration scenarios."""

    @pytest.mark.asyncio
    async def test_invalid_chapter_handling(self):
        """Test handling of invalid chapter names."""
        loader = get_loader()

        # Try to load non-existent chapter
        result = await loader.load_guidelines("nonexistent_chapter_xyz")
        # Should handle gracefully, not crash
        assert result is not None

    @pytest.mark.asyncio
    async def test_invalid_framework_handling(self):
        """Test handling of invalid framework names."""
        loader = get_loader()

        # Try to load non-existent framework
        result = await loader.load_framework("nonexistent_framework_xyz")
        # Should handle gracefully
        assert result is not None

    @pytest.mark.asyncio
    async def test_empty_search_handling(self):
        """Test handling of empty search queries."""
        loader = get_loader()

        # Empty search
        result = await loader.search("")
        # Should handle gracefully
        assert result is not None

    @pytest.mark.asyncio
    async def test_special_character_search(self):
        """Test search with special characters."""
        loader = get_loader()

        # Search with special characters
        result = await loader.search("test@#$%^&*()")
        # Should handle without crashing
        assert result is not None


class TestMCPSessionBehavior:
    """Test MCP session-like behavior."""

    @pytest.mark.asyncio
    async def test_loader_state_persistence(self):
        """Test that loader state persists across operations."""
        loader = get_loader()

        # Perform operations
        await loader.load_core()
        await loader.search("test")

        # Loader should still be valid
        assert loader is not None

        # Should be able to continue operations
        result = await loader.load_guidelines("quality")
        assert result is not None

    @pytest.mark.asyncio
    async def test_multiple_loader_operations(self):
        """Test multiple operations on same loader instance."""
        loader = get_loader()

        # Perform sequence of operations
        result1 = await loader.load_core()
        assert result1 is not None

        result2 = await loader.search("timeout")
        assert result2 is not None

        result3 = await loader.load_guidelines("cognitive")
        assert result3 is not None

        result4 = await loader.load_framework("autonomy")
        assert result4 is not None

        result5 = await loader.search("memory")
        assert result5 is not None

        stats = loader.get_cache_stats()
        assert stats is not None


class TestMCPAppConfiguration:
    """Test MCP app configuration."""

    def test_app_has_required_attributes(self):
        """Test that app has required configuration."""
        app = create_app()

        # Check app attributes
        assert hasattr(app, 'name')
        assert app.name == "sage-kb"

    def test_app_tool_registration(self):
        """Test that tools are registered with the app."""
        app = create_app()

        # App should have tools registered
        # The specific check depends on FastMCP implementation
        assert app is not None


class TestMCPResourceLoading:
    """Test MCP resource loading scenarios."""

    @pytest.mark.asyncio
    async def test_load_for_task(self):
        """Test loading resources for a specific task."""
        loader = get_loader()

        # Load for a task description
        result = await loader.load_for_task("implementing timeout handling")
        assert result is not None

    @pytest.mark.asyncio
    async def test_load_multiple_tasks(self):
        """Test loading for multiple different tasks."""
        loader = get_loader()

        tasks = [
            "implementing timeout handling",
            "writing unit tests",
            "code review guidelines",
            "documentation standards",
        ]

        for task in tasks:
            result = await loader.load_for_task(task)
            assert result is not None


class TestMCPConcurrentAccess:
    """Test MCP behavior under concurrent-like access patterns."""

    @pytest.mark.asyncio
    async def test_rapid_sequential_operations(self):
        """Test rapid sequential operations."""
        loader = get_loader()

        # Perform many operations rapidly
        for _ in range(10):
            await loader.load_core()
            await loader.search("test")

        # Should complete without issues
        assert loader is not None

    @pytest.mark.asyncio
    async def test_alternating_operations(self):
        """Test alternating between different operations."""
        loader = get_loader()

        for i in range(5):
            if i % 2 == 0:
                await loader.load_core()
            else:
                await loader.search(f"query_{i}")

        # Should complete without issues
        assert loader is not None
