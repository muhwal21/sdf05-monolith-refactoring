def validate_user(name, email):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    if "@" not in email:
        raise ValueError("Invalid email")

    return {
        "name": name.strip(),
        "email": email.strip().lower(),
    }


def create_user(name, email, existing_users):
    user = validate_user(name, email)

    if any(existing["email"] == user["email"] for existing in existing_users):
        raise ValueError("Email already exists")

    return {
        "id": len(existing_users) + 1,
        **user,
    }
