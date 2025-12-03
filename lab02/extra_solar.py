# earthmoon.py
# Example for CS 1 Lab Assignment 2.
# db, thc; 2011-2016

from cs1lib import *
from extra_system import System
from extra_body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000                 # real seconds per simulation second
PIXELS_PER_METER = 180 / 2.3e11     # distance scale for the simulation
FRAMERATE = 30                      # frames per second
TIMESTEP = 1.0 / FRAMERATE          # time between drawing each frame


pressed = False
e_pressed, v_pressed, r_pressed, a_pressed = False, False, False, False

# Mouse event handlers to track mouse press state
def mouse_pressed(x, y):
    global pressed
    pressed = True                                     # Set pressed to True when mouse is pressed

def mouse_released(x, y):
    global pressed
    pressed = False                                    # Set pressed to False when mouse is released

def key_pressed(key):
    global e_pressed, v_pressed, r_pressed, a_pressed  # Take the global variables into the function for modification
    key_pressed = key                                  # Update key_pressed to the key that was pressed on the keyboard
    if key_pressed == "e":                             # If the 'e' key is pressed
        e_pressed = True                               # set e_pressed to True
    elif key_pressed == "v": 
        v_pressed = True
    elif key_pressed == "a":
        a_pressed = True 
    elif key_pressed == "r":
        r_pressed = True   

def key_released(key):
    global e_pressed, v_pressed, r_pressed, a_pressed   # Take the global variables into the function for modification
    key_pressed = key                                   # Update key_pressed to the key that was pressed on the keyboard    
    if key_pressed == "e":                              # If the 'e' key is pressed
        e_pressed = False                               # set e_pressed to False
    elif key_pressed == "v": 
        v_pressed = False
    elif key_pressed == "a":
        a_pressed = False
    elif key_pressed == "r":
        r_pressed = False


def main():
    set_clear_color(0, 0, 0)        # black background

    clear()

    # Draw the system in its current state.
    solarsystem.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solarsystem.update(TIMESTEP * TIME_SCALE)
    
    # Change colors based on key presses to simulate displaying different planets when keys are pressed
    if e_pressed:               # If 'e' key is pressed, assign mercury to red
        solars[1].rr = 1
        solars[1].gg = 0
        solars[1].bb = 0    
    elif v_pressed:             # If 'v' key is pressed, assign venus to purple
        solars[2].rr = 1
        solars[2].gg = 0
        solars[2].bb = 1
    elif r_pressed:             # If 'r' key is pressed, assign mars to blue
        solars[3].rr = 0
        solars[3].gg = 0
        solars[3].bb = 1
    elif a_pressed:            # If 'a' key is pressed, assign earth to white
        solars[4].rr = 1
        solars[4].gg = 1
        solars[4].bb = 1

    # Handle mouse press to increase body sizes, only works with non-image(PNG) bodies. i.e, with actual radiuses
    if pressed:
        for i in range(len(solarsystem.bodies)):
            solarsystem.bodies[i].rad *= 1.01       # Increase radius for easier clicking
            solarsystem.bodies[i].x *= 1.01         # adjust position if needed
            solarsystem.bodies[i].y *= 1.01         # adjust position if needed

    # Text instructions
    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_text("Press 'e' - mercury, 'v' - venus, 'a' - earth, 'r' - mars, ", 10, 375)
    draw_text("Long press mouse on screen to zoom ", 10, 390)
    disable_stroke()


# Create the bodies
# **************************************************************************
# Please uncomment below to test the images
# **************************************************************************

# sun = Body(1.98892e30, 0, 0, 0, 0, 10, 1, 1, 0, "sun.png")
# mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0, 0, "mercury.png")
# venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 1, 0, 1, "venus.png")
# earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, 0, 0, 1, "earth.png")
# mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 1, 1, "mars.png")

# **************************************************************************
# **************************************************************************


sun = Body(1.98892e30, 0, 0, 0, 0, 12, 1, 1, 0)            # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 0, 0, 0)  # red mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 0, 0, 0)   # orange venus
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, 0, 0, 0)   # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 6, 0, 0, 0)   # white mars

solars = [sun, mercury, venus, earth, mars]

# Initialize system
solarsystem = System(solars)


# Start the graphics window with mouse event handlers associated
start_graphics(main, 2400, framerate=FRAMERATE, mouse_press=mouse_pressed, mouse_release=mouse_released, key_press=key_pressed, key_release=key_released)
