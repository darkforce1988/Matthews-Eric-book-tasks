import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    while True:
        answer = input(f"Is that you, {username}? (yes/no): ")
        if answer == 'yes':
            print(f"Welcome back, {username}!")
            break
        if answer == 'no':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
            break
        print("Please enter 'yes' or 'no'.")


greet_user()
