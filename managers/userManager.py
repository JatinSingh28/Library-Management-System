from models.userModel import User
from utils.logger import setup_logger
import json

logger = setup_logger()


class UserManager:
    """
    A class to manage user data, including loading, saving, and manipulating user information.
    """

    def __init__(self):
        """
        Initialize the UserManager, load users and indices.
        """
        self.users = []
        self.load_users()
        self.load_indices()

    def load_users(self):
        """
        Load user data from a JSON file.
        
        Input: None
        Output: None
        """
        try:
            with open("json/users_data.json", "r") as f:
                users_data = json.load(f)
                self.users = [User.from_dict(user) for user in users_data]
        except Exception as e:
            logger.error(
                f"An error occurred while loading users. Try restarting the program because some functionalities won't work: {e}"
            )

    def load_indices(self):
        """
        Load user indices (by name and ID) from JSON files.
        
        Input: None
        Output: None
        """
        try:
            with open("json/user_name_index.json", "r") as f:
                name_index = json.load(f)
                self.name_index = name_index
        except Exception as e:
            logger.error(
                f"An error occurred while loading name index. Try restarting the program because some functionalities won't work: {e}"
            )
        try:
            with open("json/user_id_index.json", "r") as f:
                id_index = json.load(f)
                self.id_index = id_index
        except Exception as e:
            logger.error(
                f"An error occurred while loading id index. Try restarting the program because some functionalities won't work: {e}"
            )

    def rebuild_indices(self):
        """
        Rebuild user indices based on current user data.
        
        Input: None
        Output: None
        """
        self.name_index = {}
        self.id_index = {}
        for i, user in enumerate(self.users):
            self.name_index[user.name] = i
            self.id_index[user.user_id] = i
        self.save_indices()

    def save_indices(self):
        """
        Save user indices to JSON files.
        
        Input: None
        Output: None
        """
        try:
            with open("json/user_name_index.json", "w") as f:
                json.dump(self.name_index, f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving name index: {e}")
        try:
            with open("json/user_id_index.json", "w") as f:
                json.dump(self.id_index, f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving id index: {e}")

    def save_users(self):
        """
        Save user data to a JSON file.
        
        Input: None
        Output: None
        """
        try:
            with open("json/users_data.json", "w") as f:
                json.dump([user.to_dict() for user in self.users], f, indent=2)
        except Exception as e:
            logger.error(f"An error occurred while saving users: {e}")

    def add_user(self):
        """
        Add a new user to the system.
        
        Input: None (prompts user for input)
        Output: None
        """
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        try:
            new_user = User(name, user_id)
            self.name_index[name] = len(self.users)
            self.id_index[user_id] = len(self.users)
            self.users.append(new_user)
            self.save_users()
            self.save_indices()
            print("User added successfully")
        except Exception as e:
            logger.error(f"An error occurred while adding user: {e}")

    def get_user(self, user_id: str = None):
        """
        Retrieve a user by their ID.
        
        Input: user_id (str, optional) - if not provided, prompts for input
        Output: User object if found, None otherwise
        """
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
        """
        Update a user's information.
        
        Input: None (prompts user for input)
        Output: None
        """
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
        """
        List all users in the system.
        
        Input: None
        Output: None
        """
        if len(self.users) == 0:
            print("No users found.")
            return
        print("List of Users")
        for user in self.users:
            print(user)

    def delete_user(self):
        """
        Delete a user from the system.
        
        Input: None (prompts user for input)
        Output: None
        """
        user_id = input("Enter User ID: ")
        try:
            index = self.id_index[user_id]
        except Exception as e:
            logger.error(f"User not found: {e}")
            return
        try:
            user = self.users[index]
            self.name_index.pop(user.name)
            self.id_index.pop(user_id)
            self.users.remove(user)
            self.rebuild_indices()
            self.save_users()
            self.save_indices()
            print("User deleted successfully.")
        except Exception as e:
            logger.error(f"An error occurred while deleting user: {e}")

    def search(self):
        """
        Search for a user by ID or name.
        
        Input: None (prompts user for input)
        Output: None
        """
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