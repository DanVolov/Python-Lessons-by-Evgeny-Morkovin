from settings import *
from tkinter import *
from tkinter import  messagebox

mode = True
matrix = None
matrix_buttons = None
main_root = None

def create_matrix(rows, cols, value=0):
    matrix = []
    global matrix_buttons
    matrix_buttons = []
    for i in range(rows): #i=0 i=1 i=2
        row = []
        for j in range(cols): #i=0 j=0,1,2  i=1 j=0,1,2 i=2 j=0,1,2 [0,0,0]
            row.append(value)
        matrix.append(row) #[[0,0,0],[0,0,0],[0,0,0]]
        matrix_buttons.append(row)
    return matrix



def print_matrix(m):

    for i in range(len(m)):
        for j in range(len(m[i])):
            btn = Button(text=m[i][j], width=15, height=10, command=lambda i=i,j=j: click_btn(i,j), font=("Arial", 14))
            btn.grid(row=i, column=j)
            matrix_buttons[i][j] = btn





def click_btn(i,j):
    global mode, matrix, matrix_buttons

    if mode:
        if matrix_buttons[i][j]['text'] == '-':
            matrix_buttons[i][j].configure(text='x')
            mode = False
    else:
        if matrix_buttons[i][j]['text'] == '-':
            matrix_buttons[i][j].configure(text='0')
            mode = True
    a = winner('0')
    b = winner('x')
    k = get_count_button()
    if a == False and b == False and k == 0:
        messagebox.showerror('Error', 'No winner')
        clear()
    if a:
        messagebox.showerror('Error', 'Winner 0')
        clear()
    if b:
        messagebox.showerror('Error', 'Winner x')
        clear()


def clear():
    for i in range(len(matrix_buttons)):
        for j in range(len(matrix_buttons)):
            matrix_buttons[i][j]['text'] = '-'

def get_count_button():
    global mode, matrix, matrix_buttons
    k = 0
    for i in matrix_buttons:
        for j in i:
            if j['text'] == '-':
                k += 1
    return k

'''
0 1 2
0 0 0 0
0 0 0 1
0 0 0 2
'''
def winner(v):
    global mode, matrix, matrix_buttons
    if (matrix_buttons[0][0]['text'] == v and matrix_buttons[0][1]['text'] == v and matrix_buttons[0][2]['text'] == v) \
        or (matrix_buttons[1][0]['text'] == v and matrix_buttons[1][1]['text'] == v and matrix_buttons[1][2]['text'] == v) \
        or (matrix_buttons[2][0]['text'] == v and matrix_buttons[2][1]['text'] == v and matrix_buttons[2][2]['text'] == v) \
        or (matrix_buttons[0][0]['text'] == v and matrix_buttons[1][0]['text'] == v and matrix_buttons[2][0]['text'] == v) \
        or (matrix_buttons[0][1]['text'] == v and matrix_buttons[1][1]['text'] == v and matrix_buttons[2][1]['text'] == v) \
        or (matrix_buttons[0][2]['text'] == v and matrix_buttons[1][2]['text'] == v and matrix_buttons[2][2]['text'] == v) \
        or (matrix_buttons[0][0]['text'] == v and matrix_buttons[1][1]['text'] == v and matrix_buttons[2][2]['text'] == v) \
        or (matrix_buttons[0][2]['text'] == v and matrix_buttons[1][1]['text'] == v and matrix_buttons[2][0]['text'] == v):
            return True
    else:
        return False

def main(tk):
    global matrix, main_root
    #tk.geometry(f'{WIDTH}x{HEIGHT}')
    tk.title(TITLE)
    main_root = tk

    matrix = create_matrix(3, 3, '-')
    print_matrix(matrix)





    '''mode = False
    while True:
        print_matrix(matrix)
        if not mode:
            print('Ходит X')
            row = int(input('Enter the row number: '))
            col = int(input('Enter the column number: '))
            row -= 1
            col -= 1
            if matrix[row][col] == '-':
                matrix[row][col] = 'X'
                mode = True
            else:
                print('Error')
        else:
            print('Ходит 0')
            row = int(input('Enter the row number: '))
            col = int(input('Enter the column number: '))
            row -= 1
            col -= 1
            if matrix[row][col] == '-':
                matrix[row][col] = '0'
                mode = False
            else:
                print('Error')'''