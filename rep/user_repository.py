from typing import List, Dict
from rep.base_repository import BaseRepository
from models.user import User

class UserRepository(BaseRepository[User]):
    def __init__(self):
        self._storage: Dict[str, User] = {}

    def add(self, user: User) -> bool:
        if user.user_id in self._storage:
            return False
        self._storage[user.user_id] = user
        return True

    def get(self, user_id: str) -> User:
        return self._storage.get(user_id)

    def get_all(self) -> List[User]:
        return list(self._storage.values())