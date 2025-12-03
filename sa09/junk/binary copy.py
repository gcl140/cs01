

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
        if left > right:
            return None
        mid = (left + right) // 2
        if the_list[mid] == key:
            return mid
        elif the_list[mid] < key:
            return binary_search(the_list, key, mid + 1, right)
        else:
            return binary_search(the_list, key, left, mid - 1)