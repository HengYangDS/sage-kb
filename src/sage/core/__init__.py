"""
SAGE Core Layer.

Core infrastructure components:
- KnowledgeLoader: Knowledge loading with timeout protection
- Layer: Knowledge layer enumeration
- DI: Dependency Injection container with lifetime management
"""

from .di import (
    DIContainer,
    DIScope,
    Lifetime,
    TypeRegistry,
    get_container,
    get_registry,
)
from .loader import KnowledgeLoader, Layer

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
]
