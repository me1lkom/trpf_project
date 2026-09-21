from users import add_user, find_user_by_name


def test_add_user():
    """
        Добавление пользователя увеличивает список на 1.
    """
    users = []
    add_user(users, 'Лев Герасимов', 'lev@example.com')
    assert len(users) == 1


def test_find_user_by_name():
    """
        Поиск находит пользователя по подстроке.
    """
    users = []
    add_user(users, 'Лев Герасимов', 'lev@example.com')
    found = find_user_by_name(users, 'лев')
    assert len(found) == 1
