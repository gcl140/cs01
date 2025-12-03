from cs1lib import *

mx = 0
nx = 0
my = 0
ny = 0
px = 0
py = 0
enter = False
lefted = False
move = False
pressedi = False

program_counter = 0

def entered(x, y):
    global mx, my, enter
    enter = True
    mx = x
    my = y

def left(x, y):
    global nx, ny, lefted, pressedi
    pressedi = False
    # lefted = True
    nx = x
    ny = y

def pressedii(x, y):
    global px, py, pressedi
    print(x, y)
    pressedi = True
    px = x
    py = y
    # pass

def moved(x, y):
    global ox, oy, move
    # print(x, y)
    move = True
    ox = x
    oy = y

def art():
    global program_counter, pressedi, move
    if program_counter == 0:
        clear()
        set_fill_color(0, 0, 0)
        draw_rectangle(0, 0, 400, 400)


    set_stroke_width(3)
    # draw_point(mx, my)
    set_stroke_width(0)

    set_stroke_width(3)
    set_stroke_color(1, 1, 1)
    # draw_point(nx, ny)
    if pressedi:
        draw_point(px, py)
        if move:
            draw_point(ox, oy)
    # draw_line(mx, my, nx, ny)
    set_stroke_width(0)
    program_counter += 1

start_graphics(art, 
            #    mouse_press=entered,
                mouse_release=left, mouse_move=moved, 
                mouse_press=pressedii
                )