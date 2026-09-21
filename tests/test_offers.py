from offers import add_offer, compare_prices, check_min_lot


def test_add_offer():
    """
        Добавление предложения увеличивает список на 1.
    """
    offers = []
    add_offer(offers, 1, 1, 1500.0, 3, 5)
    assert len(offers) == 1


def test_compare_prices():
    """
        Сравнение цен возвращает лучшее предложение.
    """
    offers = []
    add_offer(offers, 1, 1, 1500.0, 3, 5)
    add_offer(offers, 1, 2, 1450.0, 10, 7)
    best = compare_prices(offers, 1)
    assert best['price'] == 1450.0


def test_check_min_lot():
    """
        Проверка минимальной партии работает корректно.
    """
    offer = {'id': 1, 'min_lots': 5}
    assert check_min_lot(offer, 10) is True
    assert check_min_lot(offer, 3) is False
