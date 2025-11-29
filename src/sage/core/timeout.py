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

    Each level represents a different operation type with the appropriate timeout.
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
    enabled: bool = True


@dataclass
class FallbackConfig:
    """Fallback strategy configuration."""

    strategy: str = "graceful"  # graceful | strict | none
    cache_stale_ms: int = 60000  # Use stale cache up to 60 seconds

    # Action mappings for different scenarios
    timeout_short_action: str = "return_partial"
    timeout_long_action: str = "return_core"
    file_not_found_action: str = "return_error"
    parse_error_action: str = "return_raw"
    network_error_action: str = "use_cache"


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
        # suppress
        >>> breaker = CircuitBreaker()
        >>> if breaker.allow_request():
        ...     try:
        ...         result = await do_operation()
        ...         breaker.record_success()
        ...     except Exception as _:
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
        fallback_config: FallbackConfig | None = None,
    ) -> None:
        self.timeout_config = timeout_config or TimeoutConfig()
        self.circuit_breaker = CircuitBreaker(circuit_config)
        self.fallback_config = fallback_config or FallbackConfig()
        self._fallbacks: dict[str, Callable[[], Any]] = {}

    def register_fallback(self, key: str, fallback: Callable[[], Any]) -> None:
        """Register a fallback function for a specific key."""
        self._fallbacks[key] = fallback

    def get_fallback(self, key: str) -> Any | None:
        """Get fallback value for a key."""
        if key in self._fallbacks:
            return self._fallbacks[key]()
        return None

    def get_fallback_action(self, error_type: str) -> str:
        """
        Get the configured fallback action for a specific error type.

        Args:
            error_type: Type of error (timeout_short, timeout_long, file_not_found,
                       parse_error, network_error)

        Returns:
            Action string (return_partial, return_core, return_error, return_raw, use_cache)
        """
        action_map = {
            "timeout_short": self.fallback_config.timeout_short_action,
            "timeout_long": self.fallback_config.timeout_long_action,
            "file_not_found": self.fallback_config.file_not_found_action,
            "parse_error": self.fallback_config.parse_error_action,
            "network_error": self.fallback_config.network_error_action,
        }
        return action_map.get(error_type, "return_error")

    def get_fallback_strategy(self) -> str:
        """Get the configured fallback strategy (graceful, strict, none)."""
        return self.fallback_config.strategy

    def get_cache_stale_ms(self) -> int:
        """Get the maximum age of stale cache to use as fallback."""
        return self.fallback_config.cache_stale_ms

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
# Configuration Loading Helpers
# =============================================================================


def _parse_timeout_to_seconds(timeout_str: str | int | float) -> float:
    """
    Parse timeout string to seconds.

    Args:
        timeout_str: Timeout value as string (e.g., '5s', '500ms') or number.

    Returns:
        Timeout in seconds.
    """
    if isinstance(timeout_str, (int, float)):
        return float(timeout_str)
    timeout_str = str(timeout_str).strip().lower()
    if timeout_str.endswith("ms"):
        return float(timeout_str[:-2]) / 1000
    elif timeout_str.endswith("s"):
        return float(timeout_str[:-1])
    return float(timeout_str)


def _load_timeout_config_from_yaml() -> tuple[
    TimeoutConfig | None,
    CircuitBreakerConfig | None,
    FallbackConfig | None,
]:
    """
    Load timeout, circuit breaker, and fallback config from sage.yaml.

    Returns:
        Tuple of (TimeoutConfig, CircuitBreakerConfig, FallbackConfig) or None values.
    """
    try:
        from sage.core.config import load_config

        config = load_config()
        timeout_cfg = config.get("timeout", {})

        # Parse TimeoutConfig from operations
        ops = timeout_cfg.get("operations", {})
        timeout_config = TimeoutConfig(
            cache_ms=int(
                _parse_timeout_to_seconds(ops.get("cache_lookup", "100ms")) * 1000
            ),
            file_ms=int(
                _parse_timeout_to_seconds(ops.get("file_read", "500ms")) * 1000
            ),
            layer_ms=int(_parse_timeout_to_seconds(ops.get("layer_load", "2s")) * 1000),
            full_ms=int(_parse_timeout_to_seconds(ops.get("full_load", "5s")) * 1000),
            analysis_ms=int(
                _parse_timeout_to_seconds(ops.get("analysis", "10s")) * 1000
            ),
            mcp_ms=int(_parse_timeout_to_seconds(ops.get("mcp_call", "10s")) * 1000),
        )

        # Parse CircuitBreakerConfig
        cb_cfg = timeout_cfg.get("circuit_breaker", {})
        circuit_config = CircuitBreakerConfig(
            enabled=cb_cfg.get("enabled", True),
            failure_threshold=cb_cfg.get("failure_threshold", 3),
            reset_timeout_s=_parse_timeout_to_seconds(
                cb_cfg.get("reset_timeout", "30s")
            ),
            half_open_max_calls=cb_cfg.get("half_open_requests", 1),
        )

        # Parse FallbackConfig
        fb_cfg = timeout_cfg.get("fallback", {})
        fallback_config = FallbackConfig(
            strategy=fb_cfg.get("strategy", "graceful"),
            cache_stale_ms=fb_cfg.get("cache_stale_ms", 60000),
            timeout_short_action=fb_cfg.get("timeout_short", {}).get(
                "action", "return_partial"
            ),
            timeout_long_action=fb_cfg.get("timeout_long", {}).get(
                "action", "return_core"
            ),
            file_not_found_action=fb_cfg.get("file_not_found", {}).get(
                "action", "return_error"
            ),
            parse_error_action=fb_cfg.get("parse_error", {}).get(
                "action", "return_raw"
            ),
            network_error_action=fb_cfg.get("network_error", {}).get(
                "action", "use_cache"
            ),
        )

        return timeout_config, circuit_config, fallback_config

    except Exception as e:
        logger.warning(f"Failed to load timeout config from yaml: {e}")
        return None, None, None


# =============================================================================
# Global Instance
# =============================================================================

_default_manager: TimeoutManager | None = None


def get_timeout_manager() -> TimeoutManager:
    """
    Get the default timeout manager instance.

    Loads configuration from sage.yaml (config/timeout.yaml) including
    - Timeout levels (T1-T5)
    - Circuit breaker settings
    - Fallback strategies
    """
    global _default_manager
    if _default_manager is None:
        timeout_config, circuit_config, fallback_config = _load_timeout_config_from_yaml()
        _default_manager = TimeoutManager(
            timeout_config=timeout_config,
            circuit_config=circuit_config,
            fallback_config=fallback_config,
        )
    return _default_manager


def reset_timeout_manager() -> None:
    """Reset the default timeout manager (mainly for testing)."""
    global _default_manager
    _default_manager = None
