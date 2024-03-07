# API CRUD de Leads em Python

Este documento descreve uma API simples para realizar operações CRUD (Create, Read, Update, Delete) em registros de leads. A API é construída utilizando o framework Flask e SQLAlchemy para interagir com um banco de dados PostgreSQL. Além disso, fornecerei instruções sobre como clonar o repositório no Git e testar a API.

## Configuração

### Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Python (3.6 ou superior)
- Flask
- SQLAlchemy
- psycopg2
- Git

### Configuração do Banco de Dados

A API utiliza um banco de dados PostgreSQL. Certifique-se de ter um servidor PostgreSQL em execução e configure as informações de conexão no arquivo `app/configs/database.py`.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

```
|-- app
|   |-- configs
|   |   |-- database.py
|   |-- models
|   |   |-- leads_model.py
|   |-- routes
|   |   |-- leads_routes.py
|   |-- __init__.py
|-- tests
|-- .gitignore
|-- app.py
|-- requirements.txt
|-- README.md
```

- **app/configs/database.py**: Configuração do banco de dados.
- **app/models/leads_model.py**: Definição do modelo de leads utilizando SQLAlchemy.
- **app/routes/leads_routes.py**: Implementação das rotas CRUD da API.
- **tests**: Diretório para testes (opcional).
- **app.py**: Arquivo principal para iniciar a aplicação.
- **requirements.txt**: Lista de dependências.

## API CRUD

### 1. Criação de Lead

Endpoint: `POST /leads`

#### Payload de Exemplo

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "(XX)XXXXX-XXXX"
}
```

#### Resposta de Exemplo (201 Created)

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "(XX)XXXXX-XXXX",
  "creation_date": "2024-03-07T12:00:00",
  "last_visit": "2024-03-07T12:00:00",
  "visits": 1
}
```

### 2. Obter Todos os Leads

Endpoint: `GET /leads`

#### Resposta de Exemplo (200 OK)

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "(XX)XXXXX-XXXX",
    "creation_date": "2024-03-07T12:00:00",
    "last_visit": "2024-03-07T12:00:00",
    "visits": 1
  }
]
```

### 3. Atualizar Visitas de Lead

Endpoint: `PUT /leads`

#### Payload de Exemplo

```json
{
  "email": "john@example.com"
}
```

#### Resposta de Exemplo (200 OK)

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "(XX)XXXXX-XXXX",
  "creation_date": "2024-03-07T12:00:00",
  "last_visit": "2024-03-07T13:00:00",
  "visits": 2
}
```

### 4. Excluir Lead

Endpoint: `DELETE /leads`

#### Payload de Exemplo

```json
{
  "email": "john@example.com"
}
```

#### Resposta de Exemplo (200 OK)

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "(XX)XXXXX-XXXX",
  "creation_date": "2024-03-07T12:00:00",
  "last_visit": "2024-03-07T13:00:00",
  "visits": 2
}
```

## Como Clonar e Testar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:

```bash
cd nome-do-projeto
pip install -r requirements.txt
```

3. Configure o banco de dados no arquivo `app/configs/database.py`.

4. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

### Testes (Opcional)

Para executar testes (caso disponíveis), você pode usar o seguinte comando:

```bash
pytest
```

Certifique-se de ter o módulo `pytest` instalado.

Agora você pode interagir com a API CRUD de leads em Python!
