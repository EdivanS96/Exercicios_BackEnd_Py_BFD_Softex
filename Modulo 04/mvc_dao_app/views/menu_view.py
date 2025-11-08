class MenuView:
    def menu(self):
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Produtos")
        print("3 - Sair")
    
        return input("Escolha: ")


    def mostrar_mensagem(self, msg):
        print(msg)


    def selecionar_gerenciador(self):
        opcao = self.menu()


        if opcao == "1":
            return "cliente"
        elif opcao == "2":
            return "produto"
        elif opcao == "3":
            self.mostrar_mensagem("Encerrando o sistema...")
            return None
        else:
            self.mostrar_mensagem("Opção inválida!")
            return self.selecionar_gerenciador()
    