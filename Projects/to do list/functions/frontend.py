import customtkinter as ctk
import os
import dotenv
dotenv.load_dotenv()

tasks = []
'''
Задачи
- название задачи
- категория
- приоритет
'''

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


    return  frame, task_entry, category_var, priority_entry

def create_buttons(w):
    frame_button = ctk.CTkFrame(w)
    frame_button.pack(fill='x', padx=10)

    button_add = ctk.CTkButton(frame_button, text='Добавить')
    button_add.pack(side='left', padx=10, pady=10)

    button_change = ctk.CTkButton(frame_button, text='Сменить тему')
    button_change.pack(side='left', padx=10, pady=10)

    return frame_button, button_add, button_change



