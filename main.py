from products import add_product, find_product_by_name, get_product_by_id
from suppliers import (
    add_supplier_to_product,
    compare_prices,
    filter_suppliers_by_delivery,
    filter_suppliers_by_price,
    sort_suppliers_by_price,
    check_min_lot,
    calculate_order_price,
)
from storage import load_products, save_products
from utils import input_int, input_float, input_not_empty

DATA_FILE = "data/products.json"


def show_products(products: list) -> None:
    """
        Вывести список всех товаров.
    """
    if not products:
        print('Список товаров пуст.')
        return
    for product in products:
        print(f'ID: {product['id']}, Название: {product['name']},'
              f'Список поставщиков: {product['suppliers']}')


def show_suppliers(product: dict) -> None:
    """
        Вывести список поставщиков товара.
    """
    if not product['suppliers']:
        print("У этого товара нет поставщиков.")
        return
    for supplier in product['suppliers']:
        print(f'{supplier['name']}: {supplier['price']} руб., '
              f'доставка {supplier['delivery_time_days']} дн., '
              f'мин. партия {supplier['min_lots']}, '
              f'тел. {supplier['phone']}')


def choose_product(products: list) -> dict | None:
    """
        Запросить id товара и вернуть его или None.
    """
    product_id = input_int('ID товара: ')
    product = get_product_by_id(products, product_id)
    if not product:
        print('Товар не найден.')
    return product


def main() -> None:
    """Точка запуска приложения."""
    products = load_products(DATA_FILE)

    while True:
        print('\n=== Сервис сравнения поставщиков ===')
        print('1. Показать все товары')
        print('2. Добавить товар')
        print('3. Найти товар по названию')
        print('4. Показать поставщиков товара')
        print('5. Добавить поставщика к товару')
        print('6. Фильтр поставщиков по цене')
        print('7. Фильтр поставщиков по сроку доставки')
        print('8. Сортировка поставщиков по цене')
        print('9. Сравнить цены (лучшее предложение)')
        print('10. Проверить минимальную партию')
        print('11. Рассчитать стоимость заказа')
        print('0. Выход')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_products(products)
        elif choice == '2':
            name = input_not_empty('Название товара: ')
            add_product(products, name)
            save_products(DATA_FILE, products)
            print('Товар добавлен.')
        elif choice == '3':
            query = input_not_empty('Поиск: ')
            found = find_product_by_name(products, query)
            show_products(found)
        elif choice == '4':
            product = choose_product(products)
            if product:
                show_suppliers(product)
        elif choice == '5':
            product = choose_product(products)
            if not product:
                continue
            name = input_not_empty('Название поставщика: ')
            price = input_float('Цена: ')
            delivery = input_int('Срок доставки (дней): ')
            min_lots = input_int('Минимальная партия: ')
            phone = input_not_empty('Телефон: ')
            add_supplier_to_product(
                product, name, price, delivery, min_lots, phone
            )
            save_products(DATA_FILE, products)
            print('Поставщик добавлен.')
        elif choice == '6':
            product = choose_product(products)
            if not product:
                continue
            max_price = input_float('Максимальная цена: ')
            result = filter_suppliers_by_price(product, max_price)
            for s in result:
                print(f'  {s['name']}: {s['price']} руб.')
        elif choice == '7':
            product = choose_product(products)
            if not product:
                continue
            max_days = input_int('Максимальный срок доставки: ')
            result = filter_suppliers_by_delivery(product, max_days)
            for s in result:
                print(f'  {s['name']}: {s['delivery_time_days']} дн.')
        elif choice == '8':
            product = choose_product(products)
            if not product:
                continue
            for s in sort_suppliers_by_price(product):
                print(f'  {s['name']}: {s['price']} руб.')
        elif choice == '9':
            product = choose_product(products)
            if not product:
                continue
            best = compare_prices(product)
            if best:
                print(f'Лучшее предложение: {best['name']} — '
                      f'{best['price']} руб.')
            else:
                print('У товара нет поставщиков.')
        elif choice == '10':
            product = choose_product(products)
            if not product:
                continue
            query = input_not_empty('Название поставщика: ')
            found = [s for s in product['suppliers']
                     if query.lower() in s['name'].lower()]
            if not found:
                print('Поставщик не найден.')
                continue
            quantity = input_int('Количество: ')
            for s in found:
                if check_min_lot(s, quantity):
                    print(f'{s['name']}: партия подходит.')
                else:
                    print(f'{s['name']}: партия мала '
                          f'(минимум {s['min_lots']}).')
        elif choice == '11':
            product = choose_product(products)
            if not product:
                continue
            query = input_not_empty('Название поставщика: ')
            found = [s for s in product['suppliers']
                     if query.lower() in s['name'].lower()]
            if not found:
                print('Поставщик не найден.')
                continue
            quantity = input_int('Количество: ')
            for s in found:
                total = calculate_order_price(s, quantity)
                print(f'{s['name']}: итого {total} руб.')
        elif choice == '0':
            print('Выход.')
            break
        else:
            print('Некорректный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
