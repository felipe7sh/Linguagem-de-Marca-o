from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
   return render_template("inicio.html")
@app.route("/empresa")
def empresa():
  return render_template("empresa.html")

@app.route("/cidades")
def cidades():
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

@app.route("/cadastrar_empresa", methods=["POST"])
def cadastrar_empresa():
  cnpj = request.form.get("cnpj")
  razao_social = request.form.get("razao_social")
  nome_fantasia = request.form.get("nome_fantasia")
  porte = request.form.get("porte")
  data_abertura = request.form.get("data_abertura")
  cnae_principal = request.form.get("cnae_principal")
  atividade_principal = request.form.get("atividade_principal")
  cnaes_secundarios = request.form.get("cnaes_secundarios")
  atividades_secundarias = request.form.get("atividades_secundarias")
  tipo_juridico = request.form.get("tipo_juridico")
  endereco = request.form.get("endereco")
  numero = request.form.get("numero")
  complemento = request.form.get("complemento")
  bairro = request.form.get("bairro")
  cep = request.form.get("cep")
  cidade = request.form.get("cidade")
  estado = request.form.get("estado")
  email = request.form.get("email")
  telefone = request.form.get("telefone")
  situacao_cadastral = request.form.get("situacao_cadastral")

  print("Dados Recebidos:")
  print("CNPJ:", cnpj)
  print("Razão social:", razao_social)
  print("Nome fantasia:", nome_fantasia)
  print("Porte:", porte)
  print("Data de abertura:", data_abertura)
  print("CNAE principal:", cnae_principal)
  print("Atividade principal:", atividade_principal)
  print("CNAEs secundários:", cnaes_secundarios)
  print("Atividades secundárias:", atividades_secundarias)
  print("Tipo jurídico:", tipo_juridico)
  print("Endereço:", endereco)
  print("Número:", numero)
  print("Complemento:", complemento)
  print("Bairro:", bairro)
  print("CEP:", cep)
  print("Cidade:", cidade)
  print("Estado:", estado)
  print("E-mail:", email)
  print("Telefone:", telefone)
  print("Situação cadastral:", situacao_cadastral)

  return (
      f"Dados Recebidos: {cnpj}, {razao_social}, {nome_fantasia}, {porte}, "
      f"{data_abertura}, {cnae_principal}, {atividade_principal}, "
      f"{cnaes_secundarios}, {atividades_secundarias}, {tipo_juridico}, "
      f"{endereco}, {numero}, {complemento}, {bairro}, {cep}, {cidade}, "
      f"{estado}, {email}, {telefone}, {situacao_cadastral}"
  )


if __name__ == "__main__":
  app.run(debug=True)
