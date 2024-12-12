INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с "
    "числовыми значениями"
)


def validate_price_table(price_table: list[list[float | int | None]]) -> None:
    if not price_table or not all(price_table):
        raise ValueError(PARAM_ERR_MSG)

    cols = len(price_table[0])

    for row in price_table:
        if len(row) != cols:
            raise ValueError(PARAM_ERR_MSG)
        for value in row:
            if value is not None and not isinstance(value, (int, float)):
                raise ValueError(PARAM_ERR_MSG)


def get_min_cost_path(
        price_table: list[list[float | int | None]],
) -> dict[str: float | None, str: list[tuple[int, int]] | None]:
    """Возвращает путь минимальной стоимости в таблице из левого верхнего угла
    в правый нижний. Каждая ячейка в таблице имеет цену посещения. Некоторые
    ячейки запрещены к посещению, вместо цены посещения значение None.
    Перемещение из ячейки в ячейку можно производить только по горизонтали
    вправо или по вертикали вниз.

    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути или None если пути не существует,
    path - путь, список кортежей с индексами ячеек, или None если пути
    не существует.
    """

    validate_price_table(price_table)

    rows = len(price_table)
    cols = len(price_table[0])

    # Инициализация массива для хранения минимальных затрат
    table = [[INF] * cols for _ in range(rows)]
    table[0][0] = price_table[0][0] if price_table[0][0] is not None else INF

    # Заполнение массива минимальных затрат
    for row in range(rows):
        for col in range(cols):
            if price_table[row][col] is None:
                continue
            if row > 0:
                table[row][col] = min(table[row][col], table[row - 1][col] + price_table[row][col])
            if col > 0:
                table[row][col] = min(table[row][col], table[row][col - 1] + price_table[row][col])

    # Если путь невозможен
    if table[-1][-1] == INF:
        return {COST: None, PATH: None}

    # Восстановление пути
    path = []
    row, col = rows - 1, cols - 1
    while row > 0 or col > 0:
        path.append((row, col))
        if row > 0 and table[row][col] == table[row - 1][col] + price_table[row][col]:
            row -= 1
        else:
            col -= 1
    path.append((0, 0))
    path.reverse()

    return {COST: table[-1][-1], PATH: path}


def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
