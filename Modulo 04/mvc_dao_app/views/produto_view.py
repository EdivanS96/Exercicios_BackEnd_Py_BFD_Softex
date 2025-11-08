class ProdutoView:
    def menu(self):
        print("\n==== MENU PRODUTOS ====")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Sair")
        return input("Escolha: ")

    def solicitar_dados(self):
        nome = input("Nome do Produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        return nome, preco, quantidade

    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_produtos(self, produtos):
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== Lista de Produtos ===")
            for p in produtos:
                print("-", p)