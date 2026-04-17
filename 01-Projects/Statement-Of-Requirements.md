---
title: Statement of Requirements (C0) – Pilot v4.1
objective: Define the pilot project's objectives, scope, storylines, and tech stack implications for the Recognition‑First Integrated Training model.
status: approved — all open decisions resolved; ready for C3 (backend API spec) implementation
owner: MvpBot → Zcaethbot → Approved by Sean Foo
last_updated: 2026‑04‑15 06:05 SGT
approval_date: 2026‑04‑14 17:57 SGT
priority2_enhancement: Model articulations added to triad feedback (2026‑04‑15 06:05 SGT)
directive_source: OPENCLAW DIRECTIVE – PILOT v4.1 (Recognition‑First Integrated Training), 12 April 2026
data_source: 94 questions across 5 elite‑school prelim papers (ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS)
prerequisite_for: C3 (backend API spec), all downstream technical work
---

# Statement of Requirements – ATOM‑SG Pilot v4.1

## 1. Why We Are Here

After analysing **94 questions across 5 elite‑school prelim papers** (ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS), the data revealed:

| Track | Coverage | Key Pathways |
|-------|----------|-------------|
| **Word Problems** | 35.1% | Cross‑Thread Collision (12.8%), Part‑Whole with Comparison (10.6%), Data Interpretation (6.4%), Before‑After Change (5.3%) |
| **Geometry** | 31.9% | Angles, Area & Perimeter, Volume & 3D, Properties & Classification |
| **Combined** | 67% | Rising to 71.3% with Constant‑Total + Supposition variants |

The original 5‑pathway plan was too fragmented. The **real novelty** of ATOM‑SG is teaching the student to **identify the pathway type and articulate the equation shadow as the very first step of every problem**, then immediately apply it to solve. This meta‑skill is what creates the tipping point.

We are therefore pivoting to a **Recognition‑First Integrated Training** model.

## 2. Primary Objective

**Measure how fast a student can ramp up with targeted intervention training following a baseline diagnostic test.**

The key is understanding how we can make the intervention training **as powerful as possible** with ATOM‑G's unique methodology **without compromising over‑execution** — this is a pilot, not a production build. The methodology drives what we need from the tech stack, not the other way around.

## 3. Pilot Structure (5 Weeks)

### Week 1 — Baseline (Offline Paper Test)

The student takes a printed test covering **all 3 tracks**:

| Track | # Questions | Notes |
|-------|-------------|-------|
| Word Problems | 20 | Drawn from the 4 main pathways identified across 5 prelim papers |
| Geometry | 12 | Angles, area, volume, properties — aligned to existing nano‑nodes |
| Data Interpretation | 8 | Bar graphs, pie charts, tables with red‑herring data |
| **Total** | **40** | |

**Process:**
1. Student completes test on paper.
2. Parent scans the working (handwritten answers + working).
3. OpenClaw analyses the scan and returns a **gap map** showing the **3 weakest pathways** (across any track).

**Important:** Baseline has **no forced articulation** — we are measuring raw performance first.

### Weeks 2–4 — Integrated Intervention (Online MVP)

Train the **3 weakest pathways** identified from baseline (one per week).

Every problem follows this **exact loop**:

```
Student reads the question
        ↓
Forced Articulation (must type/write before solving):
  Pathway type: ________________
  Equation shadow (in your own words): ________________
        ↓
Student solves the problem
        ↓
Instant Triad‑based feedback on BOTH identification and solution
```

**Daily 5‑minute Pathway Radar warm‑up** (identification only, 10 mixed questions) builds pure recognition muscle.

### Week 5 — Transfer Test

- **40 new unseen problems** (trained + held‑back pathways) + geometry/DI transfer tests.
- Measures whether recognition skill transfers to pathways the student was *not* explicitly trained on.

## 4. Success Criteria

| Criterion | Target |
|-----------|--------|
| Pathway identification accuracy on trained pathways | ≥ 90% |
| Articulation quality reaches Level 2+ on | ≥ 90% of problems |
| Solving accuracy improvement from baseline on trained pathways | ≥ 80% |
| Transfer: identification accuracy on trained pathways | ≥ 80% (for first 3 items), ≥ 50% for held‑back pathways |

## 5. Storylines — From Wrong Answer to Mastery

### Storyline A: Word Problem — Cross‑Thread Collision

1. **The Question:** "A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday. It had 150 pens left. How many pens did it have at first?"
2. **Wrong Answer:** Student treats it as a simple fraction problem, ignoring the two‑stage change. Writes 150 ÷ (1 − 3/5 − 1/4) = wrong.
3. **Diagnosis (after baseline scan):** System maps this to **Before‑After Change** pathway. Error pattern: student did not recognise the sequential "remainder" structure — classic Cross‑Thread Collision trap (fraction language disguising a change pathway).
4. **Targeted Training UI/Flow:**
   - Student opens the day's intervention module.
   - **Forced articulation first:** "What pathway type is this?" → Student must type "Before‑After Change" before seeing any solving interface.
   - "Write the equation shadow in your own words" → Student types: "After first change, then after second change, find original."
   - **Solving phase:** Student works through the problem with the articulated framework visible.
   - **Instant Triad feedback:** Green (correct ID + correct solution), Yellow (correct ID but wrong solution), Red (wrong ID — re‑route to Pathway Radar).
5. **Retest (Week 5):** A new unseen Before‑After Change problem with different surface features. Student articulates pathway correctly and solves → ramp‑up measured.

### Storyline B: Geometry — Composite Shape Area

1. **The Question:** A composite figure made of a square and a ¾‑circle. Find the total area.
2. **Wrong Answer:** Student calculates full circle area instead of ¾, or misidentifies the square's side length as the diameter.
3. **Diagnosis:** System maps to **Area & Perimeter (Composite Shapes)** sub‑pathway. Gap: visual decomposition of overlapping regions.
4. **Targeted Training UI/Flow:**
   - Forced articulation: "Part‑Whole (Composite Shapes)" + "Total area = area of square + area of ¾ circle."
   - Interactive diagram where student shades each component before calculating.
   - Triad feedback on both the decomposition logic and the numerical answer.
5. **Retest:** New composite shape (different configuration) — student decomposes correctly → mastery confirmed.

### Storyline C: Data Interpretation — Red Herring

1. **The Question:** A bar graph shows sales for 5 products. Question asks about the difference between Product A and Product C, but Product D's bar is visually prominent and close to C.
2. **Wrong Answer:** Student reads Product D's value instead of C.
3. **Diagnosis:** System maps to **Data Interpretation — Red Herring** sub‑pathway. Gap: filtering irrelevant visual data.
4. **Targeted Training UI/Flow:**
   - Forced articulation: "Data Interpretation — comparison of two specific data points, ignore others."
   - "Data Filter" mini‑game: student must highlight only the relevant bars before answering.
   - Triad feedback on filter accuracy + numerical answer.
5. **Retest:** New chart with different red herring — student filters correctly → transfer confirmed.

## 6. What This Drives for Tech Stack & Software Build

### 6.1 What We Need (Minimum Viable)

| Component | Purpose | Priority |
|-----------|---------|----------|
| **Baseline test PDF generator** | Print 40‑question test with diagrams | Week 1 |
| **Scan upload & OCR pipeline** | Ingest scanned student answers | Week 1 end |
| **Gap map analyser** | Identify 3 weakest pathways from baseline | Week 1 end |
| **MVP online question display** | Show problems with forced articulation boxes + embedded visual diagrams (rendered from `exam.md` data). Technical constraint: Student may need to draw diagrams (bar models, graphs, angles, shapes) during training — UI should include drawing canvas/tool for this purpose. | Week 2 |
| **Forced articulation UI** | Pathway type + equation shadow input fields (must complete before solving) | Week 2 |
| **Triad feedback engine** | Instant feedback on identification + solution. **ENHANCEMENT: Include model articulations in response so students can compare their articulations against ideal ones (Priority 2 recommendation).** | Week 2 |
| **Pathway Radar warm‑up** | 5‑min, 10‑question identification‑only drill | Week 2 |
| **Radar chart visualization** | Visual radar chart showing pathway identification accuracy and trends over time (frontend-only enhancement using Chart.js/D3.js). **Recommendation from MVP-Backend Alignment (Priority 1, Low severity).** | Week 2+ |
| **Progress & milestone tracker** | Visual pathway mastery dashboard | Week 2 |
| **Transfer test generator** | 40 unseen problems (20 new + 20 held‑back) + geometry/DI transfer tests. | Week 5 |
| **Ramp‑up analytics** | Compare baseline → retest speed & accuracy | Week 5 |

### 6.2 What We Do NOT Need for Pilot

- Production‑grade infrastructure (cloud hosting, auth, multi‑user)
- Gamification engine beyond simple mini‑games
- Automated problem generation (we curate manually from prelim papers)
- Mobile app (web interface is sufficient)
- Student management system
- **MVP online question display with embedded visual diagrams** — System must render visual diagrams (bar models, pie charts, graphs, angles, shapes) directly from `exam.md` data and embed them with question text.
- **Student drawing capability during training** — MVP must support diagram annotation/drawing during training phase (e.g., for geometry problems requiring student to sketch rectangles, angles, circles). Implementation: Simple canvas tool or template editor integrated into question display. Fallback: If drawing is too complex, allow students to describe approach instead.
- **Multi‑LLM support** — Must support multiple LLM providers per bureau type (e.g., DeepSeek for pedagogical, GLM for Creative bureau tasks).

### 6.3 Technical Constraints

- **Local‑first:** File storage on the machine, not cloud. Simple Flask/FastAPI backend.
- **Static frontend:** HTML5 + JavaScript. No framework overhead.
- **Rendering:** TikZ (geometry) + Matplotlib (bar models, graphs) for diagrams. Local SVG/PDF output.
- **OCR:** Tesseract for scan ingestion. No paid vision APIs.
- **Rapid iteration:** Must allow quick changes based on what the student's data tells us.

### 6.4 Bureau Organisation (per v4.1 Directive)

| Bureau | LLM | Responsibility |
|--------|-----|---------------|
| **Pedagogy** | GLM 4.7 (pedagogical bureau) | Generate all questions + diagrams. Auto‑classify every question. Generate equation shadow + recognition cues + 3‑level articulation rubric. Alternative bureaus may use different LLMs (e.g., GLM for Creative bureau tasks). |
| **Integrity** | GLM 5.1 | Review every question for accuracy. Generate Triad feedback for every possible student articulation. |
| **Logistics** | Tesseract + TikZ/Matplotlib | Render all diagrams locally. Build the minimal MVP web interface (question display + forced articulation boxes + instant feedback). |
| **Creative** | — | Create the daily Pathway Radar warm‑up. Design the simple student reflection sheet. |

## 7. Data Foundation

The pilot is grounded in **real exam data**, not hypotheticals:

- **5 elite‑school prelim papers** (2025): ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS
- **94 questions** analysed and classified by pathway type
- **Coverage:** 67–71.3% of P6 exam content captured by the targeted pathways
- **Source files:** `neo_output/` directory containing corrected, ATOM‑SG‑analysed versions of all 5 papers

This data will be used to:
1. Select the 40 baseline questions (20 WP + 12 Geo + 8 DI)
2. Generate intervention training problems for the 3 weakest pathways
3. Create the Pathway Radar warm‑up items
4. Build the Week 5 transfer test (20 WP + 12 Geo + 8 DI)

## 8. Deliverables & Timeline

| Deliverable | Owner | Target | Status |
|-------------|-------|--------|--------|
| **SOR (this document)** | Zcaethbot | 2026‑04‑13 | 🟡 Draft — awaiting approval |
| **Baseline Test Pack (40 questions, printable PDFs)** | Pedagogy Bureau | Week 1 | Not started |
| **Gap Map Analyser** | Pedagogy + Logistics | Week 1 end | Not started |
| **MVP Web Interface** (question display + forced articulation + feedback) | Logistics Bureau | Week 2 | Not started |
| **Pathway Radar Warm‑up** | Creative Bureau | Week 2 | Not started |
| **Triad Feedback Engine** | Integrity Bureau | Week 2 | Not started |
| **Transfer Test** | Pedagogy Bureau | Week 5 | Not started |
| **Ramp‑up Analytics Report** | Zcaethbot | Week 5 end | Not started |

## 9. Open Decisions — Resolved

1. **Baseline question selection:** Which 40 questions from the 94 analysed? **Sean's decision: Balanced** — Select questions proportionally across pathways based on exam coverage.
2. **Student reflection sheet format:** Paper‑based or digital? **Sean's decision: Digital** — Create a digital reflection sheet interface in the MVP.
3. **Scan ingestion workflow:** Parent emails scan → OpenClaw processes? Or upload through MVP interface? **Sean's decision: Upload through MVP interface** — Implement scan upload directly in the MVP web interface.

*All open decisions are now resolved. Technical specification (C3) can proceed.*

---

*This document overrides all previous SOR versions. Approved by Sean Foo (2026‑04‑14 17:57 SGT).*
