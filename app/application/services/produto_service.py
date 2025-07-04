from app.domain.entities.produto import Produto
from app.domain.ports.produto_repository import IProdutoRepository

class ProdutoService:
    def __init__(self, repository: IProdutoRepository):
        self.repository = repository

    def salvar_produto(self, nome: str, descricao: str, valor: float, quantidade_estoque: int):
        produto = Produto(
            nome=nome,
            descricao=descricao,
            valor=valor,
            quantidade_estoque=quantidade_estoque
        )
        self.repository.salvar(produto)
        return produto
