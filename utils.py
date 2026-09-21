def input_int(prompt: str) -> int:
    """
    Запросить у пользователя целое число.
    При неправильном вводе, запрос повторяется.
    """

    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Ошибка ввода! Введите целое число.')


def input_float(prompt: str) -> float:
    """
    Запросить у пользователя дробное число.
    При неправильном вводе, запрос повтоярется.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('Ошибка ввода! Введите дробное число.')


def input_not_empty(prompt: str) -> str:
    """
    Запросить у пользователя не пустую строку.
    При неправильно вводе, запрос повторяется.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('Ошибка ввода! Строка не может быть пустой.')
