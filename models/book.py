class Book:
    def __init__(self, title: str, author: str, isbn: str, genre: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self._available = True

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    def available(self, value: bool):
        self._available = value

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Borrowed'}"