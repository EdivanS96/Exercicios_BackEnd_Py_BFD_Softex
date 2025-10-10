class SistemaBiblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.registros = {}

    def cadastrar_usuario(self, nome):
        matricula = len(self.usuarios) + 1
        self.usuarios[matricula] = {
            "nome": nome,
            "emprestimos": []
        }
        print(f"Usuário '{nome}' cadastrado com matrícula {matricula}.")

    def cadastrar_livro(self, titulo, autor, ano):
        codigo = len(self.livros) + 100
        self.livros[codigo] = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": True
        }
        print(f"Livro '{titulo}' cadastrado com código {codigo}.")

    def listar_livros(self, apenas_disponiveis=False):
        print("\n--- LIVROS ---")
        for cod, info in self.livros.items():
            if apenas_disponiveis and not info["disponivel"]:
                continue
            status = "Disponível" if info["disponivel"] else "Emprestado"
            print(f"[{cod}] {info['titulo']} - {info['autor']} ({info['ano']}) - {status}")
        if not self.livros:
            print("Nenhum livro cadastrado.")

    def listar_usuarios(self):
        print("\n--- USUÁRIOS ---")
        for mat, info in self.usuarios.items():
            print(f"[{mat}] {info['nome']} - {len(info['emprestimos'])} empréstimo(s)")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")

    def emprestar_livro(self, codigo_livro, matricula_usuario):
        if codigo_livro not in self.livros:
            print("Livro não encontrado.")
            return
        if matricula_usuario not in self.usuarios:
            print("Usuário não encontrado.")
            return
        if not self.livros[codigo_livro]["disponivel"]:
            print("Livro já emprestado.")
            return

        self.livros[codigo_livro]["disponivel"] = False
        self.usuarios[matricula_usuario]["emprestimos"].append(codigo_livro)
        print("Empréstimo realizado com sucesso.")

    def devolver_livro(self, codigo_livro, matricula_usuario):
        if matricula_usuario not in self.usuarios:
            print("Usuário não encontrado.")
            return
        if codigo_livro not in self.usuarios[matricula_usuario]["emprestimos"]:
            print("Esse usuário não possui esse livro.")
            return

        self.usuarios[matricula_usuario]["emprestimos"].remove(codigo_livro)
        self.livros[codigo_livro]["disponivel"] = True
        print("Livro devolvido com sucesso.")
