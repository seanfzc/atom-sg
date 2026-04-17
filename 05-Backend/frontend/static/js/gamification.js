// Gamification Module
// Handles streak tracking and achievement system (P1-1)

class Gamification {
    constructor() {
        this.achievements = {};
        this.streakDays = document.getElementById('streak-days');
        this.totalDays = document.getElementById('total-days');
        this.achievementsList = document.getElementById('achievements-list');
        this.noAchievements = document.getElementById('no-achievements');
        this.achievementModal = document.getElementById('achievement-modal');
        this.achievementTitle = document.getElementById('achievement-title');
        this.achievementDescription = document.getElementById('achievement-description');
        this.achievementDismiss = document.getElementById('achievement-dismiss');
        
        this.init();
    }

    async init() {
        // Load achievements definitions
        await this.loadAchievementsDefinitions();
        
        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'dashboard') {
                this.loadGamification();
            }
        });
        
        // Listen for practice submission
        window.addEventListener('practiceSubmitted', (e) => {
            this.handlePracticeSubmission(e.detail);
        });
        
        // Set up modal dismiss button
        this.achievementDismiss.addEventListener('click', () => {
            this.hideAchievementModal();
        });
        
        // Initial load
        this.loadGamification();
    }

    async loadAchievementsDefinitions() {
        try {
            const data = await api.getAchievements();
            this.achievements = data.achievements;
        } catch (error) {
            console.error('Failed to load achievements definitions:', error);
        }
    }

    async loadGamification() {
        try {
            const profile = await api.getProfile();
            
            if (profile.success) {
                const streak = profile.data.streak || {};
                
                // Update streak display
                if (this.streakDays) {
                    this.streakDays.textContent = streak.current || 0;
                }
                if (this.totalDays) {
                    this.totalDays.textContent = streak.totalDays || 0;
                }
                
                // Update achievements display
                this.updateAchievementsDisplay(streak.achievements || []);
            }
        } catch (error) {
            console.error('Failed to load gamification data:', error);
        }
    }

    updateAchievementsDisplay(achievementKeys) {
        if (!this.achievementsList) return;
        
        if (achievementKeys.length === 0) {
            // Show "no achievements" message
            this.achievementsList.innerHTML = '';
            if (this.noAchievements) {
                this.noAchievements.classList.remove('hidden');
            }
        } else {
            // Show achievement badges
            if (this.noAchievements) {
                this.noAchievements.classList.add('hidden');
            }
            
            this.achievementsList.innerHTML = achievementKeys.map(key => {
                const achievement = this.achievements[key];
                if (!achievement) return '';
                
                return `
                    <div class="achievement-badge" title="${achievement.description}">
                        <div class="achievement-icon">${achievement.icon}</div>
                        <div class="achievement-name">${achievement.name}</div>
                    </div>
                `;
            }).join('');
        }
    }

    handlePracticeSubmission(data) {
        // Check for newly unlocked achievements
        if (data.streak && data.streak.newlyUnlocked) {
            const newlyUnlocked = data.streak.newlyUnlocked;
            
            if (newlyUnlocked.length > 0) {
                // Show achievement notification for each new achievement
                newlyUnlocked.forEach((key, index) => {
                    setTimeout(() => {
                        const achievement = this.achievements[key];
                        if (achievement) {
                            this.showAchievementNotification(achievement);
                        }
                    }, index * 3500); // Stagger notifications by 3.5 seconds
                });
            }
        }
        
        // Reload gamification data
        this.loadGamification();
    }

    showAchievementNotification(achievement) {
        if (!this.achievementModal || !this.achievementTitle || !this.achievementDescription) return;
        
        this.achievementTitle.textContent = achievement.name;
        this.achievementDescription.textContent = achievement.description;
        this.achievementModal.classList.remove('hidden');
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            this.hideAchievementModal();
        }, 5000);
    }

    hideAchievementModal() {
        if (this.achievementModal) {
            this.achievementModal.classList.add('hidden');
        }
    }
}

// Initialize gamification when DOM is ready
let gamification;
document.addEventListener('DOMContentLoaded', () => {
    gamification = new Gamification();
});
