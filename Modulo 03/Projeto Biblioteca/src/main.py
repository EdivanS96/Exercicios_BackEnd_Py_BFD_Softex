from sistema_biblioteca import SistemaBiblioteca

def menu():
    print("\n=== MENU BIBLIOTECA ===")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar livro")
    print("3 - Listar livros")
    print("4 - Listar usuários")
    print("5 - Emprestar livro")
    print("6 - Devolver livro")
    print("0 - Sair")

def main():
    sistema = SistemaBiblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            sistema.cadastrar_usuario(nome)

        elif opcao == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            sistema.cadastrar_livro(titulo, autor, ano)

        elif opcao == "3":
            sistema.listar_livros()

        elif opcao == "4":
            sistema.listar_usuarios()

        elif opcao == "5":
            try:
                cod = int(input("Código do livro: "))
                mat = int(input("Matrícula do usuário: "))
                sistema.emprestar_livro(cod, mat)
            except ValueError:
                print("Código/matrícula inválidos!")

        elif opcao == "6":
            try:
                cod = int(input("Código do livro: "))
                mat = int(input("Matrícula do usuário: "))
                sistema.devolver_livro(cod, mat)
            except ValueError:
                print("Código/matrícula inválidos!")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
