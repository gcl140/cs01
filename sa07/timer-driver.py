# File: timer-driver.py
# Author: Gift Christian
# Date: October 20, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Driver code to test the Timer class.

# Import the Timer class from the timer file
from timer import Timer

c2 = Timer(1, 30, 0)    # Create a Timer instance set to 1 hour, 30 minutes, and 0 seconds
print(c2)               # Print the initial state of the timer

i = 0
while i < 5400:         # Loop to tick the timer 5400 times (1.5 hours)
    c2.tick()           # Decrement the timer by one second using the tick method
    print(c2)           # Print the current state of the timer after each tick
    i+=1            

print(c2.is_zero())     # Check if the timer has reached zero and print the result (True/False)