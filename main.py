def checks(matrix: list[list[int]]) -> bool:
    if not isinstance(matrix, list):
        raise Exception("Переданный объект не является матрицей. Матрица должна быть представлена в виде списка списков")
    
    if len(matrix) == 0:
        raise Exception("Передана пустая матрица. Посчитать определитель невозможно")
    
    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Переданный объект не является матрицей. Матрица должна быть представлена в виде списка списков")
        
        if len(row) != len(matrix):
            raise Exception("Переданный объект не является квадратной матрицей. Количество строк должно совпадать с количеством столбцов")
        
        for elem in row:
            if not isinstance(elem, int):
                raise Exception("В матрице есть нецелочисленные типы данных. Матрица должна состоять из целых чисел")
    
    


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    # checks_passed = False
    # if not checks_passed:
    #     checks(matrix)
    #     checks_passed = True # исправить, так как функция работает каждый раз, сделать чтобы срабатывала 1 раз

    checks(matrix)
    return __calculate_determinant_rec(matrix)



def __calculate_determinant_rec(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    det = 0
    x = 1  # -1**(i+j)
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    
    else:
        for j in range(size):
            new_matrix = [items[:j] + items[j + 1:] for items in matrix[1:]]
            det += x * matrix[0][j] * __calculate_determinant_rec(new_matrix)
            x = -1 * x

    return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)
        
    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
