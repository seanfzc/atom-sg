// PersonaUI.js - Persona-aware UI Modes
// Supports anxiety-reducing, visual learner, focus, and reading support modes

class PersonaUI {
    constructor(options = {}) {
        this.currentMode = 'default';
        this.modes = {
            default: { name: 'Default', icon: '⚙️' },
            anxiety: { name: 'Calm Mode', icon: '🧘' },
            visual: { name: 'Visual Mode', icon: '👁️' },
            focus: { name: 'Focus Mode', icon: '🎯' },
            reading: { name: 'Reading Mode', icon: '📖' }
        };
        
        this.options = {
            storageKey: 'persona-ui-mode',
            autoDetect: options.autoDetect !== false,
            transitionDuration: 300,
            ...options
        };
        
        // Pomodoro state
        this.pomodoro = {
            active: false,
            workTime: 25 * 60, // 25 minutes in seconds
            breakTime: 5 * 60, // 5 minutes in seconds
            timeRemaining: 25 * 60,
            isBreak: false,
            interval: null
        };
        
        // TTS state
        this.tts = {
            enabled: false,
            speaking: false,
            synth: window.speechSynthesis,
            voices: [],
            currentUtterance: null
        };
        
        // Initialize
        this.init();
    }
    
    init() {
        // Load saved mode
        this.loadMode();
        
        // Initialize TTS
        this.initTTS();
        
        // Create UI components
        this.createModeSelector();
        this.createPomodoroWidget();
        this.createTTSControls();
        
        // Apply initial mode
        this.applyMode(this.currentMode);
        
        // Listen for mode change events
        document.addEventListener('personaModeChange', (e) => {
            this.setMode(e.detail.mode);
        });
    }
    
    initTTS() {
        if ('speechSynthesis' in window) {
            // Load voices
            const loadVoices = () => {
                this.tts.voices = this.tts.synth.getVoices();
            };
            
            loadVoices();
            
            if (speechSynthesis.onvoiceschanged !== undefined) {
                speechSynthesis.onvoiceschanged = loadVoices;
            }
        }
    }
    
    createModeSelector() {
        // Check if selector already exists
        if (document.getElementById('persona-mode-selector')) return;
        
        const selector = document.createElement('div');
        selector.id = 'persona-mode-selector';
        selector.className = 'persona-mode-selector';
        selector.innerHTML = `
            <button class="persona-mode-btn persona-mode-toggle" title="Select UI Mode">
                <span class="persona-mode-icon">${this.modes[this.currentMode].icon}</span>
                <span class="persona-mode-name">${this.modes[this.currentMode].name}</span>
            </button>
            <div class="persona-mode-dropdown hidden">
                ${Object.entries(this.modes).map(([key, mode]) => `
                    <button class="persona-mode-option ${key === this.currentMode ? 'active' : ''}" data-mode="${key}">
                        <span class="persona-mode-icon">${mode.icon}</span>
                        <span class="persona-mode-name">${mode.name}</span>
                    </button>
                `).join('')}
            </div>
        `;
        
        document.body.appendChild(selector);
        
        // Event listeners
        const toggle = selector.querySelector('.persona-mode-toggle');
        const dropdown = selector.querySelector('.persona-mode-dropdown');
        
        toggle.addEventListener('click', () => {
            dropdown.classList.toggle('hidden');
        });
        
        selector.querySelectorAll('.persona-mode-option').forEach(btn => {
            btn.addEventListener('click', () => {
                const mode = btn.dataset.mode;
                this.setMode(mode);
                dropdown.classList.add('hidden');
            });
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!selector.contains(e.target)) {
                dropdown.classList.add('hidden');
            }
        });
    }
    
    createPomodoroWidget() {
        if (document.getElementById('pomodoro-widget')) return;
        
        const widget = document.createElement('div');
        widget.id = 'pomodoro-widget';
        widget.className = 'pomodoro-widget hidden';
        widget.innerHTML = `
            <div class="pomodoro-header">
                <span class="pomodoro-icon">🍅</span>
                <span class="pomodoro-title">Focus Timer</span>
                <button class="pomodoro-close">&times;</button>
            </div>
            <div class="pomodoro-display">
                <div class="pomodoro-time">25:00</div>
                <div class="pomodoro-status">Ready to focus</div>
            </div>
            <div class="pomodoro-controls">
                <button class="pomodoro-btn pomodoro-start">Start</button>
                <button class="pomodoro-btn pomodoro-pause hidden">Pause</button>
                <button class="pomodoro-btn pomodoro-reset">Reset</button>
            </div>
            <div class="pomodoro-settings">
                <label>
                    Work: <input type="number" class="pomodoro-work-min" value="25" min="1" max="60"> min
                </label>
                <label>
                    Break: <input type="number" class="pomodoro-break-min" value="5" min="1" max="30"> min
                </label>
            </div>
        `;
        
        document.body.appendChild(widget);
        
        // Event listeners
        const closeBtn = widget.querySelector('.pomodoro-close');
        const startBtn = widget.querySelector('.pomodoro-start');
        const pauseBtn = widget.querySelector('.pomodoro-pause');
        const resetBtn = widget.querySelector('.pomodoro-reset');
        const workInput = widget.querySelector('.pomodoro-work-min');
        const breakInput = widget.querySelector('.pomodoro-break-min');
        
        closeBtn.addEventListener('click', () => {
            widget.classList.add('hidden');
        });
        
        startBtn.addEventListener('click', () => this.startPomodoro());
        pauseBtn.addEventListener('click', () => this.pausePomodoro());
        resetBtn.addEventListener('click', () => this.resetPomodoro());
        
        workInput.addEventListener('change', () => {
            this.pomodoro.workTime = parseInt(workInput.value) * 60;
            if (!this.pomodoro.active) {
                this.pomodoro.timeRemaining = this.pomodoro.workTime;
                this.updatePomodoroDisplay();
            }
        });
        
        breakInput.addEventListener('change', () => {
            this.pomodoro.breakTime = parseInt(breakInput.value) * 60;
        });
    }
    
    createTTSControls() {
        if (document.getElementById('tts-controls')) return;
        
        const controls = document.createElement('div');
        controls.id = 'tts-controls';
        controls.className = 'tts-controls hidden';
        controls.innerHTML = `
            <div class="tts-header">
                <span class="tts-icon">🔊</span>
                <span class="tts-title">Text to Speech</span>
                <button class="tts-close">&times;</button>
            </div>
            <div class="tts-options">
                <label>
                    Speed: <input type="range" class="tts-rate" min="0.5" max="2" step="0.1" value="1">
                    <span class="tts-rate-value">1.0x</span>
                </label>
                <label>
                    Pitch: <input type="range" class="tts-pitch" min="0.5" max="2" step="0.1" value="1">
                    <span class="tts-pitch-value">1.0</span>
                </label>
            </div>
            <div class="tts-actions">
                <button class="tts-btn tts-play">▶️ Play</button>
                <button class="tts-btn tts-pause hidden">⏸️ Pause</button>
                <button class="tts-btn tts-stop">⏹️ Stop</button>
            </div>
            <div class="tts-chunk-info">
                <span class="tts-chunk-current">1</span> / <span class="tts-chunk-total">1</span>
            </div>
        `;
        
        document.body.appendChild(controls);
        
        // Event listeners
        const closeBtn = controls.querySelector('.tts-close');
        const playBtn = controls.querySelector('.tts-play');
        const pauseBtn = controls.querySelector('.tts-pause');
        const stopBtn = controls.querySelector('.tts-stop');
        const rateInput = controls.querySelector('.tts-rate');
        const pitchInput = controls.querySelector('.tts-pitch');
        
        closeBtn.addEventListener('click', () => {
            controls.classList.add('hidden');
        });
        
        playBtn.addEventListener('click', () => this.playTTS());
        pauseBtn.addEventListener('click', () => this.pauseTTS());
        stopBtn.addEventListener('click', () => this.stopTTS());
        
        rateInput.addEventListener('input', () => {
            controls.querySelector('.tts-rate-value').textContent = rateInput.value + 'x';
        });
        
        pitchInput.addEventListener('input', () => {
            controls.querySelector('.tts-pitch-value').textContent = pitchInput.value;
        });
    }
    
    setMode(mode) {
        if (!this.modes[mode]) {
            console.error(`Unknown mode: ${mode}`);
            return;
        }
        
        this.currentMode = mode;
        this.saveMode();
        this.applyMode(mode);
        this.updateModeSelector();
        
        // Dispatch event
        document.dispatchEvent(new CustomEvent('personaModeChanged', { detail: { mode } }));
    }
    
    applyMode(mode) {
        const body = document.body;
        
        // Remove all mode classes
        Object.keys(this.modes).forEach(m => body.classList.remove(`persona-mode-${m}`));
        
        // Add current mode class
        body.classList.add(`persona-mode-${mode}`);
        
        // Apply mode-specific settings
        switch (mode) {
            case 'anxiety':
                this.applyAnxietyMode();
                break;
            case 'visual':
                this.applyVisualMode();
                break;
            case 'focus':
                this.applyFocusMode();
                break;
            case 'reading':
                this.applyReadingMode();
                break;
            default:
                this.applyDefaultMode();
        }
    }
    
    applyAnxietyMode() {
        // Hide timers
        this.hideTimers();
        
        // Show calming elements
        this.showCalmingElements();
        
        // Hide Pomodoro (can cause anxiety)
        const pomodoro = document.getElementById('pomodoro-widget');
        if (pomodoro) pomodoro.classList.add('hidden');
        
        // Hide TTS controls
        const tts = document.getElementById('tts-controls');
        if (tts) tts.classList.add('hidden');
        
        // Apply calming CSS
        document.documentElement.style.setProperty('--primary-color', '#0d9488');
        document.documentElement.style.setProperty('--secondary-color', '#14b8a6');
    }
    
    applyVisualMode() {
        // Show timers
        this.showTimers();
        
        // Enhance diagrams
        this.enhanceDiagrams();
        
        // Hide Pomodoro
        const pomodoro = document.getElementById('pomodoro-widget');
        if (pomodoro) pomodoro.classList.add('hidden');
        
        // Hide TTS
        const tts = document.getElementById('tts-controls');
        if (tts) tts.classList.add('hidden');
        
        // Apply visual-friendly colors
        document.documentElement.style.setProperty('--primary-color', '#7c3aed');
        document.documentElement.style.setProperty('--secondary-color', '#8b5cf6');
    }
    
    applyFocusMode() {
        // Show timers
        this.showTimers();
        
        // Show Pomodoro
        const pomodoro = document.getElementById('pomodoro-widget');
        if (pomodoro) pomodoro.classList.remove('hidden');
        
        // Hide TTS
        const tts = document.getElementById('tts-controls');
        if (tts) tts.classList.add('hidden');
        
        // Minimal UI
        document.body.classList.add('focus-mode-active');
        
        // Apply focus colors
        document.documentElement.style.setProperty('--primary-color', '#2563eb');
        document.documentElement.style.setProperty('--secondary-color', '#3b82f6');
    }
    
    applyReadingMode() {
        // Show timers
        this.showTimers();
        
        // Show TTS controls
        const tts = document.getElementById('tts-controls');
        if (tts) tts.classList.remove('hidden');
        
        // Hide Pomodoro
        const pomodoro = document.getElementById('pomodoro-widget');
        if (pomodoro) pomodoro.classList.add('hidden');
        
        // Enable TTS
        this.tts.enabled = true;
        
        // Chunk text
        this.chunkTextContent();
        
        // Apply reading-friendly colors
        document.documentElement.style.setProperty('--primary-color', '#059669');
        document.documentElement.style.setProperty('--secondary-color', '#10b981');
    }
    
    applyDefaultMode() {
        // Show timers
        this.showTimers();
        
        // Hide special widgets
        const pomodoro = document.getElementById('pomodoro-widget');
        if (pomodoro) pomodoro.classList.add('hidden');
        
        const tts = document.getElementById('tts-controls');
        if (tts) tts.classList.add('hidden');
        
        // Remove focus mode
        document.body.classList.remove('focus-mode-active');
        
        // Reset colors
        document.documentElement.style.setProperty('--primary-color', '#2563eb');
        document.documentElement.style.setProperty('--secondary-color', '#7c3aed');
    }
    
    hideTimers() {
        document.querySelectorAll('.timer, #practice-timer, #radar-timer').forEach(el => {
            el.dataset.originalDisplay = el.style.display;
            el.style.display = 'none';
        });
    }
    
    showTimers() {
        document.querySelectorAll('.timer, #practice-timer, #radar-timer').forEach(el => {
            el.style.display = el.dataset.originalDisplay || '';
        });
    }
    
    showCalmingElements() {
        // Add breathing exercise prompt
        if (!document.getElementById('calming-breathing')) {
            const breathing = document.createElement('div');
            breathing.id = 'calming-breathing';
            breathing.className = 'calming-breathing';
            breathing.innerHTML = `
                <div class="breathing-circle"></div>
                <p class="breathing-text">Breathe with the circle</p>
            `;
            document.body.appendChild(breathing);
        }
    }
    
    enhanceDiagrams() {
        // Add zoom functionality to diagrams
        document.querySelectorAll('.problem-diagrams img, .diagram-container img').forEach(img => {
            img.classList.add('visual-mode-enhanced');
            img.addEventListener('click', () => {
                this.showImageModal(img.src);
            });
        });
    }
    
    showImageModal(src) {
        const modal = document.createElement('div');
        modal.className = 'image-modal';
        modal.innerHTML = `
            <div class="image-modal-content">
                <button class="image-modal-close">&times;</button>
                <img src="${src}" alt="Enlarged diagram">
            </div>
        `;
        document.body.appendChild(modal);
        
        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('image-modal-close')) {
                modal.remove();
            }
        });
    }
    
    chunkTextContent() {
        // Add chunk navigation to long text
        document.querySelectorAll('.problem-text, .articulation-form').forEach(el => {
            if (el.textContent.length > 200 && !el.dataset.chunked) {
                this.createTextChunks(el);
            }
        });
    }
    
    createTextChunks(element) {
        const text = element.textContent;
        const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
        const chunks = [];
        let currentChunk = '';
        
        sentences.forEach(sentence => {
            if ((currentChunk + sentence).length > 150) {
                if (currentChunk) chunks.push(currentChunk.trim());
                currentChunk = sentence;
            } else {
                currentChunk += sentence;
            }
        });
        if (currentChunk) chunks.push(currentChunk.trim());
        
        if (chunks.length > 1) {
            element.dataset.chunked = 'true';
            element.dataset.chunks = JSON.stringify(chunks);
            element.dataset.currentChunk = '0';
            
            const chunkContainer = document.createElement('div');
            chunkContainer.className = 'text-chunks';
            chunkContainer.innerHTML = `
                <div class="chunk-content">${chunks[0]}</div>
                <div class="chunk-navigation">
                    <button class="chunk-btn chunk-prev" disabled>&larr; Previous</button>
                    <span class="chunk-indicator">1 / ${chunks.length}</span>
                    <button class="chunk-btn chunk-next">Next &rarr;</button>
                </div>
            `;
            
            element.innerHTML = '';
            element.appendChild(chunkContainer);
            
            // Event listeners
            const prevBtn = chunkContainer.querySelector('.chunk-prev');
            const nextBtn = chunkContainer.querySelector('.chunk-next');
            const content = chunkContainer.querySelector('.chunk-content');
            const indicator = chunkContainer.querySelector('.chunk-indicator');
            
            prevBtn.addEventListener('click', () => {
                let current = parseInt(element.dataset.currentChunk);
                if (current > 0) {
                    current--;
                    element.dataset.currentChunk = current;
                    content.textContent = chunks[current];
                    indicator.textContent = `${current + 1} / ${chunks.length}`;
                    prevBtn.disabled = current === 0;
                    nextBtn.disabled = false;
                }
            });
            
            nextBtn.addEventListener('click', () => {
                let current = parseInt(element.dataset.currentChunk);
                if (current < chunks.length - 1) {
                    current++;
                    element.dataset.currentChunk = current;
                    content.textContent = chunks[current];
                    indicator.textContent = `${current + 1} / ${chunks.length}`;
                    nextBtn.disabled = current === chunks.length - 1;
                    prevBtn.disabled = false;
                }
            });
        }
    }
    
    // Pomodoro methods
    startPomodoro() {
        if (this.pomodoro.interval) return;
        
        this.pomodoro.active = true;
        const widget = document.getElementById('pomodoro-widget');
        widget.querySelector('.pomodoro-start').classList.add('hidden');
        widget.querySelector('.pomodoro-pause').classList.remove('hidden');
        
        this.pomodoro.interval = setInterval(() => {
            this.pomodoro.timeRemaining--;
            this.updatePomodoroDisplay();
            
            if (this.pomodoro.timeRemaining <= 0) {
                this.completePomodoroPhase();
            }
        }, 1000);
    }
    
    pausePomodoro() {
        if (!this.pomodoro.interval) return;
        
        clearInterval(this.pomodoro.interval);
        this.pomodoro.interval = null;
        
        const widget = document.getElementById('pomodoro-widget');
        widget.querySelector('.pomodoro-start').classList.remove('hidden');
        widget.querySelector('.pomodoro-pause').classList.add('hidden');
        
        this.pomodoro.active = false;
    }
    
    resetPomodoro() {
        this.pausePomodoro();
        this.pomodoro.isBreak = false;
        this.pomodoro.timeRemaining = this.pomodoro.workTime;
        this.updatePomodoroDisplay();
        
        const widget = document.getElementById('pomodoro-widget');
        widget.querySelector('.pomodoro-status').textContent = 'Ready to focus';
    }
    
    updatePomodoroDisplay() {
        const minutes = Math.floor(this.pomodoro.timeRemaining / 60);
        const seconds = this.pomodoro.timeRemaining % 60;
        const timeStr = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        
        const widget = document.getElementById('pomodoro-widget');
        widget.querySelector('.pomodoro-time').textContent = timeStr;
    }
    
    completePomodoroPhase() {
        this.pausePomodoro();
        
        // Play notification sound
        this.playNotificationSound();
        
        if (!this.pomodoro.isBreak) {
            // Work phase complete
            alert('Focus time complete! Take a break.');
            this.pomodoro.isBreak = true;
            this.pomodoro.timeRemaining = this.pomodoro.breakTime;
            
            const widget = document.getElementById('pomodoro-widget');
            widget.querySelector('.pomodoro-status').textContent = 'Break time!';
        } else {
            // Break phase complete
            alert('Break over! Ready to focus?');
            this.pomodoro.isBreak = false;
            this.pomodoro.timeRemaining = this.pomodoro.workTime;
            
            const widget = document.getElementById('pomodoro-widget');
            widget.querySelector('.pomodoro-status').textContent = 'Ready to focus';
        }
        
        this.updatePomodoroDisplay();
    }
    
    playNotificationSound() {
        // Simple beep using Web Audio API
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = 800;
            oscillator.type = 'sine';
            
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
            
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 0.5);
        } catch (e) {
            console.log('Could not play notification sound');
        }
    }
    
    // TTS methods
    playTTS() {
        if (!this.tts.synth) {
            alert('Text-to-speech is not supported in your browser');
            return;
        }
        
        // Get text to read
        const text = this.getSelectedText() || this.getMainContentText();
        if (!text) return;
        
        const controls = document.getElementById('tts-controls');
        const rate = parseFloat(controls.querySelector('.tts-rate').value);
        const pitch = parseFloat(controls.querySelector('.tts-pitch').value);
        
        // Split into chunks
        const chunks = this.splitTextIntoChunks(text);
        this.tts.chunks = chunks;
        this.tts.currentChunkIndex = 0;
        
        controls.querySelector('.tts-chunk-total').textContent = chunks.length;
        
        this.speakChunk(chunks[0], rate, pitch);
        
        controls.querySelector('.tts-play').classList.add('hidden');
        controls.querySelector('.tts-pause').classList.remove('hidden');
    }
    
    speakChunk(text, rate, pitch) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = rate;
        utterance.pitch = pitch;
        
        if (this.tts.voices.length > 0) {
            utterance.voice = this.tts.voices.find(v => v.lang === 'en-US') || this.tts.voices[0];
        }
        
        utterance.onend = () => {
            this.tts.currentChunkIndex++;
            const controls = document.getElementById('tts-controls');
            controls.querySelector('.tts-chunk-current').textContent = this.tts.currentChunkIndex + 1;
            
            if (this.tts.currentChunkIndex < this.tts.chunks.length) {
                this.speakChunk(this.tts.chunks[this.tts.currentChunkIndex], rate, pitch);
            } else {
                this.tts.speaking = false;
                controls.querySelector('.tts-play').classList.remove('hidden');
                controls.querySelector('.tts-pause').classList.add('hidden');
            }
        };
        
        this.tts.currentUtterance = utterance;
        this.tts.speaking = true;
        this.tts.synth.speak(utterance);
    }
    
    pauseTTS() {
        if (this.tts.synth) {
            this.tts.synth.pause();
            this.tts.speaking = false;
            
            const controls = document.getElementById('tts-controls');
            controls.querySelector('.tts-play').classList.remove('hidden');
            controls.querySelector('.tts-pause').classList.add('hidden');
        }
    }
    
    stopTTS() {
        if (this.tts.synth) {
            this.tts.synth.cancel();
            this.tts.speaking = false;
            this.tts.currentChunkIndex = 0;
            
            const controls = document.getElementById('tts-controls');
            controls.querySelector('.tts-play').classList.remove('hidden');
            controls.querySelector('.tts-pause').classList.add('hidden');
            controls.querySelector('.tts-chunk-current').textContent = '1';
        }
    }
    
    getSelectedText() {
        const selection = window.getSelection();
        return selection.toString().trim();
    }
    
    getMainContentText() {
        const content = document.querySelector('.problem-text, .main-content, article');
        return content ? content.textContent.trim() : '';
    }
    
    splitTextIntoChunks(text, maxLength = 200) {
        const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
        const chunks = [];
        let currentChunk = '';
        
        sentences.forEach(sentence => {
            if ((currentChunk + sentence).length > maxLength) {
                if (currentChunk) chunks.push(currentChunk.trim());
                currentChunk = sentence;
            } else {
                currentChunk += sentence;
            }
        });
        if (currentChunk) chunks.push(currentChunk.trim());
        
        return chunks.length > 0 ? chunks : [text];
    }
    
    // Storage methods
    saveMode() {
        localStorage.setItem(this.options.storageKey, this.currentMode);
    }
    
    loadMode() {
        const saved = localStorage.getItem(this.options.storageKey);
        if (saved && this.modes[saved]) {
            this.currentMode = saved;
        }
    }
    
    updateModeSelector() {
        const selector = document.getElementById('persona-mode-selector');
        if (!selector) return;
        
        const toggle = selector.querySelector('.persona-mode-toggle');
        toggle.querySelector('.persona-mode-icon').textContent = this.modes[this.currentMode].icon;
        toggle.querySelector('.persona-mode-name').textContent = this.modes[this.currentMode].name;
        
        selector.querySelectorAll('.persona-mode-option').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === this.currentMode);
        });
    }
    
    // Public API
    getCurrentMode() {
        return this.currentMode;
    }
    
    isModeActive(mode) {
        return this.currentMode === mode;
    }
    
    togglePomodoro() {
        const widget = document.getElementById('pomodoro-widget');
        if (widget) {
            widget.classList.toggle('hidden');
        }
    }
    
    toggleTTS() {
        const controls = document.getElementById('tts-controls');
        if (controls) {
            controls.classList.toggle('hidden');
        }
    }
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PersonaUI;
}
