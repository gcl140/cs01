# File: lab01.py
# Author: Gift Christian
# Date: October 13, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: An updated program that draws the paddles, the ball, for a pong game 
# and allows the user to move them up and down using the keyboard keys z and a for 
# the left paddle, and k and m for the right paddle. The ball moves and bounces off 
# the paddles and the top and bottom of the window. The game resets when the ball goes 
# off the left or right side of the window. The game starts when the spacebar is pressed 
# and quits when the 'q' key is pressed.

# Import the necessary libraries
from cs1lib import clear, cs1_quit, set_fill_color, draw_circle, draw_rectangle, set_font_size, draw_text, start_graphics

# Global constants
WIDTH, HEIGHT = 20, 80                                                      # Width and height of the paddles  
WIN_WIDTH, WIN_HEIGHT = 400, 400                                            # Width and height of the window
OFFSET = 10                                                                 # The amount the paddle moves with each key press
A_KEY, Z_KEY, K_KEY, M_KEY, Q_KEY, SPACE_KEY = 'a', 'z', 'k', 'm', 'q',' '  # Keys to move the paddles and quit and start the game
PADDLE_1_X, PADDLE_2_X = WIN_WIDTH - WIN_WIDTH, WIN_WIDTH - WIDTH           # X positions of the paddles
BALL_RADIUS = 10                                                            # Radius of the ball
BALL_MOVE_X = -5                                                            # X movement of the ball
BALL_MOVE_Y = 5                                                             # Y movement of the ball

# Global variables
paddle_1_y, paddle_2_y = 0, 320                                         # Y positions of the paddles
ball_x, ball_y = WIN_WIDTH/2, WIN_HEIGHT/2                              # Initial X and Y positions of the ball
ball_pos_x, ball_pos_y = 0, 0                                           # X and Y movement of the ball
a_pressed = z_pressed = k_pressed = m_pressed = game_started = False    # Boolean variables to track if specific keys are pressed and if the game has started

# Key press event handler
def pressed(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, game_started, ball_pos_x, ball_pos_y     # Take the global variables into the function for modification
    if key == A_KEY:                                    # If the 'a' key is pressed
        a_pressed = True                                # set a_pressed to True
    elif key == Z_KEY: 
        z_pressed = True
    elif key == K_KEY: 
        k_pressed = True
    elif key == M_KEY: 
        m_pressed = True
    elif key == Q_KEY:                                  # If the 'q' key is pressed
        call_quits()                                    # Call the Quit program function defined below
    elif key == SPACE_KEY and game_started == False:    # If the spacebar is pressed and the game has not started
        ball_pos_x = BALL_MOVE_X                        # Set the ball's X movement to BALL_MOVE_X
        ball_pos_y = BALL_MOVE_Y                        # Set the ball's Y movement to BALL_MOVE_Y
        game_started = True                             # Set game_started to True to start the game

# Key release event handler
def released(key):
    global a_pressed, z_pressed, k_pressed, m_pressed   # Take the global variables into the function for modification
    if key == A_KEY:                                    # If the 'a' key is released
        a_pressed = False                               # set a_pressed to False
    elif key == Z_KEY: 
        z_pressed = False
    elif key == K_KEY: 
        k_pressed = False
    elif key == M_KEY: 
        m_pressed = False

# Function to quit the program
def call_quits():
    cs1_quit()                                          # Call the cs1_quit function, from the cs1lib library to quit the program

# Function to move the paddles based on which keys are pressed
def move_paddles():
    global paddle_1_y, paddle_2_y                        # Take the global variables into the function for modification
    if game_started == False:                            # If the game has not started
        return  None          
    if a_pressed and paddle_1_y > 0:                     # If the 'a' key is pressed and paddle 1 is not at the top
        paddle_1_y -= OFFSET                             # Move paddle 1 up by OFFSET
    if z_pressed and paddle_1_y < WIN_HEIGHT - HEIGHT:   # If the 'z' key is pressed and paddle 1 is not at the bottom
        paddle_1_y += OFFSET                             # Move paddle 1 down by OFFSET
    if k_pressed and paddle_2_y > 0:                     # If the 'k' key is pressed and paddle 2 is not at the top
        paddle_2_y -= OFFSET                             # Move paddle 2 up by OFFSET
    if m_pressed and paddle_2_y < WIN_HEIGHT - HEIGHT:   # If the 'm' key is pressed and paddle 2 is not at the bottom
        paddle_2_y += OFFSET                             # Move paddle 2 down by OFFSET

# Function to check if the ball hits the top or bottom of the window and reverse its Y direction if it does
def hit_bottom_top():
    global ball_pos_y                           # Take the global variable into the function for modification
    if ball_y <= 0 or ball_y >= WIN_HEIGHT:     # If the ball hits the top or bottom of the window
        ball_pos_y = -ball_pos_y                # Reverse the Y direction of the ball


# Function to check if the ball hits the paddles and reverse its X direction if it does
def hit_paddles():
    global ball_pos_x                                                               # Take the global variable into the function for modification
    if paddle_1_y <= ball_y <= paddle_1_y + HEIGHT and ball_x <= WIDTH:                # If the ball hits paddle 1
        ball_pos_x = -ball_pos_x                                                    # Reverse the X direction of the ball    
    if paddle_2_y <= ball_y <= paddle_2_y + HEIGHT and ball_x >= WIN_WIDTH - WIDTH:    # If the ball hits paddle 2
        ball_pos_x = -ball_pos_x                                                    # Reverse the X direction of the ball   

# Main function to update the ball's position
def update_ball():
    global ball_x, ball_y, ball_pos_x, ball_pos_y, game_started     # Take the global variables into the function for modification
    if game_started == False:                                       # If the game has not started
        return  None                                                # Do nothing and return empty
    ball_x += ball_pos_x                                   # Update the ball's X position by its X movement
    ball_y += ball_pos_y                                   # Update the ball's Y position by its Y movement
    hit_bottom_top()                                       # Call the function to check if the ball hits the top or bottom of the window and reverse its Y direction if it does
    off_bounds()                                           # Call the function to check if the ball goes off the left or right side of the window
    hit_paddles()                                          # Call the function to check if the ball hits the paddles and reverse its X direction if it does


# Function to check if the ball goes off the left or right side of the window and reset the game if it does
def off_bounds():
    if ball_x <= 0 or ball_x >= WIN_WIDTH:          # If the ball goes off the left or right side of the window
        clear()                                     # Clear the window
        set_font_size(24)                           # Set the font size to 24
        draw_text("GAME OVER", 140, 200)            # Draw the "GAME OVER" text
        reset_game()                                # Call the reset_game function defined below to reset the game  

# Function to reset the game
def reset_game():
    global ball_x, ball_y, ball_pos_x, ball_pos_y, paddle_1_y, paddle_2_y, game_started  # Take the global variables into the function for modification
    ball_x, ball_y = WIN_WIDTH/2, WIN_HEIGHT/2                   # Reset the ball's position to the center of the window
    paddle_1_y, paddle_2_y = 0, 320                              # Reset the paddles' position to their initial bottom-top positions on the window
    ball_pos_x = ball_pos_y = 0                                  # Reset the ball's movement to 0
    game_started = False                                         # Set game_started to False to stop the game

# Function to draw the ball
def draw_ball():
    draw_circle(ball_x, ball_y, BALL_RADIUS)                     # Draw the ball at its current position with the specified radius

# The main drawing fzunction to draw the paddles and the ball, and update their positions
def pong():
    clear()                                                 # Clear the window
    set_fill_color(0,0, 0)                                  # Set the fill color to black  
    draw_rectangle(PADDLE_1_X, paddle_1_y, WIDTH, HEIGHT)   # Draw paddle 1 at its current position
    draw_rectangle(PADDLE_2_X, paddle_2_y, WIDTH, HEIGHT)   # Draw paddle 2 at its current position
    draw_ball()                                             # CAll the function to draw the ball at its current position
    move_paddles()                                          # Call the function to move the paddles based on which keys are pressed
    update_ball()                                           # Call the function to update the ball's position
    if game_started == False:                                    # If the game has not started
        set_font_size(20)                                   # Set the font size to 20
        draw_text("Press SPACE to start", 110, 150)         # Draw the "Press SPACE to start" text

# Start the graphics window with the pong function as the main drawing function, and set up keyboard event handlers, and window size
start_graphics(pong, key_press=pressed, key_release=released, width=WIN_WIDTH, height=WIN_HEIGHT)
