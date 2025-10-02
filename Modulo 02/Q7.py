from abc import ABC, abstractmethod

class Percurso(ABC):
    @abstractmethod
    def tempo_estimado(self, distancia):
        pass

class Cobranca(ABC):
    @abstractmethod
    def calcular_tarifa(self, distancia):
        pass

class Taxi(Percurso, Cobranca):
    def tempo_estimado(self, distancia):
        return distancia / 40  # km/h médio

    def calcular_tarifa(self, distancia):
        return 5 + (distancia * 2)

t = Taxi()
print("Tempo:", t.tempo_estimado(20), "h")
print("Tarifa:", t.calcular_tarifa(20), "R$")
