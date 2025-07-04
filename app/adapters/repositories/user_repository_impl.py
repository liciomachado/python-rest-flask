from typing import List
from app.domain.entities.user import User
from app.domain.ports.user_repository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self):
        self._users = [
            User(1, "Alice"),
            User(2, "Bob")
        ]

    def get_all_users(self) -> List[User]:
        return self._users
