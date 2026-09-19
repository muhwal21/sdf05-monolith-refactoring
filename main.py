from pathlib import Path

from adapters.json_user_storage import JsonUserStorage
from application.user_service import UserService
from interfaces.cli import run_cli


DATA_FILE = Path(__file__).with_name("users.json")


def main():
    storage = JsonUserStorage(DATA_FILE)
    user_service = UserService(storage)
    run_cli(user_service)


if __name__ == "__main__":
    main()
