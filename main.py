PROFIT = "profit"
DISTRIBUTION = "distribution"
PARAM_ERR_MSG = (
    "Таблица прибыли от проектов не является прямоугольной "
    "матрицей с числовыми значениями"
)
NEG_PROFIT_ERR_MSG = "Значение прибыли не может быть отрицательно"
DECR_PROFIT_ERR_MSG = "Значение прибыли не может убывать с ростом инвестиций"


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def validate_matrix(matrix: list[list[int]]) -> None:
    if not isinstance(matrix, list):
        raise ValueError(PARAM_ERR_MSG)

    if len(matrix) < 1:
        raise ValueError(PARAM_ERR_MSG)

    length = len(matrix[0])

    for row in range(len(matrix)):
        if len(matrix[row]) == 0 or len(matrix[row]) != length:
            raise ValueError(PARAM_ERR_MSG)

    # Проверка типов и неотрицательности
    for r in range(len(matrix)):
        for c in range(length):
            val = matrix[r][c]
            if not isinstance(val, (int, float)):
                raise ValueError(PARAM_ERR_MSG)
            if val < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, c, r)

    # Проверка неубывания
    for c in range(length):
        for r in range(1, len(matrix)):
            if matrix[r][c] < matrix[r-1][c]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, c, r)


def get_invest_distribution(
    profit_matrix: list[list[int]],
) -> dict[str, object]:
    """
    Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами.

    Логика:
    - Кол-во строк = R => доступно R единиц инвестиций для распределения.
    - Если для проекта i выделено k единиц (k > 0), то прибыль для проекта i: profit_matrix[k-1][i].
    - Если k = 0, проект i не получает инвестиций и прибыль = 0.
    - Нужно максимизировать суммарную прибыль, распределяя ровно R единиц по всем проектам.
    """
    validate_matrix(profit_matrix)
    level_cnt = len(profit_matrix)  
    project_cnt = len(profit_matrix[0])
    
    import math
    max_profit_matrix = [[-math.inf]*(project_cnt + 1) for _ in range(level_cnt + 1)]
    max_profit_matrix[0][0] = 0

    # Заполняем DP
    for j in range(1, project_cnt + 1):
        for i in range(level_cnt + 1):
            best_profit = -math.inf
            for invest in range(i+1):
                prev_profit = max_profit_matrix[i - invest][j - 1]
                cur_profit = prev_profit + (profit_matrix[invest - 1][j - 1] if invest > 0 else 0)
                if cur_profit > best_profit:
                    best_profit = cur_profit
            max_profit_matrix[i][j] = best_profit

    max_profit = max_profit_matrix[level_cnt][project_cnt]

    # Восстановление распределения
    distribution = []
    rem = level_cnt
    for proj_idx in range(project_cnt, 0, -1):
        best_invest_for_proj = 0
        # Текущая целевая прибыль
        current_opt_profit = max_profit_matrix[rem][proj_idx]

        for invest in range(rem+1):
            prev_profit = max_profit_matrix[rem - invest][proj_idx - 1]
            candidate_profit = prev_profit + (profit_matrix[invest - 1][proj_idx - 1] if invest > 0 else 0)
            if candidate_profit == current_opt_profit:
                best_invest_for_proj = invest
                break

        distribution.insert(0, best_invest_for_proj)
        rem -= best_invest_for_proj

    return {PROFIT: max_profit, DISTRIBUTION: distribution}


def main():
    profit_matrix = [
        [15, 18, 16, 17],
        [20, 22, 23, 19],
        [26, 28, 27, 25],
        [34, 33, 29, 31],
        [40, 39, 41, 37],
    ]
    print(get_invest_distribution(profit_matrix))


if __name__ == "__main__":
    main()
