"""Tests for sage.capabilities.monitors.health module."""

import pytest
import tempfile
from pathlib import Path

from sage.capabilities.monitors.health import (
    HealthMonitor,
    HealthCheck,
    HealthReport,
    HealthStatus,
    get_health_monitor,
)


class TestHealthStatus:
    """Test cases for HealthStatus enum."""

    def test_health_statuses_exist(self) -> None:
        """Test that expected health statuses exist."""
        assert HealthStatus.HEALTHY is not None
        assert HealthStatus.DEGRADED is not None
        assert HealthStatus.UNHEALTHY is not None
        assert HealthStatus.UNKNOWN is not None


class TestHealthCheck:
    """Test cases for HealthCheck class."""

    def test_check_creation(self) -> None:
        """Test that HealthCheck can be created."""
        check = HealthCheck(
            name="test_check",
            status=HealthStatus.HEALTHY,
            message="All good",
            duration_ms=10.0,
        )
        assert check.name == "test_check"
        assert check.status == HealthStatus.HEALTHY

    def test_check_to_dict(self) -> None:
        """Test converting check to dictionary."""
        check = HealthCheck(
            name="test_check",
            status=HealthStatus.HEALTHY,
            message="All good",
        )
        data = check.to_dict()
        assert data["name"] == "test_check"
        assert data["status"] == "healthy"
        assert "timestamp" in data


class TestHealthReport:
    """Test cases for HealthReport class."""

    def test_report_creation(self) -> None:
        """Test that HealthReport can be created."""
        checks = [
            HealthCheck(name="check1", status=HealthStatus.HEALTHY),
            HealthCheck(name="check2", status=HealthStatus.DEGRADED),
        ]
        report = HealthReport(
            overall_status=HealthStatus.DEGRADED,
            checks=checks,
            duration_ms=50.0,
        )
        assert report.overall_status == HealthStatus.DEGRADED
        assert len(report.checks) == 2

    def test_report_to_dict(self) -> None:
        """Test converting report to dictionary."""
        checks = [
            HealthCheck(name="check1", status=HealthStatus.HEALTHY),
        ]
        report = HealthReport(
            overall_status=HealthStatus.HEALTHY,
            checks=checks,
        )
        data = report.to_dict()
        assert data["overall_status"] == "healthy"
        assert "summary" in data
        assert data["summary"]["total"] == 1
        assert data["summary"]["healthy"] == 1


class TestHealthMonitor:
    """Test cases for HealthMonitor class."""

    def test_monitor_creation(self) -> None:
        """Test that HealthMonitor can be instantiated."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            assert monitor is not None

    @pytest.mark.asyncio
    async def test_check_filesystem(self) -> None:
        """Test filesystem health check."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            # Create some content
            (tmppath / "test.md").write_text("# Test")
            
            monitor = HealthMonitor(kb_path=tmppath)
            check = await monitor.check_filesystem()
            
            assert isinstance(check, HealthCheck)
            assert check.name == "filesystem"

    @pytest.mark.asyncio
    async def test_check_config(self) -> None:
        """Test config health check."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            check = await monitor.check_config()
            
            assert isinstance(check, HealthCheck)
            assert check.name == "config"

    @pytest.mark.asyncio
    async def test_check_all(self) -> None:
        """Test running all health checks."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            report = await monitor.check_all()
            
            assert isinstance(report, HealthReport)
            assert len(report.checks) > 0

    def test_register_alert_callback(self) -> None:
        """Test registering alert callback."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            
            alerts_received: list[HealthReport] = []
            
            def on_alert(report: HealthReport) -> None:
                alerts_received.append(report)
            
            monitor.register_alert_callback(on_alert)
            # Callback should be registered without error

    def test_get_history(self) -> None:
        """Test getting health check history."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            history = monitor.get_history()
            
            assert isinstance(history, list)

    def test_get_status_summary(self) -> None:
        """Test getting status summary."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = HealthMonitor(kb_path=Path(tmpdir))
            summary = monitor.get_status_summary()
            
            assert isinstance(summary, dict)


class TestGetHealthMonitor:
    """Test cases for get_health_monitor function."""

    def test_get_health_monitor_function(self) -> None:
        """Test the convenience function."""
        with tempfile.TemporaryDirectory() as tmpdir:
            monitor = get_health_monitor(kb_path=Path(tmpdir))
            assert isinstance(monitor, HealthMonitor)
