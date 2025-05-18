// Animation subtile à l'ouverture
window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.style.opacity = 0;
    form.style.transform = 'translateY(20px)';
    setTimeout(() => {
        form.style.transition = 'all 0.8s ease';
        form.style.opacity = 1;
        form.style.transform = 'translateY(0)';
    }, 200);
});

// Ajout d'un effet sonore quand on clique sur le bouton
const button = document.querySelector('button');
if (button) {
    button.addEventListener('click', () => {
        const audio = new Audio('https://assets.mixkit.co/sfx/preview/mixkit-select-click-1109.mp3');
        audio.volume = 0.3;
        audio.play();
    });
}

// Effet de survol sur les textareas
const textareas = document.querySelectorAll('textarea');
textareas.forEach((ta) => {
    ta.addEventListener('mouseenter', () => {
        ta.style.boxShadow = '0 0 15px #ff00c8';
    });
    ta.addEventListener('mouseleave', () => {
        ta.style.boxShadow = 'inset 0 0 10px #00ffe0';
    });
});
