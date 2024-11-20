from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    

def fibonacci_iter(n: int) -> int:  
    if n <= 1:
        return n
    numbers = [0, 1]
    for i in range(2, n + 1):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers[n]
    

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b   


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci_iter(n))


if __name__ == "__main__":
    main()
