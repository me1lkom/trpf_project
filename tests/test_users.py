from models.users import add_user, find_user_by_name
from models.users import User


def test_add_user():
    """Добавление пользователя возвращает объект User."""
    users = []
    user = add_user(users, 'Лев Герасимов', 'lev@example.com')
    assert isinstance(user, User)
    assert user.name == 'Лев Герасимов'
    assert user.email == 'lev@example.com'


def test_find_user_by_name():
    """Поиск находит пользователя по подстроке."""
    users = []
    add_user(users, 'Лев Герасимов', 'lev@example.com')
    found = find_user_by_name(users, 'лев')
    assert len(found) == 1
    assert found[0].name == 'Лев Герасимов'
