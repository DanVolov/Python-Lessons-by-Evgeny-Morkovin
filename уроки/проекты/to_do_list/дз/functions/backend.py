from tkinter import messagebox
from datetime import datetime

tasks = []
task_widgets = []  # !

def add_task(task_entry, category_var, priority_var, date_entry, time_enty):
    task_text = task_entry.get()
    if not task_text:
        messagebox.showerror(title="Error", message="Please enter a task.")
        return False
    new_task = {
        'title': task_text,
        'category': category_var.get(),
        'priority': priority_var.get(),
        'date': date_entry.get(),
        'time': time_enty.get(),
        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'status': False
    }


    task_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    time_enty.delete(0, 'end')
    return new_task


def click(w, task_entry, category_var, priority_var, date_entry, time_entry):
    new_task = add_task(task_entry, category_var, priority_var, date_entry, time_entry)  # !
    if new_task:  # !
        tasks.append(new_task)  
        update_tasks(w)  

def update_tasks(w=None):
    from functions.frontend import create_frame_tasks
    global task_widgets  # !
    for widget in task_widgets:  # !
        widget.destroy()
    task_widgets = []  # !
    for task in tasks: # !
        if not task:
            continue
        frame = create_frame_tasks(w, task)
        task_widgets.append(frame)  
def change_status(date, status):
    global tasks
    tasks_new = []
    for task in tasks:
        if task['created'] == date:
            task['status'] = status
        tasks_new.append(task)
    update_tasks()

def remove_task(date):
    global tasks
    tasks_new = []
    for task in tasks:
        if task['created'] != date:
            tasks_new.append(task)
    tasks = tasks_new
    update_tasks()