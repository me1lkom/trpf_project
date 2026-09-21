import json


def load_products(filename: str) -> list:
    """
    Загрузить список товаров из JSON-файла.

    Принимает путь к файлу.
    Возвращает список товаров.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Файл {filename} не найден! Начинаем с пустого списка.')
        return []
    except json.JSONDecodeError:
        print(f'Файл {filename} повреждён! Начинаем с пустого списка.')
        return []


def save_products(filename: str, products: list) -> None:
    """
    Сохранить список товаров в JSON-файл.

    Принимает путь к файлу и список товаров.
    Записывает данные.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f'Не удалось сохранить: папка для файла {filename} не найдена.')
    except PermissionError:
        print(f'Не удалось сохранить: нет прав на запись в {filename}.')
