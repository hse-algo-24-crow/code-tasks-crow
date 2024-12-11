INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с "
    "числовыми значениями"
)


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

    # Проверка на корректность входных данных
    if not price_table or not all(price_table):
        raise ValueError(PARAM_ERR_MSG)

    rows = len(price_table)
    cols = len(price_table[0])

    # Проверка на прямоугольность и числовые значения
    for row in price_table:
        if len(row) != cols:
            raise ValueError(PARAM_ERR_MSG)
        for value in row:
            if value is not None and not isinstance(value, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

    # Инициализация массива для хранения минимальных затрат
    dp = [[INF] * cols for _ in range(rows)]
    dp[0][0] = price_table[0][0] if price_table[0][0] is not None else INF

    # Заполнение массива минимальных затрат
    for i in range(rows):
        for j in range(cols):
            if price_table[i][j] is None:
                continue
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + price_table[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + price_table[i][j])

    # Если путь невозможен
    if dp[-1][-1] == INF:
        return {COST: None, PATH: None}

    # Восстановление пути
    path = []
    i, j = rows - 1, cols - 1
    while i > 0 or j > 0:
        path.append((i, j))
        if i > 0 and dp[i][j] == dp[i - 1][j] + (price_table[i][j] if price_table[i][j] is not None else INF):
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    path.reverse()

    return {COST: dp[-1][-1], PATH: path}


def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()