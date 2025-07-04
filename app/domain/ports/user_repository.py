from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass