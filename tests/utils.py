import random
import string


def generate_customer_data():
    """
    Генерирует тестовые данные для нового клиента согласно заданию.

    Алгоритм:
    1. Создается 10-значный Post Code.
    2. Индекс разбивается на 5 двузначных чисел.
    3. Каждое число преобразуется в букву английского алфавита.

    :return: first_name, post_code
    """
    # 1. Генерируем Post Code
    post_code = "".join(random.choices(string.digits, k=10))

    # 2. Генерируем First Name на основе Post Code
    first_name = ""
    alphabet = string.ascii_lowercase

    # Разбиваем Post Code на 5 частей по 2 цифры
    for i in range(0, 10, 2):
        two_digit_str = post_code[i : i + 2]
        number = int(two_digit_str)

        # Находим остаток от деления на 26, чтобы получить индекс от 0 до 25.
        letter_index = number % 26

        first_name += alphabet[letter_index]

    return first_name, post_code
