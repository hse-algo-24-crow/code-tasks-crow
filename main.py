INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с "
    "числовыми значениями"
)


def get_min_cost_path(
    price_table: list[list[float | int | None]],
) -> dict[str : float | None, str : list[tuple[int, int]] | None]:
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

    if not price_table or any(len(row) != len(price_table[0]) for row in price_table) or not all(price_table):
        raise ValueError(PARAM_ERR_MSG)
    rows, cols = len(price_table), len(price_table[0])
    for r in range(rows):
        for c in range(cols):
            val = price_table[r][c]
            if val is not None and not isinstance(val, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

    if price_table[0][0] is None or price_table[-1][-1] is None:
        return {COST: None, PATH: None}

    dp = [[None for _ in range(cols)] for _ in range(rows)]
    prev_cell = [[None for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = price_table[0][0]

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue

            if price_table[r][c] is None:
                # Клетка недоступна
                dp[r][c] = None
            else:
                top_cost = dp[r-1][c] if r > 0 else None
                left_cost = dp[r][c-1] if c > 0 else None

                candidates = []
                if top_cost is not None:
                    candidates.append((top_cost + price_table[r][c], (r-1, c)))
                if left_cost is not None:
                    candidates.append((left_cost + price_table[r][c], (r, c-1)))

                if candidates:
                    best_cost, best_prev = min(candidates, key=lambda x: x[0])
                    dp[r][c] = best_cost
                    prev_cell[r][c] = best_prev
                else:
                    dp[r][c] = None

    if dp[-1][-1] is None:
        return {COST: None, PATH: None}

    path = []
    cur = (rows-1, cols-1)
    while cur is not None:
        path.append(cur)
        cur = prev_cell[cur[0]][cur[1]]
    path.reverse()

    return {COST: dp[-1][-1], PATH: path}


def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()