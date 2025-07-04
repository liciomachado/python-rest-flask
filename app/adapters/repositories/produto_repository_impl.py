from app.domain.ports.produto_repository import IProdutoRepository
from app.domain.entities.produto import Produto
from sqlalchemy.orm import Session
from app.adapters.repositories.sqlalchemy_models import ProdutoModel

class ProdutoRepository(IProdutoRepository):
    def __init__(self, session: Session):
        self.session = session

    def salvar(self, produto: Produto) -> None:
        model = ProdutoModel.from_entity(produto)
        self.session.add(model)
        self.session.commit()
