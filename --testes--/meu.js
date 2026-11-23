function calcular() {
    const valor1 = Number(document.getElementById("valor1").value);
    const valor2 = Number(document.getElementById("valor2").value);
    const resultado = document.getElementById("resultado")
    const soma = valor1 + valor2;
    resultado.value = soma
};