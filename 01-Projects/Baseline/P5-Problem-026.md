---
type: problem
problemID: P5-Problem-026
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Line Graph - Multiple Lines Comparison
difficulty: Medium
equationShadow: Difference = Value A - Value B, Ratio = Value A ÷ Value B
traps: Visual-Linguistic Mismatch (students might confuse which line represents which data series)
visualNotes: |
  Diagram: Line graph with two lines comparing sales of two products over 6 months.
  - Title: "Monthly Sales Comparison - Product A vs Product B"
  - Y-axis: Sales ($ thousands) (scale 0-50, increments of 5)
  - X-axis: Jan, Feb, Mar, Apr, May, Jun
  - Product A (solid line): Jan=20, Feb=25, Mar=30, Apr=28, May=35, Jun=40
  - Product B (dashed line): Jan=30, Feb=28, Mar=25, Apr=32, May=30, Jun=35
  - Question: "In which month was the difference in sales greatest? When did Product A overtake Product B?"

  ASCII representation:
  ```
  Sales ($ thousands)
      |
   50 |                                    
   45 |                              
   40 |                                    ●A
   35 |                              ●A    ●B
   30 |  ●B    ●A    ●A           ●B
   25 |  ●B    ●A    ●B           ●A
   20 |  ●A         ●B
   15 |
   10 |
    5 |
    0 |______|______|______|______|______|______
         Jan   Feb   Mar   Apr   May   Jun
         
         A = solid line, B = dashed line
  ```
expectedArtifacts:
  - Student's calculations of monthly differences:
    - Jan: 30 - 20 = 10 (B higher)
    - Feb: 28 - 25 = 3 (B higher)
    - Mar: 30 - 25 = 5 (A higher)
    - Apr: 32 - 28 = 4 (B higher)
    - May: 35 - 30 = 5 (A higher)
    - Jun: 40 - 35 = 5 (A higher)
  - Greatest difference: January (10 thousand dollars)
  - Overtaking point: March (when A first exceeds B)
  - Clear identification of which product had higher sales each month
notes: |
  Medium-level problem comparing two data series on a line graph.
  Students must track two lines and calculate differences over time.

  Solution reasoning:
  Question 1: "In which month was the difference in sales greatest?"
  1. Calculate absolute differences for each month:
     - January: |20 - 30| = 10
     - February: |25 - 28| = 3
     - March: |30 - 25| = 5
     - April: |28 - 32| = 4
     - May: |35 - 30| = 5
     - June: |40 - 35| = 5
  2. Greatest difference is 10 in January
  3. Answer: January

  Question 2: "When did Product A overtake Product B?"
  1. Compare month by month:
     - January: B (30) > A (20)
     - February: B (28) > A (25)
     - March: A (30) > B (25) ← First month A is higher
  2. Product A overtook Product B in March
  3. Answer: March

  Recognition skill taught: When comparing two lines on a graph, calculate differences point by point; the overtaking point is where the lines cross (one goes from below to above the other).
---
