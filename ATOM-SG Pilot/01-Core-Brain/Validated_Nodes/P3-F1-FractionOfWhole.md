---
node_id: "P3-F1-FractionOfWhole"
source: "MOE P3 Mathematics"
thread: "Remainder Pivot Chain (Thread D)"
status: "FORGED — BRIDGE NODE"
node_type: "BRIDGE (P3) — KNOW"
triad_axis:
  linguistic:
    keywords: ["fraction of", "one-third of", "half of", "a quarter of"]
    heuristic: "Part-Whole (Fractional)"
    trigger: "REMAINDER PIVOT"
    linguistic_load: "Low — direct calculation of a fraction of a given quantity"
  visual:
    template: "Part-Whole Bar (Fractional Shading)"
    stress_score: 1.5
    description: "A single bar divided into equal sections. Some sections are shaded to represent the fraction taken."
  logic:
    moe_code: "P3-F1-FractionOfWhole"
    formula: "$\\frac{1}{3} \\times 12 = 4$"
    steps:
      - "Divide 12 into 3 equal parts"
      - "Each part = 4"
      - "1/3 of 12 = 4"
complexity_score: 1.8
vertical_continuity:
  seed_node: "P1-N2-Subtraction"
  bridge_logic: "P1: 'I had 12, took away 4, have 8 left.' P3: 'I had 12, took away 1/3 (which IS 4), have 8 left.' Same action, fractional language."
  boss_target: "P4-F2-RemainderAction"
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "30 seconds"
verb_test: "ACTION: Calculate a fraction OF a given quantity."
death_list_check: "CLEAR"
---

## P3-F1-FractionOfWhole: "What is 1/3 of 12?"

### Problem (P3 Level)

Ali has 12 stickers. He gives $\frac{1}{3}$ of them to Baba. How many stickers does he give away?

### Solution Logic

1. Divide 12 into 3 equal groups: $12 \div 3 = 4$
2. $\frac{1}{3}$ of $12 = 4$
3. Ali gives away 4 stickers

### Pedagogical Notes

- **Verb Test:** "At this level, the student learns to CALCULATE a fraction of a quantity." ✅ ACTION
- **Vertical Thread:** P1 (take away 4) → **P3 (take away 1/3, which is 4)** → P4 (take away 1/3, then calculate what REMAINS)

### Level_Config_JSON

```json
{
  "node_id": "P3-F1-FractionOfWhole",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 1.8,
  "age_6_seed": {
    "title": "The Pizza Slicer",
    "precursor_skill": "Subtraction (Taking Away)",
    "gameplay": {
      "setup": "A whole pizza with 12 slices. A friend asks for 'a third' of the pizza.",
      "mechanic": "Round 1: Pizza shows 12 slices in 3 equal colour groups (4 red, 4 blue, 4 green). Friend takes one colour group. Player counts: 4 slices given. Round 2: Pizza has 15 slices, 3 groups of 5. Friend takes one group. Round 3: 'How many slices are LEFT?' — introduction of remainder.",
      "key_insight": "A fraction is just a way of saying 'divide into equal groups, then take some.' It's the same as sharing — which you already know.",
      "no_symbols": true,
      "visual_language": "Pizzas, slices, colour groups — NO fraction notation"
    },
    "vertical_link": {
      "seed": "P1-N2-Subtraction",
      "bridge": "P1: 'Take away 4' → P3: 'Take away one-third (which IS 4)' → P6: 'Take away 1/3 of x'"
    }
  }
}
```
