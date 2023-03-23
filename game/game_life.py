import tkinter as tk
import random

CELL_SIZE = 5
ROWS = 126
COLS = 126

paused = False

def init_game(master):

    canvas = tk.Canvas(master, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='black',bd=0, highlightthickness=0)
    canvas.pack()
    grid = [[random.randint(0,1) for j in range(COLS)] for i in range(ROWS)]

    draw_grid(canvas, grid)

    return grid, canvas

def draw_grid(canvas, grid):

    canvas.delete('cell')
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                x0 = j*CELL_SIZE
                y0 = i*CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                canvas.create_rectangle(x0, y0, x1, y1, fill='white', tags='cell')

def count_neighbors(grid, i, j):
    count = 0
    for row in range(i-1, i+2):
        for col in range(j-1, j+2):
            if (row != i or col != j) and 0 <= row < ROWS and 0 <= col < COLS:
                count += grid[row][col]
    return count

def update(canvas, grid):

    if paused:
        canvas.after(100, update, canvas, grid)
        return
    
    new_grid = [[0 for j in range(COLS)] for i in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(grid,i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
                           
    grid = new_grid
    draw_grid(canvas, grid)
    canvas.after(120, update, canvas, grid)

def pause_game(bton):

    global paused

    paused = not paused

    if paused:
        bton.config(text='Play')
    else:
        bton.config(text='Pause')


def start_game(master, bton):

    bton.config(state='disabled')
    bton.configure(bg="#BDBBBB", cursor="arrow")

    grid, canvas = init_game(master)

    update(canvas, grid)
