---
node_id: "ROSYTH-P6-ALG-06"
source: "Rosyth 2026 P6 Math CA1 Q6"
thread: "B (Redistribution/Offset) — PURE"
status: "EXTRACTED — CEO VERIFIED"
node_type: "BOSS (P6)"
triad_axis:
  linguistic:
    keywords: ["more than", "express", "in terms of", "total"]
    heuristic: "Comparison Offset + Expression"
    trigger: "CONSTANT DIFFERENCE"
    linguistic_load: "Low-Medium — translate a 'more than' relationship into algebraic terms and sum"
  visual:
    template: "Comparison Bar with Offset"
    stress_score: 1.5
    description: "Two bars: Bag = k, Box = k + 12. Total bar spans both."
  logic:
    moe_code: "P6-A1-Expressions"
    formula: "$k + (k + 12) = 2k + 12$"
    steps:
      - "Bag has $k$ marbles"
      - "Box has $k + 12$ marbles (12 more than bag)"
      - "Total: $k + k + 12 = 2k + 12$"
complexity_score: 2.8
vertical_continuity:
  seed_node: "P1-N2-Comparison"
  parent_bridge: "P3-N3-DifferencePatterns"
  cls_from_parent: 1.0
  bridge_logic: "P3: 'The difference is always 12.' P6: 'Express as k and k+12, then add.'"
bimodal_calibration:
  mode: "A (Paper 1 - Sprint)"
  target_response_time: "45 seconds"
verb_test: "ACTION: Translate a comparison relationship into an algebraic expression and simplify."
death_list_check: "CLEAR"
hybrid_status: "PURE — single thread (B)"
rule_6: "N/A"
---

## Raw Text (Q6)
A bag has $k$ marbles. A box has 12 more marbles than the bag. Express the total marbles in terms of $k$.

## LaTeX Cleanup
A bag has $k$ marbles. A box has $12$ more marbles than the bag. Express the total number of marbles in terms of $k$.
**Answer:** $2k + 12$

## Triad YAML
```yaml
linguistic: "Offset comparison → expression. Trigger: CONSTANT DIFFERENCE."
visual: "Comparison Bar with Offset. Stress: 1.5."
logic: "P6-A1-Expressions. Formula: $2k + 12$."
```

### Level_Config_JSON
```json
{
  "node_id": "ROSYTH-P6-ALG-06",
  "bimodal": "Mode A (Sprint)",
  "complexity_score": 2.8,
  "p6_logic": {
    "description": "Express total of two quantities where one exceeds the other by a constant.",
    "formula": "k + (k + 12) = 2k + 12",
    "moe_code": "P6-A1-Expressions"
  },
  "age_6_seed": {
    "title": "The Magic Gap (Level 2)",
    "precursor_skill": "Comparison (More/Less) + Counting",
    "gameplay": {
      "setup": "Two jars: Blue jar has some marbles. Red jar has 12 MORE than Blue jar.",
      "mechanic": "Round 1: Blue has 10. Red has 10 + 12 = 22. Total: 32. Round 2: Blue has 5. Red has 17. Total: 22. Round 3: 'What if Blue has MYSTERY marbles?' Blue: mystery. Red: mystery + 12. Total: 2 mysteries + 12. The gap is ALWAYS 12.",
      "key_insight": "If you double the mystery and add the gap, you always get the total. The gap never changes — only the mystery does.",
      "no_symbols": true,
      "visual_language": "Jars, marbles, visible gap blocks"
    }
  }
}
```
