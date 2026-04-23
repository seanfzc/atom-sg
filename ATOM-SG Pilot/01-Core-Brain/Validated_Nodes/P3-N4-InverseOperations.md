---
node_id: "P3-N4-InverseOperations"
source: "MOE P3 Mathematics"
thread: "Equation-Solving Chain"
status: "FORGED — BRIDGE NODE (THREAD C)"
node_type: "BRIDGE (P3)"
triad_axis:
  linguistic:
    keywords: ["I started with", "then I added", "the answer was", "what did I start with", "undo", "reverse"]
    heuristic: "Working Backwards"
    trigger: "INVERSE OPERATIONS"
    linguistic_load: "Medium — requires understanding that every operation has an opposite that 'undoes' it"
  visual:
    template: "Arrow Flow (Forward → Reverse)"
    stress_score: 2
    description: "A horizontal flow diagram showing forward operations (left to right) and then the same diagram reversed (right to left) with inverse operations labelled. The student traces the arrows backwards."
  logic:
    moe_code: "P3-N4-InverseOperations"
    formula: "If $? + 5 = 12$, then $12 - 5 = ?$. If $? \\times 3 = 18$, then $18 \\div 3 = ?$."
    steps:
      - "Read the problem forwards: ? → (+5) → 12"
      - "Reverse the arrows: 12 → (−5) → ?"
      - "Calculate: 12 − 5 = 7"
      - "Check: 7 + 5 = 12 ✅"
complexity_score: 2.0
vertical_continuity:
  seed_node: "P2-N1-MissingVal"
  bridge_logic: "P2: 'What + 5 = 12? Try numbers!' (trial and error). P3: 'Addition undoes subtraction. So subtract 5 from 12.' The child moves from GUESSING to SYSTEMATIC REVERSAL."
  boss_target: "P4-A2-BalancingEquations"
  boss_bridge: "P3: 'Undo one operation' → P4: 'Undo operations on a balanced scale' → P6: 'Undo multiple operations: $3x + 5 = 20$ → $3x = 15$ → $x = 5$'"
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "30 seconds"
verb_test: "ACTION: Reverse an operation to find the starting value."
death_list_check: "CLEAR"
---

## P3-N4-InverseOperations: "Undo It to Find It"

### The Gap This Fills

| From | Missing Step | To |
| :--- | :--- | :--- |
| P2-N1 ($45 + ? = 60$, guess) | **The concept that operations can be REVERSED** | P4-A2 (Balance both sides systematically) |

P2 teaches: "Find the missing number" (trial and error).
P3 teaches: "Every operation has an OPPOSITE. Use it."
P4 teaches: "Apply inverses systematically on a balanced scale."
P6 demands: "Chain multiple inverse operations to solve $3x + 5 = 20$."

### Problem (P3 Level)

I'm thinking of a number. I add 8 to it and get 23. What is my number?

### Solution Logic

1. Forward: $? + 8 = 23$
2. Inverse of "add 8" is "subtract 8"
3. $23 - 8 = 15$
4. Check: $15 + 8 = 23$ ✅
5. My number is **15**

### Visual Guide

```
FORWARD:   [?] ──(+8)──▶ [23]

REVERSE:   [23] ──(−8)──▶ [15] ✅
```

### Multi-Step Example (P3 Extension)

I'm thinking of a number. I multiply it by 3, then add 2, and get 17. What is my number?

```
FORWARD:   [?] ──(×3)──▶ [??] ──(+2)──▶ [17]

REVERSE:   [17] ──(−2)──▶ [15] ──(÷3)──▶ [5] ✅

Check: 5 × 3 = 15, 15 + 2 = 17 ✅
```

### Pedagogical Notes

- **Verb Test:** "At this level, the student learns to REVERSE operations to find starting values." ✅ ACTION
- **Why this is CRITICAL for Thread C:** Without inverse operations, students arrive at P4 BalancingEquations with no concept of HOW to "remove 5 from both sides." They need to know that subtraction UNDOES addition before they can apply it systematically.
- **Cognitive Leap Score:**
  - P2-N1 (est. 1.0) → P3-N4 (2.0): CLS = 1.0 ✅
  - P3-N4 (2.0) → P4-A2 (2.4): CLS = 0.4 ✅
  - P4-A2 (2.4) → P6-A2 Boss (est. 3.5): CLS = 1.1 ✅

### Level_Config_JSON

```json
{
  "node_id": "P3-N4-InverseOperations",
  "source": "MOE P3 Mathematics",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 2.0,
  "p6_logic": {
    "description": "Introduce inverse operations as a systematic method to find unknowns. Precursor to equation solving.",
    "formula": "If ? + a = b, then ? = b − a",
    "moe_code": "P3-N4-InverseOperations"
  },
  "age_6_seed": {
    "title": "The Undo Machine",
    "precursor_skill": "Missing Values (Trial and Error)",
    "gameplay": {
      "setup": "A magical machine sits on a table. You put a number in one end, it does something (adds, multiplies), and a different number comes out the other end.",
      "mechanic": "Round 1: Player puts in 5, machine adds 3, out comes 8. 'What did the machine do?' → Added 3. Round 2: Out comes 11, machine added 4. 'What went IN?' Player must think: 'Undo the +4 → 11 − 4 = 7.' Round 3: Machine does TWO things — multiplies by 2, then adds 1. Out comes 9. Player reverses: 9 − 1 = 8, 8 ÷ 2 = 4. 'You put in 4!'",
      "key_insight": "Every machine action has a REVERSE button. Adding has subtracting. Multiplying has dividing. If you know what came OUT and what the machine DID, you can always figure out what went IN. This is exactly how equations work.",
      "no_symbols": true,
      "visual_language": "Machines, conveyor belts, forward/reverse buttons, number tokens — NO algebra symbols"
    },
    "vertical_link": {
      "seed": "P2-N1-MissingVal",
      "bridge": "P2: 'Guess what went in' → P3: 'Reverse the machine to find what went in' → P4: 'Balance the scale by reversing' → P6: 'Solve 3x + 5 = 20 by reversing steps'"
    }
  }
}
```
