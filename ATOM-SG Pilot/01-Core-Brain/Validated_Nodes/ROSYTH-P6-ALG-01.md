---
node_id: "ROSYTH-P6-ALG-01"
source: "Rosyth 2026 P6 Math CA1"
thread: "Algebraic Continuity"
status: "EXTRACTED - AWAITING CEO VERIFICATION"
triad_axis:
  linguistic: "Keywords: 'ratio', 'in terms of x'. Heuristic: Use Equations / Algebra. Trigger: VALUE OF UNITS."
  visual: "Template: Comparison Bar Model. Stress_Score: 1 (Baseline - single comparison, direct labels)."
  logic: "MOE Code: P6-A1-Expressions. Formula: $15 + 15x$ or $15(1 + x)$."
vertical_continuity:
  seed_node: "P1-N1-PartWhole"
  bridge_logic: "Direct mapping from 'Parts' to 'Units'. P1: 1 part Ali, unknown parts Baba. P6: 1 unit Ali ($15$), $x$ units Baba ($15x$)."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "45 seconds"
death_list_check: "CLEAR"
---

## Question 1 (Rosyth P6 Algebra Test - Node-01)

The ratio of the number of stickers Ali has to the number of stickers
Baba has is $1 : x$.
If Ali has $15$ stickers, find the total number of stickers they have
altogether in terms of $x$.

[Image: bar_model_ali_baba.png]

### Solution Logic

- Ali has $15$ stickers (1 unit = $15$)
- Baba has $x$ units → $15x$ stickers
- Total = $15 + 15x = 15(1 + x)$

### Level_Config_JSON

```json
{
  "node_id": "ROSYTH-P6-ALG-01",
  "source": "Rosyth 2026 P6 Math CA1 Q1",
  "p6_logic": {
    "description": "Ratio 1:x with known unit value. Find total in terms of x.",
    "formula": "15 + 15x = 15(1 + x)",
    "moe_code": "P6-A1-Expressions",
    "bimodal": "Mode A (Fluency, ~45s)"
  },
  "age_6_seed": {
    "title": "Mystery Box Gems",
    "precursor_skill": "Repeated Addition / Equal Groups",
    "gameplay": {
      "setup": "Player sees 1 basket with 3 gems (visible). Next to it are Mystery Boxes. Each Mystery Box contains the SAME number of gems, but the player can't see inside.",
      "mechanic": "Round 1: 2 Mystery Boxes appear. Each has 3 gems (revealed after guess). Total = 3 + 3 + 3 = 9. Round 2: 4 Mystery Boxes. Player counts equal groups: 3 + 3 + 3 + 3 + 3 = 15. Round 3: The number of boxes changes each time, but the gems per box stays the same. Player learns: 'The answer changes, but the PATTERN stays the same.'",
      "key_insight": "The Mystery Box IS the variable. The child learns that the structure (equal groups of a known size) holds regardless of how many boxes appear — which is exactly what 15x means.",
      "no_symbols": true,
      "visual_language": "Baskets, gems, Mystery Boxes — NO letters, NO 'x'"
    },
    "vertical_link": {
      "seed": "P1-N1-PartWhole",
      "bridge": "P1: 'How many parts make the whole?' → P6: 'How many units of 15 make the total?'"
    }
  }
}
```
