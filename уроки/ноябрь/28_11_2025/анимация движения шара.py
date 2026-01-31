import tkinter as tk

w = tk.Tk()
w.title('animation')
canvas = tk.Canvas(width=200, height=200)
canvas.pack()

oval = canvas.create_oval(10, 10, 60, 60, fill='red')

x_speed = 5
y_speed = 5
animation_running = False


def start_animate():
    global animation_running
    if not animation_running:
        animation_running = True
        animate()


def stop_animate():
    global animation_running
    if animation_running:
        animation_running = False


def clear_animate():
    stop_animate()
    canvas.coords(oval, 10, 10, 60, 60)


def animate():
    global animation_running, canvas, x_speed, y_speed, oval
    if not animation_running:
        return
    canvas.move(oval, x_speed, y_speed)
    x1, y1, x2, y2 = canvas.coords(oval)
    if x1 <= 0 or x2 >= 200:
        x_speed = -x_speed
    if y1 <= 0 or y2 >= 200:
        y_speed = -y_speed
    w.after(30, animate)


start = tk.Button(w, text='Старт', command=start_animate)
start.pack()

stop = tk.Button(w, text='Стоп', command=stop_animate)
stop.pack()

clear = tk.Button(w, text='Сброс', command=clear_animate)
clear.pack()






w.mainloop()