# File: counter.py
# Author: Gift Christian
# Date: October 20, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Counter class which represents a counter that can count down from a specified limit.


class Counter:
    def __init__(self, limit, initial=0, min_digits = 2):       # Initialize the Counter with a limit, initial value, and minimum digits
        self.limit = limit                                      # Set the limit for the counter        
        self.min_digits = min_digits                            # Set the minimum digits for the counter
        if 0 <= initial <= limit - 1:                           # Check if the initial value is within valid range of 0 to limit-1
            self.value = initial                                # Set the initial value
        else:
            print("Error: Initial Value is out of range")       # Print error message if initial value is out of range
            self.value = limit - 1                              # Then set value to maximum valid value (limit - 1)


    def tick(self):                                             # Decrement the counter by 1 Function
        self.value -= 1                                         # Decrease the value by 1
        if self.value < 0:                                      # Check if the value has gone below 0
            self.value = self.limit - 1                         # Wrap around to the maximum value
            return True                                         # Indicate that wrapping occurred
        return False                                            # No wrapping occurred


    def get_value(self):                                        # Get the current value of the counter Function
        return int(self.value)                                  # Return the current value of the counter as an integer


    def __str__(self):                                          # String representation of the counter class
        value_str = str(self.value)                             # Convert the current value to a string
        if len(value_str) < self.min_digits:                    # Check if padding with leading zeros is needed
            zeros_needed = self.min_digits - len(value_str)     # Calculate number of leading zeros needed
            return zeros_needed * "0" + value_str               # Return the value string with leading zeros
        else:
            return value_str                                    # Return the value string as is if no padding is needed