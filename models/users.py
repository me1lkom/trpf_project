class User:
    """
        Пользователи.
    """
    def __init__(
        self,
        user_id: int,
        name: str,
        email: str
    ) -> None:
        """
            Создание объекта класса.

            Принимает id, имя и email пользователя.
        """
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        """
            Возвращение строкового представления пользователя.
        """
        return f'{self.name} ({self.email})'

    @classmethod
    def from_data(cls, data: dict) -> 'User':
        """
            Создание пользователя из словаря JSON.

            Принимает словарь с пользователем.
            Возвращает объект User.
        """
        return cls(
            data['id'],
            data['name'],
            data['email'],
        )


def add_user(users: list[User], name: str, email: str) -> User:
    """
        Добавление нового пользователя.

        Принимает список всех пользователей, имя и email
        нового пользователя.
        Генерирует новый id, создаёт объект пользователя
        и добавляет его в список.
        Возвращает объект нового пользователя.
    """
    if users:
        new_id = max(user.id for user in users) + 1
    else:
        new_id = 1

    new_user = User(new_id, name, email)

    users.append(new_user)
    return new_user


def find_user_by_name(users: list[User], query: str) -> list[User]:
    """
        Поиск пользователя(ей) по имени.

        Принимает список всех пользователей и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит всех пользователей с запросом в имени, добавляя их в список.
        Возвращает список найденных пользователей.
    """
    find_users = [user for user in users if query.lower() in
                  user.name.lower()]

    return find_users


def get_user_by_id(users: list[User], user_id: int) -> User | None:
    """
        Поиск пользователя по id.

        Принимает список всех пользователей и id искомого.
        Находит пользователя по id.
        Возвращает объект пользователя или None, если пользователь не найден.
    """
    for user in users:
        if user_id == user.id:
            return user
    return None
