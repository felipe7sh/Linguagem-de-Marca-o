const formulario = document.getElementById("formIMC");
formulario.addEventListener("submit", function (event) {
    event.preventDefault();

    const distancia = Number(document.getElementById("distancia").value);
    const combustivel = Number(document.getElementById("combustivel").value);
    const preco = Number(document.getElementById("preco").value);
    const capacidade = Number(document.getElementById("capacidade").value);
    const Medio = distancia / combustivel;
    const Total = combustivel * preco;
    const custoPorKm = Total / distancia;
    const combustivelUtilizado = distancia / Medio;
    const combustivelRestante = Math.max(0, combustivel - combustivelUtilizado);
    const consumoAcimaDeDez = Medio > 10;
    const AbaixoDeDuzentos = Total < 200;
    const suficienteParaMaisCem = combustivel >= (100 / Medio);
    const tanqueAcimaDaMetade = combustivel > (capacidade * 0.5);
    const viagemAcimaDeCem = distancia > 100 && Medio > 12;

    console.log("Consumo médio: " + Medio.toFixed(2) + " km/l");
    console.log("Custo total: R$ " + Total.toFixed(2));
    console.log("Custo por km: R$ " + custoPorKm.toFixed(2));
    console.log("Combustível restante: " + combustivelRestante.toFixed(2) + " litros");
    console.log("Consumo acima de 10 km/l? " + consumoAcimaDeDez);
    console.log("Custo inferior a R$ 200? " + AbaixoDeDuzentos);
    console.log("Combustível suficiente para mais 100 km? " + suficienteParaMaisCem);
    console.log("Tanque acima de 50%? " + tanqueAcimaDaMetade);
    console.log("Viagem acima de 100 km e consumo acima de 12? " + viagemAcimaDeCem);
});
