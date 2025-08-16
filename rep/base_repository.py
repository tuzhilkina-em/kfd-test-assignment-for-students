from abc import ABC, abstractmethod
from typing import Dict, List, TypeVar, Generic

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, item: T) -> bool:
        pass

    @abstractmethod
    def get(self, id: str) -> T:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass