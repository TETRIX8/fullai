// Smooth scrolling for navigation links
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Copy to clipboard functionality
function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        const text = element.textContent;
        navigator.clipboard.writeText(text).then(() => {
            // Show success message
            const button = element.parentElement.querySelector('.copy-btn');
            if (button) {
                const originalText = button.textContent;
                button.textContent = 'Скопировано!';
                button.style.background = '#10b981';
                
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.background = '';
                }, 2000);
            }
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
    }
}

// Animate numbers in stats section
function animateNumbers() {
    const numbers = document.querySelectorAll('[data-target]');
    
    numbers.forEach(number => {
        const target = parseInt(number.getAttribute('data-target'));
        const increment = target / 100;
        let current = 0;
        
        const updateNumber = () => {
            if (current < target) {
                current += increment;
                number.textContent = Math.ceil(current);
                requestAnimationFrame(updateNumber);
            } else {
                number.textContent = target;
            }
        };
        
        updateNumber();
    });
}

// Intersection Observer for animations
function setupIntersectionObserver() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all model items and example cards
    document.querySelectorAll('.model-item, .example-card, .api-endpoint').forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(item);
    });
}

// Navbar scroll effect
function setupNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
        
        lastScrollTop = scrollTop;
    });
}

// Search functionality for models
function setupModelSearch() {
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Поиск моделей...';
    searchInput.className = 'model-search';
    searchInput.style.cssText = `
        width: 100%;
        max-width: 400px;
        padding: 12px 16px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        font-size: 1rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    `;
    
    const modelsSection = document.querySelector('.models-section .section-header');
    if (modelsSection) {
        modelsSection.appendChild(searchInput);
        
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase();
            const modelItems = document.querySelectorAll('.model-item');
            
            modelItems.forEach(item => {
                const title = item.querySelector('h4').textContent.toLowerCase();
                const description = item.querySelector('.model-description').textContent.toLowerCase();
                const features = Array.from(item.querySelectorAll('.feature-tag'))
                    .map(tag => tag.textContent.toLowerCase())
                    .join(' ');
                
                const matches = title.includes(searchTerm) || 
                              description.includes(searchTerm) || 
                              features.includes(searchTerm);
                
                item.style.display = matches ? 'block' : 'none';
                item.style.opacity = matches ? '1' : '0';
                item.style.transform = matches ? 'translateY(0)' : 'translateY(20px)';
            });
        });
    }
}

// Syntax highlighting for code blocks
function setupSyntaxHighlighting() {
    // Prism.js is already loaded via CDN
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }
}

// Mobile menu toggle
function setupMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    const menuToggle = document.createElement('button');
    menuToggle.className = 'mobile-menu-toggle';
    menuToggle.innerHTML = '☰';
    menuToggle.style.cssText = `
        display: none;
        background: none;
        border: none;
        color: #333;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem;
    `;
    
    const navContent = document.querySelector('.nav-content');
    navContent.appendChild(menuToggle);
    
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navContent.contains(e.target)) {
            navLinks.classList.remove('active');
        }
    });
}

// Initialize all functionality
document.addEventListener('DOMContentLoaded', function() {
    setupIntersectionObserver();
    setupNavbarScroll();
    setupModelSearch();
    setupSyntaxHighlighting();
    setupMobileMenu();
    
    // Add mobile menu styles
    const style = document.createElement('style');
    style.textContent = `
        @media (max-width: 768px) {
            .nav-links {
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: rgba(255, 255, 255, 0.98);
                backdrop-filter: blur(10px);
                flex-direction: column;
                padding: 1rem;
                gap: 1rem;
                border-top: 1px solid rgba(0, 0, 0, 0.1);
                transform: translateY(-100%);
                opacity: 0;
                transition: all 0.3s ease;
                pointer-events: none;
            }
            
            .nav-links.active {
                transform: translateY(0);
                opacity: 1;
                pointer-events: all;
            }
            
            .mobile-menu-toggle {
                display: block !important;
            }
        }
    `;
    document.head.appendChild(style);
});

// Add loading animation for model cards
function addLoadingAnimation() {
    const modelCards = document.querySelectorAll('.model-card');
    modelCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
        card.style.animation = 'fadeInUp 0.6s ease forwards';
    });
}

// Add CSS animation
const animationStyle = document.createElement('style');
animationStyle.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(animationStyle);

// Call loading animation when page loads
window.addEventListener('load', addLoadingAnimation);

