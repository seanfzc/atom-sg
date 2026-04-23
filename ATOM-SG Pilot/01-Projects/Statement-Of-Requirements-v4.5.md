---
title: Statement of Requirements (C0) – Pilot v4.5 (Revised with Independent Critique)
objective: Prove end-to-end pipeline with 4 questions, test with Zeth (real child), measure learning not plumbing.
status: draft — revised after independent critique from Claude + Grok
owner: Zcaethbot → Sean Foo (approval pending)
last_updated: 2026-04-21
directive_source: OPENCLAW DIRECTIVE – PILOT v4.1 (Recognition-First Integrated Training)
quality_standard: Reconstructed questions must be SOLVABLE — a student using only the reconstruction arrives at the same answer as the original.
---

# Statement of Requirements – ATOM-SG Pilot v4.5

## Executive Summary

**This SOR proves pipeline end-to-end with 4 questions, tested with 1 real child (Zeth), measuring whether forced identification + articulation improves solving.**

**Changes from v4.4 (based on independent critique):**
1. **12 personas dropped.** Replaced with Zeth + optionally 2-3 friends' kids. AI personas are not real testing.
2. **Timeline doubled.** 15 days → 28 days. Each stage gets realistic time.
3. **Success criteria reframed.** Stages 1-2 measure system quality. Stages 3-5 measure LEARNING.
4. **Quality metric changed.** "≤3% pixel deviation" → "solvability test" (can a student get correct answer from reconstruction?).
5. **Pedagogy section added.** What Zeth actually sees on screen, session-by-session.
6. **Fallback plan added.** What happens if Vision LLM pipeline fails.
7. **Articulation rubric defined.** Concrete examples per pathway per level.
8. **4th question changed.** One geometry question swapped for Cross-Thread Collision (the #1 pathway).
9. **Intervention stage fully specified.** No more "provide daily practice problems" hand-waving.

**Root Cause (unchanged from v4.4):**
> "We deconstructed exam data outside of OpenClaw and this resulted in reconstruction deficits. We have no choice but to do it internally."

---

## 1. Taking Stock — What Do We Have?

*Unchanged from v4.4. All internal assets (28 problem cards, 25 geometry problems, 20 word problems, taxonomy, rubrics, backend, frontend, 90 Playwright tests, OCR pipeline, Vision LLM docs) are retained.*

*External data (5 exam PDFs, extracted images) kept as source inputs. External markdown kept as reference insights only, not as structural data.*

---

## 2. Focused Scope — 4 Questions

### 2.1 Question Selection (Revised)

| # | Type | Why Selected | Source |
|---|------|-------------|--------|
| 1 | **Complex Geometry (Composite Overlap)** | Tests visual reconstruction fidelity — overlapping shapes, shaded regions, area/perimeter calculation | Select from ACS Q15 or Nanyang Q17 |
| 2 | **Complex Geometry (Isometric 3D)** | Tests 3D rendering — cube structures, orthographic projection | Select from ACS Q5 or Nanyang Q19 |
| 3 | **Cross-Thread Collision (Word Problem)** | Tests #1 pathway (12.8% of exam). Fuses ratio + fraction + before-after. | Select from ACS Q16, NH Q7, or RGPS Q11 |
| 4 | **Data Interpretation (Line Graph)** | Tests graph reconstruction + data extraction + reverse percentage | Select from ACS Q10 or Nanyang Q16 |

**Change from v4.4:** Replaced "Complex Bar Model Word Problem (Before-After Change)" with Cross-Thread Collision. XT is the most frequent pathway at 12.8%. BA is only 5.3%. Testing the most common pathway first gives the most representative data.

### 2.2 Why 4 Questions

- Proves full pipeline: Scan → Deconstruct → Reconstruct → Test → Teach → Transfer
- Small enough to iterate quickly (days, not weeks)
- Covers both tracks: Geometry (2 questions) + Word Problems (1 XT + 1 DI)
- Can pivot on individual questions without restarting everything

---

## 3. Stage 0: Smoke Test (Before Anything Else)

**Objective:** Verify Vision LLM pipeline works on ONE real exam question before committing to 4-question plan.

**Task:** Pick the simplest of the 4 selected questions (likely the line graph). Run it through the full pipeline: PDF → OCR → VLM extraction → OpenCV analysis → YAML output → rendered reconstruction.

**Success criterion:** The reconstructed question is SOLVABLE — a person looking at only the reconstruction gets the same answer as the original.

**Timeline:** 1-2 days.

**If it passes:** Proceed to Stage 1 with confidence.

**If it fails:** STOP. Diagnose what broke (OCR accuracy? VLM hallucination? rendering errors?). Determine whether the pipeline can be fixed in <3 days or whether you need a fallback approach:

### Fallback Plan (If Vision LLM Pipeline Fails)

| Severity | Symptom | Fallback |
|----------|---------|----------|
| **OCR fails on diagram text** | Labels/dimensions not extracted | Manual annotation of YAML labels only (keep automated shape extraction) |
| **VLM hallucinates shapes** | Extra shapes or wrong relationships | Use OpenCV geometric analysis as primary, VLM as secondary verification |
| **Rendering fails on composites** | Overlapping shapes render incorrectly | Simplify to non-overlapping geometry for pilot, defer composites to v2 |
| **Entire pipeline unreliable** | Multiple failures across questions | Fall back to hand-authored YAML using visual specifications already extracted (ACS/Nanyang appendices). This is slower but proven to be accurate. |

---

## 4. Process Stages

### Stage 1: Deconstruction (3-5 days)

**Objective:** Convert 4 exam questions from PDF to internal, structured YAML.

**Tasks:**
1. Run Vision LLM 3-layer pipeline (OCR + VLM + OpenCV) on each question
2. Generate tagged YAML with confidence scores
3. Verify reconstruction by SOLVABILITY TEST (not pixel comparison)

**Success Criteria:**
- 4 questions converted to YAML with all structural data (shapes, relationships, dimensions, text)
- Confidence scores ≥0.7 average on critical fields
- **Solvability test PASSES for all 4** — a human (Sean) or competent LLM solves each reconstructed question and gets the correct answer

**What "solvable" means precisely:**
- All shapes present with correct spatial relationships
- All dimensions/angles labeled correctly
- All question text complete and unambiguous
- The correct answer is derivable from ONLY reconstruction (no reference to original needed)

**Exit:** All 4 pass solvability test → proceed to Stage 2.
**Block:** Any question fails solvability → fix pipeline or apply fallback, re-test.

---

### Stage 2: Baseline PDF Generation (2-3 days)

**Objective:** Render a printable 4-question baseline test from YAML.

**Tasks:**
1. Apply rendering gates and label rules from Vision LLM documentation
2. Generate PDF with inline visuals
3. Verify rendering quality through solvability (not pixel precision)

**Success Criteria:**
- 4 questions rendered in a clean, printable PDF
- All visuals are clear enough for an 11-year-old to interpret without confusion
- Labels don't overlap shapes or each other
- PDF prints correctly on A4

**Exit:** PDF passes visual review by Sean → proceed to Stage 3.
**Block:** Rendering issues → fix and regenerate.

---

### Stage 3: Baseline Test with Zeth (1 day)

**Objective:** Establish Zeth's current performance on 4 questions BEFORE any intervention.

**Who:** Zeth. One real child. Not 12 simulated personas.

**Optionally:** If 2-3 friends' kids are available and willing, include them for diversity. But Zeth alone is sufficient for the pilot.

**Administration Protocol:**
- Zeth works on paper (printed PDF from Stage 2), in exam conditions
- No hints, no teaching, no discussion
- Sean observes silently and records:

| Data Point | How to Record |
|------------|--------------|
| Correct/Incorrect per question | Check against answer key |
| Time per question | Stopwatch |
| Where he got stuck | Observe: pencil stops, re-reads question, draws wrong model, gives up |
| Error type | Setup Error (wrong approach), Trap Error (fell for examiner trick), Execution Error (right approach, arithmetic mistake), No Attempt |
| What he drew | Photograph his working |
| What he said | Note any verbal comments ("I don't understand this", "is this a ratio question?") |

**This is NOT a UX test.** It's a learning baseline. Expect Zeth to struggle. Low scores are GOOD — they prove there's something to teach.

**Success Criteria:**
- Zeth completes all 4 questions (even if wrong)
- Sean has a complete data record for each question
- Gap map is clear: which question types Zeth can/can't do

**Exit:** Baseline data collected → proceed to Stage 4.
**Block:** Zeth refuses to engage or finds paper test format unusable → address motivation before proceeding.

---

### Stage 4: Intervention — What Zeth Actually Experiences (7-10 days)

**Objective:** Teach Zeth to identify the pathway type, articulate the equation shadow, and solve — in that order, integrated into each problem.

#### 4.1 What Zeth Sees On Screen

**Screen Layout (per problem):**

```
┌──────────────────────────────────────────────────┐
│  QUESTION                                         │
│  [Rendered diagram + question text]               │
│                                                    │
├──────────────────────────────────────────────────┤
│  STEP 1: IDENTIFY                                 │
│  "What type of problem is this?"                  │
│  [ Dropdown: XT / PW / BA / DI / Geometry ]       │
│                                                    │
├──────────────────────────────────────────────────┤
│  STEP 2: ARTICULATE                               │
│  "Explain hidden structure in your own words"  │
│  [ Text box — minimum 15 characters ]             │
│                                                    │
├──────────────────────────────────────────────────┤
│  STEP 3: SOLVE                                    │
│  "What is answer?"                            │
│  [ Answer box ]                                    │
│                                                    │
├──────────────────────────────────────────────────┤
│  [ Submit ]                                        │
└──────────────────────────────────────────────────┘
```

**After submission, Zeth sees FEEDBACK:**

```
┌──────────────────────────────────────────────────┐
│  FEEDBACK                                          │
│                                                    │
│  Pathway: ✅ Correct — this IS Cross-Thread        │
│           Collision (ratio + fraction combined)    │
│                                                    │
│  Articulation: 🟡 Level 1 — you said "there are   │
│  two things mixed together." Good start! Can you   │
│  say WHICH two things are mixed and HOW they       │
│  connect? For example: "The ratio links        │
│  two groups, and the fraction tells me how much    │
│  of each group changed."                           │
│                                                    │
│  Answer: ❌ Not quite. Your approach was right      │
│  but you multiplied instead of dividing at step 3. │
│  Here's the equation shadow:                       │
│  [Bar model diagram showing the structure]         │
│                                                    │
│  [ Try Similar Problem ] [ Next Problem ]          │
└──────────────────────────────────────────────────┘
```

#### 4.2 Articulation Rubric (Concrete Examples)

**Cross-Thread Collision:**

| Level | What Zeth Says | Score |
|-------|---------------|-------|
| **Level 0** | "I don't know" or blank | 0 |
| **Level 1** | "There are two math topics mixed together" | 1 — recognises collision exists |
| **Level 2** | "The ratio and the fraction both connect to the same unknown" | 2 — identifies the link |
| **Level 3** | "If I make the ratio units match, I can use the fraction to find one unit, then multiply to get the total" | 3 — describes solution path |

**Part-Whole with Comparison:**

| Level | What Zeth Says | Score |
|-------|---------------|-------|
| **Level 0** | Blank or irrelevant | 0 |
| **Level 1** | "I need to find a part from the whole" | 1 |
| **Level 2** | "The ratio tells me how many units each part has, and the total or difference lets me find one unit" | 2 |
| **Level 3** | "3 units = difference of 120, so 1 unit = 40, and the answer is 5 units = 200" | 3 |

**Data Interpretation:**

| Level | What Zeth Says | Score |
|-------|---------------|-------|
| **Level 0** | Blank | 0 |
| **Level 1** | "I need to read the graph" | 1 |
| **Level 2** | "The graph shows bags LEFT, not bags sold. I need to subtract to find daily sales" | 2 — identifies meaning transformation |
| **Level 3** | "Day 3 sold 16 bags (76-60=16). Revenue = 16 × $12. But $12 is 80% of the original, so original = $12 ÷ 0.8 = $15" | 3 — traces full calculation chain |

**Geometry (Angle Chasing):**

| Level | What Zeth Says | Score |
|-------|---------------|-------|
| **Level 0** | Blank | 0 |
| **Level 1** | "I need to find an angle" | 1 |
| **Level 2** | "This is a rhombus so opposite angles are equal, and it's connected to a rectangle so I know one angle is 90°" | 2 — identifies properties needed |
| **Level 3** | "∠VRS = 256° (reflex), so ∠VRQ = 360° − 256° − 90° = 14°. Then ∠QRT = 180° − 122° − 14° = 44° [reason: ∠s in △]" | 3 — executes property chain with labels |

#### 4.3 Session Structure (Per Day, ~30 min)

**Day 1-2: Pathway Recognition Focus**
- Show 3 problems from different pathways (1 XT, 1 Geometry, 1 DI)
- Zeth only does Step 1 (Identify) and Step 2 (Articulate). NO solving yet.
- Feedback focuses entirely on recognition: "Good — you spotted the ratio. But did you also see the fraction? That's what makes this Cross-Thread, not just Part-Whole."
- Purpose: Build identification muscle without cognitive overload from solving

**Day 3-5: Identification + Solving Integrated**
- Show 3 problems. Zeth does all 3 steps (Identify → Articulate → Solve).
- Ratio shifts from 70% identification focus to 50/50.
- Feedback covers all three axes.
- If Zeth identifies correctly but solves wrong: focus on execution.
- If Zeth identifies wrong: go back to recognition teaching for that pathway.

**Day 6-8: Difficulty Ramp**
- Same 3-step flow but problems increase in difficulty (Standard → Hard → Adversarial)
- Introduce traps: "The examiner used a Referent Switch here — 'remainder' changed what it referred to mid-problem"
- For geometry: introduce VSS 3-4 problems (overlapping shapes, property chaining across shared edges)

**Day 9-10: Mixed Practice**
- 4 problems mixing all types, no type labels, Zeth must identify cold
- Timed at near-PSLE pace
- This is dress rehearsal for the transfer test

#### 4.4 What Data Is Recorded Per Problem

| Field | Values |
|-------|--------|
| Pathway identification | Correct / Incorrect + what he chose |
| Articulation text | Raw text, scored Level 0-3 |
| Answer | Correct / Incorrect |
| Error type (if wrong) | Setup / Trap / Execution / No Attempt |
| Time | Seconds |
| Attempt number | 1st, 2nd (if retry) |
| Session number | Day 1-10 |

#### 4.5 Socratic Feedback Logic (For AI Tutor)

| Scenario | What the AI Says | What it Does NOT Say |
|----------|-----------------|---------------------|
| **Identification correct, articulation Level 0-1, answer wrong** | "You spotted the right type! Your explanation needs more detail — try naming the specific relationship. Here's a hint: what stays constant while other things change?" | Does NOT reveal the answer. Does NOT give a full articulation. |
| **Identification correct, articulation Level 2+, answer wrong** | "Your thinking is right! You set up the problem correctly. Check your arithmetic at step 3 — you wrote 5 × 24 = 100 but the correct multiplication is 120." | Does NOT re-explain the structure. Targets the specific execution error. |
| **Identification correct, articulation Level 2+, answer correct** | "Nailed it. The equation shadow is: [shows structure]. You saw that the ratio linked groups and the fraction revealed the unit. That's exactly how AL1 students think." | Reinforces the meta-skill, connects to the shadow concept. |
| **Identification wrong** | "Not quite — this looks like Part-Whole because you see a ratio and a total. But notice: BOTH a fraction AND a ratio are connecting to the same unknown. When two different topic rules link to the same thing, that's Cross-Thread Collision." | Does NOT shame. Explains the misidentification with a specific structural reason. |
| **Geometry: property chain incomplete** | "You used 'opposite angles in parallelogram' correctly. But you stopped one step too early. What else do you know about angles on a straight line?" | Nudges the next property in the chain without giving the full answer. |

**Maximum 3 attempts per problem.** After 3 wrong answers: reveal the full solution with the equation shadow / property chain, explain all traps, move on.

---

### Stage 5: Transfer Test (1 day)

**Objective:** Measure whether Zeth's identification and solving skills transfer to new problems of the same types.

**Method:** Generate 4 NEW problems — same pathway types as baseline, different contexts and numbers. Use YAML improvisation capability: modify parameters (side lengths, ratios, amounts) while keeping structural relationships intact.

**Administration:** Same protocol as Stage 3 baseline. Paper, timed, no hints, Sean observes.

**What's measured:**

| Metric | Baseline (Stage 3) | Transfer (Stage 5) | Target |
|--------|--------------------|--------------------|--------|
| Overall accuracy | Record | Record | Improvement ≥ 1 more correct |
| Pathway identification | Not measured (wasn't taught yet) | Measured: can Zeth name the type? | ≥ 3/4 correct |
| Articulation quality | Not measured | Measured: Level 0-3 per question | Average ≥ Level 2 |
| Time per question | Record | Record | ≥ 20% faster |
| Error type shift | Record | Record | Fewer Setup Errors (structure mistakes should decrease even if Execution Errors persist) |

**Success Criteria:**
- Zeth completes all 4 transfer questions
- Pathway identification ≥ 3/4 correct on trained types
- Average articulation ≥ Level 2
- At least 1 more question correct than baseline (e.g., baseline 1/4 → transfer 2/4)
- Setup Errors decrease (even if total errors don't decrease, the TYPE of error should shift from "wrong structure" to "right structure, arithmetic mistake")

**If optional additional kids participated:** Compare their results to Zeth's. Do they show similar patterns? This is anecdotal, not statistical — but interesting signal.

---

## 5. Quality Standard

### 5.1 Definition (Revised)

**Quality = Solvability.** A reconstructed question is "good enough" when a student using ONLY the reconstruction arrives at the same correct answer as the original.

This replaces the v4.4 "≤3% pixel deviation" metric. Reasons:
- Pixel precision doesn't guarantee mathematical correctness
- A slightly shifted diagram that is mathematically accurate is better than a pixel-perfect diagram with a wrong angle label
- Solvability is a functional test that matters for the pilot

### 5.2 How to Test Solvability

For each reconstructed question:
1. Give the reconstruction (diagram + text) to Sean WITHOUT showing the original
2. Sean solves it and records his answer
3. Compare to the known correct answer from the answer key
4. If the answer matches: PASS
5. If the answer doesn't match: analyze WHY (missing information? ambiguous diagram? wrong dimension?) and fix

### 5.3 Improvisation Standard

For transfer test questions (Stage 5):
- Each YAML file must specify which parameters are SAFE to modify (numbers, names, contexts)
- Each YAML file must specify which parameters are FIXED (structural relationships, number of shapes, angle type constraints)
- After modification, the new problem must pass the same solvability test
- Both visual and text information must be independently sufficient to solve

---

## 6. Geometry Track Decision

**Decision required:** Is Geometry a separate training track or integrated?

**Data:** Geometry is 32% of exam questions across 5 papers (30 out of 94 questions). The pilot includes 2 geometry questions out of 4 total (50% of pilot scope).

**For the pilot:** Geometry is treated as an integrated part of the same recognition-first flow:
- Step 1 (Identify): "This is a Geometry — Composite Overlap problem"
- Step 2 (Articulate): "There are two quarter circles sharing a centre point. The overlap area is given. I need to find the arc lengths plus the straight edges for the perimeter."
- Step 3 (Solve): Execute the property chain

**Geometry-specific additions:**
- Property labeling requirement: Zeth writes the reason next to every angle/calculation ("opp ∠s rhombus", "∠s on str line")
- For the 3D question: Zeth builds the structure with physical cubes BEFORE attempting the paper version (offline requirement, ~$5-10 for linking cubes)
- VSS (Visual Stress Score) governs difficulty scaling, not chain length

**Post-pilot decision:** If the pilot shows Geometry needs fundamentally different teaching (property chain vs equation shadow), bifurcate into a separate track. If the recognition-first flow works for both, keep integrated.

---

## 7. Playwright Usage (Clarified)

**Playwright IS useful for:**
- Technical smoke tests: "Does the forced articulation box appear?"
- Regression tests: "Does feedback render correctly after 33 bug fixes?"
- API integration tests: "Does the Claude API response parse correctly?"
- UI rendering: "Does the PDF generate without overflow?"

**Playwright is NOT useful for:**
- Simulating 12 children with different learning styles
- Discovering real UX issues (only a real child can do this)
- Testing pedagogical effectiveness

**Keep the existing 90 Playwright tests + 15 action verification tests.** Add the 23 domain-specific tests (problem generation quality, scoring logic, Socratic feedback, data persistence) from the earlier critique. Do NOT add persona simulation tests.

---

## 8. Decision Log (Lightweight)

Keep a simple Markdown file. No YAML ceremony.

```markdown
## Decision Log — ATOM-SG Pilot v4.5

### 2026-04-21: Revision from v4.4
- Dropped 12 personas → test with Zeth (1 real child)
- Changed quality metric from pixel deviation to solvability
- Added smoke test (Stage 0) before committing to full pipeline
- Added fallback plan if Vision LLM fails
- Swapped BA question for XT question (XT is #1 pathway at 12.8%)
- Doubled timeline to 28 days
- Added full intervention spec (screen layout, articulation rubric, session structure, feedback logic)
- Added geometry track decision point

### 2026-04-22: Stage 0 Finding 1 — Diagram vs Question Data Separation
- **Issue Identified:** YAML files were mixing diagram data with question/solution data
- **Problem:** Renderer doesn't know what to SHOW vs what to HIDE
- **Solution Applied:** Created `YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md` enforcing two clearly separated sections:
  1. `diagram_data:` — ONLY visual elements (shapes, labels, dimensions)
  2. `question:` / `solution:` / `answer_key:` — NEVER rendered
- **Updated Files:**
  - `00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md` — New schema with separation rules
  - `00-Templates/MATH_DIAGRAM_RENDERING_INSTRUCTION.md` — Updated with reference to schema
  - `topics/51-deconstruction-pipeline.md` — Updated with separation requirement
  - `topics/52-baseline-generation.md` — Updated with separation requirement
  - `topics/53-intervention.md` — Updated with separation requirement
  - `topics/54-qa-testing.md` — Updated with separation requirement
  - `01-Projects/Statement-Of-Requirements-v4.5.md` — This entry
- **Spirit Applied:** Iterating and improving (SOR v4.5 principle)
- **Validation:** All 4 existing YAML files (Q7, Q9, Q10, Q13) already have correct structure
- **Next Steps:** Apply this schema to all new YAML files created during Stages 1-5

### [Future entries go here]
```

---

## 9. Deliverables & Timeline (Revised — 28 days)

| Stage | Deliverable | Duration | Target Date | Dependencies |
|-------|-------------|----------|-------------|-------------|
| **0: Smoke Test** | 1 question through full pipeline | 2 days | Apr 23 | Vision LLM docs reviewed |
| **1: Deconstruction** | 4 questions → YAML | 5 days | Apr 28 | Smoke test passes |
| **2: Baseline PDF** | Printable 4-question test | 3 days | May 1 | Stage 1 passes solvability |
| **3: Baseline Test** | Zeth's baseline data | 1 day | May 2 | PDF printed, Zeth available |
| **4: Intervention** | 10 days of teaching sessions | 10 days | May 12 | Baseline data collected |
| **5: Transfer Test** | Transfer data + comparison | 1 day | May 13 | Intervention complete |
| **Launch Decision** | Sean reviews all data | 1 day | May 14 | All stages complete |
| **Buffer** | For pipeline failures, pivots | 5 days | May 19 | — |

**Total: 28 days (April 21 → May 19)**
**Hard deadline: Zeth's school schedule permitting**

---

## 10. Open Decisions

1. **v4.5 Approach Approval:** Is this revised approach correct? **Pending.**
2. **Question Selection:** Which specific 4 questions from the 5 exam papers? **Pending.** (Recommendation: ACS Q15 composite overlap, Nanyang Q19 isometric 3D, ACS Q16 erasers/pencils XT, ACS Q10 T-shirts line graph DI)
3. **Additional Test Subjects:** Can 2-3 friends' kids participate alongside Zeth? **Pending.** (Nice-to-have, not blocking.)
4. **Geometry Track:** Integrated or separate? **Deferred to post-pilot decision based on data.**
5. **Physical Cubes:** Has Sean purchased linking cubes for the 3D question? **Pending.**

---

## 11. What This Document Does NOT Cover (Explicitly Out of Scope)

- Scaling beyond 4 questions
- Building the full 128-node training set
- Automated baseline generation for multiple students
- Dashboard / parent-facing analytics
- Commercial positioning or pricing

These are all post-pilot decisions contingent on the pilot producing positive learning outcomes.

---

*This document supersedes SOR v4.4. Approval pending from Sean Foo.*
