import tkinter as tk


window = tk.Tk()
window.title("Widgets")

#grid
l1 = tk.Label(text='1')
l1.grid(row=0, column=0)

l2 = tk.Label(text='2')
l2.grid(row=0, column=1)

l3 = tk.Label(text='3')
l3.grid(row=0, column=2)



window.mainloop()