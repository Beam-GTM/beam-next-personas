#!/bin/bash
#
# Install Expert Personas Framework (Standalone Package)
#
# Installs:
#   - Expert personas system (00-system/expert-personas/)
#   - Related skills (00-system/skills/expert-review/, expert-improve/)
#
# Usage:
#   ./install-standalone.sh /path/to/target/nexus
#   ./install-standalone.sh                          # Prompts for path
#

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Get script directory (source)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Read version
VERSION="unknown"
if [ -f "$SCRIPT_DIR/VERSION" ]; then
    VERSION=$(cat "$SCRIPT_DIR/VERSION" | tr -d '[:space:]')
fi

# Determine source paths (standalone repo structure)
PERSONAS_SOURCE="$SCRIPT_DIR"
SKILLS_SOURCE="$SCRIPT_DIR/skills"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Nexus Expert Personas Framework - Installer"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Version: v$VERSION"
echo ""
echo "This package includes:"
echo "  • 55 expert personas across multiple categories"
echo "  • Persona selection & suggestion scripts"
echo "  • Work-type mappings configuration"
echo "  • Feedback loop workflow"
echo "  • expert-review skill (quick feedback)"
echo "  • expert-improve skill (iterative refinement)"
echo ""

# Get target path
TARGET="${1:-}"
if [ -z "$TARGET" ]; then
    read -p "Enter target Nexus path: " TARGET
fi

# Expand ~ if present
TARGET="${TARGET/#\~/$HOME}"

# Validate target
if [ ! -d "$TARGET" ]; then
    echo -e "${RED}Error: Target directory does not exist: $TARGET${NC}"
    exit 1
fi

if [ ! -d "$TARGET/00-system" ]; then
    echo -e "${YELLOW}Warning: Target doesn't look like a Nexus root (no 00-system/)${NC}"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create directories if they don't exist
mkdir -p "$TARGET/00-system"
mkdir -p "$TARGET/00-system/skills"

PERSONAS_TARGET="$TARGET/00-system/expert-personas"
SKILLS_TARGET="$TARGET/00-system/skills"

echo "Source: $SCRIPT_DIR"
echo "Target Nexus: $TARGET"
echo ""

# ============================================================================
# Install Personas
# ============================================================================

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Installing Expert Personas${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if personas already exist
if [ -d "$PERSONAS_TARGET" ]; then
    TARGET_VERSION="unknown"
    if [ -f "$PERSONAS_TARGET/VERSION" ]; then
        TARGET_VERSION=$(cat "$PERSONAS_TARGET/VERSION" | tr -d '[:space:]')
    fi
    
    echo -e "${YELLOW}Expert-personas already exists${NC}"
    echo "  Current: v$TARGET_VERSION → New: v$VERSION"
    read -p "Overwrite? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping personas installation."
        SKIP_PERSONAS=true
    else
        rm -rf "$PERSONAS_TARGET"
        SKIP_PERSONAS=false
    fi
else
    SKIP_PERSONAS=false
fi

if [ "$SKIP_PERSONAS" != "true" ]; then
    echo -e "${BLUE}Installing expert-personas v$VERSION...${NC}"
    
    # Create target directory
    mkdir -p "$PERSONAS_TARGET"
    
    # Copy personas system files (exclude install script and skills)
    cp -r "$PERSONAS_SOURCE/personas" "$PERSONAS_TARGET/"
    cp -r "$PERSONAS_SOURCE/scripts" "$PERSONAS_TARGET/"
    cp -r "$PERSONAS_SOURCE/config" "$PERSONAS_TARGET/"
    cp -r "$PERSONAS_SOURCE/workflows" "$PERSONAS_TARGET/"
    cp -r "$PERSONAS_SOURCE/templates" "$PERSONAS_TARGET/"
    cp "$PERSONAS_SOURCE/VERSION" "$PERSONAS_TARGET/" 2>/dev/null || true
    cp "$PERSONAS_SOURCE/CHANGELOG.md" "$PERSONAS_TARGET/" 2>/dev/null || true
    cp "$PERSONAS_SOURCE/README.md" "$PERSONAS_TARGET/" 2>/dev/null || true
    
    # Make scripts executable
    chmod +x "$PERSONAS_TARGET/scripts/"*.py 2>/dev/null || true
    
    # Count personas
    PERSONA_COUNT=$(find "$PERSONAS_TARGET/personas" -name "*.md" -not -name "INDEX.md" -not -name "BACKLOG.md" 2>/dev/null | wc -l | tr -d ' ')
    
    echo -e "${GREEN}✓ Personas installed${NC}"
    echo "  • $PERSONA_COUNT personas"
fi

# ============================================================================
# Install Skills
# ============================================================================

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Installing Related Skills${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if skills directory exists in source
if [ ! -d "$SKILLS_SOURCE" ]; then
    echo -e "${YELLOW}⚠ Skills not found in source directory${NC}"
    echo "  Looking for: $SKILLS_SOURCE"
    echo "  Skills will be skipped. You can install them manually from:"
    echo "    00-system/skills/expert-review/"
    echo "    00-system/skills/expert-improve/"
    SKIP_SKILLS=true
else
    SKIP_SKILLS=false
    SOURCE_SKILLS="$SKILLS_SOURCE"
    
    # Install expert-review
    if [ -d "$SKILLS_SOURCE/expert-review" ]; then
        REVIEW_TARGET="$SKILLS_TARGET/expert-review"
        if [ -d "$REVIEW_TARGET" ]; then
            echo -e "${YELLOW}expert-review skill already exists${NC}"
            read -p "Overwrite? (y/N) " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                rm -rf "$REVIEW_TARGET"
                cp -r "$SKILLS_SOURCE/expert-review" "$REVIEW_TARGET"
                echo -e "${GREEN}✓ expert-review skill installed${NC}"
            else
                echo "Skipping expert-review"
            fi
        else
            cp -r "$SKILLS_SOURCE/expert-review" "$REVIEW_TARGET"
            echo -e "${GREEN}✓ expert-review skill installed${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ expert-review skill not found in source${NC}"
    fi
    
    # Install expert-improve
    if [ -d "$SKILLS_SOURCE/expert-improve" ]; then
        IMPROVE_TARGET="$SKILLS_TARGET/expert-improve"
        if [ -d "$IMPROVE_TARGET" ]; then
            echo -e "${YELLOW}expert-improve skill already exists${NC}"
            read -p "Overwrite? (y/N) " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                rm -rf "$IMPROVE_TARGET"
                cp -r "$SKILLS_SOURCE/expert-improve" "$IMPROVE_TARGET"
                echo -e "${GREEN}✓ expert-improve skill installed${NC}"
            else
                echo "Skipping expert-improve"
            fi
        else
            cp -r "$SKILLS_SOURCE/expert-improve" "$IMPROVE_TARGET"
            echo -e "${GREEN}✓ expert-improve skill installed${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ expert-improve skill not found in source${NC}"
    fi
fi

# ============================================================================
# Verify Installation
# ============================================================================

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Verifying Installation${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$SKIP_PERSONAS" != "true" ]; then
    # Test persona scripts
    if python3 "$PERSONAS_TARGET/scripts/select_personas.py" --format list > /dev/null 2>&1; then
        echo -e "${GREEN}✓ select_personas.py works${NC}"
    else
        echo -e "${YELLOW}⚠ select_personas.py check failed${NC}"
    fi
    
    if python3 "$PERSONAS_TARGET/scripts/suggest_personas.py" --list-types > /dev/null 2>&1; then
        echo -e "${GREEN}✓ suggest_personas.py works${NC}"
    else
        echo -e "${YELLOW}⚠ suggest_personas.py check failed${NC}"
    fi
fi

# Check skills
if [ "$SKIP_SKILLS" != "true" ]; then
    if [ -f "$SKILLS_TARGET/expert-review/SKILL.md" ]; then
        echo -e "${GREEN}✓ expert-review skill found${NC}"
    fi
    if [ -f "$SKILLS_TARGET/expert-improve/SKILL.md" ]; then
        echo -e "${GREEN}✓ expert-improve skill found${NC}"
    fi
fi

# ============================================================================
# Summary
# ============================================================================

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✓ Installation complete!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Installed: Expert Personas Framework v$VERSION"
echo ""
if [ "$SKIP_PERSONAS" != "true" ]; then
    echo "Personas: $PERSONAS_TARGET"
    echo "  • $PERSONA_COUNT personas"
    echo "  • Selection & suggestion scripts"
    echo "  • Work-type mappings"
fi
if [ "$SKIP_SKILLS" != "true" ]; then
    echo ""
    echo "Skills: $SKILLS_TARGET"
    echo "  • expert-review (quick feedback)"
    echo "  • expert-improve (iterative refinement)"
fi
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Usage"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "In conversation, say:"
echo "  • 'expert review on this document' → Quick feedback"
echo "  • 'improve this with experts' → Iterative refinement"
echo "  • 'persona feedback' → Full feedback loop"
echo ""
echo "Command line:"
echo "  python3 00-system/expert-personas/scripts/select_personas.py --format list"
echo "  python3 00-system/expert-personas/scripts/suggest_personas.py --work-type content"
echo "  python3 00-system/expert-personas/scripts/check_version.py --path $TARGET"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
