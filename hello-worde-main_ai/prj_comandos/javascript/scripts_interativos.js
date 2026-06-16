document.addEventListener("DOMContentLoaded", function () {
  // Inicializa a escuta dos checkboxes de mostrar senha
  const checkboxesMostrar = document.querySelectorAll(".chk-mostrar");

  checkboxesMostrar.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      // Pega o ID do input alvo guardado no atributo 'data-target'
      const targetId = this.getAttribute("data-target");
      const inputSenha = document.getElementById(targetId);

      if (inputSenha) {
        if (this.checked) {
          inputSenha.type = "text";
        } else {
          inputSenha.type = "password";
        }
      }
    });
  });
});
