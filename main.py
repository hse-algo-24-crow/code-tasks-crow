
from profilehooks import profile


@profile
def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.
    """
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


@profile
def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.
    """
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


@profile
def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.
    """
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


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
