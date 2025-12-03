# File: lab01.py
# Author: Gift Christian
# Date: October 9, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A program that draws the paddles for a pong game and allows the user to move them up and down using the keyboard keys z and a for the left paddle, and k and m for the right paddle.

from cs1lib import *
from random import randint

WIDTH, HEIGHT = 20, 80
WIN_WIDTH, WIN_HEIGHT = 400, 400
OFFSET = 10
A_KEY, Z_KEY, K_KEY, M_KEY, Q_KEY, SPACE_KEY = 'a', 'z', 'k', 'm', 'q',' '
PADDLE_1_X, PADDLE_2_X = WIN_WIDTH - WIN_WIDTH, WIN_WIDTH - WIDTH    # X positions of the paddles
BALL_RADIUS = 5

BALL_MOVE_X = -5
BALL_MOVE_Y = 5

paddle_1_y, paddle_2_y = 0, 320
ball_x, ball_y = WIN_WIDTH/2, WIN_HEIGHT/2
ball_pos_x, ball_pos_y = 0, 0

a_pressed = z_pressed = k_pressed = m_pressed = game_started = False

def pressed(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, game_started, ball_pos_x, ball_pos_y
    if key == A_KEY: 
        a_pressed = True
    elif key == Z_KEY: 
        z_pressed = True
    elif key == K_KEY: 
        k_pressed = True
    elif key == M_KEY: 
        m_pressed = True
    elif key == Q_KEY:
        call_quits()
    elif key == SPACE_KEY and game_started == False:
        ball_pos_x = randint(-5, 5)
        while ball_pos_x == 0:
            ball_pos_x = randint(-5, 5)
        ball_pos_y = randint(-5, 5)
        while ball_pos_y == 0:
            ball_pos_y = randint(-5, 5)
        game_started = True


def released(key):
    global a_pressed, z_pressed, k_pressed, m_pressed
    if key == A_KEY: 
        a_pressed = False
    elif key == Z_KEY: 
        z_pressed = False
    elif key == K_KEY: 
        k_pressed = False
    elif key == M_KEY: 
        m_pressed = False


def call_quits():
    cs1_quit()


def move_paddles():
    global paddle_1_y, paddle_2_y
    if a_pressed and paddle_1_y > 0: 
        paddle_1_y -= OFFSET
    if z_pressed and paddle_1_y < WIN_HEIGHT - HEIGHT: 
        paddle_1_y += OFFSET
    if k_pressed and paddle_2_y > 0: 
        paddle_2_y -= OFFSET
    if m_pressed and paddle_2_y < WIN_HEIGHT - HEIGHT: 
        paddle_2_y += OFFSET


def hit_bottom_top():
    global ball_pos_y
    if ball_y <= 0 or ball_y >= WIN_HEIGHT:
        ball_pos_y = -ball_pos_y



def off_bounds():
    if ball_x <= 0 or ball_x >= WIN_WIDTH:
        clear()
        set_font_size(24)
        set_fill_color(1,1,1)
        draw_rectangle(0,0,WIN_WIDTH, WIN_HEIGHT)
        draw_text("GAME OVER", 140, 200)        
        reset_game()


def reset_game():
    global ball_x, ball_y, ball_pos_x, ball_pos_y, game_started
    ball_x, ball_y = WIN_WIDTH/2, WIN_HEIGHT/2
    ball_pos_x = ball_pos_y = 0
    game_started = False



def hit_paddles():
    global ball_pos_x
    if paddle_1_y <= ball_y <= paddle_1_y + HEIGHT and ball_x <= 20:
        ball_pos_x = -ball_pos_x
    if paddle_2_y <= ball_y <= paddle_2_y + HEIGHT and ball_x >= WIN_WIDTH - 20:
        ball_pos_x = -ball_pos_x


def update_ball():
    global ball_x, ball_y, ball_pos_x, ball_pos_y, game_started
    if game_started == False:
        return
    ball_x += ball_pos_x
    ball_y += ball_pos_y
    hit_bottom_top()
    off_bounds()
    hit_paddles()


def draw_ball():
    draw_circle(ball_x, ball_y, BALL_RADIUS)


def pong():
    clear()
    set_fill_color(0,0, 0)
    draw_rectangle(PADDLE_1_X, paddle_1_y, WIDTH, HEIGHT)
    draw_rectangle(PADDLE_2_X, paddle_2_y, WIDTH, HEIGHT)
    draw_ball()
    move_paddles()
    update_ball()


start_graphics(pong, key_press=pressed, key_release=released, width=WIN_WIDTH, height=WIN_HEIGHT)
