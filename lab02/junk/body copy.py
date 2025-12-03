from cs1lib import *
from math import sqrt
class Body:
    def __init__(self, m, x, y, v_x, v_y, rot, rr, gg, bb):
        self.mass = m
        self.x = x
        self.y = y
        self.vx = v_x
        self.vy = v_y
        self.r = rot
        self.rr = rr
        self.gg = gg
        self.bb = bb
        if x == 0:
            self.rad = 32
        else:
            self.rad = 8


    def draw(self, width, height, ppm):
        set_fill_color(self.rr, self.gg, self.bb)
        draw_circle((self.x) * ppm + width, (self.y) * ppm + height, self.rad)
        # print((self.x) * ppm + width, (self.y) * ppm + height, self.rad)


    def update_postion(self, timestep):
        self.x += 0 * timestep
        self.y += self.vy * timestep
        # self.y += 0 * timestep
        print(self.x, self.y, self.vy)
        print(self.vy)

    def update_velocity(self, ttimestep):
        # dx = -115
        # ax/a = dx/r
        # ax = a.dx/r
        # ax = a.(-115)/(self.x - self.)
        # ax = dxAm/r
        ax = 0.005
        ay = 0
        # self.vx += 1.98e20/self.mass * ttimestep
        self.vx += ax * ttimestep
        self.vy += ay * ttimestep

        v = sqrt(self.vx**2 + self.vy**2)
        return self.vx, self.vy