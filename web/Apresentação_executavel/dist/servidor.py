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
@app.route("/adm")
def adm():
    return render_template("adm.html",Cores=Cores,usuarios=usuarios)
app.run(host="0.0.0.0",port=5000)