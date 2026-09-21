from suppliers import add_supplier, get_supplier_by_id


def test_add_supplier():
    """
        Добавление поставщика увеличивает список на 1.
    """
    suppliers = []
    add_supplier(suppliers, 'ИП Гербер', '770123456789',
                 '+7-900-123-45-67', 'gerber@example.com')
    assert len(suppliers) == 1


def test_get_supplier_by_id():
    """
        Поиск по id возвращает нужного поставщика.
    """
    suppliers = []
    supplier = add_supplier(suppliers, 'ИП Гербер', '770123456789',
                            '+7-900-123-45-67', 'gerber@example.com')
    found = get_supplier_by_id(suppliers, supplier['id'])
    assert found == supplier
