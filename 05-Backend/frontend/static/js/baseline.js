// Baseline Test Module
// Handles baseline test printing and scan upload
console.log('baseline.js script loaded');

class Baseline {
    constructor() {
        console.log('Baseline constructor called');
        this.printBtn = document.getElementById('print-baseline');
        this.uploadForm = document.getElementById('upload-baseline-form');
        this.fileInput = document.getElementById('baseline-file');
        this.uploadStatus = document.getElementById('baseline-upload-status');
        this.resultsSection = document.getElementById('baseline-results');
        this.gapMap = document.getElementById('gap-map');
        
        console.log('Elements found:', {
            printBtn: !!this.printBtn,
            uploadForm: !!this.uploadForm,
            fileInput: !!this.fileInput,
            uploadStatus: !!this.uploadStatus,
            resultsSection: !!this.resultsSection,
            gapMap: !!this.gapMap
        });
        
        // Check if baseline page is active
        const baselinePage = document.getElementById('page-baseline');
        if (baselinePage) {
            const isActive = baselinePage.classList.contains('active');
            console.log('Baseline page active:', isActive);
            if (!isActive) {
                console.warn('Baseline page is not active! Navigation may have failed.');
                // Optional: force activate (may conflict with navigation)
                // baselinePage.classList.add('active');
            }
        }
        
        // Check if api is available
        console.log('API available:', typeof api !== 'undefined');
        console.log('window.api:', window.api);
        console.log('global api variable:', typeof api);
        
        this.init();
    }

    init() {
        console.log('Baseline init called');
        // Print baseline test
        this.printBtn.addEventListener('click', (e) => {
            console.log('Print baseline clicked');
            e.preventDefault();
            e.stopPropagation();
            this.printBaseline();
        });

        // Handle file upload
        this.uploadForm.addEventListener('submit', (e) => {
            console.log('Upload form submitted');
            e.preventDefault();
            this.handleUpload();
        });

        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            console.log('Page load event:', e.detail.page);
            if (e.detail.page === 'baseline') {
                this.checkForExistingResults();
            }
        });

        // Check if we're already on baseline page (in case pageLoad fired before we registered)
        if (window.navigation && window.navigation.currentPage === 'baseline') {
            console.log('Already on baseline page, checking for existing results');
            this.checkForExistingResults();
        }

        // Safety: if hash is baseline but page isn't active, try to navigate
        setTimeout(() => {
            console.log('[SAFETY CHECK] Running safety check for baseline page');
            const hash = window.location.hash.substring(1);
            console.log('[SAFETY CHECK] Current hash:', hash);
            console.log('[SAFETY CHECK] window.navigation exists:', !!window.navigation);
            if (window.navigation) {
                console.log('[SAFETY CHECK] navigation.currentPage:', window.navigation.currentPage);
            }
            const baselinePage = document.getElementById('page-baseline');
            console.log('[SAFETY CHECK] Baseline page element exists:', !!baselinePage);
            if (baselinePage) {
                console.log('[SAFETY CHECK] Baseline page active:', baselinePage.classList.contains('active'));
            }
            
            if (hash === 'baseline') {
                if (baselinePage && !baselinePage.classList.contains('active')) {
                    console.warn('[SAFETY CHECK] Baseline page not active despite hash, attempting navigation...');
                    if (window.navigation && window.navigation.navigateTo) {
                        console.log('[SAFETY CHECK] Calling navigation.navigateTo("baseline")');
                        window.navigation.navigateTo('baseline');
                    } else {
                        console.error('[SAFETY CHECK] Navigation not available, using fallback');
                        // Fallback: manually activate this page
                        baselinePage.classList.add('active');
                        // Deactivate other pages
                        document.querySelectorAll('.page').forEach(p => {
                            if (p.id !== 'page-baseline') p.classList.remove('active');
                        });
                        console.log('[SAFETY CHECK] Manually activated baseline page');
                    }
                } else {
                    console.log('[SAFETY CHECK] Baseline page already active or not found');
                }
            } else {
                console.log('[SAFETY CHECK] Hash is not baseline, ignoring');
            }
        }, 200);
    }

    printBaseline() {
        console.log('printBaseline called');
        try {
            // Check if api is available
            if (typeof api === 'undefined') {
                console.error('api is undefined in printBaseline');
                this.showStatus('API not available. Please refresh the page.', 'error');
                return;
            }
            
            // Open PDF in new tab
            console.log('Getting PDF URL for week 1');
            const pdfUrl = api.getProblemsPdf(1);
            console.log('PDF URL:', pdfUrl);
            window.open(pdfUrl, '_blank');
            console.log('PDF opened in new tab');
        } catch (error) {
            console.error('Error in printBaseline:', error);
            this.showStatus(`Failed to open PDF: ${error.message}`, 'error');
        }
    }

    async handleUpload() {
        console.log('handleUpload called');
        const file = this.fileInput.files[0];
        console.log('Selected file:', file ? file.name : 'none');
        if (!file) {
            this.showStatus('Please select a file to upload.', 'error');
            return;
        }

        // Wait for API client to be available (race condition safety)
        let apiClient = window.api || api;
        let attempts = 0;
        const maxAttempts = 10;
        const waitMs = 100;
        while (!apiClient && attempts < maxAttempts) {
            console.log(`Waiting for API client (attempt ${attempts + 1}/${maxAttempts})...`);
            await new Promise(resolve => setTimeout(resolve, waitMs));
            apiClient = window.api || api;
            attempts++;
        }
        
        console.log('API client check:', { 
            'window.api': window.api, 
            'global api': api, 
            'selected client': apiClient,
            'attempts': attempts
        });
        
        if (!apiClient) {
            console.error('api object not found after waiting', maxAttempts * waitMs, 'ms');
            this.showStatus('API not available. Please refresh the page.', 'error');
            return;
        }

        if (!apiClient.uploadScan) {
            console.error('api.uploadScan method not found', apiClient);
            this.showStatus('Upload function not available.', 'error');
            return;
        }

        this.showStatus('Uploading scan...', 'processing');
        this.uploadForm.querySelector('button[type="submit"]').disabled = true;

        try {
            // Upload scan
            console.log('Calling apiClient.uploadScan');
            const scanData = await apiClient.uploadScan(1, file);
            console.log('Upload response:', scanData);
            
            // Poll for OCR completion
            this.showStatus('Processing OCR... This may take up to 30 seconds.', 'processing');
            console.log('Starting OCR polling for scan:', scanData.id);
            await this.pollForOcrCompletion(scanData.id);
            console.log('OCR polling completed');
            
            // Show results
            console.log('Calling showResults');
            this.showResults(scanData.id);
            
        } catch (error) {
            console.error('Upload failed:', error);
            // Try to get more error details
            let errorMessage = 'Upload failed. Please try again.';
            if (error.message && error.message.includes('HTTP error')) {
                errorMessage = `Server error: ${error.message}`;
            }
            this.showStatus(errorMessage, 'error');
        } finally {
            this.uploadForm.querySelector('button[type="submit"]').disabled = false;
        }
    }

    async pollForOcrCompletion(scanId, maxAttempts = 12, interval = 2500) {
        console.log('pollForOcrCompletion called:', scanId);
        for (let i = 0; i < maxAttempts; i++) {
            console.log(`Poll attempt ${i+1}/${maxAttempts}`);
            const scanData = await api.getScan(scanId);
            console.log('Scan data:', scanData);
            
            if (scanData.status === 'completed') {
                console.log('OCR completed');
                return scanData;
            }
            
            console.log('Still processing, waiting', interval, 'ms');
            // Wait before next poll
            await new Promise(resolve => setTimeout(resolve, interval));
        }
        
        console.error('OCR processing timed out');
        throw new Error('OCR processing timed out');
    }

    async showResults(scanId) {
        console.log('showResults called:', scanId);
        try {
            console.log('Fetching scan data');
            const scanData = await api.getScan(scanId);
            console.log('Scan data:', scanData);
            console.log('Fetching baseline analytics');
            const baselineData = await api.getBaselineAnalytics();
            console.log('Baseline analytics:', baselineData);
            
            console.log('Removing hidden class from results section');
            this.resultsSection.classList.remove('hidden');
            // Safety check: ensure element is visible
            if (this.resultsSection.classList.contains('hidden')) {
                console.warn('Hidden class still present, forcing display');
                this.resultsSection.style.display = 'block';
            }
            console.log('Rendering gap map');
            this.renderGapMap(baselineData.gapMap, baselineData.scoresByPathway);
            
            this.showStatus('✅ Baseline test processed successfully!', 'success');
            console.log('Results shown successfully');
            
        } catch (error) {
            console.error('Failed to load results:', error);
            this.showStatus('Failed to load results. Please try again.', 'error');
        }
    }

    renderGapMap(gapMap, scoresByPathway) {
        const weakestPathways = gapMap.weakestPathways;
        
        this.gapMap.innerHTML = `
            <h3>Top 3 Weakest Pathways</h3>
            ${weakestPathways.map((pathway, index) => `
                <div class="gap-item weak">
                    <div>
                        <strong>#${index + 1} ${pathway.pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong>
                        <div style="font-size: 0.9rem; color: var(--text-light); margin-top: 0.25rem;">
                            Accuracy: ${(pathway.accuracy * 100).toFixed(0)}%
                        </div>
                    </div>
                    <i class="fas fa-arrow-down" style="color: var(--danger-color); font-size: 1.5rem;"></i>
                </div>
            `).join('')}
            
            <h3 style="margin-top: 2rem;">All Pathway Scores</h3>
            ${Object.entries(scoresByPathway).map(([pathway, score]) => {
                const strength = score >= 0.7 ? 'strong' : score >= 0.5 ? 'moderate' : 'weak';
                return `
                    <div class="gap-item ${strength}">
                        <div>
                            <strong>${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: bold; color: var(--${strength === 'strong' ? 'success' : strength === 'moderate' ? 'warning' : 'danger'}-color);">
                            ${(score * 100).toFixed(0)}%
                        </div>
                    </div>
                `;
            }).join('')}
            
            <div style="margin-top: 2rem; padding: 1.5rem; background: #eff6ff; border-radius: 0.5rem; border-left: 4px solid var(--primary-color);">
                <h4><i class="fas fa-info-circle"></i> Next Steps</h4>
                <p style="margin-top: 0.5rem;">
                    Based on your baseline results, we recommend focusing on the following pathways during Weeks 2-4:
                </p>
                <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                    ${weakestPathways.slice(0, 3).map(p => `
                        <li>${p.pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</li>
                    `).join('')}
                </ul>
            </div>
        `;
    }

    showStatus(message, type) {
        this.uploadStatus.textContent = message;
        this.uploadStatus.className = `upload-status ${type}`;
    }

    async checkForExistingResults() {
        // Check if there's existing baseline data and show results
        try {
            const baselineData = await api.getBaselineAnalytics();
            if (baselineData.completedAt && baselineData.scanId && baselineData.scanId !== 'scan_001') {
                console.log('Found existing baseline data, scanId:', baselineData.scanId);
                this.showResults(baselineData.scanId);
            } else {
                console.log('No real baseline data found (placeholder or missing)');
            }
        } catch (error) {
            // No existing baseline data
            console.log('No baseline data available:', error.message);
        }
    }
}

// Initialize baseline when DOM is ready
let baseline;
function initBaseline() {
    if (baseline) return; // Already initialized
    baseline = new Baseline();
    // Expose baseline on window for debugging and inline handlers
    window.baseline = baseline;
    console.log('Baseline initialized and exposed on window');
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBaseline);
} else {
    // DOM already loaded, initialize now
    initBaseline();
}
