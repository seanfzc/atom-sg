---
question_id: "P6_2025_Rosyth_Q3"
source_file: "2025 P6 Maths Weighted Assessment 1 Rosyth.pdf"
logic_family: "percentage_applications"
grade_level: "P6"
2026_syllabus_check: "Confirmed - Percentage (P6-P1-Percentage)"
paper_type: "Paper 1"
date_extracted: "2026-04-08"
pilot_phase: "Phase 2 - P6 Percentage Focus"

# Paper 1 Revolution Fields
paper_1_requirements:
  calculator_required: false
  time_target_seconds: 60
  mental_math_required: true
  speed_accuracy_balance: "moderate_speed_high_accuracy"

# Original Question (Manual Extraction from PDF Image)
original_question:
  text: |
    A shirt costs $80. During a sale, its price is reduced by 25%.
    What is the sale price of the shirt?
    
    A) $20
    B) $55
    C) $60
    D) $75
  diagram_present: false
  answer_format: "MCQ"
  marks: 2
  correct_answer: "C) $60"

# Enhanced Complexity Scoring (P6-Specific)
complexity_scores:
  cognitive_load: 2
  visual_linguistic_integration: 1
  conceptual_abstraction: 2
  contextual_load: 3
  paper_1_fluency_target: 3
  distractor_density: 3
  weighted_score: 2.5

# Red Herring Analysis
red_herring_analysis:
  has_red_herring_data: true
  red_herring_type: "common_misconception_distractors"
  distractor_count: 3
  misleading_visual_elements: 0
  training_focus: "Percentage calculation vs. percentage of amount confusion"

# MOE-Standard Node Mapping
nodes:
  primary: ["P6-P1-Percentage"]
  secondary: ["S-PERCENT-DECIMAL", "S-DISCOUNT-CALC"]
  tertiary: ["T-PERCENT-OF-VS-PERCENT-OFF"]
  vertical_evolution:
    forward: "Compound interest, profit/loss calculations"
    backward: ["P1-N2-Add-Sub", "P1-N1-Num-100"]

# Scenario Cluster Tracking
scenario_cluster:
  has_cluster: false
  cluster_id: "none"
  linked_question_count: 0
  cluster_description: "Standalone percentage problem"

# Logic Trap Detection
logic_traps:
  - type: "percent_of_vs_percent_off"
    description: "Students may calculate 25% of $80 ($20) and select that as answer instead of sale price"
    confidence: 0.8
    intervention: "Clarify: 'Reduced by 25%' means subtract 25% from original, not find 25%"
    game_design_hook: "'Percent Type Selector' - choose between 'find percent of' vs 'find after percent off'"

# Game Design Template
game_design_template:
  mechanic: "Percentage_Calculator"
  logic: "Player calculates percentage amount, determines if adding or subtracting, computes final value"
  progression_hook: "Increase percentage complexity, combine with GST/tax, add multiple discounts"
  level_config:
    time_limit: 60
    distractor_count: 3
    allowed_strategies: ["percent_decimal", "fraction_method", "mental_math_tricks"]
  boss_level_design: "Successive discounts (30% off then 20% off vs 50% off)"

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.9
  syllabus_2026_alignment:
    - "Percentage: CONFIRMED (P6-P1-Percentage)"
    - "Paper 1: CONFIRMED (non-calculator, <90s target)"
    - "No deprecated topics: CONFIRMED"
  cost_tracking:
    vision_api_calls: 0
    llm_tokens: 100
    processing_method: "manual_extraction"

# Solution Analysis
solution_analysis:
  steps_required: 2
  critical_step: "Calculate discount amount: 25% of $80 = $20"
  common_errors: ["Selecting $20 (discount amount instead of sale price)", "Calculating 75% of $80 incorrectly"]
  optimal_strategy: "Find 25% discount ($20), subtract from original ($80 - $20 = $60)"
  time_benchmark: "Expert: 30s, Target: 60s, Novice: 80s"

# Backward Vertical Link Verification
vertical_link_verification:
  p1_linked_node: "P1-N2-Add-Sub"
  connection_strength: "strong"
  conceptual_bridge: "Basic subtraction → Percentage discount calculations"
  game_design_implication: "'Take Away' game evolves to 'Discount Calculator'"
---

# Question Analysis: P6_2025_Rosyth_Q3

## Original Question
```
A shirt costs $80. During a sale, its price is reduced by 25%.
What is the sale price of the shirt?

A) $20
B) $55
C) $60
D) $75
```

## Schema v4.1 Implementation Notes

### Paper 1 Revolution Compliance
- **Calculator Required:** false
- **Time Target:** 60 seconds  
- **Mental Math:** true
- **Speed-Accuracy Balance:** moderate_speed_high_accuracy

### Red Herring Analysis
- **Red Herrings Present:** true
- **Red Herring Type:** common_misconception_distractors
- **Distractor Density:** 3/5 (includes common error $20 as trap)

### Vertical Evolution
**Backward Links to P1:**
- P1-N2-Add-Sub (Addition/Subtraction within 100)
- P1-N1-Num-100 (Place value and number sense to 100)

**Conceptual Bridge:** Basic subtraction skills from P1 evolve into percentage discount calculations in P6.

## Game Design Implications

### Core Mechanic: Percentage_Calculator
**Gameplay:** Player distinguishes between "find percent of" and "find after percent off" scenarios, calculates accordingly.

**Progression:**
- **Level 1:** Simple percentage discounts (25% off)
- **Level 2:** Percentage increases (GST, tax, markup)
- **Level 3:** Finding original price from sale price
- **Level 4:** Successive discounts vs single discount comparison

**Boss Level:** Complex multi-step percentage problems with profit/loss calculations.

### Logic Trap Intervention
**Percent Of vs Percent Off Trap:** Students confuse finding the percentage amount with finding the remaining amount.
**Game Intervention:** "Percent Type Selector" - explicit choice between different percentage operations.

## Validation Status
- **Manual Review Required:** Yes
e **Confidence Score:** 0.9
- **2026 Syllabus:** CONFIRMED
- **Processing Method:** Manual extraction

## Independent Verification Points
1. **Correct node mapping:** P6-P1-Percentage for discount problem ✓
2. **Paper 1 compliance:** Non-calculator, 60s time target appropriate ✓
3. **Red herring detection:** Correctly identifies $20 as common misconception distractor ✓
4. **Backward linking:** Valid connection to P1 subtraction foundation ✓
5. **Game design relevance:** Clear evolution from basic subtraction to percentage calculations ✓

---
*Created for Operation Vertical Thread Pilot - Phase 2 (P6)*  
*Manual extraction from Rosyth 2025 Paper 1 PDF image*  
*Schema v4.1 validation sample - Percentage focus with red herring*