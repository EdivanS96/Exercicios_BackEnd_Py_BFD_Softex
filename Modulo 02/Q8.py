from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @abstractmethod
    def detalhes_de_cadastro(self):
        pass

class Cliente(Pessoa):
    def __init__(self, id, nome, data_cadastro):
        super().__init__(id, nome)
        self.data_cadastro = data_cadastro

    def detalhes_de_cadastro(self):
        print(f"Cliente {self.nome}, cadastrado em {self.data_cadastro}")





class Fornecedor(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj

    def detalhes_de_cadastro(self):
        print(f"Fornecedor {self.nome}, CNPJ: {self.cnpj}")

def listar_pessoas(pessoas):
    for p in pessoas:
        p.detalhes_de_cadastro()

pessoas = [
    Cliente(1, "João", "2025-09-28"),
    Fornecedor(2, "Empresa X", "12.345.678/0001-99")
]
listar_pessoas(pessoas)
