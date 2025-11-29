"""
SAGE Domain Package.

Business domain models for the knowledge base system.
Contains knowledge assets, collaboration sessions, and related entities.

Version: 0.1.0
"""

from sage.domain.knowledge import (
    AssetStatus,
    ContentType,
    KnowledgeAsset,
    KnowledgeCycle,
    KnowledgeIndex,
    KnowledgeLayer,
    KnowledgeMetadata,
)
from sage.domain.session import (
    AutonomyLevel,
    CollaborationSession,
    HandoffPackage,
    Interaction,
    InteractionType,
    SessionContext,
    SessionStatus,
)

__all__ = [
    # Knowledge domain
    "KnowledgeLayer",
    "ContentType",
    "AssetStatus",
    "KnowledgeMetadata",
    "KnowledgeAsset",
    "KnowledgeCycle",
    "KnowledgeIndex",
    # Session domain
    "SessionStatus",
    "InteractionType",
    "AutonomyLevel",
    "Interaction",
    "SessionContext",
    "CollaborationSession",
    "HandoffPackage",
]
