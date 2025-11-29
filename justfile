# SAGE Knowledge Base - Just Commands
# Cross-platform task runner (https://just.systems)

# Default recipe: show available commands
default:
    @just --list

# =============================================================================
# Development
# =============================================================================

# Install all dependencies
install:
    pip install -e ".[all]"

# Install development dependencies only
install-dev:
    pip install -e ".[dev]"

# Run pre-commit hooks on all files
lint:
    pre-commit run --all-files

# Run ruff check and fix
check:
    ruff check --fix src/

# Format code with ruff
format:
    ruff format src/

# Run type checking with mypy
typecheck:
    mypy src/

# =============================================================================
# Testing
# =============================================================================

# Run all tests
test:
    pytest

# Run tests with coverage
test-cov:
    pytest --cov=src --cov-report=html

# Run specific test file
test-file FILE:
    pytest {{FILE}} -v

# =============================================================================
# Knowledge Base
# =============================================================================

# Show knowledge base info
info:
    sage info

# Get core knowledge
get-core:
    sage get core

# Search knowledge base
search QUERY:
    sage search "{{QUERY}}"

# Start MCP server
serve:
    sage serve

# =============================================================================
# Documentation
# =============================================================================

# Validate knowledge documents
validate:
    python tools/validate_knowledge.py

# =============================================================================
# Cleanup
# =============================================================================

# Clean build artifacts
clean:
    rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/

# Clean all generated files
clean-all: clean
    rm -rf .logs/* .outputs/*
