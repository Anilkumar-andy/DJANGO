const Wrapper = document.querySelector('.Wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

registerLink.addEventListener('click',()=> { Wrapper.classList.add('active')});
loginLink.addEventListener('click',()=> { Wrapper.classList.remove('active')});