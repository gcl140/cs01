# File: lab01.py
# Author: Gift Christian
# Date: October 9, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A program that draws the paddles for a pong game and allows the user to move them up and down using the keyboard keys z and a for the left paddle, and k and m for the right paddle.

from cs1lib import clear, set_fill_color, draw_rectangle, start_graphics

# Global constants
OFFSET = 10                                                 # The amount the paddle moves with each key press
A_KEY, Z_KEY, K_KEY, M_KEY = 'a', 'z', 'k', 'm'             # Keys to move the paddles
WIDTH, HEIGHT = 10, 100                                     # Width and height of the paddles
WIN_WIDTH, WIN_HEIGHT = 400, 400                            # Width and height of the window
PADDLE_1_X, PADDLE_2_X = WIN_WIDTH - WIN_WIDTH, WIN_WIDTH - WIDTH    # X positions of the paddles

# Global variables
paddle_1_y = 0          # Y position of the left paddle
paddle_2_y = 300        # Y position of the right paddle
key_pressed = False     # Variable to store the currently pressed key
z_pressed, m_pressed, k_pressed, a_pressed  = False, False, False, False    # Boolean variables to track if specific keys are pressed


# Key release event handler
def released(key):
    global key_pressed, paddle_1_y, paddle_2_y, z_pressed, m_pressed, k_pressed, a_pressed  # Take the global variables into the function for modification
    if key == A_KEY:            # If the 'a' key is released
        a_pressed = False       # Set a_pressed to False
    elif key == K_KEY:
        k_pressed = False
    elif key == M_KEY:
        m_pressed = False
    elif key == Z_KEY:
        z_pressed = False

# Key press event handler
def pressed(key):
    global key_pressed, paddle_1_y, paddle_2_y, z_pressed, m_pressed, k_pressed, a_pressed  # Take the global variables into the function for modification
    key_pressed = key                               # Update key_pressed to the key that was pressed on the keyboard    
    if key_pressed == Z_KEY and paddle_1_y < WIN_HEIGHT - HEIGHT:   # If the 'z' key is pressed and the left paddle is not at the bottom edge
        z_pressed = True                            # set z_pressed to True to move the left paddle down
    elif key_pressed == M_KEY and paddle_2_y < WIN_HEIGHT - HEIGHT: # If the 'm' key is pressed and the right paddle is not at the bottom edge
        m_pressed = True                            # set m_pressed to True to move the right paddle down
    elif key_pressed == A_KEY and paddle_1_y > 0:   # If the 'a' key is pressed and the left paddle is not at the top edge
        a_pressed = True                            # set a_pressed to True to move the left paddle up
    elif key_pressed == K_KEY and paddle_2_y > 0:   # If the 'k' key is pressed and the right paddle is not at the top edge
        k_pressed = True                            # set k_pressed to True to move the right paddle up

# Function to check which keys are pressed and move the paddles accordingly
def check_pressed():
    global a_pressed, z_pressed, k_pressed, m_pressed, paddle_1_y, paddle_2_y   # Take the global variables into the function for modification
    if a_pressed and paddle_1_y > 0:        # If the 'a' key is pressed and the left paddle is not at the top edge
        paddle_1_y -= OFFSET                # Move the left paddle up by OFFSET
    if z_pressed and paddle_1_y < WIN_HEIGHT - HEIGHT:      # If the 'z' key is pressed and the left paddle is not at the bottom edge
        paddle_1_y += OFFSET                # Move the left paddle down by OFFSET
    if k_pressed and paddle_2_y > 0:        # If the 'k' key is pressed and the right paddle is not at the top edge
        paddle_2_y -= OFFSET                # Move the right paddle up by OFFSET
    if m_pressed and paddle_2_y < WIN_HEIGHT - HEIGHT:      # If the 'm' key is pressed and the right paddle is not at the bottom edge
        paddle_2_y += OFFSET                # Move the right paddle down by OFFSET


# Main drawing function
def pong():
    global paddle_1_y, paddle_2_y                           # Take the global variables into the function for modification
    clear()                                                 # Clear the canvas
    set_fill_color(0, 0, 0)                                 # Set fill color to black
    draw_rectangle(PADDLE_1_X, paddle_1_y, WIDTH, HEIGHT)   # Draw the left paddle
    draw_rectangle(PADDLE_2_X, paddle_2_y, WIDTH, HEIGHT)   # Draw the right paddle
    check_pressed()                                         # Check which keys are pressed and move the paddles accordingly

# Start the graphics window with the pong function as the main drawing function, and set up keyboard event handlers, and window size
start_graphics(pong, key_press=pressed, key_release=released, width=WIN_WIDTH, height=WIN_HEIGHT)