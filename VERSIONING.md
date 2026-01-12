# Versioning Guide

The Expert Personas Framework uses semantic versioning (MAJOR.MINOR.PATCH) to track changes.

## Version Format

**Current Version**: See `VERSION` file (e.g., `1.0.0`)

### Version Components

- **MAJOR** (1.0.0): Breaking changes to persona format, API, or structure
- **MINOR** (1.1.0): New personas, new work types, new features, significant improvements
- **PATCH** (1.0.1): Bug fixes, documentation updates, minor corrections

## Version Tracking

### Framework Version
- **Location**: `VERSION` file in repository root
- **Format**: `MAJOR.MINOR.PATCH` (e.g., `1.0.0`)
- **Updated when**: Any change to the framework

### Individual Persona Versions (Optional)
- **Location**: YAML frontmatter in persona files (`version:` field)
- **Format**: `MAJOR.MINOR.PATCH` (e.g., `1.0.0`)
- **Updated when**: Significant changes to a specific persona
- **Default**: If not specified, inherits framework version

## Version Checking

### Check Installed Version

```bash
# Simple version check
python3 00-system/expert-personas/scripts/check_version.py --path /path/to/nexus

# Detailed version info
python3 00-system/expert-personas/scripts/check_version.py --path /path/to/nexus --format detailed

# JSON output
python3 00-system/expert-personas/scripts/check_version.py --path /path/to/nexus --format json
```

### Compare Versions

```bash
# Compare installed vs available
python3 00-system/expert-personas/scripts/check_version.py \
  --path /path/to/nexus \
  --available /path/to/beam-next-personas \
  --format detailed
```

## Version Update Process

### When to Update Version

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Add new persona | MINOR | `1.0.0` → `1.1.0` |
| Add new work type | MINOR | `1.1.0` → `1.2.0` |
| Fix bug in script | PATCH | `1.1.0` → `1.1.1` |
| Update documentation | PATCH | `1.1.1` → `1.1.2` |
| Change persona format | MAJOR | `1.x.x` → `2.0.0` |
| Breaking API change | MAJOR | `2.x.x` → `3.0.0` |

### Update Steps

1. **Make changes** to personas, scripts, or config
2. **Update VERSION file** with new version number
3. **Update CHANGELOG.md** with changes
4. **Commit and tag**:
   ```bash
   git add VERSION CHANGELOG.md
   git commit -m "Release v1.1.0: Add 5 new personas"
   git tag v1.1.0
   git push origin main --tags
   ```

## Changelog Format

See `CHANGELOG.md` for the format. Each version entry includes:

```markdown
## [1.1.0] - 2026-01-15

### Added
- New persona: [Name] ([category])
- New work type: [type] with mappings

### Changed
- Updated [persona] with new framework insights

### Fixed
- Bug in suggest_personas.py for edge cases
```

## Installation Version Handling

The install script (`install-standalone.sh`) handles version conflicts:

- **If version exists**: Shows current vs new version, asks before overwriting
- **If version is newer**: Warns user about downgrade
- **If version matches**: Can skip or reinstall

## Version in Persona Files

Personas can optionally include a `version:` field in their frontmatter:

```yaml
---
name: Geoffrey Moore
slug: geoffrey-moore
version: 1.2.0  # Optional: tracks persona-specific updates
category: b2b-enterprise
...
---
```

**When to version personas individually:**
- Major updates to persona content (new frameworks, significant rewrites)
- Persona-specific improvements that don't affect the framework

**When NOT to version individually:**
- Minor typos or formatting fixes
- Framework-wide changes (use framework version)

## Best Practices

1. **Always update VERSION** when making changes
2. **Always update CHANGELOG.md** with what changed
3. **Tag releases** in git for easy reference
4. **Use semantic versioning** consistently
5. **Document breaking changes** clearly in CHANGELOG

## Version History

See `CHANGELOG.md` for complete version history.
