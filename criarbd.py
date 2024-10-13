# importando sqlite
import sqlite3 as lite

#criando conexao
conn = lite.connect("dados/dados.db")

#criando tabela
with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
    
    