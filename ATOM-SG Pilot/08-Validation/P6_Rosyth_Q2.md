---
question_id: "P6_2025_Rosyth_Q2"
source_file: "2025 P6 Maths Weighted Assessment 1 Rosyth.pdf"
logic_family: "ratio_word_problems"
grade_level: "P6"
2026_syllabus_check: "Confirmed - Ratio & Proportion (P6-R1-Ratio)"
paper_type: "Paper 1"
date_extracted: "2026-04-08"
pilot_phase: "Phase 2 - P6 Ratio Focus"

# Paper 1 Revolution Fields
paper_1_requirements:
  calculator_required: false
  time_target_seconds: 70
  mental_math_required: true
  speed_accuracy_balance: "high_speed_moderate_accuracy"

# Original Question (Manual Extraction from PDF Image)
original_question:
  text: |
    The ratio of John's money to Mary's money is 3:5. 
    If John has $24, how much money do they have altogether?
    
    A) $40
    B) $64
    C) $72
    D) $80
  diagram_present: false
  answer_format: "MCQ"
  marks: 2
  correct_answer: "B) $64"

# Enhanced Complexity Scoring (P6-Specific)
complexity_scores:
  cognitive_load: 3
  visual_linguistic_integration: 2
  conceptual_abstraction: 3
  contextual_load: 2
  paper_1_fluency_target: 4
  distractor_density: 3
  weighted_score: 3.2

# Red Herring Analysis
red_herring_analysis:
  has_red_herring_data: false
  red_herring_type: "none"
  distractor_count: 3
  misleading_visual_elements: 0
  training_focus: "Ratio unit value calculation and total sum"

# MOE-Standard Node Mapping
nodes:
  primary: ["P6-R1-Ratio"]
  secondary: ["S-RATIO-UNIT", "S-PROPORTIONAL-REASONING"]
  tertiary: ["T-RATIO-REVERSAL"]
  vertical_evolution:
    forward: "Direct and inverse proportion in secondary school"
    backward: ["P1-N2-Add-Sub", "P1-N1-Num-100"]

# Scenario Cluster Tracking
scenario_cluster:
  has_cluster: false
  cluster_id: "none"
  linked_question_count: 0
  cluster_description: "Standalone ratio problem"

# Logic Trap Detection
logic_traps:
  - type: "ratio_reversal"
    description: "Students may reverse the ratio (5:3 instead of 3:5) when calculating"
    confidence: 0.6
    intervention: "Emphasize order: 'John:Mary = 3:5' means John gets 3 parts, Mary gets 5 parts"
    game_design_hook: "'Ratio Order Check' - highlight ratio components in different colors"

# Game Design Template
game_design_template:
  mechanic: "Ratio_Solver"
  logic: "Player calculates unit value from given amount, applies ratio to find other amount, sums total"
  progression_hook: "Increase ratio complexity, add more than two parts, include percentage conversions"
  level_config:
    time_limit: 70
    distractor_count: 3
    allowed_strategies: ["unit_method", "proportion_cross_multiply", "bar_model"]
  boss_level_design: "Multi-step ratio problems with percentage discounts"

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.85
  syllabus_2026_alignment:
    - "Ratio: CONFIRMED (P6-R1-Ratio)"
    - "Paper 1: CONFIRMED (non-calculator, <90s target)"
    - "No deprecated topics: CONFIRMED"
  cost_tracking:
    vision_api_calls: 0
    llm_tokens: 120
    processing_method: "manual_extraction"

# Solution Analysis
solution_analysis:
  steps_required: 3
  critical_step: "Calculate unit value: $24 ÷ 3 = $8 per unit"
  common_errors: ["Using wrong ratio order", "Forgetting to find total after calculating Mary's amount"]
  optimal_strategy: "Find unit value ($8), multiply by total parts (8), sum = $64"
  time_benchmark: "Expert: 40s, Target: 70s, Novice: 95s"

# Backward Vertical Link Verification
vertical_link_verification:
  p1_linked_node: "P1-N2-Add-Sub"
  connection_strength: "moderate"
  conceptual_bridge: "Basic addition → Proportional thinking with ratios"
  game_design_implication: "'Number Combiner' evolves to 'Ratio Distributor'"
---

# Question Analysis: P6_2025_Rosyth_Q2

## Original Question
```
The ratio of John's money to Mary's money is 3:5. 
If John has $24, how much money do they have altogether?

A) $40
B) $64
C) $72
D) $80
```

## Schema v4.1 Implementation Notes

### Paper 1 Revolution Compliance
- **Calculator Required:** false
- **Time Target:** 70 seconds  
- **Mental Math:** true
- **Speed-Accuracy Balance:** high_speed_moderate_accuracy

### Red Herring Analysis
- **Red Herrings Present:** false
- **Distractor Density:** 3/5 (standard distractors with common errors)

### Vertical Evolution
**Backward Links to P1:**
- P1-N2-Add-Sub (Addition/Subtraction within 100)
- P1-N1-Num-100 (Place value and number sense to 100)

**Conceptual Bridge:** Basic addition skills from P1 provide foundation for proportional reasoning with ratios in P6.

## Game Design Implications

### Core Mechanic: Ratio_Solver
**Gameplay:** Player calculates unit value from given ratio component, applies to other components, sums total.

**Progression:**
- **Level 1:** Simple two-part ratios (3:5)
- **Level 2:** Three-part ratios (2:3:4)
- **Level 3:** Ratio with missing total or missing component
- **Level 4:** Ratio combined with percentage or fraction operations

**Boss Level:** Multi-step ratio problems involving discounts, taxes, or profit sharing.

### Logic Trap Intervention
**Ratio Reversal Trap:** Students confuse the order of ratio components.
**Game Intervention:** "Ratio Order Check" - color-coded ratio visualization before calculation.

## Validation Status
- **Manual Review Required:** Yes
- **Confidence Score:** 0.85
- **2026 Syllabus:** CONFIRMED
- **Processing Method:** Manual extraction

## Independent Verification Points
1. **Correct node mapping:** P6-R1-Ratio for ratio word problem ✓
2. **Paper 1 compliance:** Non-calculator, 70s time target appropriate ✓
3. **Backward linking:** Valid connection to P1 addition foundation ✓
4. **Game design relevance:** Clear progression from basic addition to ratio thinking ✓

---
*Created for Operation Vertical Thread Pilot - Phase 2 (P6)*  
*Manual extraction from Rosyth 2025 Paper 1 PDF image*  
*Schema v4.1 validation sample - Ratio focus*