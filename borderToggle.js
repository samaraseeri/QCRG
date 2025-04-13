document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.getElementById('borderToggle');
    const list = document.getElementById('borderList');

    toggle.addEventListener('click', () => {
        list.style.display = (list.style.display === 'none' || list.style.display === '') ? 'block' : 'none';
    });
});