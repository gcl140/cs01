# File: counter-driver.py
# Author: Gift Christian
# Date: October 20, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Driver code to test the Counter class.

# Import the Counter class from the counter file
from counter import Counter

# Driver function to test two Counter instances as parameters
def driver(c1, c2):
    print("Initial Values:", c1, c2)                                # Print initial values of both counters
    i = 0                                                           # Loop to tick the first counter 12 times
    while i < 12:                                               
        print("1. After tick:", c1, "(wrapped=", c1.tick(),")")     # Tick c1 and print its value and whether it wrapped (True/False)
        i += 1
    print("1=========================================1")            # Just a separator for clarity

    i = 0
    while i < 12:
        print("2. After tick:", c2, "(wrapped=", c2.tick(),")")     # Tick c2 and print its value and whether it wrapped (True/False)
        i += 1
    print("2=========================================2")            # Just another separator for clarity


c1 = Counter(10, -1, 4)                                             # Create first Counter instance with limit 10, initial value -1, minimum digits 4
c2 = Counter(5, 6, 3)                                               # Create second Counter instance with limit 5, initial value 6, minimum digits 3

driver(c1, c2)                                                      # Call the driver function with both counters

print(c1.get_value())                                               # Print the final value of c1