# File: vertex.py
# Author: Gift Christian
# Date: November 17, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Vertex class used to represent vertices in a graph and its methods.

# Import necessary functions from cs1lib for drawing
from cs1lib import set_stroke_color, set_fill_color, draw_circle, draw_line, draw_text, set_stroke_width

RADIUS = 4
EDGE_WIDTH = 1

class Vertex:
    def __init__(self, name, edges, x, y):
        self.name = name
        self.edges = edges                                  # edges is expected to be a list of Vertex instances
        self.xlocation = x
        self.ylocation = y


    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)                             # Set the fill color for the vertex
        draw_circle(self.xlocation, self.ylocation, RADIUS)      # Draw the vertex as a circle


    def draw_edges(self, r, g, b, another_object):
        set_stroke_color(r, g, b)
        draw_line(self.xlocation, self.ylocation, another_object.xlocation, another_object.ylocation)   # Draw the edge between vertices


    def draw_all_edges(self, r, g, b):
        for i in range(len(self.edges)):                # Iterate through all edges
            self.draw_edges(r, g, b, self.edges[i])

    def is_on_vertex(self, point):
        x, y = point
        return self.xlocation - 5 <= x <= self.xlocation + 5 and self.ylocation - 5 <= y <= self.ylocation + 5
        

    def __str__(self):
        new_line = ""
        for i in range(len(self.edges)):
            new_line += self.edges[i].name + ", "
        name = self.name + "; " + "Location: " + str(self.xlocation) + ", " + str(self.ylocation) + "; Adjacent vertices: " + new_line      # Create string representation
        return name[:-2]        # Remove the last comma and space