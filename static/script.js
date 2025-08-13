  const form = document.getElementById('signup-form');
    const togglePassword = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password');
     const confirmPassword = document.getElementById('confirm-password');
    const errorMessage = document.getElementById('error-message');

    togglePassword.addEventListener('click', function () {
      const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordInput.setAttribute('type', type);

      this.classList.toggle('bx-show');
      this.classList.toggle('bx-hide');
    });
   form.addEventListener('submit', function (e) {
  if (passwordInput.value !== confirmPassword.value) {
    e.preventDefault(); // Prevent form submission
    errorMessage.textContent = "Passwords do not match. Please check again.";
    confirmPassword.style.border = "2px solid red";
    errorMessage.style.backgroundColor="red"

  } else {
    errorMessage.textContent = ""; // Clear error
    confirmPassword.style.border = ""; // Reset border
  }
});
