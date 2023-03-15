from classes import TaskManager

manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
manager.new_task("помыть посуду", 4)

while True:
    print(manager)
    action = int(input('Выберите действие:\n1 = Добавить новую задачу.\n2 = Удалить задачу.'
                       '\n3 = Посмотреть список выполненных задач.\n4 = Выход из программы.\nВвод...'))
    if action == 1:
        task = input('Введите новую задачу: ')
        priority = int(input(f'Введите приоритет задачи: '))
        manager.new_task(task, priority)
    if action == 2:
        manager.delete_task()
    if action == 3:
        manager.info_completed_tasks()
    if action == 4:
        break