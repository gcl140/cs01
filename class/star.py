from cs1lib import *

def polygon(x_list, y_list):
    draw_polygon( zip(x_list, y_list) )


y = [86, 80, 43, 80, 86, 116, 158, 138, 158, 116]

def star():
    x = [161, 119, 100, 81, 39, 70, 63, 100, 137, 130]
    # y = [86, 80, 43, 80, 86, 116, 158, 138, 158, 116]
    # global y #no need, y is the address of the list not the actual list values
    set_clear_color(1, 1, 1)
    set_fill_color(1, 1, 0)

    clear()
    polygon(x, y)
    for i in range(len(y)):
        print(y[0])
        # x[i] = x[i] + 50
        y[i] = y[i] + 1

start_graphics(star, 1)
