#!/bin/bash
#
# Push Expert Personas Framework to GitHub
#
# This script initializes git, commits all files, and pushes to GitHub.
#

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Pushing Expert Personas Framework to GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if already a git repo
if [ -d ".git" ]; then
    echo -e "${YELLOW}Git repository already exists${NC}"
    read -p "Continue with existing repo? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo -e "${BLUE}Initializing git repository...${NC}"
    git init
fi

# Add all files
echo -e "${BLUE}Adding all files...${NC}"
git add .

# Check if there are changes
if git diff --cached --quiet && git diff --quiet; then
    echo -e "${YELLOW}No changes to commit${NC}"
    exit 0
fi

# Commit
echo -e "${BLUE}Creating commit...${NC}"
git commit -m "Initial release: Expert Personas Framework v1.0.0

- 38 expert personas across 10 categories
- Persona selection and suggestion scripts
- Version checking and comparison tools
- Work-type mappings (25+ types)
- Feedback loop workflow
- Standalone installer
- Related skills: expert-review and expert-improve
- Comprehensive documentation and versioning system"

# Set up remote
echo -e "${BLUE}Setting up remote...${NC}"
if git remote | grep -q "^origin$"; then
    git remote set-url origin https://github.com/Beam-GTM/beam-next-personas.git
else
    git remote add origin https://github.com/Beam-GTM/beam-next-personas.git
fi

# Set branch to main
echo -e "${BLUE}Setting branch to main...${NC}"
git branch -M main

# Create tag
echo -e "${BLUE}Creating version tag...${NC}"
git tag -f v1.0.0 2>/dev/null || git tag v1.0.0

# Push
echo ""
echo -e "${BLUE}Pushing to GitHub...${NC}"
echo "Repository: https://github.com/Beam-GTM/beam-next-personas.git"
echo ""

read -p "Push to GitHub now? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Push cancelled. Run these commands manually:${NC}"
    echo ""
    echo "  git push -u origin main"
    echo "  git push origin v1.0.0"
    exit 0
fi

# Push main branch
echo -e "${BLUE}Pushing main branch...${NC}"
git push -u origin main

# Push tag
echo -e "${BLUE}Pushing version tag...${NC}"
git push origin v1.0.0

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✓ Successfully pushed to GitHub!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Repository: https://github.com/Beam-GTM/beam-next-personas"
echo ""
echo "Installation:"
echo "  git clone https://github.com/Beam-GTM/beam-next-personas.git"
echo "  cd beam-next-personas"
echo "  ./install-standalone.sh /path/to/nexus"
echo ""
