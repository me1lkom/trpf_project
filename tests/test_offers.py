from models.products import Product
from models.suppliers import Supplier
from models.offers import add_offer, compare_prices


def make_product():
    """Создать товар для тестов."""
    return Product(1, 'Бумага А4', 'Офисная', 'Россия')


def make_supplier():
    """Создать поставщика для тестов."""
    return Supplier(1, 'ИП Гербер', '770123456789',
                    '+7-900-123-45-67', 'gerber@example.com')


def test_add_offer():
    """Добавление предложения связывает объекты."""
    offers = []
    product = make_product()
    supplier = make_supplier()
    offer = add_offer(offers, product, supplier, 1500.0, 3, 5)
    assert offer.product is product
    assert offer.supplier is supplier
    assert offer.price == 1500.0
    assert len(offers) == 1


def test_offer_check_min_lot():
    """Проверка минимальной партии — метод объекта."""
    product = make_product()
    supplier = make_supplier()
    offer = add_offer([], product, supplier, 1500.0, 5, 5)
    assert offer.check_min_lot(10) is True
    assert offer.check_min_lot(3) is False


def test_offer_calculate_order_price():
    """Расчёт стоимости — метод объекта."""
    product = make_product()
    supplier = make_supplier()
    offer = add_offer([], product, supplier, 1500.0, 3, 5)
    assert offer.calculate_order_price(3) == 4500.0


def test_compare_prices():
    """Сравнение цен возвращает лучшее предложение."""
    product = make_product()
    supplier1 = make_supplier()
    supplier2 = Supplier(2, 'ООО Мольберд', '770987654321',
                         '+7-900-765-43-21', 'molberd@example.com')
    offers = []
    add_offer(offers, product, supplier1, 1500.0, 3, 5)
    add_offer(offers, product, supplier2, 1450.0, 10, 7)
    best = compare_prices(offers, product)
    assert best.supplier.name == 'ООО Мольберд'
