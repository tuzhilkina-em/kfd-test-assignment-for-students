from datetime import datetime, timedelta
from models.book import Book
from models.user import User, Student, Faculty, Guest
from models.borrow import BorrowingRecord
from models.user_type import UserType
from typing import List


class LibraryService:
    def __init__(self, book_repo, user_repo, borrowing_repo):
        self.book_repo = book_repo
        self.user_repo = user_repo
        self.borrowing_repo = borrowing_repo

    def add_book(self, title: str, author: str, isbn: str, genre: str) -> bool:
        book = Book(title, author, isbn, genre)  
        return self.book_repo.add(book)

    def find_book(self, isbn: str) -> Book:
        return self.book_repo.get(isbn)

    def search_books(self, query: str) -> List[Book]:
        return self.book_repo.search(query)
    

    def register_user(self, name: str, user_id: str, email: str, user_type: UserType) -> bool:
        if user_type == UserType.STUDENT:
            user = Student(name, user_id, email)  
        elif user_type == UserType.FACULTY:
            user = Faculty(name, user_id, email)  
        else:
            user = Guest(name, user_id, email)
        return self.user_repo.add(user)

    def find_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def borrow_book(self, user_id: str, isbn: str) -> bool:
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        
        if not user or not book or not book.available or not user.can_borrow():
            return False
        
        book.available = False
        user.borrow_book(isbn)
        
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=user.get_borrow_days())
        record = BorrowingRecord(user_id, isbn, borrow_date, due_date)
        
        return self.borrowing_repo.add(record)

    def return_book(self, user_id: str, isbn: str) -> bool:
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        
        if not user or not book or isbn not in user.borrowed_books:
            return False
        
        book.available = True
        user.return_book(isbn)
        return True

    def get_overdue_books(self) -> List[BorrowingRecord]:
        return self.borrowing_repo.get_overdue()