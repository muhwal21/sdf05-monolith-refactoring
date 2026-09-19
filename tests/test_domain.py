import pytest

from domain.user import create_user, validate_user


def test_validate_user_normalizes_input():
    user = validate_user(" Alice ", "ALICE@example.com")

    assert user == {
        "name": "Alice",
        "email": "alice@example.com",
    }


def test_validate_user_rejects_empty_name():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        validate_user("   ", "alice@example.com")


def test_validate_user_rejects_invalid_email():
    with pytest.raises(ValueError, match="Invalid email"):
        validate_user("Alice", "invalid-email")


def test_create_user_rejects_duplicate_email():
    existing_users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"}
    ]

    with pytest.raises(ValueError, match="Email already exists"):
        create_user("Another Alice", "ALICE@example.com", existing_users)
