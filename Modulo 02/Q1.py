#Q1
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido!")

a = Animal("Bicho")
c = Cachorro("Rex")

a.emitir_som()
c.emitir_som()