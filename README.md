# Nexus Expert Personas Framework

**Standalone package** for the Expert Personas framework. Install into any Nexus instance, regardless of version.

## What's Included

### Core Personas System
- **36+ expert personas** across multiple categories (B2B, Product, Operations, Content, etc.)
- **Selection scripts** - Filter and list personas by category/domain
- **Suggestion script** - Get persona recommendations by work type
- **Work-type mappings** - 25+ work types with recommended personas
- **Feedback loop workflow** - Iterative improvement process
- **Persona template** - Create custom personas

### Related Skills
- **`expert-review`** - Quick, single-pass expert feedback
- **`expert-improve`** - Iterative refinement until excellence (7+/10)

## Quick Start

### Installation

```bash
# Clone this repository
git clone https://github.com/Beam-GTM/beam-next-personas.git
cd beam-next-personas

# Install to your Nexus instance
./install-standalone.sh /path/to/your/nexus
```

The installer will:
1. Install personas to `00-system/expert-personas/`
2. Install skills to `03-skills/expert-review/` and `expert-improve/`
3. Verify the installation
4. Show usage instructions

### Usage

**In conversation:**
- `"expert review on this document"` → Quick feedback from 3 experts
- `"improve this LinkedIn post"` → Iterative refinement until 7+/10
- `"persona feedback"` → Full feedback loop workflow

**Command line:**
```bash
# List all personas
python3 00-system/expert-personas/scripts/select_personas.py --format list

# Get recommendations for work type
python3 00-system/expert-personas/scripts/suggest_personas.py --work-type content

# Filter by category
python3 00-system/expert-personas/scripts/select_personas.py --category b2b-enterprise
```

## Personas Overview

### Categories

| Category | Personas | Best For |
|----------|----------|----------|
| **B2B Enterprise** | Geoffrey Moore, Aaron Ross, Patrick Campbell | GTM strategy, sales, pricing |
| **Product & Growth** | Marty Cagan, Shreyas Doshi, Nikita Bier, Dan Horowitz | Product strategy, growth, PM craft |
| **Operations & Leadership** | Andy Grove, Keith Rabois, Claire Hughes Johnson | Execution, hiring, org design |
| **Process Optimization** | Eliyahu Goldratt, W. Edwards Deming | Workflows, bottlenecks, quality |
| **Content & Influence** | Justin Welsh, Ethan Mollick, Steven Pinker | LinkedIn, thought leadership, writing |
| **Innovation** | Elon Musk, Steve Jobs | Moonshots, first principles, design |
| **Relationships** | Esther Perel, Kim Scott | Difficult conversations, feedback |
| **Strategy** | Hamilton Helmer, Warren Buffett, Sequoia | Competitive advantage, fundraising |
| **Engineering** | Will Larson, Camille Fournier, Kent Beck, John Carmack | Tech leadership, practices, performance |
| **Decisions** | Charlie Munger, Annie Duke, Ray Dalio | Complex decisions, risk assessment |

### Work Types

The framework supports 25+ work types with smart persona recommendations:

- `content` - LinkedIn posts, articles, thought leadership
- `strategy` - GTM strategy, market entry, positioning
- `execution-plan` - Action items, OKRs, roadmaps
- `sales` - Sales process, outreach, revenue
- `product` - Product strategy, features, roadmap
- `pricing` - Pricing strategy, packaging, value
- `hiring` - Job descriptions, org design, team structure
- `messaging` - Value props, taglines, positioning
- `culture` - Values, team dynamics, rituals
- `writing` - Documents, clarity, editing
- `decision-making` - Complex decisions, risk assessment
- `engineering` - Tech strategy, engineering org
- ... and more

See `config/work-type-mappings.yaml` for the complete list.

## Skills

### expert-review

**Purpose**: Quick, directional feedback from expert perspectives.

**When to use**: Early drafts, sanity checks, "is this on the right track?"

**Flow**:
1. Detect work type
2. Select top 3 personas
3. Run reviews (single pass)
4. Show summary with actionable insights

### expert-improve

**Purpose**: Iteratively refine work until it reaches excellence (7+/10).

**When to use**: Final deliverables, "make this better", "polish until ready"

**Flow**:
1. Detect work type + select personas
2. Confirm once: "I'll run [personas] for up to [N] rounds. Go?"
3. Review → Apply fixes → Re-review → Repeat until target
4. Output improved version + score progression

## Repository Structure

```
beam-next-personas/
├── README.md                    # This file
├── VERSION                      # Current version
├── CHANGELOG.md                 # Version history
├── install-standalone.sh        # Enhanced installer
│
├── expert-personas/             # Core personas system
│   ├── personas/               # All persona files (36+)
│   ├── scripts/                # Python scripts
│   ├── config/                 
│   ├── workflows/              
│   └── templates/              
│
└── skills/                      # Related skills
    ├── expert-review/
    └── expert-improve/
```

## Versioning

Follows semantic versioning (MAJOR.MINOR.PATCH):
- **Major**: Breaking changes to persona format or API
- **Minor**: New personas, new work types, new features
- **Patch**: Bug fixes, documentation updates

**Current version**: See `VERSION` file

**Check installed version**:
```bash
python3 00-system/expert-personas/scripts/check_version.py --path /path/to/nexus
```

**Compare versions**:
```bash
python3 00-system/expert-personas/scripts/check_version.py \
  --path /path/to/nexus \
  --available /path/to/beam-next-personas \
  --format detailed
```

See `VERSIONING.md` for complete versioning guide.

## Requirements

- Python 3.6+ (for scripts)
- Any Nexus instance (any version)

## Contributing

To add new personas:
1. Use `scripts/generate_persona.py` or copy `templates/persona-template.md`
2. Research real expert with documented framework
3. Add to appropriate category in `personas/`
4. Update `config/work-type-mappings.yaml` if needed

**Quality bar**: Must be real person with published work, not generic role.
