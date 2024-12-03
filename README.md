# Задание №4 Вариант 1 
# Динамическое программирование
## Задачи  
1. В Файле main.py реализовать функцию *get_min_cost_path*, принимающую прямоугольную матрицу из чисел, представляющих цену посещения соответствующей ячейки, и возвращающую словарь с минимальной стоимостью пути из левого верхнего угла в правый нижний и кортежем индексов ячеек из этого пути.
## Примечания 
- Перемещение из ячейки в ячейку можно производить только по горизонтали вправо или по вертикали вниз.
- Стоимость пути из левого верхнего угла таблицы в правый нижний рассчитывается как сумма цен посещения всех ячеек на этом пути.
- Обратить внимание, что некоторые тесты ожидают вызов определенного вида исключения с заданным сообщением об ошибке.
- Разработку вести в отдельной ветке, созданной на основе данной. В названии ветки префикс main заменить на название команды.
- Корректность работы функции *get_min_cost_path* проверить запустив файл test.py с модульными тестами.