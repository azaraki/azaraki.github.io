// Academic Website JavaScript - Jan Peters Style

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.sidebar-nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get target section
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Highlight active section on scroll
    const sections = document.querySelectorAll('.content-section, .profile-header');
    const navItems = document.querySelectorAll('.sidebar-nav a');
    
    function highlightActiveSection() {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (window.pageYOffset >= (sectionTop - 100)) {
                currentSection = section.getAttribute('id');
            }
        });
        
        // Update navigation
        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href') === '#' + currentSection) {
                item.classList.add('active');
            }
        });
    }
    
    // Throttled scroll event
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(highlightActiveSection, 10);
    });
    
    // Set initial active state
    highlightActiveSection();
});

// Publications expand/collapse functionality
function toggleConferencePapers() {
    const btn = document.querySelector('.expand-btn');
    const showMoreItems = document.querySelectorAll('.show-more-conferences');
    
    if (btn.textContent.includes('Show All')) {
        // Show all conference papers - in a real implementation, you'd load the full list
        btn.textContent = 'Show Less Conference Papers';
        showMoreItems.forEach(item => item.style.display = 'flex');
    } else {
        btn.textContent = 'Show All Conference Papers (28 total)';
        showMoreItems.forEach(item => item.style.display = 'none');
    }
}

function toggleBookChapters() {
    const btns = document.querySelectorAll('.expand-btn');
    const btn = btns[1]; // Second button is for book chapters
    const showMoreItems = document.querySelectorAll('.show-more-chapters');
    
    if (btn.textContent.includes('Show All')) {
        btn.textContent = 'Show Less Book Chapters';
        showMoreItems.forEach(item => item.style.display = 'flex');
    } else {
        btn.textContent = 'Show All Book Chapters (10 total)';
        showMoreItems.forEach(item => item.style.display = 'none');
    }
}