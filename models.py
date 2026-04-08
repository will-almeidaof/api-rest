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
