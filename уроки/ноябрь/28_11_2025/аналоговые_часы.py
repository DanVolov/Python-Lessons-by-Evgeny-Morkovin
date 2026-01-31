import tkinter as tk
import math
import time

w = tk.Tk()
w.title('animate')
w.resizable(False, False)
canvas = tk.Canvas(w, width=400, height=400, bg='cyan')
canvas.pack()

central_x, central_y = 200, 200
radius = 150
def create():
    global canvas, central_x, central_y, radius
    oval = canvas.create_oval(central_x - radius, central_y - radius, central_x + radius, central_y + radius, width=2)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = central_x + (radius - 30) * math.cos(angle)
        y = central_y + (radius - 30) * math.sin(angle)
        text = canvas.create_text(x, y, text=str(i), font=('Arial', 20))

def animate():
    global canvas, central_x, central_y, radius
    canvas.delete('st')
    now_time = time.localtime()
    h = now_time.tm_hour%12
    m = now_time.tm_min
    s = now_time.tm_sec

    s_angle = math.radians(s * 6 - 90)
    x_s = central_x + (radius * 0.8) * math.cos(s_angle)
    y_s = central_y + (radius * 0.8) * math.sin(s_angle)
    s_line = canvas.create_line(central_x, central_y, x_s, y_s, tags='st')

    m_angle = math.radians(m * 6 - 90)
    x_m = central_x + (radius * 0.7) * math.cos(m_angle)
    y_m = central_y + (radius * 0.7) * math.sin(m_angle)
    m_line = canvas.create_line(central_x, central_y, x_m, y_m, tags='st')

    h_angle = math.radians(h * 6 - 90)
    x_h = central_x + (radius * 0.6) * math.cos(h_angle)
    y_h = central_y + (radius * 0.6) * math.sin(h_angle)
    h_line = canvas.create_line(central_x, central_y, x_h, y_h, tags='st')


    w.after(1000, animate)
create()
animate()
w.mainloop()