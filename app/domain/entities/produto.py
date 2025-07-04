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
