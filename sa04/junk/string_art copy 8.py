from cs1lib import *

#(x, y). This point (x, y) is always paired with the point (y, WIN_SIZE - x)
WIN_SIZE = 400
step = 20
x, y1, x2 = 0, 0, 0
y, y2, x3 = WIN_SIZE, WIN_SIZE, WIN_SIZE
has_called = False

def draw_points():
    global has_called, x, y, y1, x2, y2, x3

    if x < WIN_SIZE and y > 0:
        y -= step
        x += step
        # draw_line(0, y, x, 0)
        draw_point(0, y)

    if y1 < WIN_SIZE:
        y1 += step
        # draw_line(WIN_SIZE, y1, y1, 0)
        draw_point(y1, 0)
    
    if x2 < WIN_SIZE and y2 > 0:
        x2 += step
        y2 -= step
        # draw_line(WIN_SIZE, x2, y2,WIN_SIZE)
        draw_point(WIN_SIZE, x2)
        # draw_point(400, 380)

    if x3 > 0:
        x3 -= step
        # draw_line(x3, WIN_SIZE, 0, x3)
        draw_point(x3, WIN_SIZE)
        # call = True
        # if call:
        #     set_stroke_color(0, 0, 1)
        #     set_stroke_width(3)
        #     draw_point(x2, WIN_SIZE)
        #     call = True

def draw_lines():
    global has_called, x, y, y1, x2, y2, x3

    if x < WIN_SIZE and y > 0:
        y -= step
        x += step
        draw_line(0, y, x, 0)
        # draw_point(0, y)

    if y1 < WIN_SIZE:
        y1 += step
        draw_line(WIN_SIZE, y1, y1, 0)
        # draw_point(y1, 0)
    
    if x2 < WIN_SIZE and y2 > 0:
        x2 += step
        y2 -= step
        draw_line(WIN_SIZE, x2, y2,WIN_SIZE)

    if x3 > 0:
        x3 -= step
        draw_line(x3, WIN_SIZE, 0, x3)



def string_art():
    global has_called, x, y, y1, x2, y2, x3

    if has_called != True:
        clear()
        set_stroke_width(5)

        if x < WIN_SIZE and y > 0:
            y -= step
            x += step
            # draw_line(0, y, x, 0)
            draw_point(0, y)

        if y1 < WIN_SIZE:
            y1 += step
            # draw_line(WIN_SIZE, y1, y1, 0)
            draw_point(y1, 0)
        
        if x2 < WIN_SIZE and y2 > 0:
            x2 += step
            y2 -= step
            # draw_line(WIN_SIZE, x2, y2,WIN_SIZE)
            draw_point(WIN_SIZE, x2)
            # draw_point(400, 380)

        if x3 > 0:
            x3 -= step
            # draw_line(x3, WIN_SIZE, 0, x3)
            draw_point(x3, WIN_SIZE)
            # call = True
            # if call:
            #     set_stroke_color(0, 0, 1)
            #     set_stroke_width(3)
            #     draw_point(x2, WIN_SIZE)
            #     call = True


    has_called = True

start_graphics(string_art)