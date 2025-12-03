from cs1lib import *

#(x, y). This point (x, y) is always paired with the point (y, WIN_SIZE - x)
WIN_SIZE = 400
step = 20
x, y1, x2 = 0, 0, 0
y, y2, x3 = WIN_SIZE, WIN_SIZE, WIN_SIZE
has_called = False
def string_art():
    global has_called, x, y, y1, x2, y2, x3

    if has_called != True:
        clear()

    if x < WIN_SIZE and y > 0:
        y -= step
        x += step
        draw_line(0, y, x, 0)
        print(0, y, x, 0, "one")

    if y1 < WIN_SIZE:
        y1 += step
        draw_line(WIN_SIZE, y1, y1, 0)
        print(y1, 0, WIN_SIZE, y1, "two")
    
    if x2 < WIN_SIZE and y2 > 0:
        x2 += step
        y2 -= step
        draw_line(WIN_SIZE, x2, y2,WIN_SIZE)
        print(WIN_SIZE, x2, y2,WIN_SIZE, "three")

    if x3 > 0:
        x3 -= step
        draw_line(x3, WIN_SIZE, 0, x3)


    has_called = True

# print(x)
# print(y)
start_graphics(string_art)