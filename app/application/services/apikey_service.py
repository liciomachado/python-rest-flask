from app.domain.core.result import ForbiddenError, Result, UnauthorizedError
from app.domain.ports.api_client_repository import IApiClientRepository

class ApiKeyService:
    def __init__(self, repository: IApiClientRepository):
        self.repository = repository

    def validar_chave(self, api_key: str) -> Result[None, Exception]:
        client = self.repository.obter_por_api_key(api_key)

        if not client:
            return Result.Err(UnauthorizedError("API Key inválida"))

        if not client.ativo:
            return Result.Err(ForbiddenError("Cliente inativo"))

        if client.creditos <= 0:
            return Result.Err(ForbiddenError("Sem créditos disponíveis"))

        # Se quiser, decremente agora (ou no final da execução)
        self.repository.decrementar_credito(api_key)

        return Result.Ok(None)
