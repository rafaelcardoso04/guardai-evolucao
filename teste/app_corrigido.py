"""Versão corrigida: consulta parametrizada."""
import sqlite3

def criar_banco():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT)")
    con.execute("INSERT INTO usuarios VALUES ('admin', 'senha-do-lab')")
    return con

def login(con, usuario, senha):
    sql = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    return con.execute(sql, (usuario, senha)).fetchone() is not None

if __name__ == "__main__":
    con = criar_banco()
    u = input("Usuário: ")
    s = input("Senha: ")
    print("Login OK" if login(con, u, s) else "Login negado")
