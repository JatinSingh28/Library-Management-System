from utils.logger import setup_logger
import json
from models.bookModel import Book

logger = setup_logger()

class BooksManager:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("books_data.json", "r") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(book) for book in books_data]
        except Exception as e:
            logger.error(
                f"An error occurred while loading books. Try restarting the program because some functionalities won't work: {e}"
            )

    def save_books(self):
        try:
            with open("books_data.json", "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving books: {e}")

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        try:
            new_book = Book(title, author, isbn)
            self.books.append(new_book)
            self.save_books()
            print("Book added")
        except Exception as e:
            logger.error(f"An error occurred while adding book: {e}")

    def list_books(self):
        if(len(self.books)==0):
            print("No books found.")
            return

        print("List of books")
        for book in self.books:
            print(book)

    def checkout_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        try:
            for book in self.books:
                if book.isbn == isbn:
                    book.check_out(user_id)
                    self.save_books()
                    print("Book checked out.")
                    return
            print("Book not found.")
        except Exception as e:
            logger.error(f"An error occurred while checking out book: {e}")
            
    def checkin_book(self):
        isbn = input("Enter ISBN of the book to checkin: ")
        try:
            for book in self.books:
                if book.isbn == isbn:
                    book.check_in()
                    self.save_books()
                    print("Book checked in.")
                    return
            print("Book not found.")
        except Exception as e:
            logger.error(f"An error occurred while checking in book: {e}")
            
    def search_book(self):
        print("PRESS ENTER TO LEAVE EMPTY")
        title = input("Enter title: ")
        author_name = input("Enter Author name: ")
        isbn = input("Enter ISBN: ")
        if not any([title, author_name, isbn]):
            print("No search criteria provided")
            return
        try:
            for book in self.books:
                if (title and book.title.lower() == title.lower()) or \
                   (author_name and book.author.lower() == author_name.lower()) or \
                   (isbn and book.isbn == isbn):
                    print(book)
        except Exception as e:
            logger.error(f"An error occurred while searching book: {e}")

    def update_book(self):
        isbn = input("Enter ISBN: ")
        try:
            for book in self.books:
                if book.isbn == isbn:
                    new_title = input("Enter new title (press Enter to keep current): ")
                    new_author = input("Enter new author (press Enter to keep current): ")
                    book.update(new_title or book.title, new_author or book.author)
                    self.save_books()
                    print("Book updated.")
                    return
            print("Book not found.")
        except Exception as e:
            logger.error(f"An error occurred while updating book: {e}")

    def delete_book(self):
        isbn = input("Enter ISBN: ")
        try:
            for book in self.books:
                if book.isbn == isbn:
                    self.books.remove(book)
                    self.save_books()
                    print("Book deleted.")
                    return
            print("Book not found.")
        except Exception as e:
            logger.error(f"An error occurred while deleting book: {e}")