from cs1lib import *

def polygon(x_list, y_list):
    draw_polygon( zip(x_list, y_list) )

def star():
    x = [161, 119, 100, 81, 39, 70, 63, 100, 137, 130]
    y = [86, 80, 43, 80, 86, 116, 158, 138, 158, 116]

    set_clear_color(1, 1, 1)
    set_fill_color(1, 1, 0)

    clear()
    polygon(x, y)

start_graphics(star, 1)
