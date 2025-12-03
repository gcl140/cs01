from cs1lib import *
from ball import Ball
from random import randint, random


def draw():
    clear()
    i = 0
    while i < len(ball_list):
        ball_list[i].draw_ball()
        i += 1

    for ball in range(len(ball_list)):
        ball_list[ball].update()

    # b.draw_ball()
    # b.update()


ball_list = []
for i in range(10):
    x = randint(0, 400)
    y = randint(0, 400)
    ra = randint(10, 30)
    vx = randint(-3, 3)
    vy = randint(-3, 3)
    r = random()
    g = random()
    bl = random()
    b = Ball(x, y, ra, vx, vy, r, g, bl)
    ball_list.append(b)


start_graphics(draw, width=400, height=400)
print(b.x, b.y, b.r)