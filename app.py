import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Configuração do banco de dados SQLite
DB_PATH = "tasks.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS listas (id INTEGER PRIMARY KEY, nome TEXT UNIQUE)")
        cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, lista_id INTEGER, tarefa TEXT, concluida INTEGER DEFAULT 0, FOREIGN KEY(lista_id) REFERENCES listas(id))")
        conn.commit()

init_db()

def get_listas():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM listas")
        return cursor.fetchall()

def get_tarefas(lista_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE lista_id=?", (lista_id,))
        return cursor.fetchall()

@app.route('/')
def home():
    listas = get_listas()
    return render_template('home.html', listas=listas)

@app.route('/nova_lista', methods=['POST'])
def nova_lista():
    nome_lista = request.form.get('nome_lista')
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO listas (nome) VALUES (?)", (nome_lista,))
        conn.commit()
    return redirect(url_for('home'))

@app.route('/lista/<int:lista_id>/remover', methods=['POST'])
def remove_lista(lista_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas where lista_id=?",(lista_id,))
        cursor.execute("DELETE FROM listas where id=?",(lista_id,))
        conn.commit()
    return redirect(url_for('home'))

@app.route('/lista/<int:lista_id>')
def visualizar_lista(lista_id):
    tarefas = get_tarefas(lista_id)
    return render_template('lista.html', tarefas=tarefas, lista_id=lista_id)

@app.route('/lista/<int:lista_id>/add_tarefa', methods=['POST'])
def add_tarefa(lista_id):
    tarefa = request.form.get('tarefa')
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (lista_id, tarefa) VALUES (?, ?)", (lista_id, tarefa))
        conn.commit()
    return redirect(url_for('visualizar_lista', lista_id=lista_id))

@app.route('/lista/<int:lista_id>/del_tarefa/<int:tarefa_id>', methods=['POST'])
def del_tarefa(lista_id, tarefa_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id=?", (tarefa_id,))
        conn.commit()
    return redirect(url_for('visualizar_lista', lista_id=lista_id))

@app.route('/limpar_bd', methods=['POST'])
def limpar_bd():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas")
        cursor.execute("DELETE FROM listas")
        conn.commit()
    return "Banco de dados limpo!", 200



if __name__ == '__main__':
    app.run(debug=True)
