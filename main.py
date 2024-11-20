# -*- coding: utf-8 -*-

#from profilehooks import profile

#0 1 1 2 3 5 8 13 21 34...

def fibonacci_rec(n: int) -> int:
    # """���������� N-� ����� ���������. ����������� ���������� ��������
    # ������� ���������� ������������������.

    # :param n: ���������� ����� ����� ���������
    # :return: ����� ���������
    #"""
    if n <= 0:
        raise ValueError("The sequence number cannot be negative")
    #("���������� ����� �� ����� ���� �������������")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)    
    #pass


def fibonacci_iter(n: int) -> int:
    # """���������� N-� ����� ���������. ����������� ���������� � ��������������
    # ������� ��� �������� ����������� ������.

    # :param n: ���������� ����� ����� ���������
    # :return: ����� ���������
    # """
    if n <= 0:
        raise ValueError("The sequence number cannot be negative")
    #("���������� ����� �� ����� ���� �������������")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    fibi = [0] * n
    fibi[0] = 0
    fibi[1] = 1
    
    for i in range(2, n):
        fibi[i] = fibi[i - 1] + fibi[i - 2]
        
    return fibi[n - 1]
    #pass


def fibonacci(n: int) -> int:
    # """���������� N-� ����� ���������. ����������� ���������� ��� ������������� �������.

    # :param n: ���������� ����� ����� ���������
    # :return: ����� ���������
    # """
    if n <= 0:
        raise ValueError("The sequence number cannot be negative")
    #("���������� ����� �� ����� ���� �������������")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1

    for i in range(2, n):
        a = b
        b = a + b
        
    return b
    #pass


def main():
    n = 35
    print(f"\nCalculating {n} Fibonacci numbers is recursive:")
    #(f"���������� {n} ����� ��������� ����������:")
    print(fibonacci_rec(n))

    print(f"\nThe calculation of {n} Fibonacci numbers is iterative:")
    #(f"\n���������� {n} ����� ��������� ����������:")
    print(fibonacci_iter(n))

    print(f"\nCalculating {n} Fibonacci numbers iteratively without using an array:")
    #(f"\n���������� {n} ����� ��������� ���������� ��� ������������� �������:")
    print(fibonacci_iter(n))


if __name__ == "__main__":
    main()
