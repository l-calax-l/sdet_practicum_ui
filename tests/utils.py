import random
import string


def generate_customer_data(name_length: int = 5):
    """
    Генерирует тестовые данные для нового клиента.
    Имя генерируется заданной длины.
    """
    post_code_length = name_length * 2
    post_code = "".join(random.choices(string.digits, k=post_code_length))

    first_name = ""
    alphabet = string.ascii_lowercase

    for i in range(0, post_code_length, 2):
        two_digit_str = post_code[i:i+2]
        number = int(two_digit_str)
        letter_index = number % 26
        first_name += alphabet[letter_index]

    return first_name.capitalize(), post_code


def find_customer_to_delete(customer_names: list[str]) -> str:
    """Находит имя, длина которого ближе всего к средней арифметической."""
    if not customer_names:
        return ""
    name_lengths = [len(name) for name in customer_names]
    average_length = sum(name_lengths) / len(name_lengths)

    # Используем key=lambda для функции min, чтобы найти имя,
    # для которого разница между его длиной и средней — минимальна.
    closest_name = min(
        customer_names, key=lambda name: abs(len(name) - average_length)
    )  # noqa: E501
    return closest_name
