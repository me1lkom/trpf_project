class Supplier:
    """
        Поставщики.
    """
    def __init__(
        self,
        supplier_id: int,
        name: str,
        inn: str,
        phone: str,
        email: str
    ) -> None:
        """
            Создание объекта класса.

            Принимает id, название, ИНН,
            телефон и email поставщика.
        """
        self.id = supplier_id
        self.name = name
        self.inn = inn
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        """
            Возвращение строкового представления поставщика.
        """
        return f'{self.name} (ИНН {self.inn}, тел. {self.phone})'

    @classmethod
    def from_data(cls, data: dict) -> 'Supplier':
        """
            Создание поставщика из словаря JSON.

            Принимает словарь с поставщиками.
            Возвращает объект Supplier.
        """
        return cls(
            data['id'],
            data['name'],
            data['inn'],
            data['phone'],
            data['email']
        )


def add_supplier(suppliers: list[Supplier], name: str, inn: str,
                 phone: str, email: str) -> Supplier:
    """
        Добавление нового поставщика.

        Принимает список всех поставщиков, имя, ИНН,
        телефон и email нового поставщика.
        Генерирует новый id, создаёт объект поставщика
        и добавляет его в список.
        Возвращает объект нового поставщика.
    """
    if suppliers:
        new_id = max(supplier.id for supplier in suppliers) + 1
    else:
        new_id = 1

    new_supplier = Supplier(new_id, name, inn, phone, email)

    suppliers.append(new_supplier)
    return new_supplier


def find_supplier_by_name(suppliers: list[Supplier],
                          query: str) -> list[Supplier]:
    """
        Поиск поставщика(ов) по названию.

        Принимает список всех поставщиков и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит всех поставщиков с запросом в названии, добавляя их в список.
        Возвращает список найденных поставщиков.
    """
    find_suppliers = [supplier for supplier in suppliers if query.lower() in
                      supplier.name.lower()]

    return find_suppliers


def get_supplier_by_id(suppliers: list[Supplier],
                       supplier_id: int) -> Supplier | None:
    """
        Поиск поставщика по id.

        Принимает список всех поставщиков и id искомого.
        Находит поставщика по id.
        Возвращает объект поставщика или None, если поставщик не найден.
    """
    for supplier in suppliers:
        if supplier_id == supplier.id:
            return supplier
    return None
