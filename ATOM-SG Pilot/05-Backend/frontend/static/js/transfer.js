// Transfer Test Module
// Handles transfer test printing and scan upload

class Transfer {
    constructor() {
        this.printBtn = document.getElementById('print-transfer');
        this.uploadForm = document.getElementById('upload-transfer-form');
        this.fileInput = document.getElementById('transfer-file');
        this.uploadStatus = document.getElementById('transfer-upload-status');
        this.resultsSection = document.getElementById('transfer-results');
        this.rampUpMetrics = document.getElementById('ramp-up-metrics');
        this.successCriteria = document.getElementById('success-criteria');
        
        this.init();
    }

    init() {
        // Print transfer test - NOTE: Now handled by native <a> tag href
        // The button is an <a> tag with href="/api/v1/problems/pdf?week=5" target="_blank"
        // Keeping this listener only for logging/monitoring purposes
        if (this.printBtn) {
            this.printBtn.addEventListener('click', (e) => {
                console.log('Print transfer clicked - native link will handle navigation');
                // Let the anchor tag work naturally - don't intercept
            });
        }

        // Handle file upload
        this.uploadForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleUpload();
        });

        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'transfer') {
                this.checkForExistingResults();
            }
        });
    }

    printTransfer() {
        // Open PDF in new tab
        const pdfUrl = api.getProblemsPdf(5);
        window.open(pdfUrl, '_blank');
    }

    async handleUpload() {
        const file = this.fileInput.files[0];
        if (!file) {
            this.showStatus('Please select a file to upload.', 'error');
            return;
        }

        this.showStatus('Uploading scan...', 'processing');
        this.uploadForm.querySelector('button[type="submit"]').disabled = true;

        try {
            // Upload scan
            const scanData = await api.uploadScan(5, file);
            
            // Poll for OCR completion
            this.showStatus('Processing OCR... This may take up to 30 seconds.', 'processing');
            await this.pollForOcrCompletion(scanData.id);
            
            // Show results
            this.showResults();
            
        } catch (error) {
            console.error('Upload failed:', error);
            this.showStatus('Upload failed. Please try again.', 'error');
        } finally {
            this.uploadForm.querySelector('button[type="submit"]').disabled = false;
        }
    }

    async pollForOcrCompletion(scanId, maxAttempts = 12, interval = 2500) {
        for (let i = 0; i < maxAttempts; i++) {
            const scanData = await api.getScan(scanId);
            
            if (scanData.status === 'completed') {
                return scanData;
            }
            
            // Wait before next poll
            await new Promise(resolve => setTimeout(resolve, interval));
        }
        
        throw new Error('OCR processing timed out');
    }

    async showResults() {
        try {
            const data = await api.getTransferAnalytics();
            
            this.resultsSection.classList.remove('hidden');
            this.renderRampUpMetrics(data);
            this.renderSuccessCriteria(data.successCriteria);
            
            this.showStatus('✅ Transfer test processed successfully!', 'success');
            
        } catch (error) {
            console.error('Failed to load results:', error);
            this.showStatus('Failed to load results. Please try again.', 'error');
        }
    }

    renderRampUpMetrics(data) {
        this.rampUpMetrics.innerHTML = `
            <h3><i class="fas fa-chart-line"></i> Ramp-up Metrics</h3>
            
            <div style="background: #ecfdf5; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem; border-left: 4px solid var(--success-color);">
                <div style="font-size: 1.25rem; font-weight: bold; margin-bottom: 0.5rem;">
                    Overall Improvement
                </div>
                <div style="font-size: 2rem; font-weight: bold; color: var(--success-color);">
                    ${(data.rampUpMetrics.improvement * 100).toFixed(0)}%
                </div>
                <div style="color: var(--text-light); margin-top: 0.5rem;">
                    Baseline: ${(data.rampUpMetrics.baselineIdentificationAccuracy * 100).toFixed(0)}% → 
                    Transfer: ${(data.rampUpMetrics.transferIdentificationAccuracy * 100).toFixed(0)}%
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
                <div style="border: 2px solid var(--border-color); border-radius: 0.5rem; padding: 1rem;">
                    <h4 style="margin-bottom: 1rem;"><i class="fas fa-check-circle" style="color: var(--success-color);"></i> Trained Pathways</h4>
                    ${Object.entries(data.trainedPathways).map(([pathway, metrics]) => `
                        <div style="margin-bottom: 0.75rem; padding-bottom: 0.75rem; border-bottom: 1px solid var(--border-color);">
                            <strong>${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong>
                            <div style="font-size: 0.9rem; color: var(--text-light); margin-top: 0.25rem;">
                                ID: ${(metrics.identificationAccuracy * 100).toFixed(0)}% | 
                                Solving: ${(metrics.solvingAccuracy * 100).toFixed(0)}%
                            </div>
                        </div>
                    `).join('')}
                </div>
                
                <div style="border: 2px solid var(--border-color); border-radius: 0.5rem; padding: 1rem;">
                    <h4 style="margin-bottom: 1rem;"><i class="fas fa-minus-circle" style="color: var(--warning-color);"></i> Held-Back Pathways</h4>
                    ${Object.entries(data.heldBackPathways).map(([pathway, metrics]) => `
                        <div style="margin-bottom: 0.75rem; padding-bottom: 0.75rem; border-bottom: 1px solid var(--border-color);">
                            <strong>${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong>
                            <div style="font-size: 0.9rem; color: var(--text-light); margin-top: 0.25rem;">
                                ID: ${(metrics.identificationAccuracy * 100).toFixed(0)}% | 
                                Solving: ${(metrics.solvingAccuracy * 100).toFixed(0)}%
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    renderSuccessCriteria(criteria) {
        this.successCriteria.innerHTML = `
            <h3><i class="fas fa-trophy"></i> Success Criteria</h3>
            ${criteria.map(criterion => {
                const met = criterion.met;
                const metIcon = met ? '<i class="fas fa-check-circle success-met"></i>' : '<i class="fas fa-times-circle success-not-met"></i>';
                const metColor = met ? 'var(--success-color)' : 'var(--danger-color)';
                
                return `
                    <div class="success-criteria-item" style="border-color: ${metColor};">
                        <div>
                            <strong>${criterion.metric.replace(/([A-Z])/g, ' $1').trim()}</strong>
                            <div style="font-size: 0.9rem; color: var(--text-light); margin-top: 0.25rem;">
                                Value: ${(criterion.value * 100).toFixed(0)}% | Target: ${(criterion.target * 100).toFixed(0)}%
                            </div>
                        </div>
                        ${metIcon}
                    </div>
                `;
            }).join('')}
            
            <div style="margin-top: 1.5rem; text-align: center;">
                ${criteria.every(c => c.met) ? `
                    <div style="background: #ecfdf5; padding: 1.5rem; border-radius: 0.5rem; border: 2px solid var(--success-color);">
                        <i class="fas fa-medal" style="font-size: 2rem; color: gold;"></i>
                        <h3 style="margin-top: 0.5rem;">Congratulations!</h3>
                        <p>You have met all success criteria for the ATOM-SG Pilot!</p>
                    </div>
                ` : `
                    <p style="color: var(--text-light);">
                        <i class="fas fa-info-circle"></i> 
                        Keep practicing to meet all success criteria.
                    </p>
                `}
            </div>
        `;
    }

    showStatus(message, type) {
        this.uploadStatus.textContent = message;
        this.uploadStatus.className = `upload-status ${type}`;
    }

    async checkForExistingResults() {
        // Check if there's existing transfer data and show results
        try {
            const transferData = await api.getTransferAnalytics();
            if (transferData.rampUpMetrics) {
                this.showResults();
            }
        } catch (error) {
            // No existing transfer data
        }
    }
}

// Initialize transfer when DOM is ready
let transfer;
document.addEventListener('DOMContentLoaded', () => {
    transfer = new Transfer();
});
