// Pathway Radar Page Module
// Handles standalone pathway radar page

class PathwayRadarPage {
    constructor() {
        this.radarChart = document.getElementById('radar-chart');
        this.radarHistory = document.getElementById('radar-history');
        
        this.init();
    }

    init() {
        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'pathway-radar') {
                this.loadPathwayRadar();
                this.attachStartButtonListener();
            }
        });
    }

    attachStartButtonListener() {
        // Attach listener to Start Daily Practice button after it's rendered
        setTimeout(() => {
            const btn = document.getElementById('start-daily-practice-btn');
            if (btn) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    console.log('Start Daily Practice clicked');
                    // Use hash-based navigation which always works
                    window.location.hash = 'practice';
                    // Also try navigation module if available
                    if (window.navigation && window.navigation.navigateTo) {
                        try {
                            window.navigation.navigateTo('practice');
                        } catch (err) {
                            console.log('Navigation module failed, hash already set');
                        }
                    }
                });
            } else {
                console.warn('Start Daily Practice button not found');
            }
        }, 100);
    }

    async loadPathwayRadar() {
        try {
            // Load today's questions
            const data = await api.getPathwayRadarQuestions();
            this.renderRadarChart(data.questions);
            
            // Load history (placeholder - would need backend endpoint)
            this.renderRadarHistory();
            
        } catch (error) {
            console.error('Failed to load pathway radar:', error);
            this.radarChart.innerHTML = '<p class="text-center">Failed to load pathway radar data.</p>';
        }
    }

    renderRadarChart(questions) {
        // Group pathways by frequency
        const pathwayCounts = {};
        questions.forEach(q => {
            q.pathways.forEach(p => {
                pathwayCounts[p] = (pathwayCounts[p] || 0) + 1;
            });
        });

        // Create visual radar chart representation
        const pathways = Object.keys(pathwayCounts);
        const maxCount = Math.max(...Object.values(pathwayCounts));
        
        this.radarChart.innerHTML = `
            <div style="text-align: center; margin-bottom: 2rem;">
                <h3>Today's Warm-up Questions</h3>
                <p style="color: var(--text-light);">10 mixed pathway identification questions</p>
            </div>
            
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                ${pathways.map(pathway => {
                    const count = pathwayCounts[pathway];
                    const percentage = (count / maxCount) * 100;
                    return `
                        <div style="text-align: center; width: 200px;">
                            <div style="margin-bottom: 0.5rem; font-weight: 500;">
                                ${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                            </div>
                            <div style="height: ${percentage}%; background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); border-radius: 8px 8px 0 0; min-height: 20px;">
                            </div>
                            <div style="color: var(--text-light); margin-top: 0.5rem;">${count} questions</div>
                        </div>
                    `;
                }).join('')}
            </div>
            
            <div style="text-align: center; margin-top: 2rem; padding: 1rem;">
                <button id="start-daily-practice-btn" class="btn btn-primary btn-lg" style="font-size: 1.1rem; padding: 0.75rem 1.5rem;">
                    <i class="fas fa-dumbbell"></i> Start Daily Practice
                </button>
            </div>
        `;
    }

    renderRadarHistory() {
        // Placeholder for radar history
        // In production, this would load historical radar results from the backend
        this.radarHistory.innerHTML = `
            <p style="color: var(--text-light); text-align: center;">
                <i class="fas fa-info-circle"></i> 
                Historical pathway radar data will appear here as you complete more warm-ups.
            </p>
        `;
    }
}

// Initialize pathway radar page when DOM is ready
let pathwayRadarPage;
document.addEventListener('DOMContentLoaded', () => {
    pathwayRadarPage = new PathwayRadarPage();
});
