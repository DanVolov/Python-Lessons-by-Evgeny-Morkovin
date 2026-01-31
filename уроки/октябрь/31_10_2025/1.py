#CANVAS
import tkinter as tk

w = tk.Tk()
w.title("Canvas")
w.geometry('300x300')

canvas = tk.Canvas(w, width=250, height=250, background='white')
canvas.pack(anchor='center', expand=1)


#рисование линии
canvas.create_line(0,0,250, 250,fill='black',width=5, dash=2)

#создание прямоугольника
canvas.create_rectangle(50, 50, 200, 200, outline='#912', fill='#5ab')

#создание многоугольника
canvas.create_polygon(10, 30, 200, 200, 200, 30, fill='#912', outline='#5ab')

points = (
    (10, 30),
    (200, 200),
    (200, 30)
)
canvas.create_polygon(*points, fill='#912', outline='#5ab')

#создание_дуги
canvas.create_arc((10, 10), (200, 200), fill='#5ab')

#добавление текста

canvas.create_text(50, 50, text='Hello', fill='#5ab', anchor='center', font=('Arial', 40))

#добавление изображение

img = tk.PhotoImage(file='img.png')
canvas.create_image(10, 10, image=img, anchor='nw')

#добавление круга
canvas.create_oval(10, 10, 200, 200, fill='#912', outline='#5ab')


#добавление виджета

btn = tk.Button(text='Click')
canvas.create_window(10, 10, window=btn)

w.mainloop()