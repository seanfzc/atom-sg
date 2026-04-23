# ATOM-SG Revised Schema (Post-QA/QC Audit)
# Version: 4.0 - Incorporating Brutal Feedback & 2026 Syllabus Updates
# For: Operation Vertical Thread Pilot (20 questions)

## CRITICAL CHANGES FROM FEEDBACK:

### 1. Node Classification Fix
- **OLD:** Generic "part_whole" logic family
- **NEW:** Specific logic families based on actual question content
  - `place_value_systems`: Numbers 20-100 (tens and ones)
  - `part_whole_operations`: Addition/subtraction within 20
  - `time_intervals`: 5-minute intervals, a.m./p.m.
  - `measurement_comparison`: Length, weight comparisons
  - `data_representation`: Picture graphs, tally charts

### 2. MOE Standard Node IDs
- **OLD:** Generic P001, S012, T045
- **NEW:** Official MOE sub-strand codes
  - Primary: `P1-N1-Num-100` (Numbers to 100)
  - Primary: `P1-N2-Add-Sub` (Addition/Subtraction within 20)
  - Primary: `P1-M1-Time` (Time: hours, half-hours, 5-minute intervals)
  - Secondary: `S-VIS-SCAN` (Visual scanning/filtering)
  - Secondary: `S-UNIT-RECOG` (Unit recognition - tens as composite)
  - Tertiary: `T-UNIT-CONF` (Unit confusion error)

### 3. Vertical Thread Enhancement
- **NEW FIELD:** `vertical_evolution`
- Links P1 concepts to P6 concepts
- Example: `P1 place_value → P6 algebraic_expressions`
- Example: `P1 part_whole → P6 ratio_percentage`

### 4. Paper 1 Revolution (50% PSLE Weight)
- **NEW FIELD:** `paper_1_fluency_target` (1-5)
- 1: No time pressure (concept mastery only)
- 5: High speed required (<15 seconds for P1 MCQ)
- Impacts game design: Speed challenges required

### 5. 2026 Syllabus Compliance
- **PURGE LIST:** "Speed" (Math), "Cells" (Science)
- **ADDED:** 5-minute time intervals for P1
- **ADDED:** Linked Questions (one diagram, multiple MCQs)
- **ADDED:** "Units Printed on Answer Line" rubric awareness

---

## REVISED YAML SCHEMA (v4.0)

```yaml
---
# Core Identification (2026-Aligned)
question_id: "P1_2021_Henry_Park_Q1"
source_file: "2021 P1 Maths Quiz1 Henry Park.pdf"
logic_family: "place_value_systems"  # SPECIFIC, not generic
grade_level: "P1"
2026_syllabus_check: "Confirmed - Numbers to 100"
paper_type: "Paper 1"  # Paper 1 (50%) or Paper 2 (50%)

# Enhanced Complexity Scoring (2026-Prioritized)
complexity_scores:
  cognitive_load: 2  # Simple counting
  visual_linguistic_integration: 4  # Must filter groups vs singles
  conceptual_abstraction: 1  # Concrete objects
  contextual_load: 2  # Classroom context
  paper_1_fluency_target: 5  # HIGH - 50% weight requires speed
  weighted_score: 2.8  # Grade-adjusted with fluency weight

# MOE-Standard Node Mapping
nodes:
  primary: ["P1-N1-Num-100"]  # MOE: Numbers to 100
  secondary: ["S-VIS-SCAN", "S-UNIT-RECOG"]  # Visual scanning, Unit recognition
  tertiary: ["T-UNIT-CONF"]  # Unit confusion error
  vertical_evolution: "P6-ALG-EXP"  # Links to P6 Algebra (10x + y = Value)

# Logic Trap Detection (2026-Relevant)
logic_traps:
  - type: "unit_confusion"
    description: "Student counts each bag of 10 as '1' instead of '10'."
    confidence: 0.8
    intervention: "Socratic prompt: 'Is that one sweet, or one BAG of sweets?'"
    game_design_hook: "Unit_Slasher mechanic - slash bags to release units"

# Context Analysis (Singapore-Specific)
context_analysis:
  real_world_context: "classroom"
  cultural_assumptions: 
    - "Singapore coin system (if money question)"
    - "Local fruits/foods recognition"
    - "School bag/stationery items"
  vocabulary_demand: "low"
  prior_knowledge_required: ["counting to 100", "number recognition"]

# Game Design Template (Speed-Focused)
game_design_template:
  mechanic: "Unit_Slasher"
  logic: "Player must slash bags to 'release' 10 units, then tap single units to reach target number"
  progression_hook: "Increase target number, add distractor objects, reduce time"
  level_config: 
    target: 47
    distractors: "random"
    time_limit: 15  # Seconds (Paper 1 fluency)
  age_6_adaptation: "Color-coded bags, audio counting, touch guidance"
  age_11_adaptation: "Multiple unit types (10s, 5s, 1s), algebraic representation"
  boss_level_design: "Include 'trick' bags that are empty or contain wrong amounts"

# Validation & 2026 Compliance
validation:
  manual_review_required: true  # Always for pilot
  confidence_score: 0.9
  syllabus_2026_alignment: 
    - "Numbers to 100: CONFIRMED"
    - "Paper 1 weight: 50% - speed training REQUIRED"
    - "No deprecated topics: CONFIRMED"
  cost_tracking:
    vision_api_calls: 0  # Heuristic preferred
    llm_tokens: 150
    heuristic_bypass: true
    cost_per_node: 0.00
    processing_method: "text_keyword_heuristic"

# Linked Questions Detection (2026 Feature)
linked_questions:
  is_linked: false
  scenario_cluster_id: null  # If same diagram used for multiple questions
  linked_count: 0

# Deprecated Topics Check (2026 Purge)
deprecated_check:
  contains_speed: false
  contains_cells: false
  deprecated_2026: false
  replacement_topic: null
---
```

## 2026 SYLLABUS UPDATES INTEGRATION

### Math Updates:
1. **Paper 1 Weight**: 50% → Requires fluency/speed training
2. **P1 Time**: Must include 5-minute intervals and a.m./p.m.
3. **P4 Topics Moved Down**: Nets, Pie Charts now in P4 (was P5/P6)
4. **Purged**: Speed calculations (moved to secondary school)

### Science Updates:
1. **Purged**: Cells topic (replaced with "Systems")
2. **Linked Questions**: One diagram for 3-4 MCQs
3. **Experimental Design**: Variable identification (Constant, Independent, Dependent)

## PILOT EXECUTION REQUIREMENTS (REVISED)

### 20 Questions (10 P1 + 10 P6)
1. **All questions must pass 2026 compliance check**
2. **Include at least 2 "Linked Question" examples** (if found)
3. **Flag any deprecated topics** (Speed, Cells)
4. **Ensure vertical evolution mapping** for every question
5. **Apply Paper 1 fluency targets** based on question type

### Output Files (Enhanced)
1. Individual `.md` files in `/Pilot_Results/` with v4.0 schema
2. **2026 Compliance Report** showing syllabus alignment
3. **Vertical Evolution Map** showing P1→P6 connections
4. **Deprecated Topics Audit** listing any found violations
5. **Linked Questions Catalog** if discovered

### Success Metrics (Updated)
1. All 20 questions processed with v4.0 schema
2. **Zero node misclassifications** (verified against actual numbers)
3. **All questions have vertical_evolution mapping**
4. **Paper 1 fluency targets appropriately set**
5. **No deprecated topics processed without flagging**
6. **At least 1 linked question cluster identified** (if available)

## IMMEDIATE ACTIONS FOR PILOT:

1. **Revise all 5 existing P1 files** with v4.0 schema
2. **Verify number ranges** before assigning logic families
3. **Add MOE standard codes** using official syllabus mapping
4. **Create vertical evolution mapping** for each question
5. **Set paper_1_fluency_target** based on question complexity
6. **Check for deprecated topics** and flag if found
7. **Look for linked questions** in P6 materials

## MOE SUB-STRAND CODE REFERENCE (Partial)

### P1 Math Codes:
- `P1-N1-Num-100`: Numbers to 100
- `P1-N2-Add-Sub`: Addition and subtraction within 20
- `P1-M1-Time`: Time (hours, half-hours, 5-minute intervals)
- `P1-M2-Money`: Money (Singapore coins and notes)
- `P1-S1-Shapes`: 2D and 3D shapes
- `P1-D1-Graphs`: Picture graphs

### P6 Math Codes (Partial):
- `P6-A1-Alg`: Algebra
- `P6-R1-Ratio`: Ratio and proportion
- `P6-P1-Perc`: Percentage
- `P6-G1-Geom`: Geometry (including P4 nets and pie charts)
- `P6-S1-Stat`: Statistics and data analysis

---

*Schema Version: 4.0 (Post-QA/QC Brutal Feedback)*
*Last Updated: 2026-04-08*
*Compliance: 2026 MOE Syllabus Updates*