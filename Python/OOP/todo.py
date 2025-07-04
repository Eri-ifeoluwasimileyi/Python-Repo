class TodoTask:

    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        if type(task) != str:
            raise TypeError('invalid task')
        self.tasks.append([[], task.lower()])


    def view_tasks(self):
        for task in self.tasks:
            print(f'{task[0]} {task[1]}')


    def remove_task(self, task):
        self.tasks.remove(task)


t1 = TodoTask()
t1.add_task('going home')




