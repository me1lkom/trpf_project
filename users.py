def add_user(users: list, name: str, email: str) -> dict:
    """
        Добавление нового пользователя.

        Принимает список всех пользователей, имя и email
        нового пользователя.
        Генерирует новый id, создаёт словарь пользователя
        и добавляет его в список.
        Возвращает словарь нового пользователя.
    """
    if users:
        new_id = max(user['id'] for user in users) + 1
    else:
        new_id = 1

    new_user = {
        'id': new_id,
        'name': name,
        'email': email,
    }

    users.append(new_user)
    return new_user


def find_user_by_name(users: list, query: str) -> list:
    """
        Поиск пользователя(ей) по имени.

        Принимает список всех пользователей и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит всех пользователей с запросом в имени, добавляя их в список.
        Возвращает список найденных пользователей.
    """
    find_users = [user for user in users if query.lower() in
                  user['name'].lower()]

    return find_users


def get_user_by_id(users: list, user_id: int) -> dict | None:
    """
        Поиск пользователя по id.

        Принимает список всех пользователей и id искомого.
        Находит пользователя по id.
        Возвращает пользователя или None, если пользователь не найден.
    """
    for user in users:
        if user_id == user['id']:
            return user
    return None
