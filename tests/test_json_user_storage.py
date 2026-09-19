from adapters.json_user_storage import JsonUserStorage


def test_json_storage_returns_empty_list_when_file_does_not_exist(tmp_path):
    storage = JsonUserStorage(tmp_path / "users.json")

    assert storage.load_users() == []


def test_json_storage_saves_and_loads_users(tmp_path):
    file_path = tmp_path / "users.json"
    storage = JsonUserStorage(file_path)
    users = [
        {"id": 1, "name": "Citra", "email": "citra@example.com"}
    ]

    storage.save_users(users)

    assert storage.load_users() == users
