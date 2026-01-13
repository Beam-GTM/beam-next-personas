# Nexus Expert Personas Framework

**Standalone package** for the Expert Personas framework. Install into any Nexus instance, regardless of version.

## What's Included

### Core Personas System
- **55 expert personas** across multiple categories (AI, Sales, Product, Operations, Content, etc.)
- **Selection scripts** - Filter and list personas by category/domain
- **Suggestion script** - Get persona recommendations by work type
- **Work-type mappings** - 50+ work types with recommended personas
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
2. Install skills to `00-system/skills/expert-review/` and `expert-improve/`
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

## Personas Overview (55 Total)

### Categories

| Category | Personas | Best For |
|----------|----------|----------|
| **AI & Technology** | Andrej Karpathy, Andrew Ng, Alexandr Wang, Dario Amodei, Cassie Kozyrkov, Ethan Mollick | AI products, transformation, infrastructure, safety |
| **Sales & GTM** | Aaron Ross, David Sacks, Mark Roberge, Jacco van der Kooij, John McMahon, Meka Asonye, Chris Voss | Sales process, methodology, enterprise, founder-led |
| **B2B & Marketing** | Geoffrey Moore, April Dunford, Emily Kramer, Seth Godin, Patrick Campbell | GTM strategy, positioning, B2B marketing, pricing |
| **Product & Growth** | Marty Cagan, Shreyas Doshi, Lenny Rachitsky, Elena Verna, Nikita Bier, BJ Fogg | Product strategy, PLG, growth, activation |
| **Operations & Leadership** | Andy Grove, Keith Rabois, Claire Hughes Johnson, Frank Slootman | Execution, hiring, org design, turnarounds |
| **Design & UX** | Don Norman, Julie Zhuo, Steve Jobs, Nancy Duarte | UX, human-centered design, presentations |
| **Content & Influence** | Justin Welsh, Sahil Bloom, Steven Pinker, Paul Graham | LinkedIn, frameworks, writing, clarity |
| **Engineering** | Will Larson, Camille Fournier, Kent Beck, John Carmack | Tech leadership, practices, performance |
| **Decisions & Strategy** | Charlie Munger, Annie Duke, Ray Dalio, Hamilton Helmer, Warren Buffett | Complex decisions, competitive advantage |
| **People & Culture** | Esther Perel, Kim Scott, Lincoln Murphy, Ben Horowitz | Conversations, feedback, customer success, hard decisions |

### Work Types (50+)

The framework supports 50+ work types with smart persona recommendations:

**Strategy & GTM:**
- `strategy` - GTM strategy, market entry, positioning
- `gtm-operations` - Sales/marketing alignment
- `competitive-strategy` - Moats, competitive advantage
- `messaging` - Value props, positioning statements

**Sales:**
- `sales` - Sales process, outreach, revenue
- `sales-methodology` - SPICED, MEDDICC, deal execution
- `enterprise-sales` - Complex, high-ACV deals
- `founder-sales` - Founder-led to first sales hire
- `negotiation` - Sales negotiations, contracts

**Product & Growth:**
- `product` - Product strategy, features, roadmap
- `plg` - Product-led growth, freemium
- `growth` - User acquisition, virality, retention
- `onboarding` - User onboarding, activation
- `pricing` - Pricing strategy, packaging

**AI:**
- `ai-strategy` - AI/ML decisions, when to use AI
- `ai-product` - AI implementation, technical decisions
- `ai-transformation` - Enterprise AI adoption
- `ai-infrastructure` - AI data, services
- `ai-safety` - Responsible AI, alignment

**Operations:**
- `execution-plan` - OKRs, roadmaps, action items
- `operations` - Workflows, processes, efficiency
- `saas-metrics` - Burn multiple, magic number, CAC

**Content & Communication:**
- `content` - LinkedIn posts, articles, thought leadership
- `presentations` - Keynotes, pitch decks
- `writing` - Documents, clarity, editing
- `personal-brand` - Audience building, creator economy

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
4. Output **new versioned file** (e.g., `doc-v2.md`) + score progression

## Repository Structure

```
beam-next-personas/
├── README.md                    # This file
├── VERSION                      # Current version (1.5.0)
├── CHANGELOG.md                 # Version history
├── install-standalone.sh        # Enhanced installer
│
├── personas/                    # All 55 persona files
├── scripts/                     # Python scripts
├── config/                      # Work-type mappings
├── workflows/                   # Feedback loop workflow
├── templates/                   # Persona template
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

**Current version**: 1.5.0 (55 personas)

**Version history:**
- v1.5.0 - AI experts (Andrej Karpathy, Andrew Ng, Alexandr Wang, Dario Amodei)
- v1.4.0 - Sales experts (Mark Roberge, Jacco van der Kooij, John McMahon, Meka Asonye)
- v1.3.0 - David Sacks (SaaS metrics)
- v1.2.0 - PLG & behavior (Elena Verna, BJ Fogg, Emily Kramer, Cassie Kozyrkov, Lincoln Murphy, Sahil Bloom)
- v1.1.0 - Communication (Don Norman, Chris Voss, Nancy Duarte, Ben Horowitz)
- v1.0.0 - Initial release (36 personas)

See `CHANGELOG.md` for detailed version history.

## Requirements

- Python 3.6+ (for scripts)
- Any Nexus instance (any version)

## Contributing

To add new personas:
1. Use `templates/persona-template.md`
2. Research real expert with documented framework
3. Add to `personas/`
4. Update `config/work-type-mappings.yaml` if needed
5. Update `personas/INDEX.md`

**Quality bar**: Must be real person with published work, not generic role.
