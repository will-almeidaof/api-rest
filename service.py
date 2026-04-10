import json
from db import get_connection
from models import Pessoa

class Cadastro:
    def listar(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT name, idade FROM pessoas")
        rows = cur.fetchall()

        pessoas = [Pessoa(nome, idade) for nome, idade in rows]

        cur.close()
        conn.close()

        return pessoas

    def add(self, pessoa: Pessoa):
        conn = get_connection()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO pessoas (name, idade) VALUES (%s, %s)",
                (pessoa.name, pessoa.idade)
            )
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            cur.close()
            conn.close()

    def find(self, nome: str):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT name, idade FROM pessoas WHERE name = %s",
            (nome,)
        )

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            return Pessoa(row[0], row[1])
        
        return None
    
    def update(self, nome: str, nova_idade: int):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE pessoas SET idade = %s WHERE name = %s",
            (nova_idade, nome)
        )

        conn.commit()

        atualizado = cur.rowcount  # quantas linhas foram afetadas

        cur.close()
        conn.close()

        return atualizado > 0

    def remove(self, nome: str):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM pessoas WHERE name = %s",
            (nome,)
        )

        conn.commit()

        removido = cur.rowcount

        cur.close()
        conn.close()

        return removido > 0

