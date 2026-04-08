import json
from models import Pessoa

class Cadastro:
    def __init__(self):
        self.lista: list[Pessoa] = []
        self.file = "dados.json"
        self.load()

    def add(self, pessoa: Pessoa):
        if pessoa.idade <= 0:
            print("idade invalida")
            return
        if self.find(pessoa.name):
            return False
        self.lista.append(pessoa)
        self.save()

    def find(self, nome: str):
        for p in self.lista:
            if p.name == nome:
                return p
        return None
    
    def update(self, nome: str, nova_idade: int):
        p = self.find(nome)
        if p:
            p.idade = nova_idade
            self.save()
            return True
        return False

    def remove(self, nome: str):
        p = self.find(nome)
        if p:
            self.lista.remove(p)
            self.save()
            return True
        return False

    def save(self):
        data = [p.to_dict() for p in self.lista]
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                self.lista = [Pessoa.from_dict(p) for p in data]
        except FileNotFoundError:
            self.lista= []

    def __str__(self):
        if not self.lista:
            return "cadastro vazio"
        return "\n".join(str(x) for x in self.lista)