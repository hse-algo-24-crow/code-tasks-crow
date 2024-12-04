from typing import Any

def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    if not isinstance(items, list): #Проверка на правильный тип входной переменной
        raise TypeError("Параметр items не является списком")
    if len(set(items)) != len(items): #Проверка на отсутствие дубликатов в списке
        raise ValueError("Список элементов содержит дубликаты")
    if items == []:
        return []
    stack = [[[], items]]
    result = []
    while stack:
        couple = stack[0] #Получаем пару списков
        constant = couple[0] #Первый список пары - список элементов, в которых элементы установлены и переставляться не будут
        permutation = couple[1] #Второй список пары - список элементов, которые будут переставляться и добавляться к списку constant
        length = len(permutation)
        if length == 0: #Если в списке переставляемых элементов закончились элементы, то
            result.append(constant) #Один из вариантов перестановки готов и можно его добавить в итоговый результат
        else:
            for i in range(length):
                next_constant = constant.copy() #Формируем следующий список с постоянными элементами, который изменяться с помощью перестановки не будет
                next_constant.append(permutation[i]) #Этот список будет состоять из предыдущего постоянного списка + одного нового элемента, полученного при переборе
                next_permutation = permutation[:i:] + permutation[i + 1::] #Формируем следующий список с элементами для перестановки.
                # Он формируется из предыдущего переменного списка, но с исключением элемента, выбранного при переборе
                stack.append([next_constant, next_permutation]) #Добавляем в стек эту пару списков с постоянными и переменными элементами
        stack = stack[1::]
    return result

def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()