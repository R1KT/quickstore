document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.getElementById('password');
    const toggleButton = document.getElementById('togglePassword');
    
    // Toggle the type attribute of the password field
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleButton.textContent = 'Hide';  // Change button text to 'Hide'
    } else {
        passwordField.type = 'password';
        toggleButton.textContent = 'Show';  // Change button text to 'Show'
    }
});
