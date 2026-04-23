// AccessibilityPanel.js - Accessibility Controls Panel
// Provides font size adjustment, color contrast settings, motion reduction, and keyboard shortcuts

class AccessibilityPanel {
    constructor(options = {}) {
        this.options = {
            storageKey: 'accessibility-settings',
            defaultFontSize: options.defaultFontSize || 100, // percentage
            minFontSize: options.minFontSize || 80,
            maxFontSize: options.maxFontSize || 150,
            fontSizeStep: options.fontSizeStep || 10,
            ...options
        };
        
        // Settings state
        this.settings = {
            fontSize: this.options.defaultFontSize,
            highContrast: false,
            reduceMotion: false,
            colorBlindMode: 'none', // none, protanopia, deuteranopia, tritanopia
            dyslexiaFont: false,
            lineSpacing: 'normal', // normal, wide, extra-wide
            wordSpacing: 'normal', // normal, wide
            focusIndicator: 'default', // default, enhanced
            screenReaderMode: false
        };
        
        // Keyboard shortcuts
        this.shortcuts = {
            'Alt+1': () => this.togglePanel(),
            'Alt+Plus': () => this.increaseFontSize(),
            'Alt+Minus': () => this.decreaseFontSize(),
            'Alt+0': () => this.resetFontSize(),
            'Alt+C': () => this.toggleHighContrast(),
            'Alt+M': () => this.toggleReduceMotion(),
            'Alt+R': () => this.toggleScreenReaderMode()
        };
        
        // Initialize
        this.init();
    }
    
    init() {
        // Load saved settings
        this.loadSettings();
        
        // Create UI
        this.createPanel();
        this.createToggleButton();
        
        // Apply initial settings
        this.applySettings();
        
        // Setup keyboard shortcuts
        this.setupKeyboardShortcuts();
        
        // Setup screen reader announcements
        this.setupScreenReaderSupport();
    }
    
    createPanel() {
        if (document.getElementById('accessibility-panel')) return;
        
        const panel = document.createElement('div');
        panel.id = 'accessibility-panel';
        panel.className = 'accessibility-panel hidden';
        panel.setAttribute('role', 'dialog');
        panel.setAttribute('aria-label', 'Accessibility Settings');
        
        panel.innerHTML = `
            <div class="accessibility-panel-header">
                <h2><i class="fas fa-universal-access"></i> Accessibility</h2>
                <button class="accessibility-panel-close" aria-label="Close accessibility panel">&times;</button>
            </div>
            
            <div class="accessibility-panel-content">
                <!-- Font Size Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-font"></i> Text Size</h3>
                    <div class="font-size-controls">
                        <button class="a11y-btn font-size-decrease" aria-label="Decrease font size">
                            <i class="fas fa-minus"></i> A
                        </button>
                        <span class="font-size-value">${this.settings.fontSize}%</span>
                        <button class="a11y-btn font-size-increase" aria-label="Increase font size">
                            A <i class="fas fa-plus"></i>
                        </button>
                        <button class="a11y-btn font-size-reset" aria-label="Reset font size">
                            <i class="fas fa-undo"></i>
                        </button>
                    </div>
                    <input type="range" class="font-size-slider" 
                           min="${this.options.minFontSize}" 
                           max="${this.options.maxFontSize}" 
                           value="${this.settings.fontSize}" 
                           step="${this.options.fontSizeStep}"
                           aria-label="Font size slider">
                </div>
                
                <!-- Contrast Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-adjust"></i> Contrast</h3>
                    <label class="a11y-toggle">
                        <input type="checkbox" class="high-contrast-toggle" 
                               ${this.settings.highContrast ? 'checked' : ''}>
                        <span class="toggle-slider"></span>
                        <span class="toggle-label">High Contrast Mode</span>
                    </label>
                    
                    <div class="color-blind-options">
                        <label for="color-blind-mode">Color Vision:</label>
                        <select id="color-blind-mode" class="a11y-select">
                            <option value="none" ${this.settings.colorBlindMode === 'none' ? 'selected' : ''}>Normal</option>
                            <option value="protanopia" ${this.settings.colorBlindMode === 'protanopia' ? 'selected' : ''}>Protanopia (Red-blind)</option>
                            <option value="deuteranopia" ${this.settings.colorBlindMode === 'deuteranopia' ? 'selected' : ''}>Deuteranopia (Green-blind)</option>
                            <option value="tritanopia" ${this.settings.colorBlindMode === 'tritanopia' ? 'selected' : ''}>Tritanopia (Blue-blind)</option>
                            <option value="achromatopsia" ${this.settings.colorBlindMode === 'achromatopsia' ? 'selected' : ''}>Achromatopsia (Monochrome)</option>
                        </select>
                    </div>
                </div>
                
                <!-- Motion Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-running"></i> Motion</h3>
                    <label class="a11y-toggle">
                        <input type="checkbox" class="reduce-motion-toggle" 
                               ${this.settings.reduceMotion ? 'checked' : ''}>
                        <span class="toggle-slider"></span>
                        <span class="toggle-label">Reduce Motion</span>
                    </label>
                </div>
                
                <!-- Reading Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-book-reader"></i> Reading</h3>
                    <label class="a11y-toggle">
                        <input type="checkbox" class="dyslexia-font-toggle" 
                               ${this.settings.dyslexiaFont ? 'checked' : ''}>
                        <span class="toggle-slider"></span>
                        <span class="toggle-label">Dyslexia-friendly Font</span>
                    </label>
                    
                    <div class="spacing-options">
                        <label for="line-spacing">Line Spacing:</label>
                        <select id="line-spacing" class="a11y-select">
                            <option value="normal" ${this.settings.lineSpacing === 'normal' ? 'selected' : ''}>Normal</option>
                            <option value="wide" ${this.settings.lineSpacing === 'wide' ? 'selected' : ''}>Wide</option>
                            <option value="extra-wide" ${this.settings.lineSpacing === 'extra-wide' ? 'selected' : ''}>Extra Wide</option>
                        </select>
                    </div>
                    
                    <div class="spacing-options">
                        <label for="word-spacing">Word Spacing:</label>
                        <select id="word-spacing" class="a11y-select">
                            <option value="normal" ${this.settings.wordSpacing === 'normal' ? 'selected' : ''}>Normal</option>
                            <option value="wide" ${this.settings.wordSpacing === 'wide' ? 'selected' : ''}>Wide</option>
                        </select>
                    </div>
                </div>
                
                <!-- Focus Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-crosshairs"></i> Focus</h3>
                    <label for="focus-indicator">Focus Indicator:</label>
                    <select id="focus-indicator" class="a11y-select">
                        <option value="default" ${this.settings.focusIndicator === 'default' ? 'selected' : ''}>Default</option>
                        <option value="enhanced" ${this.settings.focusIndicator === 'enhanced' ? 'selected' : ''}>Enhanced (High Visibility)</option>
                    </select>
                </div>
                
                <!-- Screen Reader Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-volume-up"></i> Screen Reader</h3>
                    <label class="a11y-toggle">
                        <input type="checkbox" class="screen-reader-toggle" 
                               ${this.settings.screenReaderMode ? 'checked' : ''}>
                        <span class="toggle-slider"></span>
                        <span class="toggle-label">Enhanced Screen Reader Mode</span>
                    </label>
                    <p class="a11y-hint">Announces page changes and dynamic content</p>
                </div>
                
                <!-- Keyboard Shortcuts Section -->
                <div class="accessibility-section">
                    <h3><i class="fas fa-keyboard"></i> Keyboard Shortcuts</h3>
                    <ul class="keyboard-shortcuts-list">
                        <li><kbd>Alt + 1</kbd> Toggle this panel</li>
                        <li><kbd>Alt + Plus</kbd> Increase font size</li>
                        <li><kbd>Alt + Minus</kbd> Decrease font size</li>
                        <li><kbd>Alt + 0</kbd> Reset font size</li>
                        <li><kbd>Alt + C</kbd> Toggle high contrast</li>
                        <li><kbd>Alt + M</kbd> Toggle reduce motion</li>
                        <li><kbd>Alt + R</kbd> Toggle screen reader mode</li>
                        <li><kbd>Tab</kbd> Navigate between elements</li>
                        <li><kbd>Enter</kbd> Activate selected element</li>
                        <li><kbd>Escape</kbd> Close panel/dialog</li>
                    </ul>
                </div>
            </div>
        `;
        
        document.body.appendChild(panel);
        
        // Event listeners
        this.attachEventListeners(panel);
    }
    
    createToggleButton() {
        if (document.getElementById('accessibility-toggle-btn')) return;
        
        const button = document.createElement('button');
        button.id = 'accessibility-toggle-btn';
        button.className = 'accessibility-toggle-btn';
        button.setAttribute('aria-label', 'Open accessibility settings');
        button.setAttribute('title', 'Accessibility Settings (Alt+1)');
        button.innerHTML = '<i class="fas fa-universal-access"></i>';
        
        document.body.appendChild(button);
        
        button.addEventListener('click', () => this.togglePanel());
    }
    
    attachEventListeners(panel) {
        // Close button
        panel.querySelector('.accessibility-panel-close').addEventListener('click', () => {
            this.togglePanel(false);
        });
        
        // Font size controls
        panel.querySelector('.font-size-decrease').addEventListener('click', () => this.decreaseFontSize());
        panel.querySelector('.font-size-increase').addEventListener('click', () => this.increaseFontSize());
        panel.querySelector('.font-size-reset').addEventListener('click', () => this.resetFontSize());
        
        const slider = panel.querySelector('.font-size-slider');
        slider.addEventListener('input', (e) => this.setFontSize(parseInt(e.target.value)));
        
        // Toggle switches
        panel.querySelector('.high-contrast-toggle').addEventListener('change', (e) => {
            this.settings.highContrast = e.target.checked;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('.reduce-motion-toggle').addEventListener('change', (e) => {
            this.settings.reduceMotion = e.target.checked;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('.dyslexia-font-toggle').addEventListener('change', (e) => {
            this.settings.dyslexiaFont = e.target.checked;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('.screen-reader-toggle').addEventListener('change', (e) => {
            this.settings.screenReaderMode = e.target.checked;
            this.applySettings();
            this.saveSettings();
        });
        
        // Select dropdowns
        panel.querySelector('#color-blind-mode').addEventListener('change', (e) => {
            this.settings.colorBlindMode = e.target.value;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('#line-spacing').addEventListener('change', (e) => {
            this.settings.lineSpacing = e.target.value;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('#word-spacing').addEventListener('change', (e) => {
            this.settings.wordSpacing = e.target.value;
            this.applySettings();
            this.saveSettings();
        });
        
        panel.querySelector('#focus-indicator').addEventListener('change', (e) => {
            this.settings.focusIndicator = e.target.value;
            this.applySettings();
            this.saveSettings();
        });
        
        // Close on escape key
        panel.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.togglePanel(false);
            }
        });
        
        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (panel.classList.contains('hidden')) return;
            if (!panel.contains(e.target) && !e.target.closest('#accessibility-toggle-btn')) {
                this.togglePanel(false);
            }
        });
    }
    
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            const key = [];
            if (e.altKey) key.push('Alt');
            if (e.ctrlKey) key.push('Ctrl');
            if (e.metaKey) key.push('Meta');
            if (e.shiftKey) key.push('Shift');
            
            // Handle special keys
            let keyName = e.key;
            if (e.key === '+') keyName = 'Plus';
            if (e.key === '-') keyName = 'Minus';
            if (e.key === '0') keyName = '0';
            
            key.push(keyName);
            
            const shortcut = key.join('+');
            
            if (this.shortcuts[shortcut]) {
                e.preventDefault();
                this.shortcuts[shortcut]();
            }
        });
    }
    
    setupScreenReaderSupport() {
        // Create live region for announcements
        if (!document.getElementById('sr-announcements')) {
            const liveRegion = document.createElement('div');
            liveRegion.id = 'sr-announcements';
            liveRegion.setAttribute('aria-live', 'polite');
            liveRegion.setAttribute('aria-atomic', 'true');
            liveRegion.className = 'sr-only';
            document.body.appendChild(liveRegion);
        }
        
        // Monitor for dynamic content changes
        if (this.settings.screenReaderMode) {
            this.observeDynamicContent();
        }
    }
    
    observeDynamicContent() {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    // Check for important dynamic content
                    mutation.addedNodes.forEach(node => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Announce feedback messages
                            if (node.classList.contains('feedback-card') || 
                                node.classList.contains('triad-feedback')) {
                                this.announceToScreenReader('New feedback available');
                            }
                            
                            // Announce new problems
                            if (node.classList.contains('problem-display')) {
                                this.announceToScreenReader('New problem loaded');
                            }
                            
                            // Announce alerts
                            if (node.classList.contains('error-banner') || 
                                node.classList.contains('gaming-warning-notification')) {
                                const text = node.textContent || 'Alert';
                                this.announceToScreenReader(text, 'assertive');
                            }
                        }
                    });
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }
    
    announceToScreenReader(message, priority = 'polite') {
        const liveRegion = document.getElementById('sr-announcements');
        if (!liveRegion) return;
        
        liveRegion.setAttribute('aria-live', priority);
        liveRegion.textContent = message;
        
        // Clear after announcement
        setTimeout(() => {
            liveRegion.textContent = '';
        }, 1000);
    }
    
    // Font size methods
    increaseFontSize() {
        const newSize = Math.min(this.settings.fontSize + this.options.fontSizeStep, this.options.maxFontSize);
        this.setFontSize(newSize);
    }
    
    decreaseFontSize() {
        const newSize = Math.max(this.settings.fontSize - this.options.fontSizeStep, this.options.minFontSize);
        this.setFontSize(newSize);
    }
    
    resetFontSize() {
        this.setFontSize(this.options.defaultFontSize);
    }
    
    setFontSize(size) {
        this.settings.fontSize = size;
        this.applySettings();
        this.saveSettings();
        this.updatePanelUI();
    }
    
    // Toggle methods
    toggleHighContrast() {
        this.settings.highContrast = !this.settings.highContrast;
        this.applySettings();
        this.saveSettings();
        this.updatePanelUI();
    }
    
    toggleReduceMotion() {
        this.settings.reduceMotion = !this.settings.reduceMotion;
        this.applySettings();
        this.saveSettings();
        this.updatePanelUI();
    }
    
    toggleScreenReaderMode() {
        this.settings.screenReaderMode = !this.settings.screenReaderMode;
        this.applySettings();
        this.saveSettings();
        this.updatePanelUI();
        
        if (this.settings.screenReaderMode) {
            this.setupScreenReaderSupport();
        }
    }
    
    togglePanel(show = null) {
        const panel = document.getElementById('accessibility-panel');
        if (!panel) return;
        
        const shouldShow = show !== null ? show : panel.classList.contains('hidden');
        
        if (shouldShow) {
            panel.classList.remove('hidden');
            panel.setAttribute('aria-hidden', 'false');
            // Focus first focusable element
            const firstFocusable = panel.querySelector('button, input, select');
            if (firstFocusable) firstFocusable.focus();
        } else {
            panel.classList.add('hidden');
            panel.setAttribute('aria-hidden', 'true');
            // Return focus to toggle button
            const toggleBtn = document.getElementById('accessibility-toggle-btn');
            if (toggleBtn) toggleBtn.focus();
        }
    }
    
    // Apply settings
    applySettings() {
        const html = document.documentElement;
        const body = document.body;
        
        // Font size
        html.style.fontSize = `${this.settings.fontSize}%`;
        
        // High contrast
        if (this.settings.highContrast) {
            body.classList.add('high-contrast-mode');
        } else {
            body.classList.remove('high-contrast-mode');
        }
        
        // Reduce motion
        if (this.settings.reduceMotion) {
            body.classList.add('reduce-motion');
        } else {
            body.classList.remove('reduce-motion');
        }
        
        // Dyslexia font
        if (this.settings.dyslexiaFont) {
            body.classList.add('dyslexia-font');
        } else {
            body.classList.remove('dyslexia-font');
        }
        
        // Color blind mode
        body.classList.remove('protanopia', 'deuteranopia', 'tritanopia', 'achromatopsia');
        if (this.settings.colorBlindMode !== 'none') {
            body.classList.add(this.settings.colorBlindMode);
        }
        
        // Line spacing
        body.classList.remove('line-spacing-normal', 'line-spacing-wide', 'line-spacing-extra-wide');
        body.classList.add(`line-spacing-${this.settings.lineSpacing}`);
        
        // Word spacing
        body.classList.remove('word-spacing-normal', 'word-spacing-wide');
        body.classList.add(`word-spacing-${this.settings.wordSpacing}`);
        
        // Focus indicator
        body.classList.remove('focus-default', 'focus-enhanced');
        body.classList.add(`focus-${this.settings.focusIndicator}`);
        
        // Screen reader mode
        if (this.settings.screenReaderMode) {
            body.classList.add('screen-reader-mode');
        } else {
            body.classList.remove('screen-reader-mode');
        }
    }
    
    updatePanelUI() {
        const panel = document.getElementById('accessibility-panel');
        if (!panel) return;
        
        // Update font size display
        panel.querySelector('.font-size-value').textContent = `${this.settings.fontSize}%`;
        panel.querySelector('.font-size-slider').value = this.settings.fontSize;
        
        // Update toggles
        panel.querySelector('.high-contrast-toggle').checked = this.settings.highContrast;
        panel.querySelector('.reduce-motion-toggle').checked = this.settings.reduceMotion;
        panel.querySelector('.dyslexia-font-toggle').checked = this.settings.dyslexiaFont;
        panel.querySelector('.screen-reader-toggle').checked = this.settings.screenReaderMode;
        
        // Update selects
        panel.querySelector('#color-blind-mode').value = this.settings.colorBlindMode;
        panel.querySelector('#line-spacing').value = this.settings.lineSpacing;
        panel.querySelector('#word-spacing').value = this.settings.wordSpacing;
        panel.querySelector('#focus-indicator').value = this.settings.focusIndicator;
    }
    
    // Storage methods
    saveSettings() {
        localStorage.setItem(this.options.storageKey, JSON.stringify(this.settings));
    }
    
    loadSettings() {
        try {
            const saved = localStorage.getItem(this.options.storageKey);
            if (saved) {
                const parsed = JSON.parse(saved);
                this.settings = { ...this.settings, ...parsed };
            }
        } catch (e) {
            console.error('Failed to load accessibility settings:', e);
        }
    }
    
    // Public API
    getSettings() {
        return { ...this.settings };
    }
    
    updateSetting(key, value) {
        if (this.settings.hasOwnProperty(key)) {
            this.settings[key] = value;
            this.applySettings();
            this.saveSettings();
            this.updatePanelUI();
        }
    }
    
    resetSettings() {
        this.settings = {
            fontSize: this.options.defaultFontSize,
            highContrast: false,
            reduceMotion: false,
            colorBlindMode: 'none',
            dyslexiaFont: false,
            lineSpacing: 'normal',
            wordSpacing: 'normal',
            focusIndicator: 'default',
            screenReaderMode: false
        };
        this.applySettings();
        this.saveSettings();
        this.updatePanelUI();
    }
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AccessibilityPanel;
}
