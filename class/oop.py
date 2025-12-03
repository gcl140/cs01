from cs1lib import *
from ball import Ball
from ball_scene import BallScene
from random import randint, random


def draw():
    clear()

    bs.draw()
    bs.update()


bs = BallScene(1000)
start_graphics(draw, width=400, height=400)
# print(b.x, b.y, b.r)