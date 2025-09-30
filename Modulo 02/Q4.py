#q4
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @property
    @abstractmethod
    def rodas(self):
        pass

class Carro(Veiculo):
    @property
    def rodas(self):
        return 4
        
    def acelerar(self):
        print("Carro acelerando!")

class Moto(Veiculo):
    @property
    def rodas(self):
        return 2

    def acelerar(self):
        print("Moto acelerando!")

c = Carro()
m = Moto()
c.acelerar()
m.acelerar()
