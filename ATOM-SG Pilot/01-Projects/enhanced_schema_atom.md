# Enhanced ATOM-SG Schema (Post-Feedback)
# Version: 3.0 - Incorporating Independent Feedback
# For: Operation Vertical Thread Pilot (20 questions)

## Enhanced 4-Axis Complexity Scoring

### Axis 1: Cognitive Load (1-5)
**Definition:** Mental processing steps required
1. Single recall/identification
2. Simple comparison or single-step operation  
3. Two-step operation with integration
4. Multi-step with transformation
5. Abstract reasoning with justification

### Axis 2: Visual-Linguistic Integration (1-5)
**Definition:** Coordination between visual and textual elements
1. Text-only or image-only
2. Simple image-text correspondence (same info)
3. Complementary image-text (partial overlap)
4. Integrated image-text (both needed)
5. Contradictory image-text (logic trap potential)

### Axis 3: Conceptual Abstraction (1-5)
**Definition:** Distance from concrete to abstract
1. Direct concrete objects
2. Representational (pictures of objects)
3. Symbolic (numbers, basic shapes)
4. Abstract relations (ratios, percentages)
5. Meta-cognitive (explain reasoning)

### Axis 4: Contextual Load (NEW) (1-5)
**Definition:** Real-world knowledge assumed
1. Classroom context only
2. Simple daily activities (shopping, time)
3. Family/social contexts
4. Complex real-world (money management)
5. Cultural/specialized knowledge

## Logic Trap Categorization System

### Visual-Text Mismatch
- Image suggests one answer, text another
- Requires cross-verification
- **Game Design:** "Double-check" mechanic

### Cognitive Dissonance
- Contradictory information within same modality
- Requires prioritization logic
- **Game Design:** "Choose your path" branching

### Cultural Assumption
- Requires specific cultural knowledge
- Singapore-specific contexts
- **Game Design:** "Local hero" cultural adaptation

### Hidden Assumption
- Unstated premises needed
- "Common sense" gaps
- **Game Design:** "Fill the gap" puzzle

### Procedural Overload
- Too many steps to track
- Working memory overload
- **Game Design:** "Step tracker" helper

## Dynamic Node System Enhancement

### Primary Nodes (MOE Syllabus Skills)
- Source: MOE 2026 syllabus
- Fixed, curriculum-aligned
- Example: "Number bonds within 20"

### Secondary Nodes (Cognitive Processes)
- Dynamic, discovered through analysis
- Example: "Visual-spatial rotation", "Working memory tracking"
- Cost-tracking: Vision-LLM cost per node identified

### Tertiary Nodes (Error Patterns)
- Common misconceptions
- Error classification
- Example: "Off-by-one counting", "Place value confusion"

### Edge Types
1. **prerequisite** → Must master A before B
2. **co-occurs_with** → Often appear together
3. **commonly_confused_with** → Students mix them up
4. **scales_to** → Simple → complex version
5. **alternative_approach** → Different solution paths

## Enhanced YAML Schema

```yaml
---
# Core Identification
question_id: "P1_2021_HenryPark_Q3"
source_file: "2021 P1 Maths Quiz1 Henry Park.pdf"
logic_family: "part_whole"
grade_level: "P1"

# Enhanced Complexity Scoring (1-5 each)
complexity_scores:
  cognitive_load: 3
  visual_linguistic_integration: 2
  conceptual_abstraction: 1
  contextual_load: 2
  weighted_score: 2.2  # Weighted average (grade-adjusted)

# Node Mapping
nodes:
  primary: ["P001", "P005"]  # Number bonds, Addition within 20
  secondary: ["S012", "S023"]  # Systematic enumeration, Visual scanning
  tertiary: ["T045"]  # Double-counting error pattern

# Logic Trap Detection
logic_traps:
  - type: "visual_text_mismatch"
    description: "Image shows 8 objects but text mentions 'groups of 4'"
    confidence: 0.7
    game_design_hook: "Double-check mechanic: verify image vs text"

# Context Analysis
context_analysis:
  real_world_context: "classroom"
  cultural_assumptions: ["Singapore coin system"]
  vocabulary_demand: "low"
  prior_knowledge_required: ["basic counting"]

# Game Template Extraction
game_template:
  core_mechanic: "part-whole matching"
  progression_hook: "Vary total quantity and number of parts"
  age_6_adaptation: "Color-coded parts with sound feedback"
  age_11_adaptation: "Time pressure + distractors"
  boss_level_design: "Add visual-text mismatch as 'trick question' level"

# Validation & Cost Tracking
validation:
  manual_review_required: false
  confidence_score: 0.85
  cost_tracking:
    vision_api_calls: 1
    llm_tokens: 245
    heuristic_bypass: true
    cost_per_node: 0.08  # USD per secondary node identified

# Syllabus Calibration
syllabus_calibration:
  moe_skill_code: "1N1b"
  year_introduced: "P1"
  year_mastery: "P2"
  removed_by_p6: false
  vertical_mapping: "Scales to P6 ratio problems"
---
```

## Weighted Scoring by Grade Level

### P1 Weights (Age 6-7)
- Cognitive Load: 30%
- Visual-Linguistic: 25%
- Conceptual Abstraction: 20%
- Contextual Load: 25%

### P6 Weights (Age 11-12)  
- Cognitive Load: 35%
- Visual-Linguistic: 20%
- Conceptual Abstraction: 30%
- Contextual Load: 15%

## Pilot Execution Requirements

### 20 Questions (10 P1 + 10 P6)
1. All from "Part-Whole" logic family
2. Include variety of visual types
3. Ensure syllabus calibration (2026 changes)
4. Manual validation sampling (4 questions)

### Output Files
1. Individual `.md` files in `/Pilot_Results/`
2. Summary report with vertical mapping
3. Logic trap categorization report
4. Cost efficiency analysis

### Success Metrics
1. All 20 questions processed successfully
2. Complexity scores distributed appropriately
3. At least 2 logic traps identified
4. Cost per node < $0.15
5. Vertical mapping clear P1→P6