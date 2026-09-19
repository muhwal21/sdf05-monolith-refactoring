import json
from pathlib import Path

from ports.user_storage import UserStorage


class JsonUserStorage(UserStorage):
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_users(self):
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save_users(self, users):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)
