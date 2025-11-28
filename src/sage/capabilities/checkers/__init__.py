"""
Checkers Capabilities.

Provides checking capabilities that can be exposed via MCP/API:
- LinkChecker: Check for broken links in content
"""

from ai_collab_kb.capabilities.checkers.links import LinkChecker

__all__ = [
    "LinkChecker",
]
