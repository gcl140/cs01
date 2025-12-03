# File: string_art.py
# Author: Gift Christian
# Date: October 2, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Draws a string art using functions from cs1lib with lines and 
# points to represent the string and thumbstack of an actual string art, respectively.

#importing necessary functions from cs1lib
from cs1lib import clear, draw_point, draw_line, set_stroke_width, start_graphics

# Defining constants and initializing variables
                    
WIN_SIZE = 400      #Constant for the window size, by default it is 400x400

STEP = 20           #Constant for the step size, which determines the distance between points and lines
x = 0               #Starting x coordinates for the first line and point
y = 0               #Starting y coordinates for the first line and point
has_called = False  #Boolean variable to check if the function has been called before

# Defining the main function to draw the string art
def string_art():
    global has_called, x, y     # Accessing global variables since we will be modifying them

    if has_called == False:     # If the function is called for the first time, do the following: clear the window
        clear()
    
    set_stroke_width(4)         # Setting the stroke width for the points initially to 4
    draw_point(x, y)            # Drawing the starting point for the thumbstack at (x, y)
    px = y                      # Determining the ending x coordinate for the thumbstack and assigning it to px
    py = WIN_SIZE - x           # Determining the ending y coordinate for the thumbstack and assigning it to py
    draw_point(px, py)          # Drawing the ending point for the thumbstack at (px, py)
    set_stroke_width(0)         # Setting the stroke width for the lines to 0 for points only

    draw_line(x, y, px, py)     # Drawing the line to represent the thumbstack now from (x, y) to (px, py)

    if y == WIN_SIZE and x < WIN_SIZE:  # If the y coordinate is at the bottom and x is not at the right edge, increment x until it reaches the right edge

        x += STEP                       # Incrementing x by the step size

    elif x == WIN_SIZE and y > 0:       # If the x coordinate is at the right edge and y is not at the top edge, decrement y until it reach the top edge

        y -= STEP                       # Decrementing y by the step size

    elif y == 0 and x > 0:              # If the y coordinate is at the top edge and x is not at the left edge, decremet x until it reaches the left edge

        x -= STEP                       # Decrementing x by the step size

    elif x == 0 and y < WIN_SIZE:       # If the x coordinate is at the left edge and y is not at the bottom edge, increment y until it reaches the bottom edge

        y += STEP                       # Incrementing y by the step size

    has_called = True                   # Setting has_called to True after the first time it's called so that the window is not cleared on subsequent calls

start_graphics(string_art, framerate=7.5)   # Starting the graphics with the string_art function and setting the framerate to 7.5 frames per second so the drawing is visible
