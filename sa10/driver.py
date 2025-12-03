# File: driver.py
# Author: Gift Christian
# Date: November 15, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the driver code for the interactive story game.

# Import the Vertex class from vertex
from vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text

# Improved load_story function to handle multi-line descriptions
def load_story(filename):
    vertex_dict = {}
    
    with open(filename, "r") as file:                           # Use 'with' to ensure file is closed properly
        lines = file.readlines()                                # Read all lines at once
    
    i = 0                                                       # Line index
    while i < len(lines):                                       # Loop until all lines are processed
        name = lines[i].strip()                                 # Read vertex name
        i += 1
        
        if name == "":                                          # Skip empty lines using the continue statement
            continue  
        
        
        description_lines = []                                  # # Read description lines until we hit a blank line
        while i < len(lines) and lines[i].strip() != "":        # While not a blank line that exists
            description_lines.append(lines[i].strip())          # Add line to description_lines list
            i += 1
        
        
        description = ""                                        # Manually build description string  
        for j in range(len(description_lines)):                 # Loop through description_lines list
            description += description_lines[j]                 # Add each line to description string
            if j < len(description_lines) - 1:                  # Don't add newline after last line
                description += "\n"

        i += 1                                                  # Skip the blank line

        
        if i < len(lines):                                      # Read adjacency line stripped of whitespace if it exists 
            adj_line = lines[i].strip()
            i += 1
            adjacent = []                                       # Process adjacency line
            parts = adj_line.split(",")                         # Split by commas
            for part in parts:                                  # Loop through parts
                cleaned = part.strip()                          # Strip whitespace
                if cleaned != "":                               # Avoid adding empty strings
                    adjacent.append(cleaned)                    
        
        vertex_dict[name] = Vertex(name, adjacent, description) # Create Vertex and add to dictionary
    
    return vertex_dict


# Interactive play function
def play(story_dict):
    current = story_dict["START"]                           # Start at the "START" vertex
    while True:                                             # Main game loop   
        print(current.text)                                 # Print current vertex text
        if not current.adjacent:                            # If no adjacent vertices, end the game
            print("THE END")
            break                                           # Exit loop

        for i in range(len(current.adjacent)):              # List options for adjacent vertices
            v = current.adjacent[i]                         # Get adjacent vertex name
            option = chr(ord('a') + i)                      # Convert index to letter
            print(f"{option}) go to {v}")                   # Print option
            # print(option," go to ", v)                   # Print option

        choice = input("Choose: ").strip().lower()          # Get user choice
        
        if not choice:                                      # If no choice, prompt again
            continue    
        index = ord(choice) - ord('a')                     # Convert choice letter back to index
        if index < 0 or index >= len(current.adjacent):    # Validate choice
            print("Invalid choice.")
            continue
            # return "invalid choice"
        next_name = current.adjacent[index]                # Get next vertex name
        current = story_dict[next_name]                    # Move to next vertex


story_dict = load_story("story.txt")                       # Load the story from file
play(story_dict)                                           # Start the game
