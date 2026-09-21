def add_supplier_to_product(product: dict, name: str,
                            price: float, delivery_time_days: int,
                            min_lots: int, phone: str) -> dict:
    """
        Добавляем поставщика к товару.

        Принимаем словарь товара и данные поставщика.
        Создаём словарь поставщика и добавляем его в список товара.
        Возвращаем список товара.
    """
    new_supplier = {
        'name': name,
        'price': price,
        'delivery_time_days': delivery_time_days,
        'min_lots': min_lots,
        'phone': phone
    }

    product['suppliers'].append(new_supplier)
    return product


def find_suppliers_by_name(product: dict, query: str) -> list:
    """
        Поиск поставщика(ов) по названию.

        Принимает словарь товара и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит всех поставщиков с запросом в названии, добавяя их в список
        Возвращает список найденных продуктов.
    """
    find_suppliers = [supplier for supplier in product if query.lower() in
                      supplier['name'].lower()]
    return find_suppliers


def filter_suppliers_by_price(product: dict, max_price: float) -> list:
    """
        Фильтр по цене.

        Принимает словарь товара и максимальную цену.
        Создаёт пустой список для поставщиков, просматривает всех
        поставщиков у товара сверяя цену с максимальной,
        добавляет в список, если цена удовлетворяет.
        Возвращает список поставщиков с удовлетворяющей ценой.
    """
    filtered_suppliers = []
    for supplier in product['suppliers']:
        if supplier['price'] <= max_price:
            filtered_suppliers.append(supplier)
    return filtered_suppliers


def filter_suppliers_by_delivery(product: dict, max_days: int) -> list:
    """
        Фильтр по сроку доставки.

        Принимает словарь товара и максимальное количество дней доставки.
        Создаёт пустой список для поставщиков, просматривает всех
        поставщиков у товара сверяя количество дней с максимальным,
        добавляет в список, если количество дней удовлетворяет.
        Возвращает список поставщиков с удовлетворяющим
        количеством дней доставки.
    """
    filtered_suppliers = []
    for supplier in product['suppliers']:
        if supplier['delivery_time_days'] <= max_days:
            filtered_suppliers.append(supplier)
    return filtered_suppliers


def sort_suppliers_by_price(product: dict) -> list:
    """
        Сортировка поставщиков по цене.

        Принимает словарь товара.
        Сортирует поставщиков по цене.
        Возвращает отрортированный список поставщиков.
    """
    sorted_suppliers_list = sorted(product['suppliers'],
                                   key=lambda supplier: supplier['price'])
    return sorted_suppliers_list


def compare_prices(product: dict) -> dict | None:
    """
        Поиск лучшего по цене предложение от поставщика.

        Принимает словарь товара.
        Проверяет наличие поставщиков, ищет поставщика с минимальной ценой.
        Возвращает словарь поствщика.
    """
    if not product['suppliers']:
        return None

    return min(product['suppliers'], key=lambda supplier: supplier['price'])


def check_min_lot(supplier: dict, quantity: int) -> bool:
    """
        Проверка минимальной мартии поставщика с нужной к заказу.

        Принимает словарь поставщика и необходимое количество товара.
        Проверяет минимальную партию поставщика и нужную партию к заказу.
        Возвразает ответ True или False.
    """
    return supplier['min_lots'] <= quantity


def calculate_order_price(supplier: dict, quantity: int) -> float:
    """
        Расчёт стоимости заказа.

        Принимает словарь поставщика и количество товара к заказу.
        Перемножает цену поставщика на количество товара.
        Возвращает сумму заказа.
    """
    return supplier['price'] * quantity
