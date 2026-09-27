class Product:
    """
        Товары.
    """
    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        country: str
    ) -> None:
        """
            Создание объекта класса.

            Принимает id, название, описание
            и страну производства товара.
        """
        self.id = product_id
        self.name = name
        self.description = description
        self.country = country

    def __str__(self) -> str:
        """
            Возвращение строкового представления товара.
        """
        return f'{self.name} ({self.country})'

    @classmethod
    def from_data(cls, data: dict) -> 'Product':
        """
            Создание товара из словаря JSON.

            Принимает словарь с товарами.
            Возвращает объект Products.
        """
        return cls(
            data['id'],
            data['name'],
            data['description'],
            data['country']
        )


def add_product(products: list[Product], name: str,
                description: str, country: str) -> Product:
    """
        Добавление нового товара.

        Принимает список всех товаров, а также имя, описание и
        страну производства нового товара.
        Генерирует новый id, создаёт объект товара
        и добавляет его в список.
        Возвращает объект нового товара.
    """
    if products:
        new_id = max(product.id for product in products) + 1
    else:
        new_id = 1
    new_product = Product(new_id, name, description, country)

    products.append(new_product)
    return new_product


def find_product_by_name(products: list[Product], query: str) -> list[Product]:
    """
        Поиск товара(ов) по названию.

        Принимает список всех товаров и запрос на поиск.
        Приводит запрос в нижний регистр,
        находит все товары с запросом в названии, добавляя их в список.
        Возвращает список найденных товаров.
    """
    find_products = [product for product in products if query.lower() in
                     product.name.lower()]
    return find_products


def get_product_by_id(products: list[Product],
                      product_id: int) -> Product | None:
    """
        Поиск товара по id.

        Принимает список всех товаров и id искомого.
        Находит товар по id.
        Возвращает объект товара или None, если товар не найден.
    """
    for product in products:
        if product_id == product.id:
            return product
    return None
