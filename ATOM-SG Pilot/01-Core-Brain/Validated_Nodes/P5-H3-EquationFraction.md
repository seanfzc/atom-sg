---
node_id: "P5-H3-EquationFraction"
source: "ATOM-SG P5 Hybrid Bridge Forge"
thread: "Cross-Thread: C (Equation-Solving) + D (Remainder Pivot)"
status: "FORGED — P5 TRANSITION NODE"
node_type: "BRIDGE (P5) — HYBRID GEARBOX"
nickname: "The Pizza Scientist"
triad_axis:
  linguistic:
    keywords: ["solve", "fraction of x", "find x", "simplify", "clear the denominator"]
    heuristic: "Inverse Operations on Fractional Equations"
    trigger: "INTERNAL TRANSFER + REMAINDER PIVOT"
    linguistic_load: "High — must clear a fraction from an equation before applying standard inverse operations"
  visual:
    template: "Balanced Scale with Fractional Weights"
    stress_score: 3.0
    description: "A scale where one side has a fraction bar (e.g., (3x+5)/4) represented as a pizza cut into 4 slices with 3x+5 toppings. Player must 'multiply both sides by 4' to clear the fraction, then solve normally."
  logic:
    moe_code: "P5-H3-EquationFraction"
    formula: "$\\frac{3x+5}{4} = 8 \\implies 3x+5 = 32 \\implies 3x = 27 \\implies x = 9$"
    steps:
      - "Start: $\\frac{3x+5}{4} = 8$"
      - "Clear fraction: multiply both sides by 4 → $3x + 5 = 32$"
      - "Now it's a standard Thread C equation"
      - "Subtract 5: $3x = 27$"
      - "Divide by 3: $x = 9$"
      - "Check: $\\frac{3(9)+5}{4} = \\frac{32}{4} = 8$ ✅"
complexity_score: 3.4
vertical_continuity:
  parent_thread_C: "P4-A2-BalancingEquations"
  parent_thread_D: "P4-F3-RemainderChaining"
  bridge_logic: "Thread C teaches: 'Balance and apply inverse operations.' Thread D teaches: 'Fractions transform quantities.' P5-H3 FUSES them: 'The fraction IS the equation. Clear it first (Thread D skill), then solve (Thread C skill).'"
  boss_targets: ["ROSYTH-P6-ALG-10"]
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "120 seconds"
verb_test: "ACTION: Clear a fraction from an equation using inverse operations, then solve."
death_list_check: "CLEAR"
dual_parentage:
  thread_C: "P4-A2-BalancingEquations (CLS: 1.0)"
  thread_D: "P4-F3-RemainderChaining (CLS: 0.6)"
  rule_6: "COMPLIANT — dual-parentage established"
---

## P5-H3-EquationFraction: "The Pizza Scientist"

### The Fusion Point

| Thread C (Equations) | + | Thread D (Fractions) | = | P5-H3 |
| :--- | :--- | :--- | :--- | :--- |
| "$3x + 5 = 32$, solve" | | "Clear $\frac{}{4}$ by multiplying" | | "$\frac{3x+5}{4} = 8$. Clear fraction, then solve." |

### Problem (P5 Level)

$\frac{3x + 5}{4} = 8$. Find the value of $x$.

### Solution Logic

1. Clear the fraction: $3x + 5 = 8 \times 4 = 32$
2. Subtract 5: $3x = 27$
3. Divide by 3: $x = 9$
4. Check: $\frac{3(9)+5}{4} = \frac{32}{4} = 8$ ✅

### CLS Gradient

```
P4-A2-BalancingEq (2.4) → P5-H3 (3.4):  CLS = 1.0 ✅
P4-F3-RemainderChain (2.8) → P5-H3 (3.4): CLS = 0.6 ✅
P5-H3 (3.4) → ALG-10 (4.5):              CLS = 1.1 ✅
```

### Level_Config_JSON

```json
{
  "node_id": "P5-H3-EquationFraction",
  "nickname": "The Pizza Scientist",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 3.4,
  "age_6_seed": {
    "title": "The Pizza Scientist",
    "precursor_skill": "Balancing + Fraction Clearing",
    "gameplay": {
      "setup": "A pizza is cut into 4 equal slices. Written on the pizza box: 'Each slice has (3x+5)/4 toppings. The label says 8 toppings per slice.'",
      "mechanic": "Round 1: 'If each of 4 slices has 8 toppings, how many toppings TOTAL?' Player: 4 × 8 = 32. The pizza is now WHOLE — no more slices! Round 2: 'The whole pizza has 3x + 5 = 32 toppings.' Player recognises this as a Scale Master problem! Undo +5: 32 - 5 = 27. Undo ×3: 27 ÷ 3 = 9. Round 3: 'x = 9 toppings per magic ingredient!' Check: 3(9) + 5 = 32, 32/4 = 8 per slice ✅",
      "key_insight": "A fraction in an equation is like a sliced pizza. MULTIPLY to make it whole again — then it becomes a normal equation you already know how to solve. The Pizza Scientist's secret: always make the pizza whole first.",
      "no_symbols": true,
      "visual_language": "Pizza slices reassembling into whole, topping counting, oven reveals — NO formal fraction notation"
    }
  }
}
```
