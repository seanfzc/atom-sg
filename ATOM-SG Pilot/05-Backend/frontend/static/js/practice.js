// Practice Session Module
// Handles daily practice, forced articulation, and triad feedback
// P1/P2 Fixes: Timer, loading states, error handling, state management, glossary

class Practice {
    constructor() {
        this.startWarmupBtn = document.getElementById('start-warmup');
        this.startSessionBtn = document.getElementById('start-session');
        this.radarSection = document.getElementById('pathway-radar-section');
        this.sessionSection = document.getElementById('practice-session-section');

        this.currentSession = null;
        this.currentProblem = null;
        this.currentProblemId = null;
        this.currentPathwayType = null;
        this.annotations = [];

        // P1 Fix #6: Time management - timer for practice session
        this.practiceTimer = null;
        this.timeRemaining = 0;
        this.totalProblems = 0;
        this.practiceTimerInterval = null;

        // P1 Fix #12: State management - save form data
        this.formData = {};

        // P2 Fix #5: Auto-save interval
        this.autoSaveInterval = null;

        // P2 Fix #1: Glossary data
        this.glossaryData = {};

        // P1 Fix #7: Confidence history for trend visualization
        this.confidenceHistory = [];

        // Hint tracking for progressive hints
        this.hintCount = 0;
        this.lastHintTime = null;

        // ModelCanvas instance for drawing
        this.modelCanvas = null;

        this.init();

        // Load saved state on startup
        this.loadSavedState();
    }

    init() {
        // Load glossary data (P2 Fix #1)
        this.loadGlossary();

        // Start warmup
        this.startWarmupBtn.addEventListener('click', () => {
            this.startWarmup();
        });

        // Start practice session
        this.startSessionBtn.addEventListener('click', () => {
            this.startSession();
        });

        // Forced articulation confirmation
        const confirmBtn = document.getElementById('confirm-articulation');
        const pathwayType = document.getElementById('pathway-type');
        const equationShadow = document.getElementById('equation-shadow');

        // Enable/disable confirm button based on form validation
        [pathwayType, equationShadow].forEach(input => {
            input.addEventListener('input', () => {
                this.validateArticulationForm();
                // P1 Fix #12: Auto-save form data
                this.saveFormData();
            });
        });

        confirmBtn.addEventListener('click', () => {
            this.confirmArticulation();
        });

        // Submit answer
        document.getElementById('submit-answer').addEventListener('click', () => {
            this.submitAnswer();
        });

        // Next problem
        document.getElementById('next-problem').addEventListener('click', () => {
            this.loadNextProblem();
        });

        // Character count for equation shadow
        equationShadow.addEventListener('input', () => {
            const count = equationShadow.value.length;
            document.getElementById('char-count').textContent = `${count}/500`;
        });

        // P1 Fix #15: Keyboard shortcuts (P2 Fix #4)
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey || e.metaKey) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.submitAnswer();
                } else if (e.key === 'b') {
                    e.preventDefault();
                    this.showGlossaryModal();
                }
            }
        });

        // P1 Fix #13: Handle browser back button
        window.addEventListener('popstate', (e) => {
            if (e.state && e.state.page === 'practice') {
                this.restoreState(e.state);
            }
        });

        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'practice') {
                this.resetPracticeUI();
            }
        });

        // Help modal functionality
        const stuckButton = document.getElementById('stuckButton');
        const helpModal = document.getElementById('help-modal');
        const closeHelpBtn = document.getElementById('close-help');
        const hintBtn = document.getElementById('hint-btn');
        const glossaryBtn = document.getElementById('glossary-btn');
        const exampleBtn = document.getElementById('example-btn');
        const hintContent = document.getElementById('hint-content');
        const exampleContent = document.getElementById('example-content');

        // Open help modal
        if (stuckButton) {
            stuckButton.addEventListener('click', () => {
                helpModal.classList.remove('hidden');
            });
        }

        // Close help modal
        if (closeHelpBtn) {
            closeHelpBtn.addEventListener('click', () => {
                helpModal.classList.add('hidden');
            });
        }

        // Close modal on outside click
        if (helpModal) {
            helpModal.addEventListener('click', (e) => {
                if (e.target === helpModal) {
                    helpModal.classList.add('hidden');
                }
            });
        }

        // Show hint button
        if (hintBtn) {
            hintBtn.addEventListener('click', async () => {
                try {
                    const now = Date.now();
                    const cooldownMs = 30000; // 30 seconds between hints
                    // Check if cooldown active
                    if (this.lastHintTime && (now - this.lastHintTime) < cooldownMs) {
                        const remaining = Math.ceil((cooldownMs - (now - this.lastHintTime)) / 1000);
                        hintContent.innerHTML = `<p><strong>Wait for next hint:</strong> Please think about the previous hint for ${remaining} more seconds.</p>`;
                        hintContent.classList.remove('hidden');
                        return;
                    }
                    // Limit to 3 hints per problem
                    if (this.hintCount >= 3) {
                        hintContent.innerHTML = `<p><strong>Maximum hints reached:</strong> You've received all available hints for this problem. Try your best!</p>`;
                        hintContent.classList.remove('hidden');
                        return;
                    }
                    const problemId = this.currentProblemId;
                    const response = await fetch(`${API_BASE_URL}/problems/${problemId}/hint`);
                    const hint = await response.json();
                    
                    if (hint.success) {
                        this.hintCount++;
                        this.lastHintTime = now;
                        hintContent.innerHTML = `<p><strong>Hint ${this.hintCount}:</strong> ${hint.hint}</p>`;
                        hintContent.classList.remove('hidden');
                        // Disable button temporarily
                        hintBtn.disabled = true;
                        hintBtn.textContent = `Hint ${this.hintCount} Shown (wait 30s)`;
                        // Re-enable after cooldown
                        setTimeout(() => {
                            hintBtn.disabled = false;
                            hintBtn.textContent = 'Show Next Hint';
                        }, cooldownMs);
                    }
                } catch (error) {
                    console.error('Error fetching hint:', error);
                }
            });
        }

        // Open glossary button
        if (glossaryBtn) {
            glossaryBtn.addEventListener('click', () => {
                if (window.openGlossary) {
                    window.openGlossary();
                }
            });
        }

        // Show example button
        if (exampleBtn) {
            exampleBtn.addEventListener('click', async () => {
                try {
                    const pathwayType = this.currentPathwayType;
                    const response = await fetch(`${API_BASE_URL}/pathways/${pathwayType}/example`);
                    const example = await response.json();
                    
                    if (example.success) {
                        exampleContent.innerHTML = `
                            <p><strong>Example Problem:</strong> ${example.example.question}</p>
                            <p><strong>Solution Steps:</strong></p>
                            <ol>
                                ${example.example.steps.map(step => `<li>${step}</li>`).join('')}
                            </ol>
                        `;
                        exampleContent.classList.remove('hidden');
                        exampleBtn.disabled = true;
                        exampleBtn.textContent = 'Example Shown';
                    }
                } catch (error) {
                    console.error('Error fetching example:', error);
                }
            });
        }
    }

    validateArticulationForm() {
        const pathwayType = document.getElementById('pathway-type').value;
        const equationShadow = document.getElementById('equation-shadow').value.trim();

        // Minimum length (matches backend requirement of 50 chars)
        const MIN_LENGTH = 50;
        const MAX_LENGTH = 500;

        // Validation rules
        let isValid = true;
        let errorMessage = '';

        if (!pathwayType) {
            isValid = false;
            errorMessage = 'Please select a pathway type';
        } else if (!equationShadow) {
            isValid = false;
            errorMessage = 'Please explain how you would solve this problem (minimum 50 characters)';
        } else if (equationShadow.length < MIN_LENGTH) {
            isValid = false;
            errorMessage = `Too short! Please add more details (need ${MIN_LENGTH - equationShadow.length} more characters)`;
        } else if (equationShadow.length > MAX_LENGTH) {
            isValid = false;
            errorMessage = `Too long! Please be more concise (remove ${equationShadow.length - MAX_LENGTH} characters)`;
        } else if (equationShadow.split(' ').length < 3) {
            isValid = false;
            errorMessage = 'Must contain at least 3 words';
        }

        // Update character count and error message
        document.getElementById('char-count').textContent = `${equationShadow.length}/${MAX_LENGTH}`;
        document.getElementById('char-count').className = equationShadow.length < MIN_LENGTH ? 'text-red' : 'text-green';

        if (errorMessage) {
            const errorEl = document.getElementById('articulation-error');
            if (errorEl) {
                errorEl.textContent = errorMessage;
                errorEl.classList.remove('hidden');
            }
        } else {
            const errorEl = document.getElementById('articulation-error');
            if (errorEl) {
                errorEl.classList.add('hidden');
            }
        }

        document.getElementById('confirm-articulation').disabled = !isValid;
    }

    async startWarmup() {
        try {
            this.radarSection.classList.remove('hidden');
            this.sessionSection.classList.add('hidden');

            // Get today's questions
            const data = await api.getPathwayRadarQuestions();
            this.renderRadarQuestions(data.questions);

            // Start timer (5 minutes)
            this.startRadarTimer(300);

        } catch (error) {
            console.error('Failed to start warmup:', error);
            alert('Failed to start warmup. Please try again.');
        }
    }

    renderRadarQuestions(questions) {
        // P2 Fix #10: Randomize question order
        const shuffledQuestions = [...questions].sort(() => Math.random() - 0.5);

        const questionsContainer = document.getElementById('radar-questions');

        questionsContainer.innerHTML = shuffledQuestions.map((question, index) => {
            return `
                <div class="radar-question" data-question-id="${question.id}">
                    <h4>Question ${index + 1}</h4>
                    <p>${question.questionText}</p>
                    <div class="radar-options">
                        ${question.pathways.map(pathway => `
                            <button class="radar-option" data-pathway="${pathway}">
                                ${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                            </button>
                        `).join('')}
                    </div>
                    <input type="range" class="confidence-slider" min="0" max="100" value="50"
                           data-question-id="${question.id}" style="width: 100%; margin-top: 0.5rem;">
                    <div style="text-align: right; font-size: 0.875rem; color: var(--text-light);">
                        Confidence: <span class="confidence-value">50</span>%
                    </div>
                </div>
            `;
        }).join('');

        // Add event listeners for options
        questionsContainer.querySelectorAll('.radar-option').forEach(option => {
            option.addEventListener('click', () => {
                const questionEl = option.closest('.radar-question');
                questionEl.querySelectorAll('.radar-option').forEach(o => o.classList.remove('selected'));
                option.classList.add('selected');
                questionEl.dataset.selectedPathway = option.dataset.pathway;
            });
        });

        // Add event listeners for confidence sliders
        questionsContainer.querySelectorAll('.confidence-slider').forEach(slider => {
            slider.addEventListener('input', () => {
                const valueDisplay = slider.nextElementSibling.querySelector('.confidence-value');
                valueDisplay.textContent = slider.value;
            });
        });

        // Show submit button
        document.getElementById('submit-radar').classList.remove('hidden');
        document.getElementById('submit-radar').onclick = () => this.submitRadarAnswers(shuffledQuestions);
    }

    startRadarTimer(seconds) {
        let remaining = seconds;
        const timerEl = document.getElementById('radar-timer');

        const updateTimer = () => {
            const minutes = Math.floor(remaining / 60);
            const secs = remaining % 60;
            timerEl.textContent = `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

            // Update progress bar
            const progress = ((seconds - remaining) / seconds) * 100;
            document.getElementById('radar-progress-fill').style.width = `${progress}%`;

            if (remaining > 0) {
                remaining--;
                setTimeout(updateTimer, 1000);
            } else {
                alert('Time is up! Submitting your answers...');
                document.getElementById('submit-radar').click();
            }
        };

        updateTimer();
    }

    async submitRadarAnswers(questions) {
        try {
            const answers = [];

            questions.forEach(question => {
                const questionEl = document.querySelector(`[data-question-id="${question.id}"]`);
                const selectedPathway = questionEl.dataset.selectedPathway;
                const confidence = parseInt(questionEl.querySelector('.confidence-slider').value) / 100;

                if (selectedPathway) {
                    answers.push({
                        questionId: question.id,
                        identifiedPathway: selectedPathway,
                        confidence: confidence
                    });
                }
            });

            const today = new Date().toISOString().split('T')[0];
            const result = await api.submitPathwayRadar({
                date: today,
                answers: answers
            });

            // Show feedback
            this.showRadarFeedback(result);

        } catch (error) {
            console.error('Failed to submit radar answers:', error);
            
            // P0 Fix #3: Handle cooldown error
            if (error.response?.status === 429 && error.response?.data?.detail) {
                const detail = error.response.data.detail;
                if (detail.error === 'cooldown_active') {
                    this.showRadarCooldown(detail);
                    return;
                }
            }
            
            alert('Failed to submit answers. Please try again.');
        }
    }

    showRadarFeedback(result) {
        const feedbackSection = document.getElementById('radar-feedback');
        feedbackSection.classList.remove('hidden');
        
        // P0 Fix #3: Check for gaming detection warnings with consequences
        let gamingWarning = '';
        let scoreInfo = '';
        
        if (result.gamingDetection && result.gamingDetection.gamingDetected) {
            gamingWarning = `
                <div class="gaming-warning" style="background: #fff3cd; border: 2px solid #ffc107; padding: 1.5rem; margin-bottom: 1.5rem; border-radius: 8px;">
                    <h4 style="margin: 0 0 0.5rem 0; color: #0d9488;">
                        <i class="fas fa-heart"></i> We Noticed You're Answering Very Quickly
                    </h4>
                    <p style="margin: 0 0 0.5rem 0;">${result.gamingDetection.recommendation}</p>
                    ${result.gamingDetection.warnings && result.gamingDetection.warnings.length > 0 ? `
                        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                            ${result.gamingDetection.warnings.map(w => `<li>${w}</li>`).join('')}
                        </ul>
                    ` : ''}
                    <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #4caf50;">
                        <strong style="color: #0d9488;">Let's Take a Short Break:</strong>
                        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                            <li>Your current score: <strong>${result.score.currentScore}</strong> points</li>
                            <li><strong>5-minute break</strong> - Pathway radar will be available at ${new Date(result.gamingDetection.cooldownUntil).toLocaleTimeString()}</li>
                        </ul>
                        <p style="margin-top: 0.5rem; font-style: italic; color: #666;">
                            Taking time to think carefully helps you learn better! 🌟
                        </p>
                    </div>
                </div>
            `;
        }
        
        // P0 Fix #3: Show score breakdown with deduction
        scoreInfo = `
            <div style="background: var(--light-color); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Raw Score (${(result.score.accuracy * 100).toFixed(0)}%):</span>
                    <strong>${result.score.rawScore}</strong>
                </div>
                ${result.score.scoreDeduction > 0 ? `
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; color: var(--warning-color);">
                        <span>Speed adjustment:</span>
                        <strong>-${result.score.scoreDeduction}</strong>
                    </div>
                ` : ''}
                <div style="display: flex; justify-content: space-between; padding-top: 0.5rem; border-top: 2px solid var(--border-color);">
                    <span style="font-weight: bold;">Final Score:</span>
                    <strong style="font-size: 1.5rem; color: ${result.score.scoreDeduction > 0 ? 'var(--warning-color)' : 'var(--success-color)'};">${result.score.finalScore}</strong>
                </div>
            </div>
        `;
        
        feedbackSection.innerHTML = `
            <h3><i class="fas fa-chart-bar"></i> Results</h3>
            ${gamingWarning}
            ${scoreInfo}
            
            <div style="margin-bottom: 1rem;">
                <h4><i class="fas fa-check-circle" style="color: var(--success-color);"></i> Strong Pathways</h4>
                ${result.feedback.strongPathways.length > 0 ? 
                    result.feedback.strongPathways.map(p => 
                        `<span class="radar-option" style="background: var(--success-color); color: white; border-color: var(--success-color);">${p}</span>`
                    ).join(' ') : 
                    '<span style="color: var(--text-light);">None yet. Keep practicing!</span>'
                }
            </div>
            
            <div>
                <h4><i class="fas fa-exclamation-triangle" style="color: var(--danger-color);"></i> Weak Pathways</h4>
                ${result.feedback.weakPathways.length > 0 ? 
                    result.feedback.weakPathways.map(p => 
                        `<span class="radar-option" style="background: var(--danger-color); color: white; border-color: var(--danger-color);">${p}</span>`
                    ).join(' ') : 
                    '<span style="color: var(--text-light);">None. Great job!</span>'
                }
            </div>
            
            <button onclick="document.getElementById('pathway-radar-section').classList.add('hidden')" 
                    class="btn btn-primary" style="margin-top: 1.5rem;">
                <i class="fas fa-arrow-right"></i> Start Practice Session
            </button>
        `;
    }
    
    // P0 Fix #3: Show cooldown error with timer
    showRadarCooldown(cooldownInfo) {
        const feedbackSection = document.getElementById('radar-feedback');
        feedbackSection.classList.remove('hidden');
        
        const remainingSeconds = cooldownInfo.cooldownRemaining;
        const cooldownUntil = new Date(cooldownInfo.cooldownUntil);
        
        feedbackSection.innerHTML = `
            <div class="gaming-warning" style="background: #fff3cd; border: 2px solid #ffc107; padding: 2rem; border-radius: 8px; text-align: center;">
                <i class="fas fa-heart" style="font-size: 3rem; color: #0d9488; margin-bottom: 1rem;"></i>
                <h3 style="margin: 0 0 1rem 0; color: #0d9488;">Taking a Break</h3>
                <p style="margin: 0 0 1.5rem 0; font-size: 1.1rem;">${cooldownInfo.message}</p>
                
                <div style="background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <div style="font-size: 2.5rem; font-weight: bold; color: var(--warning-color);" id="cooldown-timer">
                        ${Math.floor(remainingSeconds / 60)}:${String(remainingSeconds % 60).padStart(2, '0')}
                    </div>
                    <div style="color: var(--text-light); margin-top: 0.5rem;">Time Remaining</div>
                </div>
                
                <p style="margin: 0; color: var(--text-light);">
                    <small>Cooldown ends at ${cooldownUntil.toLocaleTimeString()}</small>
                </p>
            </div>
        `;
        
        // Start countdown timer
        this.startCooldownTimer(remainingSeconds);
    }
    
    // P0 Fix #3: Countdown timer for cooldown
    startCooldownTimer(remainingSeconds) {
        const timerEl = document.getElementById('cooldown-timer');
        let seconds = remainingSeconds;
        
        const updateTimer = () => {
            if (seconds <= 0) {
                timerEl.textContent = '0:00';
                timerEl.style.color = 'var(--success-color)';
                
                // Show cooldown ended message
                const feedbackSection = document.getElementById('radar-feedback');
                feedbackSection.innerHTML = `
                    <div class="gaming-warning" style="background: #ecfdf5; border: 2px solid var(--success-color); padding: 2rem; border-radius: 8px; text-align: center;">
                        <i class="fas fa-check-circle" style="font-size: 3rem; color: var(--success-color); margin-bottom: 1rem;"></i>
                        <h3 style="margin: 0 0 1rem 0; color: var(--success-color);">Cooldown Ended</h3>
                        <p style="margin: 0;">You can now submit pathway radar answers again.</p>
                        <button onclick="document.getElementById('radar-feedback').classList.add('hidden')" 
                                class="btn btn-success" style="margin-top: 1.5rem;">
                            <i class="fas fa-redo"></i> Try Again
                        </button>
                    </div>
                `;
                return;
            }
            
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            timerEl.textContent = `${mins}:${String(secs).padStart(2, '0')}`;
            
            // Change color when low on time
            if (seconds < 60) {
                timerEl.style.color = 'var(--danger-color)';
            } else if (seconds < 180) {
                timerEl.style.color = 'var(--warning-color)';
            }
            
            seconds--;
            setTimeout(updateTimer, 1000);
        };
        
        updateTimer();
    }

    async startSession() {
        // P1 Fix #15: Show loading state
        this.showLoading('Starting practice session...');

        try {
            // Create a new practice session (Week 2, before-after-change pathway)
            const sessionData = await api.createPracticeSession({
                week: 2,
                pathway: 'before-after-change',
                sessionType: 'intervention'
            });

            this.currentSession = sessionData;
            this.totalProblems = sessionData.problems.length;
            this.sessionSection.classList.remove('hidden');

            // Update session info
            document.getElementById('session-pathway').textContent =
                `Pathway: ${sessionData.pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}`;

            // Load first problem
            await this.loadProblem();

            // P1 Fix #6: Start practice timer (30 minutes)
            this.startPracticeTimer(30);

            // P2 Fix #5: Start auto-save interval (every 30 seconds)
            this.autoSaveInterval = setInterval(() => {
                this.saveFormData();
            }, 30000);

            // P2 Fix #2: Add tooltips to technical terms
            this.addTooltips();

            // P1 Fix #13: Save state
            this.saveState();

            // Hide loading state
            this.hideLoading();

        } catch (error) {
            // Hide loading state
            this.hideLoading();

            // P1 Fix #11: Show helpful error message
            const errorMessage = error.response?.data?.detail || error.message || 'Failed to start practice session. Please try again.';
            this.showError('Session Start Failed', errorMessage);

            console.error('Failed to start session:', error);
        }
    }

    async loadProblem() {
        try {
            // Get current problem from session
            const sessionData = await api.getPracticeSession(this.currentSession.id);

            if (!sessionData.currentProblem) {
                // Session complete
                this.showSessionComplete();
                return;
            }

            this.currentProblem = sessionData.currentProblem;
            this.currentProblemId = sessionData.currentProblem.id;
            this.currentPathwayType = sessionData.currentProblem.pathway;

            // Update progress
            const completed = sessionData.currentProblemIndex;
            const total = this.currentSession.problems.length;
            document.getElementById('session-progress').textContent =
                `Progress: ${completed}/${total} problems`;
            this.updateProblemCountDisplay(completed, total);

            // Render problem
            this.renderProblem(this.currentProblem);

            // Reset UI
            this.resetProblemUI();

        } catch (error) {
            console.error('Failed to load problem:', error);
            alert('Failed to load problem. Please try again.');
        }
    }

    renderProblem(problem) {
        document.getElementById('problem-title').textContent = problem.title;

        const difficultyEl = document.getElementById('problem-difficulty');
        difficultyEl.textContent = problem.difficulty.toUpperCase();
        difficultyEl.className = `problem-difficulty ${problem.difficulty}`;

        document.getElementById('problem-text').textContent = problem.questionText;

        // Render diagrams
        const diagramsContainer = document.getElementById('problem-diagrams');
        if (problem.diagrams && problem.diagrams.length > 0) {
            diagramsContainer.innerHTML = problem.diagrams.map(diagram => `
                <div style="text-align: center; margin: 1rem 0;" class="diagram-container">
                    <img src="${diagram.renderUrl}" alt="${diagram.type} diagram" style="max-width: 100%; height: auto;">
                    ${diagram.type.includes('bar') ? `<div class="diagram-note">💡 Colors represent different parts of the problem. Match colors to fractions in the question.</div>` : ''}
                    <button class="diagram-help-btn" data-diagram-type="${diagram.type}">
                        <i class="fas fa-question-circle"></i> Confused about diagram?
                    </button>
                </div>
            `).join('');
            // Add event listeners for diagram help buttons
            document.querySelectorAll('.diagram-help-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const type = btn.getAttribute('data-diagram-type');
                    alert(`You can ask questions about the ${type} diagram. Use the 'Need Help?' button for hints or examples.`);
                });
            });
        } else {
            diagramsContainer.innerHTML = '';
        }
    }

    resetProblemUI() {
        // Reset form fields
        document.getElementById('pathway-type').value = '';
        document.getElementById('equation-shadow').value = '';
        document.getElementById('student-answer').value = '';
        document.getElementById('char-count').textContent = '0';

        // Reset UI states
        document.getElementById('solution-section').classList.add('hidden');
        document.getElementById('triad-feedback').classList.add('hidden');
        document.getElementById('confirm-articulation').disabled = true;

        // Hide articulation level info
        const articulationInfo = document.getElementById('articulation-level-info');
        if (articulationInfo) {
            articulationInfo.classList.add('hidden');
        }

        // Reset hint/example content and buttons
        const hintContent = document.getElementById('hint-content');
        const exampleContent = document.getElementById('example-content');
        const hintBtn = document.getElementById('hint-btn');
        const exampleBtn = document.getElementById('example-btn');
        
        // P0-7: Reset step-by-step section
        const stepByStepSection = document.querySelector('.step-by-step-section');
        if (stepByStepSection) {
            stepByStepSection.remove();
        }

        if (hintContent) {
            hintContent.classList.add('hidden');
            hintContent.innerHTML = '';
        }
        if (exampleContent) {
            exampleContent.classList.add('hidden');
            exampleContent.innerHTML = '';
        }
        if (hintBtn) {
            hintBtn.disabled = false;
            hintBtn.textContent = 'Show Hint';
        }
        if (exampleBtn) {
            exampleBtn.disabled = false;
            exampleBtn.textContent = 'Show Example';
        }

        // Reset hint counters
        this.hintCount = 0;
        this.lastHintTime = null;

        // Clear canvas
        if (window.canvasAnnotation) {
            window.canvasAnnotation.clearCanvas();
        }
    }

    confirmArticulation() {
        // Show solution section
        document.getElementById('solution-section').classList.remove('hidden');

        // Scroll to solution section
        document.getElementById('solution-section').scrollIntoView({ behavior: 'smooth' });
    }

    async submitAnswer() {
        // P1 Fix #3: Disable submit button while processing
        const submitBtn = document.getElementById('submit-answer');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';

        // P1 Fix #15: Show loading state
        this.showLoading('Submitting your answer...');

        // P1 Fix #1: Pause timer
        this.pauseTimer();

        try {
            const submission = {
                problemId: this.currentProblem.id,
                pathwayType: document.getElementById('pathway-type').value,
                equationShadow: document.getElementById('equation-shadow').value,
                studentAnswer: {
                    type: 'numeric',
                    value: parseFloat(document.getElementById('student-answer').value)
                }
            };

            // Submit answer
            const result = await api.submitPracticeSession(this.currentSession.id, submission);

            // Hide loading state
            this.hideLoading();

            // P1-1: Emit practiceSubmitted event for gamification
            window.dispatchEvent(new CustomEvent('practiceSubmitted', { detail: result }));

            // P1 Fix #11: Check for validation errors
            if (result.error) {
                this.showError('Validation failed', result.message);
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Answer';
                this.resumeTimer();
                return;
            }

            // Show feedback with P0 fixes (collision hints, range validation)
            this.showTriadFeedback(result.feedback);

            // Update confidence history (P1 Fix #7)
            this.updateConfidenceHistory(result.feedback.pathwayIdentification.confidence);
            this.showConfidenceTrend();

            // Update milestone (optional)
            this.updateMilestone(result.feedback);

            // P1 Fix #13: Save state
            this.saveState();

        } catch (error) {
            // Hide loading state
            this.hideLoading();

            // P1 Fix #11: Show helpful error message
            const errorMessage = error.response?.data?.detail?.message || error.message || 'Failed to submit answer. Please try again.';
            this.showError('Submission Failed', errorMessage);

            console.error('Failed to submit answer:', error);
        } finally {
            // P1 Fix #3: Re-enable submit button
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Answer';
        }
    }

    showTriadFeedback(feedback) {
        const feedbackSection = document.getElementById('triad-feedback');
        feedbackSection.classList.remove('hidden');
        feedbackSection.scrollIntoView({ behavior: 'smooth' });

        // Show articulation level info
        const articulationInfo = document.getElementById('articulation-level-info');
        if (articulationInfo) {
            articulationInfo.classList.remove('hidden');
        }

        // Pathway Identification with P0 Fix #7 (collision detection)
        const pathwayCard = document.getElementById('pathway-feedback');
        pathwayCard.className = `feedback-card ${feedback.pathwayIdentification.correct ? 'green' : 'red'}`;
        document.getElementById('pathway-icon').innerHTML =
            feedback.pathwayIdentification.correct ? '<i class="fas fa-check-circle"></i>' : '<i class="fas fa-times-circle"></i>';

        // P0 Fix #7: Show collision hint if detected
        let pathwayFeedbackText = feedback.pathwayIdentification.correct ?
            'Correctly identified the pathway!' :
            'Incorrect pathway. Review the problem again.';

        if (feedback.pathwayIdentification.collisionDetected && feedback.pathwayIdentification.hint) {
            pathwayFeedbackText += ` <br><br><strong>💡 Hint:</strong> ${feedback.pathwayIdentification.hint}`;
            pathwayCard.classList.add('collision-warning');
        }

        document.getElementById('pathway-feedback-text').innerHTML = pathwayFeedbackText;
        document.getElementById('pathway-confidence').style.width =
            `${feedback.pathwayIdentification.confidence * 100}%`;

        // P1 Fix #2: Truncate long feedback if needed (add expand/collapse)
        this.setupFeedbackTruncation('pathway-feedback-text');

        // P0 Fix #7: Side-by-side model comparison
        const articulationCard = document.getElementById('articulation-feedback');
        const articulationLevel = feedback.articulation.level;
        articulationCard.className = `feedback-card ${articulationLevel >= 2 ? 'green' : 'yellow'}`;
        document.getElementById('articulation-icon').innerHTML =
            `<i class="fas fa-star" style="color: ${articulationLevel === 3 ? 'gold' : 'silver'};"></i>`;
        document.getElementById('articulation-level-val').textContent = articulationLevel;
        
        // P0 Fix #7: Show student articulation
        const studentArticulation = document.getElementById('equation-shadow').value;
        
        // P0 Fix #7: Create comparison section
        const modelArticulation = feedback.articulation.modelArticulation || 'No model articulation available.';
        const differences = feedback.articulation.feedback || 'Focus on explaining your thinking more clearly.';
        
        const comparisonHTML = `
            <div class="comparison-section">
                <h4>Your Explanation:</h4>
                <p class="student-articulation">${studentArticulation || 'No explanation provided.'}</p>
                
                <h4>Model Explanation:</h4>
                <p class="model-articulation">${modelArticulation}</p>
                
                <h4>What You Can Improve:</h4>
                <p class="missed-points">${differences}</p>
            </div>
        `;
        
        // Insert comparison section before the articulation text
        const articulationText = document.getElementById('articulation-feedback-text');
        articulationText.innerHTML = comparisonHTML;
        
        // Hide the old model articulation section since we now have comparison
        const modelArticulationSection = document.querySelector('.model-articulation');
        if (modelArticulationSection && modelArticulationSection.parentElement) {
            modelArticulationSection.parentElement.style.display = 'none';
        }

        // Solution with P0 Fix #8 (range validation)
        const solutionCard = document.getElementById('solution-feedback');
        solutionCard.className = `feedback-card ${feedback.solution.correct ? 'green' : 'red'}`;
        document.getElementById('solution-icon').innerHTML =
            feedback.solution.correct ? '<i class="fas fa-check-circle"></i>' : '<i class="fas fa-times-circle"></i>';
        document.getElementById('solution-feedback-text').textContent = feedback.solution.feedback || '';
        document.getElementById('student-answer-val').textContent =
            feedback.solution.studentAnswer?.toFixed(2) || 'N/A';
        document.getElementById('expected-answer-val').textContent =
            feedback.solution.expectedAnswer?.toFixed(2) || 'N/A';

        // P0 Fix #8: Show range validation warnings
        if (feedback.solution.rangeValidation && feedback.solution.rangeValidation.suspicious) {
            const rangeWarnings = document.getElementById('range-validation-warnings');
            if (rangeWarnings) {
                rangeWarnings.innerHTML = feedback.solution.rangeValidation.warnings.map(w =>
                    `<li class="warning-item">⚠️ ${w}</li>`
                ).join('');
                rangeWarnings.classList.remove('hidden');
            }
        }
        
        // P0-7: Show step-by-step scaffolding for wrong answers
        if (!feedback.solution.correct && feedback.solution.stepByStep) {
            const solutionFeedbackText = document.getElementById('solution-feedback-text');
            const stepByStepData = feedback.solution.stepByStep;
            
            const stepByStepHTML = `
                <div class="step-by-step-section">
                    <h4>🔦 Let's Work Through This Step-by-Step</h4>
                    <p class="hint-text"><strong>Mistake Pattern:</strong> ${stepByStepData.pattern}</p>
                    <p class="hint-text"><strong>💡 Hint:</strong> ${stepByStepData.hint}</p>
                    <button id="show-steps-btn" class="btn btn-secondary">Show Me Steps</button>
                    <div id="detailed-steps" class="detailed-steps hidden">
                        <ol>
                            ${stepByStepData.steps.map(step => `<li>${step}</li>`).join('')}
                        </ol>
                    </div>
                </div>
            `;
            
            solutionFeedbackText.innerHTML += stepByStepHTML;
            
            // Add toggle functionality
            setTimeout(() => {
                const showStepsBtn = document.getElementById('show-steps-btn');
                const detailedSteps = document.getElementById('detailed-steps');
                
                if (showStepsBtn && detailedSteps) {
                    showStepsBtn.addEventListener('click', () => {
                        if (detailedSteps.classList.contains('hidden')) {
                            detailedSteps.classList.remove('hidden');
                            showStepsBtn.textContent = 'Hide Steps';
                        } else {
                            detailedSteps.classList.add('hidden');
                            showStepsBtn.textContent = 'Show Me Steps';
                        }
                    });
                }
            }, 100);
        }

        // P1 Fix #2: Truncate long feedback if needed
        this.setupFeedbackTruncation('solution-feedback-text');

        // P0 Fix #12: Simplified triad feedback with key message first
        const overallStatus = document.getElementById('overall-status');
        overallStatus.className = `overall-status ${feedback.overall}`;
        
        // P0 Fix #12: Create key feedback message
        let keyMessage = '';
        let feedbackClass = feedback.overall;
        let detailedFeedback = '';
        
        if (feedback.overall === 'green') {
            keyMessage = '🎉 Excellent work! You nailed it!';
            detailedFeedback = `Pathway: ${feedback.pathwayIdentification.correct ? '✓ Correct' : '✗ Incorrect'}\nArticulation Level: ${feedback.articulation.level}/3\nSolution: ${feedback.solution.correct ? '✓ Correct' : '✗ Incorrect'}`;
        } else if (feedback.overall === 'yellow') {
            keyMessage = '👍 Good effort! Room for improvement.';
            detailedFeedback = `Pathway: ${feedback.pathwayIdentification.correct ? '✓ Correct' : '✗ Incorrect'}\nArticulation Level: ${feedback.articulation.level}/3\nSolution: ${feedback.solution.correct ? '✓ Correct' : '✗ Incorrect'}`;
        } else {
            keyMessage = '💪 Keep trying! You can do this!';
            detailedFeedback = `Pathway: ${feedback.pathwayIdentification.correct ? '✓ Correct' : '✗ Incorrect'}\nArticulation Level: ${feedback.articulation.level}/3\nSolution: ${feedback.solution.correct ? '✓ Correct' : '✗ Incorrect'}`;
        }
        
        // P0 Fix #12: Insert key feedback at the top of feedback section
        feedbackSection = document.getElementById('triad-feedback');
        
        // Check if key feedback already exists, if not add it
        if (!document.querySelector('.key-feedback')) {
            const keyFeedbackDiv = document.createElement('div');
            keyFeedbackDiv.className = `key-feedback ${feedbackClass}`;
            keyFeedbackDiv.innerHTML = keyMessage;
            
            // Insert at the beginning of feedback section
            const h2 = feedbackSection.querySelector('h2');
            h2.insertAdjacentElement('afterend', keyFeedbackDiv);
            
            // Add toggle button
            const toggleBtn = document.createElement('button');
            toggleBtn.className = 'toggle-details-btn';
            toggleBtn.textContent = 'Click for detailed feedback ▼';
            toggleBtn.onclick = () => this.toggleFeedbackDetails();
            keyFeedbackDiv.insertAdjacentElement('afterend', toggleBtn);
            
            // Create wrapper for detailed feedback
            const detailsDiv = document.createElement('div');
            detailsDiv.id = 'feedback-details';
            detailsDiv.style.display = 'none';
            
            // Move all feedback cards into details wrapper
            const feedbackCards = feedbackSection.querySelectorAll('.feedback-card');
            feedbackCards.forEach(card => detailsDiv.appendChild(card));
            
            // Move overall section and next button into details wrapper
            const overallSection = feedbackSection.querySelector('.overall-feedback');
            const nextBtn = feedbackSection.querySelector('#next-problem');
            if (overallSection) detailsDiv.appendChild(overallSection);
            if (nextBtn) {
                detailsDiv.appendChild(nextBtn);
                nextBtn.style.marginTop = '1rem';
            }
            
            toggleBtn.insertAdjacentElement('afterend', detailsDiv);
        }
        
        // Update the overall title inside the details
        const overallTitle = document.getElementById('overall-title');
        if (overallTitle) {
            overallTitle.textContent =
                feedback.overall === 'green' ? 'Great Job!' :
                feedback.overall === 'yellow' ? 'Good Effort!' : 'Keep Trying!';
        }
    }

    // P0 Fix #12: Toggle feedback details visibility
    toggleFeedbackDetails() {
        const detailsDiv = document.getElementById('feedback-details');
        const toggleBtn = document.querySelector('.toggle-details-btn');
        
        if (detailsDiv.style.display === 'none') {
            detailsDiv.style.display = 'block';
            toggleBtn.textContent = 'Hide detailed feedback ▲';
        } else {
            detailsDiv.style.display = 'none';
            toggleBtn.textContent = 'Click for detailed feedback ▼';
        }
    }

    // P1 Fix #2: Setup feedback truncation with expand/collapse
    setupFeedbackTruncation(elementId) {
        const element = document.getElementById(elementId);
        if (!element) return;

        const MAX_LENGTH = 300;
        const text = element.textContent || element.innerHTML;

        if (text.length > MAX_LENGTH) {
            const truncated = text.substring(0, MAX_LENGTH) + '...';
            const full = text;

            element.innerHTML = `
                <span class="feedback-short">${truncated}</span>
                <span class="feedback-full" style="display: none;">${full}</span>
                <button class="feedback-expand-btn">Show More</button>
            `;

            const expandBtn = element.querySelector('.feedback-expand-btn');
            const shortEl = element.querySelector('.feedback-short');
            const fullEl = element.querySelector('.feedback-full');

            expandBtn.addEventListener('click', () => {
                if (fullEl.style.display === 'none') {
                    shortEl.style.display = 'none';
                    fullEl.style.display = 'inline';
                    expandBtn.textContent = 'Show Less';
                } else {
                    shortEl.style.display = 'inline';
                    fullEl.style.display = 'none';
                    expandBtn.textContent = 'Show More';
                }
            });
        }
    }

    async updateMilestone(feedback) {
        try {
            // Find or create milestone for current pathway
            const milestones = await api.getMilestones();
            const milestone = milestones.milestones.find(m =>
                m.pathway === this.currentProblem.pathway
            );

            if (milestone) {
                await api.updateMilestone(milestone.id, {
                    problemsCompleted: milestone.problemsCompleted + 1,
                    lastAttemptScore: feedback.solution.score,
                    pathwayIdentifiedCorrectly: feedback.pathwayIdentification.correct,
                    articulationLevel: feedback.articulation.level
                });
            }
        } catch (error) {
            console.error('Failed to update milestone:', error);
        }
    }

    async loadNextProblem() {
        await this.loadProblem();
    }

    showSessionComplete() {
        this.sessionSection.innerHTML = `
            <div style="text-align: center; padding: 3rem;">
                <h2><i class="fas fa-trophy" style="color: gold; font-size: 3rem;"></i></h2>
                <h2>Session Complete!</h2>
                <p style="font-size: 1.25rem; margin: 1rem 0;">
                    You've completed all problems in this session.
                </p>
                <button onclick="location.reload()" class="btn btn-primary">
                    <i class="fas fa-redo"></i> Start New Session
                </button>
            </div>
        `;
    }

    resetPracticeUI() {
        this.radarSection.classList.add('hidden');
        this.sessionSection.classList.add('hidden');

        // P1 Fix #1: Pause timer when navigating away
        if (this.practiceTimerInterval) {
            clearInterval(this.practiceTimerInterval);
        }

        // P2 Fix #5: Clear auto-save
        if (this.autoSaveInterval) {
            clearInterval(this.autoSaveInterval);
        }
    }

    // P2 Fix #1: Load glossary data
    async loadGlossary() {
        try {
            const response = await fetch(`${API_BASE_URL}/glossary`);
            const data = await response.json();
            this.glossaryData = data.terms;
        } catch (error) {
            console.error('Failed to load glossary:', error);
        }
    }

    // P2 Fix #1: Show glossary modal
    showGlossaryModal() {
        const modal = document.createElement('div');
        modal.className = 'modal-overlay';
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h2><i class="fas fa-book"></i> Glossary</h2>
                    <button class="modal-close" onclick="this.closest('.modal-overlay').remove()">&times;</button>
                </div>
                <div class="modal-body">
                    ${Object.entries(this.glossaryData).map(([term, definition]) => `
                        <div class="glossary-term">
                            <h4>${term}</h4>
                            <p>${definition}</p>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    }

    // P2 Fix #2: Add tooltips to technical terms
    addTooltips() {
        const technicalTerms = ['equation shadow', 'pathway type', 'articulation', 'triad feedback', 'forced articulation', 'pathway radar'];

        technicalTerms.forEach(term => {
            const termKey = term.toLowerCase().replace(/ /g, '-');
            const elements = document.querySelectorAll(`[data-term="${termKey}"]`);
            elements.forEach(el => {
                const definition = this.glossaryData[termKey] || this.glossaryData[term] || term;
                el.setAttribute('title', definition);
                el.classList.add('has-tooltip');
            });
        });
    }

    // P1 Fix #12: Save form data to localStorage
    saveFormData() {
        this.formData = {
            pathwayType: document.getElementById('pathway-type').value,
            equationShadow: document.getElementById('equation-shadow').value,
            studentAnswer: document.getElementById('student-answer').value
        };
        localStorage.setItem('practiceFormData', JSON.stringify(this.formData));
    }

    // P1 Fix #12: Restore form data from localStorage
    restoreFormData() {
        const saved = localStorage.getItem('practiceFormData');
        if (saved) {
            try {
                this.formData = JSON.parse(saved);
                if (this.formData.pathwayType) {
                    document.getElementById('pathway-type').value = this.formData.pathwayType;
                }
                if (this.formData.equationShadow) {
                    document.getElementById('equation-shadow').value = this.formData.equationShadow;
                    document.getElementById('char-count').textContent = this.formData.equationShadow.length;
                }
                if (this.formData.studentAnswer) {
                    document.getElementById('student-answer').value = this.formData.studentAnswer;
                }
                this.validateArticulationForm();
            } catch (error) {
                console.error('Failed to restore form data:', error);
            }
        }
    }

    // P1 Fix #12: Load saved state
    loadSavedState() {
        const savedState = localStorage.getItem('practiceState');
        if (savedState) {
            try {
                const state = JSON.parse(savedState);
                if (state.page === 'practice' && state.sessionId) {
                    this.currentSession = { id: state.sessionId };
                }
            } catch (error) {
                console.error('Failed to load saved state:', error);
            }
        }
    }

    // P1 Fix #13: Save state for browser back button
    saveState() {
        const state = {
            page: 'practice',
            sessionId: this.currentSession?.id,
            problemId: this.currentProblem?.id,
            formData: this.formData
        };
        history.pushState(state, '', '#practice');
        localStorage.setItem('practiceState', JSON.stringify(state));
    }

    // P1 Fix #13: Restore state from browser back button
    restoreState(state) {
        if (state.sessionId) {
            this.currentSession = { id: state.sessionId };
        }
        if (state.formData) {
            this.formData = state.formData;
        }
        this.loadProblem();
    }

    // P1 Fix #6: Start practice timer
    startPracticeTimer(minutes = 30) {
        this.timeRemaining = minutes * 60; // Convert to seconds
        const timerEl = document.getElementById('practice-timer');
        if (this.totalProblems > 0) {
            this.updateProblemCountDisplay(0, this.totalProblems);
        }

        if (this.practiceTimerInterval) {
            clearInterval(this.practiceTimerInterval);
        }

        this.practiceTimerInterval = setInterval(() => {
            this.timeRemaining--;
            const mins = Math.floor(this.timeRemaining / 60);
            const secs = this.timeRemaining % 60;
            timerEl.textContent = `Time: ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

            // Change color when low on time
            if (this.timeRemaining < 300) { // Less than 5 minutes
                timerEl.classList.add('timer-warning');
            }

            if (this.timeRemaining <= 0) {
                clearInterval(this.practiceTimerInterval);
                alert('Time is up! Your session has ended.');
            }
        }, 1000);
    }

    // Update problem count and progress bar
    updateProblemCountDisplay(completed, total) {
        const problemCountEl = document.getElementById('problem-count');
        if (problemCountEl) {
            const remaining = total - completed;
            const timePerProblem = remaining > 0 ? Math.floor((this.timeRemaining / 60) / remaining) : 0;
            problemCountEl.textContent = completed + '/' + total + ' problems, ~' + timePerProblem + ' min each';
        }
        // Update progress bar
        const progressFill = document.getElementById('session-progress-fill');
        if (progressFill) {
            const progressPercent = (completed / total) * 100;
            progressFill.style.width = progressPercent + '%';
        }
    }

    // P1 Fix #1: Pause timer (e.g., when navigating away)
    pauseTimer() {
        if (this.practiceTimerInterval) {
            clearInterval(this.practiceTimerInterval);
            this.practiceTimerInterval = null;
        }
    }

    // P1 Fix #1: Resume timer
    resumeTimer() {
        if (this.timeRemaining > 0) {
            this.startPracticeTimer(Math.ceil(this.timeRemaining / 60));
        }
    }

    // P1 Fix #7: Update confidence history for trend visualization
    updateConfidenceHistory(confidence) {
        this.confidenceHistory.push({
            timestamp: new Date().toISOString(),
            confidence: confidence
        });

        // Keep only last 30 entries
        if (this.confidenceHistory.length > 30) {
            this.confidenceHistory.shift();
        }

        localStorage.setItem('confidenceHistory', JSON.stringify(this.confidenceHistory));
    }

    // P1 Fix #7: Show confidence trend visualization
    showConfidenceTrend() {
        const history = JSON.parse(localStorage.getItem('confidenceHistory') || '[]');
        if (history.length < 2) return;

        // Simple visualization
        const container = document.getElementById('confidence-trend');
        if (container) {
            const avgConfidence = history.reduce((sum, h) => sum + h.confidence, 0) / history.length;
            const trend = history[history.length - 1].confidence - history[0].confidence;

            container.innerHTML = `
                <div class="confidence-trend">
                    <h4><i class="fas fa-chart-line"></i> Confidence Trend</h4>
                    <div class="trend-metrics">
                        <div class="trend-metric">
                            <span class="metric-value">${(avgConfidence * 100).toFixed(0)}%</span>
                            <span class="metric-label">Average</span>
                        </div>
                        <div class="trend-metric">
                            <span class="metric-value ${trend >= 0 ? 'positive' : 'negative'}">
                                ${trend >= 0 ? '+' : ''}${(trend * 100).toFixed(0)}%
                            </span>
                            <span class="metric-label">Trend</span>
                        </div>
                        <div class="trend-metric">
                            <span class="metric-value">${history.length}</span>
                            <span class="metric-label">Attempts</span>
                        </div>
                    </div>
                    <div class="trend-chart">
                        ${history.map((h, i) => {
                            const height = h.confidence * 100;
                            return `<div class="trend-bar" style="height: ${height}%" title="${new Date(h.timestamp).toLocaleString()}"></div>`;
                        }).join('')}
                    </div>
                </div>
            `;
        }
    }

    // P1 Fix #15: Show loading states
    showLoading(message = 'Processing...') {
        const loading = document.createElement('div');
        loading.className = 'loading-overlay';
        loading.id = 'loading-overlay';
        loading.innerHTML = `
            <div class="loading-spinner">
                <div class="spinner"></div>
                <p>${message}</p>
            </div>
        `;
        document.body.appendChild(loading);
    }

    // P1 Fix #15: Hide loading states
    hideLoading() {
        const loading = document.getElementById('loading-overlay');
        if (loading) {
            loading.remove();
        }
    }

    // P1 Fix #11: Show error with helpful message
    showError(message, details = null) {
        const errorEl = document.createElement('div');
        errorEl.className = 'error-banner';
        errorEl.innerHTML = `
            <div class="error-icon"><i class="fas fa-exclamation-circle"></i></div>
            <div class="error-message">
                <strong>Error</strong>
                <p>${message}</p>
                ${details ? `<p class="error-details">${details}</p>` : ''}
            </div>
            <button class="error-close" onclick="this.closest('.error-banner').remove()">&times;</button>
        `;
        document.body.appendChild(errorEl);

        // Auto-remove after 10 seconds
        setTimeout(() => {
            if (errorEl.parentNode) {
                errorEl.remove();
            }
        }, 10000);
    }

    // P2 Fix #3: Show help modal
    showHelpModal() {
        const modal = document.createElement('div');
        modal.className = 'modal-overlay';
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h2><i class="fas fa-question-circle"></i> Help</h2>
                    <button class="modal-close" onclick="this.closest('.modal-overlay').remove()">&times;</button>
                </div>
                <div class="modal-body">
                    <h3>How to Use Practice Mode</h3>
                    <ol>
                        <li><strong>Warm-up:</strong> Start with pathway radar to warm up your pathway identification skills.</li>
                        <li><strong>Read the problem:</strong> Carefully read the question and examine the diagrams.</li>
                        <li><strong>Identify the pathway:</strong> Choose the correct pathway type from the dropdown.</li>
                        <li><strong>Articulate your thinking:</strong> Write at least 10 characters describing how you would solve this problem.</li>
                        <li><strong>Solve and submit:</strong> Enter your numerical answer and submit for feedback.</li>
                        <li><strong>Review feedback:</strong> Use the triad feedback to improve your understanding.</li>
                    </ol>
                    <h3>Keyboard Shortcuts</h3>
                    <ul>
                        <li><kbd>Ctrl/Cmd + Enter</kbd> - Submit answer</li>
                        <li><kbd>Ctrl/Cmd + B</kbd> - Open glossary</li>
                    </ul>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    }

    // P2 Fix #6: Print optimization
    optimizePrint() {
        window.addEventListener('beforeprint', () => {
            document.body.classList.add('printing');
        });

        window.addEventListener('afterprint', () => {
            document.body.classList.remove('printing');
        });
    }
}

// Initialize practice when DOM is ready
let practice;
document.addEventListener('DOMContentLoaded', () => {
    practice = new Practice();
});
