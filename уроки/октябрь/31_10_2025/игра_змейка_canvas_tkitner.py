#pygame
import random
import tkinter as tk

w = tk.Tk()
w.title('Змейка')
canvas = tk.Canvas(w, width=300, height=300)
canvas.pack()

c = 20
sneek = [
    (100, 100)
]

food = (
    random.randint(0, 14)*c,random.randint(0, 14)*c
)
dir_x, dir_y = c, 0

def draw():
    canvas.delete('all')
    for x, y in sneek:
        canvas.create_rectangle(x,y, x+c, y+c, fill='#000')
    fx, fy = food
    canvas.create_oval(fx, fy, fx+c, fy+c, fill='#f00')

    canvas.create_text(50, 15, text=f'Счет: {len(sneek)-1}', font=('Arial', 15), fill='#000')

def move():
    global food
    head_x, head_y = sneek[0]
    new_head = (head_x + dir_x, head_y + dir_y)
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= 300 or new_head[1] >= 300 or new_head in sneek:
        return
    sneek.insert(0, new_head)
    if new_head == food:
        food = (
            random.randint(0, 14) * c, random.randint(0, 14) * c
        )
    else:
        sneek.pop()

    draw()
    w.after(150, move)


def change_dir(x, y):
    global dir_x, dir_y
    dir_x, dir_y = x, y

w.bind('<Right>', lambda e: change_dir(c, 0))
w.bind('<Left>', lambda e: change_dir(-c, 0))
w.bind('<Up>', lambda e: change_dir(0, -c))
w.bind('<Down>', lambda e: change_dir(0, c))


draw()
move()


'''
[(20, 20), (20, 20), (40, 40)]

'''

w.mainloop()