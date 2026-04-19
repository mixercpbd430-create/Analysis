/**
 * Giáo Trình 18 Phương Pháp Phân Tích - Interactive Features
 */

document.addEventListener('DOMContentLoaded', function () {

    // ===================================
    // PARTICLES BACKGROUND
    // ===================================
    (function initParticles() {
        const container = document.getElementById('particles');
        if (!container) return;
        for (let i = 0; i < 30; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = Math.random() * 100 + '%';
            p.style.top = Math.random() * 100 + '%';
            p.style.animationDelay = (Math.random() * 5) + 's';
            p.style.animationDuration = (4 + Math.random() * 4) + 's';
            container.appendChild(p);
        }
    })();

    // ===================================
    // MOBILE SIDEBAR TOGGLE
    // ===================================
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function () {
            sidebar.classList.toggle('sidebar--open');
            if (sidebarOverlay) {
                sidebarOverlay.classList.toggle('sidebar-overlay--visible');
            }
        });

        if (sidebarOverlay) {
            sidebarOverlay.addEventListener('click', function () {
                sidebar.classList.remove('sidebar--open');
                sidebarOverlay.classList.remove('sidebar-overlay--visible');
            });
        }
    }

    // ===================================
    // PILLAR FILTER TABS
    // ===================================
    const pillarTabs = document.getElementById('pillarTabs');
    const methodsGrid = document.getElementById('methodsGrid');

    if (pillarTabs && methodsGrid) {
        const tabs = pillarTabs.querySelectorAll('.pillar-tab');
        const cards = methodsGrid.querySelectorAll('.chapter-card');

        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () {
                // Update active tab
                tabs.forEach(function (t) { t.classList.remove('pillar-tab--active'); });
                tab.classList.add('pillar-tab--active');

                const pillar = tab.getAttribute('data-pillar');

                // Filter cards
                cards.forEach(function (card, index) {
                    const cardPillar = card.getAttribute('data-pillar');
                    if (pillar === 'all' || cardPillar === pillar) {
                        card.style.display = '';
                        card.style.animationDelay = (index * 0.04) + 's';
                        card.style.animation = 'none';
                        card.offsetHeight; // trigger reflow
                        card.style.animation = '';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // ===================================
    // EXAMPLE CARD TOGGLE
    // ===================================
    // Open first 3 examples by default
    const exampleCards = document.querySelectorAll('.example-card');
    exampleCards.forEach(function (card, index) {
        if (index < 3) {
            card.classList.add('example-card--open');
        }
    });

    // ===================================
    // EXPAND ALL / COLLAPSE ALL EXAMPLES
    // ===================================
    const examplesSection = document.querySelector('.examples-grid');
    if (examplesSection && exampleCards.length > 0) {
        // Create control buttons
        const controlDiv = document.createElement('div');
        controlDiv.className = 'examples-controls';
        controlDiv.innerHTML = '<button class="examples-btn" id="expandAll">📖 Mở tất cả</button>' +
            '<button class="examples-btn" id="collapseAll">📕 Thu gọn tất cả</button>';
        controlDiv.style.cssText = 'display:flex;gap:10px;margin-bottom:16px;';

        // Style buttons
        const btnStyle = 'padding:8px 16px;border-radius:8px;border:1px solid rgba(255,255,255,0.1);' +
            'background:rgba(6,182,212,0.08);color:#94a3b8;cursor:pointer;font-size:0.85rem;' +
            'font-family:Inter,sans-serif;transition:all 0.2s;';

        examplesSection.parentElement.insertBefore(controlDiv, examplesSection);

        const expandAllBtn = document.getElementById('expandAll');
        const collapseAllBtn = document.getElementById('collapseAll');

        if (expandAllBtn) {
            expandAllBtn.style.cssText = btnStyle;
            expandAllBtn.addEventListener('click', function () {
                exampleCards.forEach(function (c) { c.classList.add('example-card--open'); });
            });
            expandAllBtn.addEventListener('mouseenter', function () {
                this.style.borderColor = 'rgba(6,182,212,0.3)';
                this.style.color = '#e2e8f0';
            });
            expandAllBtn.addEventListener('mouseleave', function () {
                this.style.borderColor = 'rgba(255,255,255,0.1)';
                this.style.color = '#94a3b8';
            });
        }
        if (collapseAllBtn) {
            collapseAllBtn.style.cssText = btnStyle;
            collapseAllBtn.addEventListener('click', function () {
                exampleCards.forEach(function (c) { c.classList.remove('example-card--open'); });
            });
            collapseAllBtn.addEventListener('mouseenter', function () {
                this.style.borderColor = 'rgba(6,182,212,0.3)';
                this.style.color = '#e2e8f0';
            });
            collapseAllBtn.addEventListener('mouseleave', function () {
                this.style.borderColor = 'rgba(255,255,255,0.1)';
                this.style.color = '#94a3b8';
            });
        }
    }

    // ===================================
    // ACTIVE SIDEBAR LINK SCROLL INTO VIEW
    // ===================================
    const activeLink = document.querySelector('.sidebar__link--active');
    if (activeLink && sidebar) {
        setTimeout(function () {
            activeLink.scrollIntoView({ block: 'center', behavior: 'smooth' });
        }, 300);
    }

    // ===================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ===================================
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===================================
    // CARD STAGGER ANIMATION
    // ===================================
    document.querySelectorAll('.chapter-card').forEach(function (card, index) {
        card.style.animationDelay = (index * 0.06) + 's';
    });

});
