# ATOM-SG MVP Frontend Functional Test Plan

**Objective:** Test every button, form, and interactive element in the frontend UI to ensure correct visual response, content display, and API integration.

**Focus Areas:**
1. Button clicks produce expected UI changes
2. Form submissions validate input and call correct endpoints
3. Dynamic content loads correctly
4. Modals open/close properly
5. Canvas tools work
6. Navigation between pages works
7. Error handling displays user-friendly messages
8. P0/P1 fixes are functional (step-by-step scaffolding, gaming detection, etc.)

**Test Environment:** Deployed instance at `http://192.168.2.6/` (atom‑forge VM)

**Test Method:** Manual browser testing with developer console open to monitor network requests and JavaScript errors.

---

## 1. Navigation Bar

| Element | Expected Behavior | Test Steps | Pass/Fail |
|---------|-------------------|------------|-----------|
| Dashboard link | Navigates to dashboard page, highlights active | Click "Dashboard" | |
| Baseline Test link | Navigates to baseline page | Click "Baseline Test" | |
| Daily Practice link | Navigates to practice page | Click "Daily Practice" | |
| Pathway Radar link | Navigates to pathway radar page | Click "Pathway Radar" | |
| Transfer Test link | Navigates to transfer page | Click "Transfer Test" | |
| Reflections link | Navigates to reflections page | Click "Reflections" | |

**Validation:**
- URL hash updates (e.g., `#dashboard`)
- Correct page section becomes visible (`class="page active"`)
- Other pages hidden
- Active link highlighted with CSS class

---

## 2. Dashboard Page

### 2.1 Today's Mission Card
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Mission card | Displays Week/Day info | Check text "Week 2, Day 3" |
| Task items | Show 3 tasks with time estimates | Verify 5 min, 15 min, 10 min tasks |

### 2.2 Statistics Cards
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Problems Completed | Shows number > 0 | Check `#total-problems` updates |
| Average Score | Shows percentage | Check `#avg-score` updates |
| Pathway Recognition | Shows percentage | Check `#id-accuracy` updates |
| Explanation Quality | Shows level (0/3) | Check `#articulation-level` updates |

**API Check:** Verify dashboard.js calls `/api/v1/milestones` and `/api/v1/reflections` on load.

### 2.3 Milestones Section
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Milestones list | Loads from API | Check `#milestones-list` populated |
| Progress indicators | Show completion status | Verify in‑progress/complete styling |

### 2.4 Gamification Section (P1‑1)
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Streak counter | Shows day count | Check `#streak-days` > 0 |
| Total days | Shows total days practiced | Check `#total-days` > 0 |
| Achievements list | Shows earned achievements | Check `#achievements-list` populated |
| No achievements message | Hidden if achievements exist | Verify `#no‑achievements` visibility |

### 2.5 Achievement Notification Modal
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Modal trigger | Appears when achievement earned | Simulate achievement unlock |
| Modal content | Shows achievement title/description | Check `#achievement‑title`, `#achievement‑description` |
| Dismiss button | Closes modal | Click `#achievement‑dismiss` |

---

## 3. Baseline Test Page

### 3.1 Print Baseline Test Button
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| "START HERE →" button | Triggers print dialog or PDF download | Click `#print‑baseline` |
| Button styling | Has pulse animation | Visual check |

**Note:** Browser may block print dialog; test that click handler doesn't throw errors.

### 3.2 Upload Section
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| File input | Accepts .pdf, .png, .jpg | Test file selection |
| Upload button | Submits form | Click upload button with test file |
| Upload status | Shows progress/result | Check `#baseline‑upload‑status` |
| Form validation | Requires file selection | Submit empty form |

**API Check:** Verify baseline.js calls OCR endpoint (`/api/v1/ocr/process`) with FormData.

### 3.3 Gap Map Results
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Results section | Appears after upload | Check `#baseline‑results` visible |
| Gap map visualization | Shows diagnostic data | Check `#gap‑map` populated |

**Workflow Test:** Upload sample PDF → verify OCR pipeline → verify gap map display.

---

## 4. Daily Practice Page

### 4.1 Floating Buttons
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| "Need Help? 💡" button (P0‑3) | Opens help modal | Click `#stuckButton` |
| Glossary button | Opens glossary modal | Click `#glossaryButton` |

### 4.2 Practice Controls
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| "Start Pathway Radar Warm‑up" | Shows radar section, starts timer | Click `#start‑warmup` |
| "Start Practice Session" | Shows practice section, loads problem | Click `#start‑session` |

### 4.3 Pathway Radar Warm‑up
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Timer display | Shows 05:00 countdown | Check `#radar‑timer` updates |
| Progress bar | Fills as time passes | Check `#radar‑progress‑fill` |
| Questions | Load 10 questions from API | Check `#radar‑questions` populated |
| Submit button | Appears after time/answers | Click `#submit‑radar` |
| Feedback section | Shows results after submit | Check `#radar‑feedback` visible |

**API Check:** Verify pathway‑radar.js calls `/api/v1/pathway‑radar/questions` and `/api/v1/pathway‑radar/submit`.

### 4.4 Practice Session

#### 4.4.1 Session Header
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Pathway display | Shows current pathway type | Check `#session‑pathway` |
| Progress indicator | Shows "Problem X of Y" | Check `#session‑progress` |
| Timer | Shows elapsed time | Check `#practice‑timer` |
| Progress bar | Fills as problems completed | Check `#session‑progress‑fill` |

#### 4.4.2 Problem Display
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Problem title | Loads from API | Check `#problem‑title` |
| Problem text | Shows question | Check `#problem‑text` |
| Diagrams | Load SVG from `/renders/` | Check `#problem‑diagrams` has `<img>` |
| Difficulty badge | Shows easy/medium/hard | Check `#problem‑difficulty` |

#### 4.4.3 Canvas Tools (P0 Fix #2)
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Pen tool | Sets drawing mode to pen | Click pen button, draw on canvas |
| Line tool | Sets mode to straight line | Click line button, draw line |
| **Text tool** | **Adds text annotation** | **Click text button, click canvas, type text** |
| Eraser tool | Sets mode to eraser | Click eraser, erase drawing |
| Clear button | Clears entire canvas | Click clear, verify canvas empty |

#### 4.4.4 Forced Articulation Form (P0‑1, P0‑4)
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Pathway type dropdown | Has 5 options with tooltips | Select each option |
| Tooltip icons | Show help on hover | Hover over `?` icons |
| Equation shadow textarea | Requires ≥50 characters | Type <50 chars, check validation |
| Character counter | Updates as user types | Check `#char‑count` updates |
| Example link | Toggles example visibility | Click "See example" |
| "Confirm & Solve" button | Enabled when form valid | Verify button state |
| Articulation error message | Shows if validation fails | Check `#articulation‑error` |

**Validation Tests:**
- Empty pathway type → error
- Short equation shadow (<50 chars) → error with P0‑1 gibberish detection
- Valid input → enables button

#### 4.4.5 Solution Section
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Answer input | Accepts numeric input | Type number in `#student‑answer` |
| Submit button | Submits answer | Click `#submit‑answer` |

#### 4.4.6 Triad Feedback (P0‑7 Step‑by‑Step Scaffolding)
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Pathway feedback card | Shows correct/incorrect | Check `#pathway‑feedback‑text` |
| Articulation feedback card | Shows level 0‑3 | Check `#articulation‑level‑val` |
| Model articulation | Shows example explanation | Check `#model‑articulation‑text` |
| Solution feedback card | Shows correct/incorrect | Check `#solution‑feedback‑text` |
| Step‑by‑step guidance (P0‑7) | **Appears for wrong answers** | Submit wrong answer, check for step list |
| Step toggle | Shows/hides detailed steps | Click step expand/collapse |
| Gaming detection message (P0‑2) | **"Let's Take a Short Break"** | Submit answers too quickly |
| "Next Problem" button | Loads next problem | Click `#next‑problem` |

### 4.5 Help Modal (P0‑3)
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Modal open | From floating button | Click "Need Help?" |
| "Show Hint" button | Fetches hint from API | Click `#hint‑btn`, check `#hint‑content` |
| "Open Glossary" button | Opens glossary modal | Click `#glossary‑btn` |
| "Show Example" button | Fetches example from API | Click `#example‑btn`, check `#example‑content` |
| Close button | Closes modal | Click `#close‑help` |

**API Check:** Verify practice.js calls `/api/v1/problems/{id}/hint` and `/api/v1/pathways/{type}/example`.

---

## 5. Pathway Radar Page

| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Radar chart visualization | Shows performance history | Check `#radar‑chart` |
| History section | Lists past attempts | Check `#radar‑history` populated |

**API Check:** Verify pathway‑radar.js fetches historical data.

---

## 6. Transfer Test Page

### 6.1 Print Transfer Test Button
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Print button | Triggers print/download | Click `#print‑transfer` |

### 6.2 Upload Section
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| File input | Accepts PDF/PNG/JPG | Select test file |
| Upload button | Submits for OCR | Click upload |
| Status display | Shows progress | Check `#transfer‑upload‑status` |

### 6.3 Ramp‑up Analytics
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Results section | Appears after upload | Check `#transfer‑results` visible |
| Metrics display | Shows improvement data | Check `#ramp‑up‑metrics` |
| Success criteria | Shows pass/fail status | Check `#success‑criteria` |

---

## 7. Reflections Page

### 7.1 Reflection Form
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Week dropdown | Options 1‑5 | Select each |
| Pathway dropdown | 5 pathway types | Select each |
| Reflection textarea | Required field | Type reflection |
| Confidence slider | 1‑5 with labels | Drag slider, check `#confidence‑value` |
| Struggles checkboxes | Multiple selection | Check various boxes |
| Improvements checkboxes | Multiple selection | Check various boxes |
| Submit button | Posts to API | Click submit |

**API Check:** Verify reflections.js calls `/api/v1/reflections` POST.

### 7.2 Reflections History
| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| History list | Loads previous reflections | Check `#reflections‑list` populated |

---

## 8. Glossary Modal (P0‑5)

| Element | Expected Behavior | Test Steps |
|---------|-------------------|------------|
| Search input | Filters terms | Type "pathway", verify results |
| Glossary content | Shows all terms | Check `#glossary‑content` |
| Close button | Closes modal | Click `#close‑glossary` |
| Keyboard shortcut | Ctrl+B opens modal | Press Ctrl+B |

**API Check:** Verify glossary.js calls `/api/v1/glossary` and `/api/v1/glossary/search`.

---

## 9. Error Handling & Edge Cases

| Scenario | Expected Behavior | Test Steps |
|----------|-------------------|------------|
| API offline | Graceful error message | Block network, click buttons |
| Invalid file type | Clear error message | Upload .txt file |
| Network timeout | Loading spinner, retry option | Simulate slow network |
| Session expired | Redirect/re‑auth | N/A (MVP uses anonymous) |
| Browser back/forward | Preserves page state | Navigate back during practice |

---

## 10. P0/P1 Fix Verification Checklist

### P0‑1: Articulation Validation Enhancement
- [ ] Frontend requires ≥50 characters
- [ ] Backend validates gibberish detection
- [ ] Error messages clear and helpful

### P0‑2: Gaming Detection Language Fix
- [ ] Message changed from "Consequences Applied" to "Let's Take a Short Break"
- [ ] Supportive tone with emoji

### P0‑3: "I'm Stuck" Button
- [ ] Floating button visible on practice page
- [ ] Modal opens with 3 help options
- [ ] Hint/example API endpoints work

### P0‑4: Terminology Definitions
- [ ] Tooltips on pathway type and equation shadow labels
- [ ] Articulation level info box appears in feedback

### P0‑5: Vocabulary Support (Glossary)
- [ ] Floating glossary button works
- [ ] Modal opens with search
- [ ] Ctrl+B shortcut works

### P0‑6: Visual‑Text Mismatches
- [ ] All 25 geometry diagrams render correctly
- [ ] Diagrams accessible at `/renders/{id}.svg`
- [ ] Angle rays present (G001‑G003, G007, G008)
- [ ] Height label arrows present (G017)
- [ ] Quarter‑circle shape correct (G010)

### P0‑7: Step‑by‑Step Scaffolding
- [ ] Wrong answers trigger step‑by‑step guidance
- [ ] Steps toggle expand/collapse
- [ ] Covers 7 common mistake patterns

### P1‑1: Gamification
- [ ] Streak counter updates
- [ ] Achievements unlock and display
- [ ] Notification modal pops up

---

## 11. Test Execution Notes

**Browser Console:**
- Monitor for JavaScript errors
- Check network requests succeed (status 200)
- Verify request/response payloads match API spec

**Visual Inspection:**
- Buttons have hover/focus states
- Modals center on screen
- Text readable, no overlapping elements
- Responsive on mobile viewport

**API Integration:**
- Each button click should trigger appropriate API call
- Loading states shown during API calls
- Error states handled gracefully

**Workflow Tests:**
1. Baseline upload → gap map
2. Practice session start → problem load → articulation → submission → feedback → next problem
3. Pathway radar warm‑up → question display → submission → feedback

---

## 12. Bug Reporting Template

```
Page: [Dashboard/Baseline/Practice/etc.]
Element: [Button/Form/Modal ID]
Issue: [Description]
Steps to Reproduce:
1. 
2. 
3.
Expected:
Actual:
Console Errors: [if any]
Network Requests: [failed calls]
Screenshot: [if applicable]
Priority: [P0/P1/P2]
```

---

*Test Plan Created: 2026-04-17*
*Target Completion: Before pilot launch (2026-04-26)*
*Test Environment: http://192.168.2.6/*