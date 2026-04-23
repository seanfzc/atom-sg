// GamingDetector.js - Client-side Gaming Detection
// Tracks click patterns, speed vs accuracy, help abuse, and suspicious behavior

class GamingDetector {
    constructor(options = {}) {
        this.options = {
            apiEndpoint: options.apiEndpoint || '/api/gaming-report',
            reportInterval: options.reportInterval || 30000, // Report every 30 seconds
            maxEvents: options.maxEvents || 1000,
            enableAlerts: options.enableAlerts !== false,
            alertThreshold: options.alertThreshold || 0.7,
            ...options
        };
        
        // Tracking state
        this.events = [];
        this.sessionStartTime = Date.now();
        this.lastActivityTime = Date.now();
        this.isActive = false;
        
        // Metrics
        this.metrics = {
            clicks: [],
            keypresses: [],
            helpRequests: [],
            answerSubmissions: [],
            navigationEvents: [],
            timeOnTask: 0,
            suspiciousScore: 0
        };
        
        // Pattern detection
        this.patterns = {
            rapidClicks: 0,
            repetitiveAnswers: 0,
            helpAbuseCount: 0,
            speedAnomalies: [],
            accuracyHistory: []
        };
        
        // Initialize
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.startReporting();
        this.isActive = true;
        
        console.log('[GamingDetector] Initialized');
    }
    
    setupEventListeners() {
        // Click tracking
        document.addEventListener('click', (e) => {
            this.recordClick(e);
        });
        
        // Keypress tracking
        document.addEventListener('keydown', (e) => {
            this.recordKeypress(e);
        });
        
        // Navigation tracking
        window.addEventListener('beforeunload', () => {
            this.recordNavigation('page_exit');
        });
        
        // Visibility tracking
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.recordEvent('tab_hidden');
            } else {
                this.recordEvent('tab_visible');
            }
        });
        
        // Listen for application-specific events
        document.addEventListener('practiceSubmitted', (e) => {
            this.recordAnswerSubmission(e.detail);
        });
        
        document.addEventListener('helpRequested', (e) => {
            this.recordHelpRequest(e.detail);
        });
        
        document.addEventListener('hintShown', (e) => {
            this.recordHintRequest(e.detail);
        });
    }
    
    recordClick(e) {
        const now = Date.now();
        const clickData = {
            type: 'click',
            timestamp: now,
            x: e.clientX,
            y: e.clientY,
            target: this.getElementSelector(e.target),
            timeSinceLastClick: this.metrics.clicks.length > 0 
                ? now - this.metrics.clicks[this.metrics.clicks.length - 1].timestamp 
                : null
        };
        
        this.metrics.clicks.push(clickData);
        this.events.push(clickData);
        
        // Check for rapid clicking pattern
        if (clickData.timeSinceLastClick && clickData.timeSinceLastClick < 100) {
            this.patterns.rapidClicks++;
        }
        
        this.lastActivityTime = now;
        this.trimEvents();
    }
    
    recordKeypress(e) {
        const now = Date.now();
        const keyData = {
            type: 'keypress',
            timestamp: now,
            key: e.key,
            ctrlKey: e.ctrlKey,
            metaKey: e.metaKey,
            target: this.getElementSelector(e.target)
        };
        
        this.metrics.keypresses.push(keyData);
        this.events.push(keyData);
        this.lastActivityTime = now;
        this.trimEvents();
    }
    
    recordAnswerSubmission(data) {
        const now = Date.now();
        const submission = {
            type: 'answer_submission',
            timestamp: now,
            problemId: data.problemId,
            timeSpent: data.timeSpent,
            correct: data.correct,
            pathway: data.pathway,
            helpUsed: data.helpUsed || false
        };
        
        this.metrics.answerSubmissions.push(submission);
        this.events.push(submission);
        
        // Track accuracy
        this.patterns.accuracyHistory.push({
            timestamp: now,
            correct: data.correct
        });
        
        // Check for speed vs accuracy anomaly
        if (data.timeSpent && data.timeSpent < 5000 && data.correct) {
            // Very fast correct answer - might indicate prior knowledge or gaming
            this.patterns.speedAnomalies.push({
                type: 'fast_correct',
                timeSpent: data.timeSpent,
                timestamp: now
            });
        }
        
        this.lastActivityTime = now;
        this.trimEvents();
    }
    
    recordHelpRequest(data) {
        const now = Date.now();
        const help = {
            type: 'help_request',
            timestamp: now,
            helpType: data.type || 'general',
            problemId: data.problemId
        };
        
        this.metrics.helpRequests.push(help);
        this.events.push(help);
        
        // Check for help abuse
        const recentHelps = this.metrics.helpRequests.filter(h => 
            now - h.timestamp < 60000 // Last minute
        );
        
        if (recentHelps.length > 5) {
            this.patterns.helpAbuseCount++;
        }
        
        this.lastActivityTime = now;
        this.trimEvents();
    }
    
    recordHintRequest(data) {
        const now = Date.now();
        const hint = {
            type: 'hint_request',
            timestamp: now,
            hintLevel: data.level || 1,
            problemId: data.problemId
        };
        
        this.metrics.helpRequests.push(hint);
        this.events.push(hint);
        this.lastActivityTime = now;
        this.trimEvents();
    }
    
    recordNavigation(type) {
        const nav = {
            type: 'navigation',
            timestamp: Date.now(),
            navType: type,
            url: window.location.href
        };
        
        this.metrics.navigationEvents.push(nav);
        this.events.push(nav);
        this.trimEvents();
    }
    
    recordEvent(type, data = {}) {
        const event = {
            type: type,
            timestamp: Date.now(),
            ...data
        };
        
        this.events.push(event);
        this.trimEvents();
    }
    
    getElementSelector(element) {
        if (!element) return 'unknown';
        
        const parts = [];
        let current = element;
        
        while (current && current !== document.body) {
            let selector = current.tagName.toLowerCase();
            
            if (current.id) {
                selector += `#${current.id}`;
                parts.unshift(selector);
                break;
            }
            
            if (current.className) {
                const classes = current.className.split(' ').filter(c => c);
                if (classes.length > 0) {
                    selector += `.${classes.slice(0, 2).join('.')}`;
                }
            }
            
            parts.unshift(selector);
            current = current.parentElement;
        }
        
        return parts.join(' > ');
    }
    
    trimEvents() {
        if (this.events.length > this.options.maxEvents) {
            this.events = this.events.slice(-this.options.maxEvents);
        }
    }
    
    // Analysis methods
    analyzeClickPatterns() {
        const clicks = this.metrics.clicks;
        if (clicks.length < 10) return { score: 0, patterns: [] };
        
        const patterns = [];
        let suspiciousScore = 0;
        
        // Check for repetitive clicking (same location)
        const locationGroups = {};
        clicks.forEach(click => {
            const key = `${Math.round(click.x / 10)},${Math.round(click.y / 10)}`;
            locationGroups[key] = (locationGroups[key] || 0) + 1;
        });
        
        const maxRepeats = Math.max(...Object.values(locationGroups));
        if (maxRepeats > clicks.length * 0.5) {
            patterns.push('repetitive_location');
            suspiciousScore += 0.3;
        }
        
        // Check for inhumanly fast clicking
        const rapidClicks = clicks.filter((c, i) => {
            if (i === 0) return false;
            return c.timeSinceLastClick < 50; // Less than 50ms
        });
        
        if (rapidClicks.length > clicks.length * 0.3) {
            patterns.push('rapid_clicking');
            suspiciousScore += 0.4;
        }
        
        // Check for rhythmic clicking (bot-like)
        const intervals = clicks.slice(1).map(c => c.timeSinceLastClick).filter(t => t);
        if (intervals.length > 10) {
            const avg = intervals.reduce((a, b) => a + b, 0) / intervals.length;
            const variance = intervals.reduce((sum, t) => sum + Math.pow(t - avg, 2), 0) / intervals.length;
            const cv = Math.sqrt(variance) / avg; // Coefficient of variation
            
            if (cv < 0.1 && avg < 200) {
                patterns.push('rhythmic_clicking');
                suspiciousScore += 0.5;
            }
        }
        
        return { score: Math.min(suspiciousScore, 1), patterns };
    }
    
    analyzeSpeedVsAccuracy() {
        const submissions = this.metrics.answerSubmissions;
        if (submissions.length < 3) return { score: 0, patterns: [] };
        
        const patterns = [];
        let suspiciousScore = 0;
        
        // Calculate average time per answer
        const times = submissions.map(s => s.timeSpent).filter(t => t);
        const avgTime = times.reduce((a, b) => a + b, 0) / times.length;
        
        // Check for suspicious speed
        const fastAnswers = submissions.filter(s => s.timeSpent < 3000);
        if (fastAnswers.length > submissions.length * 0.5) {
            patterns.push('excessive_speed');
            suspiciousScore += 0.3;
        }
        
        // Check for speed-accuracy paradox (very fast but always correct)
        const fastCorrect = submissions.filter(s => s.timeSpent < 5000 && s.correct);
        if (fastCorrect.length > submissions.length * 0.7) {
            patterns.push('speed_accuracy_paradox');
            suspiciousScore += 0.4;
        }
        
        // Check for consistent timing (bot-like)
        if (times.length > 5) {
            const variance = times.reduce((sum, t) => sum + Math.pow(t - avgTime, 2), 0) / times.length;
            const cv = Math.sqrt(variance) / avgTime;
            
            if (cv < 0.15) {
                patterns.push('consistent_timing');
                suspiciousScore += 0.3;
            }
        }
        
        return { score: Math.min(suspiciousScore, 1), patterns, avgTime };
    }
    
    analyzeHelpAbuse() {
        const helps = this.metrics.helpRequests;
        if (helps.length < 3) return { score: 0, patterns: [] };
        
        const patterns = [];
        let suspiciousScore = 0;
        
        // Check for help-before-attempt pattern
        const submissions = this.metrics.answerSubmissions;
        const helpBeforeAttempt = helps.filter(h => {
            const nextSubmission = submissions.find(s => s.timestamp > h.timestamp);
            return nextSubmission && (nextSubmission.timestamp - h.timestamp < 2000);
        });
        
        if (helpBeforeAttempt.length > helps.length * 0.5) {
            patterns.push('help_before_attempt');
            suspiciousScore += 0.4;
        }
        
        // Check for excessive help usage
        const helpRate = helps.length / Math.max(submissions.length, 1);
        if (helpRate > 2) {
            patterns.push('excessive_help_usage');
            suspiciousScore += 0.3;
        }
        
        // Check for rapid help requests
        const now = Date.now();
        const recentHelps = helps.filter(h => now - h.timestamp < 300000); // Last 5 minutes
        if (recentHelps.length > 10) {
            patterns.push('rapid_help_requests');
            suspiciousScore += 0.3;
        }
        
        return { score: Math.min(suspiciousScore, 1), patterns, helpRate };
    }
    
    analyzeNavigationPatterns() {
        const navs = this.metrics.navigationEvents;
        if (navs.length < 2) return { score: 0, patterns: [] };
        
        const patterns = [];
        let suspiciousScore = 0;
        
        // Check for excessive tab switching
        const tabHides = this.events.filter(e => e.type === 'tab_hidden');
        if (tabHides.length > 5) {
            patterns.push('excessive_tab_switching');
            suspiciousScore += 0.2;
        }
        
        // Check for copy-paste behavior
        const pasteEvents = this.metrics.keypresses.filter(k => k.ctrlKey && k.key === 'v');
        if (pasteEvents.length > 3) {
            patterns.push('copy_paste_detected');
            suspiciousScore += 0.3;
        }
        
        return { score: Math.min(suspiciousScore, 1), patterns };
    }
    
    calculateGamingScore() {
        const clickAnalysis = this.analyzeClickPatterns();
        const speedAnalysis = this.analyzeSpeedVsAccuracy();
        const helpAnalysis = this.analyzeHelpAbuse();
        const navAnalysis = this.analyzeNavigationPatterns();
        
        // Weighted combination
        const weights = {
            clicks: 0.25,
            speed: 0.35,
            help: 0.25,
            navigation: 0.15
        };
        
        const totalScore = 
            clickAnalysis.score * weights.clicks +
            speedAnalysis.score * weights.speed +
            helpAnalysis.score * weights.help +
            navAnalysis.score * weights.navigation;
        
        const allPatterns = [
            ...clickAnalysis.patterns,
            ...speedAnalysis.patterns,
            ...helpAnalysis.patterns,
            ...navAnalysis.patterns
        ];
        
        return {
            score: totalScore,
            confidence: Math.min((this.events.length / 100), 1),
            patterns: [...new Set(allPatterns)],
            breakdown: {
                clicks: clickAnalysis,
                speed: speedAnalysis,
                help: helpAnalysis,
                navigation: navAnalysis
            }
        };
    }
    
    // Reporting methods
    startReporting() {
        this.reportInterval = setInterval(() => {
            this.reportToBackend();
        }, this.options.reportInterval);
    }
    
    async reportToBackend() {
        if (!this.isActive || this.events.length === 0) return;
        
        const analysis = this.calculateGamingScore();
        const sessionDuration = Date.now() - this.sessionStartTime;
        
        const report = {
            timestamp: Date.now(),
            sessionDuration: sessionDuration,
            eventCount: this.events.length,
            gamingScore: analysis.score,
            confidence: analysis.confidence,
            detectedPatterns: analysis.patterns,
            metrics: {
                clickCount: this.metrics.clicks.length,
                keypressCount: this.metrics.keypresses.length,
                helpRequestCount: this.metrics.helpRequests.length,
                submissionCount: this.metrics.answerSubmissions.length,
                avgTimePerAnswer: analysis.breakdown.speed.avgTime,
                helpRate: analysis.breakdown.help.helpRate
            },
            recentEvents: this.events.slice(-50) // Last 50 events
        };
        
        try {
            const response = await fetch(this.options.apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(report)
            });
            
            if (response.ok) {
                const result = await response.json();
                
                // Handle backend response
                if (result.action === 'warn') {
                    this.showWarning(result.message);
                } else if (result.action === 'cooldown') {
                    this.triggerCooldown(result.duration);
                }
            }
        } catch (error) {
            console.error('[GamingDetector] Failed to report:', error);
        }
        
        // Check for local alert threshold
        if (this.options.enableAlerts && analysis.score > this.options.alertThreshold) {
            this.showLocalWarning(analysis);
        }
    }
    
    showWarning(message) {
        // Create warning notification
        const warning = document.createElement('div');
        warning.className = 'gaming-warning-notification';
        warning.innerHTML = `
            <div class="gaming-warning-content">
                <span class="gaming-warning-icon">⚠️</span>
                <span class="gaming-warning-message">${message}</span>
                <button class="gaming-warning-close">&times;</button>
            </div>
        `;
        
        document.body.appendChild(warning);
        
        warning.querySelector('.gaming-warning-close').addEventListener('click', () => {
            warning.remove();
        });
        
        // Auto-remove after 10 seconds
        setTimeout(() => {
            warning.remove();
        }, 10000);
    }
    
    showLocalWarning(analysis) {
        const messages = {
            'rapid_clicking': 'We noticed very fast clicking. Please take your time.',
            'repetitive_location': 'Multiple clicks detected in the same area.',
            'rhythmic_clicking': 'Unusual clicking pattern detected.',
            'excessive_speed': 'You\'re answering very quickly. Consider reviewing the material.',
            'speed_accuracy_paradox': 'Unusually fast correct answers detected.',
            'consistent_timing': 'Very consistent answer timing detected.',
            'help_before_attempt': 'Using help before attempting the problem.',
            'excessive_help_usage': 'High rate of help requests detected.',
            'rapid_help_requests': 'Multiple help requests in short time.',
            'excessive_tab_switching': 'Frequent tab switching detected.',
            'copy_paste_detected': 'Copy-paste behavior detected.'
        };
        
        const primaryPattern = analysis.patterns[0];
        const message = messages[primaryPattern] || 'Unusual activity detected. Please focus on learning.';
        
        this.showWarning(message);
        
        // Dispatch event for other components
        document.dispatchEvent(new CustomEvent('gamingDetected', { 
            detail: { score: analysis.score, patterns: analysis.patterns }
        }));
    }
    
    triggerCooldown(duration) {
        // Dispatch cooldown event
        document.dispatchEvent(new CustomEvent('gamingCooldown', { 
            detail: { duration }
        }));
        
        // Show cooldown UI
        const overlay = document.createElement('div');
        overlay.className = 'gaming-cooldown-overlay';
        overlay.innerHTML = `
            <div class="gaming-cooldown-content">
                <h2>⏸️ Taking a Short Break</h2>
                <p>We've detected unusual activity. Please take a moment to refocus.</p>
                <div class="gaming-cooldown-timer">${Math.ceil(duration / 60)}:00</div>
                <p class="gaming-cooldown-message">Time remaining until you can continue</p>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        // Start countdown
        let remaining = duration;
        const timerEl = overlay.querySelector('.gaming-cooldown-timer');
        
        const countdown = setInterval(() => {
            remaining--;
            const mins = Math.floor(remaining / 60);
            const secs = remaining % 60;
            timerEl.textContent = `${mins}:${String(secs).padStart(2, '0')}`;
            
            if (remaining <= 0) {
                clearInterval(countdown);
                overlay.remove();
                document.dispatchEvent(new CustomEvent('gamingCooldownEnd'));
            }
        }, 1000);
    }
    
    // Public API
    getMetrics() {
        return {
            ...this.metrics,
            sessionDuration: Date.now() - this.sessionStartTime,
            eventCount: this.events.length
        };
    }
    
    getAnalysis() {
        return this.calculateGamingScore();
    }
    
    reset() {
        this.events = [];
        this.metrics = {
            clicks: [],
            keypresses: [],
            helpRequests: [],
            answerSubmissions: [],
            navigationEvents: [],
            timeOnTask: 0,
            suspiciousScore: 0
        };
        this.patterns = {
            rapidClicks: 0,
            repetitiveAnswers: 0,
            helpAbuseCount: 0,
            speedAnomalies: [],
            accuracyHistory: []
        };
        this.sessionStartTime = Date.now();
    }
    
    destroy() {
        this.isActive = false;
        if (this.reportInterval) {
            clearInterval(this.reportInterval);
        }
    }
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GamingDetector;
}
