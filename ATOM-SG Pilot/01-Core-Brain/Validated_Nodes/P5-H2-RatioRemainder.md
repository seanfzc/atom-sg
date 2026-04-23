---
node_id: "P5-H2-RatioRemainder"
source: "ATOM-SG P5 Hybrid Bridge Forge"
thread: "Cross-Thread: A (Ratio-Scaling) + D (Remainder Pivot)"
status: "FORGED — P5 TRANSITION NODE"
node_type: "BRIDGE (P5) — HYBRID GEARBOX"
triad_axis:
  linguistic:
    keywords: ["shared in the ratio", "gave away a fraction of his share", "how many left", "of his portion"]
    heuristic: "Ratio Split → Fractional Take-Away"
    trigger: "VALUE OF UNITS + REMAINDER PIVOT"
    linguistic_load: "High — must first SPLIT by ratio, then apply a fraction to ONE part only"
  visual:
    template: "Split Bar → Pull-down on One Segment"
    stress_score: 3.0
    description: "A bar is first SPLIT into ratio segments (e.g., 2:3). Then ONE segment undergoes a pull-down fractional take-away. The other segment remains untouched. Student must track which portion shrinks."
  logic:
    moe_code: "P5-H2-RatioRemainder"
    formula: "Split: $\\frac{2}{5} \\times 60 = 24$ (Ali's share). Take: $\\frac{1}{4} \\times 24 = 6$ given away. Left: $24 - 6 = 18$."
    steps:
      - "Total: 60 marbles, ratio Ali:Baba = 2:3"
      - "Ali's share: 2/5 × 60 = 24"
      - "Ali gives away 1/4 of HIS share: 1/4 × 24 = 6"
      - "Ali has left: 24 - 6 = 18"
      - "Baba untouched: 36"
      - "New total held: 18 + 36 = 54"
complexity_score: 3.3
vertical_continuity:
  parent_thread_A: "P4-A1-UnitScaling"
  parent_thread_D: "P4-F2-RemainderAction"
  bridge_logic: "Thread A teaches: 'Split a total into ratio units.' Thread D teaches: 'Take a fraction and count the remainder.' P5-H2 FUSES them: 'Split by ratio FIRST, then apply a fractional take-away to ONE person's share only.'"
  boss_targets: ["ROSYTH-P6-ALG-09"]
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "120 seconds"
verb_test: "ACTION: Apply a fraction to ONE part of a ratio, then recalculate the total."
death_list_check: "CLEAR"
dual_parentage:
  thread_A: "P4-A1-UnitScaling (CLS: 1.1)"
  thread_D: "P4-F2-RemainderAction (CLS: 1.0)"
  rule_6: "COMPLIANT — dual-parentage established"
---

## P5-H2-RatioRemainder: "Split Then Shrink"

### The Fusion Point

| Thread A (Ratio) | + | Thread D (Remainder) | = | P5-H2 |
| :--- | :--- | :--- | :--- | :--- |
| "Ratio 2:3, Ali gets 24" | | "Take 1/4, remainder = 18" | | "Split by ratio, THEN take a fraction of one share" |

### Problem (P5 Level)

Ali and Baba share 60 marbles in the ratio $2:3$. Ali gives away $\frac{1}{4}$ of his marbles to Charlie. How many marbles does Ali have left?

### Solution Logic

1. Total units: $2 + 3 = 5$
2. Ali's share: $\frac{2}{5} \times 60 = 24$ marbles
3. Ali gives away: $\frac{1}{4} \times 24 = 6$ marbles
4. Ali has left: $24 - 6 = 18$ marbles ✅

### The Critical Distinction

```
⚠️ THE TRAP: "1/4 of his marbles" = 1/4 of ALI'S SHARE (24)
              NOT 1/4 of the TOTAL (60)

The fraction applies to ONE PART of the ratio, not the whole.
This is where Thread A (ratio) and Thread D (remainder) COLLIDE.
```

### CLS Gradient

```
P4-A1-UnitScaling (2.2) → P5-H2 (3.3): CLS = 1.1 ✅
P4-F2-RemainderAction (2.3) → P5-H2 (3.3): CLS = 1.0 ✅
P5-H2 (3.3) → ALG-09 (4.0):               CLS = 0.7 ✅
```

### Level_Config_JSON

```json
{
  "node_id": "P5-H2-RatioRemainder",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 3.3,
  "age_6_seed": {
    "title": "The Shared Treasure (Split & Shrink)",
    "precursor_skill": "Unit Scaling + Remainder Action",
    "gameplay": {
      "setup": "Two pirates split a treasure chest of 60 gems in ratio 2:3. Pirate 1 gets 24 gems, Pirate 2 gets 36 gems. Then Pirate 1 gives away some of HIS gems.",
      "mechanic": "Phase 1 (Split): Gems pour into two piles by ratio. Pile 1: 24. Pile 2: 36. Phase 2 (Shrink): Pirate 1's pile shrinks — he gives away 1/4 (6 gems). His pile is now 18. KEY QUESTION: 'Did he give away 1/4 of ALL the gems or 1/4 of HIS gems?' → HIS gems! Pirate 2's pile is untouched.",
      "key_insight": "When someone gives away a fraction of THEIR share, you must know THEIR share first (from the ratio). The fraction applies to the PART, not the WHOLE. Split first, shrink second.",
      "no_symbols": true,
      "visual_language": "Two separate gem piles (colour-coded), one pile physically shrinks while the other stays — NO fractions as symbols"
    }
  }
}
```
