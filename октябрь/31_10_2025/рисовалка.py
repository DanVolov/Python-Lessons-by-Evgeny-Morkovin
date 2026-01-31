#pygame
import random
import tkinter
import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk

w = tk.Tk()
w.title('Рисовалка')
canvas = tk.Canvas(w, width=300, height=300)
canvas.pack()
current_color = '#000'
def paint(event):
    global current_color
    x,y = event.x, event.y
    canvas.create_oval(x-a,y-a,x+a,y+a,fill=current_color, outline=current_color)

def clear():
    canvas.delete('all')

canvas.bind('<B1-Motion>', paint)

btn = tk.Button(text='Clear',command=clear)
btn.pack()

def color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color


btn_color = tk.Button(text='Color',command=color)
btn_color.pack()

text = tkinter.Label(text='Введите рамзер:')
text.pack()

size = [2, 4, 8, 16, 32, 64]
l_v = tk.IntVar(value=size[0])
c = ttk.Combobox(w, values=size, textvariable=l_v)
c.pack()
a = 0

def update():
    global a
    a = l_v.get()
    w.after(500, update)

update()

w.mainloop()