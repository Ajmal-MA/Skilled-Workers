const containers = document.querySelector('.containers');
const registerBtn= document.querySelector('.register-btn');
const loginBtn= document.querySelector('.login-btn');

registerBtn.addEventListener('click', () => {
    containers.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    containers.classList.remove('active');
});