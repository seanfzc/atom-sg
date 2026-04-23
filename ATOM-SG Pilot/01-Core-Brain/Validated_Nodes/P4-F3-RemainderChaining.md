---
node_id: "P4-F3-RemainderChaining"
source: "MOE P4 Mathematics"
thread: "Remainder Pivot Chain (Thread D)"
status: "FORGED — BRIDGE NODE"
node_type: "BRIDGE (P4) — ABSTRACT"
triad_axis:
  linguistic:
    keywords: ["of the remainder", "of what was left", "then from the rest", "remaining portion"]
    heuristic: "Pull-down / Branching"
    trigger: "REMAINDER PIVOT"
    linguistic_load: "High — must track a shifting 'whole' across multiple fractional operations"
  visual:
    template: "Pull-down Bar Model"
    stress_score: 2.8
    description: "A bar that shrinks after the first fraction is removed, then 'drops down' to become a new full-width bar. A second fraction is taken from this new bar. The student sees the whole PIVOTING."
  logic:
    moe_code: "P4-F3-RemainderChaining"
    formula: "$\\text{Part}_2 = \\frac{c}{d} \\times (1 - \\frac{a}{b}) \\times \\text{Total}$"
    steps:
      - "Start with 24 stickers"
      - "Give away 1/4: 24 × 1/4 = 6. Remainder = 18."
      - "PIVOT: 18 is now the new whole."
      - "Take 1/3 of the remainder: 18 × 1/3 = 6."
      - "Final remainder: 18 - 6 = 12."
      - "Check: 6 + 6 + 12 = 24 ✅"
complexity_score: 2.8
vertical_continuity:
  seed_node: "P4-F2-RemainderAction"
  bridge_logic: "P4-F2: 'Take a fraction, count what's left.' P4-F3: 'Take a fraction, PIVOT the remainder to a new whole, take ANOTHER fraction from THAT.' The chain grows from one operation to two — same logic, applied recursively."
  boss_target: "ROSYTH-P6-ALG-04"
  boss_bridge: "P4: 'Take 1/4 of 24, remainder = 18, then 1/3 of 18 = 6' → P6: 'Take 1/4 of x, remainder = 3/4x, then 1/3 of 3/4x = 1/4x.' Numbers become variables, but the PIVOT is identical."
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "120 seconds"
verb_test: "ACTION: Pivot the 'Whole' and apply a second fraction to the remaining portion."
death_list_check: "CLEAR"
---

## P4-F3-RemainderChaining: "The Pivot — When the Remainder Becomes the Whole"

### The Gap This Fills

| From | Missing Step | To |
| :--- | :--- | :--- |
| P4-F2 (take fraction, count remainder) | **Chaining: apply a SECOND fraction to the remainder** | ROSYTH-P6-ALG-04 ($\frac{2}{3} \times \frac{3}{4}x = \frac{1}{2}x$) |

### Problem (P4 Level)

Ali had 24 stickers. He gave $\frac{1}{4}$ to Baba. Then he gave $\frac{1}{3}$ of the REMAINING stickers to Charlie. How many stickers does Ali have left?

### Solution Logic

1. Give 1/4 to Baba: $24 \times \frac{1}{4} = 6$. Remainder: $24 - 6 = 18$
2. **PIVOT:** 18 is now the new whole
3. Give 1/3 of 18 to Charlie: $18 \times \frac{1}{3} = 6$. Remainder: $18 - 6 = 12$
4. Ali has **12** stickers left
5. Check: $6 + 6 + 12 = 24$ ✅

### Visual Guide (Pull-down Bar)

```
STEP 1:  [████████████████████████] = 24 (original whole)
TAKE:    [██████]                   = 6  (1/4 to Baba)
REMAIN:  [██████████████████]       = 18

         ↓ PIVOT ↓

STEP 2:  [██████████████████]       = 18 (NEW whole)
TAKE:    [██████]                   = 6  (1/3 of 18 to Charlie)
REMAIN:  [████████████]             = 12 (final answer)
```

### CLS Gradient Check

- P3-F1 (1.8) → P4-F2 (2.3): CLS = 0.5 ✅
- P4-F2 (2.3) → P4-F3 (2.8): CLS = 0.5 ✅
- P4-F3 (2.8) → ROSYTH-P6-ALG-04 (3.6): CLS = 0.8 ✅
- **Goldilocks slope confirmed: 0.5 → 0.5 → 0.8**

### Level_Config_JSON

```json
{
  "node_id": "P4-F3-RemainderChaining",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 2.8,
  "age_6_seed": {
    "title": "The Pizza Thief (Double Heist)",
    "precursor_skill": "Remainder Action + Fraction of Whole",
    "gameplay": {
      "setup": "A pizza with 24 slices. Pirate 1 takes a quarter. Then Pirate 2 takes a third of what's LEFT.",
      "mechanic": "Round 1: Pirate 1 takes 6 slices (1/4). Pizza shrinks to 18 slices. Round 2: Pizza REDRAWS at full width but labelled '18 slices now.' Pirate 2 takes 1/3 of 18 = 6. Round 3: Player counts final: 12. Key question: 'Did Pirate 2 take 1/3 of 24 or 1/3 of 18?' → 18! The pizza SHRANK.",
      "key_insight": "After each theft, the pizza gets SMALLER. The next fraction applies to the SMALLER pizza. This is the most common mistake in P6 — students apply the second fraction to the original instead of the remainder.",
      "no_symbols": true,
      "visual_language": "Pizza that physically shrinks and redraws, pirates, slice counting"
    },
    "vertical_link": {
      "seed": "P4-F2-RemainderAction",
      "bridge": "P4-F2: 'Take, count what's left' → P4-F3: 'Take, pivot, take AGAIN from what's left' → P6: 'x → 3/4x → 1/3 of 3/4x = 1/4x'"
    }
  }
}
```
