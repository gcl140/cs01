from cs1lib import *

#(x, y). This point (x, y) is always paired with the point (y, WIN_SIZE - x)
WIN_SIZE = 400
step = 20
x = 0
y = 400
y1 = 0
has_called = False
def string_art():
    global has_called
    global x
    global y
    global y1

    if has_called != True:
        clear()

    if x < 400 and y > 0:
        y -= step
        x += step
        draw_line(0, y, x, 0)
        print(0, y, x, 0)
        # # y1 = y
        # if y1 < 400:
        #     y1 += step
        #     draw_line(y1, 0, 400, y1)
        #     print(y1, 0, 400, y1, "uigohi")
        #     x2 = x
        #     y2 = y1
        #     # if 
            # y1 = y
    if y1 < 400:
        y1 += step
        draw_line(y1, 0, 400, y1)
        print(y1, 0, 400, y1, "uigohi")
        x2 = x
        y2 = y1
            # if 

    has_called = True

# print(x)
# print(y)
start_graphics(string_art)