import tkinter as tk
from time import strftime


w = tk.Tk()
w.title('animation')
#w.geometry('300x300')
now_time = strftime('%H:%M:%S')

date_label = tk.Label(w, text=now_time, font=('Arial', 40), bg='black', fg='white')
date_label.pack()

def update_time():
    now_time = strftime('%H:%M:%S')
    date_label.config(text=now_time)

    w.after(1000, update_time)

update_time()


w.mainloop()