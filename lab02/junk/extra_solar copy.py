# earthmoon.py
# Example for CS 1 Lab Assignment 2.
# db, thc; 2011-2016

from cs1lib import *
from extra_system import System
from extra_body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 1000000               # real seconds per simulation second
                                    # PIXELS_PER_METER = 3 / 1e10  # distance scale for the simulation
PIXELS_PER_METER = 180 / 2.3e11 
FRAMERATE = 30                      # frames per second
TIMESTEP = 1.0 / FRAMERATE          # time between drawing each frame
pressed = False

# Mouse event handlers to track mouse press state
def mouse_pressed(x, y):
    global pressed
    pressed = True

def mouse_released(x, y):
    global pressed
    pressed = False

count = 0
def main():
    global count

    set_clear_color(0, 0, 0)        # black background

    clear()

    # Draw the system in its current state.
    solarsystem.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solarsystem.update(TIMESTEP * TIME_SCALE)
    
    # Handle mouse press to increase body sizes, only works with non-image(PNG) bodies. i.e, with actual radiuses
    if pressed:
        count += 1
        if count == 1:

        for i in range(len(solarsystem.bodies)):
            solarsystem.bodies[i].rad *= 1.01       # Increase radius for easier clicking
            solarsystem.bodies[i].x *= 1.01         # adjust position if needed
            solarsystem.bodies[i].y *= 1.01         # adjust position if needed


# Create the bodies
sun = Body(1.98892e30, 0, 0, 0, 0, 10, 1, 1, 0, "sun.png")
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0, 0, "mercury.png")
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 1, 0, 1, "venus.png")       
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, 0, 0, 1, "earth.png")
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 1, 1, "mars.png")        

# **************************************************************************
# Please uncomment below to test the zooming when mouse is pressed without images
# **************************************************************************


# sun = Body(1.98892e30, 0, 0, 0, 0, 10, 1, 1, 0)            # yellow sun
# mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0, 0)  # red mercury
# venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 1, 0, 1)   # orange venus
# earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, 0, 0, 1)   # blue earth
# mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 1, 1)   # white mars

# **************************************************************************
# **************************************************************************

solars = [sun]
# Initialize system
solarsystem = System([sun, mercury, venus, earth, mars])
solarsystem = System([sun, mercury, venus, earth, mars])

# Start the graphics window with mouse event handlers associated
start_graphics(main, 2400, framerate=FRAMERATE, mouse_press=mouse_pressed, mouse_release=mouse_released)
