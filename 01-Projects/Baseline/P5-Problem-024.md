---
type: problem
problemID: P5-Problem-024
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Line Graph - Trends and Comparisons
difficulty: Medium
equationShadow: Change = Final Value - Initial Value, Ratio = Value A ÷ Value B
traps: Temporal Misdirection (students must identify correct points on the line for comparison)
visualNotes: |
  Diagram: Line graph showing temperature over a week.
  - Title: "Daily Temperature (°C) - Week 1"
  - Y-axis: Temperature °C (scale 20-40, increments of 2)
  - X-axis: Mon, Tue, Wed, Thu, Fri, Sat, Sun
  - Data points: Mon=25, Tue=28, Wed=32, Thu=30, Fri=35, Sat=33, Sun=29
  - Question: "On which day was the temperature highest? What was the increase from Monday to Friday? Between which two consecutive days was the biggest drop?"

  ASCII representation:
  ```
  Temperature (°C)
      |
   40 |                                    
   38 |                                    
   36 |                              ●
   34 |                        ●     |
   32 |            ●           |     |
   30 |            |     ●     |     |
   28 |      ●     |     |     |     |
   26 |      |     |     |     |     |     ●
   24 |●     |     |     |     |     |    /
   22 | \    |     |     |     |    /    /
   20 |  \___|_____|_____|_____|___/____/
       Mon  Tue  Wed  Thu  Fri  Sat  Sun
  ```
expectedArtifacts:
  - Student's answers:
    - Highest temperature: Friday (35°C)
    - Increase from Monday to Friday: 35 - 25 = 10°C
    - Biggest drop: Saturday to Sunday (33°C to 29°C = 4°C drop)
  - Calculations showing differences between consecutive days
  - Correct identification of trend directions
notes: |
  Medium-level problem testing line graph interpretation with trend analysis.
  Students must read values, calculate changes, and identify trends.

  Solution reasoning:
  Question 1: "On which day was the temperature highest?"
  1. Scan all data points: Mon=25, Tue=28, Wed=32, Thu=30, Fri=35, Sat=33, Sun=29
  2. Highest value is 35°C on Friday
  3. Answer: Friday

  Question 2: "What was the increase from Monday to Friday?"
  1. Monday temperature: 25°C
  2. Friday temperature: 35°C
  3. Increase = 35 - 25 = 10°C
  4. Answer: 10°C increase

  Question 3: "Between which two consecutive days was the biggest drop?"
  1. Calculate changes between consecutive days:
     - Mon→Tue: 28 - 25 = +3°C (increase)
     - Tue→Wed: 32 - 28 = +4°C (increase)
     - Wed→Thu: 30 - 32 = -2°C (drop)
     - Thu→Fri: 35 - 30 = +5°C (increase)
     - Fri→Sat: 33 - 35 = -2°C (drop)
     - Sat→Sun: 29 - 33 = -4°C (drop)
  2. Biggest drop is 4°C from Saturday to Sunday
  3. Answer: Saturday to Sunday

  Recognition skill taught: Line graphs show trends over time; calculate changes by subtraction and identify increases/decreases by the slope direction.
---
