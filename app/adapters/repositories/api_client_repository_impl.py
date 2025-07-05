from sqlalchemy import text
from app.domain.entities.api_client import ApiClient
from app.domain.ports.api_client_repository import IApiClientRepository

class ApiClientRepository(IApiClientRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def obter_por_api_key(self, api_key: str):
        with self.session_factory() as session:
            row = session.execute(
                text("SELECT id, nome, api_key, creditos, ativo FROM api_clients WHERE api_key = :api_key"),
                {"api_key": api_key}
            ).fetchone()

            if row:
                return ApiClient(*row)
            return None

    def decrementar_credito(self, api_key: str):
        with self.session_factory() as session:
            session.execute(
                text("UPDATE api_clients SET creditos = creditos - 1 WHERE api_key = :api_key AND creditos > 0"),
                {"api_key": api_key}
            )
            session.commit()
