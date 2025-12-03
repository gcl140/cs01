# File: system.py
# Author: Gift Christian
# Date: October 31, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A class representing a celestial body.

# Import necessary modules from cs1lib
from cs1lib import set_fill_color, draw_circle
class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b): # m: mass, x,y: position, v_x,v_y: velocity, rot: rotation speed, rr,gg,bb: color
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rad = pixel_radius
        self.rr = r
        self.gg = g
        self.bb = b

    def draw(self, width, height, ppm):
        set_fill_color(self.rr, self.gg, self.bb)                           # Set color based on rr, gg, bb values
        draw_circle(self.x * ppm + width, self.y * ppm + height, self.rad)  # Draw circle at scaled position with radius


    def update_postion(self, ttimestep):                                    # Update position based on velocity and time step
        self.x += self.vx * ttimestep
        self.y += self.vy * ttimestep


    def update_velocity(self, ax, ay, ttimestep):                           # Update velocity (vx, vy) based on acceleration and time step
        self.vx += ax * ttimestep
        self.vy += ay * ttimestep


    def __str__(self):
        return "Body(mass=" + str(self.mass) + ", position=(" + str(self.x) + ", " + str(self.y) + "))"     # String representation of the Body object