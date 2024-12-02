STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

def validate_string(length: int):
    """
    Проверяет корректность параметра длины строки.
    :param length: Длина строки.
    :raise ValueError: Если длина строки некорректна.
    """
    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError(STR_LENGTH_ERROR_MSG)
    if length <= 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)
    
def __add_one(cur_string: str, strings: list[str], target_len: int):
    """
    Добавляет символ '1' к текущей строке и продолжает генерацию.

    :param cur_string: Текущая строка.
    :param strings: Список всех строк.
    :param target_len: Целевая длина строки.
    """
    cur_string += "1"
    if len(cur_string) == target_len:
        strings.append(cur_string)
    else:
        __add_one(cur_string, strings, target_len)
        __add_zero(cur_string, strings, target_len)
    
def __add_zero(cur_string: str, strings: list[str], target_len: int):
    """
    Добавляет символ '0' к текущей строке и продолжает генерацию,
    если последний символ текущей строки не '0'.

    :param cur_string: Текущая строка.
    :param strings: Список всех строк.
    :param target_len: Целевая длина строки.
    """
    if not cur_string or cur_string[-1] != "0":
        cur_string += "0"
        if len(cur_string) == target_len:
            strings.append(cur_string)
        else:
            __add_one(cur_string, strings, target_len)

def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    validate_string(length)

    strings = []
    __add_one("", strings, length)
    __add_zero("", strings, length)
    return strings

def validate_binomial_params(n: int, k: int):
    """
    Проверяет корректность параметров для вычисления биномиального коэффициента.
    :param n: Количество элементов в множестве.
    :param k: Количество выбираемых элементов.
    :raise ValueError: Если параметры не являются целыми неотрицательными числами
    или n меньше k.
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

def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_binomial_params(n, k)

    if use_rec:
        # Рекурсивная реализация
        if k == 0 or n == k:
            return 1
        return binomial_coefficient(n - 1, k - 1, use_rec=True) + binomial_coefficient(n - 1, k, use_rec=True)
    else:
        # Итеративная реализация
        if k > n - k:
            k = n - k
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result


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
