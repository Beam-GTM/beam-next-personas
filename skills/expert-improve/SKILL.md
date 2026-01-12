---
name: expert-improve
description: "Iterative expert refinement until work is excellent. Load when user says: 'improve this', 'make this better', 'polish until ready', 'iterate with experts', 'refine this'"
---

# Expert Improve

Iteratively refine work with expert feedback until it reaches excellence. Multiple passes, applies fixes, tracks improvement.

## When to Use

| Use This | Not This |
|----------|----------|
| "Make this better" | "What's wrong?" → use `expert-review` |
| "Polish until ready" | "Quick feedback" → use `expert-review` |
| "Iterate until good" | Early drafts, sanity checks |
| Final deliverables | Just want insights |

---

## Quick Start

**User says**: "improve my strategy" / "polish this LinkedIn post"

**AI does** (auto-run after initial confirm):
1. Detect work type + feedback type needed
2. Select top 3 personas
3. Confirm once: "I'll run [personas] for up to [N] rounds until 7+/10. Go?"
4. Run review → Apply fixes → Re-review → Repeat until target
5. Output improved version + score progression

---

## Execution Flow

### Step 1: Setup (One Confirmation)

```
Got it. I'll improve this with expert feedback.

📋 Detected: [WORK TYPE]
🎯 Goal: Refine until all experts score 7+/10

Reviewers:
1. **[Persona 1]** — [Domain]
2. **[Persona 2]** — [Domain]  
3. **[Persona 3]** — [Domain]

Plan: Up to 2 rounds of review + improvement

Start? (Enter = yes, or customize personas/rounds)
```

**After confirmation, everything runs automatically.**

---

### Step 2: Review Round (Auto)

For each persona:

```
═══════════════════════════════════════
[PERSONA NAME] — Round [N]
═══════════════════════════════════════

SCORE: X/10

STRENGTHS:
• [Keep this]
• [Keep this]

ISSUES:
• [Problem] → Fix: [Specific action]
• [Problem] → Fix: [Specific action]

KEY FIX:
[Most important change to make]
```

**Summary after all reviews**:

```
📊 ROUND [N] SCORES

| Expert | Score | Status |
|--------|-------|--------|
| [Name] | X/10 | ✅ Ready / ⚠️ Needs fix |
| [Name] | X/10 | ✅ Ready / ⚠️ Needs fix |
| [Name] | X/10 | ✅ Ready / ⚠️ Needs fix |
| **Avg** | **X.X** | [Target: 7+] |
```

---

### Step 3: Improve (Auto)

**Prioritize by consensus**:

```
🔧 APPLYING IMPROVEMENTS

MUST FIX (2+ experts agree):
1. [Issue] → [Change being made]

FIXING (single expert, high impact):
2. [Issue] → [Change being made]

PRESERVING (praised by experts):
• [Strength 1]
• [Strength 2]
```

**Show improved version** (no confirmation needed, just execute):

```
📝 IMPROVED VERSION (Round [N])

[Updated content with changes applied]

Changes made:
✓ [Change 1]
✓ [Change 2]
✓ [Change 3]
```

---

### Step 4: Iterate (Auto)

**Decision logic** (runs automatically):

```
IF all scores ≥ 7:
    → DONE! Go to Step 5
    
ELIF rounds < max_rounds:
    → Run another round (back to Step 2)
    
ELSE:
    → Finalize with current version + notes on remaining gaps
```

**Between rounds** (no user input needed):

```
⏳ Round [N] complete. Average: X.X/10
   [Persona A] needs [specific fix]
   Running Round [N+1]...
```

---

### Step 5: Final Output (Auto)

```
════════════════════════════════════════════════════════════════
🏆 FINAL VERSION
════════════════════════════════════════════════════════════════

[Clean, improved content]

════════════════════════════════════════════════════════════════
📊 IMPROVEMENT JOURNEY
════════════════════════════════════════════════════════════════

| Expert | Start | Final | Δ |
|--------|-------|-------|---|
| [Name] | 5/10 | 8/10 | +3 |
| [Name] | 6/10 | 7/10 | +1 |
| [Name] | 4/10 | 7/10 | +3 |
| **Avg** | **5.0** | **7.3** | **+2.3** |

✅ Target reached in 2 rounds

════════════════════════════════════════════════════════════════
🔧 KEY CHANGES MADE
════════════════════════════════════════════════════════════════

1. **[Change]** — Why: [Expert] said "[quote]"
2. **[Change]** — Why: Consensus from [Expert A, B]
3. **[Change]** — Why: [Expert] flagged as critical

════════════════════════════════════════════════════════════════
💡 LEARNINGS
════════════════════════════════════════════════════════════════

WHAT WORKED:
• [Pattern to replicate]
• [What experts praised]

WHAT FAILED INITIALLY:
• [Mistake to avoid]
• [Common pitfall identified]
```

---

## Configuration Defaults

| Setting | Default | Adjustable |
|---------|---------|------------|
| Personas | 3 | 2-5 |
| Max rounds | 2 | 1-3 |
| Target score | 7+/10 | 6-9 |
| Auto-apply fixes | Yes | Can confirm each |

---

## Scoring Guide

| Score | Meaning | AI Action |
|-------|---------|-----------|
| 9-10 | Exceptional | Done immediately |
| 7-8 | Solid, ship-ready | Done (target met) |
| 5-6 | Good foundation, gaps | Continue improving |
| 3-4 | Fundamental issues | Flag, may need pivot |
| 1-2 | Wrong approach | Stop, discuss with user |

---

## Available Personas

Same as `expert-review` — see that skill for full list.

**Auto-selection by work type**:

| Work Type | Default Personas |
|-----------|------------------|
| `content` | Justin Welsh, Ethan Mollick, Geoffrey Moore |
| `strategy` | Geoffrey Moore, Sequoia, Aaron Ross |
| `execution-plan` | Andy Grove, Keith Rabois, Claire Hughes Johnson |
| `sales` | Aaron Ross, Geoffrey Moore, Patrick Campbell |
| `pricing` | Patrick Campbell, Geoffrey Moore, Sequoia |
| `product` | Dan Horowitz, Nikita Bier, Geoffrey Moore |
| `operations` | Goldratt, Deming, Keith Rabois |

---

## Example Session

```
User: "improve my GTM strategy document"

AI: Got it. I'll improve this with expert feedback.

📋 Detected: STRATEGY
🎯 Goal: Refine until all experts score 7+/10

Reviewers:
1. **Geoffrey Moore** — Beachhead strategy, crossing the chasm
2. **Sequoia Partners** — Market timing, product-market fit
3. **Aaron Ross** — Predictable revenue, sales process

Plan: Up to 2 rounds of review + improvement

Start? (Enter = yes)

[User presses Enter]

═══════════════════════════════════════
GEOFFREY MOORE — Round 1
═══════════════════════════════════════

SCORE: 5/10

STRENGTHS:
• Clear problem statement
• Good competitive awareness

ISSUES:
• Beachhead too broad ("enterprises") → Fix: Define specific segment
• No bowling pin strategy → Fix: Add expansion sequence
• Missing whole product map → Fix: Add beyond-core requirements

KEY FIX:
Define beachhead: "US-based RPOs, $50-500M revenue, serving Fortune 500"

[... more reviews ...]

📊 ROUND 1 SCORES

| Expert | Score | Status |
|--------|-------|--------|
| Geoffrey Moore | 5/10 | ⚠️ Needs beachhead |
| Sequoia | 6/10 | ⚠️ Needs unit economics |
| Aaron Ross | 4/10 | ⚠️ Needs sales process |
| **Avg** | **5.0** | Target: 7+ |

🔧 APPLYING IMPROVEMENTS

MUST FIX:
1. Vague beachhead → Adding specific segment definition
2. No sales process → Adding ICP + outbound strategy

FIXING:
3. Missing unit economics → Adding CAC/LTV framework

PRESERVING:
• Clear problem statement
• Competitive positioning

📝 IMPROVED VERSION (Round 1)

[... improved strategy with changes applied ...]

⏳ Round 1 complete. Average: 5.0/10
   Running Round 2...

[... Round 2 runs automatically ...]

════════════════════════════════════════════════════════════════
🏆 FINAL VERSION
════════════════════════════════════════════════════════════════

[Final improved strategy]

📊 IMPROVEMENT JOURNEY

| Expert | Start | Final | Δ |
|--------|-------|-------|---|
| Geoffrey Moore | 5/10 | 7/10 | +2 |
| Sequoia | 6/10 | 8/10 | +2 |
| Aaron Ross | 4/10 | 7/10 | +3 |
| **Avg** | **5.0** | **7.3** | **+2.3** |

✅ Target reached in 2 rounds
```

---

## Difference from `expert-review`

| Aspect | `expert-review` | `expert-improve` |
|--------|-----------------|------------------|
| Purpose | Get feedback | Actually improve |
| Passes | 1 | 2-3 until 7+/10 |
| Output | Insights + actions | Improved version |
| User input | Confirm personas | Confirm once, then auto |
| Speed | Fast (~1 min) | Thorough (~5 min) |
| When | Early drafts | Final deliverables |

---

## Handoff from `expert-review`

If user says "improve this" after running `expert-review`:

```
AI: I have context from the review. Continuing with same personas.

[Skips to improvement phase, uses existing feedback as Round 1]
```

---

*Iterate until excellent. Auto-apply fixes. Track improvement.*
