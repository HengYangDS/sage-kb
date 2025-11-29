"""Tests for sage.core.logging.config module."""

import pytest

from sage.core.logging.config import (
    LogLevel,
    LogFormat,
    configure_logging,
    get_default_processors,
    reset_logging,
)


class TestLogLevel:
    """Test cases for LogLevel enum."""

    def test_log_levels_exist(self) -> None:
        """Test that all expected log levels exist."""
        assert LogLevel.DEBUG == "DEBUG"
        assert LogLevel.INFO == "INFO"
        assert LogLevel.WARNING == "WARNING"
        assert LogLevel.ERROR == "ERROR"
        assert LogLevel.CRITICAL == "CRITICAL"

    def test_log_level_is_string_enum(self) -> None:
        """Test that LogLevel is a string enum."""
        assert isinstance(LogLevel.INFO, str)
        assert LogLevel.INFO.value == "INFO"


class TestLogFormat:
    """Test cases for LogFormat enum."""

    def test_log_formats_exist(self) -> None:
        """Test that all expected log formats exist."""
        assert LogFormat.CONSOLE == "console"
        assert LogFormat.JSON == "json"

    def test_log_format_is_string_enum(self) -> None:
        """Test that LogFormat is a string enum."""
        assert isinstance(LogFormat.CONSOLE, str)


class TestGetDefaultProcessors:
    """Test cases for get_default_processors function."""

    def test_returns_processors_for_console(self) -> None:
        """Test that processors are returned for console format."""
        processors = get_default_processors(LogFormat.CONSOLE)
        assert processors is not None
        assert len(processors) > 0

    def test_returns_processors_for_json(self) -> None:
        """Test that processors are returned for JSON format."""
        processors = get_default_processors(LogFormat.JSON)
        assert processors is not None
        assert len(processors) > 0

    def test_default_is_console(self) -> None:
        """Test that default format is console."""
        processors = get_default_processors()
        assert processors is not None


class TestConfigureLogging:
    """Test cases for configure_logging function."""

    def teardown_method(self) -> None:
        """Reset logging after each test."""
        reset_logging()

    def test_configure_with_defaults(self) -> None:
        """Test configuring logging with default settings."""
        # Should not raise any exceptions
        configure_logging()

    def test_configure_with_debug_level(self) -> None:
        """Test configuring logging with DEBUG level."""
        configure_logging(level=LogLevel.DEBUG)

    def test_configure_with_string_level(self) -> None:
        """Test configuring logging with string level."""
        configure_logging(level="DEBUG")

    def test_configure_with_json_format(self) -> None:
        """Test configuring logging with JSON format."""
        configure_logging(format_type=LogFormat.JSON)

    def test_configure_with_string_format(self) -> None:
        """Test configuring logging with string format."""
        configure_logging(format_type="json")

    def test_configure_without_cache(self) -> None:
        """Test configuring logging without logger caching."""
        configure_logging(cache_logger=False)


class TestResetLogging:
    """Test cases for reset_logging function."""

    def test_reset_does_not_raise(self) -> None:
        """Test that reset_logging does not raise exceptions."""
        configure_logging()
        reset_logging()  # Should not raise

    def test_reset_can_be_called_multiple_times(self) -> None:
        """Test that reset can be called multiple times safely."""
        reset_logging()
        reset_logging()
        reset_logging()
