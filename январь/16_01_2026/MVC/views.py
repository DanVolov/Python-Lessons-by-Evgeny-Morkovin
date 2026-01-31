class TaskView:

    def show_menu(self):
        print('Меню:')
        print('1. Показать все задачи')
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")

    def show_tasks(self, tasks):
        if not tasks:
            print('Нет задач')
            return
        print('Список задач:')
        for task in tasks:
            print(f'{task.id} {task.title} {task.description}')

    def get_input(self, prompt):
        return input(prompt).strip()

    def print_message(self, message):
        print(message)