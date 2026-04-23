---
node_id: "P3-M2-ScaledComparison"
source: "ATOM-SG Bridge Forge — Mission 2"
thread: "Algebraic Continuity"
status: "FORGED — BRIDGE NODE"
node_type: "BRIDGE (P3)"
triad_axis:
  linguistic:
    keywords: ["times as many", "if 1 unit represents", "how many units", "altogether"]
    heuristic: "Use Equations / Proportional Reasoning"
    trigger: "VALUE OF UNITS"
    linguistic_load: "Low-Medium — 'If 1 unit represents...' is the conceptual gateway to algebraic variables"
  visual:
    template: "Equal Units Bar Model"
    stress_score: 2
    description: "Two bars drawn with clearly labelled units. Bar A has 3 units, Bar B has 1 unit. Each unit is the same size. Total = 4 units."
  logic:
    moe_code: "P3-M2-ScaledComparison"
    formula: "If $A = 3B$, then Total $= A + B = 3B + B = 4B$"
    steps:
      - "Ali has 3 times as many stickers as Baba"
      - "Let Baba's stickers = 1 unit"
      - "Ali's stickers = 3 units"
      - "Total = 3 + 1 = 4 units"
      - "If 1 unit represents 15, then Total = 4 × 15 = 60"
vertical_continuity:
  seed_node: "P2-M1-EqualGroups"
  bridge_logic: "P2: '3 groups of 5 = 15' → P3: '3 units of Baba = Ali'. The child transitions from counting equal physical groups to treating abstract 'units' as equal groups."
  boss_target: "ROSYTH-P6-ALG-01"
  boss_bridge: "P3: '1 unit represents 15' → P6: '1 unit represents 15, x units represents 15x'. The concept of 'unit value' IS the variable."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "60 seconds"
  complexity_score: 1.5
death_list_check: "CLEAR"
---

## P3-M2-ScaledComparison: "If 1 unit represents..."

### Problem (P3 Level)

Ali has 3 times as many stickers as Baba. Together they have 60 stickers. How many stickers does Baba have?

### Solution Logic

1. Let Baba's stickers = 1 unit
2. Ali's stickers = 3 units
3. Total = 4 units = 60
4. 1 unit = $60 \div 4 = 15$
5. Baba has 15 stickers

### Pedagogical Notes

- **Why this is a Bridge:** This is where "equal groups" (P2) becomes "units" (P3). The phrase "If 1 unit represents..." is the linguistic precursor to the algebraic variable. In P6, "1 unit" becomes "$x$".
- **Vertical Thread:** P2 (5 groups of 3) → P3 (1 unit = 15, 3 units = 45) → P6 ($1:x$, 1 unit = 15, $x$ units = $15x$)

### Level_Config_JSON

```json
{
  "node_id": "P3-M2-ScaledComparison",
  "source": "ATOM-SG Bridge Forge",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 1.5,
  "p6_logic": {
    "description": "Scaled comparison using unit model. Precursor to ratio with unknown variable.",
    "formula": "A = 3B, Total = 4B",
    "moe_code": "P3-M2-ScaledComparison"
  },
  "age_6_seed": {
    "title": "The Unit Factory",
    "precursor_skill": "Equal Groups / Repeated Addition",
    "gameplay": {
      "setup": "A factory has two machines. Machine A makes 3 boxes for every 1 box Machine B makes. A conveyor belt shows the boxes lining up.",
      "mechanic": "Round 1: Machine B makes 1 box, Machine A makes 3. Player counts total: 4 boxes. Round 2: Each box has 5 gems inside. Player counts total gems: 4 × 5 = 20. Round 3: 'How many gems does Machine B's box have?' → 5. The boxes are the UNITS.",
      "key_insight": "Every box (unit) holds the SAME number of gems. Once you know what 1 box holds, you know everything. This is the seed of '1 unit represents...'",
      "no_symbols": true,
      "visual_language": "Factories, conveyor belts, boxes, gems — NO letters"
    },
    "vertical_link": {
      "seed": "P2-M1-EqualGroups",
      "bridge": "P2: '3 bags of 5' → P3: '3 units of [unknown]' → P6: '3 units of x'"
    }
  }
}
```
