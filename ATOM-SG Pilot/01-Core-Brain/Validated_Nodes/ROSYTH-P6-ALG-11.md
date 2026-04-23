---
node_id: "ROSYTH-P6-ALG-11"
source: "Rosyth 2026 P6 Math CA1 Q11 (4 marks)"
thread: "HYBRID: A (Ratio) + B (Offset) + C (Equations)"
status: "EXTRACTED — AWAITING CEO VERIFICATION"
node_type: "BOSS (P6) — TRIPLE HYBRID — PAPER 2"
triad_axis:
  linguistic:
    keywords: ["ratio", "more than", "altogether", "find", "how many does each have"]
    heuristic: "Ratio Setup + Offset Substitution + Equation Solve"
    trigger: "VALUE OF UNITS + CONSTANT DIFFERENCE + INTERNAL TRANSFER"
    linguistic_load: "Very High — three-thread fusion: establish ratio, apply offset constraint, form equation, solve, verify"
  visual:
    template: "Triple-Layer Bar Model"
    stress_score: 4.0
    description: "Three bars (Ali, Baba, Charlie) drawn with ratio units. One bar has an offset block. Total bar spans all three. Visual must show ratio → offset → equation transformation."
  logic:
    moe_code: "P6-A2-Equations"
    formula: "$2x + (2x + 18) + 5x = 198$"
    steps:
      - "DO Step 1 (Thread A — Ratio): Let Ali = $2x$, Charlie = $5x$"
      - "DO Step 2 (Thread B — Offset): Baba has 18 more than Ali → Baba = $2x + 18$"
      - "DO Step 3 (Thread C — Equation): Total = $2x + (2x + 18) + 5x = 198$"
      - "DO Step 4 (Simplify): $9x + 18 = 198$"
      - "DO Step 5 (Inverse — subtract): $9x = 180$"
      - "DO Step 6 (Inverse — divide): $x = 20$"
      - "DO Step 7 (Substitute back): Ali = $40$, Baba = $58$, Charlie = $100$"
      - "DO Step 8 (Verify): $40 + 58 + 100 = 198$ ✅"
complexity_score: 4.5
vertical_continuity:
  seed_nodes: ["P2-M1-EqualGroups", "P1-N2-Comparison", "P2-N1-MissingVal"]
  parent_bridges:
    thread_A: "P5-H1-RatioEquation"
    thread_B: "P4-M3-OffsetRemoval"
    thread_C: "P4-A2-BalancingEquations"
  cls_check:
    P5_H1_to_this: 1.3
    P4_M3_to_this: "2.0 ⚠️ — mitigated via P5-H1 route"
    P4_A2_to_this: "2.1 ⚠️ — mitigated via P5-H1 route"
    primary_route: "P5-H1 (3.2) → ALG-11 (4.5) = CLS 1.3 ✅"
  bridge_logic: "This is MANY tiny problems stacked: (1) Read the ratio → Thread A skill from P2-M1-EqualGroups. (2) Apply the offset → Thread B skill from P1-N2-Comparison. (3) Form and solve the equation → Thread C skill from P2-N1-MissingVal. A child who mastered each thread separately can now see them COMBINE."
  convergence_note: "THIS IS THE CONVERGENCE POINT — where Thread A, B, and C meet for the first time in a single problem."
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "240 seconds"
  flag: "Boss Fight: FINAL BOSS — Triple-Thread Odyssey"
verb_test: "ACTION: Decompose a multi-constraint word problem into ratio units, offset, and equation — then solve step by step."
death_list_check: "CLEAR"
hybrid_status: "TRIPLE HYBRID — Thread A + Thread B + Thread C"
rule_6: "COMPLIANT — triple-parentage via P5-H1 (A+C) and P4-M3 (B)"
triple_parentage:
  thread_A: "P5-H1-RatioEquation"
  thread_B: "P4-M3-OffsetRemoval"
  thread_C: "P5-H1-RatioEquation (shared bridge)"
  persona_mapping:
    thread_A: "The Box Packer (ratio units)"
    thread_B: "The Balanced Scale (offset removal)"
    thread_C: "The Scale Master (equation solving)"
---

## Raw Text (Q11 — 4 marks)

Ali, Baba, and Charlie have stickers in the ratio $2 : ? : 5$. Baba has $18$ more stickers than Ali. They have $198$ stickers altogether. How many stickers does each person have?

## LaTeX Cleanup

Ali, Baba, and Charlie have stickers. The ratio of Ali's stickers to Charlie's stickers is $2 : 5$. Baba has $18$ more stickers than Ali. They have $198$ stickers altogether. How many stickers does each person have?

**Solution:**
Let Ali = $2x$, Charlie = $5x$.
Baba = Ali + $18$ = $2x + 18$.
Total: $2x + (2x + 18) + 5x = 198$
$9x + 18 = 198$
$9x = 180$
$x = 20$
Ali = $2(20) = 40$
Baba = $2(20) + 18 = 58$
Charlie = $5(20) = 100$
Check: $40 + 58 + 100 = 198$ ✅

## Triad YAML
```yaml
linguistic: "Ratio + Offset + Equation. Triggers: VALUE OF UNITS + CONSTANT DIFFERENCE + INTERNAL TRANSFER."
visual: "Triple-Layer Bar Model. Stress: 4.0."
logic: "P6-A2-Equations. Formula: $9x + 18 = 198$, $x = 20$."
hybrid: "Thread A + B + C. Parents: P5-H1 + P4-M3."
flag: "Boss Fight: FINAL BOSS — Triple-Thread Odyssey."
convergence: "THIS node is where Threads A, B, C converge."
```

## The "Many Tiny Problems" Decomposition

```
YOUR SON SEES:  "Ali, Baba, Charlie... ratio... 18 more... 198 altogether... 😰"

ATOM DECOMPOSITION:

  Tiny Problem 1 (Thread A — P2 Equal Groups skill):
  "Ali and Charlie share in ratio 2:5. Let 1 unit = x."
  → Ali = 2x, Charlie = 5x. Done. ✅

  Tiny Problem 2 (Thread B — P1 Comparison skill):
  "Baba has 18 MORE than Ali."
  → Baba = Ali + 18 = 2x + 18. Done. ✅

  Tiny Problem 3 (Thread C — P2 Missing Value skill):
  "Total = 198. What is x?"
  → 2x + (2x + 18) + 5x = 198
  → 9x + 18 = 198
  → 9x = 180
  → x = 20. Done. ✅

  Tiny Problem 4 (Substitute back):
  → Ali = 40, Baba = 58, Charlie = 100. Check: 198. ✅

EACH TINY PROBLEM IS A SKILL HE ALREADY HAS.
The "Boss" is just stacking them.
```

### Level_Config_JSON

```json
{
  "node_id": "ROSYTH-P6-ALG-11",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 4.5,
  "hybrid": true,
  "threads": ["A", "B", "C"],
  "flag": "Boss Fight: FINAL BOSS — Triple-Thread",
  "convergence_point": true,
  "p6_logic": {
    "description": "Three-person ratio with offset constraint. Form and solve multi-variable equation.",
    "formula": "9x + 18 = 198 → x = 20",
    "moe_code": "P6-A2-Equations",
    "do_steps": 8
  },
  "age_6_seed": {
    "title": "The Triple Treasure (Boss of Bosses)",
    "precursor_skill": "Box Packer + Balanced Scale + Scale Master",
    "gameplay": {
      "setup": "Three pirates find a treasure of 198 gems. Captain's rule: 'Ali gets 2 shares, Charlie gets 5 shares. But Baba always gets 18 EXTRA gems on top of Ali's share.'",
      "mechanic": "Phase 1 (Ratio — Box Packer): Player sets up boxes. Ali: 2 boxes. Charlie: 5 boxes. Phase 2 (Offset — Balanced Scale): Baba gets the same as Ali PLUS 18 extra gems placed in a side pouch. Phase 3 (Equation — Scale Master): All gems must add up to 198. Player: 'Ali's 2 boxes + Baba's 2 boxes + 18 extra + Charlie's 5 boxes = 198.' That's 9 boxes + 18 = 198. Remove the 18: 9 boxes = 180. Each box = 20. Phase 4 (Reveal): Ali = 40, Baba = 58, Charlie = 100. Check: 198! ✅",
      "key_insight": "A scary big problem is just THREE tiny games you already know how to play: count the boxes (ratio), handle the extra (offset), solve the equation (balance). Stack them, and you beat the Boss.",
      "no_symbols": true,
      "visual_language": "Three pirate treasure piles, boxes, side pouches for extras, a grand scale"
    },
    "vertical_links": [
      {"seed": "P2-M1-EqualGroups", "skill": "Count boxes (ratio)"},
      {"seed": "P1-N2-Comparison", "skill": "Handle the extra (offset)"},
      {"seed": "P2-N1-MissingVal", "skill": "Solve the equation (balance)"}
    ]
  }
}
```
