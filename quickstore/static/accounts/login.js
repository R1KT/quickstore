const checkbox = document.getElementById('showPass');
    const passwordField = document.getElementById('password');

    checkbox.addEventListener('change', function() {
        // Toggle password visibility
        if (checkbox.checked) {
            passwordField.type = 'text';
        } else {
            passwordField.type = 'password';
        }
});
