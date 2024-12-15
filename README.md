# Задание №6
# Оптимальное расписание. Конвейерная задача.
## Задачи  
1. Общая задача для всех вариантов - файле schedule_pack/conveyor_schedule.py реализовать два приватных метода класса ConveyorSchedule.
    - __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]: Возвращает отсортированный список задач для применения алгоритма Джонсона.
    - __fill_schedule(self, tasks: list[StagedTask]) -> None: Процедура составляет расписание из элементов ScheduleItem для каждого исполнителя, согласно алгоритму Джонсона.
2. Отдельные задачи для вариантов:
    - Вариант 1. Разработать диаграмму классов пакета schedule_pack с использованием библиотеки (mermaid-js)[https://github.com/mermaid-js/mermaid#class-diagram-docs---live-editor]
    - Вариант 2. Реализовать вывод полученного от класса Schedule расписания в формате диаграммы Ганта библиотеки (mermaid-js)[https://github.com/mermaid-js/mermaid#gantt-chart-docs---live-editor]
    - Вариант 3. Добавить новые методы для класса Schedule, для вывода времени простоя для каждого исполнителя и общего времени простоя для всего расписания.
    - Вариант 4. Добавить метод для класса Schedule, для изменения состава задач и перерасчета расписания.

## Примечания 
- **В файле main.py представлен только пример использования пакета schedule_pack, задание необходимо выполнять в файле schedule_pack/conveyor_schedule.py**.
- Для решения задачи составления оптимального расписания с использованием алгоритма Джонсона подготовлен python-пакет schedule_pack.
- Python-пакет schedule_pack реализован в объектно-ориентированной парадигме.
- Обратить внимание, что некоторые тесты ожидают вызов определенного вида исключения с заданным сообщением об ошибке.
- В пакете представлены следующие классы
    * StagedTask: Представляет задачу для составления расписания. Используется в качестве входных данных для класса ConveyorSchedule.
    * ConveyorSchedule: Представляет оптимальное расписание для списка задач и двух исполнителей. Для каждого исполнителя расписание представлено набором экземпляров класса ScheduleItem.
    * ScheduleItem: Представляет собой элемент расписания, включает в себя задачу, выполняющуюся в течение некоторого времени, с указанием моментов начала и окончания ее выполнения.
- Проверить реализацию класса Schedule можно запустив набор авто-тестов в файле schedule_pack/tests/test_conveyor_schedule.py.
- Запустить тесты для проверки всего пакета schedule_pack можно с помощью файла test_runner.py.

## Конвейерная задача
### Постановка конвейерной задачи:
1. Количество заданий произвольно;
2. Каждое задание состоит из двух последовательных этапов, длительность которых произвольна;
3. Задания независимы;
4. Запрещены прерывания при выполнении заданий;
5. Количество работников строго 2;
6. Первый работник выполняет только первый этап каждого задания, второй работник — только второй этап каждого задания;
7. Производительность работников, размеры оплаты из труда и т.д. не учитываются;
8. Требуется построить расписание выполнения всех заданий в кратчайшие сроки.

### Алгоритм Джонсона
Пусть а<sub>i</sub> и b<sub>i</sub>, — это длительности первого и второго 
этапов i-го задания. 

Разобьём список всех заданий на две группы. В первую группу попадают задания, у которых а<sub>i</sub> <= b<sub>i</sub>. Во вторую группу - все остальные задания. 

Задания из первой группы отсортируем в порядке возрастания величин а<sub>i</sub>. Задания из второй группы отсортируем в порядке убывания величин b<sub>i</sub>.

Согласно алгоритму Джонсона, расписание получается кратчайшим, если сначала выполнить все задания из первой группы в отсортированном порядке, а затем — все задания из второй группы также в отсортированном порядке.

```mermaid
gantt
    title Диаграмма Ганта - Конвейерная задача
    dateFormat DD HH:mm    
    axisFormat %H:%M
    Начало выполнения работ : milestone, m1, 01 00:00, 0h
    section Конвейер 1
    G         :a1, 01 00:00, 1h
    D         :a2, after a1, 2h
    C         :a3, after a2, 3h
    E         :a4, after a3, 4h
    F         :a5, after a4, 7h
    A         :a6, after a5, 4h
    B         :a7, after a6, 5h
    section Конвейер 2
    G         :b1, after a1, 2h
    D         :b2, after a2, 3h
    C         :b3, after a3, 5h
    E         :b4, after a4 b3, 4h
    F         :b5, after a5 b4, 6h
    A         :b6, after a6 b5, 3h
    B         :b7, after a7 b6, 2h
    Окончание выполнения работ : milestone, m2, 02 04:00, 0h
```
