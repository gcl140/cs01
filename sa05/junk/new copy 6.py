from cs1lib import *
from random import randint

nx, ny, px, py, program_counter = 0, 0, 0, 0, 0
lefted, move, has_pressed  = False, False, False
key_pressed = None
WIN_SIZE = 800
text = "Use r/R for Red"

def left(x, y):
    global nx, ny, lefted, has_pressed
    has_pressed = False
    nx = x
    ny = y

def moved(x, y):
    global ox, oy, move, curr_x, curr_y, has_pressed
    if not has_pressed:
        curr_x = x
        curr_y = y
    move = True
    ox = x
    oy = y

def pressedii(x, y):
    global px, py, has_pressed
    has_pressed = True
    px = x
    py = y

def press_button(key):
    global key_pressed
    key_pressed = key

def say_my_text():
    set_font("Courier")             # set font type to Courier
    set_font_size(15)               # set font size to 15
    set_stroke_color(1, 1, 1)       # white color for the text
    set_font_bold()                 # bolden the font
    draw_text(text, 30, WIN_SIZE - 30)   # Draw the text at the bottom left of the window 30 points up and 30 points right

def choose_stroke_color():
    if key_pressed == "b" or key_pressed == "B":
        set_stroke_color(0, 0, 1)
    elif key_pressed == "g" or key_pressed == "G":
        set_stroke_color(0, 1, 0)
    elif key_pressed == "r" or key_pressed == "R":
        set_stroke_color(1, 0, 0)
    elif key_pressed == "w" or key_pressed == "W":
        set_stroke_color(1, 1, 1)
    else:
        set_stroke_color(randint(0,10)/10, randint(0,10)/10, randint(0,10)/10)


def art():
    global program_counter, has_pressed, move, curr_y, curr_x, key_pressed
    if program_counter == 0:
        clear()
        set_fill_color(0, 0, 0)
        draw_rectangle(0, 0, WIN_SIZE, WIN_SIZE)

    set_stroke_width(3)
    # set_stroke_color(1, 1, 1)

    choose_stroke_color()

    if has_pressed:
        if move:
            draw_point(ox, oy)
            draw_line(ox, oy, curr_x, curr_y)
            curr_x = ox
            curr_y = oy
    set_stroke_width(0)

    say_my_text()
    program_counter += 1

start_graphics(art, 
                mouse_release=left,
                mouse_move=moved, 
                mouse_press=pressedii,
                key_press=press_button,
                width=WIN_SIZE,
                height=WIN_SIZE,
                )