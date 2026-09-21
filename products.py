def add_product(products: list, name: str) -> dict:
    """
        Добавление нового товара.

        Принимает список всех продуктов и имя нового продукта.
        Генерирует новый id, создаёт словарь товара с пустым списком
        поставщиков и добавляет его в список.
        Вовзвращает словарь нового товара.
    """
    if products:
        new_id = max(product['id'] for product in products) + 1
    else:
        new_id = 1

    new_product = {
        'id': new_id,
        'name': name,
        'suppliers': []
    }

    products.append(new_product)
    return new_product


def find_product_by_name(products: list, query: str) -> list:
    """
        Поиск продукта(ов) по названию.

        Принимает список всех продуктов и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит все продукты с запросом в названии, добавяя их в список
        Возвращает список найденных продуктов.
    """
    find_products = [product for product in products if query.lower() in
                     product['name'].lower()]
    return find_products


def get_product_by_id(products: list, product_id: int) -> dict | None:
    """
        Поиск продукта по id

        Принимает список всех продуктов и id поискомого
        Находит продукт по id
        Возвращает продукт или None, если продукт не найден
    """
    for product in products:
        if product_id == product['id']:
            return product
    return None
