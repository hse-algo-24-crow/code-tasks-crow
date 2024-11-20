from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть положительным")
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть положительным")
    else:
        if n == 1 or n == 2:
            return 1
        else:
            array = [1, 1]
            for i in range(n - 2):
                array.append(array[-2] + array[-1])
            return array[-1]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть положительным")
    else:
        if n == 1 or n == 2:
            return 1
        else:
            first_number = 1
            second_number = 1
            for i in range(n - 2):
                s = first_number + second_number
                first_number = second_number
                second_number = s
            return second_number


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
