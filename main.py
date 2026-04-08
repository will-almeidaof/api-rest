import json


class Pessoa:
    def __init__(self, name: str, idade: int):
        self.name = name
        self.idade = idade

    def to_dict(self):
        return {
            "name": self.name,
            "idade": self.idade
        }

    @staticmethod
    def from_dict(data):
        return Pessoa(data["name"], data["idade"])

    def __str__(self):
        return f"{self.name}: {self.idade}"


class Cadastro:
    def __init__(self):
        self.lista: list[Pessoa] = []
        self.file = "dados.json"
        self.load()

    def add(self, pessoa: Pessoa):
        if pessoa.idade <= 0:
            print("idade invalida")
            return
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
        else:
            print("pessoa não encontrada")

    def remove(self, nome: str):
        p = self.find(nome)
        if p:
            self.lista.remove(p)
            self.save()
        else:
            print("pessoa não encontrada")

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


def main():
    cadastro = Cadastro()

    while True:
        line = input(">>> ")
        args = line.split()

        if not args:
            continue

        comando = args[0]

        if comando == "end":
            break

        elif comando == "show":
            print(cadastro)

        elif comando == "add":
            if len(args) != 3:
                print("uso: add nome idade")
                continue

            nome = args[1]

            try:
                idade = int(args[2])
            except ValueError:
                print("idade invalida")
                continue

            pessoa = Pessoa(nome, idade)
            cadastro.add(pessoa)

        elif comando == "find":
            if len(args) != 2:
                print("uso: find nome")
                continue
        
            p = cadastro.find(args[1])
            print(p if p else "nao encontrado")

        elif comando == "update":
            if len(args) != 3:
                print("uso: update nome idade")
                continue
            
            try:
                idade = int(args[2])
            except:
                print("idade invalida")
                continue

            cadastro.update(args[1], idade)

        elif comando == "remove":
            if len(args) != 2:
                print("uso: remove nome")
                continue
        
            cadastro.remove(args[1])

        else:
            print("comando invalido")


if __name__ == "__main__":
    main()