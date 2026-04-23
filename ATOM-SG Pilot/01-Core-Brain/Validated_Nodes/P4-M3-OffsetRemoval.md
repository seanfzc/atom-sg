---
node_id: "P4-M3-OffsetRemoval"
source: "ATOM-SG Bridge Forge — Mission 2 (Gap Fix)"
thread: "Algebraic Continuity (Thread B: Redistribution/Offset)"
status: "FORGED — BRIDGE NODE (CRITICAL GAP FIX)"
node_type: "BRIDGE (P4)"
triad_axis:
  linguistic:
    keywords: ["extra", "more than", "remove the difference", "make them equal", "same amount"]
    heuristic: "Comparison / Internal Transfer"
    trigger: "CONSTANT DIFFERENCE + INTERNAL TRANSFER"
    linguistic_load: "Medium — requires understanding that removing a known offset from each unequal item creates equal groups"
  visual:
    template: "Comparison Model with Removable Offset Blocks"
    stress_score: 3
    description: "Two types of bars (e.g., Red and Blue). Red bars are visibly longer than Blue bars by a shaded 'extra' block. The extra blocks can be 'snapped off' to reveal equal-length bars underneath. Once snapped, all bars become equal groups."
  logic:
    moe_code: "P4-M3-OffsetRemoval"
    formula: "Total - (n × extra) = Equal Groups × count"
    steps:
      - "3 Blue bags and 5 Red bags weigh 47 kg total"
      - "Each Red bag weighs 2 kg MORE than each Blue bag"
      - "Step 1: 'Un-snap' the extra from each Red bag: 5 × 2 = 10 kg removed"
      - "Step 2: New total = 47 - 10 = 37 kg"
      - "Step 3: Now all 8 bags are EQUAL: 37 ÷ 8 = 4.625 kg each"
      - "(Whole-number version: 5 Red × 2 extra = 10. 40 - 10 = 30. 30 ÷ 6 = 5 kg each)"
vertical_continuity:
  seed_node: "P2-M1-EqualGroups"
  bridge_from: "P3-N3-DifferencePatterns"
  bridge_logic: "P3 teaches that a DIFFERENCE is constant. P4 teaches what to DO with that difference: REMOVE it to create equal groups. This is the missing 'action step' between knowing the offset exists and algebraically substituting it out."
  boss_target: "ROSYTH-P6-ALG-02"
  boss_bridge: "P4: 'Remove 2 kg extra from each of 5 Red bags, then divide equally' → P6: 'Substitute Red = Blue + y, expand, collect like terms, isolate b'. The manual un-snapping IS algebraic substitution."
bimodal_calibration:
  mode: "A (Paper 1 - Fluency)"
  target_response_time: "90 seconds"
  complexity_score: 2.5
death_list_check: "CLEAR"
---

## P4-M3-OffsetRemoval: "Un-snap the Extra to Make Them Equal"

### The Gap This Fills

| From | Missing Step | To |
| :--- | :--- | :--- |
| P3-N3 (Difference is constant) | **How to USE the difference to solve** | P6-ALG-02 ($8b + 5y = 32$) |

P3 teaches: "The extra is always there."
P4 teaches: "Remove the extra. Now you have equal groups. Solve."
P6 demands: "Substitute, expand, isolate." — same logic, symbolic form.

### Problem (P4 Level — Whole Numbers)

Ali packed 3 Blue bags and 5 Red bags. Each Red bag weighs 2 kg more than each Blue bag. The total weight is 40 kg. Find the weight of each Blue bag.

### Solution Logic

1. Each Red bag has 2 kg extra compared to Blue
2. **Un-snap the extra:** $5 \times 2 = 10$ kg of "extra" weight
3. **Remove from total:** $40 - 10 = 30$ kg
4. **Now all 8 bags are equal:** $30 \div 8$ → (adjusted for whole numbers: 6 Blue-equivalent bags, $30 \div 6 = 5$ kg)
5. Each Blue bag weighs 5 kg

### The Bridge Moment

```
BEFORE un-snapping:                    AFTER un-snapping:

Blue: [████]        = b                Blue: [████]        = b
Blue: [████]        = b                Blue: [████]        = b
Blue: [████]        = b                Blue: [████]        = b
Red:  [████][//]    = b + 2            Red:  [████]        = b  (extra removed)
Red:  [████][//]    = b + 2            Red:  [████]        = b  (extra removed)
Red:  [████][//]    = b + 2            Red:  [████]        = b  (extra removed)
Red:  [████][//]    = b + 2            Red:  [████]        = b  (extra removed)
Red:  [████][//]    = b + 2            Red:  [████]        = b  (extra removed)
─────────────────────────              ─────────────────────────
Total = 40 kg                          Total = 40 - 10 = 30 kg
                                       8 equal bags = 30 kg
                                       1 bag = 30 ÷ 8
```

### Pedagogical Notes

- **Why this is CRITICAL:** Without this node, students know the difference exists (P3) but don't know what to do with it. This node teaches the ACTION: remove, equalize, then divide. In P6, this action becomes algebraic substitution.
- **Vertical Thread (COMPLETE):**
  - P2: "5 groups of 3 = 15" (equal groups)
  - P3: "Red is always 2 more than Blue" (constant difference)
  - **P4: "Remove the 2 from each Red → now all equal → divide"** (offset removal)
  - P6: "Let Red = Blue + y → $3b + 5(b+y) = 32$ → solve" (algebraic substitution)

### Level_Config_JSON

```json
{
  "node_id": "P4-M3-OffsetRemoval",
  "source": "ATOM-SG Bridge Forge (Gap Fix)",
  "bimodal": "Mode A (Fluency)",
  "complexity_score": 2.5,
  "p6_logic": {
    "description": "Remove known offset from unequal groups to create equal groups, then solve. Direct precursor to algebraic substitution.",
    "formula": "Total - (n × extra) = equal_groups × count",
    "moe_code": "P4-M3-OffsetRemoval"
  },
  "age_6_seed": {
    "title": "The Backpack Balance",
    "precursor_skill": "Equal Groups + Comparison (More/Less)",
    "gameplay": {
      "setup": "A shelf has Blue backpacks and Red backpacks. Red backpacks are visibly BIGGER because each has an extra pocket with 2 toys inside. A scale shows total: 40 toys.",
      "mechanic": "Round 1: Player is told 'The Red ones each have 2 EXTRA toys in a side pocket.' Player taps each Red backpack to remove the side pocket. Removed toys pile up: 5 × 2 = 10 toys. Round 2: Scale updates: 40 - 10 = 30 toys left. NOW all backpacks look the SAME size. Round 3: Player shares 30 toys equally among 6 backpacks → 5 each.",
      "key_insight": "To find what's EQUAL, first remove what's DIFFERENT. Once everything is the same, it's just sharing — which you already know from P2. The 'un-snapping' is what P6 calls 'substitution.'",
      "no_symbols": true,
      "visual_language": "Backpacks, side pockets, toy removal, sharing equally — NO algebra, NO letters"
    },
    "vertical_link": {
      "seed": "P2-M1-EqualGroups",
      "bridge": "P2: 'Share equally' → P4: 'Remove extras THEN share equally' → P6: 'Substitute offset, collect terms, solve'"
    }
  }
}
```
