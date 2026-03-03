from storage import load_users, save_users


class AuthService:
    def __init__(self):
        self.users = load_users()

    def register(self, username, password):
        # BUG: allows duplicate usernames
        self.users[username] = password  # BUG: stores plain-text password
        save_users(self.users)
        return True

    def login(self, username, password):
        # BUG: crashes if username does not exist
        return self.users[username] == password