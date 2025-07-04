
from typing import List
from app.domain.entities.user import User
from app.domain.ports.user_repository import IUserRepository

class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def list_users(self) -> List[User]:
        return self.repository.get_all_users()
