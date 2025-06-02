const carousel = document.querySelector('.carousel');
const images = document.querySelectorAll('.carousel img');
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');

let index = 0;

function updateCarousel() {
  const largura = images[0].clientWidth;
  carousel.style.transform = `translateX(${-index * largura}px)`;
}

prevBtn.addEventListener('click', () => {
  index = (index === 0) ? images.length - 1 : index - 1;
  updateCarousel();
});

nextBtn.addEventListener('click', () => {
  index = (index === images.length - 1) ? 0 : index + 1;
  updateCarousel();
});

function ajustarCarousel() {
  const imgs = document.querySelectorAll('.carousel img');
  let largura = window.innerWidth <= 480 ? 240 : 320;

  imgs.forEach(img => {
    img.style.width = '100%';
  });

  updateCarousel();
}

window.addEventListener('resize', ajustarCarousel);
ajustarCarousel();
