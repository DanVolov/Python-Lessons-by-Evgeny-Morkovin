from email.policy import default

import customtkinter as ctk
import os
import dotenv
dotenv.load_dotenv()

'''
Задачи
- название задачи
- категория
- приоритет
'''
settings = None
current_theme = 'Dark'
def setup():
    ctk.set_appearance_mode('Dark')
    ctk.set_default_color_theme('blue')

    w = ctk.CTk()
    w.title(os.getenv('TITLE'))
    w.geometry(f'{os.getenv("WIDTH")}x{os.getenv("HEIGHT")}')

    return w

def create_task_fame(w):
    frame = ctk.CTkFrame(w)
    frame.pack(fill='x', padx=10, pady=(10, 0))

    task_entry = ctk.CTkEntry(frame, placeholder_text='Введите название задачи')
    task_entry.pack(side='left', fill='x', padx=10, pady=10)

    category_var = ctk.StringVar(value='Личное')
    category_combo = ctk.CTkComboBox(frame, values=['Личное', 'Рабочие', 'Учеба'], variable=category_var)
    category_combo.pack(side='left', padx=10, pady=10)

    priority_var = ctk.StringVar(value='Низкий')
    priority_entry = ctk.CTkComboBox(frame, values=['Низкий', 'Средний', 'Высокий'], variable=priority_var)
    priority_entry.pack(side='left', padx=10, pady=10)

    date_entry = ctk.CTkEntry(frame, placeholder_text='ГГГГ-ММ-ДД', width=100)
    date_entry.pack(side='left', padx=10, pady=10)

    time_entry = ctk.CTkEntry(frame, placeholder_text='ЧЧ:ММ', width=80)
    time_entry.pack(side='left', padx=10, pady=10)


    return  frame, task_entry, category_var, priority_entry, date_entry, time_entry

def change_theme():
    global settings
    settings = ctk.CTk()
    settings.geometry('400x200')
    settings.title(os.getenv('TITLE'))

    create_widgets_settings()

    settings.mainloop()
def change_theme_(ch_):
    global current_theme
    if ch_.get():
        ctk.set_appearance_mode('Light')
        ctk.set_default_color_theme('blue')
        current_theme = 'Light'

    else:
        current_theme = 'Dark'
        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('blue')


def create_widgets_settings():
    global settings
    label = ctk.CTkLabel(settings, text='Сменить тему')
    label.pack(fill='x', padx=10, pady=10)
    ch_ = ctk.BooleanVar(value=False)
    button = ctk.CTkCheckBox(settings, text=current_theme, variable=ch_, command=lambda ch_=ch_: change_theme_(ch_))
    button.pack(fill='x', padx=10, pady=10)

def create_buttons(w):
    frame_button = ctk.CTkFrame(w)
    frame_button.pack(fill='x', padx=10)

    button_add = ctk.CTkButton(frame_button, text='Добавить')
    button_add.pack(side='left', padx=10, pady=10)

    button_change = ctk.CTkButton(frame_button, text='Сменить тему', command=change_theme)
    button_change.pack(side='left', padx=10, pady=10)

    return frame_button, button_add, button_change



def create_frame_tasks(w, task):
    from functions import backend
    frame = ctk.CTkFrame(w)
    frame.pack(fill='x', pady=10)

    checkbox_var = ctk.BooleanVar(value=task['status'])

    checkbox = ctk.CTkCheckBox(frame, variable=checkbox_var, text='Выполнено' if task['status'] else 'Не выполнена',command=lambda task=task: backend.change_status(task['created'], checkbox_var.get()))

    checkbox.pack(side='left', padx=10)
    text_label = ctk.CTkLabel(frame, text=task['title'], font=ctk.CTkFont(weight='bold' if task['priority'] == 'Высокий' else 'normal')) # !
    text_label.pack(side='left', padx=10)

    category_label = ctk.CTkLabel(frame, text=task['category'])
    category_label.pack(side='left', padx=10)

    delete_btn = ctk.CTkButton(  # !
        frame,
        text='Удалить',
        fg_color='#C0392B',
        hover_color='#922B21',
        command=lambda task=task: backend.remove_task(task['created'])
    )

    delete_btn.pack(side='left', padx=10, pady=10)

    return frame # !

