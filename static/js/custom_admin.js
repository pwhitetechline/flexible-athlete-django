document.addEventListener("DOMContentLoaded", function() {
    // Example: Add a greeting to the admin dashboard
    const header = document.getElementById('header');
    if (header) {
        const greeting = document.createElement('div');
        greeting.textContent = 'Welcome to the Custom Admin Interface!';
        greeting.style.color = 'white';
        greeting.style.padding = '10px';
        header.appendChild(greeting);
    }

    // More custom JavaScript functionalities can be added here
    // Example: Hide certain fields based on selection
    const statusField = document.querySelector('#id_status');
    const publishDateField = document.querySelector('.field-published_date');
    if (statusField && publishDateField) {
        function togglePublishDateVisibility() {
            if (statusField.value === 'draft') {
                publishDateField.style.display = 'none';
            } else {
                publishDateField.style.display = 'block';
            }
        }
        togglePublishDateVisibility();
        statusField.addEventListener('change', togglePublishDateVisibility);
    }
});
