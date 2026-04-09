from flask import Flask
from flask import request, jsonify
from models import Pessoa
from service import Cadastro

app = Flask(__name__)
cadastro = Cadastro()

@app.route("/")
def home():
    return "API funcionando"

@app.route("/pessoas", methods=["GET"])
def listar():
    return jsonify([p.to_dict() for p in cadastro.listar()])

@app.route("/pessoas", methods=["POST"])
def criar():
    data = request.json

    if not data:
        return {"erro": "json invalido"}, 400

    nome = data.get("name")
    idade = data.get("idade")

    try:
        idade = int(idade)
    except:
        return {"erro": "idade invalida"}, 400

    if not nome or not idade:
        return {"erro": "dados incompletos"}, 400
    

    pessoa = Pessoa(nome, idade)
    ok = cadastro.add(pessoa)

    if not ok:
        return {"erro": "usuario ja existe"}, 400
        
    return jsonify(pessoa.to_dict()), 201

@app.route("/pessoas/<nome>", methods=["GET"])
def buscar(nome):
    p = cadastro.find(nome)

    if not p:
        return {"erro": "nao encontrado"}, 404

    return jsonify(p.to_dict())


@app.route("/pessoas/<nome>", methods=["PUT"])
def atualizar(nome):
    data = request.json

    if not data:
        return {"erro": "json invalido"}, 400
    
    idade = data.get("idade")

    if not idade:
        return {"erro": "idade obrigatoria"}, 400

    try:
        idade = int(idade)
    except:
        return {"erro": "idade invalida"}, 400

    ok = cadastro.update(nome, idade)

    if not ok:
        return {"erro": "nao encontrado"}, 404

    return {"msg": "atualizado"}

@app.route("/pessoas/<nome>", methods=["DELETE"])
def deletar(nome):
    ok = cadastro.remove(nome)

    if not ok:
        return {"erro": "nao encontrado"}, 404

    return {"msg": "removido"}

if __name__ == "__main__":
    app.run(debug=True)