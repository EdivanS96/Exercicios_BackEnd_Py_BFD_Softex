from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def verificar_saldo(self):
        print(f"Saldo: R${self.saldo}")


class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        self.saldo -= valor




contas = [ContaCorrente(1000), ContaCorrente(500)]
for c in contas:
    c.sacar(100)
    c.verificar_saldo()
