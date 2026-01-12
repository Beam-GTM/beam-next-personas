#!/usr/bin/env python3
"""
Persona Suggestion Helper

Suggests relevant expert personas based on work type.
Reads mappings from config/work-type-mappings.yaml

Usage:
    python suggest_personas.py --work-type content
    python suggest_personas.py --work-type strategy --count 4
    python suggest_personas.py --list-types
"""

import argparse
import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional


def load_mappings() -> Dict:
    """Load work-type mappings from YAML config."""
    script_dir = Path(__file__).resolve().parent
    config_path = script_dir.parent / "config" / "work-type-mappings.yaml"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def get_suggestion(work_type: str, count: int = 3) -> Dict:
    """Get persona suggestion for a work type."""
    mappings = load_mappings()
    
    if work_type.lower() not in mappings:
        return {
            "error": f"Unknown work type: {work_type}",
            "available": list(mappings.keys())
        }
    
    config = mappings[work_type.lower()]
    primary = config.get("primary", [])
    supporting = config.get("supporting", [])
    
    # Combine and limit to count
    all_personas = primary + supporting
    selected = all_personas[:max(3, min(5, count))]
    
    return {
        "work_type": work_type,
        "description": config.get("description", ""),
        "suggested_personas": selected,
        "primary": [p for p in selected if p in primary],
        "supporting": [p for p in selected if p in supporting]
    }


def list_work_types() -> Dict[str, str]:
    """List all available work types."""
    mappings = load_mappings()
    return {k: v.get("description", "") for k, v in mappings.items()}


def main():
    parser = argparse.ArgumentParser(description="Suggest personas for work type")
    parser.add_argument("--work-type", type=str, help="Type of work")
    parser.add_argument("--list-types", action="store_true", help="List available work types")
    parser.add_argument("--count", type=int, default=3, help="Number of personas (3-5)")
    args = parser.parse_args()

    if args.list_types:
        print(json.dumps(list_work_types(), indent=2))
        return

    if not args.work_type:
        print("Error: --work-type required. Use --list-types to see options.")
        return

    result = get_suggestion(args.work_type, args.count)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
