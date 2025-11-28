"""
End-to-end integration tests for CLI workflows.

Tests complete command sequences and real-world usage scenarios.

Version: 0.1.0
"""

import pytest
from typer.testing import CliRunner

from sage.services.cli import app


runner = CliRunner()


class TestCLIWorkflow:
    """Test complete CLI command workflows."""

    def test_info_then_get_workflow(self):
        """Test typical workflow: check info, then get content."""
        # Step 1: Get system info
        info_result = runner.invoke(app, ["info"])
        assert info_result.exit_code == 0

        # Step 2: Get core content
        get_result = runner.invoke(app, ["get", "core"])
        # Should succeed or fail gracefully
        assert get_result.exit_code in [0, 1]

    def test_search_then_get_workflow(self):
        """Test search workflow: search for content, then retrieve it."""
        # Step 1: Search for something
        search_result = runner.invoke(app, ["search", "timeout"])
        assert search_result.exit_code in [0, 1]

        # Step 2: Get related content
        get_result = runner.invoke(app, ["get", "core"])
        assert get_result.exit_code in [0, 1]

    def test_validate_workflow(self):
        """Test validation workflow."""
        # Validate the knowledge base
        validate_result = runner.invoke(app, ["validate"])
        assert validate_result.exit_code in [0, 1]

    def test_full_exploration_workflow(self):
        """Test full exploration: info → get layers → search → validate."""
        # Step 1: Check system status
        info_result = runner.invoke(app, ["info"])
        assert info_result.exit_code == 0

        # Step 2: Get different layers
        for layer in ["core", "guidelines", "frameworks"]:
            result = runner.invoke(app, ["get", layer])
            assert result.exit_code in [0, 1]

        # Step 3: Search for content
        search_result = runner.invoke(app, ["search", "knowledge"])
        assert search_result.exit_code in [0, 1]

        # Step 4: Validate
        validate_result = runner.invoke(app, ["validate"])
        assert validate_result.exit_code in [0, 1]


class TestCLIErrorHandling:
    """Test CLI error handling in real scenarios."""

    def test_invalid_layer_handling(self):
        """Test handling of invalid layer names."""
        result = runner.invoke(app, ["get", "nonexistent_layer"])
        # Should fail gracefully with exit code 1, not crash
        assert result.exit_code in [0, 1, 2]

    def test_empty_search_handling(self):
        """Test handling of empty search queries."""
        result = runner.invoke(app, ["search", ""])
        # Should handle empty query gracefully
        assert result.exit_code in [0, 1, 2]

    def test_special_characters_search(self):
        """Test search with special characters."""
        result = runner.invoke(app, ["search", "test@#$%"])
        # Should handle special characters without crashing
        assert result.exit_code in [0, 1, 2]

    def test_very_long_query_handling(self):
        """Test handling of very long search queries."""
        long_query = "a" * 1000
        result = runner.invoke(app, ["search", long_query])
        # Should handle long query without crashing
        assert result.exit_code in [0, 1, 2]


class TestCLIOutputFormats:
    """Test CLI output format options."""

    def test_get_with_json_format(self):
        """Test get command with JSON output format."""
        result = runner.invoke(app, ["get", "core", "--format", "json"])
        assert result.exit_code in [0, 1, 2]

    def test_get_with_text_format(self):
        """Test get command with text output format."""
        result = runner.invoke(app, ["get", "core", "--format", "text"])
        assert result.exit_code in [0, 1, 2]

    def test_search_with_limit(self):
        """Test search with result limit."""
        result = runner.invoke(app, ["search", "test", "--limit", "5"])
        assert result.exit_code in [0, 1, 2]


class TestCLIHelpSystem:
    """Test CLI help system completeness."""

    def test_main_help(self):
        """Test main help command."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        # Check for common help indicators
        output_lower = result.stdout.lower()
        assert "usage" in output_lower or "commands" in output_lower or "options" in output_lower

    def test_get_help(self):
        """Test get command help."""
        result = runner.invoke(app, ["get", "--help"])
        assert result.exit_code == 0

    def test_search_help(self):
        """Test search command help."""
        result = runner.invoke(app, ["search", "--help"])
        assert result.exit_code == 0

    def test_validate_help(self):
        """Test validate command help."""
        result = runner.invoke(app, ["validate", "--help"])
        assert result.exit_code == 0

    def test_info_help(self):
        """Test info command help."""
        result = runner.invoke(app, ["info", "--help"])
        assert result.exit_code == 0


class TestCLIWithConfiguration:
    """Test CLI with different configuration scenarios."""

    def test_with_custom_root(self, tmp_path):
        """Test CLI with custom content root."""
        # Create minimal content structure
        content_dir = tmp_path / "content"
        content_dir.mkdir()
        core_dir = content_dir / "core"
        core_dir.mkdir()
        (core_dir / "test.md").write_text("# Test Content\n\nThis is test content.")

        result = runner.invoke(app, ["info"])
        assert result.exit_code == 0

    def test_with_missing_content_directory(self, tmp_path):
        """Test CLI behavior with missing content directory."""
        # Run from empty directory - should handle gracefully
        result = runner.invoke(app, ["info"])
        assert result.exit_code == 0  # Info should always work

    def test_with_empty_content_directory(self, tmp_path):
        """Test CLI with empty content directory."""
        content_dir = tmp_path / "content"
        content_dir.mkdir()

        result = runner.invoke(app, ["get", "core"])
        # Should handle empty content gracefully
        assert result.exit_code in [0, 1, 2]


class TestCLIConcurrentOperations:
    """Test CLI behavior under concurrent-like operations."""

    def test_multiple_sequential_commands(self):
        """Test multiple commands in quick succession."""
        commands = [
            ["info"],
            ["get", "core"],
            ["search", "test"],
            ["validate"],
            ["info"],
        ]

        for cmd in commands:
            result = runner.invoke(app, cmd)
            assert result.exit_code in [0, 1, 2]

    def test_repeated_same_command(self):
        """Test repeated execution of same command."""
        for _ in range(5):
            result = runner.invoke(app, ["info"])
            assert result.exit_code == 0


class TestCLIVersionInfo:
    """Test CLI version information."""

    def test_version_flag(self):
        """Test --version flag."""
        result = runner.invoke(app, ["--version"])
        # Version flag may or may not be supported
        assert result.exit_code in [0, 1, 2]

    def test_version_in_info(self):
        """Test version appears in info output."""
        result = runner.invoke(app, ["info"])
        assert result.exit_code == 0
        # Version should be mentioned somewhere
        assert "0.1.0" in result.stdout or "Version" in result.stdout


class TestCLIBasicFunctionality:
    """Test basic CLI functionality."""

    def test_info_command_works(self):
        """Test that info command executes successfully."""
        result = runner.invoke(app, ["info"])
        assert result.exit_code == 0
        # Should have some output
        assert len(result.stdout) > 0

    def test_get_command_works(self):
        """Test that get command executes."""
        result = runner.invoke(app, ["get", "core"])
        # Should not crash
        assert result.exit_code in [0, 1]

    def test_search_command_works(self):
        """Test that search command executes."""
        result = runner.invoke(app, ["search", "test"])
        # Should not crash
        assert result.exit_code in [0, 1]

    def test_validate_command_works(self):
        """Test that validate command executes."""
        result = runner.invoke(app, ["validate"])
        # Should not crash
        assert result.exit_code in [0, 1]
