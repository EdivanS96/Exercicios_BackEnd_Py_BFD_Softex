class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __srt__ (self):
        return f"{self.nome} - R${self.preco:.2f} (Qtd: {self.quantidade})"