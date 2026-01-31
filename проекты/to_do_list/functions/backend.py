from tkinter import messagebox
from datetime import datetime
tasks = []

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


def click(w, task_entry, category_var, priority_entry, date_entry, time_entry):
    tasks.append(add_task(task_entry, category_var, priority_entry, date_entry, time_entry))
    update_tasks(w)

def update_tasks(w):
    from functions.frontend import create_frame_tasks
    for task in tasks:
        pass
