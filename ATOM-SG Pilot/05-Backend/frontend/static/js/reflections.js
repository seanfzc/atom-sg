// Reflections Module
// Handles digital reflection sheets

class Reflections {
    constructor() {
        this.reflectionForm = document.getElementById('reflection-form');
        this.confidenceSlider = document.getElementById('reflection-confidence');
        this.confidenceValue = document.getElementById('confidence-value');
        this.reflectionsList = document.getElementById('reflections-list');
        
        this.init();
    }

    init() {
        // Confidence slider
        this.confidenceSlider.addEventListener('input', () => {
            this.confidenceValue.textContent = this.confidenceSlider.value;
        });

        // Form submission
        this.reflectionForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.submitReflection();
        });

        // Listen for page load
        window.addEventListener('pageLoad', (e) => {
            if (e.detail.page === 'reflections') {
                this.loadReflections();
            }
        });
    }

    async submitReflection() {
        // Gather form data
        const week = parseInt(document.getElementById('reflection-week').value);
        const pathway = document.getElementById('reflection-pathway').value;
        const reflectionText = document.getElementById('reflection-text').value.trim();
        const confidence = parseInt(this.confidenceSlider.value);
        
        // Get struggles
        const struggles = [];
        document.querySelectorAll('.checkbox-group input[type="checkbox"]:checked').forEach(checkbox => {
            if (checkbox.name === 'struggles') {
                struggles.push(checkbox.value);
            }
        });
        
        // Get improvements
        const improvements = [];
        document.querySelectorAll('.checkbox-group input[type="checkbox"]:checked').forEach(checkbox => {
            if (checkbox.name === 'improvements') {
                improvements.push(checkbox.value);
            }
        });

        try {
            const reflectionData = await api.createReflection({
                week: week,
                pathway: pathway,
                reflection: reflectionText,
                confidence: confidence,
                struggles: struggles,
                improvements: improvements
            });

            // Show success message
            alert('Reflection submitted successfully!');
            
            // Reset form
            this.reflectionForm.reset();
            this.confidenceValue.textContent = '3';
            
            // Reload reflections list
            await this.loadReflections();
            
        } catch (error) {
            console.error('Failed to submit reflection:', error);
            alert('Failed to submit reflection. Please try again.');
        }
    }

    async loadReflections() {
        try {
            const data = await api.getReflections();
            const reflections = data.reflections;
            
            if (reflections.length === 0) {
                this.reflectionsList.innerHTML = `
                    <p style="text-align: center; color: var(--text-light);">
                        <i class="fas fa-journal-whills" style="font-size: 2rem; margin-bottom: 1rem;"></i>
                        <p>No reflections yet. Submit your first reflection above!</p>
                    </p>
                `;
                return;
            }
            
            this.reflectionsList.innerHTML = reflections.map(reflection => {
                const stars = '⭐'.repeat(Math.round(reflection.confidence));
                const date = new Date(reflection.createdAt).toLocaleDateString();
                
                return `
                    <div class="reflection-item">
                        <h4>Week ${reflection.week} - ${reflection.pathway.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                        <div class="reflection-meta">
                            <span><i class="fas fa-calendar"></i> ${date}</span>
                            <span><i class="fas fa-star"></i> Confidence: ${reflection.confidence}/5 ${stars}</span>
                        </div>
                        <p style="margin-top: 0.5rem;">${reflection.reflection}</p>
                        ${reflection.struggles && reflection.struggles.length > 0 ? `
                            <div style="margin-top: 0.5rem;">
                                <strong>Struggles:</strong> ${reflection.struggles.join(', ')}
                            </div>
                        ` : ''}
                        ${reflection.improvements && reflection.improvements.length > 0 ? `
                            <div style="margin-top: 0.5rem;">
                                <strong>Improvements:</strong> ${reflection.improvements.join(', ')}
                            </div>
                        ` : ''}
                    </div>
                `;
            }).join('');
            
        } catch (error) {
            console.error('Failed to load reflections:', error);
            this.reflectionsList.innerHTML = '<p class="text-center">Failed to load reflections.</p>';
        }
    }
}

// Initialize reflections when DOM is ready
let reflections;
document.addEventListener('DOMContentLoaded', () => {
    reflections = new Reflections();
});
