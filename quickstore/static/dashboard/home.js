document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.navLink');
    const mainContent = document.getElementById('mainContent');
    let currentStyleLink = null; // To keep track of the currently loaded CSS

    // Define paths to external HTML files for each section
    const contentMap = {
        residentContent: {
            html : '/static/dashboard/screens/residents/residents.html',
            css : '/static/dashboard/screens/residents/residents.css',
        },
        servicesContent: {
            html : '/static/dashboard/screens/services/services.html',
            css : '/static/dashboard/screens/services/services.css',
        },
        guestLogContent: {
            html : '/static/dashboard/screens/guestLog/guestLog.html',
            css : '/static/dashboard/screens/guestLog/guestLog.css',
        },
    };

    // Add click event listeners to each nav link
    function loadCSS(url) {
        if (currentStyleLink) {
            // Remove the current style link if it exists
            currentStyleLink.parentNode.removeChild(currentStyleLink);
        }
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = url;
        document.head.appendChild(link);
        currentStyleLink = link; // Update the reference to the current style
    }

    // Add click event listeners to each nav link
    navLinks.forEach(navLink => {
        navLink.addEventListener('click', async (event) => {
            event.preventDefault(); // Prevent default link behavior

            // Get the content key from the clicked link's data attribute
            const contentKey = navLink.getAttribute('data-content');

            if (contentMap[contentKey]) {
                try {
                    // Fetch the content from the corresponding HTML file
                    const response = await fetch(contentMap[contentKey].html);

                    if (!response.ok) {
                        throw new Error('Failed to load content');
                    }

                    // Get the text content of the response
                    const content = await response.text();

                    // Replace the main content with the fetched content
                    mainContent.innerHTML = content;

                    // Load the corresponding CSS file
                    loadCSS(contentMap[contentKey].css);

                } catch (error) {
                    console.error('Error loading content:', error);
                    mainContent.innerHTML = '<p>Failed to load content. Please try again later.</p>';
                }
            }
        });
    });
});

    