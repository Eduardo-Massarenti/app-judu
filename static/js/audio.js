const musica = document.getElementById("audio");

musica.play().catch(() => {
  document.addEventListener("click", () => {
    musica.play();
  }, { once: true });
  document.addEventListener("touchstart", () => {
    musica.play();
  }, { once: true });
});
