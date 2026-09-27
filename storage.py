import json
from models import Product, Supplier, Offer, User
from models.products import get_product_by_id
from models.suppliers import get_supplier_by_id


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
        print(f'Файл {filename} не найден. Начинаем с пустого списка.')
        return []
    except json.JSONDecodeError:
        print(f'Файл {filename} повреждён. Начинаем с пустого списка.')
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
        print(f'Не удалось сохранить: папка для {filename} не найдена.')
    except PermissionError:
        print(f'Не удалось сохранить: нет прав на запись в {filename}.')


def load_products(filename: str) -> list[Product]:
    """
        Загрузить товары из JSON-файла.
    """
    data = load_data(filename)
    return [Product.from_data(item) for item in data]


def save_products(filename: str, products: list[Product]) -> None:
    """
        Сохранить товары в JSON-файл.
    """
    data = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'country': product.country
        }
        for product in products
    ]
    save_data(filename, data)


def load_suppliers(filename: str) -> list[Supplier]:
    """
        Загрузить список поставщиков из JSON-файла.
    """
    data = load_data(filename)
    return [Supplier.from_data(item) for item in data]


def save_suppliers(filename: str, suppliers: list[Supplier]) -> None:
    """
        Сохранить список поставщиков в JSON-файл.
    """
    data = [
        {
            'id': supplier.id,
            'name': supplier.name,
            'inn': supplier.inn,
            'phone': supplier.phone,
            'email': supplier.email
        }
        for supplier in suppliers
    ]
    save_data(filename, data)


def load_offers(
    filename: str,
    products: list[Product],
    suppliers: list[Supplier]
) -> list[Offer]:
    """
        Загрузить предложения из JSON-файла.
    """
    data = load_data(filename)
    offers = []
    for item in data:
        product = get_product_by_id(products, item['product_id'])
        supplier = get_supplier_by_id(suppliers, item['supplier_id'])
        if not product or not supplier:
            continue
        offer = Offer(
            item['id'],
            product,
            supplier,
            item['price'],
            item['min_lots'],
            item['delivery_time_days']
        )
        offers.append(offer)
    return offers


def save_offers(filename: str, offers: list[Offer]) -> None:
    """
        Сохранить предложения в JSON-файл.
    """
    data = [
        {
            'id': o.id,
            'product_id': o.product.id,
            'supplier_id': o.supplier.id,
            'price': o.price,
            'min_lots': o.min_lots,
            'delivery_time_days': o.delivery_time_days
        }
        for o in offers
    ]
    save_data(filename, data)


def load_users(filename: str) -> list[User]:
    """
        Загрузить список пользователей из JSON-файла.
    """
    data = load_data(filename)
    return [User.from_data(item) for item in data]


def save_users(filename: str, users: list[User]) -> None:
    """
        Сохранить список пользователей в JSON-файл.
    """
    data = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        for user in users
    ]
    save_data(filename, data)
