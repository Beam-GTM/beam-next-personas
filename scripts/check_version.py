#!/usr/bin/env python3
"""
Check version of installed Expert Personas framework.

Usage:
    python3 scripts/check_version.py [--path /path/to/nexus]
"""

import argparse
import sys
from pathlib import Path


def read_version(version_file: Path) -> str:
    """Read version from VERSION file."""
    if not version_file.exists():
        return None
    
    try:
        with open(version_file, 'r') as f:
            version = f.read().strip()
        return version
    except Exception:
        return None


def compare_versions(installed: str, available: str) -> dict:
    """Compare two version strings (semantic versioning)."""
    if not installed or not available:
        return {"status": "unknown", "message": "Cannot compare versions"}
    
    installed_parts = [int(x) for x in installed.split('.')]
    available_parts = [int(x) for x in available.split('.')]
    
    # Pad to 3 parts (major.minor.patch)
    while len(installed_parts) < 3:
        installed_parts.append(0)
    while len(available_parts) < 3:
        available_parts.append(0)
    
    if installed_parts == available_parts:
        return {"status": "current", "message": f"Up to date (v{installed})"}
    elif installed_parts < available_parts:
        return {
            "status": "outdated",
            "message": f"Update available: v{installed} → v{available}"
        }
    else:
        return {
            "status": "newer",
            "message": f"Installed version (v{installed}) is newer than available (v{available})"
        }


def main():
    parser = argparse.ArgumentParser(
        description="Check version of installed Expert Personas framework"
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path to Nexus instance (default: current directory)"
    )
    parser.add_argument(
        "--available",
        type=str,
        help="Path to available version (for comparison)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["simple", "json", "detailed"],
        default="simple",
        help="Output format (default: simple)"
    )
    
    args = parser.parse_args()
    
    base_path = Path(args.path).resolve()
    installed_path = base_path / "00-system" / "expert-personas" / "VERSION"
    
    installed_version = read_version(installed_path)
    
    if args.format == "json":
        result = {
            "installed": installed_version,
            "path": str(installed_path),
            "exists": installed_path.exists()
        }
        
        if args.available:
            available_path = Path(args.available).resolve() / "VERSION"
            available_version = read_version(available_path)
            result["available"] = available_version
            if installed_version and available_version:
                comparison = compare_versions(installed_version, available_version)
                result["comparison"] = comparison
        
        import json
        print(json.dumps(result, indent=2))
        return
    
    # Simple or detailed format
    if not installed_path.exists():
        print(f"❌ Expert Personas not installed at {installed_path}")
        print(f"   Run: ./install-standalone.sh {base_path}")
        sys.exit(1)
    
    if not installed_version:
        print(f"⚠️  Version file exists but cannot be read: {installed_path}")
        sys.exit(1)
    
    if args.format == "simple":
        print(f"v{installed_version}")
    else:  # detailed
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("  Expert Personas Framework - Version Check")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"")
        print(f"Installed version: v{installed_version}")
        print(f"Location: {installed_path}")
        print("")
        
        if args.available:
            available_path = Path(args.available).resolve() / "VERSION"
            available_version = read_version(available_path)
            
            if available_version:
                comparison = compare_versions(installed_version, available_version)
                print(f"Available version: v{available_version}")
                print(f"")
                
                if comparison["status"] == "current":
                    print(f"✅ {comparison['message']}")
                elif comparison["status"] == "outdated":
                    print(f"⚠️  {comparison['message']}")
                    print(f"   To update: git pull && ./install-standalone.sh {base_path}")
                else:
                    print(f"ℹ️  {comparison['message']}")
            else:
                print("⚠️  Cannot read available version")
        else:
            print("ℹ️  Use --available /path/to/repo to compare versions")


if __name__ == "__main__":
    main()
