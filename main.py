def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы.
    Проверяет корректность переданных данных, после чего вызывает рекурсивную часть алгоритма

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """

    if not isinstance(matrix, list):
        raise Exception("Переданный параметр не является матрицей")

    if len(matrix) == 0:
        raise Exception("Пустая матрица")

    for row in matrix:
        if not (isinstance(row, list)):
            raise Exception("Переданный параметр не является матрицей")
        if len(row) != len(matrix):
            raise Exception("Переданный параметр не является квадратной матрицей")
        for num in row:
            if not (isinstance(num, int)):
                raise Exception("Матрица не целочисленная")
    return calculate_determinant_rec(matrix)


def calculate_determinant_rec(matrix: list[list[int]]) -> int:
    """Рекурсивная часть функции вычисления определителя матрицы

    :param matrix: целочисленная квадратная матрица
    :return: значение определителя
    """

    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    result = 0
    for pos in range(len(matrix)):
        sign = (-1) ** pos
        new_matrix = [col[:pos] + col[pos + 1:] for col in matrix[1:]]
        result += sign * matrix[0][pos] * calculate_determinant_rec(new_matrix)
    return result


def main():
    matrix = [[1, 2],
              [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
