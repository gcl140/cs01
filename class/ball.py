from cs1lib import set_fill_color, draw_circle
from random import randint

class Ball:
    def __init__(self, x, y, ra, vx, vy, r, g, bl):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ra = ra
        self.r = r
        self.g = g
        self.bl = bl

    
    def update(self):
        self.x += self.vx
        self.y += self.vy

    def sum(self):
        self.x + self.y

    def draw_ball(self):
        # set_fill_color(randint(0, 10)/10, randint(0, 10)/10, randint(0, 10)/10)
        set_fill_color(self.r, self.g, self.bl)
        draw_circle(self.x, self.y, self.ra)

    def __str__(self):
        return f"Ball at ({self.x}, {self.y}, {self.r})"
    