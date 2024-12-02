document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.navLink');
    const mainContent = document.getElementById('mainContent');

    // Define paths to external HTML files for each section
    const contentMap = {
        residentContent: 'screens/residents.html',
    };

    // Add click event listeners to each nav link
    navLinks.forEach(navLink => {
        navLink.addEventListener('click', async (event) => {
            event.preventDefault(); // Prevent default link behavior

            // Get the content key from the clicked link's data attribute
            const contentKey = navLink.getAttribute('data-content');

            if (contentMap[contentKey]) {
                try {
                    // Fetch the content from the corresponding HTML file
                    const response = await fetch(contentMap[contentKey]);

                    if (!response.ok) {
                        throw new Error('Failed to load content');
                    }

                    // Get the text content of the response
                    const content = await response.text();

                    // Replace the main content with the fetched content
                    mainContent.innerHTML = content;
                } catch (error) {
                    console.error('Error loading content:', error);
                    mainContent.innerHTML = '<p>Failed to load content. Please try again later.</p>';
                }
            }
        });
    });
});
