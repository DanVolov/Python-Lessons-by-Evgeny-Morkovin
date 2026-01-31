class Task:
    def __init__(self,title, description, priority=1):
        self.id = None
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority

    def to_dict(self):
        return {'id':self.id,'title':self.title,'description':self.description,'completed':self.completed,'priority':self.priority}

class TaskModel:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description, priority=1):
        task = Task(title, description, priority)
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

    def toggle_task_completed(self, id):
        task = self.get_task(id)
        if task:
            task.completed = not task.completed
            return True
        return False