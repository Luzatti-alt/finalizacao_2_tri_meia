import sys
import os
dir_atual = os.path.dirname(__file__)
dir_base = os.path.abspath(os.path.join(dir_atual, ".."))
sys.path.append(dir_base)
from flask import Flask, render_template
#impelmentar o db
from database.db import session, Cores, usuarios
app = Flask(__name__)
#integrar a um db ja existente
@app.route("/")#home page
def home():
	return render_template("index.html")#retornar o arquivo html de home
@app.route("/info")
def info():
    return render_template("informação.html",usuarios=usuarios)
@app.route("/produto")
def produto():
    return render_template("produto.html")
@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")
def adm():
    # Busca todos os registros da tabela Cores
    cores_lista = Cores.query.all()  

    # Supondo que 'usuarios' seja algo semelhante
    usuarios_lista = usuarios.query.all()  # se 'usuarios' for uma classe SQLAlchemy

    return render_template("adm.html", Cores=cores_lista, usuarios=usuarios_lista)
app.run(host="0.0.0.0",port=5000)
