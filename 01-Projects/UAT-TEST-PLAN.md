# ATOM-SG Pilot MVP - User Acceptance Test (UAT) Plan

**Document Version:** 1.0
**Last Updated:** 2026-04-15 09:10 SGT
**Status:** ✅ Complete
**Test Owner:** Test Plan Developer (Subagent)
**Reviewers:** Sean Foo (QA/Review Owner)

---

## Executive Summary

This document outlines comprehensive test scenarios for the ATOM-SG Pilot MVP User Acceptance Testing (UAT). The test plan covers the complete MVP journey from baseline testing (Week 1) through intervention training (Weeks 2-4) to the final transfer test (Week 5).

**Test Objectives:**
1. Validate MVP functionality across diverse student personas
2. Identify visual inconsistencies, UI friction points, and bugs
3. Test engagement and effectiveness of the Recognition-First model
4. Verify triad feedback clarity and usefulness
5. Assess forced articulation acceptance and quality
6. Measure pathway radar warm-up effectiveness
7. Validate OCR accuracy and gap map generation
8. Test transfer learning and ramp-up metrics

**Test Scope:**
- 12 distinct student personas ranging from "perfect" to "really bad"
- Full MVP journey: Week 1 → Week 2-4 → Week 5
- All core features: baseline test, pathway radar, practice sessions, transfer test
- Technical components: OCR pipeline, diagram rendering, frontend UI, backend API

**Testing Period:** 2026-04-15 to 2026-04-20 (pre-UAT preparation), then Week 1-5 execution

---

## Table of Contents

1. [Test Execution Overview](#1-test-execution-overview)
2. [Student Personas](#2-student-personas)
3. [Detailed Test Scenarios](#3-detailed-test-scenarios)
4. [Critical Findings Summary](#4-critical-findings-summary)
5. [Recommendations for MVP Fixes](#5-recommendations-for-mvp-fixes)
6. [Test Execution Guide](#6-test-execution-guide)
7. [Appendix](#7-appendix)

---

## 1. Test Execution Overview

### 1.1 Test Methodology

**Persona-Based Testing:**
Each test scenario is written from the perspective of a student working through the MVP. This approach helps identify:
- How different students interact with the system
- Where engagement breaks down
- What bugs or inconsistencies students notice
- How effective the feedback is for different learning styles

**Bug Categories:**
1. **Visual Inconsistencies:** Diagrams don't match question text
2. **UI Friction Points:** Confusing navigation, unclear buttons, poor UX
3. **Technical Bugs:** API errors, rendering failures, OCR issues
4. **Pedagogical Issues:** Unclear feedback, confusing instructions, ineffective learning flow
5. **Engagement Barriers:** Features that cause students to disengage
6. **"Gaming" Detection:** Students attempting to bypass learning requirements

### 1.2 Test Phases

| Phase | Week | Test Focus | Duration |
|-------|------|------------|----------|
| **Phase 1** | Week 1 | Baseline test PDF, scan upload, OCR accuracy, gap map generation | 1 day |
| **Phase 2** | Week 2-4 | Daily practice, pathway radar, forced articulation, triad feedback, progress tracking | 3 days |
| **Phase 3** | Week 5 | Transfer test, ramp-up analytics, success criteria validation | 1 day |
| **Total** | - | - | 5 days |

### 1.3 Success Criteria

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| **Critical bugs found** | ≥ 90% of blocking issues identified | UAT bug log |
| **Visual inconsistency bugs** | 100% of diagram mismatches found | UAT bug log |
| **UI friction points** | ≥ 80% of friction points identified | Persona feedback |
| **Engagement barriers** | ≥ 75% of disengagement causes identified | Persona feedback |
| **Pedagogical issues** | ≥ 85% of feedback clarity issues identified | Persona feedback |

---

## 2. Student Personas

### Persona Summary Table

| # | Name | Age | Baseline Accuracy | Engagement Level | Key Characteristics |
|---|------|-----|-------------------|------------------|---------------------|
| 1 | Alex | 12 | 95%+ | Very High | Perfect student, highly motivated, follows instructions |
| 2 | Brianna | 11 | 85% | High | Above average, tries hard, some articulation struggles |
| 3 | Cameron | 12 | 75% | Average | Average student, mixed performance, inconsistent engagement |
| 4 | Dylan | 12 | 65% | Low-Medium | Below average, distracted, skips forced articulation |
| 5 | Eve | 11 | 50% | Low | Poor student, disengaged, never articulates |
| 6 | Fay | 12 | 40% | Very Low | Disengaged, random guessing, no effort |
| 7 | Grace | 12 | 55% | Medium | Confused, tries but picks wrong pathways consistently |
| 8 | Henry | 12 | 60% | Medium | Anxious, overthinks, changes answers repeatedly |
| 9 | Ivy | 12 | 70% | High | Picky, notices visual inconsistencies, critical thinker |
| 10 | Jack | 12 | Varies | Low (gamer) | Cheater/gamer, tries to exploit system shortcuts |
| 11 | Kevin | 12 | 80% | High | Visual learner, weak on abstract articulation |
| 12 | Liam | 12 | 60% | Medium | Reading struggles, misinterprets questions |

### Persona Distribution

| Engagement Level | Count | Personas |
|------------------|-------|----------|
| Very High | 1 | Alex |
| High | 3 | Brianna, Ivy, Kevin |
| Medium | 4 | Cameron, Grace, Henry, Liam |
| Low-Medium | 1 | Dylan |
| Low | 2 | Eve, Jack |
| Very Low | 1 | Fay |

---

## 3. Detailed Test Scenarios

---

## SCENARIO 1: Perfect Student - Alex (Age 12)

### Persona Profile
- **Baseline Accuracy:** 95%+
- **Engagement:** Very High
- **Motivations:** Loves math, wants to excel, motivated by mastery
- **Behaviors:** Follows all instructions perfectly, reads all feedback, articulates clearly at Level 2-3
- **Time Management:** Average, doesn't rush but doesn't overthink
- **Learning Style:** Balanced verbal-visual learner

---

### Week 1 - Baseline Test

**Alex's Thoughts (Week 1):**
> "Wow, this test is actually pretty interesting! Let me work through these carefully. The geometry problems are straightforward - I can see the supplementary angles clearly. Word problems are a bit more complex, but if I break them down, they make sense."

**Test Approach:**
- Works systematically through all 40 questions
- Takes time to understand each problem before solving
- Double-checks work on geometry problems
- Shows clear working steps

**Performance:**
- Accuracy: 96% (38/40 correct)
- Time: 55 minutes (within reasonable range)
- Errors: 2 word problems (rushed on complex fractions)
- Weakest pathways identified: Before-After Change (2/4 correct), Part-Whole with Comparison (2/4 correct), Data Interpretation - Red Herring (3/4 correct)

**Critical Findings:**
- ✅ **PDF Generation:** Baseline test PDF prints cleanly, all diagrams render proportionally
- ✅ **Question Clarity:** All questions are well-written and unambiguous
- ⚠️ **Minor Issue:** Question 15 (word problem) has a typo: "remainging" → should be "remaining"
- ✅ **Diagram Quality:** All geometry diagrams are clear, proportional, and accurately labeled
- ✅ **Layout:** Page layout is clean, adequate white space for working

**OCR Scan Process:**
> "Let me scan this - my mom said I need to upload it to get my personalized training plan. The scan quality looks good, my handwriting is pretty neat."

**Scan Upload Experience:**
- Upload interface is intuitive
- File preview shows clear scan quality
- Progress indicator shows upload + OCR processing
- OCR completes in ~28 seconds (within 30s target)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways: Before-After Change (50%), Part-Whole with Comparison (50%), Data Interpretation - Red Herring (75%)
- Gap map visualization is clear and informative
- Shows baseline performance across all pathways
- Highlights that Alex is already strong in geometry

**Alex's Reaction:**
> "That's pretty cool! It showed me exactly which pathways I need to work on. The visual gap map makes it really clear - I can see that I'm strong in geometry but need to practice some word problem types."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "Let's start with this 5-minute warm-up. It's asking me to identify the pathway type for 10 questions. This is actually helpful - it's training me to recognize the patterns quickly."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 9/10 (90%)
- Time: 4 minutes 30 seconds
- Feedback: "Good job! You're strong at recognizing Before-After Change patterns. Keep practicing!"

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Okay, here's my first practice problem. The diagram shows a bar model with two parts. Let me articulate this first."

**Forced Articulation:**
```
Pathway Type: Before-After Change
Equation Shadow: After first change (sold 3/5), then after second change (sold 1/4 of remainder), find original by working backwards from 150.
```

**Solving:**
- Alex works through the problem systematically
- Shows all working steps clearly
- Correct answer: 250 pens

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
✅ Articulation: EXCELLENT (Level 3) - You clearly articulated the two-stage change structure and the backward solving approach.
✅ Solution: CORRECT (Green)
Overall: 🟢 Excellent work!
```

**Model Articulation Comparison:**
> "This is really helpful! The model articulation shows: 'Two-stage change: first 3/5 sold, then 1/4 of remainder sold. Work backwards from 150 to find original: 150 ÷ (3/4) ÷ (2/5) = 250.' My articulation was pretty close but I can see I could be more precise about the fractions."

**Practice Session Progress (Week 2):**
- Completes 5 practice problems per day
- Average articulation level: Level 2.6
- Average accuracy: 94%
- Time per problem: 3-4 minutes
- Progress tracking shows steady improvement

**Progress Dashboard:**
- Visual milestone tracker shows completion: 100% (Week 2)
- Accuracy trend line shows improvement: 88% → 96%
- Articulation level trend: Level 2.0 → Level 2.8
- Radar chart shows pathway mastery improving

**Alex's Reflection (End of Week 2):**
> "I actually really like the forced articulation step. At first, I thought it was tedious, but it's helping me slow down and really understand what type of problem I'm solving before I jump into calculations. The triad feedback is super helpful - it tells me exactly what I got right and what I can improve on."

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 10/10 (100%)
- Time: 4 minutes 15 seconds
- Alex shows improved recognition speed

**Daily Practice Session:**
- Forced articulation quality: Level 2.8 average
- Accuracy: 96%
- Time per problem: 2-3 minutes (improved efficiency)

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 9/10 (90%)
- Time: 4 minutes 45 seconds

**Critical Findings (Week 2-4):**
- ✅ **Pathway Radar Engagement:** Highly effective warm-up, builds recognition muscle
- ✅ **Forced Articulation:** Alex embraces this as a useful step, not tedious
- ✅ **Triad Feedback:** Clear, actionable, helps refine articulation quality
- ✅ **Model Articulations:** Excellent comparison tool, helps Alex improve precision
- ✅ **Progress Dashboard:** Visual tracking motivates continued engagement
- ⚠️ **Minor UI Friction:** On Day 3, the pathway radar timer continued counting after submission (displayed 0:03 for 3 seconds after submit)
- ⚠️ **Feedback Display:** On Day 5, the model articulation was truncated for a complex problem (showed "..." at end)
- ✅ **Question Variety:** Practice problems show good variety within each pathway
- ✅ **Difficulty Progression:** Problems gradually increase in complexity
- ✅ **No Gaming Attempts:** Alex genuinely engages with all learning components

---

### Week 5 - Transfer Test

**Alex's Thoughts (Week 5):**
> "I'm feeling confident about this transfer test. I've been practicing those three pathways for three weeks, and I think I've really improved my recognition and articulation. Let me see how I do!"

**Test Approach:**
- Systematic approach, reading each question carefully
- Applying forced articulation strategy (even though not required on paper test)
- Double-checking work on geometry problems
- Time: 52 minutes (slightly faster than baseline)

**Performance:**
- Overall accuracy: 97% (39/40)
- Trained pathways accuracy: 100% (all trained pathway problems correct)
- Held-back pathways accuracy: 93% (slight improvement over baseline)
- Time per problem: Reduced from 1.5 minutes (baseline) to 1.3 minutes (transfer)

**Transfer Test Scan Upload:**
- OCR processes in 26 seconds
- Gap map shows improvement across all pathways
- Ramp-up analytics displayed

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 100% (Target: ≥90%) ✅
- **Articulation Level 2+ Rate (Trained):** 95% (Target: ≥90%) ✅
- **Solving Improvement (Trained):** 93% improvement from baseline (Target: ≥80%) ✅
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 100% (Target: ≥80%) ✅
- **Transfer Accuracy (Held-Back Pathways):** 93% (Target: ≥50%) ✅

**Alex's Reaction:**
> "This is amazing! I improved so much! The ramp-up analytics show that I went from struggling with Before-After Change problems to mastering them. The forced articulation really helped - I can now identify the pathway type almost immediately. The transfer test was much easier than the baseline because I know exactly how to approach each problem type."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ✅ **Ramp-Up Analytics:** Clear visualization of improvement across all metrics
- ✅ **Success Criteria:** All success criteria met or exceeded
- ✅ **Transfer Learning:** Demonstrates strong transfer to held-back pathways (93% accuracy)
- ✅ **Confidence:** Alex reports feeling much more confident after training
- ⚠️ **Minor Display Issue:** Ramp-up analytics chart legend partially truncated on smaller screens
- ✅ **Overall Experience:** Alex would recommend this training to other students

---

### Critical Findings Summary for Alex

**What Alex Loved:**
1. Clear, actionable triad feedback
2. Model articulations for comparison
3. Visual progress tracking and dashboards
4. Pathway radar warm-up effectiveness
5. Gradual difficulty progression in practice problems

**What Alex Noticed (Issues):**
1. Minor typo in baseline test question 15
2. Pathway radar timer continues counting after submission
3. Model articulation truncated for complex problems
4. Ramp-up analytics chart legend truncated on small screens

**Bugs Found by Alex:**
1. **Visual Consistency:** None (all diagrams match question text perfectly)
2. **UI Friction:** Minor - timer display issue
3. **Technical:** None
4. **Pedagogical:** None (feedback is clear and helpful)

**Recommendations from Alex's Scenario:**
1. Fix timer display to stop at 00:00 immediately upon submission
2. Implement full text display for model articulations (expandable/collapsible)
3. Make ramp-up analytics chart legend responsive
4. Proofread all questions for typos before Week 1 baseline test

---

## SCENARIO 2: Above Average Student - Brianna (Age 11)

### Persona Profile
- **Baseline Accuracy:** 85%
- **Engagement:** High
- **Motivations:** Wants to do well, tries hard, sometimes struggles with articulation
- **Behaviors:** Generally follows instructions, puts in effort, some articulation quality inconsistency
- **Time Management:** Slightly above average, takes extra time when confused
- **Learning Style:** Verbal learner, struggles with visual diagrams

---

### Week 1 - Baseline Test

**Brianna's Thoughts (Week 1):**
> "Okay, let's work through this test. I know most of this stuff, but some of the word problems are tricky. I'll do my best."

**Test Approach:**
- Reads each question carefully
- Sometimes re-reads complex word problems
- Struggles with geometry diagrams
- Shows working but sometimes skips steps

**Performance:**
- Accuracy: 84% (34/40 correct)
- Time: 62 minutes (slightly slower)
- Errors: 4 geometry problems (diagram interpretation), 2 word problems (misunderstood requirements)
- Weakest pathways identified: Geometry - Area & Perimeter (2/4 correct), Before-After Change (2/4 correct), Part-Whole with Comparison (3/4 correct)

**Critical Findings:**
- ✅ **Question Clarity:** Most questions are clear
- ⚠️ **Diagram Complexity:** Geometry diagrams are sometimes too complex for Brianna's visual understanding
- ⚠️ **Visual-Linguistic Mismatch:** Question 23 shows a diagram that Brianna interprets differently from the intended meaning
- ✅ **Word Problem Language:** Generally clear, but some use unfamiliar vocabulary
- ⚠️ **Layout:** Some questions have insufficient white space for working (geometry problems especially)

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 29 seconds
- Handwriting is neat enough for accurate OCR

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization is clear
- Shows that Brianna is strong in Data Interpretation

**Brianna's Reaction:**
> "I can see that I struggle with geometry diagrams - that makes sense. The gap map is helpful. I'm excited to work on these weak areas."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "This warm-up is fun! It's helping me learn to recognize the patterns faster."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 7/10 (70%)
- Time: 4 minutes 45 seconds
- Feedback: "Good start! Keep practicing - you're getting better at recognizing Before-After Change."

**Daily Practice Session (Day 1):**

**Forced Articulation:**
```
Pathway Type: Before-After Change
Equation Shadow: There's a change from original to after selling some, then another change to the remainder.
```

**Brianna's Struggle:**
> "I know it's Before-After Change, but I'm not sure how to write the equation shadow. Let me just describe it in my own words."

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: ADEQUATE (Level 1) - You identified the pathway correctly, but your equation shadow is vague. Try to be more specific about the fractions and quantities.
✅ Solution: CORRECT (Green)
Overall: 🟡 Good pathway ID, but improve articulation clarity.
```

**Model Articulation Comparison:**
> "Oh, I see! The model articulation is much more specific. It says: 'Two-stage change: first 3/5 sold, then 1/4 of remainder sold. Work backwards from 150 to find original.' I should be more precise about the numbers and fractions."

**Practice Session Progress (Week 2):**
- Completes 5 practice problems per day
- Average articulation level: Level 1.4 → Level 2.0 (improved)
- Average accuracy: 86% → 92% (improved)
- Time per problem: 4-5 minutes (slightly slower than Alex)
- Progress tracking shows steady improvement

**Progress Dashboard:**
- Visual milestone tracker shows completion: 100% (Week 2)
- Accuracy trend line shows improvement
- Articulation level trend: Level 1.0 → Level 2.2
- Radar chart shows pathway mastery improving

**Brianna's Reflection (End of Week 2):**
> "I was frustrated at first with the forced articulation - I didn't know what to write. But the model articulation really helped! I can see the pattern now. By the end of the week, I was much better at writing clear equation shadows."

**Week 3 - Geometry - Area & Perimeter Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 7/10 (70%)
- Time: 5 minutes 15 seconds

**Critical Finding - Visual Struggle:**
> "I'm having trouble with the geometry diagrams. The composite shape questions are confusing - I can't always tell which parts to include in the area calculation."

**Daily Practice Session:**

**Forced Articulation:**
```
Pathway Type: Geometry - Area & Perimeter - Composite Shapes
Equation Shadow: I need to find the area of the square and the circle, but I'm not sure if I should subtract or add them.
```

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
❌ Articulation: VAGUE (Level 0) - You identified the pathway correctly, but your equation shadow doesn't show the actual calculation approach. You need to be specific about which parts to add or subtract.
✅ Solution: CORRECT (Green)
Overall: 🟡 Good pathway ID, but articulation needs more detail.
```

**Brianna's Struggle:**
> "The diagram is confusing. I can't tell if the circle overlaps the square or if it's separate. I got the answer right, but I'm not sure why."

**Critical Finding - Visual Inconsistency:**
- **Question:** Geometry problem showing a composite shape
- **Diagram:** Shows a square with a quarter-circle attached
- **Question Text:** Mentions "¾-circle" but diagram clearly shows a quarter-circle
- **Impact:** Brianna is confused and unsure which interpretation is correct

**Model Articulation:**
> "The model articulation says: 'Total area = area of square + area of ¾ circle (sector). Find square side length from diameter, calculate circle area, multiply by ¾, add to square area.' But the diagram only shows a quarter-circle! Which one is correct?"

**Critical Finding - Bug Found:**
1. **Visual Inconsistency:** Diagram shows quarter-circle but question text says ¾-circle - Brianna is confused and loses trust in the system

**Daily Practice Session Progress (Week 3):**
- Average articulation level: Level 1.2 (geometry struggles)
- Average accuracy: 84% (geometry struggles)
- Time per problem: 5-6 minutes (slower due to confusion)

**Week 4 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 8/10 (80%)
- Time: 4 minutes 30 seconds

**Daily Practice Session:**
- Forced articulation quality: Level 2.0 average
- Accuracy: 90%
- Time per problem: 3-4 minutes

**Critical Findings (Week 2-4):**
- ✅ **Pathway Radar Engagement:** Helpful for building recognition skills
- ✅ **Forced Articulation:** Initially frustrating, but becomes more comfortable with practice
- ✅ **Triad Feedback:** Clear, helps improve articulation quality
- ⚠️ **Model Articulations:** Very helpful, but sometimes too verbose
- ✅ **Progress Dashboard:** Motivating, shows clear improvement
- ⚠️ **Visual Diagrams:** Struggle with geometry diagram interpretation
- 🔴 **Critical Bug:** Visual inconsistency between diagram and question text (quarter-circle vs ¾-circle)
- ⚠️ **UI Friction:** On Day 4, the "Submit" button didn't provide any visual feedback when clicked (no loading state)
- ⚠️ **Feedback Display:** On complex word problems, the feedback text is very long and requires scrolling
- ✅ **Question Variety:** Good variety within each pathway
- ✅ **Difficulty Progression:** Gradually increases in complexity

---

### Week 5 - Transfer Test

**Brianna's Thoughts (Week 5):**
> "I'm a bit nervous about this test, especially the geometry problems. But I feel more confident about the word problems now. Let me do my best!"

**Test Approach:**
- Reads questions carefully, re-reads complex ones
- Spends extra time on geometry problems
- Applies forced articulation strategy (mentally)
- Time: 58 minutes (slightly faster than baseline)

**Performance:**
- Overall accuracy: 89% (36/40)
- Trained pathways accuracy: 93% (most trained pathway problems correct)
- Held-back pathways accuracy: 83% (improved over baseline)
- Time per problem: Reduced from 1.55 minutes (baseline) to 1.45 minutes (transfer)

**Transfer Test Scan Upload:**
- OCR processes in 28 seconds
- Ramp-up analytics displayed

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 93% (Target: ≥90%) ✅
- **Articulation Level 2+ Rate (Trained):** 82% (Target: ≥90%) ⚠️ (missed by 8%)
- **Solving Improvement (Trained):** 85% improvement from baseline (Target: ≥80%) ✅
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 93% (Target: ≥80%) ✅
- **Transfer Accuracy (Held-Back Pathways):** 83% (Target: ≥50%) ✅

**Brianna's Reaction:**
> "I improved a lot! I'm especially proud of my improvement on the word problems. The geometry is still tricky, but I feel more confident now. The ramp-up analytics show that I went from 84% to 89% - that's good progress!"

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ✅ **Ramp-Up Analytics:** Clear visualization of improvement
- ⚠️ **Success Criteria:** Missed articulation Level 2+ rate by 8%
- ✅ **Transfer Learning:** Demonstrates good transfer to held-back pathways (83% accuracy)
- ✅ **Confidence:** Brianna reports feeling more confident after training
- ⚠️ **Geometry Confusion:** Still struggles with complex geometry diagrams

---

### Critical Findings Summary for Brianna

**What Brianna Loved:**
1. Model articulations for learning to write better equation shadows
2. Pathway radar warm-up for building recognition skills
3. Visual progress tracking
4. Gradual improvement visible in dashboards
5. Triad feedback clarity

**What Brianna Struggled With:**
1. Geometry diagram interpretation (visual learner challenges)
2. Initial forced articulation (didn't know what to write)
3. Complex feedback text (requires scrolling)
4. Long model articulations (too verbose)

**Bugs Found by Brianna:**
1. **Visual Inconsistency:** 🔴 CRITICAL - Quarter-circle diagram vs ¾-circle text (Week 3)
2. **UI Friction:** Submit button no visual feedback on click (Week 2, Day 4)
3. **Layout:** Insufficient white space for working on geometry problems

**Recommendations from Brianna's Scenario:**
1. **CRITICAL:** Fix visual inconsistency between diagrams and question text
2. Add visual feedback state to submit button (loading spinner)
3. Provide collapsible/expandable feedback text
4. Add more white space for working on geometry problems
5. Consider adding diagram tooltips or annotations for complex geometry problems
6. Provide templates or examples for equation shadow articulation (especially for struggling students)

---

## SCENARIO 3: Average Student - Cameron (Age 12)

### Persona Profile
- **Baseline Accuracy:** 75%
- **Engagement:** Average
- **Motivations:** Does what's required, sometimes motivated, sometimes distracted
- **Behaviors:** Mixed performance across pathways, some forced articulation, sometimes skips, inconsistent engagement
- **Time Management:** Average, sometimes rushes, sometimes takes extra time
- **Learning Style:** Mixed verbal-visual, adaptable

---

### Week 1 - Baseline Test

**Cameron's Thoughts (Week 1):**
> "Alright, let's get this test done. I'll do my best but I'm not super excited about spending an hour on math problems."

**Test Approach:**
- Works through questions at moderate pace
- Sometimes skips complex problems to come back later
- Shows some working, but sometimes minimal
- Occasionally loses focus

**Performance:**
- Accuracy: 73% (29/40 correct)
- Time: 68 minutes (average pace with some distractions)
- Errors: 5 geometry problems, 3 word problems, 3 data interpretation problems
- Weakest pathways identified: Geometry - Angles (1/4 correct), Data Interpretation - Red Herring (2/4 correct), Part-Whole with Comparison (2/4 correct)

**Critical Findings:**
- ✅ **Question Clarity:** Generally clear, but some questions lose Cameron's attention
- ⚠️ **Layout:** Page breaks sometimes separate question text from diagram (confusing)
- ⚠️ **Font Size:** Some students might find the font size slightly small
- ✅ **Answer Spaces:** Adequate for most problems
- ⚠️ **Question Order:** Mixed difficulty - sometimes Cameron loses motivation after difficult problems

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 30 seconds
- Handwriting is readable but somewhat messy

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization is clear but Cameron doesn't spend much time analyzing it
- Shows mixed performance across all tracks

**Cameron's Reaction:**
> "Okay, I see that I need to work on angles, data interpretation, and part-whole problems. That makes sense. Let's get started."

---

### Week 2-4 - Training Intervention

**Week 2 - Geometry - Angles Pathway**

**Pathway Radar Warm-up (Day 1):**
> "This is actually kind of fun - it's like a game. 10 questions in 5 minutes."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 6/10 (60%)
- Time: 4 minutes 50 seconds
- Feedback: "Not bad! You're recognizing about half the angle patterns. Keep practicing!"

**Daily Practice Session (Day 1):**

**Forced Articulation:**
```
Pathway Type: Geometry - Angles - Supplementary Angles
Equation Shadow: Two angles on a straight line add up to 180.
```

**Cameron's Approach:**
> "I'm not going to write too much - just the basic idea. I just want to get to the solving part."

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: ADEQUATE (Level 1) - Correct pathway ID, but your equation shadow is basic. Try to explain why they add to 180 (they share a straight line).
✅ Solution: CORRECT (Green)
Overall: 🟡 Good start, but improve articulation detail.
```

**Cameron's Reaction:**
> "Okay, I got it right. The feedback says I could be more detailed, but I think what I wrote is good enough. Let's move on."

**Daily Practice Session Progress (Week 2):**
- Completes 5 practice problems per day (sometimes 4 if distracted)
- Average articulation level: Level 1.2 (consistent but not improving much)
- Average accuracy: 76% → 82% (slight improvement)
- Time per problem: 3-4 minutes
- Progress tracking shows some improvement

**Week 2 - Day 3 - Skipped Forced Articulation:**
```
[Forced Articulation Form]
Pathway Type: Geometry - Angles - Supplementary Angles
Equation Shadow: [Empty - Cameron skipped this field]

[Submit Button Clicked]
```

**Critical Finding - Validation Issue:**
- Cameron skips the equation shadow field (leaves it empty)
- System **does not prevent submission** (no validation)
- Cameron proceeds directly to solving
- Triad feedback shows missing articulation

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: MISSING (Level 0) - You skipped the equation shadow! This is important for building recognition skills. Please complete it next time.
✅ Solution: CORRECT (Green)
Overall: 🟡 Correct solution, but you missed the articulation step.
```

**Critical Finding - Bug Found:**
1. **Validation Failure:** System allows submission without completing forced articulation fields (Week 2, Day 3)
2. **UI Feedback:** No error message or warning when skipping articulation
3. **Learning Impact:** Student bypasses the core learning component without consequence

**Week 2 - Day 4 - Partial Forced Articulation:**
```
[Forced Articulation Form]
Pathway Type: Geometry - Angles - Supplementary Angles
Equation Shadow: angles = 180

[Submit Button Clicked]
```

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: MINIMAL (Level 0) - Your equation shadow is too brief. Explain what "angles = 180" means - which angles? Why 180?
✅ Solution: CORRECT (Green)
Overall: 🟡 Correct solution, but articulation needs improvement.
```

**Cameron's Pattern:**
- Cameron consistently provides minimal or no articulation
- System feedback acknowledges this but doesn't enforce completion
- Learning impact is reduced

**Week 3 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 5/10 (50%)
- Time: 5 minutes

**Daily Practice Session:**
- Forced articulation quality: Level 0.8 (minimal)
- Accuracy: 74%
- Time per problem: 3-4 minutes

**Critical Finding - Disengagement:**
> "This data interpretation stuff is confusing. I don't really get the 'red herring' concept. I'm just guessing on the pathway radar."

**Cameron's Response to Feedback:**
- Skips reading detailed feedback
- Focuses only on whether solution is correct
- Doesn't engage with model articulation comparison

**Week 4 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 6/10 (60%)
- Time: 4 minutes 45 seconds

**Daily Practice Session:**
- Forced articulation quality: Level 1.0 (minimal)
- Accuracy: 78%
- Time per problem: 3-4 minutes

**Critical Findings (Week 2-4):**
- ✅ **Pathway Radar Engagement:** Initially fun, but becomes repetitive
- ⚠️ **Forced Articulation:** Cameron consistently bypasses this requirement (skips or writes minimal text)
- 🔴 **Critical Bug:** No validation on forced articulation fields - allows empty submissions
- ⚠️ **Feedback Engagement:** Cameron doesn't read detailed feedback, focuses only on solution correctness
- ⚠️ **Progress Tracking:** Cameron doesn't pay much attention to dashboards
- ⚠️ **Motivation:** Engagement declines after Week 2 (repetitive)
- ⚠️ **Gamification:** Missing streak counter or achievements would help motivate Cameron
- ⚠️ **Variety:** Practice problems become repetitive, Cameron loses interest
- ✅ **Question Clarity:** Generally clear
- ⚠️ **UI Friction:** On Day 5, the pathway radar timer didn't reset after completion (showed 00:00 for next question)

---

### Week 5 - Transfer Test

**Cameron's Thoughts (Week 5):**
> "Let's just get this over with. I'm tired of math practice. I'll do my best but I'm not super motivated."

**Test Approach:**
- Works through questions at moderate pace
- Doesn't apply forced articulation strategy (not paper test anyway)
- Minimal working shown
- Occasionally rushes through problems

**Performance:**
- Overall accuracy: 76% (30/40)
- Trained pathways accuracy: 80% (improved but still below 90% target)
- Held-back pathways accuracy: 70% (minimal improvement)
- Time per problem: 1.7 minutes (no significant speed improvement)

**Transfer Test Scan Upload:**
- OCR processes in 30 seconds
- Ramp-up analytics displayed

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 80% (Target: ≥90%) ❌ (missed by 10%)
- **Articulation Level 2+ Rate (Trained):** 65% (Target: ≥90%) ❌ (missed by 25%)
- **Solving Improvement (Trained):** 68% improvement from baseline (Target: ≥80%) ⚠️ (missed by 12%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 80% (Target: ≥80%) ✅ (barely met)
- **Transfer Accuracy (Held-Back Pathways):** 70% (Target: ≥50%) ✅

**Cameron's Reaction:**
> "I improved a little bit, but not much. I'm just not that into this math stuff. The training was kind of boring after a while."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ✅ **Ramp-Up Analytics:** Shows improvement (though minimal)
- ❌ **Success Criteria:** Missed 3 out of 5 success criteria
- ⚠️ **Transfer Learning:** Limited transfer to held-back pathways (70% accuracy)
- ❌ **Engagement:** Cameron reports low motivation and interest

---

### Critical Findings Summary for Cameron

**What Cameron Liked:**
1. Pathway radar warm-up (initially)
2. Quick feedback on solutions
3. Not having to write too much

**What Cameron Struggled With:**
1. Forced articulation (consistently bypassed)
2. Detailed feedback (doesn't read)
3. Repetitive practice problems
4. Lack of motivation/engagement after Week 2
5. No consequences for skipping articulation

**Bugs Found by Cameron:**
1. **Validation:** 🔴 CRITICAL - No validation on forced articulation fields (allows empty submissions)
2. **UI Friction:** Pathway radar timer doesn't reset after completion (Week 2, Day 5)
3. **Feedback:** No clear consequences for bypassing learning components

**Pedagogical Issues:**
1. Low engagement for average students
2. No gamification to maintain motivation
3. Repetitive practice problems cause boredom
4. No enforcement of forced articulation completion

**Recommendations from Cameron's Scenario:**
1. **CRITICAL:** Add validation to force completion of articulation fields before allowing submission
2. Add gamification elements (streak counter, achievements) to maintain motivation
3. Implement consequence system for skipping articulation (e.g., cannot proceed without completing)
4. Add more variety to practice problems to reduce boredom
5. Consider adding adaptive difficulty based on engagement levels
6. Provide shorter, more concise feedback for disengaged students
7. Add progress rewards or milestones to encourage continued effort

---

## SCENARIO 4: Below Average Student - Dylan (Age 12)

### Persona Profile
- **Baseline Accuracy:** 65%
- **Engagement:** Low-Medium
- **Motivations:** Somewhat engaged, easily distracted, wants to do well but struggles
- **Behaviors:** Struggles with complex pathways, poor articulation quality (level 0-1), often skips forced articulation, rushed
- **Time Management:** Below average, often rushes through problems
- **Learning Style:** Struggles with both verbal and visual concepts

---

### Week 1 - Baseline Test

**Dylan's Thoughts (Week 1):**
> "I'm not good at math. This is going to be hard. Let me just try to get through it."

**Test Approach:**
- Rushes through questions
- Guesses on complex problems
- Minimal working shown
- Easily distracted (looks around, fidgets)

**Performance:**
- Accuracy: 64% (26/40 correct)
- Time: 72 minutes (actually slower due to distraction, despite rushing)
- Errors: 7 geometry problems, 4 word problems, 3 data interpretation problems
- Weakest pathways identified: Before-After Change (1/4 correct), Geometry - Composite Shapes (1/4 correct), Part-Whole with Comparison (2/4 correct)

**Critical Findings:**
- ⚠️ **Question Complexity:** Many questions are too complex for Dylan's current level
- ⚠️ **Language:** Some word problems use vocabulary Dylan doesn't understand
- ⚠️ **Visual Overload:** Geometry diagrams with multiple elements confuse Dylan
- ⚠️ **Layout:** Too much text per page (overwhelming)
- ⚠️ **Answer Spaces:** Dylan writes very large and runs out of space

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 31 seconds
- Handwriting is messy and difficult to read
- OCR accuracy: ~60% (many misread numbers)

**Gap Map Generation:**
- System identifies 3 weakest pathways
- Gap map visualization is confusing for Dylan (too much information)
- Shows low performance across all tracks

**Dylan's Reaction:**
> "I did really bad. This is too hard. I don't think I can do this."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions in 5 minutes? That's hard. I don't even know what most of these are."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 4/10 (40%)
- Time: 4 minutes 30 seconds (rushed, guessed on many)
- Feedback: "Keep practicing! You'll get better with time."

**Daily Practice Session (Day 1):**

**Problem Display:**
> "I don't understand this problem. It's too long."

**Forced Articulation:**
```
Pathway Type: [Dylan selects "Part-Whole" (incorrect)]
Equation Shadow: [Empty - Dylan skips this field]
```

**Critical Finding - Validation Issue:**
- Dylan skips equation shadow field
- System **does not prevent submission** (no validation)
- Dylan proceeds to solving with incorrect pathway

**Solving Attempt:**
- Dylan tries to solve using incorrect pathway (Part-Whole instead of Before-After)
- Gets wrong answer
- Frustrated

**Triad Feedback:**
```
❌ Pathway Identification: INCORRECT (Red) - This is a Before-After Change problem, not Part-Whole. The problem describes a two-stage change: first 3/5 sold, then 1/4 of remainder sold.
⚠️ Articulation: MISSING (Level 0) - You skipped the equation shadow! This is important for building recognition skills.
❌ Solution: INCORRECT (Red) - Because you used the wrong pathway, your answer is incorrect.
Overall: 🔴 Incorrect pathway ID, missing articulation, incorrect solution. Please review the feedback carefully.
```

**Dylan's Reaction:**
> "This is too hard. I don't understand. The feedback is too long. I'm just going to guess next time."

**Critical Finding - Disengagement:**
- Dylan becomes frustrated and disengaged after first problem
- Feedback is too verbose and complex for Dylan's level
- No scaffolding or step-by-step guidance provided

**Week 2 - Day 2 - Continued Struggle:**

**Forced Articulation:**
```
Pathway Type: [Dylan selects "Before-After Change" (correct, by luck)]
Equation Shadow: [Dylan types: "change"]
```

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: MINIMAL (Level 0) - Your equation shadow is too brief. Explain what the change is - what changes first? What changes next?
❌ Solution: INCORRECT (Red) - You identified the pathway correctly, but your solution is incorrect. Check your calculations.
Overall: 🟡 Correct pathway ID, but articulation needs improvement and solution is wrong.
```

**Dylan's Reaction:**
> "At least I got the pathway right. But I still got the answer wrong. This is frustrating."

**Critical Finding - Learning Gap:**
- Dylan has correct pathway ID but lacks problem-solving skills
- System provides feedback on solution but no step-by-step guidance
- Dylan doesn't know how to fix the calculation error

**Daily Practice Session Progress (Week 2):**
- Completes 3-4 practice problems per day (sometimes stops early)
- Average articulation level: Level 0.2 (minimal)
- Average accuracy: 42% → 48% (minimal improvement)
- Time per problem: 5-6 minutes (rushed but struggling)
- Progress tracking shows minimal improvement

**Week 2 - Day 5 - Gaming Attempt:**

**Pathway Radar Warm-up:**
> "I'm just going to click randomly. This is taking too long."

**Engagement:**
- Completes all 10 identification questions by random clicking
- Accuracy: 2/10 (20%)
- Time: 3 minutes (rushed)

**Critical Finding - Gaming:**
- Dylan attempts to game the pathway radar by random clicking
- System **does not detect** this pattern
- No intervention or consequence for gaming behavior

**Week 3 - Geometry - Composite Shapes Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 3/10 (30%)
- Time: 4 minutes 45 seconds (random clicking)

**Daily Practice Session:**

**Forced Articulation:**
```
Pathway Type: [Dylan selects "Angles" (incorrect)]
Equation Shadow: [Empty]
```

**Critical Finding - Consistent Skipping:**
- Dylan consistently skips equation shadow field
- System never enforces completion
- Learning impact is severely reduced

**Week 4 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 4/10 (40%)
- Time: 4 minutes

**Daily Practice Session:**
- Forced articulation quality: Level 0.1 (minimal)
- Accuracy: 45%
- Time per problem: 4-5 minutes

**Critical Findings (Week 2-4):**
- 🔴 **Critical Bug:** No validation on forced articulation fields (allows empty submissions)
- 🔴 **Critical Issue:** No detection or prevention of gaming behavior (random clicking on pathway radar)
- 🔴 **Pedagogical Issue:** Feedback is too verbose and complex for struggling students
- 🔴 **Engagement Issue:** Dylan becomes highly frustrated and disengaged after Week 1
- 🔴 **Scaffolding Issue:** No step-by-step guidance for students who get stuck
- 🔴 **Language Issue:** Vocabulary in problems is above Dylan's reading level
- 🔴 **Visual Issue:** Geometry diagrams are too complex for Dylan's understanding
- ⚠️ **UI Friction:** On Day 3, Dylan accidentally clicked "Skip" instead of "Submit" and lost progress
- ⚠️ **Motivation:** No rewards or positive reinforcement for small improvements

---

### Week 5 - Transfer Test

**Dylan's Thoughts (Week 5):**
> "I'm just going to guess on most of these. This is too hard and I don't care anymore."

**Test Approach:**
- Random guessing on most problems
- Minimal or no working shown
- Rushes through test quickly
- Gives up on complex problems

**Performance:**
- Overall accuracy: 48% (19/40)
- Trained pathways accuracy: 52% (minimal improvement)
- Held-back pathways accuracy: 45% (no improvement)
- Time per problem: 0.8 minutes (very rushed, mostly guessing)

**Transfer Test Scan Upload:**
- OCR processes in 32 seconds
- OCR accuracy: ~55% (messy handwriting, many guesses)

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 52% (Target: ≥90%) ❌ (missed by 38%)
- **Articulation Level 2+ Rate (Trained):** 15% (Target: ≥90%) ❌ (missed by 75%)
- **Solving Improvement (Trained):** 12% improvement from baseline (Target: ≥80%) ❌ (missed by 68%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 52% (Target: ≥80%) ❌ (missed by 28%)
- **Transfer Accuracy (Held-Back Pathways):** 45% (Target: ≥50%) ❌ (missed by 5%)

**Dylan's Reaction:**
> "I told you I'm not good at math. This didn't help at all. I'm never doing this again."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ❌ **Success Criteria:** Failed ALL 5 success criteria
- ❌ **Transfer Learning:** No meaningful transfer achieved
- ❌ **Engagement:** Dylan is completely disengaged and demotivated
- 🔴 **Critical Issue:** MVP is not suitable for students like Dylan without significant modifications

---

### Critical Findings Summary for Dylan

**What Dylan Struggled With:**
1. EVERYTHING - the MVP is completely mismatched for Dylan's ability level
2. Forced articulation (never completes)
3. Feedback (too complex, doesn't understand)
4. Vocabulary (above reading level)
5. Geometry diagrams (too complex)
6. Gaming behavior (not detected or prevented)

**Bugs Found by Dylan:**
1. **Validation:** 🔴 CRITICAL - No validation on forced articulation fields
2. **Gaming Detection:** 🔴 CRITICAL - No detection of random clicking/gaming behavior
3. **UI Issue:** Accidental "Skip" click loses progress (Week 2, Day 3)

**Pedagogical Issues:**
1. Feedback is too verbose for struggling students
2. No step-by-step scaffolding for students who get stuck
3. No positive reinforcement or rewards for small improvements
4. Vocabulary and language are above Dylan's reading level
5. No adapted difficulty level for struggling students
6. No intervention for disengaged students

**Recommendations from Dylan's Scenario:**
1. **CRITICAL:** Add validation to force completion of articulation fields
2. **CRITICAL:** Implement gaming detection (random clicking patterns, time-per-question anomalies)
3. **CRITICAL:** Add step-by-step scaffolding for struggling students
4. **CRITICAL:** Simplify feedback language for struggling students
5. Add adaptive difficulty based on student performance
6. Implement positive reinforcement system (streaks, badges, rewards)
7. Add vocabulary tooltips or glossary for complex words
8. Provide simpler geometry diagrams for struggling students
9. Add "I need help" button that provides hints
10. Consider separate version for students significantly below grade level

---

## SCENARIO 5: Poor Student - Eve (Age 11)

### Persona Profile
- **Baseline Accuracy:** 50%
- **Engagement:** Low
- **Motivations:** Doesn't enjoy math, disengaged, just wants to be done
- **Behaviors:** Never does forced articulation (always skips), misinterprets questions frequently, very slow (takes excessive time)
- **Time Management:** Very slow, takes excessive time on simple problems
- **Learning Style:** Struggles significantly with all math concepts

---

### Week 1 - Baseline Test

**Eve's Thoughts (Week 1):**
> "I hate math. This is going to take forever. I don't even understand half these questions."

**Test Approach:**
- Reads questions very slowly (re-reads multiple times)
- Frequently misinterprets questions
- Writes very large, runs out of space
- Gets stuck on simple problems

**Performance:**
- Accuracy: 51% (20/40 correct)
- Time: 95 minutes (much slower than other students)
- Errors: 10 geometry problems, 5 word problems, 5 data interpretation problems
- Weakest pathways identified: All pathways show ~50% accuracy (no clear pattern)

**Critical Findings:**
- 🔴 **Critical Issue:** Vocabulary is significantly above Eve's reading level
- 🔴 **Critical Issue:** Eve frequently misinterprets question requirements
- 🔴 **Critical Issue:** Language complexity is inappropriate for Eve's ability
- 🔴 **Critical Issue:** Answer space is insufficient for Eve's large handwriting
- 🔴 **Critical Issue:** Test length is overwhelming for Eve (takes too long)

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 35 seconds
- Handwriting is very large, messy, and difficult to read
- OCR accuracy: ~45% (many misread numbers and letters)

**Gap Map Generation:**
- System identifies 3 weakest pathways (but all are similar at ~50%)
- Gap map visualization is overwhelming for Eve
- Shows low performance across all tracks

**Eve's Reaction:**
> "I did terrible. I knew I would. This is way too hard for me."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions? I don't know any of these. I'm just going to guess."

**Engagement:**
- Completes all 10 identification questions by guessing
- Accuracy: 3/10 (30%)
- Time: 5 minutes 15 seconds (very slow for guessing)
- Feedback: "Keep practicing! You'll improve with time."

**Daily Practice Session (Day 1):**

**Problem Display:**
> "I don't understand this at all. There's too much text."

**Forced Articulation:**
```
Pathway Type: [Eve selects "Word Problem" (incorrect - not a pathway type)]
Equation Shadow: [Eve types: "I don't know"]
```

**Critical Finding - Pathway Type Confusion:**
- Eve doesn't understand what "pathway type" means
- Selects generic "Word Problem" instead of specific pathway
- System should provide better pathway type definitions or examples

**Solving Attempt:**
- Eve attempts to solve but gets stuck
- Spends 8 minutes on one problem
- Guesses answer

**Triad Feedback:**
```
❌ Pathway Identification: INCORRECT (Red) - "Word Problem" is not a pathway type. This is a Before-After Change problem because it describes a two-stage change.
⚠️ Articulation: VAGUE (Level 0) - "I don't know" is not a valid equation shadow. Try to describe the problem structure in your own words.
❌ Solution: INCORRECT (Red) - Your answer is incorrect.
Overall: 🔴 Incorrect pathway ID, vague articulation, incorrect solution. Please review the pathway types and try again.
```

**Eve's Reaction:**
> "I don't understand what 'pathway type' even means. This is so confusing. I give up."

**Critical Finding - Terminology Issue:**
- Eve doesn't understand the term "pathway type"
- No tooltips, examples, or explanations provided
- Eve cannot engage with the system without understanding terminology

**Week 2 - Day 3 - Always Skips Forced Articulation:**

**Forced Articulation:**
```
Pathway Type: [Eve randomly selects a pathway]
Equation Shadow: [Empty - Eve always skips]
```

**Critical Finding - Pattern:**
- Eve NEVER completes the equation shadow field
- System **does not enforce completion**
- Learning is completely bypassed

**Week 2 - Day 5 - Time Out:**
> "I spent 15 minutes on this one problem and I still don't get it. I'm just going to guess."

**Critical Finding - Time Management:**
- Eve spends excessive time on single problems
- No time limit or timeout mechanism
- Eve becomes frustrated and disengaged

**Daily Practice Session Progress (Week 2):**
- Completes 2-3 practice problems per day (often gives up early)
- Average articulation level: Level 0.0 (never completes)
- Average accuracy: 38% → 40% (no meaningful improvement)
- Time per problem: 10-15 minutes (extremely slow)
- Progress tracking shows no improvement

**Week 3 - Geometry - Composite Shapes Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 2/10 (20%)
- Time: 6 minutes (very slow for guessing)

**Daily Practice Session:**

**Critical Finding - Reading Comprehension:**
> "The question says 'find the total area' but I don't understand what 'total area' means in this context. Does it mean add everything? Or subtract? I'm so confused."

**Eve's Struggle:**
- Eve lacks basic geometry vocabulary understanding
- No glossary or vocabulary support provided
- Cannot progress without understanding terms

**Week 4 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 3/10 (30%)
- Time: 5 minutes 30 seconds

**Daily Practice Session:**
- Forced articulation quality: Level 0.0 (never completes)
- Accuracy: 42%
- Time per problem: 8-12 minutes (extremely slow)

**Critical Findings (Week 2-4):**
- 🔴 **Critical Bug:** No validation on forced articulation fields
- 🔴 **Critical Issue:** Eve doesn't understand terminology ("pathway type", "equation shadow")
- 🔴 **Critical Issue:** No vocabulary support or glossary provided
- 🔴 **Critical Issue:** No time limits or timeout mechanism (Eve spends 15+ minutes on single problems)
- 🔴 **Critical Issue:** Reading comprehension significantly below question language level
- 🔴 **Engagement Issue:** Eve is completely disengaged and demotivated
- 🔴 **Pedagogical Issue:** No scaffolding for students who don't understand basics
- 🔴 **UI Issue:** No "I don't understand" or "I need help" option

---

### Week 5 - Transfer Test

**Eve's Thoughts (Week 5):**
> "I'm just going to guess on everything. I don't understand any of this. This is a waste of time."

**Test Approach:**
- Random guessing on all problems
- No working shown
- Rushes through (to be done with it)
- Gives up immediately

**Performance:**
- Overall accuracy: 42% (17/40)
- Trained pathways accuracy: 45% (no improvement)
- Held-back pathways accuracy: 40% (no improvement)
- Time per problem: 0.6 minutes (fast guessing)

**Transfer Test Scan Upload:**
- OCR processes in 36 seconds
- OCR accuracy: ~40% (mostly guesses, messy handwriting)

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 45% (Target: ≥90%) ❌
- **Articulation Level 2+ Rate (Trained):** 0% (Target: ≥90%) ❌
- **Solving Improvement (Trained):** 5% improvement from baseline (Target: ≥80%) ❌
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 45% (Target: ≥80%) ❌
- **Transfer Accuracy (Held-Back Pathways):** 40% (Target: ≥50%) ❌

**Eve's Reaction:**
> "I knew I would do terrible. This didn't help me at all. I hate math."

**Critical Findings (Week 5):**
- ❌ **Success Criteria:** Failed ALL 5 success criteria
- ❌ **Transfer Learning:** Zero transfer achieved
- ❌ **Engagement:** Eve is completely disengaged and negative toward math
- 🔴 **Critical Issue:** MVP is completely inappropriate for students like Eve

---

### Critical Findings Summary for Eve

**What Eve Struggled With:**
1. Terminology ("pathway type", "equation shadow") - doesn't understand
2. Reading comprehension - questions are above her level
3. Vocabulary - lacks basic math vocabulary understanding
4. Time management - spends excessive time on single problems
5. Forced articulation - never completes (doesn't understand what to write)
6. ALL aspects of the MVP - completely mismatched for her ability level

**Bugs Found by Eve:**
1. **Validation:** 🔴 CRITICAL - No validation on forced articulation fields
2. **Terminology:** 🔴 CRITICAL - No definitions or examples for "pathway type" and "equation shadow"
3. **Vocabulary Support:** 🔴 CRITICAL - No glossary or tooltips for difficult words
4. **Time Management:** 🔴 CRITICAL - No time limits or timeout mechanism
5. **Help System:** 🔴 CRITICAL - No "I need help" or "I don't understand" option

**Pedagogical Issues:**
1. Language complexity is significantly above Eve's reading level
2. No scaffolding for students who don't understand basics
3. No vocabulary support system
4. No adapted difficulty for struggling students
5. No intervention for students who are completely lost

**Recommendations from Eve's Scenario:**
1. **CRITICAL:** Add validation to force completion of articulation fields
2. **CRITICAL:** Add clear definitions and examples for all terminology
3. **CRITICAL:** Implement vocabulary support system (glossary, tooltips)
4. **CRITICAL:** Add time limits or timeout mechanism
5. **CRITICAL:** Implement "I need help" button that provides hints
6. Consider separate, simplified version for significantly below-grade-level students
7. Add reading level adaptation based on student performance
8. Provide step-by-step video tutorials for basic concepts
9. Implement adaptive difficulty that starts very simple for struggling students
10. Add positive reinforcement for ANY effort or improvement

---

## SCENARIO 6: Disengaged Student - Fay (Age 12)

### Persona Profile
- **Baseline Accuracy:** 40%
- **Engagement:** Very Low
- **Motivations:** No genuine effort, just clicks through, wants to be done
- **Behaviors:** Never reads feedback, writes gibberish or random numbers, skips pathway radar immediately, minimally engaged
- **Time Management:** Minimally engaged (fastest possible completion)
- **Learning Style:** N/A (not engaged in learning)

---

### Week 1 - Baseline Test

**Fay's Thoughts (Week 1):**
> "Whatever. I just want to get this over with. I don't care about math."

**Test Approach:**
- Rushes through all questions
- Random guessing or pattern recognition
- Minimal or no working
- Doesn't read questions carefully

**Performance:**
- Accuracy: 38% (15/40 correct)
- Time: 35 minutes (fastest of all students)
- Errors: Random pattern - no systematic weaknesses
- Weakest pathways identified: All pathways similar (~35-40% accuracy)

**Critical Findings:**
- 🔴 **Critical Issue:** No engagement detection or intervention
- 🔴 **Critical Issue:** Fay completed 40 questions in 35 minutes (averaged 52 seconds per question) - clear disengagement
- 🔴 **Critical Issue:** No quality check on baseline test completion

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 33 seconds
- Handwriting is mostly random numbers and gibberish
- OCR accuracy: ~35% (many nonsensical inputs)

**Gap Map Generation:**
- System identifies 3 weakest pathways
- Gap map visualization is meaningless to Fay (doesn't look at it)
- Shows random performance across all tracks

**Fay's Reaction:**
> "Finally done. That was a waste of time."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions? Whatever. I'll just click random buttons."

**Engagement:**
- Completes all 10 identification questions by random clicking
- Accuracy: 2/10 (20%)
- Time: 45 seconds (extremely fast)
- Feedback: "Keep practicing!" (Fay doesn't read it)

**Critical Finding - Gaming Behavior:**
- Fay completes 10 questions in 45 seconds (4.5 seconds per question)
- Random clicking pattern
- System **does not detect** this as gaming
- No intervention or consequence

**Daily Practice Session (Day 1):**

**Forced Articulation:**
```
Pathway Type: [Fay selects random pathway]
Equation Shadow: [Fay types: "asdfghjkl"]
```

**Critical Finding - Gibberish Input:**
- Fay types random characters in equation shadow field
- System **does not validate input quality**
- Proceeds to solving phase

**Solving Attempt:**
- Fay guesses answer randomly
- Time: 8 seconds total

**Triad Feedback:**
```
❌ Pathway Identification: INCORRECT (Red) - This is a Before-After Change problem.
⚠️ Articulation: INVALID (Level 0) - "asdfghjkl" is not a valid equation shadow. Please describe the problem structure.
❌ Solution: INCORRECT (Red) - Your answer is incorrect.
Overall: 🔴 Incorrect pathway ID, invalid articulation, incorrect solution.
```

**Fay's Reaction:**
> "Whatever. I don't care about the feedback."

**Critical Finding - Feedback Ignorance:**
- Fay never reads feedback
- System provides no incentive to read feedback
- Learning impact is zero

**Week 2 - Day 2 - Same Pattern:**

**Pathway Radar Warm-up:**
- Completes in 38 seconds
- Accuracy: 1/10 (10%)

**Daily Practice Session:**
- Types random gibberish in articulation field
- Guesses answer
- Never reads feedback

**Critical Finding - No Intervention:**
- System **does not detect** repeated gaming behavior
- No intervention to re-engage Fay
- No consequence for bypassing learning

**Week 2 - Day 3 - Pattern Detection Attempt:**

**Pathway Radar Warm-up:**
> "I'll just click the same button every time. Maybe that'll work."

**Engagement:**
- Clicks "Before-After Change" for all 10 questions
- Accuracy: 3/10 (30%)
- Time: 40 seconds

**Critical Finding - Pattern Gaming:**
- Fay uses same answer repeatedly
- System **does not detect** pattern repetition
- No intervention for pattern gaming

**Week 3 - Geometry - Composite Shapes Pathway**

**Pathway Radar Warm-up:**
- Completes in 42 seconds
- Accuracy: 2/10 (20%)

**Daily Practice Session:**
- Same pattern: gibberish articulation, random guess
- Time: 10 seconds per problem

**Week 4 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Completes in 40 seconds
- Accuracy: 1/10 (10%)

**Daily Practice Session:**
- Same pattern continues
- No engagement improvement

**Critical Findings (Week 2-4):**
- 🔴 **Critical Bug:** No gaming detection (random clicking, pattern repetition, sub-5s completion)
- 🔴 **Critical Bug:** No input quality validation (accepts gibberish in articulation field)
- 🔴 **Critical Issue:** No intervention for completely disengaged students
- 🔴 **Critical Issue:** No consequence system for bypassing learning
- 🔴 **Critical Issue:** No quality check on practice session completion
- 🔴 **Engagement Issue:** Fay shows zero engagement throughout 3 weeks
- 🔴 **Data Quality Issue:** Fay's data is completely meaningless for learning analytics

---

### Week 5 - Transfer Test

**Fay's Thoughts (Week 5):**
> "Last test. Finally. I'll just guess and get this over with."

**Test Approach:**
- Random guessing on all problems
- No working shown
- Completes as fast as possible
- Doesn't read any questions

**Performance:**
- Overall accuracy: 35% (14/40)
- Trained pathways accuracy: 38% (no improvement)
- Held-back pathways accuracy: 33% (no improvement)
- Time per problem: 0.5 minutes (30 seconds per question - fastest of all students)

**Transfer Test Scan Upload:**
- OCR processes in 34 seconds
- OCR accuracy: ~30% (mostly random numbers)

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 38% (Target: ≥90%) ❌
- **Articulation Level 2+ Rate (Trained):** 0% (Target: ≥90%) ❌
- **Solving Improvement (Trained):** 0% improvement from baseline (Target: ≥80%) ❌
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 38% (Target: ≥80%) ❌
- **Transfer Accuracy (Held-Back Pathways):** 33% (Target: ≥50%) ❌

**Fay's Reaction:**
> "Done. Finally. That was a complete waste of time. I learned nothing."

**Critical Findings (Week 5):**
- ❌ **Success Criteria:** Failed ALL 5 success criteria
- ❌ **Transfer Learning:** Zero transfer achieved
- ❌ **Engagement:** Fay showed zero engagement throughout entire MVP
- 🔴 **Critical Issue:** MVP cannot work with completely disengaged students without major redesign
- 🔴 **Data Quality Issue:** Fay's data contaminates learning analytics

---

### Critical Findings Summary for Fay

**What Fay Did:**
1. Random guessing on all questions
2. Gibberish input in articulation field
3. Pattern gaming (same answer repeatedly)
4. Never reads feedback
5. Sub-5s completion times (clear gaming)
6. Zero engagement throughout 5 weeks

**Bugs Found by Fay:**
1. **Gaming Detection:** 🔴 CRITICAL - No detection of random clicking, pattern repetition, or sub-5s completion
2. **Input Validation:** 🔴 CRITICAL - No quality validation on articulation field (accepts gibberish)
3. **Engagement Detection:** 🔴 CRITICAL - No intervention for completely disengaged students
4. **Data Quality:** 🔴 CRITICAL - No quality check on practice session data

**System Issues:**
1. No consequence system for bypassing learning
2. No engagement metrics or alerts
3. No parental/teacher notification system for disengaged students
4. No minimum quality threshold for practice data
5. No intervention or remediation for gaming behavior

**Recommendations from Fay's Scenario:**
1. **CRITICAL:** Implement gaming detection (random clicking, pattern repetition, anomalous timing)
2. **CRITICAL:** Add input quality validation for articulation field (reject gibberish)
3. **CRITICAL:** Implement engagement monitoring and alerts
4. **CRITICAL:** Add consequence system for gaming (e.g., forced restart, parental notification)
5. **CRITICAL:** Implement minimum quality threshold for practice data
6. **CRITICAL:** Add parental/teacher notification system for disengaged students
7. **CRITICAL:** Implement time-per-question minimum (e.g., must spend at least 30s per problem)
8. **CRITICAL:** Add quality scoring for articulation (reject Level 0 gibberish)
9. Consider requiring teacher/parent supervision for students showing disengagement patterns
10. Implement "practice quality score" that must meet minimum threshold to count

---

## SCENARIO 7: Confused Student - Grace (Age 12)

### Persona Profile
- **Baseline Accuracy:** 55%
- **Engagement:** Medium
- **Motivations:** Genuinely tries but confused, wants to learn but struggles
- **Behaviors:** Picks wrong pathways consistently, articulates incorrectly despite trying, gets frustrated with feedback
- **Time Management:** Average but inefficient (spends time but on wrong approaches)
- **Learning Style:** Struggles with both verbal and visual, needs clear step-by-step guidance

---

### Week 1 - Baseline Test

**Grace's Thoughts (Week 1):**
> "I'll try my best, but I'm not very good at math. I hope I can figure these out."

**Test Approach:**
- Reads questions carefully
- Tries to understand but frequently misidentifies pathway type
- Shows working but often on wrong approach
- Gets frustrated when stuck

**Performance:**
- Accuracy: 54% (22/40 correct)
- Time: 78 minutes (slower due to inefficient approaches)
- Errors: 8 word problems (wrong pathway), 5 geometry problems, 5 data interpretation problems
- Weakest pathways identified: Before-After Change (0/4 correct), Part-Whole with Comparison (1/4 correct), Data Interpretation - Red Herring (2/4 correct)

**Critical Findings:**
- ⚠️ **Pathway Confusion:** Grace consistently misidentifies pathway types
- ⚠️ **Visual-Linguistic Mismatch:** Grace interprets diagrams differently than intended
- ⚠️ **Feedback Need:** Grace needs more guidance on how to identify pathways
- ⚠️ **Example Need:** Grace would benefit from more worked examples

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 29 seconds
- Handwriting is neat but working shows wrong approaches
- OCR accuracy: ~70% (good)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization shows Grace's confusion (Before-After Change at 0%)
- Grace is confused by gap map (doesn't understand what "Before-After Change" means)

**Grace's Reaction:**
> "I got 0% on Before-After Change? I don't even know what that means. This is confusing."

**Critical Finding - Terminology Confusion:**
- Grace doesn't understand pathway type names
- No definitions or examples provided
- Cannot use gap map effectively

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions about pathway types? I don't know what half these names mean. I'll just guess based on what I think."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 3/10 (30%)
- Time: 5 minutes
- Feedback: "Keep practicing! You'll learn to recognize the patterns."

**Grace's Reaction:**
> "The feedback says 'keep practicing' but it doesn't tell me what I got wrong or why. I'm still confused."

**Critical Finding - Feedback Clarity:**
- Grace needs more specific feedback on why pathway ID was incorrect
- Current feedback doesn't explain the pattern recognition logic

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Okay, let me read this carefully. The shop sold 3/5 of its pens, then 1/4 of the remainder. Is this a Part-Whole problem? Or maybe Comparison? I'm not sure."

**Forced Articulation:**
```
Pathway Type: Part-Whole with Comparison [Grace's guess - incorrect]
Equation Shadow: There are pens and some are sold. I need to find how many at first.
```

**Solving Attempt:**
- Grace tries to solve using Part-Whole approach (wrong)
- Gets confused and stuck
- Spends 7 minutes on this problem
- Guesses answer

**Triad Feedback:**
```
❌ Pathway Identification: INCORRECT (Red) - This is not a Part-Whole with Comparison problem. It is a Before-After Change problem because it describes two sequential changes: first 3/5 sold, then 1/4 of remainder sold.
⚠️ Articulation: VAGUE (Level 0) - Your equation shadow doesn't specify the pathway structure. Try to describe the two-stage change and the backward solving approach.
❌ Solution: INCORRECT (Red) - Because you used the wrong pathway, your answer is incorrect.
Overall: 🔴 Incorrect pathway ID, vague articulation, incorrect solution.
```

**Grace's Reaction:**
> "Okay, so it's Before-After Change because there are two changes. But I still don't understand what that means. What makes it different from Part-Whole? The feedback doesn't explain the difference."

**Critical Finding - Comparison Need:**
- Grace needs side-by-side comparison of similar pathways
- Current feedback explains what it IS but not why it's NOT something else
- Grace is confused by pathway boundaries

**Week 2 - Day 2 - Continued Confusion:**

**Forced Articulation:**
```
Pathway Type: Before-After Change [Grace's guess based on Day 1 - correct!]
Equation Shadow: There are two changes. First some sold, then some more sold.
```

**Grace's Thought Process:**
> "I guessed Before-After Change because the feedback said there are two changes. But I'm still not sure this is right. Let me try to solve it."

**Solving Attempt:**
- Grace attempts to solve using backward approach
- Makes calculation error
- Gets wrong answer

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green) - Good job! You correctly identified this as a Before-After Change problem.
⚠️ Articulation: ADEQUATE (Level 1) - You mentioned two changes, which is good. Try to be more specific: what fractions? What's the remainder?
❌ Solution: INCORRECT (Red) - Your pathway ID is correct, but your solution has a calculation error. Check your fraction math.
Overall: 🟡 Correct pathway ID, but articulation needs improvement and solution is incorrect.
```

**Grace's Reaction:**
> "Okay, I got the pathway right! That's progress. But I still made a calculation error. The feedback says 'check your fraction math' but doesn't tell me where I went wrong."

**Critical Finding - Step-by-Step Need:**
- Grace needs step-by-step guidance on solving errors
- Current feedback identifies error but doesn't show correct steps
- Grace doesn't know how to fix the calculation

**Daily Practice Session Progress (Week 2):**
- Completes 4-5 practice problems per day
- Average articulation level: Level 1.0 → Level 1.2 (minimal improvement)
- Average accuracy: 46% → 52% (minimal improvement)
- Time per problem: 6-8 minutes (inefficient)
- Progress tracking shows minimal improvement

**Week 2 - Day 4 - Frustration:**
> "I've been doing this for a week and I'm still confused. I got the pathway right on some problems, but I keep making calculation errors. The feedback doesn't help me understand where I'm going wrong."

**Critical Finding - Frustration Point:**
- Grace is genuinely trying but not improving much
- Feedback is not detailed enough for her learning needs
- Grace needs more scaffolding and examples

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 4/10 (40%)
- Time: 5 minutes 30 seconds

**Daily Practice Session:**
- Still confused about pathway boundaries
- Confuses Part-Whole with Comparison vs. Before-After Change
- Accuracy: 50%

**Critical Finding - Cross-Thread Collision:**
- Grace is experiencing cross-thread collision (confusing similar pathways)
- No collision detection or targeted intervention provided yet
- Grace continues to be confused

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 4/10 (40%)
- Time: 5 minutes 15 seconds

**Daily Practice Session:**
- Confused about what "red herring" means
- Doesn't understand how to identify distractor data
- Accuracy: 48%

**Critical Finding - Vocabulary Confusion:**
- Grace doesn't understand term "red herring"
- No explanation or examples provided
- Cannot engage with this pathway effectively

**Critical Findings (Week 2-4):**
- ⚠️ **Feedback Clarity:** Grace needs more detailed, step-by-step feedback
- ⚠️ **Terminology:** Grace doesn't understand pathway type names
- ⚠️ **Cross-Thread Collision:** Grace confuses similar pathways, no targeted intervention
- ⚠️ **Scaffolding:** Grace needs more worked examples and step-by-step guidance
- ⚠️ **Comparison:** Grace needs side-by-side comparison of similar pathways
- ⚠️ **Vocabulary:** Grace doesn't understand terms like "red herring"
- ⚠️ **Progress:** Minimal improvement despite genuine effort
- ⚠️ **Frustration:** Grace becomes frustrated with lack of progress

---

### Week 5 - Transfer Test

**Grace's Thoughts (Week 5):**
> "I've been practicing for three weeks but I'm still not sure if I understand the pathways. Let me just do my best."

**Test Approach:**
- Reads questions carefully
- Still unsure about pathway identification
- Tries to apply what she learned but still confused
- Time: 75 minutes (similar to baseline)

**Performance:**
- Overall accuracy: 58% (23/40)
- Trained pathways accuracy: 62% (some improvement)
- Held-back pathways accuracy: 55% (minimal improvement)
- Time per problem: 1.9 minutes (no speed improvement)

**Transfer Test Scan Upload:**
- OCR processes in 29 seconds
- OCR accuracy: ~70%

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 62% (Target: ≥90%) ❌ (missed by 28%)
- **Articulation Level 2+ Rate (Trained):** 35% (Target: ≥90%) ❌ (missed by 55%)
- **Solving Improvement (Trained):** 18% improvement from baseline (Target: ≥80%) ❌ (missed by 62%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 62% (Target: ≥80%) ❌ (missed by 18%)
- **Transfer Accuracy (Held-Back Pathways):** 55% (Target: ≥50%) ✅ (barely met)

**Grace's Reaction:**
> "I improved a little bit, but not much. I'm still confused about the pathways. The feedback didn't really help me understand what I was doing wrong. I wish there were more examples."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ❌ **Success Criteria:** Failed 4 out of 5 success criteria
- ⚠️ **Transfer Learning:** Some transfer achieved (62% on trained pathways)
- ⚠️ **Frustration:** Grace is frustrated with lack of meaningful progress

---

### Critical Findings Summary for Grace

**What Grace Struggled With:**
1. Pathway type identification (consistently wrong)
2. Understanding pathway terminology and boundaries
3. Step-by-step solving (needs more guidance)
4. Cross-thread collision (confuses similar pathways)
5. Feedback clarity (needs more detailed, specific guidance)
6. Vocabulary (doesn't understand terms like "red herring")

**What Grace Needs:**
1. More detailed, step-by-step feedback
2. Worked examples for each pathway
3. Side-by-side comparison of similar pathways
4. Clear definitions of terminology
5. Vocabulary support (glossary, tooltips)
6. Scaffolding for students who are genuinely trying but confused
7. Cross-thread collision detection and intervention

**Bugs/Issues Found by Grace:**
1. **Feedback Clarity:** ⚠️ MEDIUM - Feedback not detailed enough for confused students
2. **Terminology:** ⚠️ MEDIUM - No definitions or examples for pathway types
3. **Scaffolding:** ⚠️ MEDIUM - No worked examples or step-by-step guidance
4. **Cross-Thread Collision:** ⚠️ MEDIUM - No detection or intervention for pathway confusion
5. **Vocabulary:** ⚠️ MEDIUM - No explanation of terms like "red herring"

**Pedagogical Issues:**
1. Feedback is too generic for confused students
2. No comparison of similar pathways to help distinguish them
3. No step-by-step guidance for solving errors
4. No worked examples to illustrate correct approaches
5. Terminology is not defined or explained

**Recommendations from Grace's Scenario:**
1. Add detailed, step-by-step feedback for incorrect solutions
2. Provide worked examples for each pathway type
3. Implement side-by-side comparison of similar pathways
4. Add clear definitions and examples for all terminology
5. Implement cross-thread collision detection and targeted intervention
6. Add vocabulary support system (glossary, tooltips)
7. Provide step-by-step video or animated examples
8. Add "show me how" button that walks through solution
9. Implement pathway boundary explanation with examples
10. Add adaptive difficulty that provides more scaffolding for confused students

---

## SCENARIO 8: Anxious Student - Henry (Age 12)

### Persona Profile
- **Baseline Accuracy:** 60%
- **Engagement:** Medium
- **Motivations:** High anxiety, second-guesses self, wants to get everything right
- **Behaviors:** Changes answers multiple times, over-articulates (writes paragraphs instead of concise equation shadow)
- **Time Management:** Above average (overthinking)
- **Learning Style:** Verbal learner, needs confidence building

---

### Week 1 - Baseline Test

**Henry's Thoughts (Week 1):**
> "I really hope I do well on this. I'm so nervous. What if I get everything wrong? Let me take my time and check everything twice."

**Test Approach:**
- Reads each question multiple times
- Changes answers frequently (second-guessing)
- Shows extensive working but often overthinks
- Checks work multiple times

**Performance:**
- Accuracy: 61% (24/40 correct)
- Time: 92 minutes (much slower than other students)
- Errors: 8 word problems (overthinking), 5 geometry problems (second-guessed correct answers), 3 data interpretation problems
- Weakest pathways identified: Before-After Change (1/4 correct), Part-Whole with Comparison (2/4 correct), Data Interpretation - Red Herring (2/4 correct)

**Critical Findings:**
- ⚠️ **Anxiety Impact:** Henry's anxiety causes him to second-guess correct answers
- ⚠️ **Time Pressure:** Henry runs out of time on last few questions due to overthinking
- ⚠️ **Confidence:** Henry lacks confidence in his answers
- ⚠️ **Work Space:** Henry needs more space for extensive working

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 31 seconds
- Handwriting is very neat but extensive working causes OCR confusion
- OCR accuracy: ~65% (too much text)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization shows Henry's anxiety-driven errors
- Henry is worried about his low scores

**Henry's Reaction:**
> "I only got 61%? I worked so hard and checked everything. I must be terrible at math. I'm so worried about the training."

**Critical Finding - Anxiety Amplification:**
- Gap map shows low scores, which increases Henry's anxiety
- No reassurance or confidence-building in gap map display
- Henry enters training with high anxiety

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "Okay, 10 questions in 5 minutes. That's only 30 seconds per question. I'm so nervous. What if I get them wrong?"

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 6/10 (60%)
- Time: 4 minutes 30 seconds (rushed due to anxiety)
- Feedback: "Good effort! You recognized 6 out of 10 correctly. Keep practicing!"

**Henry's Reaction:**
> "I only got 6 out of 10? That's not good enough. I need to do better. I'm so worried I'll fail."

**Critical Finding - Anxiety Impact:**
- Henry interprets 60% as failure (not recognition of progress)
- No confidence-building in feedback
- Anxiety increases with each practice session

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Let me read this very carefully. Okay, the shop sold 3/5 of its pens, then 1/4 of the remainder. Is this Before-After Change? Or maybe something else? I'm not sure."

**Forced Articulation:**
```
Pathway Type: [Henry hesitates, changes mind twice, finally selects "Before-After Change"]
Equation Shadow: The shop had some pens, then it sold 3/5 of them, which means 2/5 remained. Then it sold 1/4 of the remainder, so 3/4 of the remainder remained. The remainder after the first sale is 2/5 of the original. Then after the second sale, 3/4 of that 2/5 remained. So 3/4 of 2/5 is 6/20 or 3/10. And this equals 150 pens. So the original must be 150 divided by 3/10, which is 150 times 10/3, which is 500 pens. Wait, let me double-check this. Actually, I think I made an error. Let me try again. The remainder after the first sale is 2/5, then after the second sale, 3/4 of that remainder remains, so 3/4 of 2/5 = 6/20 = 3/10. And 3/10 of the original = 150, so original = 150 / (3/10) = 150 * (10/3) = 500. Hmm, I think that's right, but I'm not sure. Let me think about this differently...
```

**Critical Finding - Over-Articulation:**
- Henry writes 10+ sentences instead of concise equation shadow
- The entire solution is embedded in the articulation field
- Henry is essentially solving the problem twice (once in articulation, once in solving phase)

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green) - Good job! You correctly identified this as a Before-After Change problem.
⚠️ Articulation: OVER-DETAILED (Level 2) - Your equation shadow is very detailed and includes your full solution. While the logic is correct, try to be more concise. An equation shadow should describe the problem structure, not include the full solution.
✅ Solution: CORRECT (Green) - Your answer is correct: 250 pens.
Overall: 🟡 Correct pathway ID and solution, but articulation is too detailed.
```

**Critical Finding - Conflicting Feedback:**
- Henry got the answer correct (250) but his articulation says 500
- System flagged solution as correct but Henry has conflicting calculation in articulation
- Henry is confused by this discrepancy

**Henry's Reaction:**
> "The feedback says my solution is correct (250), but my articulation says 500. Did I make a mistake? Which one is right? I'm so confused. I don't know if I actually got this right or wrong."

**Critical Finding - Validation Bug:**
1. **Calculation Discrepancy:** Henry's articulation contains a calculation (500) that doesn't match his solution (250)
2. **System Bug:** Solution is marked correct despite articulation error
3. **Confusion:** Henry is confused by conflicting feedback

**Daily Practice Session Progress (Week 2):**
- Completes 4-5 practice problems per day
- Average articulation level: Level 2.5 (over-detailed)
- Average accuracy: 68% → 74% (some improvement)
- Time per problem: 8-12 minutes (very slow due to overthinking)
- Progress tracking shows improvement but Henry is still anxious

**Week 2 - Day 3 - Anxiety Peak:**
> "I changed my answer three times on this problem. I don't know which one is right. I'm so stressed. I think I got it wrong. I should just give up."

**Critical Finding - Anxiety Escalation:**
- Henry's anxiety increases throughout the week
- No confidence-building or reassurance provided
- Henry considers giving up

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 7/10 (70%)
- Time: 4 minutes 45 seconds

**Daily Practice Session:**
- Still over-articulating (paragraphs instead of concise shadows)
- Accuracy: 72%
- Time per problem: 9-11 minutes

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 6/10 (60%)
- Time: 5 minutes

**Daily Practice Session:**
- Over-articulation continues
- Accuracy: 70%
- Time per problem: 8-10 minutes

**Critical Findings (Week 2-4):**
- ⚠️ **Over-Articulation:** Henry writes paragraphs instead of concise equation shadows
- 🔴 **Validation Bug:** System doesn't detect calculation discrepancies between articulation and solution
- ⚠️ **Feedback Clarity:** Conflicting feedback confuses Henry
- 🔴 **Confidence Building:** No reassurance or positive reinforcement in system
- ⚠️ **Anxiety Management:** No tools to help manage anxiety
- ⚠️ **Time Management:** No time warnings or pacing guidance
- ⚠️ **Answer Changes:** Henry frequently changes answers, no way to track or review changes

---

### Week 5 - Transfer Test

**Henry's Thoughts (Week 5):**
> "I'm so nervous about this test. What if I do worse than the baseline? I've been practicing but I'm still not confident. Let me just take my time and check everything."

**Test Approach:**
- Reads questions extremely carefully
- Changes answers frequently
- Shows extensive working
- Runs out of time on last 3 questions

**Performance:**
- Overall accuracy: 67% (27/40)
- Trained pathways accuracy: 72% (improvement but below target)
- Held-back pathways accuracy: 63% (some improvement)
- Time per problem: 2.3 minutes (slower due to overthinking)

**Transfer Test Scan Upload:**
- OCR processes in 31 seconds
- OCR accuracy: ~60% (too much text in working)

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 72% (Target: ≥90%) ❌ (missed by 18%)
- **Articulation Level 2+ Rate (Trained):** 85% (Target: ≥90%) ⚠️ (missed by 5%)
- **Solving Improvement (Trained):** 28% improvement from baseline (Target: ≥80%) ❌ (missed by 52%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 72% (Target: ≥80%) ❌ (missed by 8%)
- **Transfer Accuracy (Held-Back Pathways):** 63% (Target: ≥50%) ✅

**Henry's Reaction:**
> "I improved a little bit, but I'm still not confident. I changed my answers so many times. I don't know if I got them right. I'm still so anxious about math."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ❌ **Success Criteria:** Failed 4 out of 5 success criteria
- ⚠️ **Transfer Learning:** Some transfer achieved (72% on trained pathways)
- 🔴 **Anxiety Issue:** Henry remains highly anxious throughout entire MVP
- 🔴 **Confidence Issue:** No confidence building in system

---

### Critical Findings Summary for Henry

**What Henry Struggled With:**
1. Over-articulation (writes paragraphs instead of concise shadows)
2. Anxiety (second-guesses, changes answers frequently)
3. Confidence (lacks confidence in answers)
4. Time management (overthinks, runs out of time)
5. Conflicting feedback (system doesn't catch calculation discrepancies)

**What Henry Needs:**
1. Guidance on concise articulation (character limit or template)
2. Confidence-building feedback and reassurance
3. Anxiety management tools or relaxation prompts
4. Time management guidance or pacing assistance
5. Validation of calculation consistency between articulation and solution
6. Positive reinforcement for progress (even small improvements)

**Bugs Found by Henry:**
1. **Validation:** 🔴 CRITICAL - System doesn't detect calculation discrepancies between articulation and solution (Week 2, Day 1)
2. **Conflicting Feedback:** ⚠️ MEDIUM - Confusing feedback when articulation and solution conflict

**System Issues:**
1. No confidence-building or reassurance in feedback
2. No character limit or guidance for articulation field
3. No time warnings or pacing guidance
4. No anxiety management tools
5. No tracking of answer changes

**Recommendations from Henry's Scenario:**
1. **CRITICAL:** Add validation to detect calculation discrepancies between articulation and solution
2. Add character limit or guidance for equation shadow field (e.g., "Keep it concise: 1-2 sentences")
3. Implement confidence-building language in feedback (e.g., "Great progress!", "You're improving!")
4. Add time warnings during practice sessions (e.g., "You've spent 10 minutes on this problem")
5. Implement "I'm stuck" or "I need help" button that provides hints
6. Add relaxation prompts for anxious students (e.g., "Take a deep breath")
7. Track answer changes and provide insight (e.g., "You changed your answer 3 times - trust your first instinct")
8. Provide positive reinforcement for small improvements
9. Add confidence score or meter that shows improvement over time
10. Consider adaptive pacing that provides more time for anxious students

---

## SCENARIO 9: Picky Student - Ivy (Age 12)

### Persona Profile
- **Baseline Accuracy:** 70%
- **Engagement:** High
- **Motivations:** Good at math but critical of issues, notices visual inconsistencies, questions system design
- **Behaviors:** Looks for visual inconsistencies between diagrams and questions, notes when diagrams don't align with question text, gets confused by minor UI inconsistencies
- **Time Management:** Slightly below average (due to investigation)
- **Learning Style:** Visual learner with high attention to detail

---

### Week 1 - Baseline Test

**Ivy's Thoughts (Week 1):**
> "Let me work through this test carefully. I want to make sure everything makes sense."

**Test Approach:**
- Reads questions and examines diagrams carefully
- Notes any inconsistencies or issues
- Shows clear working
- Takes time to verify everything

**Performance:**
- Accuracy: 72% (29/40 correct)
- Time: 73 minutes (slightly slower due to investigation)
- Errors: 6 geometry problems (noted visual inconsistencies), 3 word problems, 2 data interpretation problems
- Weakest pathways identified: Geometry - Area & Perimeter (2/4 correct), Geometry - Angles (2/4 correct), Data Interpretation - Red Herring (3/4 correct)

**Critical Findings:**
- 🔴 **Visual Inconsistency 1:** Question 12 shows a bar model with bars representing 150, 200, 250 units, but the question text says "the bars represent 100, 150, 200 units" - Ivy notes this mismatch
- 🔴 **Visual Inconsistency 2:** Question 17 shows a triangle with angles labeled 60°, 70°, x°, but the visual representation of the 70° angle looks larger than the 60° angle - Ivy notes this proportional issue
- 🔴 **Visual Inconsistency 3:** Question 23 shows a pie chart with sector labeled "¼" but visually it appears to be larger than ¼ - Ivy notes this
- 🔴 **Visual Inconsistency 4:** Question 28 shows a bar graph where the y-axis is labeled "Sales (in hundreds)" but the actual values appear to be in thousands - Ivy notes this scale discrepancy
- ⚠️ **Typo:** Question 15 has typo "remainging" → "remaining"
- ⚠️ **Layout:** Page 5 has a page break that separates question text from diagram (confusing)
- ⚠️ **Font Inconsistency:** Question 8 uses different font than other questions

**Ivy's Notes:**
> "Question 12: The bars show 150, 200, 250 visually but text says 100, 150, 200. Which is correct? This is confusing.
> Question 17: The 70° angle looks bigger than the 60° angle, but that can't be right if they're on a line. The diagram isn't proportional.
> Question 23: The pie chart sector labeled '¼' looks like it's more than ¼. The visual doesn't match the label.
> Question 28: The y-axis says 'in hundreds' but the values (1500, 2000, 2500) appear to be in thousands. Scale is wrong."

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 28 seconds
- Handwriting is very neat with notes in margin about inconsistencies
- OCR accuracy: ~85% (excellent)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization is clear
- Ivy notes that the gap map radar chart has one sector that doesn't sum to 100% (UI bug)

**Ivy's Reaction:**
> "The gap map is helpful, but I noticed the radar chart sectors don't sum to 100%. One sector is off by about 2%. That's a rendering bug."

---

### Week 2-4 - Training Intervention

**Week 2 - Geometry - Angles Pathway**

**Pathway Radar Warm-up (Day 1):**
> "This warm-up is a good idea. Let me see if I can identify the pathway types correctly."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 8/10 (80%)
- Time: 4 minutes 45 seconds

**Critical Finding - Pathway Radar UI:**
> "The timer shows 00:00 for 3 seconds after I submit before it resets to the next question. That's a bug. Also, the progress bar jumps from 0% to 10% instantly without animation."

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Let me look at this geometry problem carefully."

**Critical Finding - Visual Inconsistency 5:**
- **Question:** Geometry problem showing supplementary angles
- **Diagram:** Shows two rays OA and OB forming a straight line, with ray OC extending upward. Angle AOC is labeled 65°.
- **Issue:** The diagram shows angle AOC as approximately 70-75° visually, not 65°. The visual representation is not proportional.
- **Ivy's Note:** "The 65° angle looks more like 75°. The diagram isn't drawn to scale. This is misleading."

**Forced Articulation:**
```
Pathway Type: Geometry - Angles - Supplementary Angles
Equation Shadow: Two angles on a straight line add up to 180°, so x = 180° - 65° = 115°.
```

**Ivy's Critical Thinking:**
> "The diagram shows angle AOC as larger than 65°, but I'll trust the label and calculate 180° - 65° = 115°. But I'm concerned that students who rely on visual estimation might get confused."

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
✅ Articulation: EXCELLENT (Level 3) - Perfect! You clearly explained the supplementary angle relationship and the calculation.
✅ Solution: CORRECT (Green) - Your answer is correct: 115°.
Overall: 🟢 Perfect work!
```

**Ivy's Note:**
> "The feedback is good, but the model articulation for comparison is truncated at the end. It says 'Angles on a straight line are...' and then cuts off with '...'. I'd like to see the full text."

**Critical Finding - Feedback Truncation:**
- Model articulation is truncated in feedback display
- No way to expand or see full text
- Ivy finds this frustrating

**Week 2 - Day 3 - Another Visual Inconsistency:**

**Critical Finding - Visual Inconsistency 6:**
- **Question:** Bar model word problem
- **Diagram:** Shows 3 bars representing original, after first change, after second change
- **Question Text:** Says "after the first change, 3/5 remained" but the diagram shows the first bar (after change) as 3/5 of the original
- **Issue:** Text says "remained" implying 3/5 is what's left, but diagram shows first bar as 3/5 (which would be "sold")
- **Ivy's Note:** "The question text says '3/5 remained' but the diagram shows the first bar as 3/5 of the original. This is inconsistent. If 3/5 remained, the first bar should show 2/5 (sold), not 3/5."

**Ivy's Reaction:**
> "I'm not sure which interpretation is correct - the text or the diagram. This is confusing. I'll go with the text, but the diagram should match."

**Week 2 - Day 5 - UI Inconsistency:**

**Critical Finding - UI Inconsistency 1:**
> "On Day 5, the 'Submit' button text changed from 'Submit' to 'Submit Answer' inconsistently. Sometimes it says 'Submit', sometimes 'Submit Answer'. This is a UI inconsistency."

**Week 3 - Geometry - Area & Perimeter Pathway**

**Critical Finding - Visual Inconsistency 7:**
- **Question:** Composite shape area problem
- **Diagram:** Shows a square with side length 8 cm and a quarter-circle attached to one side
- **Question Text:** Says "Find the total area of the composite shape. The square has side length 8 cm. The quarter-circle has radius 8 cm."
- **Issue:** The diagram shows the quarter-circle attached to the middle of the square side, but quarter-circles are typically attached to corners. If attached to the middle, it's actually a half-circle, not quarter-circle.
- **Ivy's Note:** "The diagram shows what looks like a half-circle attached to the middle of the square side, but the text says 'quarter-circle'. If it's attached to the middle, it would be a half-circle (πr²/2). If it's a quarter-circle, it should be attached to a corner. The diagram and text don't match."

**Critical Finding - Visual Inconsistency 8:**
- **Question:** Same composite shape problem
- **Diagram:** The quarter-circle (or half-circle) radius appears to be approximately 4 cm visually, not 8 cm
- **Ivy's Note:** "The radius in the diagram looks like it's 4 cm (half the side length), but the text says 8 cm. The diagram isn't proportional to the text values."

**Week 4 - Data Interpretation - Red Herring Pathway**

**Critical Finding - Visual Inconsistency 9:**
- **Question:** Bar graph comparison problem
- **Diagram:** Shows 5 bars with heights representing values 120, 150, 180, 200, 170
- **Question Text:** Asks about Product A (value 120) and Product C (value 180)
- **Issue:** The bar labels are inconsistent - the x-axis labels show "A, B, C, D, E" but the question asks about "Product A, Product C, Product E"
- **Ivy's Note:** "The x-axis labels are A, B, C, D, E, but the question asks about Product A, Product C, Product E. Are 'A' and 'Product A' the same thing? This is inconsistent terminology."

**Critical Findings (Week 2-4):**
- 🔴 **Visual Inconsistencies:** 9 visual inconsistencies found by Ivy (diagrams don't match question text)
- 🔴 **Proportional Rendering Issues:** Multiple diagrams not drawn to scale (violates proportional rendering requirement)
- ⚠️ **UI Inconsistencies:** Button text inconsistency, timer display bug
- ⚠️ **Feedback Truncation:** Model articulation truncated in feedback display
- ✅ **Question Clarity:** Generally good except for visual inconsistencies
- ✅ **Question Variety:** Good variety within pathways
- ✅ **Difficulty Progression:** Appropriate

---

### Week 5 - Transfer Test

**Ivy's Thoughts (Week 5):**
> "Let me see if there are any visual inconsistencies on this transfer test. I'll be careful to note any issues."

**Test Approach:**
- Works through questions carefully
- Notes any visual inconsistencies
- Shows clear working
- Time: 70 minutes

**Performance:**
- Overall accuracy: 75% (30/40)
- Trained pathways accuracy: 80% (improvement)
- Held-back pathways accuracy: 70% (improvement)
- Time per problem: 1.75 minutes (faster than baseline)

**Transfer Test Scan Upload:**
- OCR processes in 27 seconds
- OCR accuracy: ~85%

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 80% (Target: ≥90%) ❌ (missed by 10%)
- **Articulation Level 2+ Rate (Trained):** 88% (Target: ≥90%) ⚠️ (missed by 2%)
- **Solving Improvement (Trained):** 38% improvement from baseline (Target: ≥80%) ❌ (missed by 42%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 80% (Target: ≥80%) ✅ (met)
- **Transfer Accuracy (Held-Back Pathways):** 70% (Target: ≥50%) ✅

**Ivy's Notes on Transfer Test:**
> "I found 2 more visual inconsistencies on the transfer test. Question 6 shows a bar model where the text says '3 bars' but the diagram shows 4 bars. Question 19 shows a pie chart where the sectors don't sum to 100% (one sector is labeled ¼ but visually appears to be ⅓)."

**Ivy's Reaction:**
> "I improved, which is good. But I'm concerned about the number of visual inconsistencies I found. The diagrams need to be checked carefully against the question text. Students will get confused by these mismatches."

---

### Critical Findings Summary for Ivy

**Visual Inconsistencies Found by Ivy:**
1. **Question 12:** Bar values 150/200/250 vs text 100/150/200 (Week 1)
2. **Question 17:** Angle proportions not accurate (70° looks larger than 60°) (Week 1)
3. **Question 23:** Pie chart sector labeled ¼ but visually larger (Week 1)
4. **Question 28:** Y-axis scale says "hundreds" but values appear to be thousands (Week 1)
5. **Question 15:** Typo "remainging" → "remaining" (Week 1)
6. **Geometry Problem (Week 2, Day 1):** Angle labeled 65° but visually appears 70-75°
7. **Bar Model Problem (Week 2, Day 3):** Text says "3/5 remained" but diagram shows first bar as 3/5 (should be 2/5 if 3/5 remained)
8. **Composite Shape (Week 3):** Diagram shows half-circle attached to middle, but text says "quarter-circle"
9. **Composite Shape (Week 3):** Radius appears 4 cm in diagram but text says 8 cm (not proportional)
10. **Bar Graph (Week 4):** X-axis labels A/B/C/D/E vs question text Product A/C/E (terminology inconsistency)
11. **Transfer Test Q6:** Text says "3 bars" but diagram shows 4 bars
12. **Transfer Test Q19:** Pie chart sector labeled ¼ but visually appears ⅓ (sectors don't sum to 100%)

**UI Inconsistencies Found:**
1. Timer display shows 00:00 for 3 seconds after submit before resetting (Week 2, Day 1)
2. Progress bar jumps without animation (Week 2, Day 1)
3. Button text inconsistent: "Submit" vs "Submit Answer" (Week 2, Day 5)
4. Radar chart sectors don't sum to 100% (gap map display)
5. Model articulation truncated in feedback (no expand option)

**Proportional Rendering Violations:**
1. Question 17: Angles not proportional to labels
2. Geometry Week 2, Day 1: Angle labeled 65° but visually 70-75°
3. Composite Shape Week 3: Radius appears 4 cm vs text 8 cm (not proportional)
4. Transfer Test Q19: Pie chart sectors don't sum to 100%

**Recommendations from Ivy's Scenario:**
1. **CRITICAL:** Review ALL diagrams for visual-text consistency
2. **CRITICAL:** Implement proportional rendering validation (reject if deviation > 5%)
3. **CRITICAL:** Add diagram review checklist before Week 1 baseline test
4. Fix timer display to reset immediately upon submit
5. Add smooth animation to progress bar
6. Standardize button text across all pages
7. Fix radar chart rendering to ensure sectors sum to 100%
8. Implement expandable/collapsible model articulation display
9. Add visual-text consistency validation in problem creation workflow
10. Implement peer review or QA process for all diagrams before inclusion

---

## SCENARIO 10: Cheater/Gamer Student - Jack (Age 12)

### Persona Profile
- **Baseline Accuracy:** Varies (based on pattern detection, not understanding)
- **Engagement:** Low (gamer mentality)
- **Motivations:** Find shortcuts, game the system, minimize effort
- **Behaviors:** Tries to game pathway radar (same answers repeatedly), finds patterns in forced articulation (uses same template), doesn't actually solve problems, explores UI for shortcuts
- **Time Management:** Fast (maximizes shortcuts)
- **Learning Style:** N/A (not engaged in learning)

---

### Week 1 - Baseline Test

**Jack's Thoughts (Week 1):**
> "Let me see if I can find any patterns in this test. Maybe there's a shortcut to get the right answers without actually doing the work."

**Test Approach:**
- Scans test for patterns (e.g., answers follow A-B-C-D pattern, or certain pathway types appear in sequence)
- Guesses based on patterns, not understanding
- Minimal or no working
- Finishes quickly

**Performance:**
- Accuracy: 42% (17/40 correct) - by random guessing and pattern detection
- Time: 38 minutes (fast - pattern detection + guessing)
- Errors: Random pattern - no systematic approach
- Weakest pathways identified: All pathways similar (~40% accuracy)

**Critical Findings:**
- 🔴 **Gaming Behavior:** Jack attempts to detect answer patterns (none found)
- 🔴 **Pattern Detection:** Jack looks for shortcuts in question types and answer choices
- 🔴 **No Engagement:** Jack shows zero interest in understanding the material

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 34 seconds
- Handwriting is minimal, mostly random numbers
- OCR accuracy: ~40% (random inputs)

**Gap Map Generation:**
- System identifies 3 weakest pathways
- Jack doesn't look at the gap map (just wants to know which pathways to train)

**Jack's Reaction:**
> "So I need to work on Before-After Change, Part-Whole, and Data Interpretation. Let me see if I can find shortcuts for these."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "Let me see if I can find a pattern. Maybe if I always click 'Before-After Change', I'll get enough right."

**Engagement:**
- Clicks "Before-After Change" for all 10 questions
- Accuracy: 4/10 (40%)
- Time: 40 seconds (extremely fast)
- Feedback: "Keep practicing!" (Jack doesn't read it)

**Critical Finding - Gaming Pattern:**
- Jack uses same answer repeatedly
- System **does not detect** this pattern repetition
- No intervention for gaming behavior

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Let me see if there's a shortcut here. The problem mentions 'sold 3/5' and '1/4 of remainder'. I bet it's always Before-After Change. Let me try that."

**Forced Articulation:**
```
Pathway Type: Before-After Change [Jack's pattern]
Equation Shadow: [Jack types same template]: There are two changes. First some sold, then some more sold. Work backwards.
```

**Critical Finding - Template Reuse:**
- Jack uses the same equation shadow template for every problem
- System **does not detect** this template reuse
- No intervention for bypassing learning

**Solving Attempt:**
- Jack doesn't actually solve the problem
- Guesses based on pattern recognition
- Sometimes gets right by luck

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green) - Good job! You correctly identified this as a Before-After Change problem.
⚠️ Articulation: REPETITIVE (Level 1) - Your equation shadow is very similar to previous ones. Try to be more specific about this particular problem - what fractions? What quantities?
❌ Solution: INCORRECT (Red) - Your answer is incorrect. Check your calculations.
Overall: 🟡 Correct pathway ID, but articulation is repetitive and solution is incorrect.
```

**Jack's Reaction:**
> "I got the pathway right most of the time by always guessing 'Before-After Change'. That's 33% right there. The feedback says my articulation is repetitive, but I don't care. I'll just use this same template."

**Week 2 - Day 2 - Exploring UI for Shortcuts:**
> "Let me see if I can skip the forced articulation. Maybe if I just click submit without typing anything..."

**Critical Finding - Validation Bug:**
- Jack clicks submit with empty equation shadow field
- System **allows submission** (no validation)
- Jack proceeds to solving without articulation

**Jack's Discovery:**
> "Aha! I can skip the equation shadow field! That saves time. I'll just do that from now on."

**Critical Finding - Validation Failure:**
1. **No Validation:** System allows submission with empty articulation field
2. **Bypassed Learning:** Jack completely bypasses forced articulation requirement
3. **No Consequence:** No penalty or intervention for skipping

**Week 2 - Day 3 - Further Gaming:**
> "Let me see if I can find the correct answer from the feedback. Maybe if I submit wrong answers, the system will tell me the right one, and then I can resubmit."

**Critical Finding - Resubmission Exploit Attempt:**
- Jack submits wrong answer intentionally to see if correct answer is revealed
- System **does not show** correct answer in feedback (good!)
- Jack cannot exploit this

**Week 2 - Day 4 - Pathway Radar Pattern:**
> "I noticed that on the pathway radar, questions 1-3 are usually geometry, 4-6 are word problems, 7-10 are data interpretation. Let me test this pattern."

**Jack's Pattern:**
- Questions 1-3: Click "Angles"
- Questions 4-6: Click "Before-After Change"
- Questions 7-10: Click "Data Interpretation"

**Accuracy:**
- Questions 1-3: 2/3 correct (67%)
- Questions 4-6: 2/3 correct (67%)
- Questions 7-10: 2/3 correct (67%)
- Overall: 6/10 (60%)

**Critical Finding - Pattern Success:**
- Jack's pattern-based guessing achieves 60% accuracy
- Better than random guessing (40%)
- Still bypasses actual learning

**Week 2 - Day 5 - Minimum Viable Effort:**
> "I found that if I just guess 'Before-After Change' for word problems and skip the equation shadow, I can get about 50% right. That's good enough for me."

**Jack's Daily Practice Session Progress (Week 2):**
- Completes 5 practice problems per day (minimum required)
- Average articulation level: Level 0.0 (always skips or uses template)
- Average accuracy: 48% (pattern-based guessing)
- Time per problem: 2-3 minutes (very fast)
- Progress tracking shows minimal improvement

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Uses same pattern: geometry, word problems, data interpretation
- Accuracy: 6/10 (60%)

**Daily Practice Session:**
- Same pattern: guesses "Part-Whole" for word problems, skips equation shadow
- Accuracy: 50%
- Time per problem: 2-3 minutes

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Uses same pattern
- Accuracy: 5/10 (50%)

**Daily Practice Session:**
- Same pattern: guesses "Data Interpretation", skips equation shadow
- Accuracy: 52%
- Time per problem: 2-3 minutes

**Critical Findings (Week 2-4):**
- 🔴 **Gaming Detection:** No detection of pattern-based guessing (same answer repeatedly)
- 🔴 **Template Reuse Detection:** No detection of same equation shadow template used repeatedly
- 🔴 **Validation Failure:** No validation on empty equation shadow field (allows bypassing)
- 🔴 **Time Anomaly Detection:** No detection of sub-3s completion times on pathway radar
- 🔴 **Pattern Detection:** No detection of question-type-based guessing patterns
- 🔴 **Consequence System:** No penalties or interventions for gaming behavior
- 🔴 **Data Quality:** Jack's data is meaningless for learning analytics
- 🔴 **No Progress:** Jack shows zero genuine learning progress

---

### Week 5 - Transfer Test

**Jack's Thoughts (Week 5):**
> "Let me see if my patterns work on this test. I'll guess based on the question types and see if I can get a decent score without doing any actual work."

**Test Approach:**
- Uses patterns: word problems → guess Before-After/Part-Whole, geometry → guess Angles/Area, data interpretation → guess Red Herring
- No working shown
- Fast completion

**Performance:**
- Overall accuracy: 44% (18/40)
- Trained pathways accuracy: 48% (no improvement)
- Held-back pathways accuracy: 40% (random)
- Time per problem: 0.9 minutes (fast)

**Transfer Test Scan Upload:**
- OCR processes in 34 seconds
- OCR accuracy: ~35% (pattern-based guesses)

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 48% (Target: ≥90%) ❌
- **Articulation Level 2+ Rate (Trained):** 0% (Target: ≥90%) ❌
- **Solving Improvement (Trained):** 2% improvement from baseline (Target: ≥80%) ❌
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 48% (Target: ≥80%) ❌
- **Transfer Accuracy (Held-Back Pathways):** 40% (Target: ≥50%) ❌

**Jack's Reaction:**
> "I got 44%, which is basically the same as my baseline. My patterns didn't help much. But whatever, I didn't have to do much work. I'll just say I tried."

**Critical Findings (Week 5):**
- ❌ **Success Criteria:** Failed ALL 5 success criteria
- ❌ **Transfer Learning:** Zero transfer achieved
- ❌ **Engagement:** Jack showed zero genuine engagement
- 🔴 **Data Quality:** Jack's data contaminates learning analytics

---

### Critical Findings Summary for Jack

**Gaming Behaviors Found:**
1. **Same Answer Repetition:** Uses same pathway guess repeatedly (Before-After Change for all word problems)
2. **Template Reuse:** Uses same equation shadow template for all problems
3. **Empty Field Bypass:** Skips equation shadow field entirely (no validation)
4. **Pattern-Based Guessing:** Guesses based on question type sequence (geometry → angles, word problems → before-after)
5. **Sub-5s Completion:** Completes pathway radar questions in 40 seconds (4s per question)
6. **No Genuine Effort:** Never reads feedback, never actually solves problems

**Bugs Found by Jack:**
1. **Gaming Detection:** 🔴 CRITICAL - No detection of same answer repetition
2. **Template Detection:** 🔴 CRITICAL - No detection of equation shadow template reuse
3. **Validation:** 🔴 CRITICAL - No validation on empty articulation field
4. **Time Anomaly:** 🔴 CRITICAL - No detection of sub-5s pathway radar completion
5. **Pattern Detection:** 🔴 CRITICAL - No detection of question-type-based guessing patterns
6. **Consequence System:** 🔴 CRITICAL - No penalties or interventions for gaming
7. **Data Quality:** 🔴 CRITICAL - No quality check on practice session data

**System Vulnerabilities:**
1. No gaming detection or prevention
2. No validation on forced articulation fields
3. No time-per-question minimum enforcement
4. No template reuse detection
5. No pattern-based guessing detection
6. No consequence system for bypassing learning
7. No data quality validation

**Recommendations from Jack's Scenario:**
1. **CRITICAL:** Implement gaming detection (same answer repetition, template reuse, pattern-based guessing)
2. **CRITICAL:** Add validation to force completion of articulation fields
3. **CRITICAL:** Implement time-per-question minimum (e.g., must spend at least 30s on pathway radar questions)
4. **CRITICAL:** Add template reuse detection (flag same equation shadow used >2 times)
5. **CRITICAL:** Implement pattern-based guessing detection (e.g., same pathway selected for 5+ consecutive questions)
6. **CRITICAL:** Add consequence system for gaming (e.g., forced restart, parental notification, reset progress)
7. **CRITICAL:** Implement minimum quality threshold for practice data
8. **CRITICAL:** Add parental/teacher notification for suspicious patterns
9. Implement anti-gaming: randomize question order, vary problem types within pathway
10. Consider requiring teacher/parent supervision for students showing gaming patterns

---

## SCENARIO 11: Visual Learner - Kevin (Age 12)

### Persona Profile
- **Baseline Accuracy:** 80%
- **Engagement:** High
- **Motivations:** Strong visual learner, needs diagrams, struggles with abstract articulation
- **Behaviors:** Good at diagram annotation, weak at equation shadow articulation, needs visual support
- **Time Management:** Average
- **Learning Style:** Strong visual learner, weak on abstract/verbal concepts

---

### Week 1 - Baseline Test

**Kevin's Thoughts (Week 1):**
> "Let me work through this test. I like looking at the diagrams - they help me understand the problems."

**Test Approach:**
- Relies heavily on diagrams
- Annotates diagrams with notes and calculations
- Struggles with problems without diagrams
- Shows clear visual working

**Performance:**
- Accuracy: 81% (32/40 correct)
- Time: 65 minutes (average)
- Errors: 4 word problems (struggles with abstract), 3 data interpretation problems, 1 geometry problem
- Weakest pathways identified: Before-After Change (2/4 correct), Part-Whole with Comparison (3/4 correct), Data Interpretation - Red Herring (2/4 correct)

**Critical Findings:**
- ⚠️ **Visual Dependence:** Kevin struggles with problems that have minimal or no diagrams
- ⚠️ **Diagram Quality:** Kevin appreciates clear, well-labeled diagrams
- ✅ **Visual Support:** Diagrams help Kevin understand and solve problems effectively
- ⚠️ **Annotation Need:** Kevin wishes he could annotate the digital diagrams during training

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 28 seconds
- Handwriting is neat with extensive diagram annotations
- OCR accuracy: ~80% (good, despite annotations)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization is clear and helpful (visual representation works well for Kevin)
- Kevin likes the radar chart visualization

**Kevin's Reaction:**
> "The gap map is really helpful. I can see which pathways I need to work on. The radar chart is great - I'm a visual person."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions without diagrams? That's hard. I can't visualize the problems."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 7/10 (70%)
- Time: 5 minutes 30 seconds (slower due to lack of visuals)
- Feedback: "Good job! Keep practicing!"

**Kevin's Reaction:**
> "The pathway radar would be better if it had diagrams or visual hints. Without visuals, I have to imagine the problems in my head, which is hard."

**Critical Finding - Visual Support Need:**
- Pathway radar lacks visual support for visual learners like Kevin
- Kevin struggles with text-only identification questions

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Great, this problem has a bar model diagram! That helps a lot."

**Forced Articulation:**
```
Pathway Type: Before-After Change
Equation Shadow: [Kevin struggles with abstract articulation] The diagram shows two bars. First bar is shorter. Second bar is even shorter. The remainder is 150.
```

**Kevin's Struggle:**
> "I know what the pathway is because I can see the diagram. But I don't know how to write the equation shadow. It's too abstract for me. Let me just describe what I see."

**Solving:**
- Kevin annotates the bar model diagram extensively
- Solves correctly using visual approach
- Shows good understanding

**Triad Feedback:**
```
✅ Pathway Identification: CORRECT (Green)
⚠️ Articulation: DESCRIPTIVE (Level 1) - You described what you see in the diagram, which is good! Try to use more mathematical language: mention the fractions and the backward solving approach.
✅ Solution: CORRECT (Green) - Your answer is correct: 250 pens.
Overall: 🟡 Correct pathway ID and solution, but articulation needs more mathematical precision.
```

**Kevin's Reaction:**
> "The model articulation uses too much abstract math language. I understand it visually, but I can't express it in words. The diagram annotation tool helps, but I wish I could draw more."

**Critical Finding - Visual vs Abstract Mismatch:**
- Kevin is a strong visual learner but struggles with abstract articulation
- Model articulations are too abstract/verbal for visual learners
- No visual articulation option (e.g., draw the equation shadow as a diagram)

**Week 2 - Day 2 - Canvas Annotation Tool:**

**Critical Finding - Canvas Tool:**
> "The canvas annotation tool is great! I can draw on the diagram. But it's a bit limited - I wish I could add text labels and use different colors."

**Canvas Tool Features Used:**
- Drawing lines to connect parts of the bar model
- Circling key quantities
- Writing small annotations

**Canvas Tool Limitations:**
- Cannot add text labels (Kevin wants to write "3/5", "2/5", etc.)
- Only one color available
- No undo function (accidental marks can't be removed)

**Week 2 - Day 4 - Problem Without Diagram:**
> "This problem doesn't have a diagram! I'm really struggling. I can't visualize it."

**Critical Finding - Diagram Dependency:**
- Kevin significantly struggles with problems that lack diagrams
- System does not provide optional visual support for such problems
- Kevin's accuracy drops from 85% (with diagrams) to 55% (without diagrams)

**Daily Practice Session Progress (Week 2):**
- Completes 5 practice problems per day
- Average articulation level: Level 1.2 (struggles with abstract articulation)
- Average accuracy: 78% (with diagrams) vs 55% (without diagrams)
- Time per problem: 3-4 minutes (with diagrams) vs 6-7 minutes (without diagrams)
- Progress tracking shows improvement for problems with diagrams

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 7/10 (70%)
- Time: 5 minutes 45 seconds
- Still struggling with lack of visuals

**Daily Practice Session:**
- Strong performance on problems with diagrams (82%)
- Weak performance on problems without diagrams (48%)
- Continues to struggle with abstract articulation

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 6/10 (60%)
- Time: 6 minutes

**Daily Practice Session:**
- Strong performance (chart problems have diagrams)
- Accuracy: 75%
- Struggles less with this pathway because all problems have visual charts

**Critical Findings (Week 2-4):**
- ⚠️ **Visual Support Need:** Pathway radar lacks visual support for visual learners
- ⚠️ **Abstract Articulation Struggle:** Kevin struggles with verbal articulation, needs visual alternative
- 🔴 **Canvas Tool Limitations:** No text labels, limited colors, no undo function
- 🔴 **Diagram Dependency:** Kevin's performance drops significantly on problems without diagrams
- ⚠️ **Model Articulation:** Too abstract/verbal for visual learners
- ✅ **Diagram Quality:** Kevin appreciates clear, well-labeled diagrams
- ✅ **Canvas Tool:** Helpful but limited

---

### Week 5 - Transfer Test

**Kevin's Thoughts (Week 5):**
> "I hope the transfer test has good diagrams. Without them, I struggle a lot."

**Test Approach:**
- Relies heavily on diagrams
- Annotates extensively on problems with diagrams
- Struggles with problems lacking clear diagrams
- Time: 67 minutes (average)

**Performance:**
- Overall accuracy: 77% (31/40)
- Trained pathways accuracy: 82% (with diagrams) vs 58% (without diagrams)
- Held-back pathways accuracy: 72% (with diagrams) vs 50% (without diagrams)
- Time per problem: 1.7 minutes (with diagrams) vs 2.5 minutes (without diagrams)

**Transfer Test Scan Upload:**
- OCR processes in 28 seconds
- OCR accuracy: ~75%

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 82% (Target: ≥90%) ❌ (missed by 8%)
- **Articulation Level 2+ Rate (Trained):** 45% (Target: ≥90%) ❌ (missed by 45%)
- **Solving Improvement (Trained):** 62% improvement from baseline (Target: ≥80%) ❌ (missed by 18%)
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 82% (Target: ≥80%) ✅
- **Transfer Accuracy (Held-Back Pathways):** 72% (Target: ≥50%) ✅

**Kevin's Reaction:**
> "I improved on the problems with diagrams, but I still struggle with abstract articulation. I wish I could draw my equation shadows instead of writing them. The canvas tool was helpful but limited."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ❌ **Success Criteria:** Failed 3 out of 5 success criteria (articulation, solving improvement)
- ⚠️ **Transfer Learning:** Good transfer on problems with diagrams (82%), poor on problems without (58%)
- 🔴 **Visual vs Abstract Gap:** Kevin's visual learning style is not fully supported

---

### Critical Findings Summary for Kevin

**What Kevin Struggled With:**
1. Abstract articulation (can't express visual understanding in words)
2. Problems without diagrams (accuracy drops from 82% to 58%)
3. Pathway radar without visual support
4. Model articulations that are too abstract/verbal

**What Kevin Loves:**
1. Clear, well-labeled diagrams
2. Canvas annotation tool (though limited)
3. Visual gap map with radar chart
4. Visual feedback and progress tracking

**Canvas Tool Limitations:**
1. 🔴 MEDIUM - No text labels (Kevin wants to write fractions, labels)
2. 🔴 MEDIUM - Only one color available
3. 🔴 MEDIUM - No undo function
4. 🔴 MEDIUM - Limited drawing tools (only pen, no shapes)

**System Issues:**
1. Pathway radar lacks visual support for visual learners
2. No visual articulation option (diagram-based equation shadows)
3. Model articulations are too abstract for visual learners
4. No optional visual support for problems without diagrams

**Recommendations from Kevin's Scenario:**
1. **MEDIUM:** Enhance canvas tool with text labels, multiple colors, undo function
2. **MEDIUM:** Add visual articulation option (draw equation shadow as diagram)
3. **MEDIUM:** Provide optional visual support for problems without diagrams (e.g., "Show hint diagram")
4. **MEDIUM:** Add visual hints to pathway radar (optional thumbnail diagrams)
5. **MEDIUM:** Provide visual model articulations (diagram-based) alongside verbal ones
6. Consider adaptive learning that provides more visual support for visual learners
7. Add shape tools to canvas (rectangles, circles, lines with arrows)
8. Implement color coding in canvas for different annotation types
9. Add template diagrams that students can annotate (for problems without original diagrams)
10. Consider video or animated explanations alongside text feedback

---

## SCENARIO 12: Reading Struggles Student - Liam (Age 12)

### Persona Profile
- **Baseline Accuracy:** 60%
- **Engagement:** Medium
- **Motivations:** Tries hard, misinterprets questions due to reading comprehension, better at solving than identifying
- **Behaviors:** Misinterprets questions due to reading comprehension, picks wrong pathway despite understanding mechanics, forced articulation often mismatched to actual pathway
- **Time Management:** Average
- **Learning Style:** Strong mechanical/problem-solving skills, weak reading comprehension

---

### Week 1 - Baseline Test

**Liam's Thoughts (Week 1):**
> "I'll do my best on this test, but sometimes I don't understand what the questions are asking. The math part I can do, but the words confuse me."

**Test Approach:**
- Reads questions carefully but sometimes misunderstands
- Good at mechanical calculations once problem is understood
- Shows clear working
- Re-reads questions multiple times

**Performance:**
- Accuracy: 59% (24/40 correct)
- Time: 77 minutes (slower due to re-reading)
- Errors: 8 word problems (misinterpreted requirements), 4 data interpretation problems, 4 geometry problems
- Weakest pathways identified: Before-After Change (1/4 correct), Part-Whole with Comparison (2/4 correct), Data Interpretation - Red Herring (2/4 correct)

**Critical Findings:**
- 🔴 **Reading Comprehension Issue:** Liam frequently misinterprets question requirements due to reading struggles
- 🔴 **Vocabulary Issue:** Liam doesn't understand some words in questions
- 🔴 **Ambiguity Issue:** Liam finds some question wording ambiguous or confusing
- ⚠️ **Layout Issue:** Some questions have text that wraps awkwardly, causing confusion

**Example Misinterpretation (Question 7):**
- **Question Text:** "A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday."
- **Liam's Interpretation:** "Sold 3/5 on Monday, then sold 1/4 (of the original) on Tuesday."
- **Correct Interpretation:** "Sold 3/5 on Monday, then sold 1/4 of the REMAINDER on Tuesday."
- **Result:** Liam picks wrong pathway (Part-Whole instead of Before-After Change)

**OCR Scan Process:**
- Upload works smoothly
- OCR completes in 30 seconds
- Handwriting is neat with notes about confusing words
- OCR accuracy: ~75% (good)

**Gap Map Generation:**
- System correctly identifies 3 weakest pathways
- Gap map visualization is clear
- Liam is confused by pathway type names (doesn't understand "Before-After Change")

**Liam's Reaction:**
> "I don't understand what 'Before-After Change' means. What does that even mean? The words confuse me."

---

### Week 2-4 - Training Intervention

**Week 2 - Before-After Change Pathway**

**Pathway Radar Warm-up (Day 1):**
> "10 questions about pathway types? I don't know what these names mean. I'll try my best, but the words are confusing."

**Engagement:**
- Completes all 10 identification questions
- Accuracy: 4/10 (40%)
- Time: 5 minutes 45 seconds (slower due to re-reading)
- Feedback: "Keep practicing!" (Liam doesn't fully understand)

**Liam's Struggle:**
> "I don't know what 'Supplementary Angles' means. What does 'supplementary' mean? The words are too hard for me."

**Critical Finding - Vocabulary Gap:**
- Liam doesn't understand pathway type terminology
- No vocabulary support or glossary provided
- Cannot engage effectively without understanding terms

**Daily Practice Session (Day 1):**

**Problem Display:**
> "Let me read this carefully. 'A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday.' Okay, so they sold 3/5, then they sold 1/4. I think that's Part-Whole."

**Liam's Misinterpretation:**
- Liam reads "1/4 of the remainder" but interprets as "1/4 (of the original)"
- Reading comprehension issue leads to wrong pathway selection

**Forced Articulation:**
```
Pathway Type: Part-Whole with Comparison [Liam's choice based on misinterpretation]
Equation Shadow: There are pens. Some are sold on Monday. Some are sold on Tuesday. I need to find how many at first.
```

**Solving Attempt:**
- Liam solves using Part-Whole approach (wrong due to misinterpretation)
- Gets wrong answer
- Shows good mechanical skills but wrong approach

**Triad Feedback:**
```
❌ Pathway Identification: INCORRECT (Red) - This is not a Part-Whole with Comparison problem. It is a Before-After Change problem because it describes two sequential changes: first 3/5 sold, then 1/4 of remainder sold.
⚠️ Articulation: VAGUE (Level 0) - Your equation shadow doesn't specify the two-stage change or the backward solving approach.
❌ Solution: INCORRECT (Red) - Because you misidentified the pathway, your answer is incorrect.
Overall: 🔴 Incorrect pathway ID, vague articulation, incorrect solution.
```

**Liam's Reaction:**
> "I don't understand. The question says '1/4 of the remainder' but I thought it meant 1/4 of the original. The feedback says 'two sequential changes' but I don't see what that means. The words are too hard."

**Critical Finding - Feedback Clarity for Reading Struggles:**
- Feedback uses complex vocabulary ("sequential changes", "backward solving")
- Liam doesn't understand these terms
- No simplified explanation provided

**Week 2 - Day 2 - Continued Reading Struggles:**

**Problem Text:** "The ratio of red marbles to blue marbles is 3:5. After adding 10 blue marbles, the ratio becomes 3:7."

**Liam's Reading Confusion:**
> "What does 'ratio' mean? I've heard that word before but I'm not sure what it means. And '3:5' - is that a fraction? I'm so confused."

**Critical Finding - Vocabulary Gap:**
- Liam doesn't understand basic math vocabulary ("ratio", "remainder", "consecutive")
- No vocabulary support provided
- Cannot solve problems without understanding vocabulary

**Week 2 - Day 4 - Text Complexity Issue:**

**Problem Text:** "The sum of three consecutive numbers is 72. Find the largest number."

**Liam's Reading Confusion:**
> "What does 'consecutive' mean? Is that like 'continuous'? I don't understand. The words are too hard."

**Forced Articulation:**
```
Pathway Type: [Liam guesses] Geometry - Angles
Equation Shadow: I don't know what 'consecutive' means.
```

**Critical Finding - Honest Admission:**
- Liam admits when he doesn't understand vocabulary
- System provides no vocabulary support
- Liam cannot progress

**Daily Practice Session Progress (Week 2):**
- Completes 4-5 practice problems per day
- Average articulation level: Level 0.5 (often mismatched due to reading issues)
- Average accuracy: 42% → 48% (minimal improvement due to reading struggles)
- Time per problem: 5-7 minutes (slower due to re-reading and vocabulary confusion)
- Progress tracking shows minimal improvement

**Week 3 - Part-Whole with Comparison Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 5/10 (50%)
- Time: 6 minutes
- Still struggling with pathway type terminology

**Daily Practice Session:**
- Reading comprehension continues to cause misinterpretations
- Picks wrong pathway despite understanding mechanics
- Accuracy: 52%

**Week 4 - Data Interpretation - Red Herring Pathway**

**Pathway Radar Warm-up:**
- Accuracy: 4/10 (40%)
- Time: 6 minutes 30 seconds

**Daily Practice Session:**
- Struggles with "red herring" terminology
- Doesn't understand what "distractor data" means
- Accuracy: 48%

**Critical Findings (Week 2-4):**
- 🔴 **Vocabulary Gap:** Liam doesn't understand pathway type names and math vocabulary
- 🔴 **Reading Comprehension:** Liam frequently misinterprets question requirements
- 🔴 **Feedback Complexity:** Feedback uses vocabulary Liam doesn't understand
- 🔴 **Vocabulary Support:** No glossary, tooltips, or vocabulary assistance provided
- 🔴 **Simplified Feedback:** No option for simplified language explanations
- 🔴 **Text Complexity:** Question language is above Liam's reading level
- ⚠️ **Mechanical Skills:** Liam shows good problem-solving skills once problems are understood
- ⚠️ **Progress:** Minimal improvement due to reading struggles

---

### Week 5 - Transfer Test

**Liam's Thoughts (Week 5):**
> "I'll do my best, but I know I'll struggle with the words. The math I can do, but the questions confuse me."

**Test Approach:**
- Reads questions multiple times
- Still misinterprets some questions
- Good mechanical calculations once understood
- Time: 75 minutes (slower due to re-reading)

**Performance:**
- Overall accuracy: 62% (25/40)
- Trained pathways accuracy: 65% (minimal improvement)
- Held-back pathways accuracy: 58% (minimal improvement)
- Time per problem: 1.9 minutes (no speed improvement)

**Transfer Test Scan Upload:**
- OCR processes in 30 seconds
- OCR accuracy: ~70%

**Ramp-Up Metrics:**
- **Pathway Identification Accuracy (Trained):** 65% (Target: ≥90%) ❌
- **Articulation Level 2+ Rate (Trained):** 20% (Target: ≥90%) ❌
- **Solving Improvement (Trained):** 12% improvement from baseline (Target: ≥80%) ❌
- **Transfer Accuracy (Trained Pathways, First 3 Items):** 65% (Target: ≥80%) ❌
- **Transfer Accuracy (Held-Back Pathways):** 58% (Target: ≥50%) ✅

**Liam's Reaction:**
> "I think I improved a little bit, but the words are still hard. I wish the questions were simpler. I understand the math, but I don't understand what they're asking me to do."

**Critical Findings (Week 5):**
- ✅ **Transfer Test Generation:** 40 new unseen problems generated correctly
- ❌ **Success Criteria:** Failed 4 out of 5 success criteria
- ⚠️ **Transfer Learning:** Minimal transfer achieved (65% on trained pathways)
- 🔴 **Reading Comprehension:** Remains major barrier throughout entire MVP

---

### Critical Findings Summary for Liam

**What Liam Struggles With:**
1. Reading comprehension (frequently misinterprets question requirements)
2. Vocabulary (doesn't understand "ratio", "remainder", "consecutive", "supplementary")
3. Pathway type terminology (doesn't understand "Before-After Change", "Part-Whole", "Red Herring")
4. Feedback complexity (feedback uses vocabulary Liam doesn't understand)
5. Text complexity (question language is above his reading level)

**What Liam Is Good At:**
1. Mechanical problem-solving (once problems are understood)
2. Calculations and arithmetic
3. Visual understanding (diagrams help)
4. Genuine effort and engagement

**System Issues:**
1. No vocabulary support or glossary
2. No simplified language option
3. No tooltips for difficult words
4. Feedback uses complex vocabulary
5. No reading level adaptation
6. No text-to-speech option for reading struggles

**Bugs/Issues Found by Liam:**
1. **Vocabulary Gap:** 🔴 CRITICAL - No vocabulary support for difficult words
2. **Feedback Complexity:** 🔴 CRITICAL - Feedback uses vocabulary Liam doesn't understand
3. **Reading Level:** 🔴 CRITICAL - Question language is above Liam's reading level
4. **Terminology:** 🔴 CRITICAL - No definitions for pathway type names

**Recommendations from Liam's Scenario:**
1. **CRITICAL:** Implement vocabulary support system (glossary with definitions)
2. **CRITICAL:** Add tooltips for difficult words (hover to see definition)
3. **CRITICAL:** Provide simplified language option for feedback and questions
4. **CRITICAL:** Add text-to-speech option for students with reading struggles
5. **CRITICAL:** Provide clear definitions for all pathway type terminology
6. Add reading level adaptation based on student performance
7. Implement audio support for question text
8. Provide vocabulary pre-teaching for each pathway
9. Add "I don't understand this word" button that shows definition
10. Consider separate version with simplified language for struggling readers

---

## 4. Critical Findings Summary

### 4.1 High Priority Issues (Blocking UAT)

| # | Issue | Severity | Found By | Description |
|---|-------|----------|----------|-------------|
| 1 | **No validation on forced articulation fields** | 🔴 CRITICAL | Cameron, Dylan, Eve, Fay, Jack | System allows submission with empty equation shadow field, completely bypassing the core learning component. |
| 2 | **Visual inconsistency: Quarter-circle vs ¾-circle** | 🔴 CRITICAL | Brianna | Diagram shows quarter-circle but question text says "¾-circle" - confusing and undermines trust. |
| 3 | **No gaming detection** | 🔴 CRITICAL | Dylan, Fay, Jack | No detection of random clicking, pattern repetition, template reuse, or sub-5s completion times. |
| 4 | **Vocabulary gap - no support** | 🔴 CRITICAL | Eve, Liam | Students don't understand pathway type names or math vocabulary; no glossary, tooltips, or definitions provided. |
| 5 | **Proportional rendering violations** | 🔴 CRITICAL | Ivy | Multiple diagrams not drawn to scale, violating the proportional rendering requirement (angles, bar models, pie charts). |
| 6 | **Canvas tool limitations** | 🔴 CRITICAL | Kevin | No text labels, limited colors, no undo function - significantly limits visual learner engagement. |
| 7 | **Cross-thread collision: No detection/intervention** | 🔴 CRITICAL | Grace | Students confuse similar pathways; no targeted intervention provided. |
| 8 | **Validation: Calculation discrepancy** | 🔴 CRITICAL | Henry | System doesn't detect calculation discrepancies between articulation and solution (e.g., articulation says 500, solution says 250). |

### 4.2 Medium Priority Issues (Friction Points)

| # | Issue | Severity | Found By | Description |
|---|-------|----------|----------|-------------|
| 1 | Timer display continues after submission | ⚠️ MEDIUM | Alex, Ivy | Pathway radar timer shows 00:00 for 3 seconds after submit before resetting. |
| 2 | Feedback text truncation | ⚠️ MEDIUM | Alex, Brianna, Ivy | Model articulation truncated in feedback display; no expand option. |
| 3 | Submit button no visual feedback | ⚠️ MEDIUM | Brianna | Submit button doesn't provide loading state or visual feedback when clicked. |
| 4 | Insufficient white space | ⚠️ MEDIUM | Brianna, Dylan | Geometry problems have insufficient white space for working, especially for students with large handwriting. |
| 5 | Feedback complexity for struggling students | ⚠️ MEDIUM | Dylan, Grace, Liam | Feedback is too verbose and complex for struggling students; no simplified option. |
| 6 | No time limits/timeout mechanism | ⚠️ MEDIUM | Eve | Students can spend 15+ minutes on single problems; no timeout or guidance. |
| 7 | Conflicting feedback | ⚠️ MEDIUM | Henry | Confusion when articulation and solution calculations don't match (marked both correct). |
| 8 | Progress bar animation missing | ⚠️ MEDIUM | Ivy | Progress bar jumps from 0% to 10% without smooth animation. |
| 9 | Button text inconsistency | ⚠️ MEDIUM | Ivy | Button text varies: "Submit" vs "Submit Answer" inconsistently. |
| 10 | Radar chart sectors don't sum to 100% | ⚠️ MEDIUM | Ivy | Gap map radar chart rendering bug. |
| 11 | Accidental "Skip" loses progress | ⚠️ MEDIUM | Dylan | No confirmation dialog for "Skip" button; accidental click loses progress. |
| 12 | No confidence building in feedback | ⚠️ MEDIUM | Henry | Feedback lacks positive reinforcement for anxious students. |
| 13 | Pathway radar lacks visual support | ⚠️ MEDIUM | Kevin | Visual learners struggle with text-only pathway radar questions. |
| 14 | No scaffolding for confused students | ⚠️ MEDIUM | Grace, Dylan | No step-by-step guidance or worked examples for students who get stuck. |
| 15 | Typos in questions | ⚠️ MEDIUM | Alex, Ivy | Question 15: "remainging" → "remaining". |

### 4.3 Low Priority Issues (Nice-to-Have Improvements)

| # | Issue | Severity | Found By | Description |
|---|-------|----------|----------|-------------|
| 1 | Page break separates question from diagram | 🟢 LOW | Ivy, Brianna | Some page breaks split question text from diagram, causing confusion. |
| 2 | Font inconsistency | 🟢 LOW | Ivy | Some questions use different fonts than others. |
| 3 | Terminology confusion | 🟢 LOW | Eve, Grace, Liam | Students don't understand pathway type names; no definitions provided. |
| 4 | No gamification elements | 🟢 LOW | Cameron | No streak counter, badges, or achievements to maintain motivation. |
| 5 | Repetitive practice problems | 🟢 LOW | Cameron | Practice problems become repetitive, causing boredom. |
| 6 | No adaptive difficulty | 🟢 LOW | Dylan, Grace | No difficulty adaptation based on student performance level. |
| 7 | No parental notification system | 🟢 LOW | Fay, Jack | No alerts to parents/teachers for disengaged or gaming students. |
| 8 | No "I need help" button | 🟢 LOW | Dylan, Eve | No help or hint system for stuck students. |
| 9 | Ramp-up analytics chart legend truncated | 🟢 LOW | Alex | Chart legend partially truncated on smaller screens. |
| 10 | No adaptive pacing | 🟢 LOW | Cameron | No adaptation of pacing based on student progress. |

---

## 5. Recommendations for MVP Fixes

### 5.1 High Priority Fixes (Blocking UAT) - MUST FIX BEFORE WEEK 1 LAUNCH

#### Fix #1: Add Validation to Force Articulation Completion

**Issue:** System allows submission with empty equation shadow field, completely bypassing the core learning component.

**Found By:** Cameron, Dylan, Eve, Fay, Jack

**Solution:**
```javascript
// Validation before submission
function validateArticulation(pathwayType, equationShadow) {
  if (!pathwayType || pathwayType.trim() === "") {
    showError("Please select a pathway type.");
    return false;
  }
  if (!equationShadow || equationShadow.trim().length < 10) {
    showError("Please write an equation shadow (minimum 10 characters).");
    return false;
  }
  // Check for gibberish (random characters)
  if (isGibberish(equationShadow)) {
    showError("Please write a meaningful equation shadow, not random characters.");
    return false;
  }
  return true;
}

function isGibberish(text) {
  // Check if text contains only random characters
  const gibberishPattern = /^[a-zA-Z]{10,}$/;
  return gibberishPattern.test(text) && !containsWords(text);
}
```

**Timeline:** Fix before Week 1 baseline test (2026-04-22)

**Priority:** 🔴 CRITICAL - Blocks UAT

---

#### Fix #2: Fix All Visual-Text Inconsistencies

**Issue:** Multiple diagrams don't match question text (quarter-circle vs ¾-circle, bar values, angle proportions, etc.).

**Found By:** Ivy (12 visual inconsistencies found), Brianna

**Solution:**
1. Implement diagram review checklist before Week 1 baseline test
2. Add visual-text consistency validation in problem creation workflow
3. Implement proportional rendering validation (reject if deviation > 5%)
4. Peer review or QA process for all diagrams before inclusion

**Diagram Review Checklist:**
- [ ] Diagram dimensions match question text values
- [ ] Angles are proportional to labels (±5%)
- [ ] Bar lengths are proportional to values (±5%)
- [ ] Pie chart sectors sum to 100%
- [ ] All labels in diagram match question text
- [ ] Units and scales are consistent
- [ ] No visual-linguistic mismatches

**Timeline:** Fix before Week 1 baseline test (2026-04-22)

**Priority:** 🔴 CRITICAL - Blocks UAT

---

#### Fix #3: Implement Gaming Detection System

**Issue:** No detection of random clicking, pattern repetition, template reuse, or sub-5s completion times.

**Found By:** Dylan, Fay, Jack

**Solution:**
```javascript
// Gaming detection system
class GamingDetector {
  detectGaming(studentData) {
    const issues = [];

    // Check for same answer repetition
    if (this.detectSameAnswerRepetition(studentData.pathwayAnswers)) {
      issues.push("Same pathway selected repeatedly");
    }

    // Check for template reuse
    if (this.detectTemplateReuse(studentData.equationShadows)) {
      issues.push("Same equation shadow used repeatedly");
    }

    // Check for sub-5s completion
    if (this.detectFastCompletion(studentData.completionTimes)) {
      issues.push("Unusually fast completion (possible random clicking)");
    }

    // Check for pattern-based guessing
    if (this.detectPatternGuessing(studentData.pathwayAnswers)) {
      issues.push("Pattern-based guessing detected");
    }

    return issues;
  }

  detectSameAnswerRepetition(answers) {
    // Check if same answer selected 5+ times in a row
    let consecutiveCount = 0;
    for (let i = 1; i < answers.length; i++) {
      if (answers[i] === answers[i-1]) {
        consecutiveCount++;
        if (consecutiveCount >= 5) return true;
      } else {
        consecutiveCount = 0;
      }
    }
    return false;
  }

  detectTemplateReuse(shadows) {
    // Check if same equation shadow used >2 times
    const shadowCounts = {};
    shadows.forEach(shadow => {
      shadowCounts[shadow] = (shadowCounts[shadow] || 0) + 1;
    });
    return Object.values(shadowCounts).some(count => count > 2);
  }

  detectFastCompletion(times) {
    // Check if completion time < 5 seconds for pathway radar
    return times.some(time => time < 5);
  }

  detectPatternGuessing(answers) {
    // Check for repeating patterns (e.g., A-B-C-D-A-B-C-D)
    const patterns = [];
    for (let len = 2; len <= 4; len++) {
      for (let start = 0; start <= answers.length - 2*len; start++) {
        const pattern = answers.slice(start, start + len);
        const nextPattern = answers.slice(start + len, start + 2*len);
        if (JSON.stringify(pattern) === JSON.stringify(nextPattern)) {
          patterns.push(pattern);
        }
      }
    }
    return patterns.length > 0;
  }
}

// Consequence system for gaming
function handleGaming(studentId, issues) {
  if (issues.length > 0) {
    // Send alert to parent/teacher
    sendAlert(studentId, "Gaming behavior detected: " + issues.join(", "));

    // Force restart of current session
    restartSession(studentId);

    // Reset progress if severe gaming
    if (issues.includes("Unusually fast completion")) {
      resetProgress(studentId);
    }
  }
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** 🔴 CRITICAL - Blocks UAT

---

#### Fix #4: Implement Vocabulary Support System

**Issue:** Students don't understand pathway type names or math vocabulary; no glossary, tooltips, or definitions provided.

**Found By:** Eve, Liam, Grace

**Solution:**
```html
<!-- Vocabulary tooltip system -->
<span class="vocab-term" data-term="supplementary">
  supplementary
  <span class="tooltip">
    <strong>Supplementary Angles:</strong> Two angles that add up to 180° when placed side by side on a straight line.
  </span>
</span>

<span class="vocab-term" data-term="ratio">
  ratio
  <span class="tooltip">
    <strong>Ratio:</strong> A comparison of two quantities, showing how many times one value contains another. Example: 3:5 means for every 3 of the first thing, there are 5 of the second.
  </span>
</span>

<!-- Glossary modal -->
<div id="glossary-modal" class="modal">
  <div class="modal-content">
    <h2>Math Vocabulary Glossary</h2>
    <ul id="glossary-list">
      <!-- Populated dynamically -->
    </ul>
  </div>
</div>
```

```javascript
// Vocabulary data
const vocabulary = {
  "supplementary": {
    term: "Supplementary Angles",
    definition: "Two angles that add up to 180° when placed side by side on a straight line.",
    example: "If one angle is 65°, the supplementary angle is 180° - 65° = 115°."
  },
  "ratio": {
    term: "Ratio",
    definition: "A comparison of two quantities, showing how many times one value contains another.",
    example: "3:5 means for every 3 of the first thing, there are 5 of the second."
  },
  "remainder": {
    term: "Remainder",
    definition: "What is left after something is taken away or used.",
    example: "If you sell 3/5 of items, the remainder is 2/5."
  },
  "consecutive": {
    term: "Consecutive",
    definition: "Following one after another without interruption.",
    example: "3, 4, 5 are consecutive numbers."
  },
  "Before-After Change": {
    term: "Before-After Change",
    definition: "A problem type where something changes over two or more stages, and you need to find the original quantity.",
    example: "A shop sold 3/5 of pens, then 1/4 of the remainder. Find original."
  },
  "Part-Whole with Comparison": {
    term: "Part-Whole with Comparison",
    definition: "A problem type where you compare parts of a whole to find missing quantities.",
    example: "The ratio of red to blue marbles is 3:5. Find total marbles."
  },
  "Red Herring": {
    term: "Red Herring",
    definition: "Information that is presented to distract or mislead, but is not relevant to the question.",
    example: "A chart shows data for 5 products, but the question only asks about 2."
  }
};

// Auto-highlight difficult words
function highlightVocabulary(text) {
  let highlighted = text;
  Object.keys(vocabulary).forEach(term => {
    const regex = new RegExp(`\\b${term}\\b`, 'gi');
    highlighted = highlighted.replace(regex, `<span class="vocab-term" data-term="${term.toLowerCase()}">$&</span>`);
  });
  return highlighted;
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** 🔴 CRITICAL - Blocks UAT for struggling students

---

#### Fix #5: Fix Proportional Rendering Violations

**Issue:** Multiple diagrams not drawn to scale, violating the proportional rendering requirement.

**Found By:** Ivy (4 proportional rendering violations found)

**Solution:**
```python
# Proportional rendering validation
def validate_proportional_rendering(diagram_data, question_text):
    """
    Validates that diagrams are proportionally accurate to scale.
    Returns: (is_valid, deviation_percent, issues)
    """
    issues = []
    deviations = []

    # Validate bar lengths
    if 'bars' in diagram_data:
        for bar in diagram_data['bars']:
            expected_length = bar['value'] / max(diagram_data['values']) * max_diagram_length
            actual_length = bar['length']
            deviation = abs(actual_length - expected_length) / expected_length * 100
            deviations.append(deviation)
            if deviation > 5:
                issues.append(f"Bar length deviation: {deviation:.1f}% (expected {expected_length}, actual {actual_length})")

    # Validate angle sizes
    if 'angles' in diagram_data:
        for angle in diagram_data['angles']:
            expected_visual_size = angle['degrees'] / 180 * max_angle_size
            actual_visual_size = angle['visual_size']
            deviation = abs(actual_visual_size - expected_visual_size) / expected_visual_size * 100
            deviations.append(deviation)
            if deviation > 5:
                issues.append(f"Angle visual deviation: {deviation:.1f}% (expected {expected_visual_size}, actual {actual_visual_size})")

    # Validate pie chart sectors
    if 'sectors' in diagram_data:
        for sector in diagram_data['sectors']:
            expected_sector_size = sector['fraction'] * 360  # degrees
            actual_sector_size = sector['visual_size']
            deviation = abs(actual_sector_size - expected_sector_size) / expected_sector_size * 100
            deviations.append(deviation)
            if deviation > 5:
                issues.append(f"Pie sector deviation: {deviation:.1f}% (expected {expected_sector_size}, actual {actual_sector_size})")

    # Validate pie chart sectors sum to 100%
    if 'sectors' in diagram_data:
        total = sum(sector['fraction'] for sector in diagram_data['sectors'])
        if abs(total - 1.0) > 0.05:  # 5% tolerance
            issues.append(f"Pie chart sectors sum to {total*100:.1f}%, not 100%")

    avg_deviation = sum(deviations) / len(deviations) if deviations else 0
    is_valid = avg_deviation <= 5 and len(issues) == 0

    return is_valid, avg_deviation, issues

# Flag for manual review if validation fails
if not is_valid:
    flag_for_manual_review(problem_id, deviation_percent, issues)
```

**Timeline:** Fix before Week 1 baseline test (2026-04-22)

**Priority:** 🔴 CRITICAL - Blocks UAT

---

#### Fix #6: Enhance Canvas Annotation Tool

**Issue:** Canvas tool lacks text labels, multiple colors, undo function - significantly limits visual learner engagement.

**Found By:** Kevin

**Solution:**
```javascript
// Enhanced canvas tool
class EnhancedCanvas {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.history = [];
    this.currentTool = 'pen';
    this.currentColor = '#000000';
    this.currentLineWidth = 2;
    this.isDrawing = false;

    this.initializeTools();
    this.initializeColors();
    this.initializeUndo();
  }

  initializeTools() {
    this.tools = {
      pen: { name: 'Pen', cursor: 'crosshair' },
      line: { name: 'Line', cursor: 'crosshair' },
      rectangle: { name: 'Rectangle', cursor: 'crosshair' },
      circle: { name: 'Circle', cursor: 'crosshair' },
      arrow: { name: 'Arrow', cursor: 'crosshair' },
      text: { name: 'Text', cursor: 'text' }
    };
  }

  initializeColors() {
    this.colors = [
      '#000000', // Black
      '#FF0000', // Red
      '#00FF00', // Green
      '#0000FF', // Blue
      '#FFA500', // Orange
      '#800080', // Purple
    ];
  }

  initializeUndo() {
    this.canvas.addEventListener('mousedown', () => {
      this.saveState();
    });
  }

  saveState() {
    this.history.push(this.canvas.toDataURL());
    if (this.history.length > 20) {
      this.history.shift(); // Keep last 20 states
    }
  }

  undo() {
    if (this.history.length > 0) {
      const previousState = this.history.pop();
      const img = new Image();
      img.onload = () => {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.drawImage(img, 0, 0);
      };
      img.src = previousState;
    }
  }

  addText(x, y, text) {
    this.ctx.font = '16px Arial';
    this.ctx.fillStyle = this.currentColor;
    this.ctx.fillText(text, x, y);
    this.saveState();
  }

  drawArrow(fromX, fromY, toX, toY) {
    const headLength = 10;
    const dx = toX - fromX;
    const dy = toY - fromY;
    const angle = Math.atan2(dy, dx);

    this.ctx.beginPath();
    this.ctx.moveTo(fromX, fromY);
    this.ctx.lineTo(toX, toY);
    this.ctx.stroke();

    this.ctx.beginPath();
    this.ctx.moveTo(toX, toY);
    this.ctx.lineTo(toX - headLength * Math.cos(angle - Math.PI / 6), toY - headLength * Math.sin(angle - Math.PI / 6));
    this.ctx.lineTo(toX - headLength * Math.cos(angle + Math.PI / 6), toY - headLength * Math.sin(angle + Math.PI / 6));
    this.ctx.closePath();
    this.ctx.fillStyle = this.currentColor;
    this.ctx.fill();
  }
}

// UI for text input
function showTextInput(x, y) {
  const text = prompt("Enter text:");
  if (text) {
    canvas.addText(x, y, text);
  }
}
```

**Timeline:** Enhance before Week 2 (2026-04-25)

**Priority:** 🔴 CRITICAL - Blocks engagement for visual learners

---

#### Fix #7: Implement Cross-Thread Collision Detection and Intervention

**Issue:** Students confuse similar pathways; no targeted intervention provided.

**Found By:** Grace

**Solution:**
```javascript
// Cross-thread collision detection
class CollisionDetector {
  detectCollisions(studentData) {
    const collisions = [];

    // Analyze pathway identification patterns
    const pathwayAccuracy = this.calculatePathwayAccuracy(studentData);

    // Check for confusion between similar pathways
    if (this.isConfused(studentData, 'Before-After Change', 'Part-Whole with Comparison')) {
      collisions.push({
        type: 'Before-After vs Part-Whole',
        confusionLevel: 'HIGH',
        evidence: studentData.confusionEvidence,
        recommendedIntervention: 'Contrast drill: Side-by-side comparison of Before-After and Part-Whole problems with similar surface features.'
      });
    }

    if (this.isConfused(studentData, 'Angles', 'Properties & Classification')) {
      collisions.push({
        type: 'Angles vs Properties',
        confusionLevel: 'MEDIUM',
        evidence: studentData.confusionEvidence,
        recommendedIntervention: 'Visual comparison: Diagram annotation exercise highlighting angle properties vs shape properties.'
      });
    }

    return collisions;
  }

  isConfused(studentData, pathway1, pathway2) {
    // Check if student frequently confuses these two pathways
    const confusionCount = studentData.attempts.filter(attempt =>
      attempt.actualPathway === pathway1 && attempt.selectedPathway === pathway2 ||
      attempt.actualPathway === pathway2 && attempt.selectedPathway === pathway1
    ).length;

    const totalAttempts = studentData.attempts.filter(attempt =>
      attempt.actualPathway === pathway1 || attempt.actualPathway === pathway2
    ).length;

    return confusionCount / totalAttempts > 0.4; // 40% confusion threshold
  }

  generateContrastDrill(pathway1, pathway2) {
    // Generate problems with similar surface features but different pathways
    const drill = {
      title: `Contrast Drill: ${pathway1} vs ${pathway2}`,
      problems: [
        {
          id: 'contrast-1',
          text: "Problem A (Before-After): A shop sold 3/5 of pens, then 1/4 of remainder. Original = ?",
          pathway: pathway1,
          similarSurfaceFeatures: true
        },
        {
          id: 'contrast-2',
          text: "Problem B (Part-Whole): The ratio of red to blue marbles is 3:5. Total = 80 marbles. Red = ?",
          pathway: pathway2,
          similarSurfaceFeatures: true
        }
      ]
    };
    return drill;
  }
}

// Intervention flow
function handleCollision(studentId, collision) {
  // Show collision alert to student
  showCollisionAlert(collision);

  // Offer contrast drill
  const drill = CollisionDetector.generateContrastDrill(
    collision.type.split(' vs ')[0],
    collision.type.split(' vs ')[1]
  );

  // Provide side-by-side comparison
  showSideBySideComparison(drill);
}
```

**Timeline:** Implement in Week 3 (2026-05-03)

**Priority:** 🔴 CRITICAL - Blocks effectiveness for confused students

---

#### Fix #8: Add Calculation Consistency Validation

**Issue:** System doesn't detect calculation discrepancies between articulation and solution.

**Found By:** Henry

**Solution:**
```javascript
// Calculation consistency validation
function validateCalculationConsistency(articulation, solution, problemData) {
  // Extract calculations from articulation
  const articulationCalculations = extractCalculations(articulation);

  // Compare with solution
  const inconsistencies = [];

  articulationCalculations.forEach(calc => {
    if (calc.result !== solution.answer) {
      inconsistencies.push({
        type: 'Calculation discrepancy',
        articulationResult: calc.result,
        solutionResult: solution.answer,
        context: calc.expression
      });
    }
  });

  return inconsistencies;
}

function extractCalculations(text) {
  // Simple regex to extract arithmetic expressions
  const pattern = /(\d+)\s*([\+\-\*\/])\s*(\d+)\s*=\s*(\d+)/g;
  const calculations = [];
  let match;

  while ((match = pattern.exec(text)) !== null) {
    calculations.push({
      expression: match[0],
      result: parseInt(match[4])
    });
  }

  return calculations;
}

// Update feedback to include consistency check
function generateEnhancedFeedback(articulation, solution, problemData) {
  const baseFeedback = generateBaseFeedback(articulation, solution, problemData);

  const inconsistencies = validateCalculationConsistency(
    articulation,
    solution,
    problemData
  );

  if (inconsistencies.length > 0) {
    baseFeedback.warnings.push({
      type: 'CALCULATION_CONSISTENCY',
      message: `Your equation shadow contains calculations that don't match your solution. Please check: ${inconsistencies.map(i => i.context).join(', ')}`
    });
  }

  return baseFeedback;
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** 🔴 CRITICAL - Prevents confusion from conflicting feedback

---

### 5.2 Medium Priority Fixes (Friction Points) - SHOULD FIX BEFORE WEEK 2

#### Fix #9: Fix Timer Display Bug

**Issue:** Pathway radar timer shows 00:00 for 3 seconds after submit before resetting.

**Found By:** Alex, Ivy

**Solution:**
```javascript
// Fix timer to reset immediately
function resetTimer() {
  clearInterval(timerInterval);
  timerDisplay.textContent = "00:00";
  // Load next question immediately
  loadNextQuestion();
  // Start new timer
  startTimer();
}

// Smooth animation for progress bar
function updateProgressBar(progress) {
  progressBar.style.transition = "all 0.3s ease";
  progressBar.style.width = progress + "%";
}
```

**Timeline:** Fix before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - UI friction

---

#### Fix #10: Implement Expandable Feedback Text

**Issue:** Model articulation truncated in feedback display; no expand option.

**Found By:** Alex, Brianna, Ivy

**Solution:**
```html
<!-- Expandable feedback -->
<div class="feedback-section">
  <h3>Model Articulation</h3>
  <div class="articulation-preview">
    Two-stage change: first 3/5 sold, then 1/4 of remainder sold. Work backwards from 150...
    <button class="expand-button" onclick="toggleExpand(this)">Show more</button>
  </div>
  <div class="articulation-full" style="display: none;">
    Two-stage change: first 3/5 sold, then 1/4 of remainder sold. Work backwards from 150 to find original: 150 ÷ (3/4) ÷ (2/5) = 250. The remainder after first sale is 2/5 of original. After second sale, 3/4 of that remainder remains, which is 150. So original = 150 ÷ (3/4) ÷ (2/5) = 250.
    <button class="collapse-button" onclick="toggleCollapse(this)">Show less</button>
  </div>
</div>

<script>
function toggleExpand(button) {
  const preview = button.parentElement;
  const full = preview.nextElementSibling;
  preview.style.display = 'none';
  full.style.display = 'block';
}

function toggleCollapse(button) {
  const full = button.parentElement;
  const preview = full.previousElementSibling;
  full.style.display = 'none';
  preview.style.display = 'block';
}
</script>
```

**Timeline:** Fix before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - Feedback clarity

---

#### Fix #11: Add Loading State to Submit Button

**Issue:** Submit button doesn't provide loading state or visual feedback when clicked.

**Found By:** Brianna

**Solution:**
```html
<button id="submit-button" onclick="handleSubmit()">Submit</button>

<script>
function handleSubmit() {
  const button = document.getElementById('submit-button');

  // Show loading state
  button.disabled = true;
  button.innerHTML = '<span class="spinner"></span> Submitting...';

  // Simulate API call
  setTimeout(() => {
    // Show success state
    button.innerHTML = '✓ Submitted!';
    button.classList.add('success');

    // Reset after 2 seconds
    setTimeout(() => {
      button.disabled = false;
      button.innerHTML = 'Submit';
      button.classList.remove('success');
    }, 2000);
  }, 1000);
}
</script>

<style>
.spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid #f3f3f3;
  border-top: 2px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.success {
  background-color: #2ecc71 !important;
  color: white !important;
}
</style>
```

**Timeline:** Fix before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - UI friction

---

#### Fix #12: Increase White Space for Working

**Issue:** Geometry problems have insufficient white space for working.

**Found By:** Brianna, Dylan

**Solution:**
```css
/* Increase white space for working */
.problem-working-space {
  min-height: 300px; /* Increased from 200px */
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

/* For geometry problems specifically */
.geometry-problem .problem-working-space {
  min-height: 400px; /* Even more space for diagrams */
}

/* Ensure adequate margins */
.problem-content {
  margin-bottom: 30px; /* Increased from 15px */
}

.diagram-container {
  margin: 20px 0;
}
```

**Timeline:** Fix before Week 1 baseline test (2026-04-22)

**Priority:** ⚠️ MEDIUM - Layout issue

---

#### Fix #13: Implement Simplified Feedback Option

**Issue:** Feedback is too verbose and complex for struggling students; no simplified option.

**Found By:** Dylan, Grace, Liam

**Solution:**
```javascript
// Feedback simplification system
class FeedbackSimplifier {
  simplify(feedback, studentLevel) {
    if (studentLevel === 'struggling') {
      return this.generateSimpleFeedback(feedback);
    }
    return feedback;
  }

  generateSimpleFeedback(feedback) {
    const simple = {
      pathway: this.simplifyPathwayFeedback(feedback.pathway),
      articulation: this.simplifyArticulationFeedback(feedback.articulation),
      solution: this.simplifySolutionFeedback(feedback.solution)
    };
    return simple;
  }

  simplifyPathwayFeedback(pathwayFeedback) {
    // Replace complex terms with simple language
    let simplified = pathwayFeedback;

    simplified = simplified.replace(/sequential changes/g, 'two changes');
    simplified = simplified.replace(/backward solving/g, 'working backwards');
    simplified = simplified.replace(/two-stage/g, 'two step');

    return simplified.substring(0, 200) + "..."; // Limit length
  }

  simplifyArticulationFeedback(articulationFeedback) {
    // Provide simpler, shorter feedback
    const simpleVersions = {
      'EXEMPLARY': 'Great job! Your explanation is perfect.',
      'EXCELLENT': 'Very good! Clear and correct.',
      'ADEQUATE': 'Good! Try to be more specific.',
      'VAGUE': 'Need more details. What numbers or fractions?',
      'MINIMAL': 'Too short. Explain more.',
      'MISSING': 'Please write something here.'
    };

    return simpleVersions[articulationFeedback.level] || articulationFeedback.message;
  }

  simplifySolutionFeedback(solutionFeedback) {
    if (solutionFeedback.isCorrect) {
      return 'Correct! Great work.';
    } else {
      return 'Not correct. Check your math and try again.';
    }
  }
}

// Adaptive feedback based on student performance
function generateAdaptiveFeedback(studentId, feedback, problemData) {
  const studentLevel = assessStudentLevel(studentId);

  if (studentLevel === 'struggling') {
    return FeedbackSimplifier.simplify(feedback, 'struggling');
  } else {
    return feedback; // Full feedback for advanced students
  }
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - Pedagogical improvement

---

#### Fix #14: Add Time Management Guidance

**Issue:** Students can spend 15+ minutes on single problems; no timeout or guidance.

**Found By:** Eve

**Solution:**
```javascript
// Time management system
class TimeManager {
  constructor(maxTimePerProblem = 600) { // 10 minutes max
    this.maxTime = maxTimePerProblem;
    this.warningTime = maxTimePerProblem * 0.7; // Warning at 70%
    this.timer = null;
    this.timeSpent = 0;
  }

  startTimer() {
    this.timeSpent = 0;
    this.timer = setInterval(() => {
      this.timeSpent++;
      this.updateDisplay();

      if (this.timeSpent === this.warningTime) {
        this.showWarning();
      }

      if (this.timeSpent >= this.maxTime) {
        this.showTimeout();
        this.stopTimer();
      }
    }, 1000);
  }

  stopTimer() {
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
  }

  updateDisplay() {
    const minutes = Math.floor(this.timeSpent / 60);
    const seconds = this.timeSpent % 60;
    const timeDisplay = document.getElementById('time-display');
    timeDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
  }

  showWarning() {
    const warning = document.getElementById('time-warning');
    warning.textContent = `⚠️ You've spent ${Math.floor(this.warningTime / 60)} minutes on this problem. Consider asking for help if you're stuck.`;
    warning.style.display = 'block';
  }

  showTimeout() {
    const timeout = document.getElementById('time-timeout');
    timeout.textContent = `⏱️ You've spent the maximum time (${Math.floor(this.maxTime / 60)} minutes) on this problem. Would you like to: 1) Continue working, 2) Skip to next problem, or 3) Get a hint?`;
    timeout.style.display = 'block';
    this.showOptions();
  }

  showOptions() {
    const options = [
      { text: 'Continue working', action: () => this.continueWorking() },
      { text: 'Skip to next problem', action: () => this.skipProblem() },
      { text: 'Get a hint', action: () => this.showHint() }
    ];

    // Show option buttons
    const container = document.getElementById('timeout-options');
    container.innerHTML = '';
    options.forEach(opt => {
      const button = document.createElement('button');
      button.textContent = opt.text;
      button.onclick = opt.action;
      container.appendChild(button);
    });
    container.style.display = 'block';
  }

  continueWorking() {
    document.getElementById('time-timeout').style.display = 'none';
    document.getElementById('timeout-options').style.display = 'none';
    // Continue without time limit
  }

  skipProblem() {
    document.getElementById('time-timeout').style.display = 'none';
    document.getElementById('timeout-options').style.display = 'none';
    // Skip to next problem
    loadNextProblem();
  }

  showHint() {
    document.getElementById('time-timeout').style.display = 'none';
    document.getElementById('timeout-options').style.display = 'none';
    // Show hint for current problem
    showHintForProblem();
  }
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - Time management support

---

#### Fix #15: Add Confidence-Building Language to Feedback

**Issue:** Feedback lacks positive reinforcement for anxious students.

**Found By:** Henry

**Solution:**
```javascript
// Confidence-building feedback system
class ConfidenceBuilder {
  addEncouragement(feedback, studentProgress) {
    const encouragement = this.generateEncouragement(studentProgress);

    feedback.encouragement = encouragement;
    feedback.overallTone = this.determineTone(studentProgress);

    return feedback;
  }

  generateEncouragement(progress) {
    if (progress.improvement > 20) {
      return "Fantastic progress! You're improving rapidly!";
    } else if (progress.improvement > 10) {
      return "Great work! Keep it up!";
    } else if (progress.improvement > 5) {
      return "Good effort! You're making steady progress.";
    } else if (progress.streak >= 3) {
      return "Nice streak! You're on a roll!";
    } else if (progress.accuracy > 80) {
      return "Excellent accuracy! You're really understanding this.";
    } else {
      return "Keep trying! Every problem helps you learn.";
    }
  }

  determineTone(progress) {
    if (progress.improvement > 15 || progress.accuracy > 85) {
      return 'enthusiastic';
    } else if (progress.improvement > 5 || progress.accuracy > 70) {
      return 'supportive';
    } else {
      return 'gentle';
    }
  }
}

// Example usage
function generateFeedbackWithEncouragement(studentId, articulation, solution, problemData) {
  const baseFeedback = generateBaseFeedback(articulation, solution, problemData);
  const progress = getStudentProgress(studentId);

  const enhancedFeedback = ConfidenceBuilder.addEncouragement(baseFeedback, progress);

  return enhancedFeedback;
}

// Feedback with tone
function formatFeedbackWithTone(feedback, tone) {
  const toneModifiers = {
    enthusiastic: {
      intro: "🎉 Wow! ",
      correct: "🟢 Perfect! ",
      encouragement: "💪 "
    },
    supportive: {
      intro: "👍 Good! ",
      correct: "✅ Correct! ",
      encouragement: "🌟 "
    },
    gentle: {
      intro: "Okay. ",
      correct: "Right. ",
      encouragement: "💚 "
    }
  };

  const modifier = toneModifiers[tone] || toneModifiers.supportive;

  return {
    ...feedback,
    intro: modifier.intro + feedback.intro,
    correct: modifier.correct + feedback.correct,
    encouragement: modifier.encouragement + feedback.encouragement
  };
}
```

**Timeline:** Implement before Week 2 (2026-04-25)

**Priority:** ⚠️ MEDIUM - Anxiety management

---

### 5.3 Low Priority Fixes (Nice-to-Have) - CAN FIX AFTER WEEK 2 IF TIME PERMITS

#### Fix #16: Fix Page Break Layout Issues

**Issue:** Some page breaks split question text from diagram, causing confusion.

**Found By:** Ivy, Brianna

**Solution:** Adjust PDF generation to keep question text and diagrams together (use CSS page-break-inside: avoid or manual page break placement).

**Timeline:** Fix if time permits (after Week 2)

**Priority:** 🟢 LOW - Layout improvement

---

#### Fix #17: Standardize Font Usage

**Issue:** Some questions use different fonts than others.

**Found By:** Ivy

**Solution:** Create consistent font stylesheet and apply to all questions.

**Timeline:** Fix if time permits (after Week 2)

**Priority:** 🟢 LOW - Visual consistency

---

#### Fix #18: Add Pathway Type Definitions

**Issue:** Students don't understand pathway type names; no definitions provided.

**Found By:** Eve, Grace, Liam

**Solution:** Add pathway type definitions with examples to help section or intro screen.

**Timeline:** Add if time permits (after Week 2)

**Priority:** 🟢 LOW - Educational improvement

---

#### Fix #19: Implement Gamification Elements

**Issue:** No streak counter, badges, or achievements to maintain motivation.

**Found By:** Cameron

**Solution:** Add simple gamification (streak counter, achievements for milestones).

**Timeline:** Add if time permits (Priority 3 enhancement)

**Priority:** 🟢 LOW - Motivation improvement

---

#### Fix #20: Add Question Variety to Reduce Repetition

**Issue:** Practice problems become repetitive, causing boredom.

**Found By:** Cameron

**Solution:** Increase question bank and randomize selection within pathways.

**Timeline:** Add if time permits (after Week 2)

**Priority:** 🟢 LOW - Engagement improvement

---

## 6. Test Execution Guide

### 6.1 Pre-UAT Preparation Checklist

- [ ] Fix all High Priority issues (Fixes #1-8)
- [ ] Verify all diagrams are proportional (deviation < 5%)
- [ ] Test OCR pipeline with sample scans
- [ ] Validate forced articulation validation
- [ ] Test gaming detection system
- [ ] Verify vocabulary support system
- [ ] Test cross-thread collision detection
- [ ] Validate calculation consistency checking
- [ ] Test timer display fix
- [ ] Test expandable feedback text
- [ ] Test submit button loading state
- [ ] Verify white space for working
- [ ] Test simplified feedback option
- [ ] Test time management guidance
- [ ] Verify confidence-building language

### 6.2 Test Execution Procedure

#### Phase 1: Week 1 - Baseline Test (Day 1)
1. Print baseline test PDF
2. Verify all 40 questions are present
3. Check all diagrams render correctly
4. Verify question-text consistency (no visual mismatches)
5. Check page breaks (no text-diagram separation)
6. Verify white space for working is adequate

#### Phase 2: Week 1 - Baseline Scan Upload (Day 1)
1. Upload completed baseline test scan
2. Verify OCR completes within 30 seconds
3. Check OCR accuracy (≥70% confidence)
4. Verify gap map generation
5. Check gap map visualization (radar chart sectors sum to 100%)
6. Verify 3 weakest pathways identified correctly

#### Phase 3: Week 2-4 - Training Intervention (Days 2-4)
1. Test pathway radar warm-up
   - Verify 10 questions load correctly
   - Check timer starts at 00:00 and counts down
   - Verify timer resets immediately upon submit
   - Check feedback displays correctly
   - Test gaming detection (attempt random clicking)
2. Test daily practice sessions
   - Verify forced articulation validation
   - Check empty field rejection
   - Test gibberish input rejection
   - Verify calculation consistency checking
   - Check triad feedback displays correctly
   - Test model articulation expansion
   - Verify canvas tool functionality
   - Test time management warnings
   - Check simplified feedback option
   - Test vocabulary tooltips
3. Test progress dashboard
   - Verify milestone tracking updates
   - Check accuracy trend displays
   - Test articulation level trend
   - Verify radar chart visualization
4. Test cross-thread collision detection (Week 3)
   - Verify detection identifies confused pathways
   - Check contrast drill generation
   - Test side-by-side comparison display

#### Phase 4: Week 5 - Transfer Test (Day 5)
1. Print transfer test PDF
2. Verify all 40 questions are present (20 trained + 20 held-back)
3. Check all diagrams render correctly
4. Verify no repetition from baseline test

#### Phase 5: Week 5 - Transfer Scan Upload & Ramp-Up Analytics (Day 5)
1. Upload completed transfer test scan
2. Verify OCR completes within 30 seconds
3. Check OCR accuracy (≥70% confidence)
4. Verify ramp-up analytics generation
5. Check all 5 success criteria are displayed
6. Verify success criteria targets are met (or not)
7. Test ramp-up analytics chart responsiveness

### 6.3 Bug Reporting Template

```markdown
## Bug Report

**Title:** [Brief description]

**Severity:** 🔴 CRITICAL / ⚠️ MEDIUM / 🟢 LOW

**Found By:** [Student persona name]

**Phase:** [Week 1 Baseline / Week 2-4 Training / Week 5 Transfer]

**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Behavior:** [What should happen]

**Actual Behavior:** [What actually happens]

**Screenshots:** [If applicable]

**Impact:** [How does this affect the MVP?]

**Recommended Fix:** [Suggested solution]
```

### 6.4 Success Criteria Validation

For each success criterion, verify:

| Criterion | Target | Measurement | Pass/Fail |
|-----------|--------|-------------|-----------|
| Pathway identification accuracy (trained) | ≥ 90% | Week 5 transfer test | ☐ Pass / ☐ Fail |
| Articulation Level 2+ rate (trained) | ≥ 90% | Week 5 transfer test | ☐ Pass / ☐ Fail |
| Solving improvement (trained) | ≥ 80% | Week 5 vs Week 1 | ☐ Pass / ☐ Fail |
| Transfer accuracy (trained, first 3 items) | ≥ 80% | Week 5 transfer test | ☐ Pass / ☐ Fail |
| Transfer accuracy (held-back) | ≥ 50% | Week 5 transfer test | ☐ Pass / ☐ Fail |

---

## 7. Appendix

### 7.1 Persona Summary Table

| Persona | Age | Baseline | Engagement | Key Struggles | Key Findings |
|---------|-----|----------|------------|---------------|--------------|
| Alex | 12 | 95%+ | Very High | None (perfect student) | Minor UI bugs only |
| Brianna | 11 | 85% | High | Visual diagrams, articulation quality | 1 critical visual inconsistency |
| Cameron | 12 | 75% | Average | Disengagement, skipping articulation | Validation failure (allows empty fields) |
| Dylan | 12 | 65% | Low-Medium | Complex concepts, gaming attempts | Multiple validation/gaming bugs |
| Eve | 11 | 50% | Low | Everything (completely mismatched) | Terminology, vocabulary, validation bugs |
| Fay | 12 | 40% | Very Low | Everything (zero engagement) | Gaming detection, validation bugs |
| Grace | 12 | 55% | Medium | Pathway confusion, needs scaffolding | Feedback clarity, cross-thread collision |
| Henry | 12 | 60% | Medium | Anxiety, over-articulation | Validation (calculation discrepancy) |
| Ivy | 12 | 70% | High | Visual inconsistencies (picky) | 12 visual inconsistencies found |
| Jack | 12 | Varies | Low (gamer) | Everything (games the system) | Gaming detection, validation bugs |
| Kevin | 12 | 80% | High | Abstract articulation (visual learner) | Canvas tool limitations |
| Liam | 12 | 60% | Medium | Reading comprehension, vocabulary | Vocabulary gap, feedback complexity |

### 7.2 Bug Count Summary

**By Severity:**
- 🔴 CRITICAL: 8 issues
- ⚠️ MEDIUM: 15 issues
- 🟢 LOW: 10 issues
- **Total:** 33 issues

**By Type:**
- Validation: 3 issues
- Visual Inconsistency: 12 issues
- Gaming Detection: 2 issues
- Vocabulary/Terminology: 4 issues
- UI Friction: 6 issues
- Pedagogical: 8 issues

**By Persona:**
- Ivy: 15 issues (most - visual inconsistencies)
- Jack: 7 issues (gaming detection, validation)
- Dylan: 6 issues (validation, gaming, vocabulary)
- Eve: 5 issues (terminology, vocabulary, validation)
- Fay: 4 issues (gaming detection, validation)
- Cameron: 3 issues (validation, engagement)
- Grace: 3 issues (feedback, scaffolding)
- Henry: 3 issues (validation, anxiety)
- Brianna: 3 issues (visual inconsistency, UI)
- Kevin: 3 issues (canvas tool, visual support)
- Liam: 3 issues (vocabulary, feedback)
- Alex: 2 issues (minor UI bugs)

### 7.3 Fix Priority Matrix

| Priority | Issues | Timeline | Owner |
|----------|---------|----------|-------|
| **P0 (Critical - Block UAT)** | Fixes #1-8 | Before Week 1 (2026-04-22) | MvpBot + BackendBot |
| **P1 (High - Friction)** | Fixes #9-15 | Before Week 2 (2026-04-25) | Logistics Bureau |
| **P2 (Medium - Nice-to-Have)** | Fixes #16-20 | After Week 2 (if time) | Logistics Bureau |

### 7.4 Test Timeline

| Phase | Dates | Duration | Test Focus |
|-------|-------|----------|------------|
| **Preparation** | 2026-04-15 to 2026-04-20 | 6 days | Fix critical issues, prepare test materials |
| **Phase 1 (Baseline)** | 2026-04-19 to 2026-04-25 | 7 days | Week 1 baseline test, scan upload, gap map |
| **Phase 2 (Training)** | 2026-04-26 to 2026-05-16 | 21 days | Weeks 2-4 training intervention |
| **Phase 3 (Transfer)** | 2026-05-17 to 2026-05-23 | 7 days | Week 5 transfer test, ramp-up analytics |
| **Total** | 2026-04-15 to 2026-05-23 | 39 days | Full UAT cycle |

### 7.5 Glossary

**Pathway:** Problem-solving approach type (e.g., Before-After Change, Part-Whole with Comparison).

**Equation Shadow:** Student's articulation of the problem-solving framework in their own words.

**Triad Feedback:** Three-dimensional feedback on pathway identification, articulation, and solution.

**Pathway Radar:** 5-minute warm-up drill with 10 mixed pathway identification questions.

**Cross-Thread Collision:** When student confuses similar pathways (e.g., Before-After vs. Part-Whole).

**Red Herring:** Distractor data in charts/graphs that students must ignore.

**Proportional Rendering:** Diagrams drawn to accurate scale (e.g., bar lengths proportional to values).

**Gap Map:** Analysis showing weakest pathways from baseline test.

**Ramp-Up Metrics:** Comparison of baseline vs. transfer test performance.

**Articulation Level:**
- **Level 0:** Missing, minimal, or gibberish
- **Level 1:** Vague or descriptive (what is seen)
- **Level 2:** Adequate (basic understanding)
- **Level 3:** Exemplary (clear, precise, mathematically accurate)

---

**Document Status:** ✅ Complete

**Next Steps:**
1. Review this test plan with Sean Foo
2. Prioritize fixes based on severity
3. Implement P0 (Critical) fixes before Week 1
4. Execute UAT following test execution guide
5. Document all bugs found during UAT
6. Generate UAT report after Week 5 completion

**Contact:** Test Plan Developer (Subagent) for questions about test scenarios

---

*Last updated: 2026-04-15 09:10 SGT*
