# All 25 UI/UX Issues — Categorized

**Date:** 2026-04-15
**Testing Perspective:** 11-Year-Old Student (Human, Not Robot)
**Total Issues:** 25 (14 HIGH, 11 MEDIUM)

---

## 📊 Summary by Category

| Category | Count | High | Medium |
|----------|--------|-------|---------|
| Visual-Text Inconsistencies | 5 | 4 | 1 |
| Engagement Barriers | 7 | 5 | 2 |
| Touch Points | 5 | 3 | 2 |
| Expression Gaps | 4 | 2 | 2 |
| Other (Process) | 4 | 0 | 4 |
| **TOTAL** | **25** | **14** | **11** |

---

## 🎯 Category 1: Visual-Text Inconsistencies (5 issues)

### 1.1 Dashboard Labels Not Understandable 🔴 HIGH
- **Location:** Dashboard stat cards
- **Issue:** "ID Accuracy" and "Articulation Level" use technical terms
- **11-Year-Old Perspective:** "ID could mean identity card, articulation sounds like jaw movement"
- **Impact:** Can't tell if doing well or not → Disengages immediately
- **Fix:** "ID Accuracy" → "Pathway Recognition", "Articulation Level" → "Explanation Quality"

### 1.2 Pathway Radar Diagram Mismatch 🔴 HIGH
- **Location:** Pathway radar questions
- **Issue:** "points A, B, C lie on straight line" but diagram shows arrows or angles
- **11-Year-Old Perspective:** "Is this a different type of problem?"
- **Impact:** Picks wrong pathway → Feels stupid
- **Fix:** Diagrams must clearly show straight horizontal line with marked points

### 1.3 Geometry Sides Unlabeled 🔴 HIGH
- **Location:** Geometry composite shapes
- **Issue:** "joined along 5 cm side" not labeled
- **11-Year-Old Perspective:** "Which side is 5 cm? I have to guess"
- **Impact:** Wrong answer → Skips problem
- **Fix:** Label ALL sides with lengths

### 1.4 Bar Model Color Mismatch 🟡 MEDIUM
- **Location:** Bar model diagrams
- **Issue:** Colors don't match fractions (red/blue sections unlabeled)
- **11-Year-Old Perspective:** "Which color is 3/5?"
- **Impact:** Random guess on pathway
- **Fix:** Color-code with labels OR explain colors in text

### 1.5 Before-After Arrows Unclear 🔴 HIGH
- **Location:** Before-after-change problems
- **Issue:** Arrows don't show what changed (sold? given away? moved?)
- **11-Year-Old Perspective:** "Can't tell if items were sold or given away"
- **Impact:** Can't identify pathway correctly
- **Fix:** Arrows with numbers + labels ("sold 30", "gave away 15")

---

## 🚨 Category 2: Engagement Barriers (7 issues)

### 2.1 No Clear "START HERE" 🔴 HIGH
- **Location:** Homepage
- **Issue:** 6 navigation options, no clear first step
- **11-Year-Old Perspective:** "Which button do I click? Dashboard? Baseline Test?"
- **Impact:** Stares 30 seconds → Clicks randomly → Frustrated
- **Fix:** Week 1 task glows or pulses, big "START NOW" button

### 2.2 Print/Scan Baseline Test (Accepted for MVP) 🟡 MEDIUM
- **Location:** Baseline test flow
- **Issue:** Print → offline → scan → upload = too many steps
- **11-Year-Old Perspective:** "No printer! Mom's not home to scan! Too much work"
- **Impact:** Would quit → Says "forgot to do it"
- **Status:** **ACCEPTED FOR MVP** (development time constraint)
- **Post-Launch Enhancement:** Online baseline test option

### 2.3 Forced Articulation Confusing 🔴 HIGH
- **Location:** Practice articulation form
- **Issue:** "Equation Shadow" with 200-character minimum
- **11-Year-Old Perspective:** "Don't know what to write! I'll type nonsense to get past it"
- **Impact:** Defeats whole point of articulation
- **Fix:** "Explain how you'd solve this" + examples OR fill-in-blank template

### 2.4 Confusing Pathway Type Names 🔴 HIGH
- **Location:** Pathway type dropdown
- **Issue:** "Data-Interpretation-Red-Herring" — what's a red herring?
- **11-Year-Old Perspective:** "I'll pick randomly if I'm confused"
- **Impact:** Can't select correct pathway
- **Fix:** Simpler language OR hover tooltips explaining each pathway type

### 2.5 Triad Feedback Too Long 🟡 MEDIUM
- **Location:** After answer submission
- **Issue:** Three long paragraphs
- **11-Year-Old Perspective:** "Too much reading! I'll skip explanation"
- **Impact:** Won't learn from feedback
- **Fix:** Key feedback in big colorful text, long explanation in "Click for details"

### 2.6 Timer Missing Problem Count 🟡 MEDIUM
- **Location:** Practice timer
- **Issue:** Shows 30 minutes but not how many problems
- **11-Year-Old Perspective:** "Am I going too slow? Too fast? I don't know if I'll finish"
- **Impact:** Anxiety → Rushes and makes mistakes
- **Fix:** "5 problems in 30 minutes = 6 min per problem" + progress bar

### 2.7 Gaming Detection Feels Like Punishment 🔴 HIGH
- **Location:** Pathway radar gaming detection
- **Issue:** "Consequences Applied — 50 points deducted — 5-minute cooldown"
- **11-Year-Old Perspective:** "System thinks I'm cheating! I don't want to use it anymore"
- **Impact:** **Quits because system doesn't trust them**
- **Fix:** "We noticed you're answering very quickly — let's take a short break to think more carefully"

---

## 👆 Category 3: Touch Points Effectiveness (5 issues)

### 3.1 Canvas Tool Missing Features 🔴 HIGH
- **Location:** Canvas annotation tool
- **Issue:** Text tool exists in code but **not visible in UI**, no shapes, no undo/redo
- **11-Year-Old Perspective:** "I can't label 'base' of triangle, can't draw circles, can't undo mistakes"
- **Impact:** Can't annotate thinking → Skips using canvas
- **Fix:** Add text tool (📝), circle (○), rectangle (□) buttons + undo/redo visible in HTML

### 3.2 Triad Feedback Confusing 🔴 HIGH
- **Location:** Feedback display
- **Issue:** 3 long sections, confidence bar confusing ("75% — good or bad?")
- **11-Year-Old Perspective:** "I can't tell which part is most important"
- **Impact:** Feedback not actionable
- **Fix:** Most important feedback at top in big text: "You got pathway wrong — look for 'sold' and 'remainder' next time"

### 3.3 Model Comparison Not Side-by-Side 🔴 HIGH
- **Location:** Model articulation comparison
- **Issue:** Student articulation disappears when model shown, no side-by-side
- **11-Year-Old Perspective:** "Can't compare, model's is too complex ('sequential changes', 'equation framework')"
- **Impact:** Feels stupid, doesn't learn
- **Fix:** Show both side-by-side: "You said: ____ Model says: ____ What you missed: ____"

### 3.4 Progress Navigation Confusing 🟡 MEDIUM
- **Location:** Progress dashboard
- **Issue:** Don't know which week, no "Today's Tasks"
- **11-Year-Old Perspective:** "Which week am I in? Based on date or problems done? What should I do today?"
- **Impact:** Confused but not blocking
- **Fix:** "Today's Mission" at top: "You're on Week 2, Day 3. Today: Pathway Radar (5 min) + 3 Practice Problems (15 min)"

### 3.5 No "I'm Stuck" Button 🔴 HIGH
- **Location:** All problem pages
- **Issue:** No help button when stuck
- **11-Year-Old Perspective:** "I'm stuck! Where's the 'I'm stuck' button? I'll guess randomly or skip"
- **Impact:** Skips problems instead of asking for help
- **Fix:** Floating "Need Help?" button → "Show Hint", "Glossary", "Ask for Example"

---

## 💬 Category 4: Student Expression Gaps (4 issues)

### 4.1 No Text Annotation Visible 🔴 HIGH
- **Scenario:** "Make This Diagram Clearer" — can't tell which side is base
- **Current:** Can draw red line with pen
- **Missing:** Text tool visible in UI (exists in code but not HTML)
- **Impact:** Can't ask questions about diagram
- **Fix:** Add text tool button to canvas UI

### 4.2 No "Show Me Steps" Hints 🔴 HIGH
- **Scenario:** "Show Me Steps" — don't understand word problem
- **Current:** Nothing — no way to ask for help
- **Missing:** "Give me a hint" or "Break down problem" button
- **Impact:** Will guess randomly or skip
- **Fix:** Add "Give me a hint" button → shows next step without giving answer

### 4.3 No Way to Question Diagram 🟡 MEDIUM
- **Scenario:** "This Doesn't Match What I Think" — diagram shows X but think it's Y
- **Current:** Nothing — can't challenge diagram
- **Missing:** Way to ask questions or request different visualization
- **Impact:** Goes with what sees even if confusing
- **Fix:** "I'm confused about this diagram" button → ask questions

### 4.4 No Pattern Highlighting Help 🔴 HIGH
- **Scenario:** "Help Me See Pattern" — can't see pathway type
- **Current:** Nothing — no hints, no pattern highlighting
- **Missing:** Hints system, highlight change in before-after problems
- **Impact:** Can't see pattern → guesses pathway
- **Fix:** "Show me a hint" + pattern highlighting

---

## 📋 Category 5: Other Process Issues (4 issues)

### 5.1 Glossary Access Hidden 🟡 MEDIUM
- **Location:** Help system
- **Issue:** Glossary exists but students don't know Ctrl+B shortcut
- **11-Year-Old Perspective:** "How do I open glossary? I don't know Ctrl+B exists"
- **Impact:** Can't look up "equation shadow", "pathway type"
- **Fix:** Add "?" icon button → opens glossary modal

### 5.2 No Tooltips on Confusing Words 🟡 MEDIUM
- **Location:** Terminology throughout system
- **Issue:** No hover explanations on technical terms
- **11-Year-Old Perspective:** "What does 'red herring' mean? No help nearby"
- **Impact:** Can't understand pathway type names
- **Fix:** Add tooltips to confusing words (show definition on hover)

### 5.3 No Progress Indicators 🟡 MEDIUM
- **Location:** Practice sessions
- **Issue:** Don't see how many problems done vs total
- **11-Year-Old Perspective:** "How much more do I have to do?"
- **Impact:** Unclear progress
- **Fix:** "Problem 3 of 5" indicator

### 5.4 Milestones Unclear 🟡 MEDIUM
- **Location:** Dashboard
- **Issue:** Milestones have checkmarks but don't know what triggers them
- **11-Year-Old Perspective:** "How do I get checkmarks? What do I do?"
- **Impact:** Confused about progress
- **Fix:** Show requirements: "Complete Week 1 Baseline Test" + "Practice for 5 days"

---

## 🚀 Fix Priority for Launch

### 🔴 MUST FIX Before Launch (Critical — Blocks Engagement)

1. **Gaming Detection Language** — Change to supportive, not punitive
2. **Text Tool Visible in Canvas** — Add to UI (code exists)
3. **Forced Articulation UI** — "Explain how you'd solve" + examples
4. **Dashboard Labels** — Simplify terminology
5. **Pathway Type Names** — Simplify or add tooltips
6. **No "I'm Stuck" Button** — Add floating help button
7. **Side-by-Side Comparison** — Show student vs model together
8. **Clear "START HERE"** — Week 1 task highlights

### 🟡 Should Fix Before Launch (High Impact)

9. Geometry sides labeled
10. Pathway radar diagrams match text
11. Before-after arrows with labels
12. Triad feedback simplified (key feedback big + colorful)
13. Model articulation comparison side-by-side
14. Progress navigation with "Today's Mission"

### 🟢 Post-Launch Enhancements (Nice-to-Have)

15-25. Remaining 11 medium-priority issues

---

## 📊 Impact Summary

| Impact Type | Count | Description |
|-------------|--------|-------------|
| **Blocks Engagement** | 8 | Will cause students to quit or skip |
| **Causes Wrong Answers** | 6 | Visual/text mismatches, confusing UI |
| **Affects Learning Quality** | 7 | Feedback not actionable, can't learn |
| **Mildly Confusing** | 4 | Can work around but frustrating |

---

## 🎯 Most Critical Insight

**Gaming detection (Issue #2.7) is the SINGLE BIGGEST RISK:**
- Technical implementation is sound
- But language feels like punishment
- Will cause students to quit: "System doesn't trust me, why should I trust it?"
- **Fix is simple (language change) but impact is MASSIVE**

---

## 📁 Files to Modify

| File | Changes Required |
|------|----------------|
| `dashboard.html` | Simplify labels, add "Today's Mission" |
| `practice.html` | Add "I'm Stuck" button, simplify triad feedback |
| `main.py` | Change gaming detection language |
| `canvas.js` | Ensure text/shapes tools visible in HTML |
| `style.css` | Add tooltip styles |

---

**Total Estimated Fix Time:** 2-3 hours for critical issues
