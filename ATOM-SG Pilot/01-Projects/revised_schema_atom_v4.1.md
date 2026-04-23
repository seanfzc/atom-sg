# ATOM-SG Revised Schema (Post-Second Feedback)
# Version: 4.1 - Incorporating Paper 1 Revolution & Scenario Cluster Logic
# For: Operation Vertical Thread Pilot - P6 Phase (10 questions)

## NEW ADDITIONS FOR P6 PROCESSING:

### 1. Paper 1 Revolution Enhancement
- **NEW FIELD:** `time_target_seconds`
  - Target solution time without calculator
  - Based on PSLE Paper 1 time constraints
  - Example: 90 seconds for complex P6 questions
  
- **NEW FIELD:** `calculator_required` (boolean)
  - `false` for Paper 1 questions
  - `true` for Paper 2 questions
  - Impacts game design: mental math vs. calculation tools

- **Enhanced Speed-Accuracy Game Templates**
  - Questions solvable in <90 seconds → "Speed-Accuracy" mechanics
  - Balance between speed pressure and accuracy requirements

### 2. Scenario Cluster Logic (Science Focus)
- **Enhanced `scenario_cluster_id` tracking**
  - Track same diagram/scenario across multiple questions
  - Enable "World-Based Levels" game design
  - Example: Same electrical circuit diagram used for 3 different MCQs

- **NEW FIELD:** `linked_question_count`
  - Number of questions sharing same scenario
  - Helps identify "Linked Question" format (2026 PSLE feature)

### 3. Visual-Linguistic Stress Score Refinement
- **NEW FIELD:** `distractor_density` (1-5)
  - 1: No distractors (straightforward)
  - 3: Moderate distractors (some irrelevant data)
  - 5: High "Red Herring" data (intentional misleading information)
  
- **NEW FIELD:** `red_herring_data` (boolean)
  - Flags intentionally misleading information
  - Critical for training to avoid "careless mistakes"

### 4. P6-Specific Logic Families
- **Algebra:** `algebraic_expressions`, `algebraic_equations`
- **Ratio & Proportion:** `ratio_basics`, `ratio_word_problems`
- **Percentage:** `percentage_basics`, `percentage_applications`
- **Geometry:** `geometry_measurement`, `geometry_properties`
- **Statistics:** `data_interpretation`, `probability_basics`

### 5. Enhanced Vertical Evolution Mapping
- **Bidirectional linking:** P6→P1 and P1→P6
- **Specific concept bridges:**
  - P1 place_value → P6 algebraic_expressions (10x + y = value)
  - P1 part_whole → P6 ratio_word_problems
  - P1 counting → P6 probability_basics
  - P1 measurement → P6 geometry_measurement

---

## REVISED YAML SCHEMA (v4.1)

```yaml
---
# Core Identification (2026-Aligned)
question_id: "P6_2026_PSLE_Specimen_Q1"
source_file: "2026 PSLE Mathematics Specimen Paper 1.pdf"
logic_family: "algebraic_expressions"  # P6-specific
grade_level: "P6"
2026_syllabus_check: "Confirmed - Algebra"
paper_type: "Paper 1"  # 50% weight, non-calculator
date_extracted: "2026-04-08"
pilot_phase: "Phase 2 - P6 Algebra Focus"

# Paper 1 Revolution Fields
paper_1_requirements:
  calculator_required: false
  time_target_seconds: 90  # PSLE Paper 1 time constraint
  mental_math_required: true
  speed_accuracy_balance: "high_speed_moderate_accuracy"

# Enhanced Complexity Scoring (P6-Specific)
complexity_scores:
  cognitive_load: 4  # Multi-step reasoning
  visual_linguistic_integration: 5  # High - potential red herrings
  conceptual_abstraction: 4  # Abstract algebraic thinking
  contextual_load: 3  # Some real-world context
  paper_1_fluency_target: 4  # High speed required
  distractor_density: 4  # High - contains irrelevant data
  weighted_score: 4.0  # P6 weights adjusted

# Red Herring Analysis
red_herring_analysis:
  has_red_herring_data: true
  red_herring_type: "extra_numbers_not_needed"
  distractor_count: 2
  misleading_visual_elements: 1
  training_focus: "Data filtering, identifying relevant information"

# MOE-Standard Node Mapping (P6 Codes)
nodes:
  primary: ["P6-A1-Alg"]  # MOE: Algebra
  secondary: ["S-DATA-FILTER", "S-ABSTRACT-REP"]  # Data filtering, Abstract representation
  tertiary: ["T-RED-HERRING"]  # Red herring detection error
  vertical_evolution: 
    forward: "Secondary school algebraic manipulation"
    backward: ["P1-N1-Num-100"]  # Links back to P1 place value

# Scenario Cluster Tracking
scenario_cluster:
  has_cluster: true
  cluster_id: "SC-ALG-001"
  linked_question_count: 3
  cluster_description: "Same algebraic expression diagram used for 3 MCQs"
  game_design_implication: "World-Based Level: Solve multiple puzzles in same algebraic world"

# Logic Trap Detection (P6-Enhanced)
logic_traps:
  - type: "red_herring_distraction"
    description: "Question includes extra numbers that are not needed for solution"
    confidence: 0.8
    intervention: "Prompt: 'Which numbers are actually needed to solve this?'"
    game_design_hook: "'Data Filter' mechanic - drag needed numbers to solution area"

# Game Design Template (Speed-Accuracy Focus)
game_design_template:
  mechanic: "Algebra_Speed_Solver"
  logic: "Player must filter relevant data, set up algebraic expression, solve under time pressure"
  progression_hook: "Increase red herring count, reduce time limit, add multiple steps"
  level_config:
    time_limit: 90  # Seconds (Paper 1 constraint)
    distractor_count: 3
    allowed_strategies: ["mental_math", "estimation", "elimination"]
  age_11_adaptation: "Algebraic notation, variable isolation, real-world applications"
  age_14_adaptation: "Quadratic equations, simultaneous equations, algebraic proof"
  boss_level_design: "Multiple red herrings with similar-looking relevant data"

# Validation & 2026 Compliance (Enhanced)
validation:
  manual_review_required: true
  confidence_score: 0.85
  syllabus_2026_alignment:
    - "Algebra: CONFIRMED (P6-A1-Alg)"
    - "Paper 1: CONFIRMED (non-calculator, <90s target)"
    - "Linked Questions: DETECTED (scenario cluster)"
    - "No deprecated topics: CONFIRMED"
  cost_tracking:
    vision_api_calls: 1  # May need for diagram analysis
    llm_tokens: 200
    heuristic_bypass: false
    cost_per_node: 0.05
    processing_method: "vision_llm_integrated"

# Original Question Metadata
original_question:
  text: "[Full question text]"
  diagram_present: true
  answer_format: "MCQ"  # or "Short Answer"
  marks: 2  # PSLE marking scheme

# Solution Analysis
solution_analysis:
  steps_required: 3
  critical_step: "Identify relevant variables from distractors"
  common_errors: ["Using all given numbers", "Misinterpreting algebraic relationship"]
  optimal_strategy: "Extract needed data, write expression, solve"
  time_benchmark: "Expert: 60s, Target: 90s, Novice: 120s"

# Backward Vertical Link Verification
vertical_link_verification:
  p1_linked_node: "P1-N1-Num-100"
  connection_strength: "strong"
  conceptual_bridge: "Place value (tens/ones) → Algebraic coefficients"
  game_design_implication: "Same 'Unit_Slasher' mechanic but with variables instead of concrete objects"
---
```

## P6 PROCESSING REQUIREMENTS

### Source Files Needed:
1. **2026 PSLE Specimen Paper** (Mathematics)
2. **Focus on:** Algebra and Ratio questions
3. **Paper Type:** Paper 1 (non-calculator) preferred
4. **Look for:** Linked questions (same diagram, multiple MCQs)

### Processing Workflow:
1. **Identify P6 source files** with Algebra/Ratio content
2. **Extract 10 questions** focusing on Paper 1 format
3. **Apply v4.1 schema** with new fields
4. **Verify backward links** to P1 questions
5. **Identify scenario clusters** for "World-Based Levels"
6. **Analyze distractor density** for red herring training

### Success Metrics for P6 Phase:
1. **All 10 questions** processed with v4.1 schema
2. **Backward links verified** to appropriate P1 concepts
3. **At least 2 scenario clusters** identified
4. **Red herring analysis** completed for each question
5. **Time target seconds** appropriately set based on complexity
6. **Game design templates** reflect Paper 1 speed-accuracy balance

## INTEGRATION WITH P1 PHASE

### Vertical Thread Completion:
- **P1 Phase Complete:** 5 questions with v4.0 schema
- **P6 Phase Starting:** 10 questions with v4.1 schema  
- **Final Output:** 15-question vertical map (P1→P6)

### Cross-Grade Validation:
1. **Concept Bridges:** Verify P1→P6 logical progression
2. **Game Mechanics:** Ensure consistent adaptation across grades
3. **Error Patterns:** Track how misconceptions evolve P1→P6
4. **Intervention Strategies:** Develop grade-appropriate fixes

### Pilot Completion Deliverables:
1. **15 question files** (5 P1 + 10 P6) with complete metadata
2. **Vertical Evolution Report** showing P1→P6 concept mapping
3. **Scenario Cluster Catalog** for "World-Based Levels"
4. **Red Herring Analysis** for careless mistake training
5. **Game Design Recommendations** for each question type
6. **2026 Syllabus Compliance Report**

---

## IMMEDIATE NEXT STEPS

### 1. **Identify P6 Source Files**
```bash
find /Users/zcaeth/Desktop/sg_exam_papers -name "*2026*PSLE*" -type f
find /Users/zcaeth/Desktop/sg_exam_papers -name "*P6*Algebra*" -type f  
find /Users/zcaeth/Desktop/sg_exam_papers -name "*P6*Ratio*" -type f
```

### 2. **Create P6 Processing Pipeline**
- Update existing Python scripts for v4.1 schema
- Add red herring detection logic
- Implement scenario cluster tracking
- Set time targets based on question complexity

### 3. **Process 10 P6 Questions**
- Focus on Algebra and Ratio
- Prioritize Paper 1 (non-calculator) questions
- Look for linked question clusters
- Apply backward linking to P1 concepts

### 4. **Generate Vertical Map**
- Create P1→P6 concept bridges
- Identify "seed concepts" that evolve across grades
- Develop game design progression across levels

---

*Schema Version: 4.1 (Post-Second Feedback - Paper 1 Revolution)*
*Last Updated: 2026-04-08*
*Focus: P6 Algebra/Ratio with backward linking to P1*