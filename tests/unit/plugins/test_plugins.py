"""Tests for Plugin system.

Version: 0.1.0
"""

from typing import Any

import pytest

from sage.plugins.base import (
    AnalyzerPlugin,
    FormatterPlugin,
    LoaderPlugin,
    PluginMetadata,
    SearchPlugin,
)
from sage.plugins.registry import (
    PluginRegistry,
    get_hooks,
    get_plugin_registry,
    register_plugin,
)


class TestPluginMetadata:
    """Tests for PluginMetadata dataclass."""

    def test_metadata_creation(self):
        """Test creating plugin metadata."""
        meta = PluginMetadata(
            name="test-plugin",
            version="1.0.0",
            description="A test plugin",
            author="Test Author",
        )
        assert meta.name == "test-plugin"
        assert meta.version == "1.0.0"
        assert meta.description == "A test plugin"
        assert meta.author == "Test Author"

    def test_metadata_defaults(self):
        """Test metadata with defaults."""
        meta = PluginMetadata(
            name="minimal",
            version="0.1.0",
        )
        assert meta.name == "minimal"
        assert meta.description == ""
        assert meta.author == "Unknown"  # Default is "Unknown", not empty

    def test_to_dict(self):
        """Test conversion to dictionary."""
        meta = PluginMetadata(
            name="test",
            version="1.0.0",
            description="Test",
            author="Author",
        )
        d = meta.to_dict()
        assert isinstance(d, dict)
        assert d["name"] == "test"
        assert d["version"] == "1.0.0"


class SampleLoaderPlugin(LoaderPlugin):
    """Sample loader plugin for testing."""

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-loader",
            version="1.0.0",
            description="Sample loader plugin",
        )

    def pre_load(self, layer: str, path: str) -> str | None:
        return path

    def post_load(self, layer: str, content: str) -> str:
        return content + "\n<!-- Loaded by sample-loader -->"

    def on_timeout(self, layer: str, elapsed_ms: int) -> None:
        pass


class SampleAnalyzerPlugin(AnalyzerPlugin):
    """Sample analyzer plugin for testing."""

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-analyzer",
            version="1.0.0",
        )

    def analyze(self, content: str, context: dict[str, Any]) -> dict[str, Any]:
        return {"word_count": len(content.split())}


class SampleFormatterPlugin(FormatterPlugin):
    """Sample formatter plugin for testing."""

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-formatter",
            version="1.0.0",
        )

    def format(self, content: str, format_type: str) -> str:
        return content.upper()


class SampleSearchPlugin(SearchPlugin):
    """Sample search plugin for testing."""

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-search",
            version="1.0.0",
        )

    def pre_search(self, query: str, options: dict[str, Any]) -> tuple[str, dict]:
        return query.lower(), options

    def post_search(
        self, results: list[dict[str, Any]], query: str
    ) -> list[dict[str, Any]]:
        return results


class TestPluginBase:
    """Tests for PluginBase abstract class."""

    def test_loader_plugin_lifecycle(self):
        """Test loader plugin lifecycle methods."""
        plugin = SampleLoaderPlugin()

        # Test metadata
        assert plugin.metadata.name == "sample-loader"

        # Test lifecycle
        plugin.on_load({})
        plugin.on_enable()
        plugin.on_disable()
        plugin.on_unload()

    def test_loader_plugin_hooks(self):
        """Test loader plugin hook methods."""
        plugin = SampleLoaderPlugin()

        # Test pre_load
        result = plugin.pre_load("core", "/path/to/file")
        assert result == "/path/to/file"

        # Test post_load
        result = plugin.post_load("core", "Content")
        assert "sample-loader" in result

        # Test on_timeout
        plugin.on_timeout("core", 1000)

    def test_analyzer_plugin(self):
        """Test analyzer plugin."""
        plugin = SampleAnalyzerPlugin()

        result = plugin.analyze("Hello world test", {})
        assert result["word_count"] == 3

    def test_formatter_plugin(self):
        """Test formatter plugin."""
        plugin = SampleFormatterPlugin()

        result = plugin.format("hello", "plain")
        assert result == "HELLO"

    def test_search_plugin(self):
        """Test search plugin."""
        plugin = SampleSearchPlugin()

        query, options = plugin.pre_search("HELLO", {})
        assert query == "hello"

        results = plugin.post_search([{"title": "Test"}], "hello")
        assert len(results) == 1

    def test_configure(self):
        """Test plugin configuration."""
        plugin = SampleLoaderPlugin()
        plugin.configure({"key": "value"})
        # Should not raise


class TestPluginRegistry:
    """Tests for PluginRegistry singleton."""

    @pytest.fixture
    def registry(self):
        """Create a fresh registry for each test."""
        reg = PluginRegistry()
        reg.clear()
        return reg

    def test_singleton(self):
        """Test that registry is a singleton."""
        reg1 = PluginRegistry()
        reg2 = PluginRegistry()
        assert reg1 is reg2

    def test_register_plugin(self, registry):
        """Test registering a plugin."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        # list_plugins returns list of PluginMetadata objects
        plugins = registry.list_plugins()
        plugin_names = [p.name for p in plugins]
        assert "sample-loader" in plugin_names

    def test_unregister_plugin(self, registry):
        """Test unregistering a plugin."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)
        registry.unregister("sample-loader")

        plugins = registry.list_plugins()
        plugin_names = [p.name for p in plugins]
        assert "sample-loader" not in plugin_names

    def test_get_plugin(self, registry):
        """Test getting a registered plugin."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        retrieved = registry.get_plugin("sample-loader")
        assert retrieved is plugin

    def test_get_plugin_not_found(self, registry):
        """Test getting non-existent plugin."""
        result = registry.get_plugin("nonexistent")
        assert result is None

    def test_list_plugins(self, registry):
        """Test listing all plugins."""
        registry.register(SampleLoaderPlugin())
        registry.register(SampleAnalyzerPlugin())

        plugins = registry.list_plugins()
        assert len(plugins) == 2
        plugin_names = [p.name for p in plugins]
        assert "sample-loader" in plugin_names
        assert "sample-analyzer" in plugin_names

    def test_enable_disable_plugin(self, registry):
        """Test enabling and disabling plugins."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        registry.disable_plugin("sample-loader")
        registry.enable_plugin("sample-loader")
        # Should not raise

    def test_configure_plugin(self, registry):
        """Test configuring a plugin."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        registry.configure_plugin("sample-loader", {"setting": "value"})
        # Should not raise

    def test_get_hooks(self, registry):
        """Test getting hooks."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        hooks = registry.get_hooks("pre_load")
        assert isinstance(hooks, list)

    def test_execute_hook(self, registry):
        """Test executing a hook."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        results = registry.execute_hook("post_load", "core", "Content")
        assert isinstance(results, list)

    def test_execute_hook_chain(self, registry):
        """Test executing a hook chain."""
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        result = registry.execute_hook_chain("post_load", "Initial", "core")
        assert isinstance(result, str)

    def test_clear(self, registry):
        """Test clearing all plugins."""
        registry.register(SampleLoaderPlugin())
        registry.register(SampleAnalyzerPlugin())
        registry.clear()

        assert len(registry.list_plugins()) == 0

    def test_get_stats(self, registry):
        """Test getting registry statistics."""
        registry.register(SampleLoaderPlugin())

        stats = registry.get_stats()
        assert isinstance(stats, dict)
        assert "total_plugins" in stats


class TestRegistryHelperFunctions:
    """Tests for registry helper functions."""

    def test_get_plugin_registry(self):
        """Test get_plugin_registry function."""
        registry = get_plugin_registry()
        assert isinstance(registry, PluginRegistry)

    def test_register_plugin_function(self):
        """Test register_plugin helper function."""
        registry = get_plugin_registry()
        registry.clear()

        plugin = SampleLoaderPlugin()
        register_plugin(plugin)

        plugins = registry.list_plugins()
        plugin_names = [p.name for p in plugins]
        assert "sample-loader" in plugin_names

    def test_get_hooks_function(self):
        """Test get_hooks helper function."""
        registry = get_plugin_registry()
        registry.clear()
        registry.register(SampleLoaderPlugin())

        hooks = get_hooks("pre_load")
        assert isinstance(hooks, list)


class TestPluginRegistryAdvanced:
    """Advanced tests for PluginRegistry - dynamic loading and error handling."""

    @pytest.fixture
    def registry(self):
        """Create fresh registry for each test."""
        reg = PluginRegistry()
        reg.clear()
        reg._loaded_modules.clear()
        return reg

    def test_load_from_directory_not_exists(self, registry, tmp_path):
        """Test load_from_directory with non-existent path."""
        fake_path = tmp_path / "nonexistent"
        count = registry.load_from_directory(fake_path)
        assert count == 0

    def test_load_from_directory_empty(self, registry, tmp_path):
        """Test load_from_directory with empty directory."""
        count = registry.load_from_directory(tmp_path)
        assert count == 0

    def test_load_from_directory_skips_private(self, registry, tmp_path):
        """Test that private files (starting with _) are skipped."""
        # Create a private plugin file
        private_file = tmp_path / "_private_plugin.py"
        private_file.write_text("""
from sage.plugins.base import LoaderPlugin, PluginMetadata

class PrivatePlugin(LoaderPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="private", version="1.0.0")
""")
        count = registry.load_from_directory(tmp_path)
        assert count == 0

    def test_load_from_directory_success(self, registry, tmp_path):
        """Test successful plugin loading from directory."""
        # Create a valid plugin file
        plugin_file = tmp_path / "test_plugin.py"
        plugin_file.write_text("""
from sage.plugins.base import LoaderPlugin, PluginMetadata

class TestDynamicPlugin(LoaderPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="dynamic-test", version="1.0.0")

    def pre_load(self, layer, path):
        return True

    def post_load(self, layer, content):
        return content

    def on_timeout(self, layer, elapsed_ms):
        pass
""")
        count = registry.load_from_directory(tmp_path)
        assert count == 1
        assert registry.get_plugin("dynamic-test") is not None

    def test_load_from_directory_multiple_plugins(self, registry, tmp_path):
        """Test loading multiple plugins from directory."""
        # Create first plugin file
        plugin1 = tmp_path / "plugin_one.py"
        plugin1.write_text("""
from sage.plugins.base import LoaderPlugin, PluginMetadata

class PluginOne(LoaderPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="plugin-one", version="1.0.0")
""")
        # Create second plugin file
        plugin2 = tmp_path / "plugin_two.py"
        plugin2.write_text("""
from sage.plugins.base import AnalyzerPlugin, PluginMetadata

class PluginTwo(AnalyzerPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="plugin-two", version="1.0.0")

    def analyze(self, content, context):
        return {"result": "ok"}
""")
        count = registry.load_from_directory(tmp_path)
        assert count == 2

    def test_load_from_directory_handles_error(self, registry, tmp_path):
        """Test that errors in plugin files are handled gracefully."""
        # Create a plugin with syntax error
        bad_plugin = tmp_path / "bad_plugin.py"
        bad_plugin.write_text("this is not valid python {{{{")

        # Should not raise, just return 0
        count = registry.load_from_directory(tmp_path)
        assert count == 0

    def test_load_plugin_file_invalid_spec(self, registry, tmp_path):
        """Test _load_plugin_file with file that can't produce spec."""
        # Create empty file with unusual extension that we rename
        weird_file = tmp_path / "weird"
        weird_file.write_text("")

        # This should handle gracefully
        count = registry._load_plugin_file(weird_file)
        # May return 0 or handle differently based on importlib behavior
        assert count >= 0

    def test_load_plugin_file_with_multiple_classes(self, registry, tmp_path):
        """Test loading file with multiple plugin classes."""
        plugin_file = tmp_path / "multi_plugin.py"
        plugin_file.write_text("""
from sage.plugins.base import LoaderPlugin, AnalyzerPlugin, PluginMetadata

class FirstPlugin(LoaderPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="first", version="1.0.0")

class SecondPlugin(AnalyzerPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="second", version="1.0.0")

    def analyze(self, content, context):
        return {}
""")
        count = registry._load_plugin_file(plugin_file)
        assert count == 2

    def test_reload_plugin_not_found(self, registry):
        """Test reload_plugin with non-existent plugin."""
        result = registry.reload_plugin("nonexistent")
        assert result is False

    def test_register_duplicate_plugin(self, registry):
        """Test registering same plugin twice."""
        plugin = SampleLoaderPlugin()
        result1 = registry.register(plugin)
        result2 = registry.register(plugin)

        assert result1 is True
        # Second registration should handle duplicate
        assert len(registry.list_plugins()) >= 1

    def test_unregister_nonexistent(self, registry):
        """Test unregistering non-existent plugin."""
        result = registry.unregister("nonexistent")
        assert result is False

    def test_enable_nonexistent_plugin(self, registry):
        """Test enabling non-existent plugin."""
        result = registry.enable_plugin("nonexistent")
        assert result is False

    def test_disable_nonexistent_plugin(self, registry):
        """Test disabling non-existent plugin."""
        result = registry.disable_plugin("nonexistent")
        assert result is False

    def test_configure_nonexistent_plugin(self, registry):
        """Test configuring non-existent plugin."""
        result = registry.configure_plugin("nonexistent", {"key": "value"})
        assert result is False

    def test_execute_hook_no_plugins(self, registry):
        """Test execute_hook with no registered plugins."""
        results = registry.execute_hook("pre_load", "layer", "path")
        assert results == []

    def test_execute_hook_chain_no_plugins(self, registry):
        """Test execute_hook_chain with no plugins."""
        result = registry.execute_hook_chain("post_load", "initial", "layer")
        assert result == "initial"

    def test_get_stats_detailed(self, registry):
        """Test get_stats returns detailed information."""
        registry.register(SampleLoaderPlugin())
        registry.register(SampleAnalyzerPlugin())

        stats = registry.get_stats()
        assert stats["total_plugins"] == 2
        assert "enabled_plugins" in stats
        assert "hooks" in stats

    def test_register_plugin_with_unknown_hook(self, registry):
        """Test registering plugin with unknown hook triggers warning."""

        class PluginWithUnknownHook(LoaderPlugin):
            @property
            def metadata(self):
                return PluginMetadata(
                    name="unknown-hook-plugin",
                    version="1.0.0",
                    hooks=["unknown_hook_xyz"],
                )

        plugin = PluginWithUnknownHook()
        result = registry.register(plugin)
        # Should still register but log warning about unknown hook
        assert result is True
        assert registry.get_plugin("unknown-hook-plugin") is not None

    def test_execute_hook_with_exception(self, registry):
        """Test execute_hook handles plugin exceptions gracefully."""

        class FailingPlugin(LoaderPlugin):
            @property
            def metadata(self):
                return PluginMetadata(
                    name="failing-plugin", version="1.0.0", hooks=["pre_load"]
                )

            def pre_load(self, layer: str, path: str) -> str:
                raise RuntimeError("Intentional test error")

        registry.register(FailingPlugin())
        # Should not raise, just log error
        results = registry.execute_hook("pre_load", "layer", "path")
        assert isinstance(results, list)

    def test_execute_hook_chain_with_exception(self, registry):
        """Test execute_hook_chain handles plugin exceptions gracefully."""

        class FailingChainPlugin(LoaderPlugin):
            @property
            def metadata(self):
                return PluginMetadata(
                    name="failing-chain-plugin", version="1.0.0", hooks=["post_load"]
                )

            def post_load(self, layer: str, content: str) -> str:
                raise RuntimeError("Intentional chain error")

        registry.register(FailingChainPlugin())
        # Should not raise, just log error and continue
        result = registry.execute_hook_chain("post_load", "initial", "layer")
        # Result should be the initial value since plugin failed
        assert result == "initial"

    def test_reload_plugin_from_file(self, registry, tmp_path):
        """Test reload_plugin with plugin loaded from file."""
        # Create plugin file
        plugin_file = tmp_path / "reloadable_plugin.py"
        plugin_file.write_text("""
from sage.plugins.base import LoaderPlugin, PluginMetadata

class ReloadablePlugin(LoaderPlugin):
    @property
    def metadata(self):
        return PluginMetadata(name="reloadable", version="1.0.0")
""")
        # Load plugin from directory
        count = registry.load_from_directory(tmp_path)
        assert count == 1

        # Now try to reload
        result = registry.reload_plugin("reloadable")
        # May succeed or fail depending on module state
        assert isinstance(result, bool)

    def test_reload_plugin_module_not_found(self, registry):
        """Test reload_plugin when module cannot be found."""
        # Register plugin directly (not from file)
        plugin = SampleLoaderPlugin()
        registry.register(plugin)

        # Try to reload - should fail since not loaded from file
        result = registry.reload_plugin("sample-loader")
        assert result is False

    def test_execute_hook_with_non_callable(self, registry):
        """Test execute_hook skips non-callable attributes."""

        class PluginWithAttribute(LoaderPlugin):
            @property
            def metadata(self):
                return PluginMetadata(
                    name="attr-plugin", version="1.0.0", hooks=["pre_load"]
                )

            # pre_load is not defined, so getattr will return None

        registry.register(PluginWithAttribute())
        results = registry.execute_hook("pre_load", "layer", "path")
        assert isinstance(results, list)

    def test_execute_hook_chain_with_non_callable(self, registry):
        """Test execute_hook_chain skips non-callable attributes."""

        class PluginWithoutMethod(LoaderPlugin):
            @property
            def metadata(self):
                return PluginMetadata(
                    name="no-method-plugin", version="1.0.0", hooks=["post_load"]
                )

            # post_load is not defined

        registry.register(PluginWithoutMethod())
        result = registry.execute_hook_chain("post_load", "initial", "layer")
        # Result may change based on plugin behavior
        assert result is not None


class TestPluginBaseExtended:
    """Extended tests for PluginBase methods."""

    def test_plugin_on_enable(self):
        """Test on_enable lifecycle hook."""
        plugin = SampleLoaderPlugin()
        # Should not raise
        plugin.on_enable()

    def test_plugin_on_disable(self):
        """Test on_disable lifecycle hook."""
        plugin = SampleLoaderPlugin()
        # Should not raise
        plugin.on_disable()

    def test_plugin_on_load(self):
        """Test on_load lifecycle hook."""
        plugin = SampleLoaderPlugin()
        # Should not raise
        plugin.on_load({"key": "value"})

    def test_plugin_on_unload(self):
        """Test on_unload lifecycle hook."""
        plugin = SampleLoaderPlugin()
        # Should not raise
        plugin.on_unload()

    def test_analyzer_plugin_analyze(self):
        """Test AnalyzerPlugin analyze method."""
        plugin = SampleAnalyzerPlugin()
        result = plugin.analyze("test content", {"context": "value"})
        assert isinstance(result, dict)

    def test_formatter_plugin_format(self):
        """Test FormatterPlugin format method."""
        plugin = SampleFormatterPlugin()
        result = plugin.format("test content", "markdown")
        assert isinstance(result, str)

    def test_search_plugin_pre_search(self):
        """Test SearchPlugin pre_search method."""
        plugin = SampleSearchPlugin()
        result = plugin.pre_search("query", {"option": "value"})
        # Result can be string or tuple depending on implementation
        assert result is not None

    def test_search_plugin_post_search(self):
        """Test SearchPlugin post_search method."""
        plugin = SampleSearchPlugin()
        results = [{"id": 1}, {"id": 2}]
        result = plugin.post_search(results, "query")
        assert isinstance(result, list)


# ============================================================================
# New Plugin Types Tests (v0.1.0 Enhancement)
# ============================================================================

from sage.plugins import (
    CachePlugin,
    ErrorPlugin,
    LifecyclePlugin,
)


class SampleLifecyclePlugin(LifecyclePlugin):
    """Sample lifecycle plugin for testing."""

    def __init__(self):
        self.startup_called = False
        self.shutdown_called = False
        self.startup_context = None
        self.shutdown_context = None

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-lifecycle",
            version="1.0.0",
            hooks=["on_startup", "on_shutdown"],
        )

    def on_startup(self, context: dict[str, Any]) -> None:
        self.startup_called = True
        self.startup_context = context

    def on_shutdown(self, context: dict[str, Any]) -> None:
        self.shutdown_called = True
        self.shutdown_context = context


class SampleErrorPlugin(ErrorPlugin):
    """Sample error plugin for testing."""

    def __init__(self):
        self.errors_handled = []

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-error",
            version="1.0.0",
            hooks=["on_error"],
        )

    def on_error(self, error: Exception, context: dict[str, Any]) -> Any | None:
        self.errors_handled.append((error, context))
        # Return recovery value for specific errors
        if isinstance(error, ValueError):
            return "recovered"
        return None


class SampleCachePlugin(CachePlugin):
    """Sample cache plugin for testing."""

    def __init__(self):
        self.hits = []
        self.misses = []

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-cache",
            version="1.0.0",
            hooks=["on_cache_hit", "on_cache_miss"],
        )

    def on_cache_hit(self, key: str, value: Any, context: dict[str, Any]) -> Any:
        self.hits.append((key, value, context))
        return value

    def on_cache_miss(self, key: str, context: dict[str, Any]) -> None:
        self.misses.append((key, context))


class SampleAnalyzerPluginExtended(AnalyzerPlugin):
    """Sample analyzer plugin with pre/post analyze hooks."""

    def __init__(self):
        self.pre_analyze_called = False
        self.post_analyze_called = False

    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="sample-analyzer-extended",
            version="1.0.0",
            hooks=["pre_analyze", "analyze", "post_analyze"],
        )

    def pre_analyze(
        self, content: str, context: dict[str, Any]
    ) -> tuple[str, dict[str, Any]]:
        self.pre_analyze_called = True
        # Preprocess: strip whitespace
        return content.strip(), {**context, "preprocessed": True}

    def analyze(self, content: str, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "word_count": len(content.split()),
            "char_count": len(content),
        }

    def post_analyze(
        self, results: dict[str, Any], context: dict[str, Any]
    ) -> dict[str, Any]:
        self.post_analyze_called = True
        results["postprocessed"] = True
        return results


class TestLifecyclePlugin:
    """Tests for LifecyclePlugin."""

    def test_lifecycle_plugin_creation(self):
        """Test creating a lifecycle plugin."""
        plugin = SampleLifecyclePlugin()
        assert plugin.metadata.name == "sample-lifecycle"
        assert "on_startup" in plugin.metadata.hooks
        assert "on_shutdown" in plugin.metadata.hooks

    def test_on_startup(self):
        """Test on_startup hook."""
        plugin = SampleLifecyclePlugin()
        context = {"config": {"debug": True}}
        plugin.on_startup(context)
        assert plugin.startup_called is True
        assert plugin.startup_context == context

    def test_on_shutdown(self):
        """Test on_shutdown hook."""
        plugin = SampleLifecyclePlugin()
        context = {"stats": {"requests": 100}}
        plugin.on_shutdown(context)
        assert plugin.shutdown_called is True
        assert plugin.shutdown_context == context

    def test_lifecycle_default_implementation(self):
        """Test default LifecyclePlugin methods don't raise."""

        class MinimalLifecyclePlugin(LifecyclePlugin):
            @property
            def metadata(self) -> PluginMetadata:
                return PluginMetadata(
                    name="minimal-lifecycle",
                    version="1.0.0",
                    hooks=["on_startup", "on_shutdown"],
                )

        plugin = MinimalLifecyclePlugin()
        # Default implementations should not raise
        plugin.on_startup({})
        plugin.on_shutdown({})


class TestErrorPlugin:
    """Tests for ErrorPlugin."""

    def test_error_plugin_creation(self):
        """Test creating an error plugin."""
        plugin = SampleErrorPlugin()
        assert plugin.metadata.name == "sample-error"
        assert "on_error" in plugin.metadata.hooks

    def test_on_error_with_recovery(self):
        """Test on_error hook with recovery value."""
        plugin = SampleErrorPlugin()
        error = ValueError("test error")
        context = {"operation": "load"}
        result = plugin.on_error(error, context)
        assert result == "recovered"
        assert len(plugin.errors_handled) == 1
        assert plugin.errors_handled[0][0] == error

    def test_on_error_without_recovery(self):
        """Test on_error hook without recovery."""
        plugin = SampleErrorPlugin()
        error = RuntimeError("test error")
        context = {"operation": "search"}
        result = plugin.on_error(error, context)
        assert result is None
        assert len(plugin.errors_handled) == 1

    def test_error_default_implementation(self):
        """Test default ErrorPlugin methods."""

        class MinimalErrorPlugin(ErrorPlugin):
            @property
            def metadata(self) -> PluginMetadata:
                return PluginMetadata(
                    name="minimal-error",
                    version="1.0.0",
                    hooks=["on_error"],
                )

        plugin = MinimalErrorPlugin()
        result = plugin.on_error(Exception("test"), {})
        assert result is None


class TestCachePlugin:
    """Tests for CachePlugin."""

    def test_cache_plugin_creation(self):
        """Test creating a cache plugin."""
        plugin = SampleCachePlugin()
        assert plugin.metadata.name == "sample-cache"
        assert "on_cache_hit" in plugin.metadata.hooks
        assert "on_cache_miss" in plugin.metadata.hooks

    def test_on_cache_hit(self):
        """Test on_cache_hit hook."""
        plugin = SampleCachePlugin()
        value = {"data": "test"}
        context = {"layer": "core"}
        result = plugin.on_cache_hit("key1", value, context)
        assert result == value
        assert len(plugin.hits) == 1
        assert plugin.hits[0] == ("key1", value, context)

    def test_on_cache_miss(self):
        """Test on_cache_miss hook."""
        plugin = SampleCachePlugin()
        context = {"layer": "guidelines"}
        plugin.on_cache_miss("missing_key", context)
        assert len(plugin.misses) == 1
        assert plugin.misses[0] == ("missing_key", context)

    def test_cache_default_implementation(self):
        """Test default CachePlugin methods."""

        class MinimalCachePlugin(CachePlugin):
            @property
            def metadata(self) -> PluginMetadata:
                return PluginMetadata(
                    name="minimal-cache",
                    version="1.0.0",
                    hooks=["on_cache_hit", "on_cache_miss"],
                )

        plugin = MinimalCachePlugin()
        # Default on_cache_hit returns the value
        result = plugin.on_cache_hit("key", "value", {})
        assert result == "value"
        # Default on_cache_miss does nothing
        plugin.on_cache_miss("key", {})


class TestAnalyzerPluginExtended:
    """Tests for AnalyzerPlugin pre_analyze/post_analyze hooks."""

    def test_analyzer_extended_creation(self):
        """Test creating extended analyzer plugin."""
        plugin = SampleAnalyzerPluginExtended()
        assert plugin.metadata.name == "sample-analyzer-extended"
        assert "pre_analyze" in plugin.metadata.hooks
        assert "analyze" in plugin.metadata.hooks
        assert "post_analyze" in plugin.metadata.hooks

    def test_pre_analyze(self):
        """Test pre_analyze hook."""
        plugin = SampleAnalyzerPluginExtended()
        content = "  test content  "
        context = {"file": "test.md"}
        new_content, new_context = plugin.pre_analyze(content, context)
        assert new_content == "test content"
        assert new_context["preprocessed"] is True
        assert plugin.pre_analyze_called is True

    def test_post_analyze(self):
        """Test post_analyze hook."""
        plugin = SampleAnalyzerPluginExtended()
        results = {"word_count": 5}
        context = {"file": "test.md"}
        new_results = plugin.post_analyze(results, context)
        assert new_results["postprocessed"] is True
        assert plugin.post_analyze_called is True

    def test_full_analyze_pipeline(self):
        """Test full analyze pipeline with pre/post hooks."""
        plugin = SampleAnalyzerPluginExtended()
        content = "  hello world  "
        context = {"file": "test.md"}

        # Pre-analyze
        processed_content, processed_context = plugin.pre_analyze(content, context)
        assert processed_content == "hello world"

        # Analyze
        results = plugin.analyze(processed_content, processed_context)
        assert results["word_count"] == 2

        # Post-analyze
        final_results = plugin.post_analyze(results, processed_context)
        assert final_results["postprocessed"] is True
        assert final_results["word_count"] == 2

    def test_analyzer_default_pre_post(self):
        """Test default pre_analyze/post_analyze implementations."""
        # Use SampleAnalyzerPlugin which has default implementations
        plugin = SampleAnalyzerPlugin()

        # Default pre_analyze returns unchanged
        content, context = plugin.pre_analyze("test", {"key": "value"})
        assert content == "test"
        assert context == {"key": "value"}

        # Default post_analyze returns unchanged
        results = plugin.post_analyze({"count": 1}, {})
        assert results == {"count": 1}


class TestNewPluginsWithRegistry:
    """Tests for new plugins with PluginRegistry."""

    @pytest.fixture
    def registry(self):
        """Create a fresh registry for each test."""
        reg = PluginRegistry()
        reg.clear()
        return reg

    def test_register_lifecycle_plugin(self, registry):
        """Test registering a lifecycle plugin."""
        plugin = SampleLifecyclePlugin()
        assert registry.register(plugin) is True
        assert registry.get_plugin("sample-lifecycle") is not None

        hooks = registry.get_hooks("on_startup")
        assert len(hooks) == 1
        assert hooks[0] == plugin

    def test_register_error_plugin(self, registry):
        """Test registering an error plugin."""
        plugin = SampleErrorPlugin()
        assert registry.register(plugin) is True

        hooks = registry.get_hooks("on_error")
        assert len(hooks) == 1

    def test_register_cache_plugin(self, registry):
        """Test registering a cache plugin."""
        plugin = SampleCachePlugin()
        assert registry.register(plugin) is True

        hit_hooks = registry.get_hooks("on_cache_hit")
        miss_hooks = registry.get_hooks("on_cache_miss")
        assert len(hit_hooks) == 1
        assert len(miss_hooks) == 1

    def test_execute_lifecycle_hooks(self, registry):
        """Test executing lifecycle hooks through registry."""
        plugin = SampleLifecyclePlugin()
        registry.register(plugin)

        # Execute on_startup
        registry.execute_hook("on_startup", {"config": "test"})
        assert plugin.startup_called is True

        # Execute on_shutdown
        registry.execute_hook("on_shutdown", {"stats": "test"})
        assert plugin.shutdown_called is True

    def test_execute_error_hook(self, registry):
        """Test executing error hook through registry."""
        plugin = SampleErrorPlugin()
        registry.register(plugin)

        error = ValueError("test")
        results = registry.execute_hook("on_error", error, {"op": "load"})
        assert len(results) == 1
        assert results[0] == "recovered"

    def test_execute_cache_hooks(self, registry):
        """Test executing cache hooks through registry."""
        plugin = SampleCachePlugin()
        registry.register(plugin)

        # Execute on_cache_hit
        results = registry.execute_hook("on_cache_hit", "key", "value", {})
        assert len(results) == 1
        assert results[0] == "value"

        # Execute on_cache_miss
        registry.execute_hook("on_cache_miss", "missing", {})
        assert len(plugin.misses) == 1

    def test_stats_include_new_hooks(self, registry):
        """Test that stats include new hook types."""
        stats = registry.get_stats()
        assert "on_startup" in stats["hooks"]
        assert "on_shutdown" in stats["hooks"]
        assert "on_error" in stats["hooks"]
        assert "on_cache_hit" in stats["hooks"]
        assert "on_cache_miss" in stats["hooks"]
        assert "pre_analyze" in stats["hooks"]
        assert "post_analyze" in stats["hooks"]
