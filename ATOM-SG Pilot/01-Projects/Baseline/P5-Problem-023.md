---
type: problem
problemID: P5-Problem-023
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Bar Graph - Finding Mode and Range
difficulty: Easy
equationShadow: Mode = most frequent value, Range = Maximum - Minimum
traps: Visual-Linguistic Mismatch (students might confuse mode with mean, or read wrong max/min values)
visualNotes: |
  Diagram: Bar graph showing test scores of students.
  - Title: "Test Scores Distribution"
  - Y-axis: Number of students (frequency)
  - X-axis: Score (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
  - Bar heights: 0=0, 10=1, 20=2, 30=3, 40=5, 50=8, 60=6, 70=4, 80=2, 90=1, 100=0
  - Question: "What is the modal score? What is the range of scores?"

  ASCII representation:
  ```
  Frequency
     |
   8 |                              ████
   7 |                              ████
   6 |                              ████  ████
   5 |                  ████        ████  ████
   4 |                  ████        ████  ████  ████
   3 |      ████        ████        ████  ████  ████
   2 |  ████████  ████  ████        ████  ████  ████  ████
   1 |  ████████  ████  ████  ████  ████  ████  ████  ████  ████
   0 |__████████__████__████__████__████__████__████__████__████__
       10   20   30   40   50   60   70   80   90
  ```
expectedArtifacts:
  - Student's identification:
    - Mode: 50 (highest bar, 8 students)
    - Range: 90 - 10 = 80 (or 80 if excluding empty categories)
  - Correct answers: Mode = 50, Range = 80
  - Clear explanation of how mode and range were found
notes: |
  Easy-level problem testing identification of mode and range from a bar graph.
  Mode is the value with highest frequency; range is max minus min.

  Solution reasoning:
  Finding the Mode:
  1. Look for the tallest bar (highest frequency)
  2. The bar at score 50 has height 8 (highest)
  3. Mode = 50

  Finding the Range:
  1. Identify the highest score with non-zero frequency: 90
  2. Identify the lowest score with non-zero frequency: 10
  3. Range = Maximum - Minimum = 90 - 10 = 80

  Alternative interpretation:
  - If considering only scores achieved by at least one student
  - Range could also be expressed as "10 to 90"

  Common errors:
  - Confusing mode with mean (calculating average instead of finding most frequent)
  - Using frequency values instead of score values for range
  - Including empty categories (0 and 100) in range calculation

  Recognition skill taught: Mode is the data value with the highest frequency (tallest bar); range is the difference between the maximum and minimum data values shown.
---
