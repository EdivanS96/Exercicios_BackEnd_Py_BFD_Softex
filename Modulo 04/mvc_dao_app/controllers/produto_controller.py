from models.produto import Produto
from models.produto_dao import ProdutoDAO
from views.produto_view import ProdutoView

class ProdutoController:
    def __init__(self):
        self.dao = ProdutoDAO()
        self.view = ProdutoView()

    def iniciar(self):
        while True:
            opcao = self.view.menu()

            if opcao == "1":
                nome, preco, quantidade = self.view.solicitar_dados()
                produto = Produto(nome, preco, quantidade)
                self.dao.salvar(produto)
                self.view.mostrar_mensagem("Produto cadastrado com sucesso!")

            elif opcao == "2":
                produtos = self.dao.listar()
                self.view.mostrar_produtos(produtos)

            elif opcao == "3":
                self.view.mostrar_mensagem("Encerrando o sistema...")
                break

            else:
                self.view.mostrar_mensagem("Opção inválida!")