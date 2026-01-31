#обработка, основная логика приложения, связывает models и views

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()

            n = self.view.get_input("Выберите действие: ")
            if n == '1':
                tasks = self.model.get_all_tasks()
                self.view.show_tasks(tasks)
            elif n == '2':
                task_name = self.view.get_input('Введите название задачи: ')
                task_description = self.view.get_input('Введите описание задачи: ')
                self.model.create_task(task_name, task_description)
                self.view.print_message('Задача добавлена')
            elif n == '3':
                task_id = int(self.view.get_input('Введите id задачи'))
                self.model.delete_task(task_id)
                self.view.print_message('Задача удалена')
            elif n == '4':
                break
            else:
                self.view.print_message('Команда не распознана')