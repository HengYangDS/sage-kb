# Plugin Development Guide

> Guide to creating custom plugins for SAGE Knowledge Base

---

## Table of Contents

[1. Overview](#1-overview) · [2. Plugin Architecture](#2-plugin-architecture) · [3. Creating a Plugin](#3-creating-a-plugin) · [4. Plugin Lifecycle](#4-plugin-lifecycle) · [5. Hook Points](#5-hook-points) · [6. Configuration](#6-configuration) · [7. Testing Plugins](#7-testing-plugins) · [8. Best Practices](#8-best-practices) · [9. Example Plugins](#9-example-plugins)

---

## 1. Overview

### 1.1 What are Plugins?

Plugins extend SAGE functionality without modifying core code. They can:

- Add new content processing capabilities
- Integrate external services
- Customize loading behavior
- Add caching strategies
- Implement custom search algorithms

### 1.2 Plugin Types

| Type | Purpose | Example |
|------|---------|---------|
| **Processor** | Transform content | Markdown preprocessor |
| **Provider** | Add content sources | External API integration |
| **Cache** | Custom caching | Redis cache adapter |
| **Search** | Search enhancement | Semantic search |
| **Hook** | Event handlers | Logging, metrics |

### 1.3 Built-in Plugins

| Plugin | Location | Purpose |
|--------|----------|---------|
| `cache_plugin` | `src/sage/plugins/bundled/` | In-memory caching |
| `semantic_search` | `src/sage/plugins/bundled/` | Semantic search capability |

---

## 2. Plugin Architecture

### 2.1 Architecture Overview

```
┌─────────────────────────────────────────┐
│              SAGE Core                   │
├─────────────────────────────────────────┤
│           Plugin Registry                │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ Plugin1 │ │ Plugin2 │ │ Plugin3 │   │
│  └─────────┘ └─────────┘ └─────────┘   │
├─────────────────────────────────────────┤
│              EventBus                    │
│  (pre_load, post_load, on_timeout...)   │
└─────────────────────────────────────────┘
```

### 2.2 Key Components

| Component | Role |
|-----------|------|
| `PluginBase` | Base class for all plugins |
| `PluginRegistry` | Manages plugin lifecycle |
| `EventBus` | Plugin communication |
| `PluginConfig` | Plugin configuration |

### 2.3 Communication Flow

```
Event Triggered → EventBus → Registered Plugins → Execute Hooks
```

---

## 3. Creating a Plugin

### 3.1 Basic Plugin Structure

```python
"""
My Custom Plugin

Purpose: Brief description of what this plugin does
Author: Your Name
Version: 1.0.0
"""

from typing import Any, Optional

from sage.plugins.base import PluginBase, PluginConfig


class MyPlugin(PluginBase):
    """Custom plugin implementation."""
    
    # Plugin metadata
    name = "my_plugin"
    version = "1.0.0"
    description = "A custom plugin for SAGE"
    
    def __init__(self, config: Optional[PluginConfig] = None) -> None:
        """Initialize plugin.
        
        Args:
            config: Plugin configuration.
        """
        super().__init__(config)
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize plugin resources."""
        # Setup code here
        self._initialized = True
    
    async def shutdown(self) -> None:
        """Clean up plugin resources."""
        # Cleanup code here
        self._initialized = False
    
    def is_healthy(self) -> bool:
        """Check plugin health status."""
        return self._initialized
```

### 3.2 File Structure

```
src/sage/plugins/
├── __init__.py
├── base.py              # PluginBase class
├── registry.py          # PluginRegistry
├── bundled/             # Built-in plugins
│   ├── __init__.py
│   ├── cache_plugin.py
│   └── semantic_search.py
└── custom/              # Your custom plugins
    ├── __init__.py
    └── my_plugin.py
```

### 3.3 Registering a Plugin

```python
# Method 1: Decorator registration
from sage.plugins.registry import register_plugin

@register_plugin
class MyPlugin(PluginBase):
    name = "my_plugin"
    # ...

# Method 2: Manual registration
from sage.plugins.registry import PluginRegistry

registry = PluginRegistry()
registry.register(MyPlugin)

# Method 3: Configuration-based
# config/capabilities/plugins.yaml
plugins:
  enabled:
    - my_plugin
  config:
    my_plugin:
      option1: value1
```

---

## 4. Plugin Lifecycle

### 4.1 Lifecycle Stages

```
┌─────────┐   ┌──────────┐   ┌────────┐   ┌──────────┐
│ Created │ → │ Registered │ → │ Active │ → │ Shutdown │
└─────────┘   └──────────┘   └────────┘   └──────────┘
```

| Stage | Method Called | Description |
|-------|---------------|-------------|
| Created | `__init__()` | Plugin instantiated |
| Registered | `on_register()` | Added to registry |
| Initialized | `initialize()` | Resources setup |
| Active | Hook methods | Handling events |
| Shutdown | `shutdown()` | Cleanup resources |

### 4.2 Lifecycle Methods

```python
class MyPlugin(PluginBase):
    
    async def on_register(self) -> None:
        """Called when plugin is registered."""
        self.logger.info(f"Plugin {self.name} registered")
    
    async def initialize(self) -> None:
        """Called during SAGE startup."""
        await self._connect_to_service()
    
    async def shutdown(self) -> None:
        """Called during SAGE shutdown."""
        await self._disconnect_from_service()
    
    async def on_unregister(self) -> None:
        """Called when plugin is unregistered."""
        self.logger.info(f"Plugin {self.name} unregistered")
```

---

## 5. Hook Points

### 5.1 Available Hooks

| Hook | Trigger | Use Case |
|------|---------|----------|
| `pre_load` | Before content loading | Validation, preprocessing |
| `post_load` | After content loading | Transformation, caching |
| `on_timeout` | When timeout occurs | Fallback handling |
| `pre_search` | Before search | Query enhancement |
| `post_search` | After search | Result filtering |
| `on_error` | When error occurs | Error handling |

### 5.2 Implementing Hooks

```python
from sage.plugins.base import PluginBase
from sage.core.events import Event


class MyPlugin(PluginBase):
    name = "my_plugin"
    
    # Declare which hooks this plugin uses
    hooks = ["pre_load", "post_load", "on_error"]
    
    async def pre_load(self, event: Event) -> Event:
        """Called before content loading.
        
        Args:
            event: Event containing load request details.
            
        Returns:
            Modified or original event.
        """
        # Access event data
        layer = event.data.get("layer")
        path = event.data.get("path")
        
        # Modify event if needed
        event.data["preprocessed"] = True
        
        self.logger.debug(f"Pre-load for layer: {layer}")
        return event
    
    async def post_load(self, event: Event) -> Event:
        """Called after content loading.
        
        Args:
            event: Event containing loaded content.
            
        Returns:
            Modified or original event.
        """
        content = event.data.get("content")
        
        # Process loaded content
        if content:
            event.data["content"] = self._transform_content(content)
        
        return event
    
    async def on_error(self, event: Event) -> Event:
        """Called when an error occurs.
        
        Args:
            event: Event containing error details.
            
        Returns:
            Event (can provide fallback).
        """
        error = event.data.get("error")
        self.logger.error(f"Error occurred: {error}")
        
        # Optionally provide fallback
        event.data["fallback"] = self._get_fallback()
        
        return event
```

### 5.3 Hook Priority

```python
class HighPriorityPlugin(PluginBase):
    name = "high_priority"
    priority = 100  # Higher = runs first (default: 50)

class LowPriorityPlugin(PluginBase):
    name = "low_priority"
    priority = 10  # Lower = runs later
```

---

## 6. Configuration

### 6.1 Plugin Configuration

```yaml
# config/capabilities/plugins.yaml
plugins:
  enabled:
    - cache_plugin
    - semantic_search
    - my_plugin
  
  disabled:
    - deprecated_plugin
  
  config:
    cache_plugin:
      max_size_mb: 100
      ttl_seconds: 3600
    
    my_plugin:
      api_endpoint: "https://api.example.com"
      timeout_ms: 5000
      retry_count: 3
```

### 6.2 Accessing Configuration

```python
class MyPlugin(PluginBase):
    name = "my_plugin"
    
    # Default configuration
    default_config = {
        "api_endpoint": "https://api.example.com",
        "timeout_ms": 5000,
        "retry_count": 3,
    }
    
    def __init__(self, config: Optional[PluginConfig] = None) -> None:
        super().__init__(config)
        
        # Access configuration
        self.api_endpoint = self.config.get("api_endpoint")
        self.timeout_ms = self.config.get("timeout_ms", 5000)
        self.retry_count = self.config.get("retry_count", 3)
```

### 6.3 Environment Variables

```python
import os

class MyPlugin(PluginBase):
    name = "my_plugin"
    
    def __init__(self, config: Optional[PluginConfig] = None) -> None:
        super().__init__(config)
        
        # Support environment variable override
        self.api_key = os.environ.get(
            "MY_PLUGIN_API_KEY",
            self.config.get("api_key")
        )
```

---

## 7. Testing Plugins

### 7.1 Unit Tests

```python
"""Tests for MyPlugin."""

import pytest
from unittest.mock import AsyncMock, MagicMock

from sage.plugins.custom.my_plugin import MyPlugin
from sage.core.events import Event


class TestMyPlugin:
    """Tests for MyPlugin."""
    
    @pytest.fixture
    def plugin(self):
        """Create plugin instance."""
        config = {"api_endpoint": "https://test.api.com"}
        return MyPlugin(config=config)
    
    @pytest.fixture
    def mock_event(self):
        """Create mock event."""
        return Event(
            name="test_event",
            data={"layer": "core", "path": "test.md"}
        )
    
    def test_plugin_metadata(self, plugin):
        """Test plugin has correct metadata."""
        assert plugin.name == "my_plugin"
        assert plugin.version == "1.0.0"
    
    @pytest.mark.asyncio
    async def test_initialize(self, plugin):
        """Test plugin initialization."""
        await plugin.initialize()
        assert plugin.is_healthy()
    
    @pytest.mark.asyncio
    async def test_pre_load_hook(self, plugin, mock_event):
        """Test pre_load hook."""
        await plugin.initialize()
        
        result = await plugin.pre_load(mock_event)
        
        assert result.data.get("preprocessed") is True
    
    @pytest.mark.asyncio
    async def test_shutdown(self, plugin):
        """Test plugin shutdown."""
        await plugin.initialize()
        await plugin.shutdown()
        
        assert not plugin.is_healthy()
```

### 7.2 Integration Tests

```python
"""Integration tests for plugin with SAGE."""

import pytest

from sage.core.loader import ContentLoader
from sage.plugins.registry import PluginRegistry
from sage.plugins.custom.my_plugin import MyPlugin


class TestMyPluginIntegration:
    """Integration tests for MyPlugin."""
    
    @pytest.fixture
    async def registry_with_plugin(self):
        """Create registry with plugin."""
        registry = PluginRegistry()
        plugin = MyPlugin()
        await registry.register(plugin)
        await registry.initialize_all()
        yield registry
        await registry.shutdown_all()
    
    @pytest.mark.asyncio
    async def test_plugin_with_loader(self, registry_with_plugin):
        """Test plugin works with content loader."""
        loader = ContentLoader(plugin_registry=registry_with_plugin)
        
        content = await loader.load("core")
        
        # Verify plugin processed content
        assert content is not None
```

### 7.3 Running Plugin Tests

```bash
# Run all plugin tests
pytest tests/unit/plugins/ -v

# Run specific plugin tests
pytest tests/unit/plugins/test_my_plugin.py -v

# Run with coverage
pytest tests/unit/plugins/ --cov=src/sage/plugins
```

---

## 8. Best Practices

### 8.1 Design Guidelines

| Guideline | Description |
|-----------|-------------|
| **Single Responsibility** | One plugin, one purpose |
| **Fail Gracefully** | Don't crash SAGE on plugin error |
| **Async First** | Use async methods for I/O |
| **Configurable** | Make behavior configurable |
| **Testable** | Design for easy testing |

### 8.2 Error Handling

```python
class MyPlugin(PluginBase):
    name = "my_plugin"
    
    async def pre_load(self, event: Event) -> Event:
        """Hook with proper error handling."""
        try:
            # Plugin logic
            result = await self._process(event)
            event.data["result"] = result
            
        except ExternalServiceError as e:
            # Log but don't crash
            self.logger.warning(f"External service error: {e}")
            # Continue without plugin processing
            
        except Exception as e:
            # Unexpected error - log and continue
            self.logger.error(f"Unexpected error in pre_load: {e}")
        
        return event
```

### 8.3 Resource Management

```python
class MyPlugin(PluginBase):
    name = "my_plugin"
    
    async def initialize(self) -> None:
        """Initialize with proper resource management."""
        self._client = await self._create_client()
        self._cache = {}
    
    async def shutdown(self) -> None:
        """Clean shutdown with resource cleanup."""
        if self._client:
            await self._client.close()
            self._client = None
        
        self._cache.clear()
```

### 8.4 Logging

```python
class MyPlugin(PluginBase):
    name = "my_plugin"
    
    def __init__(self, config: Optional[PluginConfig] = None) -> None:
        super().__init__(config)
        # Logger is provided by PluginBase
        # self.logger is ready to use
    
    async def pre_load(self, event: Event) -> Event:
        """Hook with appropriate logging."""
        self.logger.debug(f"Processing event: {event.name}")
        
        try:
            result = await self._process(event)
            self.logger.info(f"Successfully processed: {event.name}")
        except Exception as e:
            self.logger.error(f"Failed to process: {e}")
        
        return event
```

---

## 9. Example Plugins

### 9.1 Cache Plugin

```python
"""Simple in-memory cache plugin."""

from typing import Any, Optional
from datetime import datetime, timedelta

from sage.plugins.base import PluginBase
from sage.core.events import Event


class CachePlugin(PluginBase):
    """In-memory caching plugin."""
    
    name = "cache_plugin"
    version = "1.0.0"
    hooks = ["pre_load", "post_load"]
    
    default_config = {
        "max_size": 1000,
        "ttl_seconds": 3600,
    }
    
    def __init__(self, config=None):
        super().__init__(config)
        self._cache: dict[str, tuple[Any, datetime]] = {}
    
    async def pre_load(self, event: Event) -> Event:
        """Check cache before loading."""
        cache_key = self._make_key(event)
        
        if cache_key in self._cache:
            value, expiry = self._cache[cache_key]
            if datetime.now() < expiry:
                event.data["content"] = value
                event.data["cache_hit"] = True
                self.logger.debug(f"Cache hit: {cache_key}")
        
        return event
    
    async def post_load(self, event: Event) -> Event:
        """Cache loaded content."""
        if event.data.get("cache_hit"):
            return event
        
        content = event.data.get("content")
        if content:
            cache_key = self._make_key(event)
            ttl = self.config.get("ttl_seconds", 3600)
            expiry = datetime.now() + timedelta(seconds=ttl)
            self._cache[cache_key] = (content, expiry)
            self.logger.debug(f"Cached: {cache_key}")
        
        return event
    
    def _make_key(self, event: Event) -> str:
        """Create cache key from event."""
        return f"{event.data.get('layer')}:{event.data.get('path')}"
```

### 9.2 Metrics Plugin

```python
"""Metrics collection plugin."""

from collections import defaultdict
from time import time

from sage.plugins.base import PluginBase
from sage.core.events import Event


class MetricsPlugin(PluginBase):
    """Collect and expose metrics."""
    
    name = "metrics_plugin"
    version = "1.0.0"
    hooks = ["pre_load", "post_load", "on_error"]
    
    def __init__(self, config=None):
        super().__init__(config)
        self._metrics = defaultdict(lambda: {"count": 0, "total_time": 0})
        self._start_times: dict[str, float] = {}
    
    async def pre_load(self, event: Event) -> Event:
        """Record load start time."""
        event_id = id(event)
        self._start_times[event_id] = time()
        return event
    
    async def post_load(self, event: Event) -> Event:
        """Record load completion."""
        event_id = id(event)
        if event_id in self._start_times:
            duration = time() - self._start_times.pop(event_id)
            layer = event.data.get("layer", "unknown")
            self._metrics[layer]["count"] += 1
            self._metrics[layer]["total_time"] += duration
        return event
    
    async def on_error(self, event: Event) -> Event:
        """Record errors."""
        self._metrics["errors"]["count"] += 1
        return event
    
    def get_metrics(self) -> dict:
        """Get collected metrics."""
        return dict(self._metrics)
```

---

## Related

- `docs/design/05-plugin-memory.md` — Plugin system design
- `.context/decisions/ADR-0008-plugin-system.md` — Plugin architecture decision
- `src/sage/plugins/base.py` — Base plugin implementation
- `config/capabilities/plugins.yaml` — Plugin configuration

---

*Part of SAGE Knowledge Base*
