from abc import ABC, abstractmethod

class ICarFunctionClient(ABC):
    @abstractmethod
    def consultar_por_codigo(self, codigo: str) -> dict:
        pass
