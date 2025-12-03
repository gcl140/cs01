from cs1lib import *

WIN_SIZE = 400
STEP = 20
# x, y1, x2 = 0, 0, 0
x, y, y2, x3 = 400, 400, WIN_SIZE, WIN_SIZE

px, py1, px2 = 0, 0, 0
py, py2, px3 = WIN_SIZE, WIN_SIZE, WIN_SIZE

has_called = False

def draw_points():
    global has_called, px, py, py1, px2, py2, px3

    if px < WIN_SIZE and py > 0:
        py -= STEP
        px += STEP
        draw_point(0, py)

    if py1 < WIN_SIZE:
        py1 += STEP
        draw_point(py1, 0)
    
    if px2 < WIN_SIZE and py2 > 0:
        px2 += STEP
        py2 -= STEP
        draw_point(WIN_SIZE, px2)

    if px3 > 0:
        px3 -= STEP
        draw_point(px3, WIN_SIZE)


def draw_lines():
    global has_called, x, y, y1, x2, y2, x3

    if x < WIN_SIZE and y > 0:
        y -= STEP
        x += STEP
        draw_line(0, y, x, 0)

    if y1 < WIN_SIZE:
        y1 += STEP
        draw_line(WIN_SIZE, y1, y1, 0)
    
    if x2 < WIN_SIZE and y2 > 0:
        x2 += STEP
        y2 -= STEP
        draw_line(WIN_SIZE, x2, y2,WIN_SIZE)

    if x3 > 0:
        x3 -= STEP
        draw_line(x3, WIN_SIZE, 0, x3)


def string_art():
    global has_called, x, y, y1, x2, y2, x3

    if has_called != True:
        clear()
    x += STEP
    y += STEP
    draw_line(x, y, y, WIN_SIZE - x)
    print(x, y, y, WIN_SIZE - x)


    # set_stroke_width(5)
    # draw_points()
    # set_stroke_width(0)
    # draw_lines()

    has_called = True

start_graphics(string_art, framerate=7.5)