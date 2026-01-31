#login, password, age, checkbutton(подтверждение регистрации)
import tkinter as tk
from tkinter import messagebox

main = tk.Tk()
main.title('Заголовок')

main.geometry('300x300')

def reg():
    if variable.get() == True:
        login1 = login.get()
        password1 = password.get()
        age1 = age.get()
        with open('users.txt', 'a', encoding='utf-8') as f:
            f.write(login1 + '\n')
            f.write(password1 + '\n')
            f.write(age1 + '\n')
        messagebox.showinfo('Succes', 'Регистрация прошла успешно')
    else:
        messagebox.showerror('Error', 'Text error')
l = tk.Label(text='login:')
l.pack()
login = tk.Entry(main, width=50)
login.pack()

p = tk.Label(text='password:')
p.pack()
password = tk.Entry(main, width=50)
password.pack()

a = tk.Label(text='age:')
a.pack()
age = tk.Entry(main, width=50)
age.pack()

variable = tk.BooleanVar()
c = tk.Checkbutton(main, variable=variable, text='Согласие с условиями регистрации')
c.pack()



b = tk.Button(text='Регистрация', command=reg)
b.pack()

main.mainloop()