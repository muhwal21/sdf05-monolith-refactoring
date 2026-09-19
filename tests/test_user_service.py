from application.user_service import UserService
from ports.user_storage import UserStorage


class FakeUserStorage(UserStorage):
    def __init__(self, users=None):
        self.users = list(users or [])

    def load_users(self):
        return list(self.users)

    def save_users(self, users):
        self.users = list(users)


def test_create_user_saves_through_storage_interface():
    storage = FakeUserStorage()
    service = UserService(storage)

    user = service.create_user("Budi", "BUDI@example.com")

    assert user == {
        "id": 1,
        "name": "Budi",
        "email": "budi@example.com",
    }
    assert storage.users == [user]


def test_list_users_reads_from_storage_interface():
    existing_users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"}
    ]
    service = UserService(FakeUserStorage(existing_users))

    assert service.list_users() == existing_users
