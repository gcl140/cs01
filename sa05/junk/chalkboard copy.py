from cs1lib import *

def clicked(mx, my):
    global x, y, drawn
    drawn = True
    x = mx
    y = my


def graphics():
    draw_rectangle(0, 0, 400, 400)
    if drawn:
        set_stroke_width(4)
        draw_point(x, y)

x = 0
y = 0
drawn = False

start_graphics(graphics, 2400, mouse_press=clicked)