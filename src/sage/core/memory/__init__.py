"""Memory persistence system for cross-task continuity.

This module provides persistent memory storage, token budget management,
and session continuity for seamless task handoff.

Components:
    - MemoryStore: Persistent storage with priority-based retention
    - TokenBudget: Token usage tracking with automatic actions
    - SessionContinuity: Session management with checkpoint/restore

Example:
    >>> from sage.core.memory import (
    ...     MemoryStore, MemoryEntry, MemoryType, MemoryPriority,
    ...     TokenBudget, TokenBudgetConfig, TokenWarningLevel,
    ...     SessionContinuity, SessionState, HandoffPackage,
    ... )
    >>>
    >>> # Initialize components
    >>> store = MemoryStore()
    >>> budget = TokenBudget(store, TokenBudgetConfig(max_tokens=128000))
    >>> continuity = SessionContinuity(store, budget)
    >>>
    >>> # Start a session
    >>> session = continuity.start_session(
    ...     objective="Implement feature X",
    ...     steps=["Design", "Implement", "Test"],
    ... )
    >>>
    >>> # Track progress
    >>> continuity.update_progress(
    ...     completed_step="Design",
    ...     decision="Use Protocol-based interfaces",
    ... )
    >>>
    >>> # Check token budget
    >>> usage = budget.get_usage(session.session_id)
    >>> print(f"Token usage: {usage.used_percentage:.1%}")
    >>>
    >>> # Prepare handoff when needed
    >>> if usage.level.value in ("warning", "critical"):
    ...     handoff = continuity.prepare_handoff()
    ...     print(handoff.to_prompt())

Version: 0.1.0
"""

from sage.core.memory.session import (
    HandoffPackage,
    SessionContinuity,
    SessionState,
    SessionStatus,
)
from sage.core.memory.store import (
    MemoryEntry,
    MemoryPriority,
    MemoryStore,
    MemoryType,
)
from sage.core.memory.token_budget import (
    TokenBudget,
    TokenBudgetConfig,
    TokenUsage,
    TokenWarningLevel,
)

__all__ = [
    # Store
    "MemoryStore",
    "MemoryEntry",
    "MemoryType",
    "MemoryPriority",
    # Token Budget
    "TokenBudget",
    "TokenBudgetConfig",
    "TokenUsage",
    "TokenWarningLevel",
    # Session
    "SessionContinuity",
    "SessionState",
    "SessionStatus",
    "HandoffPackage",
]
