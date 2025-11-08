from models.cliente import Cliente
from database.connection import DatabaseConnection

class ClienteDAO:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        with DatabaseConnection() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')

    def salvar(self, cliente: Cliente):
        with DatabaseConnection() as cursor:
            cursor.execute(
                'INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)',
                (cliente.nome, cliente.email, cliente.telefone)
            )

    def listar(self):
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT nome, email, telefone FROM cliente')
            rows = cursor.fetchall()
            return [Cliente(nome, email, telefone) for nome, email, telefone in rows]
