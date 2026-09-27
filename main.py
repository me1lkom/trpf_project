from models.products import (
    add_product,
    find_product_by_name,
    get_product_by_id,
)
from models.suppliers import (
    add_supplier,
    find_supplier_by_name,
    get_supplier_by_id,
)
from models.offers import (
    add_offer,
    find_offers_by_product,
    compare_prices,
    filter_offers_by_price,
    filter_offers_by_delivery,
    sort_offers_by_price,
)
from models.users import add_user, find_user_by_name, get_user_by_id
from storage import (
    load_products, save_products,
    load_suppliers, save_suppliers,
    load_offers, save_offers,
    load_users, save_users,
)
from utils import input_int, input_float, input_not_empty


PRODUCTS_FILE = 'data/products.json'
SUPPLIERS_FILE = 'data/suppliers.json'
OFFERS_FILE = 'data/offers.json'
USERS_FILE = 'data/users.json'


def show_products(products: list) -> None:
    """
        Вывести список товаров.
    """
    if not products:
        print('Список товаров пуст.')
        return
    for p in products:
        print(f'ID: {p.id}, {p}')


def show_suppliers(suppliers: list) -> None:
    """
        Вывести список поставщиков.
    """
    if not suppliers:
        print('Список поставщиков пуст.')
        return
    for s in suppliers:
        print(f'ID: {s.id}, {s}')


def show_offers(offers: list) -> None:
    """
        Вывести список предложений.
    """
    if not offers:
        print('Список предложений пуст.')
        return
    for o in offers:
        print(f'ID: {o.id}, {o}')


def show_users(users: list) -> None:
    """
        Вывести список пользователей.
    """
    if not users:
        print('Список пользователей пуст.')
        return
    for u in users:
        print(f'ID: {u.id}, {u}')


def menu_products(products: list) -> None:
    """
        Подменю для работы с товарами.
    """
    while True:
        print('\n=== Товары ===')
        print('1. Показать все')
        print('2. Добавить')
        print('3. Найти по названию')
        print('4. Найти по ID')
        print('0. Назад')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_products(products)
        elif choice == '2':
            name = input_not_empty('Название: ')
            description = input_not_empty('Описание: ')
            country = input_not_empty('Страна: ')
            add_product(products, name, description, country)
            save_products(PRODUCTS_FILE, products)
            print('Товар добавлен.')
        elif choice == '3':
            query = input_not_empty('Поиск: ')
            show_products(find_product_by_name(products, query))
        elif choice == '4':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if product:
                show_products([product])
            else:
                print('Товар не найден.')
        elif choice == '0':
            break
        else:
            print('Некорректный выбор.')


def menu_suppliers(suppliers: list) -> None:
    """
        Подменю для работы с поставщиками.
    """
    while True:
        print('\n=== Поставщики ===')
        print('1. Показать всех')
        print('2. Добавить')
        print('3. Найти по названию')
        print('4. Найти по ID')
        print('0. Назад')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_suppliers(suppliers)
        elif choice == '2':
            name = input_not_empty('Название: ')
            inn = input_not_empty('ИНН: ')
            phone = input_not_empty('Телефон: ')
            email = input_not_empty('Email: ')
            add_supplier(suppliers, name, inn, phone, email)
            save_suppliers(SUPPLIERS_FILE, suppliers)
            print('Поставщик добавлен.')
        elif choice == '3':
            query = input_not_empty('Поиск: ')
            show_suppliers(find_supplier_by_name(suppliers, query))
        elif choice == '4':
            supplier_id = input_int('ID поставщика: ')
            supplier = get_supplier_by_id(suppliers, supplier_id)
            if supplier:
                show_suppliers([supplier])
            else:
                print('Поставщик не найден.')
        elif choice == '0':
            break
        else:
            print('Некорректный выбор.')


def menu_offers(
    offers: list,
    products: list,
    suppliers: list
) -> None:
    """
        Подменю для работы с предложениями.
    """
    while True:
        print('\n=== Предложения ===')
        print('1. Показать все')
        print('2. Добавить')
        print('3. Показать по товару')
        print('4. Фильтр по цене')
        print('5. Фильтр по сроку доставки')
        print('6. Сортировка по цене')
        print('7. Лучшее предложение по товару')
        print('8. Проверка минимальной партии')
        print('9. Расчёт стоимости заказа')
        print('0. Назад')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_offers(offers)
        elif choice == '2':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            supplier_id = input_int('ID поставщика: ')
            supplier = get_supplier_by_id(suppliers, supplier_id)
            if not supplier:
                print('Поставщик не найден.')
                continue
            price = input_float('Цена: ')
            min_lots = input_int('Минимальная партия: ')
            delivery = input_int('Срок доставки (дней): ')
            add_offer(offers, product, supplier,
                      price, min_lots, delivery)
            save_offers(OFFERS_FILE, offers)
            print('Предложение добавлено.')
        elif choice == '3':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            show_offers(find_offers_by_product(offers, product))
        elif choice == '4':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            max_price = input_float('Максимальная цена: ')
            show_offers(
                filter_offers_by_price(offers, product, max_price)
            )
        elif choice == '5':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            max_days = input_int('Максимальный срок доставки: ')
            show_offers(
                filter_offers_by_delivery(offers, product, max_days)
            )
        elif choice == '6':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            show_offers(sort_offers_by_price(offers, product))
        elif choice == '7':
            product_id = input_int('ID товара: ')
            product = get_product_by_id(products, product_id)
            if not product:
                print('Товар не найден.')
                continue
            best = compare_prices(offers, product)
            if best:
                print(f'Лучшее предложение: ID {best.id}, '
                      f'поставщик {best.supplier.name}, '
                      f'цена {best.price}')
            else:
                print('Предложений по товару нет.')
        elif choice == '8':
            offer_id = input_int('ID предложения: ')
            quantity = input_int('Количество: ')
            offer = next(
                (o for o in offers if o.id == offer_id), None
            )
            if not offer:
                print('Предложение не найдено.')
                continue
            if offer.check_min_lot(quantity):
                print('Партия подходит.')
            else:
                print(f'Партия мала (минимум {offer.min_lots}).')
        elif choice == '9':
            offer_id = input_int('ID предложения: ')
            quantity = input_int('Количество: ')
            offer = next(
                (o for o in offers if o.id == offer_id), None
            )
            if not offer:
                print('Предложение не найдено.')
                continue
            total = offer.calculate_order_price(quantity)
            print(f'Итого: {total} руб.')
        elif choice == '0':
            break
        else:
            print('Некорректный выбор.')


def menu_users(users: list) -> None:
    """
        Подменю для работы с пользователями.
    """
    while True:
        print('\n=== Пользователи ===')
        print('1. Показать всех')
        print('2. Добавить')
        print('3. Найти по имени')
        print('4. Найти по ID')
        print('0. Назад')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_users(users)
        elif choice == '2':
            name = input_not_empty('Имя: ')
            email = input_not_empty('Email: ')
            add_user(users, name, email)
            save_users(USERS_FILE, users)
            print('Пользователь добавлен.')
        elif choice == '3':
            query = input_not_empty('Поиск: ')
            show_users(find_user_by_name(users, query))
        elif choice == '4':
            user_id = input_int('ID пользователя: ')
            user = get_user_by_id(users, user_id)
            if user:
                show_users([user])
            else:
                print('Пользователь не найден.')
        elif choice == '0':
            break
        else:
            print('Некорректный выбор.')


def main() -> None:
    """
        Точка запуска приложения.
    """
    products = load_products(PRODUCTS_FILE)
    suppliers = load_suppliers(SUPPLIERS_FILE)
    offers = load_offers(OFFERS_FILE, products, suppliers)
    users = load_users(USERS_FILE)

    while True:
        print('\n=== Сервис сравнения предложений поставщиков ===')
        print('1. Товары')
        print('2. Поставщики')
        print('3. Предложения')
        print('4. Пользователи')
        print('0. Выход')

        choice = input('Выберите раздел: ').strip()

        if choice == '1':
            menu_products(products)
        elif choice == '2':
            menu_suppliers(suppliers)
        elif choice == '3':
            menu_offers(offers, products, suppliers)
        elif choice == '4':
            menu_users(users)
        elif choice == '0':
            print('Выход.')
            break
        else:
            print('Некорректный выбор.')


if __name__ == '__main__':
    main()
