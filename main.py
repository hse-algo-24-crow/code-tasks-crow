INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)


def validate_matrix(matrix: list[list]) -> None:
    """Проверяет корректность ввода матрицы
    :param matrix: Матрица.
    :raise ValueError: Если матрица не является прямоугольной матрицей с
    числовыми значениями.
    """
    if not isinstance(matrix, list):
        raise ValueError(PARAM_ERR_MSG)
    if len(matrix) == 0:
        raise ValueError(PARAM_ERR_MSG)

    for i in range(len(matrix)):
        row = matrix[i]
        if not isinstance(row, list):
            raise ValueError(PARAM_ERR_MSG)
        if len(row) != len(matrix[0]):
            raise ValueError(PARAM_ERR_MSG)
        if len(row) == 0:
            raise ValueError(PARAM_ERR_MSG)
        for j in range(len(row)):
            if not isinstance(matrix[i][j], (int, float)):
                raise ValueError(PARAM_ERR_MSG)


def get_min_cost_path(
    price_table: list[list[float | int]],
) -> dict[str: float, str: list[tuple[int, int]]]:
    """Возвращает путь минимальной стоимости в таблице из левого верхнего угла
    в правый нижний. Каждая ячейка в таблице имеет цену посещения. Перемещение
    из ячейки в ячейку можно производить только по горизонтали вправо или по
    вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути,
    path - путь, список кортежей с индексами ячеек.
    """

    validate_matrix(price_table)
    result = {}
    cost_matrix = [[price_table[j][i] for i in range(len(price_table[j]))] for j in range(len(price_table))]
    path_matrix = [[(0, 0) for i in range(len(price_table[j]))] for j in range(len(price_table))]

    for row in range(len(price_table)):
        for col in range(len(price_table[row])):
            if row == 0 and col == 0:
                path_matrix[row][col] = (-1, -1)
            elif row == 0:
                cost_matrix[row][col] += cost_matrix[row][col - 1]
                path_matrix[row][col] = (row, col - 1)
            elif col == 0:
                cost_matrix[row][col] += cost_matrix[row - 1][col]
                path_matrix[row][col] = (row - 1, col)
            else:
                if cost_matrix[row - 1][col] <= cost_matrix[row][col - 1]:
                    cost_matrix[row][col] += cost_matrix[row - 1][col]
                    path_matrix[row][col] = (row - 1, col)
                else:
                    cost_matrix[row][col] += cost_matrix[row][col - 1]
                    path_matrix[row][col] = (row, col - 1)

    result[COST] = float(cost_matrix[-1][-1])
    move_to = path_matrix[-1][-1]
    path = [(len(cost_matrix) - 1, len(cost_matrix[-1]) - 1)]
    while move_to != (-1, -1):
        path = [move_to] + path
        move_to = path_matrix[move_to[0]][move_to[1]]
    result[PATH] = path
    return result


def main():
    table = [[1, 2, 2], [3, 4, 2], [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
