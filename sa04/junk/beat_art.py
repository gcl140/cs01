from cs1lib import *

#(x, y). This point (x, y) is always paired with the point (y, WIN_SIZE - x)
WIN_SIZE = 400
step = 20
x = 0
y = 0
has_called = False
def string_art():
    global has_called
    if has_called != True:
        clear()
    global x
    global y
    # x += step
    set_stroke_width(4)
    if x < 400 and y < 400:
        y += step
        x += step
        draw_line(x, y, y, WIN_SIZE - x)
        # print(x)
        print(y)
    has_called = True

print(x)
print(y)
start_graphics(string_art)