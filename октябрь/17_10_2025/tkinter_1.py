#checkbox, radiobutton, listbox, combox, progressbar, menu, notebook, canvas

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Widgets")
#window.geometry("300x300")

main_menu = tk.Menu(window)
#main_menu.add_cascade(label="File")
#main_menu.add_cascade(label="Edit")
#main_menu.add_cascade(label="view")

def exit_window():
    window.destroy()
file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
settings_menu = tk.Menu(tearoff=0)
settings_menu.add_command(label="Save")
settings_menu.add_command(label="Open")
file_menu.add_cascade(label="Settings", menu=settings_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_window)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="view")

window.config(menu=main_menu)

enabled = tk.IntVar()
def ff():
    if enabled.get() == 1:
        tx.configure(text='Ok')
    else:
        tx.configure(text='Not Ok')
ch = tk.Checkbutton(window, text="Checkbutton", variable=enabled, command=ff)
ch.pack()

tx = tk.Label(window, text=enabled.get())
tx.pack()

position = {'padx': 6, 'pady': 6, 'anchor': tk.NW}

def fff():
    print(lang.get())
python = 'Python'
java = 'Java'
javascript = 'JavaScript'
lang = tk.StringVar(value=java)

python_btn = tk.Radiobutton(window, value=python, text=python, variable=lang, command=fff)
python_btn.pack()

java_btn = tk.Radiobutton(window, value=java,text=java, variable=lang, command=fff)
java_btn.pack()

js_btn = tk.Radiobutton(window, value=javascript,text=javascript, variable=lang, command=fff)

js_btn.pack()

def add_element():
    element = entry_element.get()
    l.insert(0, element)

def delete_element():
    try:
        index = l.curselection()
        l.delete(index[0])
    except:
        messagebox.showerror('Error', 'No such element')


languages = ['Python', 'JavaScript', 'Java']
lang_var = tk.Variable(value=languages)

l = tk.Listbox(listvariable=lang_var)
l.pack()

entry_element = tk.Entry(window)
entry_element.pack()
add_btn = tk.Button(window, text="Add", command=add_element)
add_btn.pack()

delete_btn = tk.Button(window, text='Delete', command=delete_element)
delete_btn.pack()


languages = ['Python', 'JavaScript', 'Java']
l_v = tk.StringVar(value=languages[0])
c = ttk.Combobox(window, values=languages, textvariable=l_v)
c.pack()

ttk.Progressbar(window, length=100, value=40, orient='horizontal').pack()
ttk.Progressbar(window, length=100, value=40, orient='vertical').pack()


value_var = tk.IntVar(value=30)
progress = ttk.Progressbar(window, length=100, orient='horizontal', variable=value_var)
progress.pack()

def start():
    progress.start(1000)

def stop():
    progress.stop()

l_1 = ttk.Label(window, text=value_var.get())
l_1.pack()
start_btn = tk.Button(window, text="Start", command=start)
start_btn.pack()
stop_btn = tk.Button(window, text="Stop", command=stop)
stop_btn.pack()


#notebook


notebook = ttk.Notebook(window)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame1.pack()
frame2.pack()


notebook.add(frame1, text='Frame 1')
notebook.add(frame2, text='Frame 2')

python_logo = tk.PhotoImage(file='img.png', width=32, height=32)
java_logo = tk.PhotoImage(file='img_1.png', width=32, height=32)
notebook.add(frame1, image=python_logo, text='Python', compound='left')
notebook.add(frame2, image=java_logo, text='Java', compound='left')




window.mainloop()