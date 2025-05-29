document.addEventListener('DOMContentLoaded', function() {
    // --- Enhanced Navigation ---
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - document.querySelector('.navbar').offsetHeight,
                        behavior: 'smooth'
                    });

                    // Update active link in navigation
                    navLinks.forEach(navLink => navLink.classList.remove('active'));
                    this.classList.add('active');

                    // Collapse navbar on mobile after clicking a link
                    const navbarToggler = document.querySelector('.navbar-toggler');
                    const navbarCollapse = document.querySelector('#navbarNav');
                    if (navbarCollapse.classList.contains('show') && window.getComputedStyle(navbarToggler).display !== 'none') {
                        navbarToggler.click();
                    }
                }
            } else {
                // For non-hash links, remove active class from others
                navLinks.forEach(navLink => navLink.classList.remove('active'));
                this.classList.add('active');
            }
        });

        // Set active class for the current page (optional, if you have different pages)
        const currentPath = window.location.pathname;
        const navItemLink = link.getAttribute('href');
        if (navItemLink !== '#' && currentPath.endsWith(navItemLink)) {
            link.classList.add('active');
        }
    });

    // --- "Scroll to Top" Button ---
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollToTopBtn.classList.add('btn', 'btn-outline-primary', 'scroll-to-top');
    document.body.appendChild(scrollToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });

    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // --- Category Dropdown Enhancement ---
    const categoryDropdown = document.getElementById('newsCategoryDropdown');
    if (categoryDropdown) {
        const dropdownItems = categoryDropdown.nextElementSibling.querySelectorAll('.dropdown-item');
        dropdownItems.forEach(item => {
            item.addEventListener('click', function(e) {
                // No need for preventDefault as it's a regular link
                const selectedCategoryName = this.textContent.trim();
                categoryDropdown.querySelector('.fa-newspaper').nextSibling.textContent = ' ' + selectedCategoryName;
                // The filtering is handled by the URL parameter, no JS filtering needed here for this setup.
            });
        });

        // Highlight the current category in the dropdown on load
        const currentCategoryCode = getQueryParam('category');
        if (currentCategoryCode) {
            dropdownItems.forEach(item => {
                const href = new URL(item.href, window.location.origin);
                const categoryCode = href.searchParams.get('category');
                if (categoryCode === currentCategoryCode) {
                    const categoryName = item.textContent.trim();
                    categoryDropdown.querySelector('.fa-newspaper').nextSibling.textContent = ' ' + categoryName;
                }
            });
        } else {
            categoryDropdown.querySelector('.fa-newspaper').nextSibling.textContent = ' All Categories';
        }
    }

    function getQueryParam(name) {
        const urlSearchParams = new URLSearchParams(window.location.search);
        return urlSearchParams.get(name);
    }

    // --- Image Error Handling Enhancement ---
    const newsImages = document.querySelectorAll('#newsContainer .card-img-top');
    newsImages.forEach(img => {
        img.onerror = function() {
            this.onerror = null;
            this.src = "{% static 'images/news-placeholder.jpg' %}"; // Fallback image path
        };
    });

    // --- Modal Enhancements ---
    const newsModals = document.querySelectorAll('.modal');
    newsModals.forEach(modal => {
        modal.addEventListener('show.bs.modal', function (event) {
            const relatedTarget = event.relatedTarget; // Button that triggered the modal
            // You can add more dynamic content loading here if needed,
            // e.g., fetching more details based on the clicked article.
        });
    });
});