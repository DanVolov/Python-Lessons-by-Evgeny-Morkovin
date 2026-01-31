from datetime import datetime, timedelta


class Priority:
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, title, description, priority=Priority.MEDIUM):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = None
        self.created = datetime.now()
        self.status = False

    def set_deadline(self, days):
        self.deadline = datetime.now() + timedelta(days=days)

    def set_status(self):
        self.status = True

    def __str__(self):
        return f'{self.title} {self.description} {self.priority} {self.deadline} {self.status}'


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.members = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_member(self, member):
        self.members.append(member)

    def get_tasks_pending(self):
        tasks_pending = []
        for task in self.tasks:
            if not task.status:
                tasks_pending.append(task)
        return tasks_pending

    def get_tasks_completed(self):
        tasks_pending = []
        for task in self.tasks:
            if task.status:
                tasks_pending.append(task)
        return tasks_pending


    def get_tasks_by_priority(self, priority):
        tasks_pending = []
        for task in self.tasks:
            if task.priority == priority and task.status == False:
                tasks_pending.append(task)
        return tasks_pending


class User:
    def __init__(self, login, email):
        self.login = login
        self.email = email
        self.projects = []

    def create_project(self, project_name):
        if not project_name:
            raise ValueError('Project name cannot be empty')
        project = Project(project_name)
        project.add_member(self)
        self.projects.append(project)
        return project


    def get_all_tasks(self):
        all_tasks = []
        for project in self.projects:
            all_tasks.extend(project.tasks)
        return all_tasks


user = User('user1', 'user1@user.ru')
project = user.create_project('project1')

task1 = Task('Task #1', 'Task #1', Priority.HIGH)
task1.set_deadline(3)

task2 = Task('Task #2', 'Task #2', Priority.LOW)
task2.set_deadline(1)


project.add_task(task1)
project.add_task(task2)

task2.status = True

for task in project.get_tasks_completed():
    print(task)
