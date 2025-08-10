from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")#home page
def home():
	return render_template("home.html")#retornar o arquivo html de home
@app.route("/info")
def info():
    return render_template("informação.html")
@app.route("/produto)")
def produto():
    return render_template("produto.html")
@app.route("/adm")
def adm():
    return render_template("adm.html")
app.run(host="0.0.0.0",port=5000)