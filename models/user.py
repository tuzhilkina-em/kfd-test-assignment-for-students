from abc import ABC, abstractmethod
from .user_type import UserType

class User(ABC):
    def __init__(self, name: str, user_id: str, email: str):
        self.name = name
        self.user_id = user_id
        self.email = email
        self._borrowed_books = []

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books

    @abstractmethod
    def get_max_books(self) -> int:
        pass

    @abstractmethod
    def get_borrow_days(self) -> int:
        pass

    @abstractmethod
    def get_fine_per_day(self) -> float:
        pass

    def can_borrow(self) -> bool:
        return len(self._borrowed_books) < self.get_max_books()

    def borrow_book(self, isbn: str) -> bool:
        if self.can_borrow():
            self._borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn: str) -> bool:
        if isbn in self._borrowed_books:
            self._borrowed_books.remove(isbn)
            return True
        return False

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (ID: {self.user_id}) - {len(self._borrowed_books)}/{self.get_max_books()} books borrowed"

class Student(User):
    def get_max_books(self) -> int:
        return 3

    def get_borrow_days(self) -> int:
        return 14

    def get_fine_per_day(self) -> float:
        return 0.50

class Faculty(User):
    def get_max_books(self) -> int:
        return 10

    def get_borrow_days(self) -> int:
        return 30

    def get_fine_per_day(self) -> float:
        return 0.20

class Guest(User):
    def get_max_books(self) -> int:
        return 1

    def get_borrow_days(self) -> int:
        return 7

    def get_fine_per_day(self) -> float:
        return 1.00