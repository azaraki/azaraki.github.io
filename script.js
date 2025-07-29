// Academic Website JavaScript - Bilge Mutlu Style

document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navTrigger = document.querySelector('.nav-trigger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navTrigger && navMenu) {
        navTrigger.addEventListener('click', function() {
            navTrigger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const headerHeight = document.querySelector('.site-header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (navMenu && navMenu.classList.contains('active')) {
                    navTrigger.classList.remove('active');
                    navMenu.classList.remove('active');
                }
            }
        });
    });

    // Active navigation highlighting
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.page-link[href^="#"]');
    
    function highlightActiveSection() {
        const scrollPosition = window.scrollY + 150;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === `#${sectionId}`) {
                        item.classList.add('active');
                        item.style.color = '#0066cc';
                        item.style.fontWeight = '600';
                    } else {
                        item.style.color = '#333';
                        item.style.fontWeight = '400';
                    }
                });
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
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (navMenu && navMenu.classList.contains('active')) {
            if (!navTrigger.contains(e.target) && !navMenu.contains(e.target)) {
                navTrigger.classList.remove('active');
                navMenu.classList.remove('active');
            }
        }
    });
    
    // Handle profile photo error (if image doesn't exist)
    const profilePhoto = document.querySelector('.profile-photo');
    if (profilePhoto) {
        profilePhoto.addEventListener('error', function() {
            this.style.backgroundImage = 'none';
            this.style.backgroundColor = '#f0f0f0';
            this.style.border = '2px dashed #ccc';
            this.style.display = 'flex';
            this.style.alignItems = 'center';
            this.style.justifyContent = 'center';
            this.style.color = '#999';
            this.style.fontSize = '3rem';
            this.innerHTML = '👤';
        });
    }
});