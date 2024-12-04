STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    validate_strings(length)
    strings = []
    __add_one("", strings, length)
    __add_zero("", strings, length)
    return strings


def validate_strings(length: int) -> None:
    """Проверяет параметр length на корректность."""
    if not type(length) is int or length <= 0:   # isinstance не работает, тк bool подкласс int
        raise ValueError(STR_LENGTH_ERROR_MSG)


def __add_one(current_string: str, strings: list[str], length: int) -> None:
    """Добавляет в строку 1 и рекурсивно вызывает __add_zero."""
    current_string += "1"
    if len(current_string) == length:
        strings.append(current_string)
    else:
        __add_one(current_string, strings, length)
        __add_zero(current_string, strings, length)


def __add_zero(current_string: str, strings: list[str], length: int) -> None:
    """Добавляет в строку 0 и рекурсивно вызывает __add_one."""
    current_string += "0"
    if len(current_string) == length:
        strings.append(current_string)
    else:
        __add_one(current_string, strings, length)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_params(n, k)

    return binomial_coefficient_recursive(n, k) if use_rec else binomial_coefficient_iterative(n, k)


def validate_params(n: int, k: int) -> None:
    """Проверяет параметры на корректность."""
    if not type(n) is int:   # isinstance не работает, тк bool подкласс int
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not type(k) is int:   # isinstance не работает, тк bool подкласс int
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)


def binomial_coefficient_recursive(n: int, k: int) -> int:
    """Рекурсивная реализация вычисления биномиального коэффициента."""
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    
    return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n -1, k)


def binomial_coefficient_iterative(n:int, k:int) -> int:
    k = min(k, n-k)  # минимизируем количество итераций
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n-i)
        denominator *= (i+1)

    return numerator // denominator


def main():
    n = 10
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k, use_rec=True),
    )


if __name__ == "__main__":
    main()
