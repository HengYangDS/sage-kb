"""Tests for sage.capabilities.checkers.links module."""

import tempfile
from pathlib import Path

from sage.capabilities.checkers.links import (
    LinkChecker,
    LinkReport,
    LinkResult,
    LinkStatus,
    LinkType,
    check_links,
)


class TestLinkType:
    """Test cases for LinkType enum."""

    def test_link_types_exist(self) -> None:
        """Test that expected link types exist."""
        assert LinkType.INTERNAL is not None
        assert LinkType.EXTERNAL is not None
        assert LinkType.ANCHOR is not None


class TestLinkStatus:
    """Test cases for LinkStatus enum."""

    def test_link_statuses_exist(self) -> None:
        """Test that expected link statuses exist."""
        assert LinkStatus.VALID is not None
        assert LinkStatus.BROKEN is not None
        assert LinkStatus.WARNING is not None
        assert LinkStatus.SKIPPED is not None


class TestLinkResult:
    """Test cases for LinkResult class."""

    def test_result_to_dict(self) -> None:
        """Test converting result to dictionary."""
        result = LinkResult(
            source_file="test.md",
            line_number=10,
            link_text="Test Link",
            link_target="./other.md",
            link_type=LinkType.INTERNAL,
            status=LinkStatus.VALID,
        )
        data = result.to_dict()
        assert data["source_file"] == "test.md"
        assert data["line_number"] == 10


class TestLinkReport:
    """Test cases for LinkReport class."""

    def test_broken_rate_calculation(self) -> None:
        """Test broken link rate calculation."""
        report = LinkReport(
            total_links=100,
            valid_count=90,
            broken_count=10,
            warning_count=0,
            skipped_count=0,
            results=[],
            files_checked=5,
            duration_ms=100.0,
        )
        rate = report.broken_rate
        assert rate == 10.0  # 10% as percentage

    def test_broken_rate_zero_total(self) -> None:
        """Test broken rate with zero total links."""
        report = LinkReport(
            total_links=0,
            valid_count=0,
            broken_count=0,
            warning_count=0,
            skipped_count=0,
            results=[],
            files_checked=0,
            duration_ms=0.0,
        )
        rate = report.broken_rate
        assert rate == 0.0

    def test_report_to_dict(self) -> None:
        """Test converting report to dictionary."""
        report = LinkReport(
            total_links=10,
            valid_count=8,
            broken_count=2,
            warning_count=0,
            skipped_count=0,
            results=[],
            files_checked=3,
            duration_ms=50.0,
        )
        data = report.to_dict()
        assert data["total_links"] == 10
        assert "broken_rate" in data


class TestLinkChecker:
    """Test cases for LinkChecker class."""

    def test_checker_creation(self) -> None:
        """Test that LinkChecker can be instantiated."""
        with tempfile.TemporaryDirectory() as tmpdir:
            checker = LinkChecker(kb_path=Path(tmpdir))
            assert checker is not None

    def test_check_file_with_valid_links(self) -> None:
        """Test checking a file with valid internal links."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create target file
            (tmppath / "target.md").write_text("# Target\n\nContent.")

            # Create source file with link to target
            source = tmppath / "source.md"
            source.write_text("# Source\n\nLink to [target](./target.md).")

            checker = LinkChecker(kb_path=tmppath)
            results = checker.check_file(source)

            assert isinstance(results, list)

    def test_check_file_with_broken_links(self) -> None:
        """Test checking a file with broken links."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create source file with broken link
            source = tmppath / "source.md"
            source.write_text("# Source\n\nLink to [missing](./missing.md).")

            checker = LinkChecker(kb_path=tmppath)
            results = checker.check_file(source)

            # Should find the broken link
            broken = [r for r in results if r.status == LinkStatus.BROKEN]
            assert len(broken) >= 1

    def test_check_all(self) -> None:
        """Test checking all files in directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create test files
            (tmppath / "file1.md").write_text("# File 1\n\nNo links.")
            (tmppath / "file2.md").write_text("# File 2\n\nNo links.")

            checker = LinkChecker(kb_path=tmppath)
            report = checker.check_all()

            assert isinstance(report, LinkReport)

    def test_get_broken_links(self) -> None:
        """Test getting only broken links."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create file with broken link
            (tmppath / "test.md").write_text("[broken](./missing.md)")

            checker = LinkChecker(kb_path=tmppath)
            checker.check_all()
            broken = checker.get_broken_links()

            assert isinstance(broken, list)

    def test_clear_cache(self) -> None:
        """Test clearing the checker cache."""
        with tempfile.TemporaryDirectory() as tmpdir:
            checker = LinkChecker(kb_path=Path(tmpdir))
            checker.clear_cache()  # Should not raise


class TestCheckLinksFunction:
    """Test cases for check_links convenience function."""

    def test_check_links_function(self) -> None:
        """Test the convenience function."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "test.md").write_text("# Test\n\nNo links.")

            report = check_links(kb_path=tmppath)
            assert isinstance(report, LinkReport)
