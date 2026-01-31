from models import TaskModel
from views import TaskView
from controllers import TaskController


model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

model.create_task('Task1', 'Desc1')
model.create_task('Task2', 'Desc2')


controller.run()