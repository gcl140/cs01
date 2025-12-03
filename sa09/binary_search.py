# File: binary_search.py
# Author: Gift Christian
# Date: November 5, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Performs binary search on a sorted list of random numbers using recursion.

from random import randint

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.
def binary_search(the_list, key, left = None, right = None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1
    
    # YOU FILL IN THE REST OF THIS FUNCTION.
    
# ==============================================================================================
# START OF MY CODE
# ==============================================================================================

    if left > right or len(the_list) == 0:                          # If it occurs the list is empty or left index exceeds right index from the parameters passed (i.e illogical search space)
            return None                                             # Return None as key cannot be found
    mid = (left + right) // 2                                       # Calculate the middle index of the current search space
    if key == the_list[mid]:                                        # If the key is found at the middle index
            return mid                                              # Return the middle index
    if the_list[mid] < key:                                         # If the key is greater than the middle element
            return binary_search(the_list, key, mid + 1, right)     # Call the function again to recursively search the right half of the list
    else:                                                           # If the key is less than the middle element
            return binary_search(the_list, key, left, mid - 1)      # Call the function again to recursively search the left half of the list

# ==============================================================================================
# THE END
# ==============================================================================================



# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1
    
# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")
    
    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)    
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))
