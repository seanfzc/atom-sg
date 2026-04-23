---
node_id: "ROSYTH-P6-ALG-08"
source: "Rosyth 2026 P6 Math CA1 Q8"
thread: "C (Equation-Solving) — PURE"
status: "EXTRACTED — CEO VERIFIED"
node_type: "BOSS (P6)"
triad_axis:
  linguistic:
    keywords: ["find the value of", "when", "substitution"]
    heuristic: "Direct Substitution + Simplification"
    trigger: "INTERNAL TRANSFER"
    linguistic_load: "Low — plug in value, compute, simplify fraction"
  visual:
    template: "None (Computational)"
    stress_score: 1
    description: "Pure computation after substitution. No diagram."
  logic:
    moe_code: "P6-A1-Expressions"
    formula: "$\\frac{4(5) + 12}{2} = \\frac{32}{2} = 16$"
    steps:
      - "Substitute $a = 5$: $\\frac{4(5) + 12}{2}$"
      - "Numerator: $20 + 12 = 32$"
      - "Divide: $\\frac{32}{2} = 16$"
complexity_score: 2.5
vertical_continuity:
  seed_node: "P2-N1-MissingVal"
  parent_bridge: "P4-A2-BalancingEquations"
  cls_from_parent: 0.1
  bridge_logic: "P4: 'Substitute a known value into an expression.' P6: 'Substitute, compute numerator, then divide by denominator.'"
bimodal_calibration:
  mode: "A (Paper 1 - Sprint)"
  target_response_time: "30 seconds"
verb_test: "ACTION: Substitute a given value into an expression and evaluate."
death_list_check: "CLEAR"
hybrid_status: "PURE — single thread"
rule_6: "N/A"
---

## Raw Text (Q8)
Find the value of $\frac{4a + 12}{2}$ when $a = 5$.

## LaTeX Cleanup
Find the value of $\frac{4a + 12}{2}$ when $a = 5$.
**Answer:** $\frac{4(5) + 12}{2} = \frac{32}{2} = 16$

## Triad YAML
```yaml
linguistic: "Direct substitution. Trigger: INTERNAL TRANSFER."
visual: "None. Stress: 1."
logic: "P6-A1-Expressions. Formula: $\frac{32}{2} = 16$."
```

### Level_Config_JSON
```json
{
  "node_id": "ROSYTH-P6-ALG-08",
  "bimodal": "Mode A (Sprint)",
  "complexity_score": 2.5,
  "p6_logic": {
    "description": "Substitute value into fractional expression and evaluate.",
    "formula": "(4×5 + 12) / 2 = 32/2 = 16",
    "moe_code": "P6-A1-Expressions"
  },
  "age_6_seed": {
    "title": "The Recipe Machine",
    "precursor_skill": "Substitution / Following Instructions",
    "gameplay": {
      "setup": "A recipe machine says: 'Take your number, multiply by 4, add 12, then cut in half.'",
      "mechanic": "Round 1: Input = 5. Machine: 5 × 4 = 20. Add 12 = 32. Cut in half = 16. Round 2: Input = 3. Machine: 3 × 4 = 12. Add 12 = 24. Half = 12. Round 3: 'What if you put in 10?' Player follows the recipe.",
      "key_insight": "A formula is just a recipe. Put in the ingredient (the number), follow the steps in order, get the result. The recipe never changes — only the ingredient does.",
      "no_symbols": true,
      "visual_language": "Kitchen machine, ingredient slots, step-by-step conveyor"
    }
  }
}
```
