---
node_id: "P5-H1-RatioEquation"
source: "ATOM-SG P5 Hybrid Bridge Forge"
thread: "Cross-Thread: A (Ratio-Scaling) + C (Equation-Solving)"
status: "FORGED — P5 TRANSITION NODE"
node_type: "BRIDGE (P5) — HYBRID GEARBOX"
triad_axis:
  linguistic:
    keywords: ["ratio", "total", "find the value of x", "altogether", "how many does each have"]
    heuristic: "Ratio Setup → Equation Solving"
    trigger: "VALUE OF UNITS + INTERNAL TRANSFER"
    linguistic_load: "Medium-High — must translate a ratio relationship INTO an equation, then solve"
  visual:
    template: "Equal Units Bar → Balanced Scale (transition)"
    stress_score: 2.5
    description: "Starts as a comparison bar model (ratio units), then TRANSFORMS into a balanced equation. The visual bridge shows the bar model collapsing into Left = Right."
  logic:
    moe_code: "P5-H1-RatioEquation"
    formula: "$x + 3x = 48 \\implies 4x = 48 \\implies x = 12$"
    steps:
      - "Ali has x stickers, Baba has 3x stickers (ratio 1:3)"
      - "Total: x + 3x = 48"
      - "Simplify: 4x = 48"
      - "Solve: x = 12"
      - "Ali has 12, Baba has 36. Check: 12 + 36 = 48 ✅"
complexity_score: 3.2
vertical_continuity:
  parent_thread_A: "P4-A1-UnitScaling"
  parent_thread_C: "P4-A2-BalancingEquations"
  bridge_logic: "Thread A teaches: '1 unit = value, scale to total.' Thread C teaches: 'Balance both sides, apply inverse.' P5-H1 FUSES them: 'Express the ratio as units of x, set up an equation for the total, then balance and solve.'"
  boss_targets: ["ROSYTH-P6-ALG-07"]
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "60 seconds"
verb_test: "ACTION: Set up a ratio AS an equation and solve for the unknown."
death_list_check: "CLEAR"
dual_parentage:
  thread_A: "P4-A1-UnitScaling (CLS: 1.0)"
  thread_C: "P4-A2-BalancingEquations (CLS: 0.8)"
  rule_6: "COMPLIANT — dual-parentage established"
---

## P5-H1-RatioEquation: "When Ratios Become Equations"

### The Fusion Point

| Thread A (Ratio) | + | Thread C (Equations) | = | P5-H1 |
| :--- | :--- | :--- | :--- | :--- |
| "1 unit = 12, 3 units = 36" | | "$4x = 48$, solve" | | "Ratio 1:3, total 48. $x + 3x = 48$. Solve." |

### Problem (P5 Level)

Ali and Baba share stickers in the ratio $1:3$. They have 48 stickers altogether. How many stickers does Ali have?

### Solution Logic

1. Let Ali = $x$, Baba = $3x$ (ratio expressed as algebra)
2. Total: $x + 3x = 48$
3. Simplify: $4x = 48$
4. Divide both sides by 4: $x = 12$
5. Ali has 12 stickers ✅

### CLS Gradient

```
P4-A1-UnitScaling (2.2) → P5-H1 (3.2): CLS = 1.0 ✅
P4-A2-BalancingEq (2.4) → P5-H1 (3.2): CLS = 0.8 ✅
P5-H1 (3.2) → ALG-07 (3.8):            CLS = 0.6 ✅
```

### Level_Config_JSON

```json
{
  "node_id": "P5-H1-RatioEquation",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 3.2,
  "age_6_seed": {
    "title": "The Box Scale",
    "precursor_skill": "Unit Scaling + Balancing",
    "gameplay": {
      "setup": "A scale with boxes on both sides. Left side: 1 small box (Ali's). Right side: 3 small boxes (Baba's). A sign says 'Total: 48 gems across ALL boxes.'",
      "mechanic": "Round 1: 'All boxes are the same size.' Player counts: 4 boxes total. 48 ÷ 4 = 12 gems per box. Round 2: Ali's 1 box = 12 gems. Baba's 3 boxes = 36 gems. Round 3: Different ratio (2:5), total 70. Player: 7 boxes, 70 ÷ 7 = 10 each. The RATIO tells you how many boxes. The TOTAL tells you how to fill them.",
      "key_insight": "A ratio is just a way of counting boxes. Once you know the total gems and the total boxes, you DIVIDE — which is the same as solving an equation.",
      "no_symbols": true,
      "visual_language": "Boxes on scales, gem piles, counting groups — NO algebra"
    }
  }
}
```
