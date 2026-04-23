---
type: problem
problemID: P5-Problem-028
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Pie Chart - Working Backwards from Partial Data
difficulty: Hard
equationShadow: Total = Known Value ÷ (Known Angle ÷ 360°), or Total = Known Value ÷ Known Percentage
traps: Temporal Misdirection (students must work backwards from a known value to find the total)
visualNotes: |
  Diagram: Pie chart showing survey results with one actual value given.
  - Title: "Favorite Sports Survey"
  - Categories: Swimming, Running, Cycling, Basketball, Others
  - Given: Basketball sector angle = 72°, and this represents 45 students
  - Other angles shown: Swimming = 90°, Running = 60°, Cycling = 45°
  - Students need to find total number of students surveyed
  - Then find how many chose Swimming

  ASCII representation:
  ```
              Swimming
               (90°)
                 ___
               /     \
    Running   /   ●   \    Cycling
    (60°)    |    |    |   (45°)
              \    |    /
               \   |   /
                \__|__/
                 
          Basketball     Others
           (72°)         (?°)
          = 45 students
  ```
expectedArtifacts:
  - Student's calculation:
    - Step 1: Find what percentage 72° represents: 72° ÷ 360° = 0.20 = 20%
    - Step 2: If 20% = 45 students, then 1% = 45 ÷ 20 = 2.25 students
    - Step 3: Total students = 2.25 × 100 = 225 students
    - Alternative: Total = 45 ÷ (72/360) = 45 ÷ 0.2 = 225
    - Step 4: Swimming angle = 90°, so Swimming = (90/360) × 225 = 56.25 ≈ 56 students
  - Correct answers: Total = 225 students, Swimming = 56 students (accept 56 or 56.25)
  - Clear reasoning showing the working backwards approach
notes: |
  Hard-level problem requiring students to work backwards from a known value to find the total.
  Tests understanding of the relationship between angles, percentages, and actual values.

  Solution reasoning:
  Step 1 - Find the total number of students:
  1. Basketball angle = 72°
  2. Fraction of total = 72° ÷ 360° = 1/5 = 20% = 0.2
  3. This fraction represents 45 students
  4. Total students = 45 ÷ 0.2 = 225 students
     (Or: If 20% = 45, then 100% = 45 × 5 = 225)

  Step 2 - Find number of students who chose Swimming:
  1. Swimming angle = 90°
  2. Fraction = 90° ÷ 360° = 1/4 = 25% = 0.25
  3. Number of students = 0.25 × 225 = 56.25
  4. Since we can't have 0.25 of a student, answer ≈ 56 students
     (Or accept 56.25 as the mathematical answer)

  Verification:
  - Swimming: 90° → 56.25 students
  - Running: 60° → 37.5 students
  - Cycling: 45° → 28.125 students
  - Basketball: 72° → 45 students
  - Others: 360° - 90° - 60° - 45° - 72° = 93° → 58.125 students
  - Total: 56.25 + 37.5 + 28.125 + 45 + 58.125 = 225 ✓

  Common errors:
  - Assuming 72° = 72 students (confusing angle with count)
  - Incorrect fraction conversion
  - Forgetting to verify the total

  Recognition skill taught: When one value is known in a pie chart, work backwards using the angle proportion to find the total, then calculate other values.
---
