from models.user_type import UserType
from rep.book_repository import BookRepository
from rep.user_repository import UserRepository
from rep.borrowing_repository import BorrowingRepository
from serv.library_service import LibraryService

def main():
    # Инициализация репозиториев и сервиса
    book_repo = BookRepository()
    user_repo = UserRepository()
    borrowing_repo = BorrowingRepository()
    library = LibraryService(book_repo, user_repo, borrowing_repo)

    # Простой консольный интерфейс
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Register User")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Overdue Books")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "0":
            break
        
        elif choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre: ")  # Добавьте эту строку
            if library.add_book(title, author, isbn, genre):  # Добавьте genre
                print("Book added successfully!")
            else:
                print("Failed to add book (ISBN might already exist)")
                
        elif choice == "2":
            query = input("Enter search query: ")
            books = library.search_books(query)
            if books:
                print("\nSearch Results:")
                for book in books:
                    print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
            else:
                print("No books found")

        elif choice == "3":
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            email = input("Enter user email: ")  # Добавьте эту строку
            print("User types: 1. Student, 2. Faculty, 3. Guest")
            type_choice = input("Select user type: ")
    
            user_type = None
            if type_choice == "1":
                user_type = UserType.STUDENT
            elif type_choice == "2":
                user_type = UserType.FACULTY
            elif type_choice == "3":
                user_type = UserType.GUEST
            else:
                print("Invalid user type")
                continue
        
            if library.register_user(name, user_id, email, user_type):  # Добавьте email
                print("User registered successfully!")
            else:
                print("Failed to register user (ID might already exist)")

        elif choice == "4":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            if library.borrow_book(user_id, isbn):
                print("Book borrowed successfully!")
            else:
                print("Failed to borrow book (check user ID, ISBN, or availability)")
                
        elif choice == "5":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            if library.return_book(user_id, isbn):
                print("Book returned successfully!")
            else:
                print("Failed to return book (check user ID or ISBN)")
                
        elif choice == "6":
            overdue = library.get_overdue_books()
            if overdue:
                print("\nOverdue Books:")
                for record in overdue:
                    print(f"- ISBN: {record.isbn}, User: {record.user_id}, Due: {record.due_date.date()}")
            else:
                print("No overdue books")
                
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()