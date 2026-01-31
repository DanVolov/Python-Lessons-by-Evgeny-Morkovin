class Task:
    def __init__(self,title, description):
        self.id = None
        self.title = title
        self.description = description

    def to_dict(self):
        return {'id':self.id,'title':self.title,'description':self.description}

class TaskModel:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(title, description)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task

    def delete_task(self, id):
        task = self.get_task(id)
        if task:
            self.tasks.remove(task)
            return True
        return False