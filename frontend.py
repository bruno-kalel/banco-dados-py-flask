import backend
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/retorno", methods=['POST'])
def retorno():
    nome = request.form['name']
    return render_template('retorno.html', nome=nome, dados=backend.pesquisar_por_varchar(nome))
