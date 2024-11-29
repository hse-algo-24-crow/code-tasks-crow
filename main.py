PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

def validate_coefficient(n: int, k:int):
    """Проверка параметров n и k"""
    if not isinstance(n, int): raise ValueError(NOT_INT_VALUE_TEMPL.format('n'))
    if not isinstance(k, int): raise ValueError(NOT_INT_VALUE_TEMPL.format('k'))
    
    if n<0: raise ValueError(NEGATIVE_VALUE_TEMPL.format('n'))
    if k<0: raise ValueError(NEGATIVE_VALUE_TEMPL.format('k'))

    if n<k: raise ValueError(N_LESS_THAN_K_ERROR_MSG)

def validate_triangle(length: int):
    """Проверка длины"""
    if type(length) is not int: raise ValueError(PATH_LENGTH_ERROR_MSG)
    if length <= 0: raise ValueError(PATH_LENGTH_ERROR_MSG)


def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между тремя
    вершинами треугольника A, B и C. Маршруты начинаются и оканчиваются в
    вершине A vertex. Допустимыми являются все пути между различными вершинами.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным
    числом.
    :return: Количество маршрутов.
    """
    validate_triangle(length)

    def a(n):
        if n == 1: return 0
        return b(n-1) + c(n-1)

    def b(n):
        if n == 1: return 1
        return a(n-1) + c(n-1)

    def c(n):
        if n == 1: return 1
        return a(n-1) + b(n-1)
    
    return a(length)


def binomial_coefficient_iter(n: int, k: int):
    """Итеративное вычисление биномиального коэффициента"""
    coefficients = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                coefficients[i][j] = 1
            else:
                coefficients[i][j] = coefficients[i - 1][j - 1] + coefficients[i - 1][j]

    return coefficients[n][k]

def binomial_coefficient_recursion(n: int, k: int):
    """Рекурсивное вычисление биномиального коэффициента"""
    if k == 1 or n == 1: return n
    if k == 0 or k == n: return 1
    return binomial_coefficient_recursion(n - 1, k - 1) + binomial_coefficient_recursion(n - 1, k)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_coefficient(n,k)
    if use_rec: return binomial_coefficient_recursion(n,k)
    else: return binomial_coefficient_iter(n,k)


def main():
    n = 10
    print(f"Количество маршрутов длиной {n} = {get_triangle_path_count(n)}")

    n = 10
    k = 5
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
