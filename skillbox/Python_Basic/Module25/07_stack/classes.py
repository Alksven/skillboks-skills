class Stak:
    list_tasks = dict()

    def sort(self, task, priority):
        if priority in self.list_tasks:
            self.list_tasks[priority].append(task)
        else:
            self.list_tasks[priority] = [task]

    def delete_task(self, task):
        if len(self.list_tasks[task[1]]) == 1:
            self.list_tasks[task[1]].remove(task[0])
            del self.list_tasks[task[1]]
        else:
            self.list_tasks[task[1]].remove(task[0])


class TaskManager:

    def __init__(self):
        self.stak = Stak()
        self.all_tasks = []
        self.completed_tasks = []

    def new_task(self, task, priority):
        self.all_tasks.append([task, priority])
        self.stak.sort(task, priority)

    def delete_task(self):
        print(f'\nЗадача "{self.all_tasks[-1][0]}" удалена.\n')
        self.completed_tasks.append(self.all_tasks[-1])
        self.stak.delete_task(self.all_tasks[-1])
        self.all_tasks.pop()

    def info_completed_tasks(self):
        print('\nЗавершенный список задач:')
        for num, task in enumerate(self.completed_tasks):
            print(f'{num + 1}. {task[0]}')
            if num + 1 == len(self.completed_tasks):
                print()

    def __str__(self):
        print('Текущий список задач:')
        for i in sorted(self.stak.list_tasks):
            print(f"{i} - {', '.join(str(x) for x in self.stak.list_tasks[i])}")
        return ''