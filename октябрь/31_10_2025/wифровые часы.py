#CANVAS
import tkinter as tk
import datetime
import random

w = tk.Tk()
w.title("Canvas")
w.geometry('700x700')

canvas = tk.Canvas(w, width=400, height=400, background='white')
canvas.pack(anchor='center', expand=1)
backgrounds = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
def update():
    canvas.delete('all')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    canvas.create_oval(20, 20, 380, 380, fill=random.choice(backgrounds), outline='#5ab')
    canvas.create_text(200, 200,anchor='center', text=time, font=('Arial', 30), fill='#fff')
    w.after(1000, update)

update()

w.mainloop()