# To-Do List em Flask

To Do List desenvolvida em flask para o case técnico.

## 📌 Requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.x
- Flask
- SQLite3

## 🚀 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/Tiago1604/To_Do_List.git
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  ou No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicialize o banco de dados:

```bash
python
>>> from app import init_db
>>> init_db()
>>> exit()
```

## 🎯 Como Executar

Após instalar as dependências, execute o seguinte comando:

```bash
python app.py
```

O servidor estará rodando em `http://127.0.0.1:5000/`.


## 🔗 Tecnologias Utilizadas

- Python + Flask
- SQLite
- HTML + CSS
