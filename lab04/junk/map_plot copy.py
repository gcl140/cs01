# File: map_plot.py
# Author: Gift Christian
# Date: November 17, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the code to plot the graph on a map using cs1lib.

# Import necessary functions from cs1lib and the create_vertex_dictionary function
from cs1lib import start_graphics, load_image, draw_image, clear
from load_graph import create_vertex_dictionary
from bfs import bfs

# Load the graph from the specified file
graph = create_vertex_dictionary("dartmouth_graph.txt")
start_vertex = graph["Sudikoff"]
end_vertex = graph["1953 Commons"]

print(bfs(start_vertex, end_vertex))
start_point = None, None
end_point = None, None
mvt = clickedd = False
def pressed(px, py):
    global clickedd
    clickedd = True
    return px, py

def moved(mx, my):
    global end_point, mvt
    end_point = mx, my
    mvt = True
    print(end_point)
    return mx, my

def released(rx, ry):
    global start_point
    start_point = rx, ry
    return rx, ry

def main():
    clear()
    img = load_image("dartmouth_map.png")       # Load the background map image
    draw_image(img, 0, 0)                       # Draw the map image at the origin (0,0)
    for vertex in graph:                        # Iterate through all vertices in the graph
        graph[vertex].draw_vertex(0, 0, 1)      # Draw each vertex in blue
        graph[vertex].draw_all_edges(0, 0, 1)   # Draw all edges in blue
        if mvt:
            # graph[vertex].is_on_vertex(end_point)
            print(graph[vertex].is_on_vertex(end_point))
        if clickedd:
            graph[vertex].is_on_vertex(start_point)
        # if released

start_graphics(main, width=1012, height=811, mouse_press=pressed, mouse_release=released, mouse_move=moved)    # Start the graphics window with specified dimensions



