from suppliers import (
    add_supplier_to_product,
    compare_prices,
    check_min_lot,
)


def make_product():
    """
        Создать пустой товар для тестов.
    """
    return {'id': 1, 'name': 'Бумага А4', 'suppliers': []}


def test_add_supplier_to_product():
    """
        Добавление поставщика увеличивает список на 1.
    """
    product = make_product()
    add_supplier_to_product(
        product, 'ИП Гербер', 1500.0, 5, 3, '+7-900-123-45-67'
    )
    assert len(product['suppliers']) == 1


def test_compare_prices():
    """
        Сравнение цен возвращает лучшее предложение.
    """
    product = make_product()
    add_supplier_to_product(
        product, 'ИП Гербер', 1500.0, 5, 3, '+7-900-123-45-67'
    )
    add_supplier_to_product(
        product, 'ООО Мольберд', 1450.0, 7, 10, '+7-900-765-43-21'
    )
    best = compare_prices(product)
    assert best['name'] == 'ООО Мольберд'


def test_check_min_lot():
    """
        Проверка минимальной партии.
    """
    supplier = {'name': 'ИП Гербер', 'min_lots': 5}
    assert check_min_lot(supplier, 10) is True
    assert check_min_lot(supplier, 3) is False
