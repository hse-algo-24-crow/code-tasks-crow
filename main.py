def validate_matrix(matrix: list[list[int]]) -> None:
    
    if not isinstance(matrix, list):
        raise Exception("Параметр не является трехдиагональной матрицей")
    if len(matrix) < 1:
        raise Exception("Параметр не является трехдиагональной матрицей")
    if len(matrix)==1 and len(matrix[0])==1: return 
    
    row_index = 0 
    d1, d2, d3 = 0,0,0 #хранение ненулевых элементов

    for row in matrix: 
        """Проверяет выброс исключения при передаче прямоугольной матрицы"""
        if len(row) < 1 or len(matrix) != len(row): 
            raise Exception("Параметр не является трехдиагональной матрицей")
        
        """Проверяет выброс исключения при передаче в параметре матрицы с не целым значением"""
        for item in row:
            if not isinstance(item, int):
                raise Exception("Элемент матрицы не равен целому числу")
    
        """Проверяет выброс исключения при передаче в параметре матрицы с не нулевым значением вне диагонали"""
        for index, value in enumerate(row):

            if row_index == 0 and (index != 0 and index != 1) and (value!=0):
                raise Exception("Параметр не является трехдиагональной матрицей")
            
            if 0 < row_index < len(matrix)-1 and (index < row_index-1 or index > row_index+1) and (value!=0):
                raise Exception("Параметр не является трехдиагональной матрицей")
            
            if row_index == len(matrix)-1 and (index != len(row)-1 and index != len(row)-2) and (value!=0):
                raise Exception("Параметр не является трехдиагональной матрицей")
            
        row_index += 1

    row_index = 0
    """Проверяет выброс исключения при передаче в параметре матрицы с неверным значением на одной из диагоналей"""
    for row in matrix:
        for index, value in enumerate(row):
            if row_index == 0:
                d2, d3 = row[0], row[1]

            elif row_index == 1 and len(row)>2 and row[1] == d2 and row[2] == d3: d1 = row[0]
            elif row_index == 1 and len(row)==2 and row[1] == d2: d1 = row[0]

            elif 1<row_index<len(matrix)-1:
                if row[row_index-1]!=d1 or row[row_index]!=d2 or row[row_index+1]!=d3:
                    raise Exception("Параметр не является трехдиагональной матрицей")
            
            elif row_index == len(matrix)-1 and (d2!=row[-1] or d1!=row[-2]):
                raise Exception("Параметр не является трехдиагональной матрицей")
            
        row_index += 1


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    validate_matrix(matrix)

    n = len(matrix)
    if n == 1: return matrix[0][0]
    
    det = [0]*2
    det[0] = matrix[-1][-1]
    det[1] = matrix[-2][-2]*matrix[-1][-1]-matrix[-2][-1]*matrix[-1][-2]
    
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]

    for i in range(2, n):
        d = a*det[1] - b*c*det[0]
        det[0] = det[1]
        det[1] = d
    return det[1]

def main():
    matrix = [[1, 2], [2, 1]]

    if matrix is not None:
        print("Трехдиагональная матрица")
        for row in matrix:
            print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
