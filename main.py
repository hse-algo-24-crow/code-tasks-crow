from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<=0: return None
    elif n <= 2:
        return 1
    return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)
    pass


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<=0: return None
    a = [1] * n
    for i in range(2, n):
        a[i] = a[i - 2] + a[i - 1]
    return a[n - 1]
    pass


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<=0: return None
    elif n==1 or n==2: return 1
    previous = 1
    current = 1
    for i in range(3, n+1):
        temp = current
        current += previous
        previous = temp
        i += 1
    return current
    pass


def main():
    n = 5
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
