// Main Entry Point
// Initializes all modules and handles global events

// Initialize all modules
document.addEventListener('DOMContentLoaded', () => {
    console.log('ATOM-SG Pilot MVP - Frontend Initialized');
    console.log('API Base URL:', '/api/v1');
    
    // Check backend health
    checkBackendHealth();
    
    // Add global event listeners
    setupGlobalEventListeners();
});

// Check backend health
async function checkBackendHealth() {
    try {
        const health = await api.getHealth();
        console.log('Backend Status:', health.status);
        console.log('Backend Version:', health.version);
    } catch (error) {
        console.error('Backend health check failed:', error);
        console.warn('Backend may not be running. Start with: python main.py');
    }
}

// Setup global event listeners
function setupGlobalEventListeners() {
    // Handle browser back button
    window.addEventListener('popstate', (e) => {
        if (e.state && e.state.page) {
            // Navigation module will handle this
        }
    });
    
    // Handle keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + K: Quick search (placeholder)
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            console.log('Quick search - not implemented yet');
        }
        
        // Escape: Close modals (placeholder)
        if (e.key === 'Escape') {
            // Close any open modals
            console.log('Escape pressed - close modals');
        }
    });
    
    // Handle online/offline status
    window.addEventListener('online', () => {
        console.log('You are back online');
        showNotification('You are back online', 'success');
    });
    
    window.addEventListener('offline', () => {
        console.log('You are offline');
        showNotification('You are offline. Some features may not work.', 'warning');
    });
}

// Show notification (placeholder)
function showNotification(message, type = 'info') {
    console.log(`[${type.toUpperCase()}] ${message}`);
    
    // In production, create a toast notification element
    // For MVP, we'll just use console
}

// Utility functions
const Utils = {
    // Format date
    formatDate(date) {
        return new Date(date).toLocaleDateString('en-SG', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    // Format percentage
    formatPercentage(value) {
        return `${(value * 100).toFixed(0)}%`;
    },
    
    // Debounce function
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Throttle function
    throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },
    
    // Local storage helpers
    storage: {
        get(key) {
            try {
                const item = localStorage.getItem(key);
                return item ? JSON.parse(item) : null;
            } catch (e) {
                console.error('Failed to get from localStorage:', e);
                return null;
            }
        },
        set(key, value) {
            try {
                localStorage.setItem(key, JSON.stringify(value));
            } catch (e) {
                console.error('Failed to set to localStorage:', e);
            }
        },
        remove(key) {
            try {
                localStorage.removeItem(key);
            } catch (e) {
                console.error('Failed to remove from localStorage:', e);
            }
        },
        clear() {
            try {
                localStorage.clear();
            } catch (e) {
                console.error('Failed to clear localStorage:', e);
            }
        }
    }
};

// Export utils to global scope
window.Utils = Utils;

// Log loaded modules
setTimeout(() => {
    console.log('Loaded modules:', {
        navigation: typeof navigation !== 'undefined',
        dashboard: typeof dashboard !== 'undefined',
        baseline: typeof baseline !== 'undefined',
        practice: typeof practice !== 'undefined',
        pathwayRadarPage: typeof pathwayRadarPage !== 'undefined',
        transfer: typeof transfer !== 'undefined',
        reflections: typeof reflections !== 'undefined',
        canvasAnnotation: typeof canvasAnnotation !== 'undefined'
    });
}, 1000);

console.log('ATOM-SG Pilot MVP Frontend - Ready! 🚀');
