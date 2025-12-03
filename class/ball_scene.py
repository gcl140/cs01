from random import random, randint
from ball import Ball

class BallScene:
    #Create a new scene of bouncing balls
    def __init__(self, n):
        ball_list = []
        for i in range(n):
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

        self.ball_list = ball_list


    def draw(self):
        for b in range(len(self.ball_list)):
            self.ball_list[b].draw_ball()

    def update(self):
        # i = 0
        # while i < len(self.ball_list):
        #     self.ball_list[i].draw_ball()
        #     i += 1

        # for ball in range(len(self.ball_list)):
        #     self.ball_list[ball].update()

        for ball in self.ball_list:
            if ball.x - ball.r <= 0 or ball.x + ball.r >= 400:
                ball.vx = -(ball.vx)
            if ball.y <= 0 or ball.y >= 400:
                ball.vy = -(ball.vy)
            ball.update()

        # for ball in range(len(self.ball_list)):
        #     if self.ball_list[ball].x <= 0 or self.ball_list[ball].x >= 400:
        #         self.ball_list[ball].vx = -(self.ball_list[ball].vx)
        #     if self.ball_list[ball].y <= 0 or self.ball_list[ball].y >= 400:
        #         self.ball_list[ball].vy = -(self.ball_list[ball].vy)
        #     self.ball_list[ball].update()