def validate_tridiagonal(matrix: list[list[int]]) -> None:
    """
    Проверяет правильность трехдиагональной матрицы.
    :param matrix: матрица для проверки.
    :raises Exception: если матрица не соответствует стандартам.
    """
    if matrix is None:
        raise Exception("Параметр не является трехдиагональной матрицей")

    # Убедимся, что это список и он не пуст
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Параметр не является трехдиагональной матрицей")

    # Вычисляем количество элементов в первой строке
    row_length = len(matrix[0])

    # Проверка всех строк
    for row in matrix:
        if not isinstance(row, list) or len(row) != row_length:
            raise Exception("Параметр не является трехдиагональной матрицей")
        if not all(isinstance(value, int) for value in row):
            raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка, что матрица квадратная
    if len(matrix) != row_length:
        raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка на трехдиагональность
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка на одинаковые элементы в диагоналях
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if abs(i - j) > 1 and value != 0:
                raise ValueError("Параметр не является трехдиагональной матрицей")

    # Главная диагональ
    for i in range(1, len(matrix)):
        if matrix[i][i] != matrix[0][0]:
            raise ValueError("Параметр не является трехдиагональной матрицей")

    if len(matrix) > 1:
        # Проверка верхней диагонали
        for i in range(len(matrix) - 1):
            if matrix[i][i + 1] != matrix[0][1]:
                raise ValueError("Параметр не является трехдиагональной матрицей")

        # Проверка нижней диагонали
        for i in range(len(matrix) - 1):
            if matrix[i + 1][i] != matrix[1][0]:
                raise ValueError("Параметр не является трехдиагональной матрицей")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    validate_tridiagonal(matrix)

    size = len(matrix)

    # Для матрицы 1x1
    if size == 1:
        return matrix[0][0]

    # Для матрицы 2x2
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Для матриц большего размера
    prev2 = matrix[0][0]
    prev1 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Итеративное вычисление определителя
    for i in range(2, size):
        a = matrix[i][i]
        b = matrix[i][i - 1]
        c = matrix[i - 1][i]
        current = a * prev1 - b * c * prev2
        prev2, prev1 = prev1, current

    return prev1


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    if matrix is not None:
        print("Трехдиагональная матрица")
        for row in matrix:
            print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()