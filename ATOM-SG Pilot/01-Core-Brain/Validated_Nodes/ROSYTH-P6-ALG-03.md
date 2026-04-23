---
node_id: "ROSYTH-P6-ALG-03"
source: "Rosyth 2026 P6 Math CA1 Q3"
thread: "Equation-Solving Chain"
status: "EXTRACTED — AWAITING CEO VERIFICATION"
node_type: "BOSS (P6)"
triad_axis:
  linguistic:
    keywords: ["solve", "find the value of", "equation", "unknown"]
    heuristic: "Use Equations / Inverse Operations"
    trigger: "INTERNAL TRANSFER"
    linguistic_load: "Medium-High — requires parsing a two-step equation and applying inverse operations in sequence"
  visual:
    template: "Balanced Scale Model (Abstract)"
    stress_score: 2
    description: "No physical diagram required. The equation itself IS the visual — two sides of an equals sign. Students who internalised the P4 seesaw now see $3x + 5 = 20$ as a balanced scale."
  logic:
    moe_code: "P6-A2-Equations"
    formula: "$3x + 5 = 20$"
    steps:
      - "Identify the equation: $3x + 5 = 20$"
      - "Inverse of +5: subtract 5 from both sides → $3x = 15$"
      - "Inverse of ×3: divide both sides by 3 → $x = 5$"
      - "Check: $3(5) + 5 = 15 + 5 = 20$ ✅"
complexity_score: 3.5
vertical_continuity:
  seed_node: "P2-N1-MissingVal"
  bridge_chain:
    - node: "P3-N4-InverseOperations"
      role: "KNOW — every operation has an inverse"
      cls_to_next: 0.4
    - node: "P4-A2-BalancingEquations"
      role: "DO — apply inverses on both sides of a balanced scale"
      cls_to_next: 1.1
  bridge_logic: "P2: 'Guess ? + 5 = 12' → P3: 'Undo: 12 − 5 = 7' → P4: 'Remove from BOTH sides of the scale' → P6: 'Chain two inverse operations: subtract then divide'"
  boss_bridge: "The P4 seesaw becomes the equals sign. The toy blocks become algebraic terms. The treasure box becomes x."
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey / Heuristic Reasoning)"
  target_response_time: "90 seconds"
verb_test: "ACTION: Solve a two-step linear equation by chaining inverse operations."
death_list_check: "CLEAR — pure algebra, no speed/compass/cells"
---

## Question 3 (Rosyth P6 Algebra - Node-03: Thread C Boss)

Solve the equation: $3x + 5 = 20$

### Solution Logic

1. Start: $3x + 5 = 20$
2. Subtract 5 from both sides: $3x = 15$
3. Divide both sides by 3: $x = 5$
4. Check: $3(5) + 5 = 15 + 5 = 20$ ✅

### The Complete Thread C Chain

```
P2-N1-MissingVal          P3-N4-InverseOps           P4-A2-BalancingEq          ROSYTH-P6-ALG-03
─────────────────         ─────────────────          ─────────────────          ─────────────────
"? + 5 = 12"         →   "Undo: 12 − 5 = 7"    →   "Remove from BOTH      →   "3x + 5 = 20
 Try numbers!"            Every + has a −"            sides of the scale"        → 3x = 15
                                                                                  → x = 5"

Complexity: ~1.0          Complexity: 2.0             Complexity: 2.4            Complexity: 3.5
                   CLS=1.0 ✅            CLS=0.4 ✅             CLS=1.1 ✅
```

### v2.0 Verification Checklist

| Rule | Check | Result |
| :--- | :--- | :--- |
| **Rule 1: Verb Test** | P3-N4: "Reverse an operation" ✅ P4-A2: "Balance both sides" ✅ P6-03: "Solve by chaining inverses" ✅ | ✅ ALL ACTION |
| **Rule 2: CLS** | P2→P3: 1.0 ✅ P3→P4: 0.4 ✅ P4→P6: 1.1 ✅ | ✅ ALL ≤ 1.5 |
| **Rule 3: KNOW/DO/ABSTRACT** | KNOW: P3-N4 (inverse ops exist) ✅ DO: P4-A2 (apply on balanced scale) ✅ ABSTRACT: ALG-03 (chain in symbolic equation) ✅ | ✅ COMPLETE |
| **Rule 4: Pre-Flight** | All nodes have atomic files, complexity scores, verb tests ✅ | ✅ PASS |
| **Rule 5: Forge-Before-Extract** | P3-N4 and P4-A2 forged BEFORE this Boss was extracted ✅ | ✅ COMPLIANT |
| **Death List** | No speed, compass, or cells ✅ | ✅ CLEAR |

### Pedagogical Notes

- **Bimodal:** Mode B — Although $3x + 5 = 20$ appears simple, the TWO-STEP inverse chain elevates it beyond fluency. Students must plan the sequence (subtract first, then divide) rather than pattern-match.
- **Vertical Thread:** This is the culmination of Thread C. A student who played "The Undo Machine" (P3) and "The Scale Master" (P4) should see this equation as: "The machine did ×3 then +5 to get 20. Undo: −5 then ÷3."

### Level_Config_JSON

```json
{
  "node_id": "ROSYTH-P6-ALG-03",
  "source": "Rosyth 2026 P6 Math CA1 Q3",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 3.5,
  "p6_logic": {
    "description": "Two-step linear equation. Apply chained inverse operations to isolate x.",
    "formula": "3x + 5 = 20 → x = 5",
    "moe_code": "P6-A2-Equations"
  },
  "age_6_seed": {
    "title": "The Double Undo Machine",
    "precursor_skill": "Inverse Operations (single step) + Balancing",
    "gameplay": {
      "setup": "The Undo Machine from P3 has been UPGRADED. Now it does TWO things: first it multiplies, then it adds. Out comes the number 20.",
      "mechanic": "Round 1: Machine shows its steps: [?] → ×3 → [??] → +5 → [20]. Player must press UNDO twice. First undo: 20 − 5 = 15. Second undo: 15 ÷ 3 = 5. 'You put in 5!' Round 2: Different machine: [?] → ×2 → +7 → [19]. Undo: 19 − 7 = 12, 12 ÷ 2 = 6. Round 3: Machine does THREE things. Player chains three undos. The pattern is always the same: undo the LAST thing first.",
      "key_insight": "To undo a chain of operations, you reverse the ORDER and flip each operation. Last in, first out. This is EXACTLY how you solve 3x + 5 = 20: undo the +5 first (subtract), then undo the ×3 (divide).",
      "no_symbols": true,
      "visual_language": "Upgraded machine, conveyor belt with multiple stations, reverse buttons — NO algebra"
    },
    "vertical_link": {
      "seed": "P2-N1-MissingVal",
      "bridge": "P2: 'Guess the input' → P3: 'Single undo' → P4: 'Undo on balanced scale' → P6: 'Chain two undos on 3x + 5 = 20'"
    }
  }
}
```
