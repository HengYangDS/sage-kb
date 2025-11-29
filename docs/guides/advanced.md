# Advanced Usage Guide

> Deep dive into SAGE Knowledge Base advanced features and customization

---

## Table of Contents

[1. Configuration](#1-configuration) · [2. CLI Advanced](#2-cli-advanced) · [3. MCP Advanced](#3-mcp-advanced) · [4. Python API Advanced](#4-python-api-advanced) · [5. Plugin Development](#5-plugin-development) · [6. Performance Tuning](#6-performance-tuning)

---

## 1. Configuration

### 1.1 Configuration Files

SAGE uses a modular configuration system:

```
config/
├── sage.yaml           # Main configuration
├── core/               # Core layer settings
│   ├── di.yaml         # Dependency injection
│   ├── logging.yaml    # Logging configuration
│   ├── memory.yaml     # Memory/persistence
│   ├── security.yaml   # Security settings
│   └── timeout.yaml    # Timeout hierarchy
├── services/           # Service layer settings
│   ├── api.yaml        # REST API config
│   ├── cli.yaml        # CLI config
│   └── mcp.yaml        # MCP server config
├── knowledge/          # Knowledge management
│   ├── content.yaml    # Content paths
│   ├── loading.yaml    # Loading strategies
│   ├── triggers.yaml   # Auto-load triggers
│   └── token_budget.yaml
└── capabilities/       # Capability settings
    ├── autonomy.yaml
    ├── plugins.yaml
    └── quality.yaml
```

### 1.2 Environment Variable Overrides

Override any configuration with environment variables:

```bash
# Pattern: SAGE_<SECTION>_<KEY>=value
export SAGE_TIMEOUT_CACHE_LOOKUP=200ms
export SAGE_LOGGING_LEVEL=DEBUG
export SAGE_MCP_PORT=8080
```

### 1.3 Custom Configuration

Create a custom configuration file:

```yaml
# my-sage.yaml
extends: config/sage.yaml

timeout:
  operations:
    cache_lookup: 200ms  # Override default
    
logging:
  level: DEBUG
  format: json
```

Load with:

```bash
sage --config my-sage.yaml get core
```

---

## 2. CLI Advanced

### 2.1 Output Formats

```bash
# JSON output
sage get core --format json

# YAML output
sage get core --format yaml

# Minimal output (content only)
sage get core --format minimal

# Rich formatted (default)
sage get core --format rich
```

### 2.2 Filtering and Selection

```bash
# Get specific layer
sage get --layer guidelines

# Get by topic
sage get --topic timeout

# Combine filters
sage get --layer practices --topic testing
```

### 2.3 Search Options

```bash
# Case-insensitive search (default)
sage search "timeout"

# Regex search
sage search --regex "timeout|circuit"

# Search in specific layer
sage search "pattern" --layer frameworks

# Limit results
sage search "api" --limit 10
```

### 2.4 Batch Operations

```bash
# Export all knowledge
sage export --output ./export/

# Export specific layers
sage export --layers core,guidelines --output ./export/

# Import knowledge
sage import ./external-knowledge/
```

### 2.5 Shell Completion

```bash
# Bash
sage --install-completion bash

# Zsh
sage --install-completion zsh

# Fish
sage --install-completion fish
```

---

## 3. MCP Advanced

### 3.1 Server Configuration

```yaml
# config/services/mcp.yaml
mcp:
  host: "0.0.0.0"
  port: 8765
  
  # Connection settings
  max_connections: 100
  connection_timeout: 30s
  
  # Security
  require_auth: false
  allowed_origins:
    - "localhost"
    - "127.0.0.1"
  
  # Tools exposure
  tools:
    enabled:
      - get_knowledge
      - search_knowledge
      - kb_info
      - get_framework
      - analyze_code
      - check_quality
    disabled:
      - admin_tools
```

### 3.2 Multi-Client Support

```python
# Server with multiple client handling
from sage.services.mcp import create_mcp_server

server = create_mcp_server(
    max_clients=50,
    client_timeout=300,  # 5 minutes
    rate_limit=100,      # requests per minute
)
```

### 3.3 Custom Tools

```python
from sage.services.mcp import MCPServer
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sage-custom")

@mcp.tool()
async def my_custom_tool(query: str) -> str:
    """Custom tool description."""
    # Your implementation
    return result

# Register with SAGE
server = MCPServer()
server.register_custom_tool(my_custom_tool)
```

### 3.4 Prompts and Resources

```python
# Custom prompt
@mcp.prompt()
def code_review_prompt(code: str, language: str) -> str:
    """Generate code review prompt."""
    return f"""
    Review the following {language} code:
    
    ```{language}
    {code}
    ```
    
    Consider: readability, performance, security.
    """

# Custom resource
@mcp.resource("sage://custom/{path}")
async def custom_resource(path: str) -> str:
    """Serve custom resource."""
    return await load_custom_content(path)
```

---

## 4. Python API Advanced

### 4.1 Async Operations

```python
import asyncio
from sage.core.loader import KnowledgeLoader

async def load_multiple():
    loader = KnowledgeLoader()
    
    # Concurrent loading
    results = await asyncio.gather(
        loader.load_core(timeout_ms=2000),
        loader.load_guidelines(timeout_ms=2000),
        loader.load_frameworks(timeout_ms=3000),
    )
    
    return results

# Run
results = asyncio.run(load_multiple())
```

### 4.2 Custom Loader

```python
from sage.core.protocols import LoaderProtocol
from sage.core.models import LoadResult

class CustomLoader(LoaderProtocol):
    """Custom knowledge loader."""
    
    async def load(
        self,
        path: str,
        timeout_ms: int = 2000,
    ) -> LoadResult:
        # Custom loading logic
        content = await self._fetch_content(path)
        
        return LoadResult(
            content=content,
            metadata={"source": "custom"},
            tokens=self._count_tokens(content),
        )
    
    async def _fetch_content(self, path: str) -> str:
        # Your implementation
        pass
```

### 4.3 Event Handling

```python
from sage.core.events import EventBus

bus = EventBus()

# Subscribe to events
@bus.subscribe("knowledge.loaded")
async def on_knowledge_loaded(event):
    print(f"Loaded: {event.data['path']}")
    print(f"Tokens: {event.data['tokens']}")

@bus.subscribe("timeout.exceeded")
async def on_timeout(event):
    print(f"Timeout at level {event.data['level']}")

# Publish events
await bus.publish("custom.event", {"key": "value"})
```

### 4.4 Token Budget Management

```python
from sage.core.memory import TokenBudget

budget = TokenBudget(max_tokens=8000)

# Allocate tokens
budget.allocate("core", 2000)
budget.allocate("guidelines", 1500)

# Check availability
if budget.available >= 1000:
    budget.allocate("frameworks", 1000)

# Get usage report
report = budget.get_report()
print(f"Used: {report.used}/{report.total}")
```

### 4.5 Circuit Breaker

```python
from sage.core.timeout import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    recovery_timeout=30,
)

async def protected_operation():
    async with breaker:
        return await risky_operation()

# Check state
if breaker.is_open:
    print("Circuit is open, using fallback")
```

---

## 5. Plugin Development

### 5.1 Plugin Structure

```
my_plugin/
├── __init__.py
├── plugin.py          # Main plugin class
├── tools.py           # MCP tools
├── config.yaml        # Plugin configuration
└── README.md
```

### 5.2 Basic Plugin

```python
# my_plugin/plugin.py
from sage.plugins import PluginBase, hookimpl

class MyPlugin(PluginBase):
    """My custom plugin."""
    
    name = "my-plugin"
    version = "1.0.0"
    
    @hookimpl
    def on_load(self, context):
        """Called when plugin loads."""
        self.logger.info("Plugin loaded")
    
    @hookimpl
    def on_knowledge_request(self, request):
        """Intercept knowledge requests."""
        # Modify or enhance request
        return request
    
    @hookimpl
    def on_knowledge_response(self, response):
        """Process knowledge responses."""
        # Add custom processing
        return response
```

### 5.3 Plugin Configuration

```yaml
# my_plugin/config.yaml
name: my-plugin
version: 1.0.0
description: My custom SAGE plugin

settings:
  feature_enabled: true
  custom_path: ./data/

hooks:
  - on_load
  - on_knowledge_request
  - on_knowledge_response

dependencies:
  - sage>=0.1.0
```

### 5.4 Register Plugin

```yaml
# config/capabilities/plugins.yaml
plugins:
  enabled:
    - my-plugin
  
  paths:
    - ./plugins/
    - ~/.sage/plugins/
  
  settings:
    my-plugin:
      feature_enabled: true
```

---

## 6. Performance Tuning

### 6.1 Timeout Optimization

```yaml
# Aggressive timeouts for fast responses
timeout:
  operations:
    cache_lookup: 50ms    # Reduce from 100ms
    file_read: 300ms      # Reduce from 500ms
    layer_load: 1500ms    # Reduce from 2s
```

### 6.2 Caching Strategy

```yaml
# config/core/memory.yaml
cache:
  enabled: true
  backend: memory  # or: redis, filesystem
  
  ttl:
    core: 3600        # 1 hour
    guidelines: 1800  # 30 minutes
    search: 300       # 5 minutes
  
  max_size: 100MB
  eviction: lru
```

### 6.3 Loading Optimization

```yaml
# config/knowledge/loading.yaml
loading:
  strategy: lazy  # eager | lazy | on-demand
  
  preload:
    - core/principles.md
    - core/defaults.md
  
  parallel:
    enabled: true
    max_workers: 4
```

### 6.4 Memory Management

```python
from sage.core.memory import MemoryManager

manager = MemoryManager(
    max_memory_mb=512,
    gc_threshold=0.8,
)

# Monitor memory
stats = manager.get_stats()
print(f"Memory: {stats.used_mb}/{stats.max_mb} MB")

# Force cleanup
manager.cleanup()
```

### 6.5 Profiling

```bash
# Enable profiling
export SAGE_PROFILING=true

# Run with profiling
sage get core --profile

# Output: timing breakdown for each operation
```

---

## Related

- [Quick Start](quickstart.md) — Basic usage guide
- [Troubleshooting](troubleshooting.md) — Common issues and solutions
- `docs/design/` — Design documents
- `docs/api/` — API reference

---

*Part of SAGE Knowledge Base - Advanced Usage Guide*
