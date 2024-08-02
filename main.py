# This is a deliberately poorly implemented main script for a Library Management System.
from managers.bookManager import BooksManager
from managers.userManager import UserManager


class LibrarySystem:
    def __init__(self):
        self.books = BooksManager()
        self.users = UserManager()

    def main_menu(self) -> int:
        print("\n--------------------------------------------------")
        print("Library Management System")
        print("1. Book operations (add, search, update, checkout)")
        print("2. User Operations")
        print("3. Exit")
        print("--------------------------------------------------")
        choice = int(input("Enter choice: "))
        return choice

    def start(self):
        while True:
            choice = self.main_menu()
            if choice == 1:
                print("--------------------------------------------------")
                print("1. List Books")
                print("2. Add Book")
                print("3. Checkout Book")
                print("4. Checkin Book")
                print("5. Update Book")
                print("6. Search Book")
                print("7. Delete Book")
                print("8. Return to main menu")
                print("--------------------------------------------------")

                sub_choice = int(input("Enter choice: "))
                if sub_choice == 1:
                    self.books.list_books()
                elif sub_choice == 2:
                    self.books.add_book()
                elif sub_choice == 3:
                    self.books.checkout_book()
                elif sub_choice == 4:
                    self.books.checkin_book()
                elif sub_choice == 5:
                    self.books.update_book()
                elif sub_choice == 6:
                    self.books.search_book()
                elif sub_choice == 7:
                    self.books.delete_book()
                elif sub_choice == 8:
                    print("Exiting.")
                    continue
                else:
                    print("Invalid choice, please try again.")

            elif choice == 2:
                print("--------------------------------------------------")
                print("1. List Users")
                print("2. Get User")
                print("3. Add User")
                print("4. Update User")
                print("5. Delete User")
                print("6. Search User")
                print("7. Return to main menu")
                print("--------------------------------------------------")

                sub_choice = int(input("Enter choice: "))

                if sub_choice == 1:
                    self.users.list_users()
                elif sub_choice == 2:
                    self.users.get_user()
                elif sub_choice == 3:
                    self.users.add_user()
                elif sub_choice == 4:
                    self.users.update_user()
                elif sub_choice == 5:
                    self.users.delete_user()
                elif sub_choice == 6:
                    self.users.search()
                elif sub_choice == 7:
                    print("Exiting.")
                    continue
                else:
                    print("Invalid choice, please try again.")
            elif choice == 3:
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    library = LibrarySystem()
    library.start()
