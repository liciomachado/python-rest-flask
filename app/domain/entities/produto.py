from datetime import datetime
from uuid import UUID, uuid4

class Produto:
    def __init__(self, nome: str, descricao: str, valor: float, quantidade_estoque: int, id: UUID = None, data_criacao: datetime = None):
        self.id = id or uuid4()
        self.data_criacao = data_criacao or datetime.utcnow()
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "data_criacao": self.data_criacao.isoformat(),
            "nome": self.nome,
            "descricao": self.descricao,
            "valor": self.valor,
            "quantidade_estoque": self.quantidade_estoque
        }
