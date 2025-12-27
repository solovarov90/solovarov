// ========================================
// САЙТ-ВИЗИТКА ПЕТРА СОЛОВАРОВА
// JavaScript: Digital AI Background + Interactivity
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    initDigitalCanvas();
    initScrollReveal();
    initSmoothScroll();
    initProjectCards();
});

// ========================================
// DIGITAL GRID BACKGROUND (AI/Matrix style)
// OPTIMIZED VERSION - lighter for slow networks/devices
// ========================================
function initDigitalCanvas() {
    const canvas = document.getElementById('digitalCanvas');
    if (!canvas) return;

    // Performance check - skip heavy animation on slow devices
    const isSlowDevice = navigator.hardwareConcurrency <= 2 ||
        navigator.connection?.effectiveType === '2g' ||
        navigator.connection?.effectiveType === 'slow-2g' ||
        navigator.connection?.saveData === true;

    // Skip animation entirely on very slow devices
    if (isSlowDevice) {
        canvas.style.display = 'none';
        return;
    }

    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];
    let animationId;
    let lastFrameTime = 0;
    const targetFPS = 30; // Reduced from 60 for better performance
    const frameInterval = 1000 / targetFPS;

    // Resize canvas
    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        initParticles();
    }

    // Initialize particles - REDUCED count
    function initParticles() {
        particles = [];
        // Much fewer particles for better performance
        const isMobile = window.innerWidth < 768;
        const particleCount = isMobile ? 15 : Math.min(Math.floor((width * height) / 50000), 40);

        for (let i = 0; i < particleCount; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.2,
                vy: (Math.random() - 0.5) * 0.2,
                size: Math.random() * 1.5 + 0.5,
                color: getRandomColor()
            });
        }
    }

    function getRandomColor() {
        const colors = [
            'rgba(139, 92, 246, 0.5)',  // violet
            'rgba(6, 182, 212, 0.5)',   // cyan
            'rgba(236, 72, 153, 0.4)',  // pink
            'rgba(99, 102, 241, 0.4)'   // indigo
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    // Draw - optimized
    function draw(currentTime) {
        animationId = requestAnimationFrame(draw);

        // Throttle to target FPS
        const elapsed = currentTime - lastFrameTime;
        if (elapsed < frameInterval) return;
        lastFrameTime = currentTime - (elapsed % frameInterval);

        ctx.clearRect(0, 0, width, height);

        // Skip grid on mobile for performance
        const isMobile = window.innerWidth < 768;
        if (!isMobile) {
            // Draw grid lines (subtle) - less frequent
            ctx.strokeStyle = 'rgba(139, 92, 246, 0.02)';
            ctx.lineWidth = 1;

            const gridSize = 80; // Larger grid = fewer lines
            for (let x = 0; x < width; x += gridSize) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, height);
                ctx.stroke();
            }
            for (let y = 0; y < height; y += gridSize) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(width, y);
                ctx.stroke();
            }
        }

        // Update and draw particles
        particles.forEach((p, i) => {
            // Update position
            p.x += p.vx;
            p.y += p.vy;

            // Bounce off edges
            if (p.x < 0 || p.x > width) p.vx *= -1;
            if (p.y < 0 || p.y > height) p.vy *= -1;

            // Draw particle
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.fill();

            // Draw connections - only check nearby particles (optimization)
            const connectionDistance = isMobile ? 80 : 120;
            for (let j = i + 1; j < particles.length; j++) {
                const p2 = particles[j];
                const dx = p.x - p2.x;
                const dy = p.y - p2.y;

                // Quick distance check without sqrt
                const distSq = dx * dx + dy * dy;
                const maxDistSq = connectionDistance * connectionDistance;

                if (distSq < maxDistSq) {
                    const dist = Math.sqrt(distSq);
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(139, 92, 246, ${0.08 * (1 - dist / connectionDistance)})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        });
    }

    // Initialize with delay to not block initial render
    requestIdleCallback ? requestIdleCallback(() => {
        resize();
        draw(0);
    }) : setTimeout(() => {
        resize();
        draw(0);
    }, 100);

    // Handle resize - debounced
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(resize, 300);
    });

    // Pause animation when tab is not visible
    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            cancelAnimationFrame(animationId);
        } else {
            draw(0);
        }
    });
}

// ========================================
// SCROLL REVEAL ANIMATION
// ========================================
function initScrollReveal() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add staggered delay for cards
                const cardIndex = Array.from(document.querySelectorAll('.project-card')).indexOf(entry.target);
                const delay = cardIndex * 150;

                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay);

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe project cards
    const cards = document.querySelectorAll('.project-card');
    cards.forEach(card => observer.observe(card));
}

// ========================================
// PROJECT CARDS EXPAND/COLLAPSE
// ========================================
function initProjectCards() {
    const expandButtons = document.querySelectorAll('.project-expand-btn');

    expandButtons.forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.project-card');
            const isExpanded = card.classList.contains('expanded');

            // Toggle state
            card.classList.toggle('expanded');
            button.setAttribute('aria-expanded', !isExpanded);

            // Update button text
            const span = button.querySelector('span');
            span.textContent = isExpanded ? 'Подробнее' : 'Свернуть';

            // Smooth scroll to card if expanding
            if (!isExpanded) {
                setTimeout(() => {
                    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        });
    });
}

// ========================================
// SMOOTH SCROLL
// ========================================
function initSmoothScroll() {
    const scrollLinks = document.querySelectorAll('a[href^="#"]');

    scrollLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ========================================
// CURSOR GLOW EFFECT (Optional - for desktop)
// ========================================
function initCursorGlow() {
    // Only on desktop with hover capability
    if (!window.matchMedia('(hover: hover)').matches) return;

    const glow = document.createElement('div');
    glow.style.cssText = `
        position: fixed;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.08) 0%, transparent 70%);
        pointer-events: none;
        z-index: -1;
        transform: translate(-50%, -50%);
        transition: opacity 0.3s ease;
        opacity: 0;
    `;
    document.body.appendChild(glow);

    let lastX = 0, lastY = 0;
    let rafId;

    document.addEventListener('mousemove', (e) => {
        lastX = e.clientX;
        lastY = e.clientY;
        glow.style.opacity = '1';

        if (!rafId) {
            rafId = requestAnimationFrame(() => {
                glow.style.left = lastX + 'px';
                glow.style.top = lastY + 'px';
                rafId = null;
            });
        }
    });

    document.addEventListener('mouseleave', () => {
        glow.style.opacity = '0';
    });
}

// Enable cursor glow effect
initCursorGlow();
