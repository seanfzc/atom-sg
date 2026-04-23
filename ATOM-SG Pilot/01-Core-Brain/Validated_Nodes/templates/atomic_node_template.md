---
node_id: "{{NODE_ID}}"
source: "{{SOURCE}}"
thread: "{{THREAD}}"
status: "EXTRACTED - AWAITING CEO VERIFICATION"
triad_axis:
  linguistic:
    keywords: [{{KEYWORDS}}]
    heuristic: "{{HEURISTIC}}"
    trigger: "{{LINGUISTIC_TRIGGER}}"
    linguistic_load: "{{LINGUISTIC_LOAD}}"
  visual:
    template: "{{VISUAL_TEMPLATE}}"
    stress_score: {{STRESS_SCORE}}
    description: "{{VISUAL_DESCRIPTION}}"
  logic:
    moe_code: "{{MOE_CODE}}"
    formula: "{{FORMULA}}"
    steps:
      - "{{STEP_1}}"
      - "{{STEP_2}}"
      - "{{STEP_3}}"
vertical_continuity:
  seed_node: "{{SEED_NODE}}"
  bridge_logic: "{{BRIDGE_LOGIC}}"
bimodal_calibration:
  mode: "{{BIMODAL_MODE}}"
  target_response_time: "{{RESPONSE_TIME}}"
  complexity_score: {{COMPLEXITY_SCORE}}
death_list_check: "CLEAR"
---

## {{QUESTION_TITLE}}

{{QUESTION_TEXT}}

### Solution Logic

{{SOLUTION_STEPS}}

### Pedagogical Notes

- **Bimodal Classification:** {{BIMODAL_RATIONALE}}
- **Vertical Thread:** {{VERTICAL_RATIONALE}}

### Level_Config_JSON

```json
{
  "node_id": "{{NODE_ID}}",
  "source": "{{SOURCE}}",
  "bimodal": "{{BIMODAL_MODE}}",
  "complexity_score": {{COMPLEXITY_SCORE}},
  "p6_logic": {
    "description": "{{P6_LOGIC_DESCRIPTION}}",
    "formula": "{{FORMULA}}",
    "moe_code": "{{MOE_CODE}}"
  },
  "age_6_seed": {
    "title": "{{GAME_TITLE}}",
    "precursor_skill": "{{PRECURSOR_SKILL}}",
    "gameplay": {
      "setup": "{{GAME_SETUP}}",
      "mechanic": "{{GAME_MECHANIC}}",
      "key_insight": "{{KEY_INSIGHT}}",
      "no_symbols": true,
      "visual_language": "{{VISUAL_LANGUAGE}}"
    },
    "vertical_link": {
      "seed": "{{SEED_NODE}}",
      "bridge": "{{GAME_BRIDGE}}"
    }
  }
}
```
