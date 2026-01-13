# Changelog

All notable changes to the Expert Personas Framework.

## [1.6.1] - 2026-01-13

### Changed
- **Install path for skills**: Now installs to `00-system/skills/` instead of `03-skills/`
  - `expert-review` → `00-system/skills/expert-review/`
  - `expert-improve` → `00-system/skills/expert-improve/`

### Migration Note
If you have an existing installation with skills in `03-skills/`, you can either:
1. Run the installer again (it will install to new location)
2. Manually move: `mv 03-skills/expert-* 00-system/skills/`

## [1.6.0] - 2026-01-13

### Added
- **Roelof Botha** - Sequoia Managing Partner, PayPal CFO, company building arcs
- **Bill Gurley** - Benchmark partner, Uber board, "All Revenue Not Equal", marketplaces

### Removed
- **Sequoia Perspective** - Replaced with real person (Roelof Botha)

### New Work Types
- `marketplace`, `unit-economics`, `business-model`, `investor-pitch`

### Stats
- Total personas: 56

## [1.5.0] - 2026-01-13

### Added - AI Expertise
- **Andrej Karpathy**, **Andrew Ng**, **Alexandr Wang**, **Dario Amodei**

### New Work Types
- `ai-product`, `ai-transformation`, `ai-infrastructure`, `ai-safety`, `ai-technical`

### Stats
- Total personas: 55

## [1.4.0] - 2026-01-12

### Added - Sales Expertise
- **Mark Roberge**, **Jacco van der Kooij**, **John McMahon**, **Meka Asonye**

### Stats
- Total personas: 51

## [1.3.0] - 2026-01-12

### Added
- **David Sacks** - SaaS metrics, GTM operations

### Stats
- Total personas: 47

## [1.2.0] - 2026-01-12

### Added
- **Elena Verna**, **Emily Kramer**, **BJ Fogg**, **Cassie Kozyrkov**, **Lincoln Murphy**, **Sahil Bloom**

### Stats
- Total personas: 46

## [1.1.0] - 2026-01-12

### Added
- **Don Norman**, **Chris Voss**, **Nancy Duarte**, **Ben Horowitz**

### Stats
- Total personas: 40

## [1.0.0] - 2026-01-12

### Initial Release
- 36 expert personas
- Work-type mappings, scripts, templates, workflows
