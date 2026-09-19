def run_cli(user_service):
    name = input("Name: ")
    email = input("Email: ")

    try:
        user = user_service.create_user(name, email)
        print(f"User created: {user}")
    except ValueError as error:
        print(f"Error: {error}")
