"""
SAGE Timeout Management.

Production-grade timeout handling with circuit breaker pattern.

Features:
- 5-level timeout hierarchy (T1-T5)
- Circuit breaker pattern for fault tolerance
- Graceful degradation strategies
- Configurable timeout settings

Version: 0.1.0

Timeout Hierarchy:
    T1_CACHE (100ms)    - Cache lookup
    T2_FILE (500ms)     - Single file read
    T3_LAYER (2s)       - Layer load
    T4_FULL (5s)        - Full KB load
    T5_ANALYSIS (10s)   - Complex analysis
"""

import asyncio
import logging
import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from typing import Any, Generic, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


class TimeoutLevel(Enum):
    """
    5-level timeout hierarchy.

    Each level represents a different operation type with appropriate timeout.
    """

    T1_CACHE = 1  # 100 ms - Cache lookup
    T2_FILE = 2  # 500 ms - Single file read
    T3_LAYER = 3  # 2 s - Layer load
    T4_FULL = 4  # 5 s - Full KB load
    T5_ANALYSIS = 5  # 10 s - Complex analysis


class CircuitState(Enum):
    """Circuit breaker states."""

    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing recovery


@dataclass
class TimeoutConfig:
    """
    Configurable timeout settings.

    All values in milliseconds.
    """

    cache_ms: int = 100
    file_ms: int = 500
    layer_ms: int = 2000
    full_ms: int = 5000
    analysis_ms: int = 10000
    mcp_ms: int = 10000

    def get_timeout(self, level: TimeoutLevel) -> float:
        """Get timeout in seconds for a given level."""
        mapping = {
            TimeoutLevel.T1_CACHE: self.cache_ms,
            TimeoutLevel.T2_FILE: self.file_ms,
            TimeoutLevel.T3_LAYER: self.layer_ms,
            TimeoutLevel.T4_FULL: self.full_ms,
            TimeoutLevel.T5_ANALYSIS: self.analysis_ms,
        }
        return mapping.get(level, self.full_ms) / 1000

    def get_timeout_ms(self, level: TimeoutLevel) -> int:
        """Get timeout in milliseconds for a given level."""
        return int(self.get_timeout(level) * 1000)


@dataclass
class CircuitBreakerConfig:
    """Circuit breaker configuration."""

    failure_threshold: int = 3
    reset_timeout_s: float = 30.0
    half_open_max_calls: int = 1


@dataclass
class TimeoutResult(Generic[T]):
    """
    Result of a timeout-protected operation.

    Attributes:
        success: Whether the operation succeeded
        value: The result value (if successful)
        error: Error message (if failed)
        duration_ms: Actual execution time
        timeout_ms: Configured timeout
        partial: Whether result is partial
        fallback_used: Whether fallback was used
    """

    success: bool
    value: T | None = None
    error: str | None = None
    duration_ms: int = 0
    timeout_ms: int = 0
    partial: bool = False
    fallback_used: bool = False

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "success": self.success,
            "value": self.value,
            "error": self.error,
            "duration_ms": self.duration_ms,
            "timeout_ms": self.timeout_ms,
            "partial": self.partial,
            "fallback_used": self.fallback_used,
        }


class CircuitBreaker:
    """
    Circuit breaker for fault tolerance.

    States:
    - CLOSED: Normal operation, requests pass through
    - OPEN: Too many failures, requests are rejected immediately
    - HALF_OPEN: Testing if service recovered

    Example:
        >>> breaker = CircuitBreaker()
        >>> if breaker.allow_request():
        ...     try:
        ...         result = await do_operation()
        ...         breaker.record_success()
        ...     except Exception:
        ...         breaker.record_failure()
    """

    def __init__(self, config: CircuitBreakerConfig | None = None) -> None:
        self.config = config or CircuitBreakerConfig()
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time: float | None = None
        self._half_open_calls = 0

    @property
    def state(self) -> CircuitState:
        """Get the current circuit state, checking for auto reset."""
        if self._state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self._state = CircuitState.HALF_OPEN
                self._half_open_calls = 0
        return self._state

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        if self._last_failure_time is None:
            return True
        elapsed = time.monotonic() - self._last_failure_time
        return elapsed >= self.config.reset_timeout_s

    def record_success(self) -> None:
        """Record a successful call."""
        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.CLOSED
            logger.info("Circuit breaker closed after successful recovery")
        self._failure_count = 0

    def record_failure(self) -> None:
        """Record a failed call."""
        self._failure_count += 1
        self._last_failure_time = time.monotonic()

        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.OPEN
            logger.warning("Circuit breaker opened after half-open failure")
        elif self._failure_count >= self.config.failure_threshold:
            self._state = CircuitState.OPEN
            logger.warning(
                f"Circuit breaker opened after {self._failure_count} failures"
            )

    def allow_request(self) -> bool:
        """Check if a request should be allowed."""
        state = self.state  # This may trigger state transition

        if state == CircuitState.CLOSED:
            return True
        elif state == CircuitState.OPEN:
            return False
        else:  # HALF_OPEN
            if self._half_open_calls < self.config.half_open_max_calls:
                self._half_open_calls += 1
                return True
            return False

    def reset(self) -> None:
        """Manually reset the circuit breaker."""
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time = None
        self._half_open_calls = 0


class TimeoutManager:
    """
    Production-grade timeout manager with circuit breaker support.

    Features:
    - 5-level timeout hierarchy
    - Circuit breaker for fault tolerance
    - Graceful degradation with fallbacks
    - Configurable settings

    Example:
        >>> manager = TimeoutManager()
        >>> result = await manager.execute_with_timeout(
        ...     load_content(),
        ...     TimeoutLevel.T3_LAYER,
        ...     fallback_key="default_content"
        ... )
        >>> if result.success:
        ...     print(result.value)
    """

    def __init__(
        self,
        timeout_config: TimeoutConfig | None = None,
        circuit_config: CircuitBreakerConfig | None = None,
    ) -> None:
        self.timeout_config = timeout_config or TimeoutConfig()
        self.circuit_breaker = CircuitBreaker(circuit_config)
        self._fallbacks: dict[str, Callable[[], Any]] = {}

    def register_fallback(self, key: str, fallback: Callable[[], Any]) -> None:
        """Register a fallback function for a specific key."""
        self._fallbacks[key] = fallback

    def get_fallback(self, key: str) -> Any | None:
        """Get fallback value for a key."""
        if key in self._fallbacks:
            return self._fallbacks[key]()
        return None

    async def execute_with_timeout(
        self,
        coro: Any,
        level: TimeoutLevel,
        fallback_key: str | None = None,
        timeout_ms: int | None = None,
    ) -> TimeoutResult[Any]:
        """
        Execute a coroutine with timeout protection.

        Args:
            coro: Coroutine to execute
            level: Timeout level (T1-T5)
            fallback_key: Key for fallback value if timeout
            timeout_ms: Override timeout in milliseconds

        Returns:
            TimeoutResult with success status, value and metadata
        """
        # Check circuit breaker
        if not self.circuit_breaker.allow_request():
            logger.warning("Circuit breaker open, using fallback")
            # Close the coroutine to prevent "coroutine never awaited" warning
            if hasattr(coro, "close"):
                coro.close()
            fallback = self.get_fallback(fallback_key) if fallback_key else None
            return TimeoutResult(
                success=False,
                value=fallback,
                error="Circuit breaker open",
                fallback_used=fallback is not None,
            )

        # Calculate timeout
        if timeout_ms is not None:
            timeout_s = timeout_ms / 1000
        else:
            timeout_s = self.timeout_config.get_timeout(level)

        timeout_ms_actual = int(timeout_s * 1000)
        start_time = time.monotonic()

        try:
            result = await asyncio.wait_for(coro, timeout=timeout_s)
            duration_ms = int((time.monotonic() - start_time) * 1000)

            self.circuit_breaker.record_success()

            return TimeoutResult(
                success=True,
                value=result,
                duration_ms=duration_ms,
                timeout_ms=timeout_ms_actual,
            )

        except TimeoutError:
            duration_ms = int((time.monotonic() - start_time) * 1000)
            self.circuit_breaker.record_failure()

            # Try fallback
            fallback = self.get_fallback(fallback_key) if fallback_key else None

            logger.warning(
                f"Timeout after {duration_ms}ms (limit: {timeout_ms_actual}ms)"
            )

            return TimeoutResult(
                success=False,
                value=fallback,
                error=f"Timeout after {duration_ms}ms",
                duration_ms=duration_ms,
                timeout_ms=timeout_ms_actual,
                fallback_used=fallback is not None,
            )

        except Exception as e:
            duration_ms = int((time.monotonic() - start_time) * 1000)
            self.circuit_breaker.record_failure()

            logger.error(f"Error during execution: {e}")

            return TimeoutResult(
                success=False,
                error=str(e),
                duration_ms=duration_ms,
                timeout_ms=timeout_ms_actual,
            )

    def timeout_decorator(
        self,
        level: TimeoutLevel,
        fallback_key: str | None = None,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        Decorator for adding timeout protection to async functions.

        Usage:
            @timeout_manager.timeout_decorator(TimeoutLevel.T2_FILE)
            async def load_file(path: str) -> str:
                ...
        """

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            async def wrapper(*args: Any, **kwargs: Any) -> TimeoutResult[Any]:
                return await self.execute_with_timeout(
                    func(*args, **kwargs), level, fallback_key
                )

            return wrapper

        return decorator


# =============================================================================
# Global Instance
# =============================================================================

_default_manager: TimeoutManager | None = None


def get_timeout_manager() -> TimeoutManager:
    """Get the default timeout manager instance."""
    global _default_manager
    if _default_manager is None:
        _default_manager = TimeoutManager()
    return _default_manager


def reset_timeout_manager() -> None:
    """Reset the default timeout manager (mainly for testing)."""
    global _default_manager
    _default_manager = None
