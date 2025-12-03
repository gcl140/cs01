# File: logo.py
# Author: Gift Christian
# Date: September 15, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Draws a logo of my name using emojis, with my actual name in the middle. Using multiple prints.

from cs1lib import clear, draw_point, draw_line, set_stroke_width, start_graphics

WIN_SIZE = 400
STEP = 20
x, y = 0, 0
has_called = False

def string_art():
    global has_called, x, y

    if has_called == False:
        clear()
    
    set_stroke_width(4)  
    draw_point(x, y)
    px = y
    py = WIN_SIZE - x
    draw_point(px, py)
    set_stroke_width(0)

    draw_line(x, y, px, py)

    if y == WIN_SIZE and x < WIN_SIZE:

        x += STEP

    elif x == WIN_SIZE and y > 0:

        y -= STEP

    elif y == 0 and x > 0:

        x -= STEP

    elif x == 0 and y < WIN_SIZE:

        y += STEP

    has_called = True

start_graphics(string_art, framerate=7.5)
