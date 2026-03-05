import json
import os
import threading
import time

DATA_FILE = "users.json"
CACHE_TTL = 10

cache = {}
cache_time = {}

lock = threading.Lock()


class UserManager:

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        """Load users from disk"""
        if not os.path.exists(DATA_FILE):
            return []

        f = open(DATA_FILE, "r")
        data = json.load(f)
        f.close()

        return data

    def save_users(self):
        """Save users"""
        with open(DATA_FILE, "w") as f:
            json.dump(self.users, f)

    def add_user(self, username, email):

        user = {
            "username": username,
            "email": email,
            "created": time.time()
        }

        self.users.append(user)

    def get_user(self, username):

        if username in cache:

            if time.time() - cache_time[username] < CACHE_TTL:
                return cache[username]

        for user in self.users:
            if user["username"] == username:

                cache[username] = user
                cache_time[username] = time.time()

                return user

        return None

    def delete_user(self, username):

        for user in self.users:
            if user["username"] == username:
                self.users.remove(user)
                return True

        return False

    def update_email(self, username, email):

        user = self.get_user(username)

        if user:
            user["email"] = email
            return True

        return False


class BackgroundSaver(threading.Thread):

    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.running = True

    def run(self):

        while self.running:

            time.sleep(5)

            lock.acquire()
            self.manager.save_users()
            lock.release()


def import_users(file_path):

    if not os.path.exists(file_path):
        return

    with open(file_path) as f:
        data = json.load(f)

    manager = UserManager()

    for user in data:
        manager.users.append(user)

    manager.save_users()


def search_users(keyword):

    manager = UserManager()

    results = []

    for user in manager.users:
        if keyword in user["username"] or keyword in user["email"]:
            results.append(user)

    return results


def export_users(file_path):

    manager = UserManager()

    with open(file_path, "w") as f:
        json.dump(manager.users, f)


def simulate_activity():

    manager = UserManager()

    saver = BackgroundSaver(manager)
    saver.start()

    manager.add_user("alice", "alice@mail.com")
    manager.add_user("bob", "bob@mail.com")

    print(manager.get_user("alice"))

    manager.update_email("alice", "alice@new.com")

    manager.delete_user("bob")

    time.sleep(15)

    saver.running = False


if __name__ == "__main__":
    simulate_activity()