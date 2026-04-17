# ATOM-SG Pilot MVP - Frontend Documentation

Static HTML5 + JavaScript frontend for the ATOM-SG Pilot v4.1 Recognition-First Integrated Training system.

## Overview

The frontend is built with vanilla HTML5, CSS3, and JavaScript (ES6+). No frameworks or build tools are required, making it lightweight and easy to deploy.

## File Structure

```
frontend/
├── index.html                    # Main HTML file (single-page application)
└── static/
    ├── css/
    │   └── style.css            # Main stylesheet
    └── js/
        ├── api.js               # API client module
        ├── navigation.js        # Page navigation
        ├── dashboard.js         # Dashboard functionality
        ├── baseline.js          # Baseline test upload
        ├── practice.js          # Daily practice session
        ├── pathway-radar.js     # Pathway radar warm-up
        ├── transfer.js          # Transfer test upload
        ├── reflections.js       # Digital reflection sheets
        ├── canvas.js            # Diagram annotation canvas
        └── main.js              # Main entry point
```

## Getting Started

1. **Ensure backend is running:**
   ```bash
   cd ATOM-SG\ Pilot/05-Backend
   python main.py
   ```

2. **Open in browser:**
   ```
   http://localhost:5000/
   ```

3. **Frontend will be served from:** `/static/*` endpoints

## Pages & Features

### 1. Dashboard
- **Features:**
  - Progress statistics (problems completed, avg score, ID accuracy, articulation level)
  - Milestone tracking with progress bars
  - Weekly progress timeline
  - Pathway performance heatmap

- **Endpoints Used:**
  - `GET /api/v1/milestones`
  - `GET /api/v1/analytics/progress`
  - `GET /api/v1/analytics/baseline`

### 2. Baseline Test
- **Features:**
  - Print baseline test PDF (Week 1)
  - Upload completed test for OCR processing
  - Display gap map with weakest 3 pathways
  - View all pathway scores

- **Endpoints Used:**
  - `GET /api/v1/problems/pdf?week=1`
  - `POST /api/v1/scans` (with `week=1`)
  - `GET /api/v1/scans/{id}` (polling for OCR completion)
  - `GET /api/v1/analytics/baseline`

- **User Flow:**
  1. Click "Print Baseline Test"
  2. Student completes 40-question paper test
  3. Parent/teacher scans and uploads
  4. System processes OCR (30 seconds)
  5. Display gap map results

### 3. Daily Practice
- **Features:**
  - Pathway Radar warm-up (10 questions, 5 minutes)
  - Practice session with curated problems
  - Forced articulation form (pathway type + equation shadow)
  - Diagram annotation canvas (pen, line, eraser tools)
  - Triad feedback (pathway ID + articulation + solution)
  - Model articulation comparison
  - Progress tracking

- **Endpoints Used:**
  - `GET /api/v1/pathway-radar/questions`
  - `POST /api/v1/pathway-radar/submit`
  - `POST /api/v1/practice-sessions`
  - `GET /api/v1/practice-sessions/{id}`
  - `POST /api/v1/practice-sessions/{id}/submit`
  - `PATCH /api/v1/milestones/{id}`

- **User Flow:**
  1. Start Pathway Radar warm-up (optional)
  2. Answer 10 identification questions
  3. Submit and view strong/weak pathway feedback
  4. Start Practice Session
  5. View problem with embedded diagram
  6. Complete forced articulation (pathway type + equation shadow)
  7. Annotate diagram with canvas tools (optional)
  8. Solve problem
  9. Submit and receive triad feedback
  10. View model articulation for comparison
  11. Continue to next problem

### 4. Pathway Radar
- **Features:**
  - Visual radar chart of pathway distribution
  - Historical performance (placeholder)
  - Quick link to start daily practice

- **Endpoints Used:**
  - `GET /api/v1/pathway-radar/questions`

### 5. Transfer Test
- **Features:**
  - Print transfer test PDF (Week 5)
  - Upload completed test for OCR processing
  - Display ramp-up metrics
  - Show success criteria with pass/fail status

- **Endpoints Used:**
  - `GET /api/v1/problems/pdf?week=5`
  - `POST /api/v1/scans` (with `week=5`)
  - `GET /api/v1/analytics/transfer`

- **User Flow:**
  1. Click "Print Transfer Test"
  2. Student completes 40 new unseen problems
  3. Parent/teacher scans and uploads
  4. System processes OCR
  5. Display ramp-up metrics (baseline vs. transfer)
  6. View success criteria (90% ID accuracy, 90% articulation Level 2+, 80% solving improvement)

### 6. Reflections
- **Features:**
  - Digital reflection sheet form
  - Week and pathway selection
  - Reflection text input
  - Confidence slider (1-5)
  - Struggles and improvements checkboxes
  - View previous reflections

- **Endpoints Used:**
  - `POST /api/v1/reflections`
  - `GET /api/v1/reflections`

## JavaScript Modules

### api.js
Handles all backend API communication using the Fetch API.

**Key Methods:**
- `getProblems(filters)` - List problems
- `getProblem(problemId)` - Get problem details
- `uploadScan(week, file)` - Upload scan for OCR
- `createPracticeSession(data)` - Start practice session
- `submitPracticeSession(sessionId, submission)` - Submit answer
- `getPathwayRadarQuestions(date)` - Get warm-up questions
- `submitPathwayRadar(submission)` - Submit radar answers
- `getMilestones()` - Get progress milestones
- `getBaselineAnalytics()` - Get baseline results
- `getTransferAnalytics()` - Get ramp-up metrics
- `createReflection(data)` - Submit reflection

### navigation.js
Handles single-page navigation and active state management.

**Features:**
- Hash-based routing (`#dashboard`, `#practice`, etc.)
- Browser history management
- Active link highlighting
- Smooth page transitions

### canvas.js
Handles diagram annotation canvas functionality.

**Tools:**
- Pen (freehand drawing)
- Line (straight lines)
- Eraser
- Clear All

**Methods:**
- `saveAnnotations()` - Export canvas as data URL
- `restoreAnnotations()` - Redraw saved annotations
- `clearCanvas()` - Clear all drawings

## CSS Styling

### Color Scheme
- Primary: `#2563eb` (blue)
- Secondary: `#7c3aed` (purple)
- Success: `#10b981` (green)
- Warning: `#f59e0b` (yellow)
- Danger: `#ef4444` (red)
- Dark: `#1f2937`
- Light: `#f3f4f6`

### Responsive Design
- Desktop-first approach (minimum viewport: 1024px × 768px)
- Mobile support (breakpoint: 768px)
- Flexbox and Grid layouts
- Sticky navigation

### Key Components
- `.navbar` - Top navigation bar
- `.stat-card` - Dashboard statistic cards
- `.milestone-item` - Milestone progress item
- `.progress-bar` - Progress indicator
- `.problem-display` - Problem view with diagrams
- `.articulation-form` - Forced articulation form
- `.triad-feedback` - Three-dimensional feedback
- `.feedback-card` - Individual feedback dimension
- `.canvas-container` - Annotation canvas wrapper

## Browser Support

Tested on:
- Chrome 90+
- Safari 14+
- Edge 90+
- Firefox 88+

**Required Features:**
- ES6+ JavaScript support
- CSS Grid and Flexbox
- Fetch API
- Canvas API
- Local Storage (optional)

## Accessibility

- Semantic HTML5 elements (`<nav>`, `<main>`, `<section>`, `<article>`)
- Proper heading hierarchy (h1, h2, h3)
- Labels for all form inputs
- Alt text for images (auto-generated from problem text)
- ARIA labels for interactive elements
- Skip navigation link
- Keyboard navigation support

## Performance Optimization

### Caching Strategy
- Cache problem data in `localStorage` (24-hour TTL)
- Cache diagram renders (SVG) for 7 days
- Cache milestone progress
- Clear cache on new week start

### Best Practices
- Minimize API calls by caching responses
- Lazy load images and renders
- Debounce search inputs
- Throttle scroll events
- Use `requestAnimationFrame` for animations

## Development

### Running Locally
```bash
# Start backend
python main.py

# Open in browser
open http://localhost:5000/
```

### Debugging
- Open browser DevTools (F12)
- Console logs show API calls and errors
- Network tab shows HTTP requests
- Check backend logs for server errors

### Adding New Features
1. Add new HTML section to `index.html`
2. Add CSS styles to `style.css`
3. Create new JS module in `static/js/`
4. Import module in `main.js`
5. Update navigation links

### Testing Checklist
- [ ] All pages load correctly
- [ ] API calls return data
- [ ] Forms submit successfully
- [ ] Canvas annotations work
- [ ] Navigation works smoothly
- [ ] Responsive design on mobile
- [ ] Error handling works
- [ ] Browser compatibility

## Troubleshooting

### Frontend not loading
- Check if backend is running (`python main.py`)
- Verify port 5000 is not in use
- Check browser console for errors
- Clear browser cache

### API calls failing
- Check backend health (`GET /api/v1/system/health`)
- Verify CORS settings in backend
- Check network tab for HTTP errors
- Verify API endpoints are implemented

### Canvas not working
- Verify canvas element exists in DOM
- Check browser support for Canvas API
- Look for JavaScript errors in console
- Try clearing browser cache

### File upload failing
- Check file size limits in backend
- Verify file type (PDF, PNG, JPG)
- Check browser permissions
- Look for network errors

## License

Proprietary - ATOM-SG Pilot Project
