from cs1lib import *

start_x = 0
start_y = 0
end_x = 0
end_y = 0
has_started_drawing = False

def draw_lines():
        step = 20
        x1 = start_x #0
        y1 = start_y + 400 #400
        y2 = end_y   #0
        x2 = end_x   #0

        while y1 >= 0 and x2 <= 400:
            draw_line(x1, y1, x2, y2)
            y1 -= step
            x2 += step

        x1 = start_x #0
        y1 = start_y #400
        x2 = end_x + 400 #0
        y2 = end_y   #0
 
        while x1 <= 400 and y2 <= 400:
            draw_line(x1, y1, x2, y2)
            x1 += step
            y2 += step

        x1 = start_x + 400 #0
        y1 = start_y #400
        x2 = end_x + 400 #0
        y2 = end_y + 400 #0

        while x2 >= 0 and y1 <= 400:
            draw_line(x1, y1, x2, y2)
            y1 += step
            x2 -= step

        x1 = start_x + 400 #0
        y1 = start_y + 400 #400
        x2 = end_x #0
        y2 = end_y + 400 #0

        while x1 >= 0 and y2 >= 0:
            draw_line(x1, y1, x2, y2)
            x1 -= step
            y2 -= step

def draw_points():
        step = 20
        x1 = start_x #0
        y1 = start_y + 400 #400
        y2 = end_y   #0
        x2 = end_x   #0


        while y1 >= 0:
            # set_stroke_width(5)
            # set_stroke_color(0, 0, 1)
            draw_point(x1, y1)
            y1 -= step

        x1 = start_x #0
        y1 = start_y + 400 #400
        y2 = end_y   #0
        x2 = end_x   #0


        while y1 >= 0:
            # set_stroke_width(5)
            # set_stroke_color(0, 0, 1)
            draw_point(x1, y1)
            y1 -= step
     
def draw_art():
    clear()
    has_started_drawing = True
    if has_started_drawing:
        global start_x
        global start_y
        global end_x
        global end_y

        # step = 20
        draw_lines()

        draw_points()


start_graphics(draw_art)

