from cs1lib import *

mx = 0
nx = 0
my = 0
ny = 0
px = 0
py = 0
enter = False
lefted = False
moving = False

program_counter = 0

def entered(x, y):
    global mx, my, enter
    enter = True
    mx = x
    my = y

def left(x, y):
    global nx, ny, lefted
    lefted = True
    nx = x
    ny = y

def move(x, y):
    global px, py, moving
    print(x, y)
    moving = True
    px = x
    py = y
    # pass

def art():
    global program_counter
    if program_counter == 0:
        clear()
        print("called once")
        set_fill_color(0, 0, 0)
        draw_rectangle(0, 0, 400, 400)

    # if enter:
    #     set_stroke_width(3)
    #     draw_point(mx, my)
    #     set_stroke_width(0)

    set_stroke_width(3)
    draw_point(mx, my)
    set_stroke_width(0)

    set_stroke_width(3)
    set_stroke_color(1, 1, 1)
    draw_point(nx, ny)
    draw_point(px, py)
    # draw_line(mx, my, nx, ny)
    set_stroke_width(0)
    program_counter += 1

# start_graphics(art, mouse_press=entered)
start_graphics(art, 2400, mouse_press=entered, mouse_release=left, mouse_move=move)