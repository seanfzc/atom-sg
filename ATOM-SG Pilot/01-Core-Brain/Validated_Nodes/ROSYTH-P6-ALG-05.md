---
node_id: "ROSYTH-P6-ALG-05"
source: "Rosyth 2026 P6 Math CA1 Q5"
thread: "A (Ratio-Scaling) — PURE"
status: "EXTRACTED — CEO VERIFIED"
node_type: "BOSS (P6)"
triad_axis:
  linguistic:
    keywords: ["simplify", "expression", "collect like terms"]
    heuristic: "Direct Simplification"
    trigger: "VALUE OF UNITS"
    linguistic_load: "Low — direct like-term collection with both positive and negative terms"
  visual:
    template: "None (Abstract symbolic)"
    stress_score: 1
    description: "Pure symbolic manipulation. No diagram."
  logic:
    moe_code: "P6-A1-Expressions"
    formula: "$7x + 15 - 3x - 4 = 4x + 11$"
    steps:
      - "Group x-terms: $7x - 3x = 4x$"
      - "Group constants: $15 - 4 = 11$"
      - "Result: $4x + 11$"
complexity_score: 2.6
vertical_continuity:
  seed_node: "P1-N1-PartWhole"
  parent_bridge: "P4-A1-UnitScaling"
  cls_from_parent: 0.4
  bridge_logic: "P4: 'Units can be grouped and scaled.' P6: 'x-terms are units — group positives and negatives separately.'"
bimodal_calibration:
  mode: "A (Paper 1 - Sprint)"
  target_response_time: "30 seconds"
verb_test: "ACTION: Collect positive and negative like terms to simplify."
death_list_check: "CLEAR"
hybrid_status: "PURE — single thread"
rule_6: "N/A"
---

## Raw Text (Q5)
Simplify the expression $7x + 15 - 3x - 4$.

## LaTeX Cleanup
Simplify $7x + 15 - 3x - 4$.
**Answer:** $4x + 11$

## Triad YAML
```yaml
linguistic: "Collect like terms (positive and negative). Trigger: VALUE OF UNITS."
visual: "None. Stress: 1."
logic: "P6-A1-Expressions. Formula: $4x + 11$."
```

### Level_Config_JSON
```json
{
  "node_id": "ROSYTH-P6-ALG-05",
  "bimodal": "Mode A (Sprint)",
  "complexity_score": 2.6,
  "p6_logic": {
    "description": "Simplify expression with positive and negative x-terms and constants.",
    "formula": "7x + 15 - 3x - 4 = 4x + 11",
    "moe_code": "P6-A1-Expressions"
  },
  "age_6_seed": {
    "title": "The Gem Sorter",
    "precursor_skill": "Grouping / Part-Whole",
    "gameplay": {
      "setup": "A messy table: 7 red gems, 15 blue gems, 3 cracked red gems, 4 cracked blue gems.",
      "mechanic": "Step 1: Group reds — 7 good, 3 cracked. Keep 4 good reds. Step 2: Group blues — 15 good, 4 cracked. Keep 11 good blues. Final: 4 red + 11 blue.",
      "key_insight": "Sort by type, remove the damaged ones. Same colour = same group. In algebra, same letter = same group.",
      "no_symbols": true,
      "visual_language": "Coloured gems, sorting trays, cracked vs whole"
    }
  }
}
```
