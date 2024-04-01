
document.addEventListener('DOMContentLoaded', () => {
    let lang = navigator.language;
    window.sessionStorage.setItem('activebutton', lang.substr(0, 2));
    let buttonId = document.getElementById(lang.substr(0, 2));
    window.sessionStorage.setItem('active', buttonId);

});