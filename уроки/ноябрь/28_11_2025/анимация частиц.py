import tkinter as tk
import random

w = tk.Tk()
w.title('animation')
canvas = tk.Canvas(w, width=200, height=200, bg='white')
canvas.pack()

particlce = []

def create(count):
    global canvas, particlce
    for i in range(count):
        x, y = random.randint(0, 200), random.randint(0, 200)
        size = random.randint(1, 6)
        speed_x, speed_y = random.randint(-2, 2), random.randint(-2, 2)
        color = random.choice(['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'cyan'])
        oval = canvas.create_oval(x, y, x+size, y+size, fill=color)
        particlce.append({'id': oval, 'x': x, 'y': y, 'size': size, 'color': color, 'speed_x': speed_x, 'speed_y': speed_y})

create(50)
def animate():
    global canvas, particlce
    for j in particlce:
        j['x'] += j['speed_x']
        j['y'] += j['speed_y']
        if j['x'] <= 0 or j['x'] >= 200:
            j['speed_x'] = -j['speed_x']
        if j['y'] <= 0 or j['y'] >= 200:
            j['speed_y'] = -j['speed_y']
        canvas.coords(j['id'], j['x'], j['y'], j['x'] + j['size'], j['y'] + j['size'])
    w.after(30, animate)
animate()
w.mainloop()