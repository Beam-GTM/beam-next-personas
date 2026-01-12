#!/usr/bin/env python3
"""
Expert Personas Metadata Scanner

Scans all expert persona files and outputs metadata for AI selection.
Each persona is a separate .md file with YAML frontmatter.

Usage:
    python select_personas.py [--category CATEGORY] [--domain DOMAIN] [--format FORMAT]

Arguments:
    --category  Filter by category (e.g., product-growth, venture, relationships)
    --domain    Filter by domain (e.g., B2C Virality & Growth, Product Strategy)
    --format    Output format: 'full' (default), 'brief', 'list'

Output:
    JSON array with metadata for each persona
"""

import yaml
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional

def extract_yaml_frontmatter(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Extract YAML frontmatter from markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match YAML frontmatter: ---\n[yaml]\n---
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None

        yaml_content = match.group(1)
        metadata = yaml.safe_load(yaml_content)

        if metadata:
            metadata['_file_path'] = str(file_path)
            metadata['_file_name'] = file_path.name
            # Extract category from parent folder
            metadata['_category_folder'] = file_path.parent.name

        return metadata

    except Exception as e:
        return {'error': str(e), '_file_path': str(file_path)}

def scan_personas(personas_dir: Path, category_filter: Optional[str] = None, domain_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Scan all persona files recursively and extract metadata.

    Structure: personas/{category}/{expert-slug}.md
    """
    personas = []

    if not personas_dir.exists():
        return []

    # Find all .md files recursively in category subdirectories
    for persona_file in personas_dir.glob("**/*.md"):
        # Skip README files
        if persona_file.name.lower() == 'readme.md':
            continue
            
        metadata = extract_yaml_frontmatter(persona_file)
        if metadata and 'error' not in metadata:
            # Apply category filter if specified
            if category_filter:
                persona_category = metadata.get('category', metadata.get('_category_folder', ''))
                if persona_category != category_filter:
                    continue

            # Apply domain filter if specified
            if domain_filter:
                persona_domain = metadata.get('domain', '')
                if domain_filter.lower() not in persona_domain.lower():
                    continue

            personas.append({
                "name": metadata.get('name', ''),
                "slug": metadata.get('slug', ''),
                "category": metadata.get('category', metadata.get('_category_folder', '')),
                "domain": metadata.get('domain', ''),
                "description": metadata.get('description', ''),
                "when_to_use": metadata.get('when_to_use', []),
                "best_for": metadata.get('best_for', ''),
                "famous_for": metadata.get('famous_for', ''),
                "file": metadata.get('_file_path', '')
            })

    # Sort by category, then by name
    personas.sort(key=lambda x: (x.get('category', ''), x.get('name', '')))

    return personas

def format_output(personas: List[Dict[str, Any]], format_type: str) -> str:
    """Format output based on requested format."""
    if format_type == 'brief':
        # Compact format: just name, category, domain, description
        brief = []
        for p in personas:
            brief.append({
                "name": p.get('name'),
                "category": p.get('category'),
                "domain": p.get('domain'),
                "description": p.get('description')
            })
        return json.dumps(brief, indent=2, ensure_ascii=False)

    elif format_type == 'list':
        # Ultra-compact: just names grouped by category
        by_category = {}
        for p in personas:
            cat = p.get('category', 'other')
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(p.get('name'))
        return json.dumps(by_category, indent=2, ensure_ascii=False)

    else:  # 'full'
        return json.dumps(personas, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description='Scan expert personas metadata')
    parser.add_argument('--category', type=str, help='Filter by category')
    parser.add_argument('--domain', type=str, help='Filter by domain (partial match)')
    parser.add_argument('--format', type=str, default='full',
                        choices=['full', 'brief', 'list'],
                        help='Output format')
    args = parser.parse_args()

    # Auto-detect base path
    # Script lives in: {nexus-root}/00-system/expert-personas/scripts/
    script_path = Path(__file__).resolve()
    expert_personas_dir = script_path.parent.parent

    # Personas directory - individual files organized by category
    personas_dir = expert_personas_dir / "personas"

    # Scan all personas
    all_personas = scan_personas(personas_dir, args.category, args.domain)

    # Output formatted JSON
    print(format_output(all_personas, args.format))

if __name__ == "__main__":
    main()
