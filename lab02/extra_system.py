# File: system.py
# Author: Gift Christian
# Date: October 31, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A class representing a system of celestial bodies.

G = 6.67430e-11                                                     # gravitational constant
class System:
    def __init__(self, bodies):                                     # bodies is a list of Body objects
        self.bodies = bodies

    def draw(self, width, height, ppm):                             # ppm is pixels per meter
        for i in range(len(self.bodies)):                           # Draw each body
            self.bodies[i].draw(width, height, ppm)

    def compute_acceleration(self, body_i, body_j):                 # Compute acceleration on body_i due to body_j
        dx = body_j.x - body_i.x                                    # Distance x components
        dy = body_j.y - body_i.y                                    # Distance y components
        r = (dx**2 + dy**2)**0.5                                    # Distance between bodies
        a = G * body_j.mass / r**2                                  # Acceleration magnitude
        ax = dx * a/r                                               # Acceleration x components
        ay = dy * a/r                                               # Acceleration y components
        return ax, ay                                               # Return a tuple of acceleration components

    def update(self, ttimestep):
        for i in range(len(self.bodies)):                                                   # Update each body
            ax_total = 0
            ay_total = 0
            for j in range(len(self.bodies)):                                               # Compute net acceleration on body i
                if i != j:                                                                  # Skip self-interaction
                    ax, ay = self.compute_acceleration(self.bodies[i], self.bodies[j])      # Get acceleration due to body j
                    ax_total += ax                                                          # Sum x components
                    ay_total += ay                                                          # Sum y components
            self.bodies[i].update_velocity(ax_total, ay_total, ttimestep)                   # Update velocity based on net acceleration
            self.bodies[i].update_postion(ttimestep)                                        # Update position based on new velocity

    def __str__(self):                                                                      # String representation of the System object
        body_strings = []
        for body in self.bodies:
            body_strings.append(str(body))
        return "System with bodies: " + str(body_strings)