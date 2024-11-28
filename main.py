def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы
    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    # Валидация входной матрицы
    validate_matrix(matrix)

    # Базовый случай: если размер матрицы 1x1
    if len(matrix) == 1:
        return matrix[0][0]

    # Базовый случай: если размер матрицы 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Рекурсивный случай
    determinant = 0
    for col in range(len(matrix)):
        # Создаем минор путем удаления первой строки и текущего столбца
        minor = [
            [matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(1, len(matrix))
        ]
        # Алгебраическое дополнение и рекурсивный вызов
        cofactor = (-1) ** col * matrix[0][col] * calculate_determinant(minor)
        determinant += cofactor

    return determinant

def validate_matrix(matrix: list[list[int]]) -> None:
    # Проверка, что matrix является списком
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком.")

    # Проверка, что каждый элемент матрицы также является списком
    if not all(isinstance(row, list) for row in matrix):
        raise Exception("Каждая строка матрицы должна быть списком.")

    # Проверка, что матрица не пуста и является квадратной
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise Exception("Матрица должна быть квадратной и непустой.")

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица:")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")

if __name__ == "__main__":
    main()