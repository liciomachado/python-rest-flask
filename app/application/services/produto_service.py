from app.config import Config
from app.domain.core.result import AppError, BadRequestError, NotFoundError, Result
from app.domain.entities.produto import Produto
from app.domain.ports.event_bus import IEventBus
from app.domain.ports.produto_repository import IProdutoRepository
from app.domain.ports.car_function_client import ICarFunctionClient

class ProdutoService:
    def __init__(self, repository: IProdutoRepository, car_function_client: ICarFunctionClient,  event_bus: IEventBus):
        self.repository = repository
        self.car_function_client = car_function_client
        self.event_bus = event_bus

    def salvar_produto(self, nome: str, descricao: str, valor: float, quantidade_estoque: int, codigo_car: str = None) -> Result[Produto, AppError]:
        try:
            if not nome:
                return Result.Err(BadRequestError("Nome do produto é obrigatório"))

            if valor <= 0:
                return Result.Err(BadRequestError("Valor deve ser maior que zero"))

            if codigo_car:
                car_info = self.car_function_client.consultar_por_codigo(codigo_car)
                if not car_info:
                    return Result.Err(NotFoundError("Código CAR não encontrado"))

            produto = Produto(nome, descricao, valor, quantidade_estoque)
            self.repository.salvar(produto)

            # ✅ Publica mensagem no RabbitMQ
            self.event_bus.publish("produto_criado", produto.to_dict())

            return Result.Ok(produto)

        except Exception as e:
            return Result.Err(AppError(f"Erro inesperado: {str(e)}"))

    def listar_produtos(self) -> list[Produto]:
        print("environment:", Config.ENV)
        print("CAR_FUNCTION_API_KEY:", Config.CAR_FUNCTION_API_KEY)
        return self.repository.listar_todos()
