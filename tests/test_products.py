from products import add_product, find_product_by_name


def test_add_product():
    """
        Добавление товара увеличивает список на 1.
    """
    products = []
    add_product(products, 'Бумага А4', 'Офисная', 'Россия')
    assert len(products) == 1


def test_find_product_by_name():
    """
        Поиск находит товар по подстроке.
    """
    products = []
    add_product(products, 'Бумага А4', 'Офисная', 'Россия')
    found = find_product_by_name(products, 'бумага')
    assert len(found) == 1
