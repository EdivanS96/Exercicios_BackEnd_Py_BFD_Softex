from models.cliente import Cliente
from models.cliente_dao import ClienteDAO
from views.cliente_view import ClienteView

class ClienteController:
    def __init__(self):
        self.dao = ClienteDAO()
        self.view = ClienteView()

    def iniciar(self):
        while True:
            opcao = self.view.menu()

            if opcao == "1":
                nome, email, telefone = self.view.solicitar_dados()
                cliente = Cliente(nome, email, telefone)
                self.dao.salvar(cliente)
                self.view.mostrar_mensagem("✅ Cliente cadastrado com sucesso!")

            elif opcao == "2":
                clientes = self.dao.listar()
                self.view.mostrar_clientes(clientes)

            elif opcao == "3":
                self.view.mostrar_mensagem("👋 Encerrando o sistema...")
                break

            else:
                self.view.mostrar_mensagem("❌ Opção inválida!")
