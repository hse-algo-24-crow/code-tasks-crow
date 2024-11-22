from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
        формуле вычисления последовательности.

        :param n: порядковый номер числа Фибоначчи
        :return: число Фибоначчи
        """
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> list[int]:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
        массива для хранения вычисляемых данных.

        :param n: порядковый номер числа Фибоначчи
        :return: число Фибоначчи
        """
    if n == 0:
        return 0

    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

        :param n: порядковый номер числа Фибоначчи
        :return: число Фибоначчи
        """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


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