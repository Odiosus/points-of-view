let lastScroll = 0;
const defaultOffset = 100;
const header = document.querySelector('.header');

const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;
const containHide = () => header.classList.contains('hide');

window.addEventListener('scroll', () => {
    if(scrollPosition() > lastScroll && !containHide() && scrollPosition() > defaultOffset) {
        header.classList.add('hide');
    }
    else if(scrollPosition() < lastScroll && containHide()){
        header.classList.remove('hide');
    }

    lastScroll = scrollPosition();
})




document.querySelector('.burger').addEventListener('click', function() {
    document.querySelector('.first-line').classList.toggle('active');
    document.querySelector('.second-line').classList.toggle('active');
    document.querySelector('.nav').classList.toggle('open');
})





var animation = bodymovin.loadAnimation({
        container: document.getElementById('animation-1-2'),
        path: 'https://lottie.host/c404786e-2d84-4239-a092-5fa55366d5a7/DRPRrsgJH4.json', // Путь к вашему JSON-файлу
        renderer: 'svg', // Формат рендеринга (SVG, canvas или HTML)
        loop: true, // Повторять анимацию
        autoplay: true, // Автоматическое воспроизведение
        name: "Demo Animation" // Название анимации (опционально)
    });

//import lottieWeb from 'https://cdn.skypack.dev/lottie-web';
//
//var animation = lottieWeb.loadAnimation({
//  container: document.getElementById('animation-1-2'),
//  path: 'Soft_point.json',
//  renderer: 'svg',
//  loop: true,
//  autoplay: true,
//  name: "Demo Animation",
//});