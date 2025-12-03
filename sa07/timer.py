
# File: counter.py
# Author: Gift Christian
# Date: October 20, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Timer class which represents a timer that can count down from a specified time.

# Import the Counter class from the counter file
from counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):    # Initialize the Timer with hours, minutes, and seconds
        self.hours = Counter(24, hours)             # Set the hours counter with a limit of 24
        self.minutes = Counter(60, minutes)         # Set the minutes counter with a limit of 60
        self.seconds = Counter(60, seconds)         # Set the seconds counter with a limit of 60

    def tick(self):
        if self.seconds.tick():                     # Decrement the seconds counter by 1, and if it wraps, decrement minutes
            if self.minutes.tick():                 # If seconds wrapped (returned True), decrement minutes counter by 1
                self.hours.tick()                   # If minutes wrapped (returned True), decrement hours counter by 1

    def is_zero(self):
        return self.hours.value == 0 and self.minutes.value == 0 and self.seconds.value == 0    # Check if the timer has reached zero for hours, minutes, and seconds
        
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)  # Return the string representation of the timer in HH:MM:SS format