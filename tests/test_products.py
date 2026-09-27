from models.products import add_product, find_product_by_name
from models.products import Product


def test_add_product():
    """Добавление товара возвращает объект Product."""
    products = []
    product = add_product(products, 'Бумага А4', 'Офисная', 'Россия')
    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name == 'Бумага А4'
    assert len(products) == 1


def test_product_str():
    """__str__ возвращает читаемое представление."""
    product = Product(1, 'Бумага А4', 'Офисная', 'Россия')
    assert str(product) == 'Бумага А4 (Россия)'


def test_find_product_by_name():
    """Поиск находит товар по подстроке."""
    products = []
    add_product(products, 'Бумага А4', 'Офисная', 'Россия')
    found = find_product_by_name(products, 'бумага')
    assert len(found) == 1
    assert found[0].name == 'Бумага А4'
