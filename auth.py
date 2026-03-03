from storage import load_users, save_users
import hashlib

def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class AuthService:
    def __init__(self):
        self.users = load_users()

    def register(self, username, password):
        if username in self.users:
            print("Error: Username already exists.")
            return False

        self.users[username] = hash_password(password)
        save_users(self.users)
        return True


    def login(self, username, password):
        if username not in self.users:
            return False

        return self.users[username] == hash_password(password)

    def reset_password(self, username, new_password):
        """
        Resets password for existing user.
        """
        if username not in self.users:
            print("Error: User does not exist.")
            return False

        self.users[username] = new_password

        save_users(self.users)
        return True