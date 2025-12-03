# File: system.py
# Author: Gift Christian
# Date: October 31, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A class representing a celestial body.

# Import necessary modules from cs1lib
from cs1lib import set_fill_color, draw_circle, draw_image, load_image


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b, img_path=None):   # Initialize body with mass, position, velocity, visual properties, and optional image
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rad = pixel_radius
        self.rr = r
        self.gg = g
        self.bb = b
        if img_path != None:                                                        # Load image if provided    
            self.img = load_image(img_path)
        else:
            self.img = None


    def draw(self, width, height, ppm):
        if self.img != None:                                                        # Draw image if available
            draw_image(self.img, self.x * ppm + width, self.y * ppm + height)       # Draw the image at the scaled position
        else:                                                                       # Otherwise, draw a colored circle    
            set_fill_color(self.rr, self.gg, self.bb)                               # Set color for the body
            draw_circle(self.x * ppm + width, self.y * ppm + height, self.rad)      # Draw the body as a circle at the scaled position


    def update_postion(self, ttimestep):                                            # Update position based on velocity and time step
        self.x += self.vx * ttimestep
        self.y += self.vy * ttimestep


    def update_velocity(self, ax, ay, ttimestep):                                   # Update velocity (vx, vy) based on acceleration and time step
        self.vx += ax * ttimestep
        self.vy += ay * ttimestep


    def __str__(self):
        return "Body(mass=" + str(self.mass) + ", position=(" + str(self.x) + ", " + str(self.y) + "))"     # String representation of the Body object