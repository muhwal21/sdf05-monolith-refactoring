from domain.user import create_user


class UserService:
    def __init__(self, storage):
        self.storage = storage

    def create_user(self, name, email):
        users = self.storage.load_users()
        user = create_user(name, email, users)
        users.append(user)
        self.storage.save_users(users)
        return user

    def list_users(self):
        return self.storage.load_users()
