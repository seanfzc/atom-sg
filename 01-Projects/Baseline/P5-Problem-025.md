---
type: problem
problemID: P5-Problem-025
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Data Interpretation - Line Graph - Interpolation
difficulty: Medium
equationShadow: Interpolated value = value between two known points (estimation)
traps: Temporal Misdirection (students might try to calculate exact value instead of estimating)
visualNotes: |
  Diagram: Line graph showing plant growth over time with missing data point.
  - Title: "Plant Height Growth"
  - Y-axis: Height in cm (scale 0-30, increments of 2)
  - X-axis: Week 0, Week 2, Week 4, Week 6, Week 8, Week 10
  - Data points: W0=5, W2=9, W4=14, W6=20, W8=25, W10=30
  - Question: "Estimate the height of the plant at Week 3. Explain your reasoning."

  ASCII representation:
  ```
  Height (cm)
      |
   30 |                                          ●
   28 |                                    
   26 |                                    
   24 |                                    
   22 |                              ●
   20 |                              ●
   18 |                        
   16 |                  ●
   14 |                  ●
   12 |            
   10 |      ●
    8 |      ●
    6 |●
    4 |●
    2 |
    0 |______|______|______|______|______|______
         W0    W2    W4    W6    W8   W10
  
         ↑
       Estimate
       Week 3
  ```
expectedArtifacts:
  - Student's estimate for Week 3: approximately 11-12 cm
  - Reasoning showing interpolation between Week 2 (9 cm) and Week 4 (14 cm)
  - Method: (9 + 14) ÷ 2 = 11.5 cm, or recognizing it's closer to Week 2
  - Acceptable range: 11-12 cm with valid explanation
notes: |
  Medium-level problem testing interpolation from a line graph.
  Students must estimate a value between two known data points.

  Solution reasoning:
  1. Identify the known points surrounding Week 3:
     - Week 2: 9 cm
     - Week 4: 14 cm
  2. Week 3 is exactly halfway between Week 2 and Week 4
  3. Linear interpolation: estimate ≈ (9 + 14) ÷ 2 = 11.5 cm
  4. Since the line is slightly curved (growth accelerating), a reasonable estimate is 11-12 cm

  Alternative valid approaches:
  - "Week 3 is halfway between Week 2 and Week 4, so about halfway between 9 and 14, which is about 11 or 12 cm"
  - "The plant grew 5 cm from Week 2 to Week 4, so it grew about 2-3 cm in the first week, making Week 3 height about 11-12 cm"

  Common errors:
  - Choosing 9 cm or 14 cm (not interpolating)
  - Calculating exact average without considering the trend
  - Estimating outside the range (less than 9 or more than 14)

  Recognition skill taught: Interpolation estimates values between known data points by considering the trend and relative position between the known points.
---
