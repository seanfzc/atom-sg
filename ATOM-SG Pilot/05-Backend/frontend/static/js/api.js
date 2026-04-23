// API Client Module
// Handles all backend API communication

// Production with same-origin (nginx reverse proxy)
// Safe against duplicate script loading
if (typeof API_BASE_URL === 'undefined') {
    var API_BASE_URL = '/api/v1';
}

// Note: For local testing, use http://localhost:50519/api/v1

class ApiClient {
    async request(url, options = {}) {
        try {
            const response = await fetch(`${API_BASE_URL}${url}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }

    // Problems
    async getProblems(filters = {}) {
        const params = new URLSearchParams();
        if (filters.track) params.append('track', filters.track);
        if (filters.pathway) params.append('pathway', filters.pathway);
        if (filters.week) params.append('week', filters.week);
        
        const queryString = params.toString();
        return this.request(`/problems${queryString ? `?${queryString}` : ''}`);
    }

    async getProblem(problemId) {
        return this.request(`/problems/${problemId}`);
    }

    async getProblemsPdf(week) {
        // Returns a URL for download
        return `/api/v1/problems/pdf?week=${week}`;
    }

    // Rubrics
    async getRubrics() {
        return this.request('/rubrics');
    }

    async getRubric(rubricId) {
        return this.request(`/rubrics/${rubricId}`);
    }

    // Renders
    async createRender(renderData) {
        return this.request('/renders', {
            method: 'POST',
            body: JSON.stringify(renderData)
        });
    }

    async getRender(renderId) {
        return this.request(`/renders/${renderId}`);
    }

    async listRenders(filters = {}) {
        const params = new URLSearchParams();
        if (filters.problemId) params.append('problemId', filters.problemId);
        if (filters.format) params.append('format', filters.format);
        
        const queryString = params.toString();
        return this.request(`/renders${queryString ? `?${queryString}` : ''}`);
    }

    // Scans
    async uploadScan(week, file) {
        const formData = new FormData();
        formData.append('week', week);
        formData.append('file', file);

        const response = await fetch(`${API_BASE_URL}/scans`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    async getScan(scanId) {
        return this.request(`/scans/${scanId}`);
    }

    // Practice Sessions
    async createPracticeSession(sessionData) {
        return this.request('/practice-sessions', {
            method: 'POST',
            body: JSON.stringify(sessionData)
        });
    }

    async getPracticeSession(sessionId) {
        return this.request(`/practice-sessions/${sessionId}`);
    }

    async submitPracticeSession(sessionId, submission) {
        return this.request(`/practice-sessions/${sessionId}/submit`, {
            method: 'POST',
            body: JSON.stringify(submission)
        });
    }

    // Individual Practice
    async submitPractice(submission) {
        return this.request('/practice', {
            method: 'POST',
            body: JSON.stringify(submission)
        });
    }

    // Pathway Radar
    async getPathwayRadarQuestions(date = null) {
        const queryString = date ? `?date=${date}` : '';
        return this.request(`/pathway-radar/questions${queryString}`);
    }

    async submitPathwayRadar(submission) {
        return this.request('/pathway-radar/submit', {
            method: 'POST',
            body: JSON.stringify(submission)
        });
    }

    // Milestones
    async getMilestones() {
        return this.request('/milestones');
    }

    async getMilestone(milestoneId) {
        return this.request(`/milestones/${milestoneId}`);
    }

    async updateMilestone(milestoneId, updateData) {
        return this.request(`/milestones/${milestoneId}`, {
            method: 'PATCH',
            body: JSON.stringify(updateData)
        });
    }

    // Analytics
    async getBaselineAnalytics() {
        return this.request('/analytics/baseline');
    }

    async getTransferAnalytics() {
        return this.request('/analytics/transfer');
    }

    async getProgressAnalytics() {
        return this.request('/analytics/progress');
    }

    // Advanced Analytics (Week 3+)
    async analyzeCollision(request) {
        return this.request('/collision', {
            method: 'POST',
            body: JSON.stringify(request)
        });
    }

    async getInterpretation(filters = {}) {
        const params = new URLSearchParams();
        if (filters.week) params.append('week', filters.week);
        if (filters.pathway) params.append('pathway', filters.pathway);
        if (filters.includeRedHerringAnalysis) params.append('includeRedHerringAnalysis', 'true');
        
        const queryString = params.toString();
        return this.request(`/interpretation${queryString ? `?${queryString}` : ''}`);
    }

    // Reflections
    async createReflection(reflection) {
        return this.request('/reflections', {
            method: 'POST',
            body: JSON.stringify(reflection)
        });
    }

    async getReflections(filters = {}) {
        const params = new URLSearchParams();
        if (filters.week) params.append('week', filters.week);
        if (filters.pathway) params.append('pathway', filters.pathway);
        
        const queryString = params.toString();
        return this.request(`/reflections${queryString ? `?${queryString}` : ''}`);
    }

    // System
    async getHealth() {
        return this.request('/system/health');
    }

    async getStats() {
        return this.request('/system/stats');
    }

    // P1-1: Gamification
    async getProfile(userId = 'anonymous') {
        const queryString = `?user_id=${userId}`;
        return this.request(`/profile/me${queryString}`);
    }

    async getAchievements() {
        return this.request('/achievements');
    }
}

// Global API client instance (safe against duplicate loading)
if (typeof api === 'undefined') {
    var api = new ApiClient();
}

// Ensure api is available on window for debugging
if (typeof window !== 'undefined') {
    window.api = api;
}
