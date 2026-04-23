---
node_id: "ROSYTH-P6-ALG-04"
source: "Rosyth 2026 P6 Math CA1 Q4"
thread: "Remainder Pivot Chain (Thread D)"
status: "EXTRACTED — AWAITING CEO VERIFICATION"
node_type: "BOSS (P6)"
triad_axis:
  linguistic:
    keywords: ["spent", "of her money", "of the remainder", "of what was left", "how much at first"]
    heuristic: "Working Backwards / Remainder Pivot"
    trigger: "REMAINDER PIVOT + FRACTIONAL TRANSFER"
    linguistic_load: "High — requires chaining two fractional operations on a diminishing whole, then working backwards from final value"
  visual:
    template: "Pull-down Bar Model (Abstract)"
    stress_score: 3.6
    description: "Bar shrinks twice. Original bar → first remainder bar → second remainder bar. Each pull-down represents a fractional take-away. Final remainder is given; student works backwards."
  logic:
    moe_code: "P6-A3-WordProbs"
    formula: "$\\frac{2}{3} \\times \\frac{3}{4}x = \\frac{1}{2}x = 24 \\implies x = 48$"
    steps:
      - "Let total money = $x$"
      - "Spent $\\frac{1}{4}$ on books: remainder = $\\frac{3}{4}x$"
      - "PIVOT: $\\frac{3}{4}x$ is the new whole"
      - "Spent $\\frac{1}{3}$ of remainder on food: $\\frac{1}{3} \\times \\frac{3}{4}x = \\frac{1}{4}x$"
      - "Left: $\\frac{3}{4}x - \\frac{1}{4}x = \\frac{2}{4}x = \\frac{1}{2}x$"
      - "$\\frac{1}{2}x = 24 \\implies x = 48$"
      - "Check: Books = 12, Food = 12, Left = 24. Total: 48 ✅"
complexity_score: 3.6
vertical_continuity:
  seed_node: "P1-N2-Subtraction"
  bridge_chain:
    - node: "P3-F1-FractionOfWhole"
      role: "KNOW — a fraction represents a part of a quantity"
      cls_to_next: 0.5
    - node: "P4-F2-RemainderAction"
      role: "DO — take a fraction, calculate what remains"
      cls_to_next: 0.5
    - node: "P4-F3-RemainderChaining"
      role: "ABSTRACT — chain multiple fractional take-aways, pivot the whole"
      cls_to_next: 0.8
  bridge_logic: "P1: 'Had 10, gave 3, have 7' → P3: '1/3 of 12 = 4' → P4-F2: 'Take 1/4, remainder = 18' → P4-F3: 'Take from remainder, pivot, take again' → P6: 'Chain with variables: 3/4x → 1/3 of 3/4x → solve'"
  boss_bridge: "The concrete pizza slices and shrinking treasure chests become algebraic fractions of x. The PIVOT logic is identical — only the representation changes."
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "180 seconds"
verb_test: "ABSTRACT: Simplify nested fractional variables into a single expression and solve."
death_list_check: "CLEAR — pure fraction/algebra, no speed/compass/cells"
---

## Question 4 (Rosyth P6 Algebra - Node-04: Thread D Boss)

Mei had some money. She spent $\frac{1}{4}$ of it on books. She then spent $\frac{1}{3}$ of the remainder on food. She had $24 left. How much money did Mei have at first?

### Solution Logic

1. Let total = $x$
2. Spent on books: $\frac{1}{4}x$. Remainder: $\frac{3}{4}x$
3. **PIVOT:** $\frac{3}{4}x$ is the new whole
4. Spent on food: $\frac{1}{3} \times \frac{3}{4}x = \frac{1}{4}x$
5. Left: $\frac{3}{4}x - \frac{1}{4}x = \frac{1}{2}x$
6. $\frac{1}{2}x = 24 \implies x = 48$
7. Check: Books = $12, Food = $12, Left = $24. Total: $48 ✅

### Visual Guide (Pull-down Bar)

```
STEP 1:  [████████████████████████████████████████████████] = x (full bar)
BOOKS:   [████████████]                                     = 1/4x (spent)
REMAIN:  [████████████████████████████████████]              = 3/4x

         ↓ PIVOT ↓

STEP 2:  [████████████████████████████████████]              = 3/4x (NEW whole)
FOOD:    [████████████]                                     = 1/3 of 3/4x = 1/4x
REMAIN:  [████████████████████████]                          = 2/3 of 3/4x = 1/2x

         ↓ SOLVE ↓

         1/2x = 24 → x = 48
```

### The Complete Thread D Chain

```
P1-N2-Subtraction    P3-F1-FractionOfWhole    P4-F2-RemainderAction    P4-F3-RemainderChaining    ROSYTH-P6-ALG-04
────────────────     ────────────────────     ────────────────────     ──────────────────────     ────────────────
"Had 10, gave 3,     "1/3 of 12 = 4"         "Take 1/4, count        "Take, PIVOT, take         "1/4x spent, 1/3
 have 7 left"                                  what's LEFT: 18"        again from remainder"      of 3/4x spent,
                                                                                                   1/2x = 24, x=48"

Complexity: ~1.0     Complexity: 1.8          Complexity: 2.3          Complexity: 2.8            Complexity: 3.6
              CLS=0.8 ✅         CLS=0.5 ✅           CLS=0.5 ✅              CLS=0.8 ✅
```

### v2.0 Verification Checklist

| Rule | Check | Result |
| :--- | :--- | :--- |
| **Rule 1: Verb Test** | P3-F1: "Calculate fraction of" ✅ P4-F2: "Take and count remainder" ✅ P4-F3: "Pivot and chain" ✅ ALG-04: "Simplify nested fractions" ✅ | ✅ ALL ACTION |
| **Rule 2: CLS** | 0.8 → 0.5 → 0.5 → 0.8 | ✅ ALL ≤ 1.5 |
| **Rule 3: KNOW/DO/ABSTRACT** | KNOW: P3-F1 ✅ DO: P4-F2 ✅ ABSTRACT: P4-F3 + ALG-04 ✅ | ✅ COMPLETE |
| **Rule 4: Pre-Flight** | All nodes have atomic files, CLS scores, verb tests ✅ | ✅ PASS |
| **Rule 5: Forge-Before-Extract** | P3-F1, P4-F2, P4-F3 all forged BEFORE this Boss ✅ | ✅ COMPLIANT |
| **Death List** | No speed, compass, or cells ✅ | ✅ CLEAR |

### Level_Config_JSON

```json
{
  "node_id": "ROSYTH-P6-ALG-04",
  "source": "Rosyth 2026 P6 Math CA1 Q4",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 3.6,
  "p6_logic": {
    "description": "Chained remainder pivot with two fractional take-aways. Solve for original from final remainder.",
    "formula": "(2/3) × (3/4)x = (1/2)x = 24 → x = 48",
    "moe_code": "P6-A3-WordProbs"
  },
  "age_6_seed": {
    "title": "The Greedy Banker",
    "precursor_skill": "Remainder Chaining + Working Backwards",
    "gameplay": {
      "setup": "A piggy bank full of coins. Two 'bankers' visit. Banker 1 takes a quarter of the coins. Banker 2 takes a third of what's LEFT. The piggy bank shows 24 coins remaining.",
      "mechanic": "Round 1 (Forward): Piggy bank has 48 coins. Banker 1 takes 12 (1/4). Piggy bank shrinks to 36. Banker 2 takes 12 (1/3 of 36). Piggy bank shrinks to 24. 'See? 24 left!' Round 2 (Backwards — the real game): Piggy bank shows 24 coins. Sign says 'Banker 2 took 1/3 of what was here.' Player must figure out: 'If 24 is 2/3, then 1/3 = 12, so BEFORE Banker 2 there were 36.' Then: 'Banker 1 took 1/4 of the ORIGINAL. If 36 is 3/4, then 1/4 = 12, so original = 48.' Round 3: Different numbers, same logic. Player builds confidence that the PATTERN never changes.",
      "key_insight": "Working backwards through TWO shrinks. Each banker takes from a DIFFERENT-sized pile. The pile BEFORE Banker 2 is NOT the original pile. You must undo each step in reverse order — last banker first.",
      "no_symbols": true,
      "visual_language": "Piggy banks that shrink, banker characters, coin piles, reverse arrows — NO fractions as symbols"
    },
    "vertical_link": {
      "seed": "P1-N2-Subtraction",
      "bridge": "P1: 'Had 10, gave 3' → P3: '1/3 of 12' → P4: 'Take, count remainder, PIVOT' → P6: 'Chain two pivots with variables, solve backwards'"
    }
  }
}
```
