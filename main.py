STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def validate_string_length(string_length):
    if isinstance(string_length, bool) or not isinstance(string_length, int) or string_length <= 0:  
        raise ValueError(STR_LENGTH_ERROR_MSG)



def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    validate_string_length(length)
    strings = []
    
    _add_one("", strings, length)
    _add_zero("", strings, length)
    return strings


def _add_one(cur_string, strings, target_length):
    if len(cur_string) == target_length:
        strings.append(cur_string)
    elif len(cur_string) + 1 == target_length:
        _add_one(cur_string + "1", strings, target_length)
    else:
        _add_one(cur_string + "1", strings, target_length)
        _add_zero(cur_string + "1", strings, target_length)


def _add_zero(cur_string, strings, target_length):
    if len(cur_string) == target_length:
        strings.append(cur_string)
    else:
        _add_one(cur_string + "0", strings, target_length)


def validate_n_k(n_check, k_check):
    if not isinstance(n_check, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not isinstance(k_check, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    if n_check < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k_check < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    if n_check < k_check:
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

    validate_n_k(n, k)
    
    if use_rec:  # рекурсивный алгоритм
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coefficient(n - 1, k, True) + binomial_coefficient(n - 1, k - 1, True)
    else:  # итерационный алгоритм
        results = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0 or i == j:
                    results[i][j] = 1
                else:
                    results[i][j] = results[i - 1][j] + results[i - 1][j - 1]
        return results[n][k]


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
