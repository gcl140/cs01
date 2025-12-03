# File: vertex.py
# Author: Gift Christian
# Date: November 15, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Vertex class used in the interactive story game.


class Vertex:
    def __init__(self, name, adjacent, text):   
        self.name = name                    # name of the vertex
        self.adjacent = adjacent            # list of names of adjacent vertices
        self.text = text                    # text description of the vertex

    def __str__(self):
        return f"Vertex(name={self.name}, adjacent={self.adjacent}, text={self.text})"