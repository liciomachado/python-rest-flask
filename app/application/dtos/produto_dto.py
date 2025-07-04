from app.domain.entities.produto import Produto

class ProdutoDTO:
    def __init__(self, id, data_criacao, nome, descricao, valor, quantidade_estoque):
        self.id = id
        self.data_criacao = data_criacao
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque

    @staticmethod
    def from_entity(produto: Produto):
        return ProdutoDTO(
            id=str(produto.id),
            data_criacao=produto.data_criacao.isoformat(),
            nome=produto.nome,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade_estoque=produto.quantidade_estoque
        )

    def to_dict(self):
        return {
            "id": self.id,
            "data_criacao": self.data_criacao,
            "nome": self.nome,
            "descricao": self.descricao,
            "valor": self.valor,
            "quantidade_estoque": self.quantidade_estoque
        }
