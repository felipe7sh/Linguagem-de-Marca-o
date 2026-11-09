from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("cidades.html")

@app.route("/cadastrar_cidade", methods=["POST"])
def cadastrar_cidade():
    cidade = request.form.get("cidade")
    estado = request.form.get("estado")
    ibge = request.form.get("ibge")
    populacao = request.form.get("populacao")
    regiao = request.form.get("regiao")

    print("Dados Recebidos:")
    print("Cidade:", cidade)
    print("Estado:", estado)
    print("ibge:", ibge)
    print("populacao:", populacao)
    print("regiao:", regiao)

    return f"Dados Recebidos: {cidade}, {estado}, {ibge}, {populacao}, {regiao}"
if __name__ == "__main__":
    app.run(debug=True)