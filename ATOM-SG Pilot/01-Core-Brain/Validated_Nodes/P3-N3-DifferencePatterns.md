---
node_id: "P3-N3-DifferencePatterns"
source: "ATOM-SG Bridge Forge — Mission 2"
thread: "Algebraic Continuity"
status: "FORGED — BRIDGE NODE"
node_type: "BRIDGE (P3)"
triad_axis:
  linguistic:
    keywords: ["older than", "heavier than", "more than", "difference", "years later"]
    heuristic: "Comparison / Constant Difference"
    trigger: "CONSTANT DIFFERENCE"
    linguistic_load: "Medium — requires understanding that a difference remains constant across transformations"
  visual:
    template: "Comparison Model with Shaded Difference Box"
    stress_score: 2
    description: "Two horizontal bars. Bar A (longer) and Bar B (shorter). The gap between Bar A's end and Bar B's end is SHADED and labelled as the 'Difference'. This shaded box stays the same size regardless of what happens to both bars."
  logic:
    moe_code: "P3-N3-DifferencePatterns"
    formula: "$(A + x) - (B + x) = A - B$ (Difference is invariant)"
    steps:
      - "Ali is 8 years old, Baba is 5 years old. Difference = 3."
      - "In 10 years: Ali = 18, Baba = 15. Difference = still 3."
      - "The SHADED BOX never changes size."
death_list_compliance:
  check: "CLEAR"
  note: "This is a P3 comparison/difference concept. NOT a P6 'Speed' problem. Speed involves distance/time/rate calculations — this involves static age/weight differences. Auditor confirms: no Death List violation."
  speed_trap_verification: "The word 'years later' could superficially resemble time-based speed problems. However, the logic axis confirms this is CONSTANT DIFFERENCE (algebraic offset), not SPEED (rate × time = distance). No rate calculation is involved."
vertical_continuity:
  seed_node: "P1-N2-Comparison"
  bridge_logic: "P1: 'Ali has 3 MORE than Baba' → P3: 'Ali is ALWAYS 3 years older, no matter when you check' → P6: 'Red weight is y kg HEAVIER than Blue' ($b + y$)"
  boss_target: "ROSYTH-P6-ALG-02"
  boss_bridge: "P3: 'The difference stays the same' → P6: 'Substitute Red = Blue + y'. The shaded difference box BECOMES the algebraic offset variable."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "45 seconds"
  complexity_score: 1.8
---

## P3-N3-DifferencePatterns: The Shaded Difference Box

### Problem (P3 Level)

Ali is 8 years old. Baba is 5 years old. In 10 years, what will be the difference in their ages?

### Solution Logic

1. Current difference: $8 - 5 = 3$ years
2. In 10 years: Ali = $18$, Baba = $15$
3. Difference: $18 - 15 = 3$ years
4. **The difference never changes.**

### Visual Guide

```
Ali:   [████████████████████] 18
Baba:  [█████████████████]   15
                          [///] ← Shaded Difference = 3 (CONSTANT)
```

### Pedagogical Notes

- **Why this is a Bridge:** The "shaded difference box" is the visual precursor to the algebraic offset. In P6, when a student sees "$y$ kg heavier," they should visualise this exact shaded box — it's the same concept, just with a letter instead of a number.
- **Death List Compliance:** The word "years later" might trigger a false positive for "Speed." The Auditor confirms this is CONSTANT DIFFERENCE logic (static offset), NOT speed/rate logic. No distance or rate calculations are involved.
- **Vertical Thread:** P1 (3 more than) → P3 (always 3 more, shaded box) → P6 ($b + y$, algebraic offset)

### Level_Config_JSON

```json
{
  "node_id": "P3-N3-DifferencePatterns",
  "source": "ATOM-SG Bridge Forge",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 1.8,
  "p6_logic": {
    "description": "Constant difference across transformations. Precursor to algebraic offset substitution.",
    "formula": "(A + x) - (B + x) = A - B",
    "moe_code": "P3-N3-DifferencePatterns"
  },
  "age_6_seed": {
    "title": "The Magic Gap",
    "precursor_skill": "Comparison (More/Less Than)",
    "gameplay": {
      "setup": "Two towers of blocks on screen. Tower A has 8 blocks. Tower B has 5 blocks. A glowing gap between their tops is highlighted.",
      "mechanic": "Round 1: Player adds 2 blocks to BOTH towers. A: 10, B: 7. The gap is STILL 3. Round 2: Player adds 5 more to BOTH. A: 15, B: 12. Gap: STILL 3. Round 3: Player tries to CHANGE the gap by adding to only one tower. NOW the gap changes. Key moment: 'The gap only stays the same when you do the SAME thing to both!'",
      "key_insight": "The difference between two things stays the same if you add or remove the same amount from both. This is the foundation of constant difference — and later, algebraic offset.",
      "no_symbols": true,
      "visual_language": "Block towers, glowing gaps, adding/removing blocks — NO numbers shown as equations"
    },
    "vertical_link": {
      "seed": "P1-N2-Comparison",
      "bridge": "P1: 'Ali has 3 more' → P3: 'The gap is always 3' → P6: 'The offset is y'"
    }
  }
}
```
