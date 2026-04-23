# Comprehensive Gap Analysis: ATOM-SG Pilot
## Training Programme, Backend, Frontend & 12 Persona Coverage

**Date:** 2026-04-19  
**Version:** 1.0  
**Scope:** Complete system analysis including pedagogy, technology, and learner profiles

---

## Table of Contents

1. [Training/Intervention Programme Gaps](#1-trainingintervention-programme-gaps)
2. [Backend System Gaps](#2-backend-system-gaps)
3. [Frontend System Gaps](#3-frontend-system-gaps)
4. [12 Persona Coverage Analysis](#4-12-persona-coverage-analysis)
5. [Integrated Recommendations](#5-integrated-recommendations)

---

## 1. Training/Intervention Programme Gaps

### 1.1 Current Intervention Model

The current ATOM-SG intervention follows a simplified loop:
```
Baseline Test → Gap Identification → Daily Practice → Transfer Test
```

**Components:**
- Pathway Radar (warm-up identification)
- Forced Articulation (explain before solving)
- Triad Feedback (pathway + articulation + solution)
- Step-by-step scaffolding (P0-7 fixes)
- Glossary for vocabulary gaps

### 1.2 Critical Pedagogical Gaps

#### Gap 1.1: No Differentiated Learning Paths

| Aspect | Current | Required |
|--------|---------|----------|
| **Content adaptation** | Same problems for all | Differentiated by persona |
| **Pacing** | Fixed schedule | Adaptive based on mastery |
| **Scaffolding intensity** | Uniform hints | Tiered by struggle profile |
| **Review frequency** | Daily for all | Spaced repetition per retention |

**Impact:** High-achievers (Alex, Brianna) bored; strugglers (Eve, Fay) overwhelmed

#### Gap 1.2: Missing Metacognitive Training

Current system teaches *what* to solve but not *how* to think:

**Missing Components:**
- Self-monitoring strategies ("Am I using the right pathway?")
- Error detection training ("Does my answer make sense?")
- Strategic planning ("Should I draw a model first?")
- Reflection protocols beyond simple articulation

**Evidence from 12 Personas:**
- Grace (confused) needs explicit pathway discrimination training
- Henry (anxious) needs confidence-building metacognitive routines
- Kevin (visual) needs model-drawing strategy instruction

#### Gap 1.3: Insufficient Transfer Training

Current transfer test is a single endpoint assessment.

**Missing:**
- Near-transfer practice (same pathway, different context)
- Far-transfer challenges (different pathway, novel context)
- Mixed pathway drills (discrimination training)
- Real-world application problems

**Exam Standard Requirement:**
Cross-Thread Collision problems require automatic pathway discrimination - current training doesn't build this fluency.

#### Gap 1.4: No Social/Emotional Learning Integration

| Persona Type | Emotional Need | Current Support |
|--------------|----------------|-----------------|
| Henry (Anxious) | Anxiety management | None |
| Cameron (Disengaged) | Motivation/engagement | Gamification only |
| Fay (Random) | Attention/focus | None |
| Jack (Gamer) | Integrity/effort | Detection only |

**Missing:**
- Growth mindset interventions
- Anxiety reduction techniques
- Engagement hooks for disengaged learners
- Self-regulation training

#### Gap 1.5: Incomplete Feedback Loop

Current triad feedback:
```
Pathway ID → Articulation → Solution
```

**Missing Dimensions:**
- Process feedback (how they arrived at answer)
- Strategic feedback (better approaches)
- Affective feedback (encouragement calibrated to persona)
- Comparative feedback (progress over time)

#### Gap 1.6: No Parent/Teacher Dashboard

Current system is student-facing only.

**Missing:**
- Progress reports for parents
- Intervention recommendations for teachers
- Home-school connection activities
- Parent guidance for supporting each persona type

---

## 2. Backend System Gaps

### 2.1 Data Model Limitations

#### Gap 2.1.1: No Persona-Aware Data Model

Current `Problem` model:
```python
class Problem(BaseModel):
    id: str
    title: str
    track: TrackType
    pathway: str
    difficulty: DifficultyLevel
    questionText: str
    diagrams: List[Diagram]
    expectedAnswer: ExpectedAnswer
```

**Missing:**
- Persona suitability flags
- Cognitive demand metrics
- Visual stress score
- Trap density rating
- Recommended scaffolding level

#### Gap 2.1.2: No Learning Profile Persistence

Current session data:
```python
class PracticeSession(BaseModel):
    id: str
    student_id: str
    problems: List[ProblemAttempt]
    completed_at: datetime
```

**Missing:**
- Persona classification persistence
- Long-term learning trajectory
- Skill mastery tracking over time
- Forgetting curve modeling

#### Gap 2.1.3: No Adaptive Problem Selection

Current problem selection is random or fixed sequence.

**Required:**
```python
class AdaptiveSelector:
    def select_next_problem(self, student_profile: Persona, 
                           mastery_state: MasteryMap) -> Problem:
        # Consider:
        # - Current mastery gaps
        # - Persona learning preferences
        # - Spaced repetition schedule
        # - Difficulty calibration
        pass
```

### 2.2 API Endpoint Gaps

| Endpoint Needed | Purpose | Priority |
|-----------------|---------|----------|
| `GET /personas/{id}/profile` | Retrieve full learner profile | HIGH |
| `POST /personas/{id}/classify` | Classify student into persona | HIGH |
| `GET /problems/recommended` | Adaptive problem selection | HIGH |
| `POST /interventions/suggest` | AI-powered intervention suggestions | MEDIUM |
| `GET /progress/trajectory` | Long-term progress visualization | MEDIUM |
| `POST /feedback/affective` | Generate persona-calibrated encouragement | MEDIUM |
| `GET /reports/parent/{student_id}` | Parent-facing progress report | LOW |

### 2.3 Algorithm Gaps

#### Gap 2.3.1: No Persona Classification Algorithm

Current: Manual assignment or default

**Required:**
```python
def classify_persona(baseline_results: dict, 
                     behavioral_data: dict) -> PersonaType:
    """
    Classify student into 1 of 12 personas based on:
    - Accuracy patterns
    - Error types
    - Time spent
    - Help-seeking behavior
    - Confidence ratings
    """
    pass
```

#### Gap 2.3.2: No Gaming Detection (Jack Persona)

Current: Basic pattern detection placeholder

**Required:**
```python
def detect_gaming_behavior(session_data: Session) -> GamingRisk:
    """
    Detect:
    - Speed patterns (too fast = guessing)
    - Answer patterns (systematic errors)
    - Help abuse (clicking through hints)
    - Navigation patterns (skipping articulation)
    Returns: LOW, MEDIUM, HIGH risk + evidence
    """
    pass
```

#### Gap 2.3.3: No Spaced Repetition System

Current: Daily practice only

**Required:**
```python
class SpacedRepetition:
    def schedule_review(self, problem_id: str, 
                       performance: PerformanceLevel) -> datetime:
        """
        Schedule next review based on:
        - Performance (correct/incorrect)
        - Time since last review
        - Historical retention rate
        - Persona-specific forgetting curve
        """
        pass
```

### 2.4 Database/Storage Gaps

| Storage Need | Current | Required |
|--------------|---------|----------|
| **Persona profiles** | In-memory only | Persistent database |
| **Learning trajectories** | Session-only | Long-term history |
| **Problem attempts** | Basic log | Detailed analytics |
| **Intervention outcomes** | None | A/B test results |
| **Content metadata** | Basic | Rich pedagogical tags |

---

## 3. Frontend System Gaps

### 3.1 UI/UX Gaps by Persona Type

#### Gap 3.1.1: Visual Learners (Brianna, Kevin)

**Current:** Text-heavy interface, static diagrams
**Required:**
- Interactive model-drawing canvas
- Animated solution walkthroughs
- Visual pathway maps
- Color-coded concept connections

**Implementation:**
```javascript
// Interactive model canvas
class ModelCanvas {
    constructor() {
        this.canvas = document.getElementById('model-canvas');
        this.tools = ['bar', 'unit', 'comparison', 'before-after'];
    }
    
    enableDrawing(pathwayType) {
        // Provide appropriate model template
        // Guide student through construction
        // Validate model correctness
    }
}
```

#### Gap 3.1.2: Anxious Learners (Henry)

**Current:** Timer visible, progress bars, score emphasis
**Required:**
- Anxiety-reducing UI mode
- Optional timer hiding
- Progress emphasis on effort not score
- Calming color scheme option
- "Take a break" prompts

#### Gap 3.1.3: Disengaged Learners (Cameron, Fay)

**Current:** Basic gamification (streaks, badges)
**Required:**
- Narrative/adventure mode
- Choice in problem topics
- Social comparison (leaderboards)
- Unlockable content
- Variable reward schedules

#### Gap 3.1.4: Reading Struggles (Liam)

**Current:** Text-only problems
**Required:**
- Text-to-speech integration
- Simplified language mode
- Visual problem summaries
- Chunked text presentation
- Highlighting/key term extraction

### 3.2 Interaction Pattern Gaps

#### Gap 3.2.1: No Drawing/Annotation Tools

**Required for:**
- Grid construction problems (G6)
- Model drawing (all pathways)
- Working space utilization
- Teacher review of student work

```javascript
class AnnotationLayer {
    constructor() {
        this.tools = {
            pen: { color: 'black', width: 2 },
            highlighter: { color: 'yellow', opacity: 0.3 },
            eraser: { size: 20 },
            shapes: ['line', 'circle', 'rectangle']
        };
    }
}
```

#### Gap 3.2.2: No Collaborative Features

**Missing:**
- Peer discussion forums
- Study group formation
- Parent-student shared view
- Teacher-student messaging

### 3.3 Accessibility Gaps

| Accessibility Need | Current | WCAG 2.1 AA Required |
|-------------------|---------|---------------------|
| **Screen reader** | Partial | Full support |
| **Keyboard navigation** | Basic | Complete |
| **Color contrast** | Passes | Enhanced for low vision |
| **Font sizing** | Fixed | Adjustable |
| **Motion reduction** | None | Respect prefers-reduced-motion |
| **Cognitive load** | High | Simplified modes |

### 3.4 Mobile/Responsive Gaps

Current frontend is desktop-first.

**Required:**
- Touch-optimized model drawing
- Mobile-friendly navigation
- Offline mode for practice
- Push notifications for spaced repetition

---

## 4. 12 Persona Coverage Analysis

### 4.1 Persona Definitions & Current Support

| ID | Persona | Accuracy | Key Traits | Current Support | Gap Severity |
|----|---------|----------|------------|-----------------|--------------|
| 1 | **Alex** (Perfect) | 95%+ | Self-directed, fast | ✅ Full | LOW |
| 2 | **Brianna** (Visual) | 85% | Needs diagrams | ⚠️ Partial | MEDIUM |
| 3 | **Cameron** (Disengaged) | 75% | Low motivation | ⚠️ Gamification only | HIGH |
| 4 | **Dylan** (Distracted) | 65% | Attention issues | ❌ None | HIGH |
| 5 | **Eve** (Struggling) | 50% | Needs intensive help | ⚠️ Basic hints | HIGH |
| 6 | **Fay** (Random) | 40% | Guessing, gaming | ⚠️ Detection only | HIGH |
| 7 | **Grace** (Confused) | 55% | Wrong pathways | ⚠️ Feedback only | HIGH |
| 8 | **Henry** (Anxious) | 60% | Second-guesses | ❌ None | HIGH |
| 9 | **Ivy** (Critical) | 70% | UI/UX focused | ⚠️ Basic UI | MEDIUM |
| 10 | **Jack** (Gamer) | Variable | Pattern exploitation | ⚠️ Detection only | HIGH |
| 11 | **Kevin** (Visual) | 80% | Weak articulation | ⚠️ Partial | MEDIUM |
| 12 | **Liam** (Reading) | 60% | Misinterprets | ❌ None | HIGH |

### 4.2 Detailed Persona Gap Analysis

#### Alex (Perfect Student - 95%+)
**Current:** Well supported
**Gap:** Needs challenge/extension problems
**Recommendation:**
- Unlock "expert mode" with Cross-Thread Collision
- Peer tutoring opportunities
- Leadership roles in collaborative features

#### Brianna (Visual Learner - 85%)
**Current:** Static diagrams only
**Gaps:**
- No interactive model drawing
- No animated solutions
- No visual pathway maps
**Recommendations:**
- Implement interactive canvas
- Add "draw your model" feature
- Visual articulation options (sketch + label)

#### Cameron (Disengaged - 75%)
**Current:** Basic gamification
**Gaps:**
- No narrative/mission structure
- No choice in content
- No social features
**Recommendations:**
- Adventure mode with storyline
- Topic selection autonomy
- Class leaderboards
- Variable reward schedules

#### Dylan (Distracted - 65%)
**Current:** No support
**Gaps:**
- No focus mode
- No attention training
- No break reminders
**Recommendations:**
- "Focus mode" (minimal UI)
- Pomodoro-style sessions
- Attention-building exercises
- Progress saving for interruptions

#### Eve (Struggling - 50%)
**Current:** Basic hints
**Gaps:**
- No intensive scaffolding
- No prerequisite review
- No confidence building
**Recommendations:**
- Prerequisite pathway review
- Maximum scaffolding mode
- Success spirals (easy → medium)
- Celebrate small wins

#### Fay (Random Guesser - 40%)
**Current:** Gaming detection only
**Gaps:**
- No engagement hooks
- No attention diagnosis
- No intervention for guessing
**Recommendations:**
- Detect random patterns
- Require working for all answers
- Gamification that rewards effort
- Attention assessment

#### Grace (Confused Pathways - 55%)
**Current:** Feedback only
**Gaps:**
- No pathway discrimination training
- No explicit strategy instruction
- No metacognitive scaffolding
**Recommendations:**
- Pathway discrimination drills
- "Which pathway?" mini-lessons
- Strategy decision trees
- Metacognitive prompts

#### Henry (Anxious - 60%)
**Current:** No support
**Gaps:**
- No anxiety-reducing UI
- Timer increases stress
- Score emphasis harmful
**Recommendations:**
- Anxiety-reducing UI mode
- Optional timer hiding
- Effort-based feedback
- Breathing exercises
- "It's okay to be wrong" messaging

#### Ivy (Critical/UI-Focused - 70%)
**Current:** Basic UI
**Gaps:**
- No feedback mechanism
- No customization options
- No accessibility features
**Recommendations:**
- Feedback button
- UI customization
- Accessibility options
- Beta tester program

#### Jack (Gamer/Exploiter - Variable)
**Current:** Pattern detection placeholder
**Gaps:**
- No robust gaming detection
- No intervention strategies
- No integrity education
**Recommendations:**
- Robust behavioral analytics
- Gentle redirection messages
- Integrity-focused feedback
- Parent/teacher alerts

#### Kevin (Visual/Weak Articulation - 80%)
**Current:** Text-only articulation
**Gaps:**
- No visual articulation options
- No scaffolded explanation
- No model-to-text bridge
**Recommendations:**
- Draw-and-label articulation
- Sentence starters
- Model annotation tools
- Gradual text scaffolding

#### Liam (Reading Struggles - 60%)
**Current:** Text-only problems
**Gaps:**
- No text-to-speech
- No simplified text
- No visual summaries
**Recommendations:**
- TTS integration
- Simplified language mode
- Visual problem summaries
- Chunked text presentation

### 4.3 Persona-Based Intervention Matrix

| Intervention | Alex | Brianna | Cameron | Dylan | Eve | Fay | Grace | Henry | Ivy | Jack | Kevin | Liam |
|--------------|------|---------|---------|-------|-----|-----|-------|-------|-----|------|-------|------|
| **Adaptive difficulty** | ↑ | → | ↓ | ↓ | ↓↓ | ↓ | → | → | → | ↓ | → | ↓ |
| **Visual scaffolding** | - | ★★ | ★ | ★ | ★★ | ★ | ★★ | ★ | - | - | ★★ | ★★ |
| **Text-to-speech** | - | - | - | - | ★ | - | - | - | - | - | - | ★★ |
| **Extended time** | - | - | - | ★ | ★★ | ★ | ★ | ★★ | - | - | ★ | ★ |
| **Hint intensity** | - | ★ | ★★ | ★★ | ★★★ | ★★ | ★★★ | ★★ | ★ | ★ | ★ | ★★ |
| **Gamification** | ★ | ★ | ★★★ | ★★★ | ★★ | ★★★ | ★★ | ★ | - | ★★ | ★ | ★ |
| **Anxiety support** | - | - | - | ★ | ★ | - | ★ | ★★★ | - | - | - | ★ |
| **Focus mode** | - | - | ★ | ★★★ | ★ | ★★ | ★ | ★ | - | ★ | ★ | ★ |
| **Social features** | ★★ | ★ | ★★★ | ★ | - | ★ | ★ | - | ★ | - | ★ | - |

★ = Beneficial, ★★ = Highly beneficial, ★★★ = Critical

---

## 5. Integrated Recommendations

### 5.1 Priority Matrix

| Priority | Initiative | Impact | Effort | Personas Helped |
|----------|-----------|--------|--------|-----------------|
| **P0** | Persona classification system | HIGH | MEDIUM | All 12 |
| **P0** | Adaptive problem selection | HIGH | HIGH | All 12 |
| **P0** | Interactive model canvas | HIGH | HIGH | Brianna, Kevin, Grace |
| **P1** | Gaming detection (Jack) | HIGH | MEDIUM | Jack, Fay |
| **P1** | Anxiety-reducing UI (Henry) | HIGH | LOW | Henry, Eve |
| **P1** | Accessibility features (Liam) | HIGH | MEDIUM | Liam, Eve |
| **P2** | Spaced repetition system | MEDIUM | HIGH | All 12 |
| **P2** | Social/collaborative features | MEDIUM | HIGH | Cameron, Alex |
| **P2** | Parent/teacher dashboards | MEDIUM | MEDIUM | All 12 |
| **P3** | Narrative/adventure mode | MEDIUM | HIGH | Cameron, Fay |
| **P3** | Mobile app | LOW | HIGH | Dylan, Cameron |

### 5.2 Implementation Roadmap

#### Phase 1: Foundation (Weeks 1-4)
1. **Persona Classification System**
   - Backend: Classification algorithm
   - Database: Persona profile storage
   - Frontend: Persona onboarding flow

2. **Basic Adaptive Selection**
   - Difficulty adjustment per persona
   - Problem type weighting
   - Simple spaced repetition

3. **Critical Accessibility**
   - Text-to-speech
   - Simplified text mode
   - Anxiety-reducing UI option

#### Phase 2: Core Features (Weeks 5-8)
1. **Interactive Model Canvas**
   - Bar model drawing
   - Grid construction
   - Annotation tools

2. **Gaming Detection**
   - Behavioral analytics
   - Intervention messages
   - Teacher alerts

3. **Enhanced Scaffolding**
   - Tiered hint system
   - Prerequisite review
   - Strategy instruction

#### Phase 3: Advanced Features (Weeks 9-12)
1. **Social Features**
   - Peer discussion
   - Study groups
   - Parent dashboard

2. **Narrative Mode**
   - Adventure storyline
   - Unlockable content
   - Variable rewards

3. **Mobile Optimization**
   - Touch interfaces
   - Offline mode
   - Push notifications

### 5.3 Success Metrics by Persona

| Persona | Primary Metric | Target |
|---------|---------------|--------|
| Alex | Challenge completion rate | 90% |
| Brianna | Visual tool usage | 80% |
| Cameron | Session completion | 70% |
| Dylan | Focus time per session | 15 min |
| Eve | Help-seeking → success rate | 60% |
| Fay | Random guessing reduction | 50% |
| Grace | Pathway accuracy | 75% |
| Henry | Anxiety self-report reduction | 30% |
| Ivy | UI satisfaction | 4/5 |
| Jack | Gaming incidents | <5% |
| Kevin | Articulation quality | Level 2+ |
| Liam | Reading comprehension | 70% |

---

## Appendix: Technical Architecture Recommendations

### Recommended Tech Stack Additions

| Component | Current | Recommended |
|-----------|---------|-------------|
| **Database** | In-memory | PostgreSQL + Redis |
| **ML/AI** | None | scikit-learn (persona classification) |
| **Analytics** | Basic | Mixpanel/Amplitude |
| **Canvas** | None | Fabric.js or Konva.js |
| **TTS** | None | Web Speech API or AWS Polly |
| **Mobile** | Responsive | React Native or PWA |

### API Extensions Needed

```python
# New endpoints for persona-aware system

@app.post("/personas/classify")
def classify_student(assessment_data: AssessmentData) -> PersonaProfile:
    """Classify student into 1 of 12 personas"""
    pass

@app.get("/problems/adaptive")
def get_adaptive_problem(
    student_id: str,
    session_context: SessionContext
) -> Problem:
    """Get next problem based on persona and mastery"""
    pass

@app.post("/interventions/suggest")
def suggest_intervention(
    student_id: str,
    struggle_pattern: StrugglePattern
) -> Intervention:
    """AI-powered intervention suggestion"""
    pass

@app.get("/analytics/persona/{persona_id}")
def get_persona_analytics(
    persona_id: str,
    time_range: TimeRange
) -> PersonaAnalytics:
    """Aggregated data for persona optimization"""
    pass
```

---

## Conclusion

The ATOM-SG Pilot has significant gaps across all dimensions:

1. **Pedagogical:** Lacks differentiated instruction, metacognitive training, and transfer practice
2. **Backend:** Missing persona-aware data model, adaptive algorithms, and robust analytics
3. **Frontend:** Insufficient accessibility, no interactive tools, limited persona-specific UX
4. **Persona Coverage:** Only Alex (perfect student) is well-supported; 11 personas have major gaps

**Estimated effort to close all gaps:** 3-4 months with 2-3 developers
**Recommended priority:** Focus on P0 items (persona classification, adaptive selection, model canvas) for pilot success.
