from app.domain.entities.produto import Produto
from app.domain.ports.produto_repository import IProdutoRepository
from app.domain.ports.car_function_client import ICarFunctionClient

class ProdutoService:
    def __init__(self, repository: IProdutoRepository, car_function_client: ICarFunctionClient):
        self.repository = repository
        self.car_function_client = car_function_client

    def salvar_produto(self, nome: str, descricao: str, valor: float, quantidade_estoque: int, codigo_car: str = None):
        if nome:
            print("Passando no car", nome)
            car_info = self.car_function_client.consultar_por_codigo(nome)
            # Você pode fazer algo com essa resposta, como registrar no produto, validar, etc.
            print("Resultado da API externa:", car_info)

        produto = Produto(
            nome=nome,
            descricao=descricao,
            valor=valor,
            quantidade_estoque=quantidade_estoque
        )
        self.repository.salvar(produto)
        return produto

    def listar_produtos(self) -> list[Produto]:
        return self.repository.listar_todos()
