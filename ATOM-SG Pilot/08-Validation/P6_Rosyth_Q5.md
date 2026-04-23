---
question_id: "P6_2025_Rosyth_Q5"
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
  time_target_seconds: 60
  mental_math_required: true
  speed_accuracy_balance: "moderate_speed_high_accuracy"

# Original Question (Manual Extraction from PDF Image)
original_question:
  text: |
    In a class, the ratio of boys to girls is 2:3.
    If there are 15 girls, how many boys are there?
    
    A) 6
    B) 9
    C) 10
    D) 12
  diagram_present: false
  answer_format: "MCQ"
  marks: 2
  correct_answer: "C) 10"

# Enhanced Complexity Scoring (P6-Specific)
complexity_scores:
  cognitive_load: 2
  visual_linguistic_integration: 2
  conceptual_abstraction: 2
  contextual_load: 3
  paper_1_fluency_target: 3
  distractor_density: 3
  weighted_score: 2.4

# Red Herring Analysis
red_herring_analysis:
  has_red_herring_data: false
  red_herring_type: "none"
  distractor_count: 3
  misleading_visual_elements: 0
  training_focus: "Ratio unit finding and application"

# MOE-Standard Node Mapping
nodes:
  primary: ["P6-R1-Ratio"]
  secondary: ["S-RATIO-APPLY", "S-UNIT-FINDING"]
  tertiary: ["T-RATIO-SUM-VS-PART"]
  vertical_evolution:
    forward: "Ratio in geometry, scale drawings, similarity"
    backward: ["P1-N2-Add-Sub", "P1-N1-Num-20"]

# Scenario Cluster Tracking
scenario_cluster:
  has_cluster: false
  cluster_id: "none"
  linked_question_count: 0
  cluster_description: "Standalone ratio application problem"

# Logic Trap Detection
logic_traps:
  - type: "ratio_sum_vs_part"
    description: "Students may calculate total children (25) instead of just boys (10)"
    confidence: 0.6
    intervention: "Highlight question: 'how many boys' not 'how many children'"
    game_design_hook: "'Question Focus' - highlight key words in question before solving"

# Game Design Template
game_design_template:
  mechanic: "Ratio_Unit_Finder"
  logic: "Player finds unit value from given ratio component, applies to find other component"
  progression_hook: "Increase ratio complexity, find missing total, work backwards from total"
  level_config:
    time_limit: 60
    distractor_count: 3
    allowed_strategies: ["unit_method", "proportion_cross_multiply", "fraction_method"]
  boss_level_design: "Ratio combined with percentage or algebra (boys:girls = 2:3, total = 40, 25% leave...)"

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.88
  syllabus_2026_alignment:
    - "Ratio: CONFIRMED (P6-R1-Ratio)"
    - "Paper 1: CONFIRMED (non-calculator, <90s target)"
    - "No deprecated topics: CONFIRMED"
  cost_tracking:
    vision_api_calls: 0
    llm_tokens: 110
    processing_method: "manual_extraction"

# Solution Analysis
solution_analysis:
  steps_required: 2
  critical_step: "Find unit value: 15 girls ÷ 3 parts = 5 per unit"
  common_errors: ["Using 15 ÷ 5 = 3 (wrong ratio application)", "Finding total instead of boys"]
  optimal_strategy: "Girls = 3 units = 15, so 1 unit = 5, boys = 2 units = 10"
  time_benchmark: "Expert: 35s, Target: 60s, Novice: 85s"

# Backward Vertical Link Verification
vertical_link_verification:
  p1_linked_node: "P1-N2-Add-Sub"
  connection_strength: "moderate"
  conceptual_bridge: "Basic grouping and sharing → Proportional distribution with ratios"
  game_design_implication: "'Fair Sharer' evolves to 'Ratio Distributor'"
---

# Question Analysis: P6_2025_Rosyth_Q5

## Original Question
```
In a class, the ratio of boys to girls is 2:3.
If there are 15 girls, how many boys are there?

A) 6
B) 9
C) 10
D) 12
```

## Schema v4.1 Implementation Notes

### Paper 1 Revolution Compliance
- **Calculator Required:** false
- **Time Target:** 60 seconds  
- **Mental Math:** true
- **Speed-Accuracy Balance:** moderate_speed_high_accuracy

### Red Herring Analysis
- **Red Herrings Present:** false
- **Distractor Density:** 3/5 (standard distractors with common ratio errors)

### Vertical Evolution
**Backward Links to P1:**
- P1-N2-Add-Sub (Addition/Subtraction within 20)
- P1-N1-Num-20 (Number sense and place value to 20)

**Conceptual Bridge:** Basic grouping and sharing concepts from P1 provide foundation for proportional thinking with ratios in P6.

## Game Design Implications

### Core Mechanic: Ratio_Unit_Finder
**Gameplay:** Player identifies given ratio component, calculates unit value, applies to find unknown component.

**Progression:**
- **Level 1:** Simple two-part ratios with one component given
- **Level 2:** Three-part ratios
- **Level 3:** Find missing total or missing ratio
- **Level 4:** Ratio problems with additional constraints (percentage, fractions)

**Boss Level:** Complex ratio word problems involving rates, speed, or mixtures.

### Logic Trap Intervention
**Ratio Sum vs Part Trap:** Students calculate total instead of requested component.
**Game Intervention:** "Question Focus" - highlight key question words before solving begins.

## Validation Status
- **Manual Review Required:** Yes
- **Confidence Score:** 0.88
- **2026 Syllabus:** CONFIRMED
- **Processing Method:** Manual extraction

## Independent Verification Points
1. **Correct node mapping:** P6-R1-Ratio for ratio application problem ✓
2. **Paper 1 compliance:** Non-calculator, 60s time target appropriate ✓
3. **Backward linking:** Valid connection to P1 grouping/sharing foundation ✓
4. **Logic trap detection:** Identifies common error of finding total vs part ✓
5. **Game design relevance:** Clear evolution from basic sharing to ratio thinking ✓

---
*Created for Operation Vertical Thread Pilot - Phase 2 (P6)*  
*Manual extraction from Rosyth 2025 Paper 1 PDF image*  
*Schema v4.1 validation sample - Ratio unit finding focus*