# Импорт модулей
import customtkinter as ctk
from math import sqrt

# Создание окна
root = ctk.CTk()
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
root.geometry("330x500")
root.title("Calculator")
root.iconbitmap('icon.ico')

# Функция для ввода только чисел и математических символов
def validate(event):
    allowed_chars = set('0123456789+-*/()., ')
    special_keys = {
        'BackSpace', 'Delete', 'Left', 'Right',
        'Home', 'End', 'Tab', 'Return'
    }
    if event.keysym in special_keys:
        return
    if event.char not in allowed_chars:
        return "break"

input_field = ctk.CTkEntry(root, placeholder_text='0', justify='right', height=125, font=('Arial', 60))
input_field.pack(fill='x')

# Функция для добавления символа в поле ввода
def insert_symbol(symbol):
    current_text = input_field.get()
    if current_text == '0' and symbol not in {'.', ','}:
        input_field.delete(0, 'end')
    if symbol == ',':
        symbol = '.'
    input_field.insert('end', symbol)

# Функция для обработки всех операторов
def handle_operator(operator):
    current_text = input_field.get()
    if operator == '=':
        try:
            expression = current_text.replace(',', '.').replace('÷', '/')
            result = eval(expression)
            input_field.delete(0, 'end')
            if isinstance(result, float) and result.is_integer():
                input_field.insert(0, str(int(result)))
            else:
                input_field.insert(0, str(result))
        except:
            input_field.delete(0, 'end')
            input_field.insert(0, 'Error')
    elif operator == 'C':
        input_field.delete(0, 'end')
        input_field.insert(0, '0')
    elif operator == 'CE':
        input_field.delete(0, 'end')
        input_field.insert(0, '0')
    elif operator == '⌫':
        if current_text and current_text != '0':
            new_text = current_text[:-1]
            input_field.delete(0, 'end')
            if new_text:
                input_field.insert(0, new_text)
            else:
                input_field.insert(0, '0')
    elif operator == '±':
        if current_text and current_text != '0':
            if current_text[0] == '-':
                input_field.delete(0, 'end')
                input_field.insert(0, current_text[1:])
            else:
                input_field.delete(0, 'end')
                input_field.insert(0, '-' + current_text)
    elif operator == '%':
        try:
            expression = current_text.replace(',', '.').replace('÷', '/')
            result = eval(expression) / 100
            input_field.delete(0, 'end')
            input_field.insert(0, str(result))
        except:
            input_field.delete(0, 'end')
            input_field.insert(0, 'Error')
    elif operator == '1/x':
        try:
            value = float(current_text.replace(',', '.'))
            if value != 0:
                result = 1 / value
                input_field.delete(0, 'end')
                input_field.insert(0, str(result))
            else:
                input_field.delete(0, 'end')
                input_field.insert(0, 'Error')
        except:
            input_field.delete(0, 'end')
            input_field.insert(0, 'Error')
    elif operator == 'x²':
        try:
            value = float(current_text.replace(',', '.'))
            result = value ** 2
            input_field.delete(0, 'end')
            input_field.insert(0, str(result))
        except:
            input_field.delete(0, 'end')
            input_field.insert(0, 'Error')
    elif operator == '√x':
        try:
            value = float(current_text.replace(',', '.'))
            if value >= 0:
                result = sqrt(value)
                input_field.delete(0, 'end')
                input_field.insert(0, str(result))
            else:
                input_field.delete(0, 'end')
                input_field.insert(0, 'Error')
        except:
            input_field.delete(0, 'end')
            input_field.insert(0, 'Error')
    else:
        insert_symbol(operator)

# Функция для очистки поля ввода
def clear_display():
    input_field.delete(0, 'end')
    input_field.insert(0, '0')

# Создание frame для кнопок
buttons_frame = ctk.CTkFrame(root)
buttons_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Объявление символов
# Словарь функций для операторов и специальных кнопок
symbols = {
    '%': lambda: handle_operator('%'),
    'CE': lambda: handle_operator('CE'),
    'C': lambda: handle_operator('C'),
    '⌫': lambda: handle_operator('⌫'),
    '1/x': lambda: handle_operator('1/x'),
    'x²': lambda: handle_operator('x²'),
    '√x': lambda: handle_operator('√x'),
    '÷': lambda: insert_symbol('÷'),
    '*': lambda: insert_symbol('*'),
    '-': lambda: insert_symbol('-'),
    '+': lambda: insert_symbol('+'),
    '=': lambda: handle_operator('='),
    '±': lambda: handle_operator('±'),
    ',': lambda: insert_symbol(','),
    '(': lambda: insert_symbol('('),
    ')': lambda: insert_symbol(')')
}

# Словарь функций для цифровых кнопок
numbers = {
    '0': lambda: insert_symbol('0'),
    '1': lambda: insert_symbol('1'),
    '2': lambda: insert_symbol('2'),
    '3': lambda: insert_symbol('3'),
    '4': lambda: insert_symbol('4'),
    '5': lambda: insert_symbol('5'),
    '6': lambda: insert_symbol('6'),
    '7': lambda: insert_symbol('7'),
    '8': lambda: insert_symbol('8'),
    '9': lambda: insert_symbol('9')
}

# Матрица раскладки кнопок (6 строк, 4 столбца)
buttons_layout = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√x', '÷'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['±', '0', ',', '=']
]

# Создание кнопок перебором матрицы раскладки
for row_idx, row in enumerate(buttons_layout):
    for col_idx, button_text in enumerate(row):
        if button_text in ['=', '+', '-', '*', '÷']:
            button_color = "#00f"
            text_color = "white"
        elif button_text in ['C', 'CE', '⌫']:
            button_color = "#f00"
            text_color = "white"
        elif button_text in ['%', '1/x', 'x²', '√x', '±', ',']:
            button_color = "#d3d3d3"
            text_color = "black"
        else:
            button_color = "#f0f0f0"
            text_color = "black"
        if button_text in symbols:
            command = symbols[button_text]
        elif button_text in numbers:
            command = numbers[button_text]
        else:
            command = None
        button = ctk.CTkButton(
            buttons_frame,
            text=button_text,
            command=command,
            width=70,
            height=70,
            font=('Arial', 24),
            fg_color=button_color,
            text_color=text_color,
            hover_color=button_color
        )
        button.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky='nsew')
    buttons_frame.grid_rowconfigure(row_idx, weight=1)
    buttons_frame.grid_columnconfigure(col_idx, weight=1)

# Бинд для ввода чисел с клавиатуры
input_field.bind("<Key>", validate)

# Запуск главного цикла обработки событий
root.mainloop()