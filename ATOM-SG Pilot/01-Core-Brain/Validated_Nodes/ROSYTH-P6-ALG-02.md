---
node_id: "ROSYTH-P6-ALG-02"
source: "Rosyth 2026 P6 Math CA1 Q2"
thread: "Algebraic Continuity"
status: "EXTRACTED - AWAITING CEO VERIFICATION"
bimodal_mode: "B (Paper 2 - Odyssey / Heuristic Reasoning)"
complexity_score: 3.8
triad_axis:
  linguistic:
    keywords: ["weights", "heavier than", "equal", "total"]
    heuristic: "Substitution (Comparison Offset)"
    trigger: "CONSTANT DIFFERENCE"
    linguistic_load: "High — requires parsing 'Y kg heavier' as an algebraic offset, then substituting into a total equation"
  visual:
    template: "Comparison Offset"
    stress_score: 3
    description: "Two bar types (Blue/Red) with Red bars visually extending beyond Blue by offset Y. Multi-bar grouping (3 + 5 = 8 bars total)."
  logic:
    moe_code: "P6-A2-Equations"
    formula: "$8b + 5y = 32$ → $b = \\frac{32 - 5y}{8}$"
    steps:
      - "Let Blue weight = $b$, Red weight = $b + y$"
      - "$3b + 5(b + y) = 32$"
      - "$3b + 5b + 5y = 32$"
      - "$8b + 5y = 32$"
      - "$b = \\frac{32 - 5y}{8}$"
vertical_continuity:
  seed_node: "P2-M1-EqualGroups"
  bridge_logic: "Substitution IS Equal Groups with a known difference. P2: '5 groups of 3 = 15'. P6: '5 groups of (b + y)' — the child replaces 'Red' with 'Blue + extra', which is the same as breaking a group into a known part plus an offset."
  secondary_seed: "P1-N2-Comparison"
  secondary_bridge: "'Y kg heavier' maps directly to P1 Comparison (More/Less than)"
death_list_check: "CLEAR"
---

## Question 2 (Rosyth P6 Algebra - Node-02: ODYSSEY)

3 Blue Weights and 5 Red Weights sit on a scale. Together they weigh 32 kg.
A Red Weight is $y$ kg heavier than a Blue Weight.
Find the weight of one Blue Weight in terms of $y$.

### Solution Logic

1. Let Blue weight = $b$, Red weight = $b + y$ (Comparison Offset)
2. Total equation: $3b + 5(b + y) = 32$
3. Expand: $3b + 5b + 5y = 32$
4. Simplify: $8b + 5y = 32$
5. Isolate: $b = \frac{32 - 5y}{8}$

### Pedagogical Notes

- **Why this is Mode B:** Requires multi-step algebraic manipulation, substitution of a comparison offset, and fraction-based result. Not solvable by pattern recognition alone.
- **Vertical Thread:** The child who understood "5 bags of 3 apples" in P2 is now doing "5 groups of (blue + extra)" — same structure, symbolic representation.

### Level_Config_JSON

```json
{
  "node_id": "ROSYTH-P6-ALG-02",
  "source": "Rosyth 2026 P6 Math CA1 Q2",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 3.8,
  "p6_logic": {
    "description": "Substitution with comparison offset. Find unknown weight as fraction involving y.",
    "formula": "b = (32 - 5y) / 8",
    "moe_code": "P6-A2-Equations"
  },
  "age_6_seed": {
    "title": "The Balanced Scale",
    "precursor_skill": "Equal Groups + Comparison (More/Less)",
    "gameplay": {
      "setup": "A giant scale sits in the middle of the screen. On one side: 3 Blue blocks and 5 Red blocks. On the other side: a treasure chest showing '32 gems'. The scale is balanced.",
      "mystery": "A sign says: 'Each Red block has some EXTRA hidden gems inside compared to a Blue block.'",
      "mechanic_round_1": "The extra gems are revealed: each Red block has 2 extra gems. Player must 'peel off' the 2 extra gems from each of the 5 Red blocks. That's 10 gems removed from the treasure side too. Now the scale shows: 8 EQUAL blocks = 22 gems.",
      "mechanic_round_2": "Player divides 22 gems equally among the 8 blocks. Each block = 22/8... the game rounds to whole numbers for Age 6, e.g., extra = 0, so 32/8 = 4 gems each.",
      "key_insight": "By removing the 'extra' from every Red block, you MAKE them equal to Blue. Now you have EQUAL GROUPS — the same skill from P2. The 'taking away the extra to make things equal' IS substitution.",
      "no_symbols": true,
      "visual_language": "Blocks, gems, scale, peeling off extras — NO letters, NO fractions"
    },
    "vertical_link": {
      "seed": "P2-M1-EqualGroups",
      "bridge": "P2: 'Share 15 gems into 5 equal bags' → P6: 'Remove the offset, then share 32-5y gems into 8 equal groups'"
    }
  }
}
```
