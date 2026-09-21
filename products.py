def add_product(products: list, name: str,
                description: str, country: str) -> dict:
    """
        Добавление нового товара.

        Принимает список всех товаров, а также имя, описание и
        страну производства нового товара.
        Генерирует новый id, создаёт словарь товара
        и добавляет его в список.
        Возвращает словарь нового товара.
    """
    if products:
        new_id = max(product['id'] for product in products) + 1
    else:
        new_id = 1

    new_product = {
        'id': new_id,
        'name': name,
        'description': description,
        'country': country
    }

    products.append(new_product)
    return new_product


def find_product_by_name(products: list, query: str) -> list | None:
    """
        Поиск товара(ов) по названию.

        Принимает список всех товаров и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит все товары с запросом в названии, добавляя их в список.
        Возвращает список найденных товаров.
    """
    find_products = [product for product in products if query.lower() in
                     product['name'].lower()]
    return find_products


def get_product_by_id(products: list, product_id: int) -> dict | None:
    """
        Поиск товара по id.

        Принимает список всех товаров и id искомого.
        Находит товар по id.
        Возвращает товар или None, если товар не найден.
    """
    for product in products:
        if product_id == product['id']:
            return product
    return None
