"""
Plugin System - Extensible plugin architecture for SAGE Knowledge Base.

This package provides:
- PluginBase: Base class for all plugins
- LoaderPlugin: Plugin for customizing knowledge loading
- AnalyzerPlugin: Plugin for custom content analysis
- FormatterPlugin: Plugin for output formatting
- SearchPlugin: Plugin for customizing search behavior
- LifecyclePlugin: Plugin for system lifecycle events
- ErrorPlugin: Plugin for error handling
- CachePlugin: Plugin for cache events
- PluginRegistry: Central plugin management with hot-reload support

Extension Points (15 hooks):
- pre_load: Before loading content
- post_load: After loading content
- on_timeout: On timeout event
- pre_search: Before search
- post_search: After search
- pre_format: Before output formatting
- post_format: After output formatting
- pre_analyze: Before content analysis
- analyze: Custom content analysis
- post_analyze: After content analysis
- on_startup: System startup event
- on_shutdown: System shutdown event
- on_error: Error handling event
- on_cache_hit: Cache hit event
- on_cache_miss: Cache miss event

Example:
    from sage.plugins import PluginBase, PluginMetadata, get_plugin_registry

    class MyPlugin(PluginBase):
        @property
        def metadata(self) -> PluginMetadata:
            return PluginMetadata(
                name="my-plugin",
                version="0.1.0",
                hooks=["post_load"],
            )

        def post_load(self, layer: str, content: str) -> str:
            return content.upper()

    # Register the plugin
    registry = get_plugin_registry()
    registry.register(MyPlugin())

Author: SAGE AI Collab Team
Version: 0.1.0
"""

from .base import (
    AVAILABLE_HOOKS,
    HOOK_TYPES,
    AnalyzerPlugin,
    CachePlugin,
    ErrorPlugin,
    FormatterPlugin,
    LifecyclePlugin,
    LoaderPlugin,
    PluginBase,
    PluginMetadata,
    SearchPlugin,
)
from .registry import (
    PluginRegistry,
    get_hooks,
    get_plugin_registry,
    register_plugin,
)

__all__ = [
    # Metadata
    "PluginMetadata",
    # Base classes
    "PluginBase",
    "LoaderPlugin",
    "AnalyzerPlugin",
    "FormatterPlugin",
    "SearchPlugin",
    "LifecyclePlugin",
    "ErrorPlugin",
    "CachePlugin",
    # Registry
    "PluginRegistry",
    "get_plugin_registry",
    "register_plugin",
    "get_hooks",
    # Constants
    "HOOK_TYPES",
    "AVAILABLE_HOOKS",
]
