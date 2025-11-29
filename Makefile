.PHONY: help install dev test test-unit test-integration lint format serve clean \
        validate validate-format validate-links validate-arch validate-index \
        new-adr new-convention new-practice new-guide index check-all

# Default target
help:  ## Show all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation
install:  ## Install production dependencies
	pip install -e .

dev:  ## Install dev dependencies + pre-commit
	pip install -e ".[dev]"
	@if [ -f .pre-commit-config.yaml ]; then pre-commit install; fi

# Testing
test:  ## Run all tests with coverage
	pytest tests/ -v --cov=sage --cov-report=term-missing

test-unit:  ## Run unit tests only
	pytest tests/unit/ -v -m unit

test-integration:  ## Run integration tests only
	pytest tests/integration/ -v -m integration

test-fast:  ## Run tests in parallel (requires pytest-xdist)
	pytest tests/ -v -n auto

# Code Quality
lint:  ## Run ruff + mypy
	ruff check src/ tests/
	mypy src/

format:  ## Format code with ruff
	ruff format src/ tests/
	ruff check --fix src/ tests/

# Services
serve:  ## Start MCP server
	python -m sage serve

serve-mcp:  ## Start MCP server only
	python -m sage.services.mcp_server

# CLI
cli:  ## Run CLI help
	sage --help

# Cleanup
clean:  ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	rm -rf htmlcov/ .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

clean-all: clean  ## Clean everything including venv
	rm -rf .venv/

# Development
setup-dev:  ## Run development setup script
	python -m tools.dev_scripts.setup_dev

verify:  ## Verify setup (imports, config)
	python -m tools.dev_scripts.setup_dev --verify-only

# Documentation
docs:  ## Build documentation (placeholder)
	@echo "Documentation build not yet configured"

# Version
version:  ## Show version
	python -c "from sage import __version__; print(__version__)"

# ===========================================================================
# SAGE Validation Commands
# ===========================================================================

validate: validate-format validate-links validate-arch validate-index  ## Run all SAGE validations

validate-format:  ## Validate document format
	python -m tools.dev_scripts.validate_format -v

validate-links:  ## Check for broken links
	python -m tools.dev_scripts.check_links -v

validate-arch:  ## Check architecture rules
	python -m tools.dev_scripts.check_architecture -v

validate-index:  ## Validate index files
	python -m tools.dev_scripts.generate_index --check -v

check-all: lint test validate  ## Run all checks (lint, test, validate)

# ===========================================================================
# SAGE Index Generation
# ===========================================================================

index:  ## Regenerate all index files
	python -m tools.dev_scripts.generate_index --all --write -v

# ===========================================================================
# SAGE File Creation Commands
# ===========================================================================

new-adr:  ## Create new ADR (usage: make new-adr NAME="use-xyz")
	python -m tools.dev_scripts.new_file adr "$(NAME)"

new-convention:  ## Create new convention doc (usage: make new-convention NAME="naming")
	python -m tools.dev_scripts.new_file convention "$(NAME)"

new-practice:  ## Create new practice doc (usage: make new-practice NAME="caching" CAT="engineering")
	python -m tools.dev_scripts.new_file practice "$(NAME)" --category "$(CAT)"

new-guide:  ## Create new guide (usage: make new-guide NAME="getting-started")
	python -m tools.dev_scripts.new_file guide "$(NAME)"
