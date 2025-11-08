#from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController
from controllers.menu_controller import MenuController

if __name__ == "__main__":
    #app = ClienteController()
    #app = ProdutoController()
    #app.iniciar()
    app = MenuController()
    app.iniciar()