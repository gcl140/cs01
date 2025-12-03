# File: chalkboard.py
# Author: Gift Christian
# Date: October 4, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A program that draws a canvas for drawing on using the mouse when pressed, and allows choosing
#               different colors using keyboard keys. 

# Importing libraries I will need
# from the cs1lib library, import only functions i would need.
from cs1lib import set_font, set_font_size, set_stroke_color, set_font_bold, draw_text, clear, set_fill_color, draw_rectangle, draw_point, draw_line, set_stroke_width, start_graphics  

# from the random library, import only the randint function that generates random integers
from random import randint  

# Global constants
WIN_SIZE = 800

# Global variables
nx, ny, px, py, program_counter = 0, 0, 0, 0, 0     #Initialize variables to 0
move, has_pressed  = False, False    #Initialize boolean variables to False
key_pressed = None                                  #Initialize key_pressed to None, meaning no key has been pressed yet

#Text to display instructions to the user
text = "c/C-Clear, r/R-Red, w/W-White, g/G-Green, b/B-Blue, y/Y-Yellow, any other-random" 

# Mouse event handlers
# When the left mouse button is released
def left(x, y):
    global nx, ny, has_pressed  #Take these global variables into the function for modification
    has_pressed = False         #Set has_pressed to False when the left mouse button is released
    nx = x                      #Update the global nx variable to the current x position of the mouse
    ny = y                      #Update the global ny variable to the current y position of the mouse

# When the mouse is moved around in the window
def moved(x, y):
    global mx, my, move, curr_x, curr_y, has_pressed    #Take these global variables into the function for modification
    if not has_pressed:                                 #If the mouse button is not pressed
        curr_x = x                                      #Assign curr_x to the current x position (last known x position) of the mouse
        curr_y = y                                      #Assign curr_y to the current y position (last known y position) of the mouse
    move = True                                         #Set move to True when the mouse is moved
    mx = x                                              #Update the global mx variable to the current x position of the mouse
    my = y                                              #Update the global my variable to the current y position of the mouse

# When the left mouse button is pressed down
def has_pressed_func(x, y):
    global px, py, has_pressed              #Take these global variables into the function for modification
    has_pressed = True                      #Set has_pressed to True when the left mouse button is pressed
    px = x                                  #Update the global px variable to the current x position of the mouse
    py = y                                  #Update the global py variable to the current y position of the mouse

# When a key is pressed on the keyboard
def press_button(key):              
    global key_pressed              #Take the global variable key_pressed into the function for modification
    key_pressed = key               #Update key_pressed to the key that was pressed on the keyboard

# Function to display instructional text on the canvas
def say_my_text():
    set_font("Courier")             # set font type to Courier
    set_font_size(15)               # set font size to 15
    set_stroke_color(1, 1, 1)       # white color for the text
    draw_text(text, 30, WIN_SIZE - 30)   # Draw the text at the bottom left of the window 30 points up and 30 points right

# Function to choose the stroke color based on the key pressed by the user on the keyboard
def choose_stroke_color():
    global key_pressed            #Take the global variable key_pressed into the function for modification
    # Check for specific color keys first
    if key_pressed == "b" or key_pressed == "B":
        set_stroke_color(0, 0, 1)  # Blue if B or b is pressed
    elif key_pressed == "g" or key_pressed == "G":
        set_stroke_color(0, 1, 0)  # Green if G or g is pressed 
    elif key_pressed == "r" or key_pressed == "R":
        set_stroke_color(1, 0, 0)  # Red if R or r is pressed
    elif key_pressed == "y" or key_pressed == "Y":
        set_stroke_color(1, 1, 0)  # Yellow if Y or y is pressed
    elif key_pressed == "w" or key_pressed == "W":
        set_stroke_color(1, 1, 1)  # White if W or w is pressed
    elif key_pressed == "c" or key_pressed == "C":   # Clear the canvas if C or c is pressed
        clear()                                      # Clear the canvas
        set_fill_color(0, 0, 0)                      # Set fill color to black
        draw_rectangle(0, 0, WIN_SIZE, WIN_SIZE)     # Then draw a black rectangle covering the entire window
        key_pressed = "w"                            # Reset key_pressed to w after clearing the canvas so that the default color is set back to white

    else:
        if key_pressed:                                                            # If any other key is pressed that is not specifically handled above
            set_stroke_color(randint(0,10)/10, randint(0,10)/10, randint(0,10)/10) # Use randint to Produce a very random color
        else:                                                                      # If no key has been pressed yet
            set_stroke_color(1, 1, 1)                                              # Default to White

# The main drawing function that gets called repeatedly to update the canvas
def art():
    global program_counter, has_pressed, move, curr_y, curr_x, key_pressed  #Take these global variables into the function for modification
    if program_counter == 0:                                                #If this is the first time the function is called
        clear()                                                             #Clear the canvas
        set_fill_color(0, 0, 0)                                             # Set fill color to black
        draw_rectangle(0, 0, WIN_SIZE, WIN_SIZE)                            # Then draw a black rectangle covering the entire window

    choose_stroke_color()                                                   # Call the function to choose the stroke color based on key pressed

    set_stroke_width(3)                                                     # Initially Set stroke width to 3 for the coming drawing
    if has_pressed:                                                         # If the mouse button is currently pressed
        if move:                                                            # And if the mouse has moved
            draw_point(mx, my)                                              # Draw a point at the current mouse position
            draw_line(mx, my, curr_x, curr_y)                               # Draw a line from the last known position to the current position
            curr_x = mx                                                     # Update curr_x to the current x position of the mouse by assigning mx to curr_x
            curr_y = my                                                     # Update curr_y to the current y position of the mouse by assigning my to curr_y
    set_stroke_width(0)                                                     # Reset stroke width to 0 at the end of the drawing

    say_my_text()                                                           # Call the function to display instructional text on the canvas
    program_counter += 1                                                    # Increment the program counter by 1


# Start the graphics window with the art function as the main drawing function, and set up mouse and keyboard event handlers, and window size
start_graphics(art,         
                mouse_release=left,            # Function left called when the left mouse button is released
                mouse_move=moved,              # Function moved called when the mouse is moved
                mouse_press=has_pressed_func,  # Function has_pressed_func called when the left mouse button is pressed
                key_press=press_button,        # Function press_button called when a key is pressed
                width=WIN_SIZE,                # Set the window width to WIN_SIZE
                height=WIN_SIZE,               # Set the window height to WIN_SIZE
                )