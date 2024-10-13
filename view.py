# importando sqlite
import sqlite3 as lite

# criando conexão
conn = lite.connect("dados/dados.db")

# Create Read Update Delete (CRUD)
# --------------------------Criar inventario-----------------------------------------
# inserir inventario
def inserir_form(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO inventario(nome,local,descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# ----------------------------Atualizar inventario-----------------------------------------
# atualizar inventario
def atualizar_form(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# --------------------------Deleta inventatio------------------------------------------
# deleta inventario
def deletar_form(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


# -----------------------------Ver inventario-----------------------------------------------
# ver inventario
def ver_form():
    lista_itens = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# --------------------------Ver dados no inventario------------------------------------------
# ver itens no inventario
def ver_item(id):
    lista_itens = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens
