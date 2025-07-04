from abc import ABC, abstractmethod
from app.domain.entities.produto import Produto

class IProdutoRepository(ABC):
    @abstractmethod
    def salvar(self, produto: Produto) -> None:
        pass
