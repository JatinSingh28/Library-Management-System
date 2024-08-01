from models.userModel import User
from utils.logger import setup_logger
import json

logger = setup_logger()

class UserManager:
    def __init__(self):
        self.users = []
        self.load_users()

    def load_users(self):
        try:
            with open("users_data.json", "r") as f:
                users_data = json.load(f)
                self.users = [User.from_dict(user) for user in users_data]
        except Exception as e:
            logger.error(
                f"An error occurred while loading users. Try restarting the program because some functionalities won't work: {e}"
            )

    def save_users(self):
        try:
            with open("users_data.json", "w") as f:
                json.dump([user.to_dict() for user in self.users], f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving users: {e}")

    def add_user(self):
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        try:
            new_user = User(name, user_id)
            self.users.append(new_user)
            self.save_users()
            print("User added successfully")
        except Exception as e:
            logger.error(f"An error occurred while adding user: {e}")

    def get_user(self, user_id: str = None):
        if user_id is None:
            user_id = input("Enter User ID: ")
        try:
            for user in self.users:
                if user.user_id == user_id:
                    print(user)
                    return user
            print("User not found.")
            return None
        except Exception as e:
            logger.error(f"An error occurred while getting user: {e}")
            return None

    def update_user(self):
        user_id = input("Enter User ID: ")
        user = self.get_user(user_id)
        if user:
            new_name = input("Enter new username: ")
            try:
                user.update(new_name)
                self.save_users()
                print("User updated successfully.")
            except Exception as e:
                logger.error(f"An error occurred while updating user: {e}")
        else:
            print("User not found.")

    def list_users(self):
        if(len(self.users)==0):
            print("No users found.")
            return
        print("List of Users")
        for user in self.users:
            print(user)

    def delete_user(self):
        user_id = input("Enter User ID: ")
        try:
            for user in self.users:
                if user.user_id == user_id:
                    self.users.remove(user)
                    self.save_users()
                    print("User deleted successfully.")
                    return
            print("User not found.")
        except Exception as e:
            logger.error(f"An error occurred while deleting user: {e}")

    def search(self):
        print("Search with")
        print("1. User ID")
        print("2. Name")
        try:
            choice = int(input())
            if choice == 1:
                user_id = input("Enter User ID: ")
                self.get_user(user_id)
            elif choice == 2:
                name = input("Enter name: ")
                found = False
                for user in self.users:
                    if user.name.lower() == name.lower():
                        print(user)
                        found = True
                if not found:
                    print("User not found.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            logger.error(f"An error occurred while searching for user: {e}")