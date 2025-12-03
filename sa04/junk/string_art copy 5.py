from cs1lib import *

#(x, y). This point (x, y) is always paired with the point (y, WIN_SIZE - x)
WIN_SIZE = 400
step = 20
x = 0
y = 400
has_called = False
def string_art():
    global has_called
    global x
    global y

    if has_called != True:
        clear()

    if x < 400 and y > 0:
        y -= step
        x += step
        draw_line(0, y, x, 0)
        print(0, y, x, 0)
        # draw_point(0, y)

        # x1 = 400
        y1 = y
        # print(x1, y1)
        if y1 < 400:
            # print("called")
            y1 += step
        #     x += step
            draw_line(y1, 0, 400, y1)
            # print(y, 0, x, y)
        #     draw_point(x, 0)
            # print(x, y)
        
    # print(x, y)

    # x = x - 20
    # y = y - 20
    # print(0, y, x, 0)




        # print(0, y, x, 0)
    
    # if x < 400 and y > 0:
    #     y -= step
    #     x += step
    #     # print(x)
    #     # print(y)
    #     draw_line(0, y, x, 0)
    #     draw_point(0, y)
    #     # print(0, y, x, 0)

    # if x < 400 and y > 0:
    #     y -= step
    #     x += step
    #     # print(x)
    #     # print(y)
    #     draw_line(0, y, x, 0)
    #     draw_point(0, y)
    #     # print(0, y, x, 0)
    has_called = True

# print(x)
# print(y)
start_graphics(string_art)