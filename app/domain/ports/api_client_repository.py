from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.api_client import ApiClient

class IApiClientRepository(ABC):
    @abstractmethod
    def obter_por_api_key(self, api_key: str) -> Optional["ApiClient"]:
        pass

    @abstractmethod
    def decrementar_credito(self, api_key: str) -> None:
        pass
