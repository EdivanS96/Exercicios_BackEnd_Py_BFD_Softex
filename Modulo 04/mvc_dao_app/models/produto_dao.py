from models.produto import Produto
from database.connection import DatabaseConnection2

class ProdutoDAO:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        with DatabaseConnection2() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL
                )
            ''')

    def salvar(self, produto: Produto):
        with DatabaseConnection2() as cursor:
            cursor.execute(
                'INSERT INTO produto (nome, preco, quantidade) VALUES (?, ?, ?)',
                (produto.nome, produto.preco, produto.quantidade)
            )

    def listar(self):
        with DatabaseConnection2() as cursor:
            cursor.execute('SELECT nome, preco, quantidade FROM produto')
            rows = cursor.fetchall()
            return [Produto(nome, preco, quantidade) for nome, preco, quantidade in rows]