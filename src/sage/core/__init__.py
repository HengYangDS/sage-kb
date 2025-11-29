"""
SAGE Core Layer.

Core infrastructure components:
- KnowledgeLoader: Knowledge loading with timeout protection
- Layer: Knowledge layer enumeration
- DI: Dependency Injection container with lifetime management
- Models: Data classes for SAGE protocol
- Protocols: SAGE protocol interfaces
- Exceptions: Structured exception hierarchy
- Config: Configuration management

Version: 0.1.0
"""

from .config import (
    CacheConfig,
    KnowledgeBaseConfig,
    LoggingConfig,
    MCPConfig,
    MemoryConfig,
    PluginConfig,
    SAGEConfig,
    TimeoutConfig,
    get_config,
    load_config,
    reset_config,
)
from .di import (
    DIContainer,
    DIScope,
    Lifetime,
    TypeRegistry,
    get_container,
    get_registry,
)
from .exceptions import (
    CLIError,
    ConfigError,
    ConfigNotFoundError,
    ConfigParseError,
    ContentNotFoundError,
    LoadError,
    MCPError,
    PluginError,
    PluginExecutionError,
    PluginLoadError,
    QueryError,
    SAGEError,
    SearchError,
    ServiceError,
    TimeoutError,
    ValidationError,
)
from .loader import KnowledgeLoader, Layer
from .models import (
    AnalysisRequest,
    AnalysisResult,
    CheckpointData,
    GenerateRequest,
    GenerateResult,
    LoadRequest,
    LoadResult,
    LoadStatus,
    MetricsSnapshot,
    SearchResult,
    SourceRequest,
    SourceResult,
)
from .protocols import (
    AnalyzeProtocol,
    EvolveProtocol,
    GenerateProtocol,
    SAGEProtocol,
    SourceProtocol,
)

__all__ = [
    # Loader
    "KnowledgeLoader",
    "Layer",
    # DI Container
    "DIContainer",
    "DIScope",
    "Lifetime",
    "get_container",
    "TypeRegistry",
    "get_registry",
    # Config
    "SAGEConfig",
    "TimeoutConfig",
    "CacheConfig",
    "LoggingConfig",
    "PluginConfig",
    "MemoryConfig",
    "MCPConfig",
    "KnowledgeBaseConfig",
    "get_config",
    "load_config",
    "reset_config",
    # Models
    "LoadRequest",
    "LoadResult",
    "LoadStatus",
    "SearchResult",
    "SourceRequest",
    "SourceResult",
    "AnalysisRequest",
    "AnalysisResult",
    "GenerateRequest",
    "GenerateResult",
    "MetricsSnapshot",
    "CheckpointData",
    # Protocols
    "SourceProtocol",
    "AnalyzeProtocol",
    "GenerateProtocol",
    "EvolveProtocol",
    "SAGEProtocol",
    # Exceptions
    "SAGEError",
    "LoadError",
    "TimeoutError",
    "ContentNotFoundError",
    "ValidationError",
    "SearchError",
    "QueryError",
    "ConfigError",
    "ConfigNotFoundError",
    "ConfigParseError",
    "PluginError",
    "PluginLoadError",
    "PluginExecutionError",
    "ServiceError",
    "MCPError",
    "CLIError",
]
