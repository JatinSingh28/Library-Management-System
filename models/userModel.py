from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    user_id: str
    borrowed_books: List[str] = field(default_factory=list)

    def borrow_book(self, book_isbn: str):
        if book_isbn not in self.borrowed_books:
            self.borrowed_books.append(book_isbn)
        else:
            print("User has already borrowed this book")

    def return_book(self, book_isbn: str):
        if book_isbn in self.borrowed_books:
            self.borrowed_books.remove(book_isbn)
        else:
            print("User has not borrowed this book")
        
    def update(self, name: str):
        self.name = name
        
    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"
    