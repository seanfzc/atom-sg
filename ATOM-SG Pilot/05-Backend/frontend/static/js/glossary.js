/**
 * Glossary of mathematical and system terminology for 11-year-old students.
 */

const GLOSSARY_TERMS = {
    // Pathway Types
    "before-after-change": {
        term: "Before-After Change",
        definition: "Problems where something changes from an original state. You need to track what happens step-by-step.",
        example: "A shop had 120 pens. They sold 3/4 of them, then sold 1/3 of the remainder. How many are left?",
        synonyms: ["change", "transformation", "before-after"]
    },
    "part-whole-comparison": {
        term: "Part-Whole with Comparison",
        definition: "Problems where you compare parts to a whole. You often multiply by a fraction.",
        example: "Ali has $120. Ben has 4/5 as much as Ali. How much does Ben have?",
        synonyms: ["part-whole", "fraction", "comparison"]
    },
    "data-interpretation-red-herring": {
        term: "Data Problems with Tricky Details",
        definition: "Problems with charts or tables that have extra information to distract you. You need to ignore the tricky details.",
        example: "A bar chart shows sales for 4 months. They tell you January sales. You need to find December sales, ignoring other months.",
        synonyms: ["red herring", "data interpretation", "tricky"]
    },
    
    // System Terms
    "equation-shadow": {
        term: "Equation Shadow",
        definition: "A simple description of how you would solve a problem, without actually calculating the answer.",
        example: "First, find the total by adding all quantities together. Then, subtract the amount sold to find the remainder.",
        synonyms: ["articulation", "problem structure", "approach"]
    },
    "articulation": {
        term: "Articulation",
        definition: "Explaining your thinking clearly. It helps you recognize problem patterns and remember them.",
        example: "When you say 'This is a Before-After Change problem because there are two stages', that's articulation.",
        synonyms: ["explanation", "thinking process", "recognition"]
    },
    "pathway-type": {
        term: "Pathway Type",
        definition: "The category or pattern of a math problem. Each type has its own way to solve it.",
        example: "Before-After Change, Part-Whole, Data Interpretation are all pathway types.",
        synonyms: ["problem type", "pattern", "category"]
    },
    "red-herring": {
        term: "Red Herring",
        definition: "Extra information in a problem that tries to distract you. You should ignore it to find the right answer.",
        example: "A problem tells you about 5 different months but only asks about 2 of them. The other 3 months are red herrings.",
        synonyms: ["distraction", "tricky detail", "extra information"]
    },
    
    // Math Terms
    "fraction": {
        term: "Fraction",
        definition: "A part of a whole. It has a top number (numerator) and bottom number (denominator).",
        example: "3/4 means 3 parts out of 4 equal parts.",
        synonyms: ["part", "ratio", "proportion"]
    },
    "remainder": {
        term: "Remainder",
        definition: "What's left over after something is removed or used.",
        example: "If you have 10 apples and eat 3, the remainder is 7.",
        synonyms: ["leftover", "remaining", "what's left"]
    },
    "proportional": {
        term: "Proportional",
        definition: "When two things change together in a fixed ratio. If one doubles, the other also doubles.",
        example: "If a diagram shows a triangle with sides 3cm and 5cm, and it's proportional to the real triangle, the real triangle also has sides in ratio 3:5.",
        synonyms: ["to scale", "in proportion", "same ratio"]
    }
};

/**
 * Search glossary for a term.
 */
function searchGlossary(searchTerm) {
    const term = searchTerm.toLowerCase().trim();
    
    // Direct match
    if (GLOSSARY_TERMS[term]) {
        return GLOSSARY_TERMS[term];
    }
    
    // Synonym match
    for (const [key, value] of Object.entries(GLOSSARY_TERMS)) {
        if (value.synonyms.some(s => s.toLowerCase() === term)) {
            return value;
        }
    }
    
    return null;
}

/**
 * Get all glossary terms for display.
 */
function getAllGlossaryTerms() {
    return Object.values(GLOSSARY_TERMS);
}

/**
 * Open glossary modal.
 */
function openGlossary() {
    const modal = document.getElementById('glossary-modal');
    if (modal) {
        modal.classList.remove('hidden');
        loadGlossaryContent();
        
        const searchInput = document.getElementById('glossary-search-input');
        if (searchInput) {
            searchInput.focus();
        }
    }
}

/**
 * Close glossary modal.
 */
function closeGlossary() {
    const modal = document.getElementById('glossary-modal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

/**
 * Load glossary content into modal.
 */
function loadGlossaryContent(searchTerm = '') {
    const content = document.getElementById('glossary-content');
    if (!content) return;
    
    const terms = getAllGlossaryTerms();
    
    const filteredTerms = searchTerm
        ? terms.filter(term => {
            const searchLower = searchTerm.toLowerCase();
            return term.term.toLowerCase().includes(searchLower) ||
                   term.definition.toLowerCase().includes(searchLower) ||
                   term.synonyms.some(s => s.toLowerCase().includes(searchLower));
        })
        : terms;
    
    if (filteredTerms.length === 0) {
        content.innerHTML = `
            <div class="glossary-no-results">
                <p>No terms found for "${searchTerm}". Try a different search term.</p>
            </div>
        `;
        return;
    }
    
    content.innerHTML = filteredTerms.map(term => `
        <div class="glossary-entry">
            <div class="glossary-term">${term.term}</div>
            <div class="glossary-definition">${term.definition}</div>
            <div class="glossary-example"><strong>Example:</strong> ${term.example}</div>
            <div class="glossary-synonyms">
                <strong>Also called:</strong> ${term.synonyms.join(', ')}
            </div>
        </div>
    `).join('');
}

/**
 * Initialize glossary modal event listeners.
 */
function initializeGlossaryModal() {
    const closeBtn = document.getElementById('close-glossary');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeGlossary);
    }
    
    const searchInput = document.getElementById('glossary-search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            loadGlossaryContent(e.target.value);
        });
    }
    
    const modal = document.getElementById('glossary-modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeGlossary();
            }
        });
    }
    
    // Glossary button in help modal
    const glossaryBtn = document.getElementById('glossary-btn');
    if (glossaryBtn) {
        glossaryBtn.addEventListener('click', (e) => {
            e.preventDefault();
            openGlossary();
        });
    }
    
    // Floating glossary button
    const floatingGlossaryBtn = document.getElementById('glossaryButton');
    if (floatingGlossaryBtn) {
        floatingGlossaryBtn.addEventListener('click', (e) => {
            e.preventDefault();
            openGlossary();
        });
    }
}

// Make functions available globally
window.openGlossary = openGlossary;
window.closeGlossary = closeGlossary;
window.loadGlossaryContent = loadGlossaryContent;

document.addEventListener('DOMContentLoaded', initializeGlossaryModal);

// Add keyboard shortcut (Ctrl+B)
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'b') {
        e.preventDefault();
        openGlossary();
    }
});
