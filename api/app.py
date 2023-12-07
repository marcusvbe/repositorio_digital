from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/") # criando rotas com decorator
def index():
    return render_template("index.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")

@app.route("/projetos.html")
def projetos():
    proj1 = "Dados da Covid – Projeto Integrado (API) 01/2023"
    proj2 = "Desafio UNES – Desenvolvimento Web"
    proj3 = "Portfólio – Design Digital"
    proj4 = "Sistema de Gestão de Chamados (API) 02/2023"
    return render_template("projetos.html", projeto1=proj1, projeto2=proj2, projeto3=proj3, projeto4=proj4)

@app.route("/contato.html")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)





