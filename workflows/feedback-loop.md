# Persona Feedback Loop

Apply expert perspectives iteratively to challenge and improve any piece of work.

**Trigger phrases**: "persona feedback", "expert review", "improve with personas"

> **Skill Available**: The full implementation is in `03-skills/expert-feedback/SKILL.md`
> Say "persona feedback" or "expert review" to trigger the skill.

## Quick Start

```bash
# Suggest personas for your work type
python3 00-system/expert-personas/scripts/suggest_personas.py --work-type content

# List all personas
python3 00-system/expert-personas/scripts/select_personas.py --format brief
```

## Default Configuration

| Setting | Default | Range |
|---------|---------|-------|
| Personas | 3 | 3-5 |
| Iterations | 2 | 1-3 |
| Target | 7+/10 | Adjustable |

---

## Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  1. SETUP                                                        │
│  → Understand the work, suggest personas, configure iterations   │
├─────────────────────────────────────────────────────────────────┤
│  2. REVIEW                                                       │
│  → Each persona evaluates independently                          │
├─────────────────────────────────────────────────────────────────┤
│  3. IMPROVE                                                      │
│  → Synthesize feedback, prioritize changes, create new version   │
├─────────────────────────────────────────────────────────────────┤
│  4. ITERATE                                                      │
│  → Repeat review/improve until target scores reached             │
├─────────────────────────────────────────────────────────────────┤
│  5. OUTPUT                                                       │
│  → Final version + scores + learnings                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Setup

**Ask**: "What work would you like expert feedback on?"

Then suggest personas based on work type:

| Work Type | Recommended Personas |
|-----------|---------------------|
| Content | Justin Welsh, Ethan Mollick |
| Strategy | Geoffrey Moore, Sequoia, Aaron Ross |
| Operations | Goldratt, Deming |
| Product | Dan Horowitz, Nikita Bier |
| Pricing | Patrick Campbell, Geoffrey Moore |

**Configure**:
- Personas: 3-5 (suggest based on work type)
- Iterations: 1-3 (default: 2)

---

## Phase 2: Review

⚠️ **Evaluate from each persona's perspective independently.**

For each persona, load their file and provide:

```
═══════════════════════════════════════
[PERSONA NAME] REVIEW
═══════════════════════════════════════

SCORE: X/10

CORE REACTION:
[1-2 sentences]

WHAT WORKS:
- [Strength]
- [Strength]

CONCERNS:
- [Issue from their framework]
- [Issue from their framework]

KEY RECOMMENDATION:
[Their most important advice]
```

**Summary table after all reviews**:

| Persona | Score | Biggest Strength | Biggest Gap |
|---------|-------|------------------|-------------|
| [Name] | X/10 | | |
| **Average** | **X.X/10** | | |

---

## Phase 3: Improve

Prioritize changes:
1. **Must Address** — flagged by 2+ personas
2. **Should Address** — strong single-persona concern
3. **Consider** — nice-to-have

Apply changes while preserving what personas praised.

---

## Phase 4: Iterate

| Result | Action |
|--------|--------|
| All personas 7+ | → Done |
| Average < 6.5 | → Iterate |
| One persona < 6 | → Address their concern |
| Max iterations | → Finalize with notes |

---

## Phase 5: Output

```
════════════════════════════════════════════════════════════════
🏆 FINAL VERSION
════════════════════════════════════════════════════════════════
[Content]

SCORES:
| Persona | Score | Verdict |
|---------|-------|---------|
| [Name] | X/10 | [1-line] |
| Average | X.X/10 | |

KEY IMPROVEMENTS:
1. [Change and why]
2. [Change and why]

LEARNINGS:
- [Pattern to replicate]
- [Pitfall to avoid]
```

---

## Work Type Reference

See `config/work-type-mappings.yaml` for full mappings.

| Type | Primary | Supporting |
|------|---------|------------|
| content | Justin Welsh, Ethan Mollick | Geoffrey Moore |
| strategy | Geoffrey Moore, Sequoia | Aaron Ross |
| sales | Aaron Ross, Geoffrey Moore | Patrick Campbell |
| operations | Goldratt, Deming | Patrick Campbell |
| product | Dan Horowitz, Nikita Bier | Geoffrey Moore |
| pricing | Patrick Campbell, Geoffrey Moore | Sequoia |
| fundraising | Sequoia, Geoffrey Moore | Patrick Campbell |
| innovation | Elon Musk, Goldratt | Dan Horowitz |
| communication | Esther Perel, Justin Welsh | Deming |
| growth | Nikita Bier, Justin Welsh | Dan Horowitz |
