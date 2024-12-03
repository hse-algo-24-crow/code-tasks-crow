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
    if not type(length) is int or length <= 0: #isinstance не работает, тк bool подкласс int
        raise ValueError(STR_LENGTH_ERROR_MSG)
    return generate_strings_engine(length)


def generate_strings_engine(length: int) -> list[str]:
    return generate_strings_with_ending_zero(length) + generate_strings_with_ending_one(length)


def generate_strings_with_ending_one(length: int) -> list[str]:
    if length == 1:
        return ['1']
    
    return [string + '1' for string in generate_strings(length-1)]

    
def generate_strings_with_ending_zero(length: int) -> list[str]:
    if length == 1:
        return ['0']
    
    return [string + '0' for string in generate_strings_with_ending_one(length-1)]


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    if not isinstance(n, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)

    return binomial_coefficient_recursive(n, k) if use_rec else binomial_coefficient_iterative(n, k)


def binomial_coefficient_recursive(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    
    return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n -1, k)


def binomial_coefficient_iterative(n:int, k:int) -> int:
    k = min(k, n-k) # минимизируем количество итераций
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
