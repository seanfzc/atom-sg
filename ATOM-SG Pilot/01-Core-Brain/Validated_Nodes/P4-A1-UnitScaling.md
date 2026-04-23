---
node_id: "P4-A1-UnitScaling"
source: "MOE P4 Mathematics"
thread: "Ratio-Scaling Chain"
status: "FORGED — BRIDGE NODE (THREAD A FIX)"
node_type: "BRIDGE (P4)"
triad_axis:
  linguistic:
    keywords: ["if 1 unit is", "find 10 units", "how many altogether", "value of 1 unit"]
    heuristic: "Scaling / Unitary Method"
    trigger: "VALUE OF UNITS"
    linguistic_load: "Low — direct multiplication from known unit value"
  visual:
    template: "Equal Units Model"
    stress_score: 1.5
    description: "A row of identical boxes or bars, each labelled with the same value. Student counts or multiplies to find total."
  logic:
    moe_code: "P4-A1-UnitScaling"
    formula: "$1u = V \\implies nu = n \\times V$"
    steps:
      - "Identify the value of 1 unit"
      - "Determine how many units are needed"
      - "Multiply: total = units × value per unit"
complexity_score: 2.2
vertical_continuity:
  seed_node: "P3-M2-ScaledComparison"
  bridge_logic: "P3: 'Ali has 3 units, Baba has 1 unit. 1 unit = 15.' → P4: 'If 1 unit = 15, then 10 units = 150.' The child moves from KNOWING units to CALCULATING with them."
  boss_target: "ROSYTH-P6-ALG-01"
  boss_bridge: "P4: 'n units = n × 15' → P6: 'x units = 15x'. The numeric multiplier becomes the variable."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "45 seconds"
verb_test: "ACTION: Use unit value to scale to a total."
death_list_check: "CLEAR"
---

## P4-A1-UnitScaling: "If 1 unit is 15, what are 10 units?"

### The Gap This Fills

| From | Missing Step | To |
| :--- | :--- | :--- |
| P3-M2 (1 unit represents 15) | **How to SCALE units to find totals** | ROSYTH-P6-ALG-01 ($15 + 15x$) |

P3 teaches: "1 unit = 15."
P4 teaches: "So $n$ units = $n × 15$. Calculate it."
P6 demands: "$x$ units = $15x$. Express it."

### Problem (P4 Level)

Ali and Baba share stickers in the ratio 3 : 7. If Ali has 15 stickers, how many stickers do they have altogether?

### Solution Logic

1. Ali has 3 units = 15 stickers
2. 1 unit = $15 \div 3 = 5$ stickers
3. Baba has 7 units = $7 \times 5 = 35$ stickers
4. Total = 10 units = $10 \times 5 = 50$ stickers

### Pedagogical Notes

- **Verb Test:** "At this level, the student learns to CALCULATE totals using a known unit value." ✅ ACTION
- **Vertical Thread:** P2 (equal groups of known size) → P3 (units represent a value) → **P4 (scale units to find totals)** → P6 (units become variables: $15x$)

### Level_Config_JSON

```json
{
  "node_id": "P4-A1-UnitScaling",
  "source": "MOE P4 Mathematics",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 2.2,
  "p6_logic": {
    "description": "Scale from known unit value to total. Direct precursor to expressing totals with algebraic variables.",
    "formula": "1u = V → nu = n × V",
    "moe_code": "P4-A1-UnitScaling"
  },
  "age_6_seed": {
    "title": "The Box Packer",
    "precursor_skill": "Equal Groups / Repeated Addition",
    "gameplay": {
      "setup": "A warehouse with identical boxes. Each box has 15 gems. A truck is waiting to be loaded.",
      "mechanic": "Round 1: Load 1 box → truck shows 15 gems. Round 2: Load 3 boxes → 45 gems. Round 3: 'The truck needs 150 gems. How many boxes?' Player counts: 10 boxes. Round 4: 'Now each box has a MYSTERY number of gems. You loaded 4 boxes and got 60 gems. How many in each box?' → 15.",
      "key_insight": "If you know what ONE box holds, you can figure out ANY number of boxes. The number of boxes can change — the gems per box stays the same. In P6, the number of boxes becomes 'x'.",
      "no_symbols": true,
      "visual_language": "Boxes, gems, trucks, loading — NO letters, NO algebra"
    },
    "vertical_link": {
      "seed": "P3-M2-ScaledComparison",
      "bridge": "P3: '1 unit = 15' → P4: '10 units = 150' → P6: 'x units = 15x'"
    }
  }
}
```
