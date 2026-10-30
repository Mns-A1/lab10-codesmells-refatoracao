from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, distancia):
        pass

class FreteMoto(EstrategiaFrete):
    def calcular(self, distancia): 
        return distancia * 2.0

class FreteCarro(EstrategiaFrete):
    def calcular(self, distancia): 
        return distancia * 3.5 + 10.0

class FreteCaminhao(EstrategiaFrete):
    def calcular(self, distancia): 
        return distancia * 8.0 + 50.0

class FreteBicicleta(EstrategiaFrete):
    def calcular(self, distancia): 
        return distancia * 1.0

class CalculadoraDeFrete:
    def calcular_frete(self, estrategia: EstrategiaFrete, distancia):
        return estrategia.calcular(distancia)
