# File: lab01.py
# Author: Gift Christian
# Date: October 9, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A program that draws the paddles for a pong game and allows the user to move them up and down using the keyboard keys z and a for the left paddle, and k and m for the right paddle.

# from cs1lib import clear, set_fill_color, draw_rectangle, start_graphics
from cs1lib import *
from random import randint
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

ball_x = WIN_WIDTH/2
ball_y = WIN_HEIGHT/2
go_right = False
go_left = False
go_down = False
go_up = False
random_start = False
start_game = False
called_first = True
start_temp_y = 0
start_temp_x = 0

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
    global key_pressed, paddle_1_y, paddle_2_y, z_pressed, m_pressed, k_pressed, a_pressed, go_left, start_game, ball_x, ball_y, go_right  # Take the global variables into the function for modification
    key_pressed = key                               # Update key_pressed to the key that was pressed on the keyboard    
    if key_pressed == Z_KEY and paddle_1_y < WIN_HEIGHT - HEIGHT:   # If the 'z' key is pressed and the left paddle is not at the bottom edge
        z_pressed = True                            # set z_pressed to True to move the left paddle down
    elif key_pressed == M_KEY and paddle_2_y < WIN_HEIGHT - HEIGHT: # If the 'm' key is pressed and the right paddle is not at the bottom edge
        m_pressed = True                            # set m_pressed to True to move the right paddle down
    elif key_pressed == A_KEY and paddle_1_y > 0:   # If the 'a' key is pressed and the left paddle is not at the top edge
        a_pressed = True                            # set a_pressed to True to move the left paddle up
    elif key_pressed == K_KEY and paddle_2_y > 0:   # If the 'k' key is pressed and the right paddle is not at the top edge
        k_pressed = True                            # set k_pressed to True to move the right paddle up
    elif key_pressed == " ":
        start_game = True

# Function to check which keys are pressed and move the paddles accordingly
def check_pressed():
    global a_pressed, z_pressed, k_pressed, m_pressed, paddle_1_y, paddle_2_y, start_game, go_left, random_start, ball_x, go_right   # Take the global variables into the function for modification
    if a_pressed and paddle_1_y > 0:        # If the 'a' key is pressed and the left paddle is not at the top edge
        paddle_1_y -= OFFSET                # Move the left paddle up by OFFSET
    if z_pressed and paddle_1_y < WIN_HEIGHT - HEIGHT:      # If the 'z' key is pressed and the left paddle is not at the bottom edge
        paddle_1_y += OFFSET                # Move the left paddle down by OFFSET
    if k_pressed and paddle_2_y > 0:        # If the 'k' key is pressed and the right paddle is not at the top edge
        paddle_2_y -= OFFSET                # Move the right paddle up by OFFSET
    if m_pressed and paddle_2_y < WIN_HEIGHT - HEIGHT:      # If the 'm' key is pressed and the right paddle is not at the bottom edge
        paddle_2_y += OFFSET                # Move the right paddle down by OFFSET
    if start_game:
        random_start = True
        print(ball_x, ball_y)
    

def update_ball_position():
    global ball_x, ball_y, go_right, go_left, called_first, start_temp_y,start_temp_x, random_start

    if random_start:
        if called_first:
            start_temp_y = randint(0, 8)
            start_temp_x = randint(0, 8)
            called_first = False
        ball_y += start_temp_y
        ball_x += start_temp_x

    if go_right and ball_x < 390:
        ball_x += 5
        ball_y += 0
    if go_left and ball_x > 0 and ball_y >= 0:       
        ball_x -= 5

    if go_down and ball_y < 400:
        ball_x += 0
        ball_y += 5

    if go_up and ball_y > 0:
        ball_x += 0
        ball_y -= 5

def collide_paddle():
    global paddle_1_y, ball_y, ball_x, go_right, go_left, go_up, go_down, start_game, random_start, start_temp_y, start_temp_x
    if ball_x != 200:
        start_game = False
    if ball_x >= 400:
        random_start = False
        go_right = False
    if ball_x <= 0:
        random_start = False
        go_left = False
    if ball_y <= 0:
        random_start = False
        go_up = False
    if ball_y >= 400:
        random_start = False
        go_down = False


    if paddle_1_y <= ball_y and paddle_1_y + 100 >= ball_y and ball_x <= 10: 
        random_start = False
        start_temp_x = -1 * start_temp_x
        random_start = True

    if paddle_2_y <= ball_y and paddle_2_y + 100 >= ball_y and ball_x >= 390: 
        random_start = False
        start_temp_x = -1 * start_temp_x
        random_start = True

    if ball_y >= 400:
        random_start = False
        start_temp_y = -1 * start_temp_y
        # start_temp_x = -1 * start_temp_x
        random_start = True

    if ball_y <= 0: 
        random_start = False
        start_temp_y = -1 * start_temp_y
        random_start = True

    # if ball_x <= 0:
    #     clear()
    #     draw_text("Game overrr", 190, 200)
    # if ball_x >= 400:
    #     clear()
    #     draw_text("Game over", 190, 200)

def draw_ball():
    global ball_y, ball_x
    draw_circle(ball_x, ball_y, 5)

# Main drawing function
def pong():
    global paddle_1_y, paddle_2_y                           # Take the global variables into the function for modification
    clear()                                                 # Clear the canvas
    set_fill_color(0, 0, 0)                                 # Set fill color to black
    draw_rectangle(PADDLE_1_X, paddle_1_y, WIDTH, HEIGHT)   # Draw the left paddle
    draw_rectangle(PADDLE_2_X, paddle_2_y, WIDTH, HEIGHT)   # Draw the right paddle
    check_pressed()                                         # Check which keys are pressed and move the paddles accordingly
    draw_ball()
    update_ball_position()
    collide_paddle()
    print(ball_x, ball_y)

# Start the graphics window with the pong function as the main drawing function, and set up keyboard event handlers, and window size
start_graphics(pong, key_press=pressed, key_release=released, width=WIN_WIDTH, height=WIN_HEIGHT)