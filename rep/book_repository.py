from typing import List, Dict
from rep.base_repository import BaseRepository
from models.book import Book

class BookRepository(BaseRepository[Book]):
    def __init__(self):
        self._storage: Dict[str, Book] = {}

    def add(self, book: Book) -> bool:
        if book.isbn in self._storage:
            return False
        self._storage[book.isbn] = book
        return True

    def get(self, isbn: str) -> Book:
        return self._storage.get(isbn)

    def get_all(self) -> List[Book]:
        return list(self._storage.values())

    def search(self, query: str) -> List[Book]:
        query = query.lower()
        return [book for book in self._storage.values() 
                if (query in book.title.lower() or 
                    query in book.author.lower() or 
                    query in book.isbn.lower())]