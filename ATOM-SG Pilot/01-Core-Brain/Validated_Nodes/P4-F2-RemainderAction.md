---
node_id: "P4-F2-RemainderAction"
source: "MOE P4 Mathematics"
thread: "Remainder Pivot Chain (Thread D)"
status: "FORGED — BRIDGE NODE"
node_type: "BRIDGE (P4) — DO"
triad_axis:
  linguistic:
    keywords: ["remainder", "what was left", "remaining", "rest of"]
    heuristic: "Working Backwards / Remainder Pivot"
    trigger: "REMAINDER PIVOT"
    linguistic_load: "Medium — must track what was taken AND what remains, then operate on the remainder"
  visual:
    template: "Pull-down Visual Template"
    stress_score: 2.5
    description: "A bar that SHRINKS after a fraction is removed. The remaining bar is re-drawn at full width to become the 'new whole.' A second fraction is then taken from this new bar."
  logic:
    moe_code: "P4-F2-RemainderAction"
    formula: "$x - \\frac{1}{3}x = \\frac{2}{3}x$ (remainder becomes new whole)"
    steps:
      - "Start with 24 stickers"
      - "Give away 1/3: 24 ÷ 3 = 8 given away"
      - "Remainder: 24 - 8 = 16"
      - "The 16 is now the NEW WHOLE for the next operation"
complexity_score: 2.3
vertical_continuity:
  seed_node: "P3-F1-FractionOfWhole"
  bridge_logic: "P3: 'Take 1/3 of 12 = 4.' P4: 'Take 1/3 of 12 = 4. What's LEFT? 8. Now take 1/4 of THAT 8.' The remainder PIVOTS to become the new input."
  boss_target: "P4-F3-RemainderChaining"
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "60 seconds"
verb_test: "ACTION: Take a fraction away and calculate what REMAINS."
death_list_check: "CLEAR"
---

## P4-F2-RemainderAction: "Take Some, Count What's Left"

### Problem (P4 Level)

Ali had 24 stickers. He gave $\frac{1}{3}$ of them to Baba. How many stickers does Ali have left?

### Solution Logic

1. $\frac{1}{3}$ of 24 = $24 \div 3 = 8$ (given away)
2. Remainder: $24 - 8 = 16$
3. Ali has **16** stickers left

### The Pivot Moment

```
BEFORE:  [████████████████████████] = 24 (full bar)
TAKE:    [████████]                 = 8  (1/3 removed)
AFTER:   [████████████████]         = 16 (2/3 remains — THIS is now the new whole)
```

### Pedagogical Notes

- **Verb Test:** "At this level, the student learns to CALCULATE what remains after a fractional take-away." ✅ ACTION
- **Why the Pull-down Template:** The visual must show the bar SHRINKING. Students need to see that "of the remainder" means the bar gets smaller — not that you go back to the original.

### Level_Config_JSON

```json
{
  "node_id": "P4-F2-RemainderAction",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 2.3,
  "age_6_seed": {
    "title": "The Shrinking Treasure",
    "precursor_skill": "Fraction of a Whole + Subtraction",
    "gameplay": {
      "setup": "A treasure chest with 24 gems. Pirate 1 arrives and takes 'a third.'",
      "mechanic": "Round 1: Pirate takes 8 gems. Chest shrinks visually to show 16 remaining. Round 2: 'How many are LEFT?' Player counts: 16. Round 3: Pirate 2 arrives and wants 'a quarter of what's left' — NOT a quarter of the original! Player must use the SHRUNK chest (16), not the original (24). Quarter of 16 = 4.",
      "key_insight": "Once something is taken away, the pile SHRINKS. The next fraction applies to the SMALLER pile, not the original. This is the hardest concept in remainder problems — and the most common mistake.",
      "no_symbols": true,
      "visual_language": "Treasure chests that physically shrink, pirates, gem piles — NO fractions as symbols"
    },
    "vertical_link": {
      "seed": "P3-F1-FractionOfWhole",
      "bridge": "P3: 'Take 1/3 of 12' → P4: 'Take 1/3, count what's LEFT, then take from THAT' → P6: 'Chain multiple fractional take-aways algebraically'"
    }
  }
}
```
