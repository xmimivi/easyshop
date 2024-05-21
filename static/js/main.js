const swiperTop = new Swiper('.top_swiper', {
  // Optional parameters
 
  loop: true,



  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },


});

const swiperAbout = new Swiper(".about_slider", {
  slidesPerView: 4,
  spaceBetween: 20,
  freeMode: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

document.querySelectorAll('.accordion_triger').forEach((item) => {
  item.addEventListener('click', () => {
    item.parentNode.classList.toggle('accordion_item--active')
  })
});