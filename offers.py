def add_offer(offers: list, product_id: int, supplier_id: int,
              price: float, min_lots: int, delivery_time_days: int) -> dict:
    """
        Добавление нового предложения.

        Принимает список всех предложений, id товара, id поставщика,
        цену, минимальную партию и срок доставки.
        Генерирует новый id, создаёт словарь предложения
        и добавляет его в список.
        Возвращает словарь нового предложения.
    """
    if offers:
        new_id = max(offer['id'] for offer in offers) + 1
    else:
        new_id = 1

    new_offer = {
        'id': new_id,
        'product_id': product_id,
        'supplier_id': supplier_id,
        'price': price,
        'min_lots': min_lots,
        'delivery_time_days': delivery_time_days
    }

    offers.append(new_offer)
    return new_offer


def find_offers_by_product(offers: list, product_id: int) -> list:
    """
        Поиск предложений по id товара.

        Принимает список всех предложений и id товара.
        Находит все предложения, относящиеся к этому товару.
        Возвращает список найденных предложений.
    """
    find_offers = [offer for offer in offers if
                   product_id == offer['product_id']]
    return find_offers


def find_offers_by_supplier(offers: list, supplier_id: int) -> list:
    """
        Поиск предложений по id поставщика.

        Принимает список всех предложений и id поставщика.
        Находит все предложения, относящиеся к этому поставщику.
        Возвращает список найденных предложений.
    """
    find_offers = [offer for offer in offers if
                   supplier_id == offer['supplier_id']]
    return find_offers


def filter_offers_by_price(offers: list, product_id: int,
                           max_price: float) -> list:
    """
        Фильтр предложений по максимальной цене.

        Принимает список всех предложений, id товара и максимальную цену.
        Отбирает предложения по товару с ценой не выше max_price.
        Возвращает список подходящих предложений.
    """
    filtered_offers = []
    for offer in offers:
        if offer['product_id'] == product_id and offer['price'] <= max_price:
            filtered_offers.append(offer)
    return filtered_offers


def filter_offers_by_delivery(offers: list, product_id: int,
                              max_days: int) -> list:
    """
        Фильтр предложений по максимальному сроку доставки.

        Принимает список всех предложений, id товара и максимальный срок.
        Отбирает предложения по товару со сроком доставки не больше max_days.
        Возвращает список подходящих предложений.
    """
    filtered_offers = []
    for offer in offers:
        if (offer['product_id'] == product_id
                and offer['delivery_time_days'] <= max_days):
            filtered_offers.append(offer)
    return filtered_offers


def sort_offers_by_price(offers: list, product_id: int) -> list:
    """
        Сортировка предложений по цене.

        Принимает список всех предложений и id товара.
        Находит предложения по товару и сортирует их по цене
        по возрастанию.
        Возвращает новый отсортированный список предложений.
    """
    sorted_offers = find_offers_by_product(offers, product_id)
    sorted_suppliers_list = sorted(sorted_offers,
                                   key=lambda offer: offer['price'])
    return sorted_suppliers_list


def compare_prices(offers: list, product_id: int) -> dict | None:
    """
        Поиск лучшего предложения по цене.

        Принимает список всех предложений и id товара.
        Находит предложение с минимальной ценой по этому товару.
        Возвращает предложение с минимальной ценой
        или None, если предложений по товару нет.
    """
    product_offers = find_offers_by_product(offers, product_id)
    if not product_offers:
        return None
    return min(product_offers, key=lambda offer: offer['price'])


def check_min_lot(offer: dict, quantity: int) -> bool:
    """
        Проверка минимальной партии предложения.

        Принимает словарь предложения и количество товара.
        Возвращает True, если количество не меньше минимальной
        партии, иначе False.
    """
    return offer['min_lots'] <= quantity


def calculate_order_price(offer: dict, quantity: int) -> float:
    """
        Расчёт стоимости заказа по предложению.

        Принимает словарь предложения и количество товара.
        Перемножает цену предложения на количество.
        Возвращает итоговую стоимость заказа.
    """
    return offer['price'] * quantity
