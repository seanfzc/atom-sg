// Dashboard Module
// Handles progress dashboard functionality

class Dashboard {
    constructor() {
        this.milestonesList = document.getElementById('milestones-list');
        this.weeklyProgress = document.getElementById('weekly-progress');
        this.pathwayPerformance = document.getElementById('pathway-performance');
        
        this.init();
    }

    async init() {
        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'dashboard') {
                this.loadDashboardData();
            }
        });

        // Initial load
        this.loadDashboardData();
    }

    async loadDashboardData() {
        try {
            // Load milestones
            await this.loadMilestones();
            
            // Load weekly progress
            await this.loadWeeklyProgress();
            
            // Load pathway performance
            await this.loadPathwayPerformance();
            
        } catch (error) {
            console.error('Failed to load dashboard data:', error);
        }
    }

    async loadMilestones() {
        try {
            const data = await api.getMilestones();
            const milestones = data.milestones;
            
            this.milestonesList.innerHTML = milestones.map(milestone => {
                const progress = (milestone.problemsCompleted / milestone.problemsTotal) * 100;
                
                return `
                    <div class="milestone-item ${milestone.status}">
                        <div class="milestone-info">
                            <h4>Week ${milestone.week} - ${milestone.pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                            <div class="milestone-status">
                                ${milestone.status === 'completed' ? '✅ Completed' : `In Progress (${milestone.problemsCompleted}/${milestone.problemsTotal})`}
                            </div>
                        </div>
                        <div class="milestone-metrics">
                            <div>Avg Score: ${(milestone.averageScore * 100).toFixed(0)}%</div>
                            <div>Pathway Recognition: ${(milestone.pathwayIdentificationAccuracy * 100).toFixed(0)}%</div>
                        </div>
                        <div class="milestone-requirements">
                            ${milestone.week === 1 ? 'Complete Baseline Test' : milestone.week === 2 ? 'Practice 5 problems with 80% accuracy' : 'Master pathway identification'}
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${progress}%"></div>
                        </div>
                    </div>
                `;
            }).join('');
            
            // Update overall stats
            if (milestones.length > 0) {
                const totalCompleted = milestones.reduce((sum, m) => sum + m.problemsCompleted, 0);
                const avgScore = milestones.reduce((sum, m) => sum + m.averageScore, 0) / milestones.length;
                const avgIdAccuracy = milestones.reduce((sum, m) => sum + m.pathwayIdentificationAccuracy, 0) / milestones.length;
                const avgArticulation = milestones.reduce((sum, m) => sum + m.articulationLevel, 0) / milestones.length;
                
                document.getElementById('total-problems').textContent = totalCompleted;
                document.getElementById('avg-score').textContent = `${(avgScore * 100).toFixed(0)}%`;
                document.getElementById('id-accuracy').textContent = `${(avgIdAccuracy * 100).toFixed(0)}%`;
                document.getElementById('articulation-level').textContent = avgArticulation.toFixed(1);
            }
        } catch (error) {
            console.error('Failed to load milestones:', error);
            this.milestonesList.innerHTML = '<p class="text-center">Failed to load milestones. Please try again.</p>';
        }
    }

    async loadWeeklyProgress() {
        try {
            const data = await api.getProgressAnalytics();
            const weeklyProgress = data.weeklyProgress;
            
            this.weeklyProgress.innerHTML = weeklyProgress.map(week => {
                const statusColor = week.status === 'completed' ? 'green' : 'yellow';
                const statusIcon = week.status === 'completed' ? '✅' : '🔄';
                
                return `
                    <div class="weekly-item" style="border-left: 4px solid var(--${statusColor}-color); padding-left: 1rem; margin-bottom: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <strong>${statusIcon} Week ${week.week}</strong>
                            <span style="color: var(--text-light);">${week.status.toUpperCase()}</span>
                        </div>
                        ${week.averageScore ? `
                            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
                                <div>Score: ${(week.averageScore * 100).toFixed(0)}%</div>
                                <div>Pathway Recognition: ${(week.identificationAccuracy * 100).toFixed(0)}%</div>
                                <div>Explanation Quality: Level ${week.articulationLevel?.toFixed(1) || 'N/A'}</div>
                            </div>
                        ` : `
                            <div style="margin-top: 0.5rem; color: var(--text-light);">
                                ${week.baselineScore ? `Baseline Score: ${(week.baselineScore * 100).toFixed(0)}%` : 'Not started'}
                            </div>
                        `}
                    </div>
                `;
            }).join('');
        } catch (error) {
            console.error('Failed to load weekly progress:', error);
            this.weeklyProgress.innerHTML = '<p class="text-center">Failed to load weekly progress.</p>';
        }
    }

    async loadPathwayPerformance() {
        try {
            const baselineData = await api.getBaselineAnalytics();
            const scoresByPathway = baselineData.scoresByPathway;
            
            this.pathwayPerformance.innerHTML = Object.entries(scoresByPathway).map(([pathway, score]) => {
                const scorePercentage = (score * 100).toFixed(0);
                const strength = score >= 0.7 ? 'strong' : score >= 0.5 ? 'moderate' : 'weak';
                
                return `
                    <div class="gap-item ${strength}">
                        <div>
                            <strong>${pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: bold; color: var(--${strength === 'strong' ? 'success' : strength === 'moderate' ? 'warning' : 'danger'}-color);">
                            ${scorePercentage}%
                        </div>
                    </div>
                `;
            }).join('');
        } catch (error) {
            console.error('Failed to load pathway performance:', error);
            this.pathwayPerformance.innerHTML = '<p class="text-center">Failed to load pathway performance.</p>';
        }
    }
}

// Initialize dashboard when DOM is ready
let dashboard;
document.addEventListener('DOMContentLoaded', () => {
    dashboard = new Dashboard();
});
