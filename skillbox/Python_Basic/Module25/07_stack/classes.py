class Stak:
    list_tasks = dict()

    def __init__(self, task):
        self.sort(task)



    def sort(self, task):
        if task[1] in self.list_tasks:
            self.list_tasks[task[1]] += ', ' + task[0]
        else:
            self.list_tasks[task[1]] = task[0]

        print(self.list_tasks)




class TaskManager:


    def new_task(self, task, priority):
        task_add = [task, priority]
        Stak(task_add)



