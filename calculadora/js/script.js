const formulario = document.getElementById("formIMC");
formulario.addEventListener("submit", function(event) {
    event.preventDefault();
    const valor1 = parseFloat(document.getElementById("valor1").value);
    const valor2 = parseFloat(document.getElementById("valor2").value);
    const soma = valor1 + valor2 
    document.getElementById("resultado").value = soma.toFixed(2)
    alert("A soma é: " + soma.toFixed(2))
});