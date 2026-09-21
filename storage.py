import json


def load_data(filename: str) -> list:
    """
        Загрузка данных из JSON-файла.

        Принимает путь к файлу.
        Возвращает список данных.
        Если файл не найден или повреждён — возвращает пустой список.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Начинаем с пустого списка.")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён. Начинаем с пустого списка.")
        return []


def save_data(filename: str, data: list) -> None:
    """
        Сохранение данных в JSON-файл.

        Принимает путь к файлу и список данных.
        Записывает данные с отступами и без ASCII-экранирования.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f"Не удалось сохранить: папка для {filename} не найдена.")
    except PermissionError:
        print(f"Не удалось сохранить: нет прав на запись в {filename}.")


def load_products(filename: str) -> list:
    """
        Загрузить список товаров из JSON-файла.
    """
    return load_data(filename)


def save_products(filename: str, products: list) -> None:
    """
        Сохранить список товаров в JSON-файл.
    """
    save_data(filename, products)


def load_suppliers(filename: str) -> list:
    """
        Загрузить список поставщиков из JSON-файла.
    """
    return load_data(filename)


def save_suppliers(filename: str, suppliers: list) -> None:
    """
        Сохранить список поставщиков в JSON-файл.
    """
    save_data(filename, suppliers)


def load_offers(filename: str) -> list:
    """
        Загрузить список предложений из JSON-файла.
    """
    return load_data(filename)


def save_offers(filename: str, offers: list) -> None:
    """
        Сохранить список предложений в JSON-файл.
    """
    save_data(filename, offers)


def load_users(filename: str) -> list:
    """
        Загрузить список пользователей из JSON-файла.
    """
    return load_data(filename)


def save_users(filename: str, users: list) -> None:
    """
        Сохранить список пользователей в JSON-файл.
    """
    save_data(filename, users)
