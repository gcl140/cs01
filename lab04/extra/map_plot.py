# File: map_plot.py
# Author: Gift Christian
# Date: November 18, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the map plotting functionality for the Dartmouth graph.

# Import necessary functions from cs1lib, bfs, and the create_vertex_dictionary function
from cs1lib import start_graphics, load_image, draw_image, clear, set_stroke_color, draw_line
from load_graph import create_vertex_dictionary
from bfs import bfs

graph = create_vertex_dictionary("dartmouth_graph.txt") # Load the graph from the specified file

start_vertex = None     # Initialize start vertex
end_vertex = None       # Initialize end vertex
current_hover = None    # Initialize current hover vertex

def mouse_press(x, y):
    return x, y

def mouse_release(x, y):                    # Set the start vertex on mouse release
    global start_vertex
    for key in graph:                       # Iterate through all vertices in the graph
        vatex = graph[key]
        if vatex.is_on_vertex((x, y)):      # Check if the mouse release position is on the vertex
            start_vertex = vatex            # Set it as the start vertex
            break                           # Exit the loop once the start vertex is found

def mouse_move(x, y):
    global current_hover, end_vertex
    hover_candidate = None                  # Initialize hover candidate
    for key in graph:                       # Iterate through all vertices in the graph
        vatex = graph[key]                  # Get the vertex object
        if vatex.is_on_vertex((x, y)):      # Check if the mouse position is on the vertex
            hover_candidate = vatex         # Set it as the hover candidate
            break                           # Exit the loop once the hover candidate is found
    current_hover = hover_candidate         # Update the current hover vertex


    if start_vertex != None and current_hover != None and current_hover != start_vertex:    # Only set goal if start already picked AND hovering something else
        end_vertex = current_hover                                          # Set the end vertex
    else:
        end_vertex = None                                                   # no valid goal


def main():
    clear()
    background = load_image("dartmouth_map.png")        # Load the background map image
    draw_image(background, 0, 0)

    for key in graph:
        vatex = graph[key]                          # iterate through all vertices in the graph to get the vertex object
        vatex.draw_all_edges(0, 0, 1)               # draw all edges in blue
        vatex.draw_vertex(0, 0, 1)                  # draw each vertex in blue

    
    if current_hover:                               # red highlight for hover     
        current_hover.draw_vertex(1, 0, 0)          

    
    if start_vertex:                                # if start picked, draw it yellow
        start_vertex.draw_vertex(1, 1, 0)

    if start_vertex != None and end_vertex != None: # if valid goal selected, compute BFS path
        path = bfs(start_vertex, end_vertex)        # get the path from bfs
        if path != None:                            # if a path was found    
            r = g = b = 0
            for vatex in path:                      # color vertices green   
                r += 0.3
                g += 0.25
                b += 0.1
                vatex.draw_vertex(r, g, b)          # draw vertex in green


            for i in range(len(path) - 1):         # draw edges in green
                v1 = path[i]                       # get the first vertex
                v2 = path[i + 1]                   # get the second vertex
                r = g = b = 0
                r += 0.3
                g += 0.25
                b += 0.1
                set_stroke_color(0, 1, 0)          
                draw_line(v1.xlocation, v1.ylocation, v2.xlocation, v2.ylocation)   # draw line between the two vertices

# Start the graphics window with specified dimensions and mouse event handlers
start_graphics(main, width=1012, height=811, mouse_press=mouse_press, mouse_release=mouse_release, mouse_move=mouse_move)