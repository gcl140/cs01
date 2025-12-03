# File: drawing.py
# Author: Gift Christian
# Date: September 22, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Draws a cover image of my favorite book using cs1lib. The program
#              structures the drawing into functions for each body part, and so it is
#               modular, easy to read, and scalable.

# Import cs1lib functions that I need
from sa01.cs1lib import set_stroke_color, set_fill_color, draw_circle, clear, draw_line, draw_rectangle, start_graphics, set_font, set_font_size, set_font_bold, draw_text

# Constants
x = 200                 # center x
y = x/2                 # center y
r = 50                  # radius
l = 2 * r               # length of body 
name = "Gift Christian" # my name to be displayed on and in the window


# Helper functions
# Color setter functions
def set_green():
    set_fill_color(0, 1, 0)   # green

def set_white():
    set_fill_color(1, 1, 1)   # white

def set_black():
    set_fill_color(0, 0, 0)   # black


# Make background black
def make_background_black():
    clear()                        # clear the window
    set_black()                    # black
    draw_rectangle(0, 0, 400, 400) # draw black rectangle to fill window, SHAPE 1


def draw_antennas():
    set_stroke_color(1, 1, 1)           # white
    draw_line(x, y, x + 50, y - 100)    # right antenna, LINE 1
    draw_line(x, y, x - 50, y - 100)    # left antenna, LINE 2


def draw_head():
    set_green()                            # green
    draw_circle(x, y, r)                   # head position and size, SHAPE 2


def draw_eyes():
    set_white()                           # white
    draw_circle(x - 20, y - 20, r/5)      # left eye, SHAPE 3
    draw_circle(x + 20, y - 20, r/5)      # right eye, SHAPE 4


def draw_legs():
    set_green()                                            # green
    set_stroke_color(0, 0, 0)                              # black stroke
    draw_rectangle(x - l/2 + l/10, y + 100, l/10, 0.7 * l) # left leg, SHAPE 5
    draw_rectangle(x + l/2 - l/5, y + 100, l/10, 0.7 * l)  # right leg, SHAPE 6


def draw_body():
    set_stroke_color(1, 1, 1)             # white stroke
    set_green()                           # green fill
    draw_rectangle(x - l/2, y + 10, l, l) # body position and size, SHAPE 7


def draw_arms():
    set_stroke_color(0, 0, 0)                         # black stroke
    draw_rectangle(x - l/2 - 15, y, l * 0.1, 0.7 * l) # left arm, SHAPE 8
    draw_rectangle(x + l/2 + 5, y, l * 0.1, 0.7 * l)  # right arm, SHAPE 9


def say_my_name():
    set_font("Courier")             # set font type to Courier
    set_font_size(15)               # set font size to 15
    set_stroke_color(1, 1, 1)       # white color for the text
    set_font_bold()                 # bolden the font
    draw_text(name, 30, 400 - 30)   # Draw the text at the bottom left of the window 30 points up and 30 points right


# Main drawing function
def draw_the_android():

    #Function calls to draw the android
    make_background_black()

    #draw antennas first so they are behind the head
    draw_antennas() 

    #draw head next so it is in front of the antennas
    draw_head()
    
    # draw eyes after head so they are on top of the head
    draw_eyes() 
    
    # draw legs before body so they are behind the body
    draw_legs() 

    # draw body after legs so it is on top of the legs
    draw_body()

    # to draw arms 
    draw_arms() 

    # to write my name on the bottom left corner of the window
    say_my_name()


#prepare the window title with my name
title = name + "'s Android"


# Start the graphics, title the window "Android"... voula!
start_graphics(draw_the_android, title=title)
