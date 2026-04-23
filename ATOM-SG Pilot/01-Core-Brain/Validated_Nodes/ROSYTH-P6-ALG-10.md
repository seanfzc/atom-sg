---
node_id: "ROSYTH-P6-ALG-10"
source: "Rosyth 2026 P6 Math CA1 Q10"
thread: "HYBRID: C (Equation-Solving) + D (Remainder Pivot)"
status: "EXTRACTED — CEO VERIFIED"
node_type: "BOSS (P6) — HYBRID"
triad_axis:
  linguistic:
    keywords: ["half of", "poured", "then added", "express in terms of"]
    heuristic: "Remainder Pivot + Expression Building"
    trigger: "REMAINDER PIVOT + INTERNAL TRANSFER"
    linguistic_load: "Medium — sequential operations on a variable quantity: halve, then add"
  visual:
    template: "Pull-down Bar + Addition Block"
    stress_score: 2.0
    description: "Container bar halved (pull-down to show half poured into tank), then a +5 block added to the tank bar."
  logic:
    moe_code: "P6-A1-Expressions"
    formula: "$\\frac{w}{2} + 5$"
    steps:
      - "Container has $w$ liters"
      - "Half poured into tank: $\\frac{w}{2}$"
      - "5 liters added to tank: $\\frac{w}{2} + 5$"
complexity_score: 3.0
vertical_continuity:
  seed_nodes: ["P2-N1-MissingVal", "P1-N2-Subtraction"]
  parent_bridges:
    thread_C: "P4-A2-BalancingEquations"
    thread_D: "P4-F2-RemainderAction"
    hybrid: "P5-H3-EquationFraction"
  cls_check:
    P5_H3_to_this: 0.4
    P4_A2_to_this: 0.6
    P4_F2_to_this: 0.7
  bridge_logic: "Thread D: 'Take a fraction (half) of a quantity.' Thread C: 'Build an expression from operations.' P5-H3 bridges both: 'Work with fractions inside expressions.' Q10 applies: halve w, then add 5."
bimodal_calibration:
  mode: "A (Paper 1 - Sprint)"
  target_response_time: "45 seconds"
verb_test: "ACTION: Apply sequential operations (halve, then add) to form an expression in terms of a variable."
death_list_check: "CLEAR — no speed/volume/compass. 'Liters' is a measurement context, not a Volume topic per Death List."
hybrid_status: "HYBRID — Thread C + Thread D"
rule_6: "COMPLIANT — dual-parentage via P5-H3-EquationFraction (Pizza Scientist)"
dual_parentage:
  thread_C: "P4-A2-BalancingEquations"
  thread_D: "P4-F2-RemainderAction"
  hybrid_bridge: "P5-H3-EquationFraction (Pizza Scientist)"
  persona_mapping:
    thread_C: "The Scale Master (expression building)"
    thread_D: "The Shrinking Treasure (halving)"
    hybrid: "The Pizza Scientist (fractions in expressions)"
---

## Raw Text (Q10)
A container has $w$ liters of water. Half of the water is poured into a tank. $5$ liters of water are then added to the tank. Express the water in the tank in terms of $w$.

## LaTeX Cleanup
A container has $w$ liters of water. Half of the water is poured into a tank. $5$ liters of water are then added to the tank. Express the water in the tank in terms of $w$.
**Answer:** $\frac{w}{2} + 5$

## Triad YAML
```yaml
linguistic: "Remainder pivot (half) + addition. Triggers: REMAINDER PIVOT + INTERNAL TRANSFER."
visual: "Pull-down Bar + Addition Block. Stress: 2.0."
logic: "P6-A1-Expressions. Formula: $\frac{w}{2} + 5$."
hybrid: "Thread C + Thread D. Parent: P5-H3-EquationFraction (Pizza Scientist)."
```

### Level_Config_JSON
```json
{
  "node_id": "ROSYTH-P6-ALG-10",
  "bimodal": "Mode A (Sprint)",
  "complexity_score": 3.0,
  "hybrid": true,
  "threads": ["C", "D"],
  "p6_logic": {
    "description": "Sequential operations on a variable: halve then add a constant.",
    "formula": "w/2 + 5",
    "moe_code": "P6-A1-Expressions"
  },
  "age_6_seed": {
    "title": "The Water Pourer",
    "precursor_skill": "Halving (Pizza Scientist) + Adding",
    "gameplay": {
      "setup": "A big jug with 'w' cups of water. An empty fish tank next to it.",
      "mechanic": "Round 1: w = 20. Pour HALF into the tank: 10 cups. Add 5 more cups. Tank has 15. Round 2: w = 30. Pour half: 15. Add 5: 20. Round 3: w = MYSTERY. Pour half: mystery ÷ 2. Add 5: mystery ÷ 2 + 5. 'The recipe is always: half, then add 5. No matter how much water you start with!'",
      "key_insight": "Two operations in sequence: first HALVE (a fraction operation — Thread D), then ADD (a constant — Thread C). The operations are separate steps, but together they make one expression.",
      "no_symbols": true,
      "visual_language": "Jugs, fish tanks, pouring animations, cup counting"
    }
  }
}
```
