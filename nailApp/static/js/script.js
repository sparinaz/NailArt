const cards = document.querySelectorAll(".card img");
const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const closeBtn = document.querySelector(".close");

cards.forEach((img) => {
  img.addEventListener("click", () => {
    lightbox.classList.add("active");
    lightboxImg.src = img.src;
  });
});

closeBtn.addEventListener("click", () => {
  lightbox.classList.remove("active");
});

lightbox.addEventListener("click", (e) => {
  if (e.target === lightbox) {
    lightbox.classList.remove("active");
  }
});
