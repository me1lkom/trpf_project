from models.suppliers import add_supplier, get_supplier_by_id
from models.suppliers import Supplier


def test_add_supplier():
    """Добавление поставщика возвращает объект Supplier."""
    suppliers = []
    supplier = add_supplier(suppliers, 'ИП Гербер', '770123456789',
                            '+7-900-123-45-67', 'gerber@example.com')
    assert isinstance(supplier, Supplier)
    assert supplier.name == 'ИП Гербер'
    assert supplier.inn == '770123456789'


def test_get_supplier_by_id():
    """Поиск по id возвращает нужного поставщика."""
    suppliers = []
    supplier = add_supplier(suppliers, 'ИП Гербер', '770123456789',
                            '+7-900-123-45-67', 'gerber@example.com')
    found = get_supplier_by_id(suppliers, supplier.id)
    assert found is supplier
