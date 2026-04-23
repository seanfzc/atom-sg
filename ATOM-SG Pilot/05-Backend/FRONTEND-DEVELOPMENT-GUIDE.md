# Frontend Development Guide - ATOM-SG Pilot MVP

## Quick Start

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend:**
   ```bash
   python main.py
   ```

3. **Open in browser:**
   ```
   http://localhost:5000/
   ```

## Architecture Overview

The frontend is a **Single Page Application (SPA)** built with vanilla JavaScript. All pages are loaded in a single HTML file (`index.html`), and navigation is handled by showing/hiding sections.

### Technology Stack
- **HTML5** - Semantic markup
- **CSS3** - Styling with Flexbox/Grid
- **JavaScript (ES6+)** - No frameworks
- **Fetch API** - HTTP requests
- **Canvas API** - Diagram annotations

## Module Structure

### Core Modules
1. **api.js** - Backend API client
2. **navigation.js** - Page routing
3. **main.js** - Entry point & global utilities

### Feature Modules
4. **dashboard.js** - Progress dashboard
5. **baseline.js** - Baseline test upload
6. **practice.js** - Daily practice session
7. **pathway-radar.js** - Warm-up drill
8. **transfer.js** - Transfer test upload
9. **reflections.js** - Digital reflection sheets
10. **canvas.js** - Diagram annotations

## API Integration

All backend communication goes through `api.js`. The API client handles:
- Request/response formatting
- Error handling
- Headers management
- Base URL configuration

### Example API Call
```javascript
// Get problems with filters
const problems = await api.getProblems({
    track: 'word-problems',
    pathway: 'before-after-change',
    week: 2
});

// Submit practice answer
const result = await api.submitPracticeSession(sessionId, {
    problemId: 'prob_001',
    pathwayType: 'before-after-change',
    equationShadow: 'Sequential changes, find original',
    studentAnswer: {
        type: 'numeric',
        value: 300
    }
});
```

## Page Navigation

Navigation is handled by the `Navigation` class in `navigation.js`. Pages are identified by `data-page` attributes:

```html
<nav class="navbar">
    <ul class="nav-links">
        <li><a href="#" data-page="dashboard" class="active">Dashboard</a></li>
        <li><a href="#" data-page="practice">Daily Practice</a></li>
    </ul>
</nav>

<main class="main-content">
    <section id="page-dashboard" class="page active">
        <!-- Dashboard content -->
    </section>
    
    <section id="page-practice" class="page">
        <!-- Practice content -->
    </section>
</main>
```

### Programmatic Navigation
```javascript
// Navigate to a page
window.dispatchEvent(new CustomEvent('pageLoad', { detail: { page: 'practice' }}));

// Navigate via navigation instance
navigation.navigateTo('practice');
```

## Component Patterns

### 1. Data Loading Pattern
```javascript
class ExampleFeature {
    async loadData() {
        try {
            const data = await api.getEndpoint();
            this.renderData(data);
        } catch (error) {
            console.error('Failed to load data:', error);
            this.showError();
        }
    }
    
    renderData(data) {
        // Render data to DOM
    }
    
    showError() {
        // Show error message
    }
}
```

### 2. Form Submission Pattern
```javascript
class ExampleForm {
    init() {
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleSubmit();
        });
    }
    
    async handleSubmit() {
        const formData = this.gatherFormData();
        this.setLoadingState(true);
        
        try {
            const result = await api.submitData(formData);
            this.showSuccess(result);
        } catch (error) {
            this.showError(error);
        } finally {
            this.setLoadingState(false);
        }
    }
    
    gatherFormData() {
        // Extract values from form inputs
    }
    
    setLoadingState(isLoading) {
        // Show/hide loading spinner
    }
}
```

### 3. Polling Pattern (for async operations)
```javascript
class PollingFeature {
    async pollForResult(operationId, maxAttempts = 12, interval = 2500) {
        for (let i = 0; i < maxAttempts; i++) {
            const result = await api.checkStatus(operationId);
            
            if (result.status === 'completed') {
                return result;
            }
            
            // Wait before next poll
            await new Promise(resolve => setTimeout(resolve, interval));
        }
        
        throw new Error('Operation timed out');
    }
}
```

## Styling Guide

### CSS Variables
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #7c3aed;
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --danger-color: #ef4444;
}
```

### Utility Classes
```css
.hidden { display: none !important; }
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
```

### Responsive Breakpoints
```css
/* Desktop */
@media (min-width: 1024px) {
    /* Desktop styles */
}

/* Mobile */
@media (max-width: 768px) {
    /* Mobile styles */
}
```

## Debugging

### Console Logging
```javascript
console.log('Message');           // Regular log
console.error('Error');           // Error log
console.warn('Warning');           // Warning log
console.table(data);              // Tabular data
console.group('Section');         // Grouped logs
console.groupEnd();
```

### Network Debugging
1. Open DevTools (F12)
2. Go to Network tab
3. Filter by "Fetch/XHR"
4. Click request to see:
   - Request headers
   - Request payload
   - Response data
   - Status code

### Common Issues

**Issue: API calls failing**
- Check if backend is running
- Verify API endpoint URL
- Check browser console for CORS errors
- Verify request/response format

**Issue: Canvas not drawing**
- Verify canvas element exists in DOM
- Check canvas context initialization
- Look for JavaScript errors
- Try clearing browser cache

**Issue: Navigation not working**
- Verify `data-page` attributes match section IDs
- Check if JavaScript is enabled
- Look for errors in navigation.js
- Verify event listeners are attached

## Performance Tips

1. **Minimize API calls:** Cache responses in `localStorage`
2. **Lazy load images:** Use `loading="lazy"` attribute
3. **Debounce inputs:** Add delay to search/filter inputs
4. **Throttle events:** Limit frequency of scroll/resize handlers
5. **Optimize images:** Use WebP format when possible
6. **Minify CSS/JS:** (Optional for production)

## Accessibility Checklist

- [ ] Semantic HTML5 elements used
- [ ] Proper heading hierarchy (h1, h2, h3)
- [ ] Labels for all form inputs
- [ ] Alt text for images
- [ ] ARIA labels for interactive elements
- [ ] Keyboard navigation support
- [ ] Sufficient color contrast (4.5:1 for text)
- [ ] Focus indicators for interactive elements

## Testing Checklist

### Functional Testing
- [ ] All pages load correctly
- [ ] Navigation works smoothly
- [ ] API calls return data
- [ ] Forms submit successfully
- [ ] Canvas annotations work
- [ ] File uploads work
- [ ] Polling operations complete

### Visual Testing
- [ ] Layout looks correct on desktop
- [ ] Responsive design works on tablet
- [ ] Responsive design works on mobile
- [ ] All buttons are clickable
- [ ] All forms are usable
- [ ] Color scheme is consistent

### Cross-Browser Testing
- [ ] Works in Chrome
- [ ] Works in Safari
- [ ] Works in Edge
- [ ] Works in Firefox

### Performance Testing
- [ ] Page loads within 3 seconds
- [ ] API calls complete within 1 second
- [ ] No memory leaks
- [ ] No console errors

## Contributing

When adding new features:
1. Follow existing code patterns
2. Use semantic HTML
3. Add comments for complex logic
4. Update this guide
5. Test across browsers
6. Check accessibility

## Resources

- [MDN Web Docs](https://developer.mozilla.org/)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
- [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
