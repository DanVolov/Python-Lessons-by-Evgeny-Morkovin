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
                if tasks:
                    task_id_input = self.view.get_input('Введите id задачи для изменения статуса (или Enter для возврата): ')
                    if task_id_input.strip():
                        task_id = int(task_id_input)
                        if self.model.toggle_task_completed(task_id):
                            self.view.print_message('Статус задачи изменен')
                        else:
                            self.view.print_message('Задача не найдена')
            elif n == '2':
                task_name = self.view.get_input('Введите название задачи: ')
                task_description = self.view.get_input('Введите описание задачи: ')
                while True:
                    priority_input = self.view.get_input('Введите приоритет (1-3): ')
                    priority = int(priority_input)
                    if 1 <= priority <= 3:
                        break
                    else:
                        self.view.print_message('Приоритет должен быть от 1 до 3')
                self.model.create_task(task_name, task_description, priority)
                self.view.print_message('Задача добавлена')
            elif n == '3':
                task_id = int(self.view.get_input('Введите id задачи: '))
                self.model.delete_task(task_id)
                self.view.print_message('Задача удалена')
            elif n == '4':
                break
            else:
                self.view.print_message('Команда не распознана')