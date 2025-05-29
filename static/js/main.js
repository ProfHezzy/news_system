document.addEventListener('DOMContentLoaded', function() {
    // Handle dropdown selections
    const categoryDropdown = document.getElementById('newsCategoryDropdown');
    if (categoryDropdown) {
        categoryDropdown.addEventListener('click', function(e) {
            e.preventDefault();
        });
    }

    // Show loading spinner when changing categories
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    dropdownItems.forEach(item => {
        item.addEventListener('click', function() {
            document.getElementById('newsContainer').innerHTML = `
                <div class="loading-spinner"></div>
                <p class="text-center mt-2">Loading news...</p>
            `;
        });
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 0.5rem 2rem 0 rgba(58, 59, 69, 0.3)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1)';
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});