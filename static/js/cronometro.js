const inicioRelacionamento = new Date(2016, 10, 18, 12, 0, 0);

function atualizarCronometro() {
  const agora = new Date();
  let diff = agora - inicioRelacionamento;

  const segundos = Math.floor(diff / 1000) % 60;
  const minutos = Math.floor(diff / (1000 * 60)) % 60;
  const horas = Math.floor(diff / (1000 * 60 * 60)) % 24;
  const dias = Math.floor(diff / (1000 * 60 * 60 * 24)) % 30;
  const meses = Math.floor(diff / (1000 * 60 * 60 * 24 * 30)) % 12;
  const anos = Math.floor(diff / (1000 * 60 * 60 * 24 * 365));

  document.getElementById('timer').innerHTML =
    `${anos} anos, ${meses} meses, ${dias} dias <br> ${horas}h ${minutos}m ${segundos}s`;
}

setInterval(atualizarCronometro, 1000);
atualizarCronometro();
