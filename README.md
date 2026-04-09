# 🚀 API de Pessoas — Flask + PostgreSQL

API REST desenvolvida para gerenciamento de pessoas, com persistência em banco de dados e arquitetura em camadas.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de backend, incluindo:

* Criação de APIs REST
* Integração com banco de dados relacional
* Organização de código em camadas
* Operações CRUD completas

---

## 🧠 Arquitetura

O projeto segue uma separação clara de responsabilidades:

```
app.py        → rotas e comunicação HTTP  
service.py    → regras de negócio e acesso ao banco  
models.py     → estrutura dos dados  
db.py         → conexão com banco de dados  
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* Flask
* PostgreSQL
* psycopg2

---

## 🔄 Funcionalidades (CRUD)

* ✅ Criar pessoa
* ✅ Listar pessoas
* ✅ Buscar por nome
* ✅ Atualizar idade
* ✅ Remover pessoa

---

## 🌐 Endpoints

### 🔹 Listar pessoas

```
GET /pessoas
```

---

### 🔹 Criar pessoa

```
POST /pessoas
```

**Body:**

```json
{
  "name": "joao",
  "idade": 20
}
```

---

### 🔹 Buscar pessoa

```
GET /pessoas/{nome}
```

---

### 🔹 Atualizar pessoa

```
PUT /pessoas/{nome}
```

**Body:**

```json
{
  "idade": 25
}
```

---

### 🔹 Remover pessoa

```
DELETE /pessoas/{nome}
```

---

## 🛠️ Como Executar

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/api-pessoas-flask.git
cd api-pessoas-flask
```

---

### 2. Instalar dependências

```
pip install flask psycopg2-binary
```

---

### 3. Configurar banco de dados

Crie um banco chamado:

```
pessoas_db
```

Tabela:

```
pessoas
```

Colunas:

* id (serial, primary key)
* name (text)
* idade (integer)

---

### 4. Configurar conexão

No arquivo `db.py`, ajuste:

```python
host="localhost"
database="pessoas_db"
user="postgres"
password="SUA_SENHA"
```

---

### 5. Rodar a aplicação

```
python app.py
```

---

## 🧪 Testes

A API pode ser testada utilizando ferramentas como Postman ou Insomnia.

---

## 📈 Evolução do Projeto

Este projeto evoluiu de:

```
CLI (input/print) → JSON → API REST → PostgreSQL
```

---

## 🎯 Objetivo

Demonstrar habilidades práticas em:

* Backend com Python
* Desenvolvimento de APIs REST
* Integração com banco de dados
* Organização de código em projetos reais

---

## 🚀 Próximos Passos

* Autenticação com JWT
* Estrutura profissional (controllers, routes)
* Deploy em ambiente cloud

---

## 👨‍💻 Autor

Desenvolvido por [Seu Nome]

---
