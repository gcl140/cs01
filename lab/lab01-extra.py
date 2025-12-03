# File: lab01.py
# Author: Gift Christian
# Date: October 13, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: An updated program that draws the paddles, the ball, for a pong game 
# and allows the user to move them up and down using the keyboard keys z and a for 
# the left paddle, and k and m for the right paddle. The ball moves and bounces off 
# the paddles and the top and bottom of the window. The game resets when the ball goes 
# off the left or right side of the window. The game starts when the spacebar is pressed 
# and quits when the 'q' key is pressed. It is enhanced with random colors for the paddles
# and the ball, random initial direction for the ball, and random movement for the ball
# when it hits the paddles.

# Import the necessary libraries
# from cs1lib import clear, cs1_quit, set_fill_color, draw_circle, draw_rectangle, set_font_size, draw_text, start_graphics
from cs1lib import *                                 # Import all functions from the cs1lib library#
from random import randint                           # Import the randint function from the random library for generating random integers

# Global constants
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 80                                        # Width and height of the paddles  
WIN_WIDTH, WIN_HEIGHT = 400, 400                                            # Width and height of the window
OFFSET = 10                                                                 # The amount the paddle moves with each key press
A_KEY, Z_KEY, K_KEY, M_KEY, Q_KEY, SPACE_KEY = 'a', 'z', 'k', 'm', 'q',' '  # Keys to move the paddles and quit and start the game
PADDLE_1_X, PADDLE_2_X = WIN_WIDTH - WIN_WIDTH, WIN_WIDTH - PADDLE_WIDTH    # X positions of the paddles
BALL_RADIUS = 5                                                             # Radius of the ball
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
        ball_pos_x = randint(-5, 5)                     # Set the ball's X movement to a random integer between -5 and 5
        while ball_pos_x == 0 or ball_pos_x == 1 or ball_pos_x == 2:    # Ensure the ball's X movement is not 0, 1, or 2 using a while loop (avoids straight vertical movement)
            ball_pos_x = randint(-5, 5)                                 # Keep generating a new random integer until it is not 0, 1, or 2
        ball_pos_y = randint(-5, 5)                    # Set the ball's Y movement to a random integer between -5 and 5
        while ball_pos_y == 0 or ball_pos_y == 1 or ball_pos_y == 2:    # Ensure the ball's Y movement is not 0, 1, or 2 using a while loop (avoids straight horizontal movement)
            ball_pos_y = randint(-5, 5)                                 # Keep generating a new random integer until it is not 0, 1, or 2
        game_started = True                            # Set game_started to True to start the game

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
        return  None                                     # Do nothing and return empty
    if a_pressed and paddle_1_y > 0:                     # If the 'a' key is pressed and paddle 1 is not at the top
        paddle_1_y -= OFFSET                             # Move paddle 1 up by OFFSET
    if z_pressed and paddle_1_y < WIN_HEIGHT - PADDLE_HEIGHT:   # If the 'z' key is pressed and paddle 1 is not at the bottom
        paddle_1_y += OFFSET                             # Move paddle 1 down by OFFSET
    if k_pressed and paddle_2_y > 0:                     # If the 'k' key is pressed and paddle 2 is not at the top
        paddle_2_y -= OFFSET                             # Move paddle 2 up by OFFSET
    if m_pressed and paddle_2_y < WIN_HEIGHT - PADDLE_HEIGHT:   # If the 'm' key is pressed and paddle 2 is not at the bottom
        paddle_2_y += OFFSET                             # Move paddle 2 down by OFFSET

# Function to check if the ball hits the top or bottom of the window and reverse its Y direction if it does
def hit_bottom_top():
    global ball_pos_y                           # Take the global variable into the function for modification
    if ball_y <= 0 or ball_y >= WIN_HEIGHT:     # If the ball hits the top or bottom of the window
        ball_pos_y = -ball_pos_y                # Reverse the Y direction of the ball


# Function to check if the ball hits the paddles and reverse its X direction if it does
def hit_paddles():
    global ball_pos_x, ball_pos_y                                                                    # Take the global variable into the function for modification
    if paddle_1_y <= ball_y <= paddle_1_y + PADDLE_HEIGHT and ball_x <= PADDLE_WIDTH:                # If the ball hits paddle 1
        ball_pos_x = -ball_pos_x + randint(-5, 5)                                                    # Reverse the X direction of the ball and add some random horizontal movement    
        ball_pos_y += randint(-2, 2)                                                                 # Add some random vertical movement
    if paddle_2_y <= ball_y <= paddle_2_y + PADDLE_HEIGHT and ball_x >= WIN_WIDTH - PADDLE_WIDTH:    # If the ball hits paddle 2
        ball_pos_x = -ball_pos_x + randint(-5, 5)                                                    # Reverse the X direction of the ball and add some random horizontal movement
        ball_pos_y += randint(-2, 2)                                                                 # Add some random vertical movement


# Main function to update the ball's position
def update_ball():
    global ball_x, ball_y, ball_pos_x, ball_pos_y, game_started     # Take the global variables into the function for modification
    if game_started == False:                                       # If the game has not started
        return  None                                                # Do nothing and return empty
    ball_x += ball_pos_x                                   # Update the ball's x position based on its movement
    ball_y += ball_pos_y                                   # Update the ball's y position based on its movement
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
    ball_x, ball_y = WIN_WIDTH/2, WIN_HEIGHT/2                                           # Reset the ball's position to the center of the window
    paddle_1_y, paddle_2_y = WIN_HEIGHT - WIN_HEIGHT, WIN_HEIGHT - PADDLE_HEIGHT         # Reset the paddles' position to their initial bottom-top positions on the window
    ball_pos_x = ball_pos_y = 0                                                          # Reset the ball's movement to 0
    game_started = False                                                                 # Set game_started to False to stop the game

# Function to draw the ball
def draw_ball():
    img = load_image("ball.png")                            # Load the ball image from the file "ball.png"
    draw_image(img, ball_x, ball_y)                         # Draw the ball image at the ball's current position

# The main drawing function to draw the paddles and the ball, and update their positions
def pong():
    clear()                                                                     # Clear the window
    set_fill_color(randint(0, 10)/10, randint(0, 10)/10, randint(0, 10)/10)     # Set the fill color to random colors
    draw_rectangle(PADDLE_1_X, paddle_1_y, PADDLE_WIDTH, PADDLE_HEIGHT)         # Draw paddle 1 at its current position
    draw_rectangle(PADDLE_2_X, paddle_2_y, PADDLE_WIDTH, PADDLE_HEIGHT)         # Draw paddle 2 at its current position
    draw_ball()                                             # CAll the function to draw the ball at its current position
    move_paddles()                                          # Call the function to move the paddles based on which keys are pressed
    update_ball()                                           # Call the function to update the ball's position
    if not game_started:                                    # If the game has not started
        set_font_size(20)                                   # Set the font size to 20
        set_stroke_color(randint(0, 10)/10, randint(0, 10)/10, randint(0, 10)/10) # Set the stroke color to random colors
        set_font_bold()                                     # Set the font to bold
        draw_text("PRESS SPACE TO START", 80, 150)          # Draw the "Press SPACE to start" text


# Start the graphics window with the pong function as the main drawing function, and set up keyboard event handlers, and window size
start_graphics(pong, key_press=pressed, key_release=released, width=WIN_WIDTH, height=WIN_HEIGHT)
