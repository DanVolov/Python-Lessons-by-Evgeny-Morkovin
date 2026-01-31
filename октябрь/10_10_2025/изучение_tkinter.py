import tkinter
#from tkinter import *
#import tkinter as tk
from tkinter import messagebox


main = tkinter.Tk() #создание окна (создание обьекта - ООП)

main.title('Моя первая программа')
main.geometry('700x500')
main.resizable(False, False)
#.ico  .png
#main.iconbitmap(default='icon.ico')

icon = tkinter.PhotoImage(file='img.png')
main.iconphoto(False, icon)

#добавление текста
header = tkinter.Label(text='Моя первая программа', bg='#1ba', fg='#fff', font=('Tahoma', 20)) #создание виджета Label
header.pack(padx=10, pady=20) #grid()

#добавление изображения
#icon_1 = tkinter.PhotoImage(file='img_1.png')
#image_label = tkinter.Label(main, image=icon_1)
#image_label.pack(padx=10, pady=20)

login_label = tkinter.Label(text='Login: ')
login_label.pack() #grid()
#ENtry - представляет поле для ввода текста
login = tkinter.Entry(main,  font=('Tahoma', 20))
login.pack(padx=10)


password_label = tkinter.Label(text='Password: ')
password_label.pack() #grid()
#ENtry - представляет поле для ввода текста
password = tkinter.Entry(main,  font=('Tahoma', 20), show='*')
password.pack(padx=10)

def reg():
    l = login.get()
    p = password.get()
    if l == '' or p == '':
        messagebox.showerror('Error', 'Error login or/and password')
    else:
        with open('users.txt', 'a') as f:
            f.write(f'login:{l};password:{p}\n')
            messagebox.showinfo('Success', 'Reg successfully')
            login.delete(0, 'end')
            password.delete(0, 'end')

button = tkinter.Button(text='Регистрация', bg='green', fg='white', font=('Tahoma', 20),command=reg)
button.pack(padx=10, pady=20)
def auth():
    def auth_in():
        login_auth = login_1.get()
        password_auth = password_1.get()
        m = False
        with open('users.txt', 'r') as f:
            for line in f:
                c = line.split(';')
                ll = c[0].split(':')[1]
                pp = c[1].split(':')[1].replace('\n', '')
                if login_auth == ll and password_auth == pp:
                    messagebox.showinfo('Success', 'Auth successfully')
                    m = True
                    break

        if not m:
            messagebox.showerror('Error', 'Auth failed')

    authoriztion = tkinter.Tk()
    login_label_1 = tkinter.Label(authoriztion, text='Login: ')
    login_label_1.pack()  # grid()
    login_1 = tkinter.Entry(authoriztion, font=('Tahoma', 20))
    login_1.pack(padx=10)

    password_label_1 = tkinter.Label(authoriztion, text='Password: ')
    password_label_1.pack()  # grid()
    password_1 = tkinter.Entry(authoriztion, font=('Tahoma', 20), show='*')
    password_1.pack(padx=10)

    button_3 = tkinter.Button(authoriztion, text='Вход', bg='blue', fg='white', font=('Tahoma', 20), command=auth_in)
    button_3.pack(padx=10, pady=20)


button_1 = tkinter.Button(text='Авторизация', bg='blue', fg='white', font=('Tahoma', 20),command=auth)
button_1.pack(padx=10, pady=20)


main.mainloop()

'''
rgb
000
111
222
333
444
555
666
777
888
999
aaa
bbb
ccc
ddd
eee
fff

rgb
000
fff
f00
0f0
19a


Menu, progressbar, listbox, radiobutton, checkbox
'''