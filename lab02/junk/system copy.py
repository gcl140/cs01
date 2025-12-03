# File: system.py
# Author: Gift Christian
# Date: October 31, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A class representing a system of celestial bodies.
G = 6.67430e-11  # gravitational constant
Mmoon = 7.3477e22  # mass of the moon
class System:
    def __init__(self, bodies):         # bodies is a list of Body objects
        self.bodies = bodies

    def draw(self, width, height, ppm):                             # ppm is pixels per meter
        for i in range(len(self.bodies)):                           # Draw each body
            self.bodies[i].draw(width, height, ppm)                 # Draw the i-th body from the list

    def compute_acceleration(self, body_i, body_j):
        dx = body_j.x - body_i.x
        dy = body_j.y - body_i.y
        r = (dx**2 + dy**2)**0.5
        a = G * body_j.mass / r**2
        ax = dx * a/r
        ay = dy * a/r
        return ax, ay
    
    def update(self, ttimestep):
        no_bodies = len(self.bodies)
                    # print(ax_total, ay_total, a, (ax_total**2 + ay_total**2)**0.5)
                    # print("pos: ", dx, dy, r)

            self.bodies[i].update_velocity(ax_total, ay_total, ttimestep)
            self.bodies[i].update_postion(ttimestep)

    def __str__(self):                                              # String representation of the System object
        body_strings = []
        for body in self.bodies:
            body_strings.append(str(body))
        return "System with bodies: " + str(body_strings)