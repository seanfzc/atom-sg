---
node_id: "ROSYTH-P6-ALG-07"
source: "Rosyth 2026 P6 Math CA1 Q7"
thread: "HYBRID: B (Offset) + C (Equation-Solving)"
status: "EXTRACTED — CEO VERIFIED"
node_type: "BOSS (P6) — HYBRID"
triad_axis:
  linguistic:
    keywords: ["costs more than", "identical", "total cost", "find the value of"]
    heuristic: "Offset Substitution → Simultaneous Setup → Solve"
    trigger: "CONSTANT DIFFERENCE + INTERNAL TRANSFER"
    linguistic_load: "High — requires setting up two relationships (offset + total), substituting, then solving"
  visual:
    template: "Comparison Bar + Balanced Scale (Hybrid)"
    stress_score: 3.5
    description: "Two item types with offset (blender = kettle + 12). Bars show offset. Then total equation placed on a scale."
  logic:
    moe_code: "P6-A2-Equations"
    formula: "Let kettle = $t$, blender = $t + 12$. $t + (t+12) = 150 \\implies 2t = 138 \\implies t = 69$. Blender = $81$. $y = 3(81) + 2(69) = 243 + 138 = 381$."
    steps:
      - "Let kettle cost = $t$, blender cost = $t + 12$"
      - "1 blender + 1 kettle = $150: $(t+12) + t = 150$"
      - "Simplify: $2t + 12 = 150$"
      - "Subtract 12: $2t = 138$"
      - "Divide by 2: $t = 69$"
      - "Kettle = $69, Blender = $81"
      - "Total $y = 3(81) + 2(69) = 243 + 138 = 381$"
      - "Check: 3 blenders + 2 kettles = $243 + $138 = $381 ✅"
complexity_score: 4.1
vertical_continuity:
  seed_nodes: ["P1-N2-Comparison", "P2-N1-MissingVal"]
  parent_bridges:
    thread_B: "P4-M3-OffsetRemoval"
    thread_C: "P5-H1-RatioEquation"
  cls_check:
    P4_M3_to_this: 1.6
    P5_H1_to_this: 0.9
  bridge_logic: "P4-M3 teaches offset removal (un-snap the extra). P5-H1 teaches ratio-to-equation. Q7 FUSES: set up offset relationship, form equation, solve, then scale to total."
  flag: "CLS from P4-M3 = 1.6 ⚠️ — mitigated via P5-H1 route (CLS 0.9 ✅)"
bimodal_calibration:
  mode: "B (Paper 2 - Odyssey)"
  target_response_time: "180 seconds"
  flag: "Boss Fight: Odyssey Level — $C_t = 4.1$"
verb_test: "ACTION: Set up offset relationship, form equation from total, solve, then compute final expression."
death_list_check: "CLEAR"
hybrid_status: "HYBRID — Thread B + Thread C"
rule_6: "COMPLIANT — dual-parentage via P4-M3-OffsetRemoval (B) + P5-H1-RatioEquation (C)"
dual_parentage:
  thread_B: "P4-M3-OffsetRemoval"
  thread_C: "P5-H1-RatioEquation"
  persona_mapping:
    thread_B: "The Balanced Scale (offset removal)"
    thread_C: "The Scale Master (equation solving)"
---

## Raw Text (Q7)
3 identical blenders and 2 identical kettles cost $\$y$. A blender costs $\$12$ more than a kettle. If the total cost of 1 blender and 1 kettle is $\$150$, find the value of $y$.

## LaTeX Cleanup
$3$ identical blenders and $2$ identical kettles cost $\$y$. A blender costs $\$12$ more than a kettle. If the total cost of $1$ blender and $1$ kettle is $\$150$, find the value of $y$.

**Solution:**
Let kettle = $t$, blender = $t + 12$.
$(t + 12) + t = 150$
$2t + 12 = 150$
$2t = 138$
$t = 69$
Blender = $\$81$, Kettle = $\$69$
$y = 3(81) + 2(69) = 243 + 138 = \$381$

## Triad YAML
```yaml
linguistic: "Offset ('$12 more') + equation setup. Triggers: CONSTANT DIFFERENCE + INTERNAL TRANSFER."
visual: "Comparison Bar + Scale. Stress: 3.5."
logic: "P6-A2-Equations. Multi-step: offset → equation → solve → compute total."
hybrid: "Thread B + Thread C. Parents: P4-M3 (Balanced Scale) + P5-H1 (Scale Master)."
flag: "Boss Fight: Odyssey Level. Ct = 4.1."
```

### Level_Config_JSON
```json
{
  "node_id": "ROSYTH-P6-ALG-07",
  "bimodal": "Mode B (Odyssey)",
  "complexity_score": 4.1,
  "hybrid": true,
  "threads": ["B", "C"],
  "flag": "Boss Fight: Odyssey Level",
  "p6_logic": {
    "description": "Multi-step: establish offset, form equation from constraint, solve, compute expression.",
    "formula": "t + (t+12) = 150 → t = 69, y = 3(81) + 2(69) = 381",
    "moe_code": "P6-A2-Equations"
  },
  "age_6_seed": {
    "title": "The Market Scale (Boss Battle)",
    "precursor_skill": "Balanced Scale + Offset Removal",
    "gameplay": {
      "setup": "A market stall sells blenders and kettles. A sign says: 'A blender costs MORE than a kettle.' Another sign: '1 blender + 1 kettle = $150.'",
      "mechanic": "Phase 1 (Offset): 'The blender costs $12 more.' Player sees two items on a scale — blender side is heavier by a $12 block. Phase 2 (Balance): Remove the $12 extra. Now both items cost the same! 2 equal items = $150 - $12 = $138. Each = $69. Kettle = $69, Blender = $69 + $12 = $81. Phase 3 (Scale Up): '3 blenders + 2 kettles = ?' Player: 3×81 + 2×69 = 243 + 138 = $381.",
      "key_insight": "First remove the OFFSET to make things equal (Thread B skill). Then SOLVE (Thread C skill). Then SCALE UP to the final answer. Three skills in sequence — this is an Odyssey.",
      "no_symbols": true,
      "visual_language": "Market stall, price tags, offset blocks, scales, calculator"
    }
  }
}
```
