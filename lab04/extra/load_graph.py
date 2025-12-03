# File: load_graph.py
# Author: Gift Christian
# Date: November 17, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the functions to load a graph from a text file and create a dictionary of Vertex instances.

from collections import deque
from vertex import Vertex                                       # Import the Vertex class

def parse_line(line):
    section_split = line.split(";")                             # Split the line into sections
    name = section_split[0].strip()                             # Get the vertex name 
    adjacent = section_split[1].strip().split(",")              # Get the list of adjacent vertices    
    x = int((section_split[2].strip()).split(",")[0].strip())   # Get the x-coordinate
    y = int((section_split[2].strip()).split(",")[1].strip())   # Get the y-coordinate
    vertices = []                                               # Initialize the list of adjacent vertices
    for a in adjacent:                                          # Iterate through adjacent vertices
        if a:
            vertices.append(a.strip())                          # Add the vertex to the list if it's not empty
    return name, vertices, x, y                                 # Return the parsed values


def create_vertex_dictionary(filename):
    graph_dict = {}                                     # Initialize an empty dictionary to hold the graph
    lines = open(filename, "r")                         # Open the file for reading
    for line in lines:                                  # 1st Iteration through each line in the file  
        if len(line.split(";")) == 3:                   # Ensure the line has the correct format
            name, adjacent, x, y = parse_line(line)     # Parse the line to get vertex details
            avertex = Vertex(name, [], x, y)            # Create a Vertex instance with an empty edges list
            graph_dict[name] = avertex                  # Add the vertex to the dictionary
    lines.close()
    
    lines = open(filename, "r")                                             # Re-open the file for the 2nd Iteration 
    for line in lines:
        if len(line.split(";")) == 3:
            name, adjacent, x, y = parse_line(line)
            current_vertex = graph_dict[name]                               # Get the current vertex from the dictionary
            for item in range(len(adjacent)):                               # Iterate through adjacent vertices
                current_vertex.edges.append(graph_dict[adjacent[item]])     # Append the actual Vertex instances to the edges list
    lines.close()                                                           # Close the file after reading
    return graph_dict                            # Return the completed graph dictionary    
