from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    available: bool = True
    checked_out_by: str = None
    checked_out_date: datetime = None

    def check_out(self, user_id: str):
        if self.available:
            self.available = False
            self.checked_out_by = user_id
            self.checked_out_date = datetime.now().isoformat()
        else:
            print("Book is not available for checkout")

    def check_in(self):
        if not self.available:
            self.available = True
            self.checked_out_by = None
            self.checked_out_date = None
        else:
            print("Book is already checked in")

    def update(self, title: str, author: str):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "checked_out_by": self.checked_out_by,
            "checked_out_date": self.checked_out_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
