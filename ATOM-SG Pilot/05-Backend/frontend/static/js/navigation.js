// Navigation Module
// Handles page navigation and active state

class Navigation {
    constructor() {
        this.navLinks = document.querySelectorAll('.nav-links a');
        this.pages = document.querySelectorAll('.page');
        this.currentPage = 'dashboard';
        
        this.init();
    }

    isValidPage(page) {
        // Check if page element exists
        const element = document.getElementById(`page-${page}`);
        console.log(`isValidPage('${page}'): element`, element ? `found (id: ${element.id})` : 'NOT FOUND');
        return element !== null;
    }

    init() {
        console.log('Navigation init called');
        console.log('Nav links found:', this.navLinks.length);
        console.log('Pages found:', this.pages.length);
        this.pages.forEach((p, i) => {
            console.log(`Page ${i}: ${p.id}, active: ${p.classList.contains('active')}`);
        });
        
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const page = link.getAttribute('data-page');
                console.log('Nav link clicked:', page);
                this.navigateTo(page);
            });
        });

        // Handle browser back/forward
        window.addEventListener('popstate', (e) => {
            if (e.state && e.state.page) {
                console.log('Popstate:', e.state.page);
                this.showPage(e.state.page);
            }
        });

        // Load initial page - respect URL hash
        const hash = window.location.hash.substring(1);
        console.log('URL hash:', hash);
        const isValid = hash && this.isValidPage(hash);
        console.log(`isValidPage('${hash}'):`, isValid);
        const initialPage = isValid ? hash : 'dashboard';
        console.log('Initial page:', initialPage);
        console.log('Page element exists:', document.getElementById(`page-${initialPage}`) !== null);
        this.navigateTo(initialPage);
        
        // Safety check: after 300ms, verify correct page is active
        setTimeout(() => {
            const currentHash = window.location.hash.substring(1);
            const currentPage = this.currentPage;
            console.log('[NAV SAFETY] Current hash:', currentHash, 'currentPage:', currentPage);
            
            if (currentHash && currentHash !== currentPage) {
                console.warn('[NAV SAFETY] Hash/page mismatch! Hash:', currentHash, 'Page:', currentPage);
                console.log('[NAV SAFETY] Attempting to correct...');
                if (this.isValidPage(currentHash)) {
                    this.navigateTo(currentHash);
                    console.log('[NAV SAFETY] Corrected to:', currentHash);
                }
            }
        }, 300);
    }

    navigateTo(page) {
        if (page === this.currentPage) return;
        
        this.currentPage = page;
        this.showPage(page);
        
        // Update browser history
        window.history.pushState({ page }, '', `#${page}`);
        
        // Trigger page load event
        window.dispatchEvent(new CustomEvent('pageLoad', { detail: { page } }));
    }

    showPage(page) {
        console.log('Showing page:', page);
        
        // Update nav links
        this.navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-page') === page) {
                link.classList.add('active');
                console.log('Activated nav link for:', page);
            }
        });

        // Show/hide pages
        this.pages.forEach(p => {
            p.classList.remove('active');
            if (p.id === `page-${page}`) {
                p.classList.add('active');
                console.log('Activated page element:', p.id);
            }
        });

        // Scroll to top
        window.scrollTo(0, 0);
    }
}

// Initialize navigation when DOM is ready
let navigation;
document.addEventListener('DOMContentLoaded', () => {
    navigation = new Navigation();
});
