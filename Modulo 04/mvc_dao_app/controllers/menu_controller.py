from views.menu_view import MenuView

class MenuController:
    def __init__(self):
        self.view = MenuView()

    def iniciar(self):
        while True:
            gerenciador = self.view.selecionar_gerenciador()

            if gerenciador is None:
                break

            if gerenciador == "cliente":
                from controllers.cliente_controller import ClienteController
                app = ClienteController()
                app.iniciar()

            elif gerenciador == "produto":
                from controllers.produto_controller import ProdutoController
                app = ProdutoController()
                app.iniciar()