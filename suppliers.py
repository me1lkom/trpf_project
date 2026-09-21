def add_supplier(suppliers: list, name: str, inn: str,
                 phone: str, email: str) -> dict:
    """
        Добавление нового поставщика.

        Принимает список всех поставщиков, имя, ИНН,
        телефон и email нового поставщика.
        Генерирует новый id, создаёт словарь поставщика
        и добавляет его в список.
        Возвращает словарь нового поставщика.
    """
    if suppliers:
        new_id = max(supplier['id'] for supplier in suppliers) + 1
    else:
        new_id = 1

    new_supplier = {
        'id': new_id,
        'name': name,
        'inn': inn,
        'email': email,
        'phone': phone
    }

    suppliers.append(new_supplier)
    return new_supplier


def find_supplier_by_name(suppliers: list, query: str) -> list:
    """
        Поиск поставщика(ов) по названию.

        Принимает список всех поставщиков и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит всех поставщиков с запросом в названии, добавляя их в список.
        Возвращает список найденных поставщиков.
    """
    find_suppliers = [supplier for supplier in suppliers if query.lower() in
                      supplier['name'].lower()]

    return find_suppliers


def get_supplier_by_id(suppliers: list, supplier_id: int) -> dict | None:
    """
        Поиск поставщика по id.

        Принимает список всех поставщиков и id искомого.
        Находит поставщика по id.
        Возвращает поставщика или None, если поставщик не найден.
    """
    for supplier in suppliers:
        if supplier_id == supplier['id']:
            return supplier
    return None
