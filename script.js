// Al-folio theme JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navToggler = document.querySelector('.navbar-toggler');
    const navMenu = document.querySelector('#navbarNav');
    
    if (navToggler && navMenu) {
        navToggler.addEventListener('click', function() {
            navToggler.classList.toggle('collapsed');
            navMenu.classList.toggle('show');
            
            // Animate hamburger icon
            const iconBars = navToggler.querySelectorAll('.icon-bar');
            if (navToggler.classList.contains('collapsed')) {
                iconBars[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                iconBars[1].style.opacity = '0';
                iconBars[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
            } else {
                iconBars[0].style.transform = 'rotate(0) translate(0, 0)';
                iconBars[1].style.opacity = '1';
                iconBars[2].style.transform = 'rotate(0) translate(0, 0)';
            }
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
                const headerHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (navMenu && navMenu.classList.contains('show')) {
                    navToggler.classList.add('collapsed');
                    navMenu.classList.remove('show');
                }
            }
        });
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (navMenu && navMenu.classList.contains('show')) {
            if (!navToggler.contains(e.target) && !navMenu.contains(e.target)) {
                navToggler.classList.add('collapsed');
                navMenu.classList.remove('show');
                
                // Reset hamburger icon
                const iconBars = navToggler.querySelectorAll('.icon-bar');
                iconBars[0].style.transform = 'rotate(0) translate(0, 0)';
                iconBars[1].style.opacity = '1';
                iconBars[2].style.transform = 'rotate(0) translate(0, 0)';
            }
        }
    });
    
    // Handle navbar scroll effect
    let lastScrollTop = 0;
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            navbar.style.transform = 'translateY(0)';
        }
        lastScrollTop = scrollTop;
    });
    
    // Add publication abstract toggle functionality
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('abstract')) {
            e.preventDefault();
            // This would toggle abstract visibility in a real implementation
            console.log('Abstract toggle clicked');
        }
    });
});