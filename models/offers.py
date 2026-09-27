from models.products import Product
from models.suppliers import Supplier


class Offer:
    """
        Предложение.
    """
    def __init__(
        self,
        offer_id: int,
        product: Product,
        supplier: Supplier,
        price: float,
        min_lots: int,
        delivery_time_days: int,
    ) -> None:
        """
            Создание объекта класса.

            Принимает id, товар, поставщик, цену,
            минимальную партию и количество дней доставки.
        """
        self.id = offer_id
        self.product = product
        self.supplier = supplier
        self.price = price
        self.min_lots = min_lots
        self.delivery_time_days = delivery_time_days

    def __str__(self) -> str:
        """
            Возвращение строкового представления предложения.
        """
        return f'{self.product}, {self.supplier} ({self.price})'

    def check_min_lot(self, quantity: int) -> bool:
        """
            Проверка минимальной партии предложения.

            Принимает количество товара.
            Возвращает True, если количество не меньше минимальной
            партии, иначе False.
        """
        return self.min_lots <= quantity

    def calculate_order_price(self, quantity: int) -> float:
        """
            Расчёт стоимости заказа по предложению.

            Принимает количество товара.
            Перемножает цену предложения на количество.
            Возвращает итоговую стоимость заказа.
        """
        return self.price * quantity


def add_offer(offers: list[Offer], product: Product, supplier: Supplier,
              price: float, min_lots: int, delivery_time_days: int) -> Offer:
    """
        Добавление нового предложения.

        Принимает список всех предложений, объект товара, объект поставщика,
        цену, минимальную партию и срок доставки.
        Генерирует новый id, создаёт словарь предложения
        и добавляет его в список.
        Возвращает словарь нового предложения.
    """
    if offers:
        new_id = max(offer.id for offer in offers) + 1
    else:
        new_id = 1

    new_offer = Offer(new_id, product, supplier,
                      price, min_lots, delivery_time_days)

    offers.append(new_offer)
    return new_offer


def find_offers_by_product(offers: list[Offer],
                           product: Product) -> list[Offer]:
    """
        Поиск предложений по id товара.

        Принимает список всех предложений и объект товара.
        Находит все предложения, относящиеся к этому товару.
        Возвращает список найденных предложений.
    """
    find_offers = [offer for offer in offers if
                   offer.product.id == product.id]
    return find_offers


def find_offers_by_supplier(offers: list[Offer],
                            supplier: Supplier) -> list[Offer]:
    """
        Поиск предложений по id поставщика.

        Принимает объект всех предложений и объект поставщика.
        Находит все предложения, относящиеся к этому поставщику.
        Возвращает список найденных предложений.
    """
    find_offers = [offer for offer in offers if
                   supplier == offer.supplier]
    return find_offers


def filter_offers_by_price(offers: list[Offer], product: Product,
                           max_price: float) -> list[Offer]:
    """
        Фильтр предложений по максимальной цене.

        Принимает список всех предложений, объект товара и максимальную цену.
        Отбирает предложения по товару с ценой не выше max_price.
        Возвращает список подходящих предложений.
    """
    filtered_offers = []
    for offer in offers:
        if offer.product == product and offer.price <= max_price:
            filtered_offers.append(offer)
    return filtered_offers


def filter_offers_by_delivery(offers: list[Offer], product: Product,
                              max_days: int) -> list[Offer]:
    """
        Фильтр предложений по максимальному сроку доставки.

        Принимает список всех предложений, объект товара и максимальный срок.
        Отбирает предложения по товару со сроком доставки не больше max_days.
        Возвращает список подходящих предложений.
    """
    filtered_offers = []
    for offer in offers:
        if (offer.product == product
                and offer.delivery_time_days <= max_days):
            filtered_offers.append(offer)
    return filtered_offers


def sort_offers_by_price(offers: list[Offer], product: Product) -> list[Offer]:
    """
        Сортировка предложений по цене.

        Принимает список всех предложений и id товара.
        Находит предложения по товару и сортирует их по цене
        по возрастанию.
        Возвращает новый отсортированный список предложений.
    """
    sorted_offers = find_offers_by_product(offers, product)
    sorted_offers_list = sorted(sorted_offers,
                                key=lambda offer: offer.price)
    return sorted_offers_list


def compare_prices(offers: list[Offer], product: Product) -> Offer | None:
    """
        Поиск лучшего предложения по цене.

        Принимает список всех предложений и id товара.
        Находит предложение с минимальной ценой по этому товару.
        Возвращает предложение с минимальной ценой
        или None, если предложений по товару нет.
    """
    product_offers = find_offers_by_product(offers, product)
    if not product_offers:
        return None
    return min(product_offers, key=lambda offer: offer.price)
