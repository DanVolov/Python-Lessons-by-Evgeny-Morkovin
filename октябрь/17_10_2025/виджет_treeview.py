import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Widgets")

columns = ('name', 'age', 'email')
tree = ttk.Treeview(window, columns=columns, show='headings')
tree.pack()

tree.heading('name', text='Имя')
tree.heading('age', text='Возраст')
tree.heading('email', text='Email')

users = [
    ('User 1', 22, 'user1@gmail.com'),
    ('User 2', 23, 'user2@gmail.com'),
    ('User 3', 24, 'user3@gmail.com'),
]

for i in users:
    tree.insert('', tk.END, values=i)

window.mainloop()