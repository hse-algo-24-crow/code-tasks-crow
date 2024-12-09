PROFIT = "profit"
DISTRIBUTION = "distribution"
PARAM_ERR_MSG = (
"Таблица прибыли от проектов не является прямоугольной "
"матрицей с числовыми значениями"
)
NEG_PROFIT_ERR_MSG = "Значение прибыли не может быть отрицательно"
DECR_PROFIT_ERR_MSG = "Значение прибыли не может убывать с ростом инвестиций"

def validate_matrix(matrix: list[list[int]]) -> None:

    if not isinstance(matrix, list):
        raise ValueError(PARAM_ERR_MSG)

    if len(matrix) < 1:
        raise ValueError(PARAM_ERR_MSG)

    length = len(matrix[0])

    for row in range(len(matrix)):
        if len(matrix[row]) == 0 or len(matrix[row]) != length:
            raise ValueError(PARAM_ERR_MSG)

    for index in range(len(matrix[row])):
        if not isinstance(matrix[row][index], int):
            raise ValueError(PARAM_ERR_MSG)
        if matrix[row][index] < 0:
            raise ProfitValueError(NEG_PROFIT_ERR_MSG, index, row)


    for element_index in range(length):
        for row_index in range(1, len(matrix)):
            if matrix[row_index-1][element_index] > matrix[row_index][element_index]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, element_index, row_index)



class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distribution(
    profit_matrix: list[list[int]],
) -> dict[str:int, str : list[int]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distribution - распределение инвестиций между проектами.
    """
    validate_matrix(profit_matrix)
    level_cnt = len(profit_matrix)
    project_cnt = len(profit_matrix[0])

    # Создание матрицы для хранения максимальной прибыли
    max_profit_matrix = [[0] * (project_cnt + 1) for _ in range(level_cnt + 1)]

    # Для восстановления распределения инвестиций
    distribution_matrix = [[0] * (project_cnt + 1) for _ in range(level_cnt + 1)]

    for proj_idx in range(1, project_cnt + 1):
        for level in range(level_cnt + 1):
            max_profit = 0
            best_part_for_current = 0

            for part_for_prev in range(level + 1):
                part_for_current = level - part_for_prev

                profit_from_prev = max_profit_matrix[part_for_prev][proj_idx - 1]

                profit_from_current = profit_matrix[part_for_current - 1][proj_idx - 1] if part_for_current > 0 else 0

                current_profit = profit_from_prev + profit_from_current

                if current_profit > max_profit:
                    max_profit = current_profit
                    best_part_for_current = part_for_current

                max_profit_matrix[level][proj_idx] = max_profit
                distribution_matrix[level][proj_idx] = best_part_for_current

            max_profit = max_profit_matrix[level_cnt][project_cnt]

    # Восстановим распределение инвестиций
    distribution = [] # Список для хранения распределения инвестиций
    level = level_cnt

    for proj_idx in range(project_cnt, 0, -1):
        distribution.insert(0, distribution_matrix[level][proj_idx])
        level -= distribution_matrix[level][proj_idx]

    return {PROFIT: max_profit, DISTRIBUTION: distribution}


def main():
    # profit_matrix = [
    # [15, 18, 16, 17],
    # [20, 22, 23, 19],
    # [26, 28, 27, 25],
    # [34, 33, 29, 31],
    # [40, 39, 41, 37],
    # ]
    profit_matrix = [[1, 1, 1], [2, 3, 2], [2, 2, 3]]
    print(get_invest_distribution(profit_matrix))


    if __name__ == "__main__":
        main()