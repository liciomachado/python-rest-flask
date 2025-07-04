from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class ProdutoModel(Base):
    __tablename__ = "produtos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    valor = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)

    def to_entity(self):
        from app.domain.entities.produto import Produto
        return Produto(
            id=self.id,
            data_criacao=self.data_criacao,
            nome=self.nome,
            descricao=self.descricao,
            valor=self.valor,
            quantidade_estoque=self.quantidade_estoque
        )

    @staticmethod
    def from_entity(produto):
        return ProdutoModel(
            id=produto.id,
            data_criacao=produto.data_criacao,
            nome=produto.nome,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade_estoque=produto.quantidade_estoque
        )
