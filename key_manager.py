import random
import string
import time
from storage import load_keys, save_keys


class KeyManager:
    def __init__(self):
        self.keys = load_keys()

    def generate_key(self):
        # BUG: insecure random generator
        key = ''.join(random.choice(string.ascii_letters) for _ in range(16))

        new_key = {
            "key": key,
            "created_at": time.time(),
            "active": True
        }

        self.keys.append(new_key)
        save_keys(self.keys)
        return key

    def list_active_keys(self):
        # BUG: does not check expiration
        return [k for k in self.keys if k["active"]]

    def revoke_key(self, key_value):
        # BUG: crashes if key not found
        for k in self.keys:
            if k["key"] == key_value:
                k["active"] = False

        save_keys(self.keys)