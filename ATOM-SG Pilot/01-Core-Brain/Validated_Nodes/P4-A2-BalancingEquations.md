---
node_id: "P4-A2-BalancingEquations"
source: "MOE P4 Mathematics"
thread: "Equation-Solving Chain"
status: "FORGED — BRIDGE NODE (THREAD C UNBLOCK)"
node_type: "BRIDGE (P4)"
triad_axis:
  linguistic:
    keywords: ["is the same as", "equals", "balance", "both sides", "if I add to one side"]
    heuristic: "Balancing / Scales"
    trigger: "INTERNAL TRANSFER"
    linguistic_load: "Medium — requires understanding that equality is maintained by performing the same operation on both sides"
  visual:
    template: "Balanced Scale Model"
    stress_score: 2.0
    description: "A seesaw or balance scale with blocks/weights on both sides. Adding or removing from one side requires the same action on the other to maintain balance."
  logic:
    moe_code: "P4-A2-BalancingEquations"
    formula: "$\\text{Left} = \\text{Right} \\implies x + a = b$"
    steps:
      - "Both sides of the scale are equal"
      - "To keep balance, do the SAME thing to both sides"
      - "Remove known values from both sides to isolate the unknown"
      - "Example: x + 5 = 12 → remove 5 from both sides → x = 7"
complexity_score: 2.4
vertical_continuity:
  seed_node: "P2-N1-MissingVal"
  bridge_logic: "P2: 'What number + 5 = 12? Try numbers until it works.' → P4: 'The scale is balanced. Remove 5 from BOTH sides. Now x = 7.' The child moves from GUESSING the missing value to DEDUCING it through a systematic operation."
  boss_target: "P6-A2-Equations"
  boss_bridge: "P4: 'Remove 5 from both sides' → P6: '$3x + 5 = 20$ → subtract 5 → $3x = 15$ → divide by 3 → $x = 5$'. Same logic, more steps."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "60 seconds"
verb_test: "ACTION: Balance two sides of an equation by removing/adding equal parts."
death_list_check: "CLEAR"
---

## P4-A2-BalancingEquations: "Make Both Sides Equal"

### The Gap This Fills

| From | Missing Step | To |
| :--- | :--- | :--- |
| P2-N1 (45 + ? = 60, guess) | **The concept of EQUALITY and INVERSE OPERATIONS** | P6-A2 ($3x + 5 = 20$, solve) |

P2 teaches: "Find the missing number" (trial and error).
P4 teaches: "Both sides are equal. Undo operations systematically."
P6 demands: "Apply inverse operations across multiple steps."

### Problem (P4 Level)

A balance scale has blocks on both sides. On the left: a mystery bag and 5 blocks. On the right: 12 blocks. How many blocks are in the mystery bag?

### Solution Logic

1. Left side: mystery bag + 5 blocks = Right side: 12 blocks
2. Remove 5 blocks from BOTH sides (to keep balance)
3. Left side: mystery bag = Right side: 7 blocks
4. The mystery bag has 7 blocks

### Pedagogical Notes

- **Verb Test:** "At this level, the student learns to BALANCE an equation by performing equal operations on both sides." ✅ ACTION
- **Why this matters:** This is the conceptual leap from "guess the number" to "deduce the number." Without this, students face P6 equation-solving with no systematic method.
- **Vertical Thread:** P2 (guess missing value) → **P4 (balance both sides, inverse operations)** → P6 (multi-step algebraic solving)

### Level_Config_JSON

```json
{
  "node_id": "P4-A2-BalancingEquations",
  "source": "MOE P4 Mathematics",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 2.4,
  "p6_logic": {
    "description": "Introduce equality concept via balanced scales. Teach inverse operations to isolate unknowns.",
    "formula": "Left = Right → x + a = b → x = b - a",
    "moe_code": "P4-A2-BalancingEquations"
  },
  "age_6_seed": {
    "title": "The Scale Master",
    "precursor_skill": "Missing Values / Comparison",
    "gameplay": {
      "setup": "A giant seesaw in a playground. On one side: a locked treasure box and 5 toy blocks. On the other side: 12 toy blocks. The seesaw is perfectly balanced.",
      "mechanic": "Round 1: 'The seesaw is balanced — both sides weigh the same!' Round 2: Player removes 1 block from the RIGHT side. Seesaw tilts! 'Oops — remove 1 from the LEFT too!' Round 3: Player removes 5 blocks from BOTH sides. Left: just the treasure box. Right: 7 blocks. 'The treasure box weighs the same as 7 blocks!' Round 4: Harder — treasure box + 3 blocks = 15 blocks. Player removes 3 from both sides → box = 12.",
      "key_insight": "Whatever you do to one side, you MUST do to the other. This is not just a rule — it's the reason equations WORK. The seesaw is the equation.",
      "no_symbols": true,
      "visual_language": "Seesaws, toy blocks, treasure boxes — NO letters, NO equals signs"
    },
    "vertical_link": {
      "seed": "P2-N1-MissingVal",
      "bridge": "P2: 'What + 5 = 12? Try 7!' → P4: 'Remove 5 from both sides → x = 7' → P6: '3x + 5 = 20 → 3x = 15 → x = 5'"
    }
  }
}
```
