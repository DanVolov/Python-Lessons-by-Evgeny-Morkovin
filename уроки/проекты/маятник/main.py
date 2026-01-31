import tkinter as tk
import math

root = tk.Tk()
root.title('Маятник')
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

line_x1, line_y1, line_x2, line_y2 = 375, 100, 375, 250
oval_x1, oval_y1, oval_x2, oval_y2 = 350, 250, 400, 300
oval_width = oval_x2 - oval_x1
oval_height = oval_y2 - oval_y1

line = canvas.create_line(line_x1, line_y1, line_x2, line_y2, fill='black')
oval = canvas.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, fill='red')

pivot_x, pivot_y = line_x1, line_y1
rod_length = line_y2 - line_y1

def start_animation():
    global animation_running, time_counter
    animation_running = True
    time_counter = 0
    animate_smooth()

def animate_smooth():
    global animation_running, time_counter

    if not animation_running:
        return

    time_counter += 0.1

    amplitude = math.radians(45)
    frequency = 1.0

    angle = amplitude * math.sin(frequency * time_counter)

    center_x = pivot_x + rod_length * math.sin(angle)
    center_y = pivot_y + rod_length * math.cos(angle)

    canvas.coords(oval,
                  center_x - oval_width / 2,
                  center_y - oval_height / 2,
                  center_x + oval_width / 2,
                  center_y + oval_height / 2)

    canvas.coords(line, pivot_x, pivot_y, center_x, center_y)

    if animation_running:
        canvas.after(20, animate_smooth)

def stop_animation():
    global animation_running
    animation_running = False

animation_running = False
time_counter = 0

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

btn_start = tk.Button(control_frame, text="Старт", command=start_animation)
btn_start.pack(side='left', padx=5)

btn_stop = tk.Button(control_frame, text="Стоп", command=stop_animation)
btn_stop.pack(side='left', padx=5)

root.mainloop()