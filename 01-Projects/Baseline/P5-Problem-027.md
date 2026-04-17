---
type: problem
problemID: P5-Problem-027
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Pie Chart - Angle Calculations
difficulty: Hard
equationShadow: Angle = (Percentage ÷ 100) × 360°, or Angle = (Value ÷ Total) × 360°
traps: Temporal Misdirection (students must convert between percentages/values and angles)
visualNotes: |
  Diagram: Pie chart showing budget allocation with some angles/percentages given.
  - Title: "Monthly Budget Allocation"
  - Categories: Food (given as 90°), Rent (given as 120°), Transport, Entertainment, Savings
  - Total must equal 360°
  - Given: Food = 90°, Rent = 120°, Transport = 25% of budget
  - Students need to find the angle for Entertainment and Savings (equal angles)

  ASCII representation:
  ```
              Savings (?°)
                 ___
               /     \
              /   ●   \
    Food     |    |    |    Rent
    (90°)    \    |    /    (120°)
              \   |   /
               \__|__/
                 
         Transport      Entertainment
          (25%)            (?°)
  ```
  
  Or with approximate proportions:
  - Food: 90° (25%)
  - Rent: 120° (33.3%)
  - Transport: 90° (25%)
  - Entertainment + Savings: 60° total (16.7%), so 30° each
expectedArtifacts:
  - Student's calculation:
    - Transport angle = 25% × 360° = 90°
    - Remaining angle = 360° - 90° - 120° - 90° = 60°
    - Entertainment angle = Savings angle = 60° ÷ 2 = 30° each
  - Correct answers: Entertainment = 30°, Savings = 30°
  - Clear showing of angle calculations and verification (sum = 360°)
notes: |
  Hard-level problem requiring conversion between percentages and angles in a pie chart.
  Students must work with the constraint that all angles sum to 360°.

  Solution reasoning:
  1. Understand that a full pie chart = 360°
  2. Convert given percentage to angle:
     - Transport = 25% of total
     - Transport angle = 25% × 360° = 0.25 × 360° = 90°
  3. Sum of known angles:
     - Food: 90°
     - Rent: 120°
     - Transport: 90°
     - Total known: 90° + 120° + 90° = 300°
  4. Calculate remaining angle:
     - Remaining = 360° - 300° = 60°
  5. Split equally between Entertainment and Savings:
     - Each = 60° ÷ 2 = 30°
  6. Verify: 90° + 120° + 90° + 30° + 30° = 360° ✓

  Common errors:
  - Forgetting that pie chart total is 360° (not 100 or 180)
  - Incorrect percentage to angle conversion
  - Not splitting the remaining angle equally

  Recognition skill taught: Pie chart angles are proportional to the quantities they represent; full circle = 360°; convert percentages using (percentage ÷ 100) × 360°.
---
