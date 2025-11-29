"""Tests for sage.capabilities.analyzers.content module."""

import pytest
import tempfile
from pathlib import Path

from sage.capabilities.analyzers.content import (
    ContentAnalyzer,
    ContentMetrics,
    analyze_content,
)


class TestContentMetrics:
    """Test cases for ContentMetrics class."""

    def test_metrics_creation(self) -> None:
        """Test that ContentMetrics can be created."""
        metrics = ContentMetrics(
            file_path="test.md",
            total_lines=100,
            total_chars=5000,
            estimated_tokens=500,
            header_count=10,
            code_block_count=5,
            table_count=2,
            link_count=15,
        )
        assert metrics.total_lines == 100
        assert metrics.header_count == 10

    def test_efficiency_score(self) -> None:
        """Test efficiency score calculation."""
        metrics = ContentMetrics(
            file_path="test.md",
            total_lines=100,
            estimated_tokens=500,
            tokens_per_section=100,
        )
        score = metrics.efficiency_score
        assert 0 <= score <= 100

    def test_to_dict(self) -> None:
        """Test converting metrics to dictionary."""
        metrics = ContentMetrics(
            file_path="test.md",
            total_lines=100,
            total_chars=5000,
            estimated_tokens=500,
            header_count=10,
        )
        data = metrics.to_dict()
        assert data["file_path"] == "test.md"
        assert data["basic"]["lines"] == 100
        assert "efficiency" in data


class TestContentAnalyzer:
    """Test cases for ContentAnalyzer class."""

    def test_analyzer_creation(self) -> None:
        """Test that ContentAnalyzer can be instantiated."""
        analyzer = ContentAnalyzer()
        assert analyzer is not None

    def test_analyze_content_basic(self) -> None:
        """Test analyzing basic markdown content."""
        analyzer = ContentAnalyzer()
        content = """# Title

This is a paragraph.

## Section 1

Some content here.

```python
print("hello")
```
"""
        metrics = analyzer.analyze_content(content, "test.md")
        assert metrics is not None
        assert metrics.header_count > 0
        assert metrics.code_block_count > 0

    def test_analyze_content_with_tables(self) -> None:
        """Test analyzing content with tables."""
        analyzer = ContentAnalyzer()
        content = """# Table Example

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""
        metrics = analyzer.analyze_content(content, "test.md")
        assert metrics.table_count > 0

    def test_analyze_file(self) -> None:
        """Test analyzing a file."""
        analyzer = ContentAnalyzer()
        
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False
        ) as f:
            f.write("# Test\n\nContent here.")
            f.flush()
            
            metrics = analyzer.analyze_file(Path(f.name))
            assert metrics is not None
            assert metrics.header_count >= 1

    def test_analyze_directory(self) -> None:
        """Test analyzing a directory."""
        analyzer = ContentAnalyzer()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            (Path(tmpdir) / "test1.md").write_text("# File 1\n\nContent.")
            (Path(tmpdir) / "test2.md").write_text("# File 2\n\nMore content.")
            
            metrics_list = analyzer.analyze_directory(Path(tmpdir))
            assert len(metrics_list) >= 2

    def test_estimate_tokens(self) -> None:
        """Test token estimation."""
        analyzer = ContentAnalyzer()
        text = "This is a test sentence with some words."
        tokens = analyzer.estimate_tokens(text)
        assert tokens > 0

    def test_suggest_optimizations(self) -> None:
        """Test optimization suggestions."""
        analyzer = ContentAnalyzer()
        metrics = ContentMetrics(
            file_path="test.md",
            total_lines=1000,
            total_chars=50000,
            estimated_tokens=5000,
            header_count=1,
            tokens_per_section=5000,
        )
        suggestions = analyzer.suggest_optimizations(metrics)
        assert isinstance(suggestions, list)


class TestAnalyzeContentFunction:
    """Test cases for analyze_content convenience function."""

    def test_analyze_content_function(self) -> None:
        """Test the convenience function."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False
        ) as f:
            f.write("# Test\n\nContent here.")
            f.flush()
            
            metrics = analyze_content(Path(f.name))
            assert metrics is not None
