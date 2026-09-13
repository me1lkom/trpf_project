supplier_1 = 'ИП Гербер'
price_1 = 1500.0
delivery_time_days = 5
min_lots_1 = 3

supplier_2 = 'ООО Мольберд'
price_2 = 1450.0
delivery_time_days = 7
min_lots_2 = 10

order_quantity = 15

def calculate_order_price(price, quantity):
    return price * quantity

def check_min_lot(min_lot, quantity):
    if quantity >= min_lot:
        return 'Объём соответствует минимальному заказу'
    return 'Не соблюден миниальный объём заказа от поставщика'

def compare_prices(supplier_1, price_1, supplier_2, price_2):
    if price_1 < price_2: 
        return f'Предложение от поставщика "{supplier_1}" лучше.'
    else: 
        return f'Предложение от поставщика "{supplier_2}" лучше.'
    
    
total_1 = calculate_order_price(price_1, order_quantity)
total_2 = calculate_order_price(price_2, order_quantity)

print(f"Поставщик: {supplier_1}")
print(f"Цена за единицу: {price_1} руб.")
print(f"Итоговая стоимость: {total_1} руб.")
print(check_min_lot(min_lots_1, order_quantity))
print()

print(f"Поставщик: {supplier_2}")
print(f"Цена за единицу: {price_2} руб.")
print(f"Итоговая стоимость: {total_2} руб.")
print(check_min_lot(min_lots_2, order_quantity))
print()

print(compare_prices(supplier_1, price_1, supplier_2, price_2))
