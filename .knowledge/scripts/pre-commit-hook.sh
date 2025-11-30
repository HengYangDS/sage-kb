#!/bin/bash
#
# Pre-commit hook for .knowledge documentation validation
#
# Installation:
#   cp .knowledge/scripts/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# Or create a symlink:
#   ln -s ../../.knowledge/scripts/pre-commit-hook.sh .git/hooks/pre-commit
#

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}📋 Running documentation checks...${NC}"

# Check if any .knowledge/*.md files are staged
STAGED_MD=$(git diff --cached --name-only --diff-filter=ACM | grep '\.knowledge/.*\.md$')

if [ -z "$STAGED_MD" ]; then
    echo -e "${GREEN}✓ No .knowledge markdown files staged, skipping checks${NC}"
    exit 0
fi

echo "Staged files:"
echo "$STAGED_MD" | while read file; do
    echo "  - $file"
done
echo ""

# Run markdown format check
echo -e "${YELLOW}🔍 Checking Markdown format...${NC}"
python .knowledge/scripts/check_markdown.py
MARKDOWN_RESULT=$?

if [ $MARKDOWN_RESULT -ne 0 ]; then
    echo -e "${RED}✗ Markdown format check failed${NC}"
    echo -e "${RED}Please fix the errors above before committing.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Markdown format OK${NC}"

# Run link validation
echo -e "${YELLOW}🔗 Checking cross-references...${NC}"
python .knowledge/scripts/check_links.py
LINKS_RESULT=$?

if [ $LINKS_RESULT -ne 0 ]; then
    echo -e "${RED}✗ Link validation failed${NC}"
    echo -e "${RED}Please fix broken links before committing.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Links OK${NC}"

echo ""
echo -e "${GREEN}✅ All documentation checks passed!${NC}"
exit 0
