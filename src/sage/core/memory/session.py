"""Session continuity for cross-task persistence.

This module provides session state management, checkpoint/restore
functionality, and handoff packages for seamless task continuation.

Version: 0.1.0
"""

from __future__ import annotations

import json
import logging
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from sage.core.memory.store import MemoryEntry, MemoryStore
    from sage.core.memory.token_budget import TokenBudget

logger = logging.getLogger(__name__)


class SessionStatus(str, Enum):
    """Session lifecycle status."""

    ACTIVE = "active"  # Currently running
    PAUSED = "paused"  # Temporarily paused
    COMPLETED = "completed"  # Successfully finished
    HANDED_OFF = "handed_off"  # Transferred to new task
    FAILED = "failed"  # Terminated with error


@dataclass
class SessionState:
    """Complete session state for tracking and handoff.

    Captures all information needed to understand current progress
    and continue work in a new task.
    """

    session_id: str
    task_id: Optional[str] = None
    status: SessionStatus = SessionStatus.ACTIVE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    # Context
    current_objective: str = ""
    completed_steps: list[str] = field(default_factory=list)
    pending_steps: list[str] = field(default_factory=list)

    # Progress
    progress_percentage: float = 0.0
    last_action: str = ""
    last_result: str = ""

    # Memory references
    key_decisions: list[str] = field(default_factory=list)
    important_context: list[str] = field(default_factory=list)
    total_tokens_used: int = 0

    # Metadata
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        data = asdict(self)
        data["status"] = self.status.value
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SessionState:
        """Create from dictionary."""
        data = data.copy()
        data["status"] = SessionStatus(data["status"])
        data["created_at"] = datetime.fromisoformat(data["created_at"])
        data["updated_at"] = datetime.fromisoformat(data["updated_at"])
        return cls(**data)

    def calculate_progress(self) -> float:
        """Calculate progress based on completed/pending steps."""
        total = len(self.completed_steps) + len(self.pending_steps)
        if total == 0:
            return 0.0
        return len(self.completed_steps) / total


@dataclass
class HandoffPackage:
    """Package for session handoff to new task.

    Contains everything needed to continue work seamlessly
    in a new task/session.
    """

    session_state: SessionState
    summary: str  # AI-generated or auto-generated summary
    key_context: list[Any]  # Critical context entries (MemoryEntry)
    decisions: list[Any]  # Important decisions (MemoryEntry)
    continuation_prompt: str  # Prompt to continue work
    token_count: int

    def to_prompt(self) -> str:
        """Generate continuation prompt for new task.

        Returns:
            Formatted markdown prompt for continuing the work.
        """
        # Build list sections
        completed = "\n".join(
            f"- ✓ {step}" for step in self.session_state.completed_steps
        ) or "- (none yet)"

        pending = "\n".join(
            f"- {step}" for step in self.session_state.pending_steps
        ) or "- (none remaining)"

        decisions_text = "\n".join(
            f"- {d.content[:200]}..." if hasattr(d, 'content') and len(d.content) > 200
            else f"- {d.content}" if hasattr(d, 'content')
            else f"- {str(d)[:200]}"
            for d in self.decisions
        ) or "- (no key decisions recorded)"

        context_text = "\n".join(
            f"- {c.content[:200]}..." if hasattr(c, 'content') and len(c.content) > 200
            else f"- {c.content}" if hasattr(c, 'content')
            else f"- {str(c)[:200]}"
            for c in self.key_context
        ) or "- (no additional context)"

        return f"""## Session Continuation

### Previous Session Summary
{self.summary}

### Current Objective
{self.session_state.current_objective or "(no objective set)"}

### Completed Steps
{completed}

### Pending Steps
{pending}

### Key Decisions Made
{decisions_text}

### Important Context
{context_text}

### Last Action
{self.session_state.last_action or "(none)"}

### Last Result
{self.session_state.last_result or "(none)"}

---
**Progress**: {self.session_state.progress_percentage:.0f}% complete
**Token Budget Used**: {self.token_count:,} tokens
**Session ID**: {self.session_state.session_id}
"""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "session_state": self.session_state.to_dict(),
            "summary": self.summary,
            "key_context": [
                c.to_dict() if hasattr(c, 'to_dict') else str(c)
                for c in self.key_context
            ],
            "decisions": [
                d.to_dict() if hasattr(d, 'to_dict') else str(d)
                for d in self.decisions
            ],
            "continuation_prompt": self.continuation_prompt,
            "token_count": self.token_count,
        }


class SessionContinuity:
    """Service for managing session continuity.

    Provides checkpoint/restore functionality and handoff package
    generation for seamless cross-task continuation.

    Example:
        >>> store = MemoryStore()
        >>> budget = TokenBudget(store)
        >>> continuity = SessionContinuity(store, budget)
        >>>
        >>> # Start a new session
        >>> session = continuity.start_session(
        ...     objective="Implement feature X",
        ...     steps=["Design", "Implement", "Test"],
        ... )
        >>>
        >>> # Track progress
        >>> continuity.update_progress(
        ...     completed_step="Design",
        ...     last_action="Created design document",
        ... )
        >>>
        >>> # Prepare handoff when needed
        >>> handoff = continuity.prepare_handoff()
        >>> print(handoff.to_prompt())
    """

    def __init__(
        self,
        store: MemoryStore,
        budget: Optional[TokenBudget] = None,
    ) -> None:
        """Initialize the session continuity service.

        Args:
            store: Memory store for persistence.
            budget: Optional token budget controller.
        """
        self._store = store
        self._budget = budget
        self._current_session: Optional[SessionState] = None

    @property
    def current_session(self) -> Optional[SessionState]:
        """Get the current session state."""
        return self._current_session

    def start_session(
        self,
        objective: str,
        steps: Optional[list[str]] = None,
        task_id: Optional[str] = None,
        resume_from: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> SessionState:
        """Start a new session or resume from checkpoint.

        Args:
            objective: The main objective for this session.
            steps: List of planned steps.
            task_id: Optional task identifier.
            resume_from: Optional checkpoint ID to resume from.
            metadata: Optional additional metadata.

        Returns:
            The new or resumed session state.
        """
        if resume_from:
            # Resume from checkpoint
            session = self._restore_session(resume_from)
            if session:
                session.status = SessionStatus.ACTIVE
                session.updated_at = datetime.now()
                if objective:
                    session.current_objective = objective
                if steps:
                    # Merge new steps with pending
                    session.pending_steps = steps
                self._current_session = session
                logger.info(f"Resumed session from checkpoint: {resume_from}")
                return session

        # Create new session
        session = SessionState(
            session_id=str(uuid.uuid4()),
            task_id=task_id,
            current_objective=objective,
            pending_steps=steps or [],
            metadata=metadata or {},
        )

        self._current_session = session
        self._save_session_state()

        logger.info(f"Started new session: {session.session_id}")
        return session

    def _restore_session(self, checkpoint_id: str) -> Optional[SessionState]:
        """Restore session state from checkpoint."""
        checkpoints = self._store.list_checkpoints()
        checkpoint = next(
            (c for c in checkpoints if c["checkpoint_id"] == checkpoint_id),
            None
        )

        if not checkpoint:
            logger.warning(f"Checkpoint not found: {checkpoint_id}")
            return None

        # Load session state from checkpoint metadata
        checkpoint_path = (
            self._store._base_path / "checkpoints" / f"{checkpoint_id}.json"
        )

        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "session_state" in data:
                return SessionState.from_dict(data["session_state"])
            else:
                # Reconstruct from checkpoint data
                return SessionState(
                    session_id=data.get("session_id", str(uuid.uuid4())),
                )
        except (json.JSONDecodeError, OSError, KeyError) as e:
            logger.error(f"Failed to restore session from checkpoint: {e}")
            return None

    def _save_session_state(self) -> None:
        """Save current session state."""
        if not self._current_session:
            return

        from sage.core.memory.store import MemoryType, MemoryPriority

        # Store session state as a memory entry
        self._store.add(
            type=MemoryType.CHECKPOINT,
            content=json.dumps(self._current_session.to_dict()),
            priority=MemoryPriority.HIGH,
            session_id=self._current_session.session_id,
            tags=["session_state", "auto_checkpoint"],
            metadata={"is_session_state": True},
        )

    def update_progress(
        self,
        *,
        completed_step: Optional[str] = None,
        last_action: Optional[str] = None,
        last_result: Optional[str] = None,
        decision: Optional[str] = None,
        context: Optional[str] = None,
    ) -> Optional[SessionState]:
        """Update session progress.

        Args:
            completed_step: Step that was just completed.
            last_action: Description of last action taken.
            last_result: Result of last action.
            decision: Important decision made (will be recorded).
            context: Important context to remember.

        Returns:
            Updated session state, or None if no active session.
        """
        if not self._current_session:
            logger.warning("No active session to update")
            return None

        session = self._current_session
        session.updated_at = datetime.now()

        if completed_step:
            # Move from pending to completed
            if completed_step in session.pending_steps:
                session.pending_steps.remove(completed_step)
            if completed_step not in session.completed_steps:
                session.completed_steps.append(completed_step)

        if last_action:
            session.last_action = last_action

        if last_result:
            session.last_result = last_result

        # Record decision as memory entry
        if decision:
            from sage.core.memory.store import MemoryType, MemoryPriority

            entry = self._store.add(
                type=MemoryType.DECISION,
                content=decision,
                priority=MemoryPriority.HIGH,
                session_id=session.session_id,
                tags=["decision"],
            )
            session.key_decisions.append(entry.id)

        # Record context as memory entry
        if context:
            from sage.core.memory.store import MemoryType, MemoryPriority

            entry = self._store.add(
                type=MemoryType.CONTEXT,
                content=context,
                priority=MemoryPriority.NORMAL,
                session_id=session.session_id,
                tags=["context"],
            )
            session.important_context.append(entry.id)

        # Update progress percentage
        session.progress_percentage = session.calculate_progress() * 100

        # Update token count if budget available
        if self._budget:
            usage = self._budget.get_usage(session.session_id)
            session.total_tokens_used = usage.total_tokens

        logger.debug(
            f"Session progress updated: {session.progress_percentage:.0f}% "
            f"({len(session.completed_steps)}/{len(session.completed_steps) + len(session.pending_steps)} steps)"
        )

        return session

    def add_step(self, step: str) -> Optional[SessionState]:
        """Add a new step to the pending list.

        Args:
            step: Step description to add.

        Returns:
            Updated session state.
        """
        if not self._current_session:
            return None

        if step not in self._current_session.pending_steps:
            self._current_session.pending_steps.append(step)
            self._current_session.updated_at = datetime.now()

        return self._current_session

    def create_checkpoint(
        self,
        checkpoint_id: Optional[str] = None,
    ) -> str:
        """Create a checkpoint of the current session.

        Args:
            checkpoint_id: Optional custom checkpoint ID.

        Returns:
            The checkpoint ID.
        """
        if not self._current_session:
            raise RuntimeError("No active session to checkpoint")

        session = self._current_session

        # Create checkpoint in store
        cp_id = self._store.create_checkpoint(
            session_id=session.session_id,
            checkpoint_id=checkpoint_id,
        )

        # Also save session state in checkpoint
        checkpoint_path = self._store._base_path / "checkpoints" / f"{cp_id}.json"

        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            data["session_state"] = session.to_dict()

            with open(checkpoint_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"Failed to save session state to checkpoint: {e}")

        logger.info(f"Created checkpoint: {cp_id}")
        return cp_id

    def prepare_handoff(
        self,
        max_tokens: int = 4000,
        summary: Optional[str] = None,
    ) -> HandoffPackage:
        """Prepare a handoff package for task continuation.

        Args:
            max_tokens: Maximum tokens for the handoff package.
            summary: Optional pre-generated summary.

        Returns:
            HandoffPackage ready for new task.
        """
        if not self._current_session:
            raise RuntimeError("No active session for handoff")

        session = self._current_session
        from sage.core.memory.store import MemoryType, MemoryPriority

        # Get key decisions
        decisions = []
        for decision_id in session.key_decisions[-10:]:  # Last 10 decisions
            entry = self._store.get(decision_id)
            if entry:
                decisions.append(entry)

        # Get important context
        key_context = []
        for context_id in session.important_context[-10:]:  # Last 10 context items
            entry = self._store.get(context_id)
            if entry:
                key_context.append(entry)

        # Also get high-priority entries
        high_priority = self._store.query(
            session_id=session.session_id,
            min_priority=MemoryPriority.HIGH,
            limit=5,
        )
        for entry in high_priority:
            if entry not in key_context and entry not in decisions:
                key_context.append(entry)

        # Generate summary if not provided
        if not summary:
            summary = self._generate_summary(session, decisions, key_context)

        # Calculate token count
        token_count = session.total_tokens_used
        if self._budget:
            usage = self._budget.get_usage(session.session_id)
            token_count = usage.total_tokens

        # Update session status
        session.status = SessionStatus.HANDED_OFF
        session.updated_at = datetime.now()

        # Create handoff package
        handoff = HandoffPackage(
            session_state=session,
            summary=summary,
            key_context=key_context,
            decisions=decisions,
            continuation_prompt="",  # Will be set below
            token_count=token_count,
        )

        # Generate continuation prompt
        handoff.continuation_prompt = handoff.to_prompt()

        logger.info(
            f"Prepared handoff package for session: {session.session_id} "
            f"({len(decisions)} decisions, {len(key_context)} context items)"
        )

        return handoff

    def _generate_summary(
        self,
        session: SessionState,
        decisions: list[Any],
        context: list[Any],
    ) -> str:
        """Generate an auto-summary of the session.

        Args:
            session: Current session state.
            decisions: Key decisions made.
            context: Important context entries.

        Returns:
            Generated summary text.
        """
        parts = []

        parts.append(f"Session working on: {session.current_objective}")

        if session.completed_steps:
            parts.append(
                f"Completed {len(session.completed_steps)} of "
                f"{len(session.completed_steps) + len(session.pending_steps)} steps."
            )

        if decisions:
            parts.append(f"Made {len(decisions)} key decisions.")

        if session.last_action:
            parts.append(f"Last action: {session.last_action}")

        if session.last_result:
            parts.append(f"Last result: {session.last_result}")

        return " ".join(parts)

    def end_session(
        self,
        status: SessionStatus = SessionStatus.COMPLETED,
        final_result: Optional[str] = None,
    ) -> Optional[SessionState]:
        """End the current session.

        Args:
            status: Final session status.
            final_result: Optional final result description.

        Returns:
            Final session state.
        """
        if not self._current_session:
            return None

        session = self._current_session
        session.status = status
        session.updated_at = datetime.now()

        if final_result:
            session.last_result = final_result

        # Save final state
        self._save_session_state()

        logger.info(f"Session ended: {session.session_id} ({status.value})")

        self._current_session = None
        return session

    def get_session_summary(self) -> Optional[str]:
        """Get a summary of the current session.

        Returns:
            Formatted session summary, or None if no active session.
        """
        if not self._current_session:
            return None

        session = self._current_session

        status_icon = {
            SessionStatus.ACTIVE: "🟢",
            SessionStatus.PAUSED: "⏸️",
            SessionStatus.COMPLETED: "✅",
            SessionStatus.HANDED_OFF: "🔄",
            SessionStatus.FAILED: "❌",
        }

        lines = [
            f"## Session Summary {status_icon.get(session.status, '❓')}",
            "",
            f"**Session ID**: {session.session_id}",
            f"**Status**: {session.status.value}",
            f"**Objective**: {session.current_objective or '(not set)'}",
            f"**Progress**: {session.progress_percentage:.0f}%",
            "",
            f"**Completed**: {len(session.completed_steps)} steps",
            f"**Pending**: {len(session.pending_steps)} steps",
            f"**Decisions**: {len(session.key_decisions)}",
            f"**Tokens Used**: {session.total_tokens_used:,}",
        ]

        return "\n".join(lines)
