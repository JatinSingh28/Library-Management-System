from utils.logger import setup_logger
import json
from models.bookModel import Book

logger = setup_logger()


class BooksManager:
    """
    Manages a collection of books, including loading, saving, and operations on books.
    """

    def __init__(self):
        """
        Initializes the BooksManager by loading books and indices.
        """
        self.books = []
        self.load_books()
        self.load_indices()

    def load_books(self):
        """
        Loads books from a JSON file.
        Input: None
        Output: None
        """
        try:
            with open("json/books_data.json", "r") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(book) for book in books_data]
        except Exception as e:
            logger.error(
                f"An error occurred while loading books. Try restarting the program because some functionalities won't work: {e}"
            )

    def load_indices(self):
        """
        Loads title, ISBN, and author indices from JSON files.
        Input: None
        Output: None
        """
        # Loading title index
        try:
            with open("json/book_title_index.json", "r") as f:
                title_index = json.load(f)
                self.title_index = title_index
        except Exception as e:
            logger.error(
                f"An error occurred while loading title index. Try restarting the program because some functionalities won't work: {e}"
            )

        # Loading ISBN index
        try:
            with open("json/book_isbn_index.json", "r") as f:
                isbn_index = json.load(f)
                self.isbn_index = isbn_index
        except Exception as e:
            logger.error(
                f"An error occurred while loading isbn index. Try restarting the program because some functionalities won't work: {e}"
            )

        # Loading author index
        try:
            with open("json/book_author_index.json", "r") as f:
                author_index = json.load(f)
                self.author_index = author_index
        except Exception as e:
            logger.error(
                f"An error occurred while loading author index. Try restarting the program because some functionalities won't work: {e}"
            )

    def save_indices(self):
        """
        Saves title, ISBN, and author indices to JSON files.
        Input: None
        Output: None
        """
        try:
            with open("json/book_title_index.json", "w") as f:
                json.dump(self.title_index, f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving title index: {e}")

        try:
            with open("json/book_isbn_index.json", "w") as f:
                json.dump(self.isbn_index, f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving isbn index: {e}")

        try:
            with open("json/book_author_index.json", "w") as f:
                json.dump(self.author_index, f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving author index: {e}")

    def save_books(self):
        """
        Saves the current list of books to a JSON file.
        Input: None
        Output: None
        """
        try:
            with open("json/books_data.json", "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving books: {e}")

    def rebuild_indices(self):
        """
        Rebuilds all indices (ISBN, title, author) based on the current list of books.
        Input: None
        Output: None
        """
        self.isbn_index.clear()
        self.title_index.clear()
        self.author_index.clear()
        for i, book in enumerate(self.books):
            self.isbn_index[book.isbn] = i
            self.title_index[book.title.lower()] = i
            self.author_index[book.author.lower()] = i
        self.save_indices()

    def add_book(self):
        """
        Adds a new book to the collection based on user input.
        Input: None (gets input from user)
        Output: None
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        try:
            new_book = Book(title, author, isbn)
            self.isbn_index[isbn] = len(self.books)
            self.title_index[title] = len(self.books)
            self.author_index[author] = len(self.books)
            self.books.append(new_book)
            self.save_books()
            self.save_indices()
            print("Book added")
        except Exception as e:
            logger.error(f"An error occurred while adding book: {e}")

    def list_books(self):
        """
        Lists all books in the collection.
        Input: None
        Output: None
        """
        if len(self.books) == 0:
            print("No books found.")
            return

        print("List of books")
        for book in self.books:
            print(book)

    def checkout_book(self):
        """
        Checks out a book to a user based on ISBN.
        Input: None (gets input from user)
        Output: None
        """
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
        """
        Checks in a book based on ISBN.
        Input: None (gets input from user)
        Output: None
        """
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
        """
        Searches for books based on title, author, or ISBN.
        Input: None (gets input from user)
        Output: None
        """
        print("PRESS ENTER TO LEAVE EMPTY")
        title = input("Enter title: ")
        author_name = input("Enter Author name: ")
        isbn = input("Enter ISBN: ")
        if not any([title, author_name, isbn]):
            print("No search criteria provided")
            return
        try:
            if isbn is not None:
                isbn = isbn.strip()
                index = self.isbn_index[isbn]
                book = self.books[index]
                print(book)
                return
            if title is not None:
                title = title.strip()
                index = self.title_index[title]
                book = self.books[index]
                print(book)
                return
            if author_name is not None:
                author_name = author_name.strip()
                index = self.author_index[author_name]
                book = self.books[index]
                print(book)
                return

            print("Not found through indexing. Iterating though db")
            for book in self.books:
                if (
                    (title and book.title.lower() == title.lower())
                    or (author_name and book.author.lower() == author_name.lower())
                    or (isbn and book.isbn == isbn)
                ):
                    print(book)
        except Exception as e:
            logger.error(f"An error occurred while searching book: {e}")

    def update_book(self):
        """
        Updates a book's title or author based on ISBN.
        Input: None (gets input from user)
        Output: None
        """
        isbn = input("Enter ISBN: ")
        try:
            for book in self.books:
                if book.isbn == isbn:
                    new_title = input("Enter new title (press Enter to keep current): ")
                    new_author = input(
                        "Enter new author (press Enter to keep current): "
                    )
                    book.update(new_title or book.title, new_author or book.author)
                    self.save_books()
                    print("Book updated.")
                    return
            print("Book not found.")
        except Exception as e:
            logger.error(f"An error occurred while updating book: {e}")

    def delete_book(self):
        """
        Deletes a book based on ISBN.
        Input: None (gets input from user)
        Output: None
        """
        isbn = input("Enter ISBN: ")
        try:
            index = self.isbn_index[isbn]
        except Exception as e:
            logger.error(f"Book not found: {e}")
            return
        try:
            book = self.books[index]
            self.isbn_index.pop(isbn)
            self.title_index.pop(book.title)
            self.books.remove(book)
            self.save_books()
            self.rebuild_indices()
            self.save_indices()
            print("Book deleted.")
        except Exception as e:
            logger.error(f"An error occurred while deleting book: {e}")